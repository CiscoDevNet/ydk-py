#  ----------------------------------------------------------------
# Copyright 2016 Cisco Systems
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------

""" _provider_plugin.py

   Service Providers module. Current implementation supports the
   NetconfServiceProvider which uses ncclient (a Netconf client library)
   to provide CRUD services.

"""
from lxml import etree

from ydk._core._dm_meta_info import REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS
from ydk.errors import YPYServiceProviderError, YPYErrorCode
from ydk.types import YList, YListItem, YLeafList, Empty

from ._decoder import XmlDecoder
from ._encoder import XmlEncoder
from ._ydk_types import _SessionTransportMode


from ncclient import manager
from ncclient.operations import RPC, RPCReply

import abc
import logging
import importlib
from ._importer import _yang_ns

try:
    import ydk_client
except:
    pass


class YdkClient(object):
    def __init__(self, username, password, host, port):
        try:
            self.client = ydk_client.NetconfClient(username, password, host, port, 0)
        except Exception as e:
            if isinstance(e, ImportError):
                raise YPYServiceProviderError(error_msg='Native YDK client is not installed. Try installing all dependencies in README and re-installing ydk: ' + str(e))
            else:
                raise YPYServiceProviderError(error_msg=str(type(e)) + '. Could not connect to client: ' + str(e))

    def connect(self):
        self.client.connect()

    def execute_payload(self, payload):
        reply = ''
        try:
            reply = self.client.execute_payload(payload)
            return reply
        except Exception as e:
            raise YPYServiceProviderError(error_msg='Could not execute RPC: ' + str(e))

    def get_capabilities(self):
        caps = []
        caps.extend(self.client.get_capabilities())
        return caps

    def disconnect(self):
        self.client.close()


class _SPPlugin(object):
    def __init__(self, service_protocol_name):
        self.service_protocol_name = service_protocol_name

    @abc.abstractmethod
    def encode(self, entity, optype):
        pass

    @abc.abstractmethod
    def decode(self, payload):
        pass

    @abc.abstractmethod
    def execute_operation(self, session, payload, options=None):
        pass


class _ClientSPPlugin(_SPPlugin):

    def __init__(self, timeout, use_native_client):
        self.head = None
        self._nc_manager = None
        self.use_native_client = use_native_client
        if use_native_client:
            self.ydk_client = None
        else:
            self._nc_manager = None
        self.netconf_sp_logger = logging.getLogger(__name__)
        self.timeout = timeout

    def encode(self, entity, operation, only_config):
        root = self._create_root()
        if operation_is_edit(operation):
            root = self._encode_edit_request(root, entity, operation)
        else:
            root = self._encode_read_request(root, entity, operation, only_config)
        payload = etree.tostring(self.head, method='xml', pretty_print='True', encoding='utf-8').decode('utf-8')
        return payload

    def encode_rpc(self, rpc):
        if not self._is_rpc(rpc):
            self._raise_non_rpc_error()
        root = self._create_root()
        self._encode_rpc_request(root, rpc)
        payload = etree.tostring(self.head, method='xml', pretty_print='True', encoding='utf-8').decode('utf-8')
        return payload

    def decode(self, payload, read_filter):
        if read_filter is None:
            return XmlDecoder().decode(payload)
        if self._is_rpc_reply(read_filter):
            if 'ok' in payload or not self._is_rpc_reply_with_output_data(read_filter):
                return None
            XmlDecoder()._bind_to_object(payload, read_filter.output, {})
            return read_filter.output

        # In order to figure out which fields are the
        # ones we are interested find the field list
        entity = self._create_top_level_entity_from_read_filter(read_filter)
        XmlDecoder._bind_to_object(payload, entity, self._get_capabilities())
        # drill down to figure out the field access expression
        # that matches the entity or entities to be returned
        # not the argument passed in as a filter might have
        # incomplete key paths, in which case what is returned
        # will be the entity whose common path can be determined

        current = entity
        current_entity = read_filter
        current_meta = current_entity.i_meta

        yang_nodes = []

        while hasattr(current_meta, 'parent'):
            yang_nodes.append(current_meta.yang_name)
            current_meta = current_meta.parent
        if current_meta:
            yang_nodes.append(current_meta.yang_name)

        yang_nodes = list(reversed(yang_nodes))
        yang_nodes = yang_nodes[1:]

        for yang_node_name in yang_nodes:

            found = False
            for member in current._meta_info().meta_info_class_members:
                if member.name == yang_node_name:
                    found = True
                    current = getattr(current, member.presentation_name)
                    if current is None:
                        return None
                    if isinstance(current, YList):
                        if len(current) == 0:
                            return None
                        if len(current) > 0:
                            return current

                    break

            if not found:
                self.netconf_sp_logger.error('Error determing what needs to be returned')
                raise YPYServiceProviderError(error_msg='Error determining what needs to be returned')

        return current

    def _create_top_level_entity_from_read_filter(self, read_filter):
        non_list_filter = read_filter

        while isinstance(non_list_filter, YList):
            non_list_filter = non_list_filter.parent

        if non_list_filter is None:
            self.netconf_sp_logger.error('Cannot determine hierarchy for entity. Please set the parent reference')
            raise YPYServiceProviderError(error_msg='Cannot determine hierarchy for entity. Please set the parent reference')

        top_entity_meta_info = non_list_filter._meta_info()

        while hasattr(top_entity_meta_info, 'parent') and top_entity_meta_info.parent is not None:
            # need to find the member that has
            top_entity_meta_info = top_entity_meta_info.parent

        module = importlib.import_module(top_entity_meta_info.pmodule_name)
        entity = getattr(module, top_entity_meta_info.name)()
        return entity

    def _get_capabilities(self):
        if self.use_native_client:
            return self.ydk_client.get_capabilities()
        else:
            return self._nc_manager.server_capabilities

    def execute_operation(self, payload, operation):
        '''
            Raises exception on error, else returns result
        '''
        reply_str = "FAILED!"
        if len(payload) == 0:
            return reply_str

        if self.use_native_client:
            assert self.ydk_client is not None
            reply = self.ydk_client.execute_payload(payload)
            self.netconf_sp_logger.debug('\n%s', _get_pretty(reply.xml))
            return self._handle_rpc_reply(operation, payload, reply)
        else:
            service_provider_rpc = self._create_rpc_instance(self.timeout)
            payload = payload.replace("101", service_provider_rpc._id, 1)
            self.netconf_sp_logger.debug('\n%s', payload)
            reply = service_provider_rpc._request(payload)
            self.netconf_sp_logger.debug('\n%s', _get_pretty(reply.xml))
            return self._handle_rpc_reply(operation, payload, reply.xml)

    def _create_rpc_instance(self, timeout):
        assert self._nc_manager is not None
        class _SP_RPC(RPC):
            def _wrap(self, subele):
                return subele

        class _SP_REPLY_CLS(RPCReply):
            def parse(self):
                self._parsed = True
                return True

        RPC.REPLY_CLS = _SP_REPLY_CLS
        return _SP_RPC(self._nc_manager._session, self._nc_manager._device_handler, timeout=timeout)

    def _handle_rpc_reply(self, optype, payload, reply_str):
        if 'ok' in reply_str:
            self._handle_rpc_ok(optype, payload, reply_str)
            return reply_str
        err, pathlist = check_errors(reply_str)
        if err:
            self._handle_rpc_error(payload, reply_str, pathlist)

        root = etree.fromstring(reply_str.encode('utf-8'))
        payload = etree.tostring(root, method='xml', pretty_print='True', encoding='utf-8').decode('utf-8')
        return payload

    def _handle_rpc_ok(self, optype, payload, reply_str):
#         assert self._nc_manager is not None
        if operation_is_edit(optype) and confirmed_commit_supported(self._get_capabilities()):
            self._handle_commit(payload, reply_str)

    def _handle_rpc_error(self, payload, reply_str, pathlist):
        self.netconf_sp_logger.error('\n%s\n%s' , payload, reply_str)
        raise YPYServiceProviderError(error_code=YPYErrorCode.SERVER_REJ, error_msg=reply_str)

    def _handle_commit(self, payload, reply_str):
        commit = '<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">\n  <commit/>\n</rpc>\n'
        self.netconf_sp_logger.debug('\n%s', _get_pretty(commit))
        if self.use_native_client:
            assert self.ydk_client is not None
            rep = self.ydk_client.execute_payload(commit)
        else:
            assert self._nc_manager is not None
            rep = self._nc_manager.commit()
            rep = rep.xml

        if 'ok' not in rep:
            self.netconf_sp_logger.error('\n%s\n%s\ncommit-reply\n%s', payload, reply_str, rep)
            raise YPYServiceProviderError(error_code=YPYErrorCode.SERVER_COMMIT_ERR, error_msg=rep)
        else:
            self.netconf_sp_logger.debug('\n%s', _get_pretty(reply_str))

    def connect(self, session_config):
        assert session_config.transportMode == _SessionTransportMode.SSH
        if self.use_native_client:
            self.ydk_client = YdkClient(
                username=session_config.username,
                password=session_config.password,
                host=session_config.hostname,
                port=session_config.port)
            self.ydk_client.connect()
            return self.ydk_client
        else:
            self._nc_manager = manager.connect(
                host=session_config.hostname,
                port=session_config.port,
                username=session_config.username,
                password=session_config.password,
                look_for_keys=False,
                allow_agent=False,
                hostkey_verify=False)
            return self._nc_manager

    def disconnect(self):
        if self.use_native_client:
            assert self.ydk_client is not None
            self.ydk_client.disconnect()
        else:
            assert self._nc_manager is not None
            self._nc_manager.close_session()

    def _get_target_datastore(self):
#         assert self._nc_manager is not None
        target_ds = 'candidate'
        if not confirmed_commit_supported(self._get_capabilities()):
            target_ds = 'running'
        return target_ds

    def _create_root(self):
        NSMAP = {'xmlns': 'urn:ietf:params:xml:ns:netconf:base:1.0'}
        self.head = etree.Element('rpc', NSMAP)
        if not self.use_native_client:
            self.head.set('message-id', '101')
        return self.head

    def _match_key(self, root, entity):
        if type(entity) == YListItem:
            return self._match_leaflist_key(root, entity)
        else:
            return self._match_list_key(root, entity)

    def _match_leaflist_key(self, root, entity):
        target_root = None
        chs = root.getchildren()
        # leaflist of enum
        if hasattr(entity, 'i_meta') and entity.i_meta.mtype == REFERENCE_ENUM_CLASS:
            key_value = getattr(entity, entity.presentation_name)
            key_value.name.replace('_', '-').lower()
        value = str(entity.item)
        for ch in chs:
            if ch.tag == entity.name and ch.text == value:
                target_root = ch
                return target_root
        return target_root

    def _match_list_key(self, root, entity):
        target_root = None
        chs = root.getchildren()
        keys = entity.i_meta.key_members()
        for key in keys:
            key_value = getattr(entity, key.presentation_name)
            if key.mtype == REFERENCE_ENUM_CLASS:
                key_value = key_value.name.replace('_', '-').lower()
            elif key.mtype == REFERENCE_IDENTITY_CLASS:
                identity_inst = getattr(entity, key.presentation_name)
                if _yang_ns._namespaces[key.module_name] == _yang_ns._namespaces[identity_inst._meta_info().module_name]:
                    key_value = identity_inst._meta_info().yang_name
                else:
                    key_value = 'idx:%s' % identity_inst._meta_info().yang_name
            key_value = str(key_value)
            for ch in chs:
                if key.name == ch.tag and key_value == ch.text:
                    target_root = root
                    return target_root
        return target_root


    def _attach_tag(self, root, entity, optype):
        if type(entity) == YList or type(entity) == YLeafList:
            self._attach_list_tag(root, entity, optype)
        elif type(entity) == YListItem:
            # attach tag to this particular leaflist element
            chs = root.getchildren()
            for ch in chs:
                # match parent
                if entity.parent.i_meta.yang_name == ch.tag:
                    ch.clear()
                    elem = etree.SubElement(ch, entity.name)
                    xc = 'urn:ietf:params:xml:ns:netconf:base:1.0'
                    elem.set('{' + xc + '}operation', 'delete')
                    elem.text = str(entity.item)

        else:
            chs = root.getchildren()
            for ch in chs:
                if entity.i_meta.yang_name == ch.tag:
                    elem = ch
                    xc = 'urn:ietf:params:xml:ns:netconf:base:1.0'
                    elem.set('{' + xc + '}operation', 'delete')

    def _attach_list_tag(self, root, entity, optype):
        if type(entity) == YList or type(entity) == YLeafList:
            for item in entity:
                self._attach_list_tag(root, item, optype)
        else:
            chs = root.getchildren()
            for ch in chs:
                elem = self._match_key(ch, entity)
                if elem is not None:
                    xc = 'urn:ietf:params:xml:ns:netconf:base:1.0'
                    elem.set('{' + xc + '}operation', 'delete')


    def _encode_epilogue(self, entity, root, optype):
        if type(entity) == YLeafList or type(entity) == YListItem:
            # parent_meta_tuple_list is not created for leaflist's parent
            entity = entity.parent
            XmlEncoder().encode_to_xml(entity, root, optype)
        elif type(entity) == YList:
            for item in entity:
                self._encode_epilogue(item, root, optype)
        else:
            XmlEncoder().encode_to_xml(entity, root, optype)

    def _check_read_only_edit_error(self, entity):
        if type(entity) == YLeafList:
            pass
        elif type(entity) == YListItem:
            pass
        elif isinstance(entity, YList):
            for item in entity:
                self._check_read_only_edit_error(item)
        else:
            if not entity.is_config():
                self._raise_read_only_edit_error()

    def _encode_edit_request(self, root, entity, optype):
        self._check_read_only_edit_error(entity)

        root = self._create_element(root,
                                    'edit-config',
                                    'target',
                                    self._get_target_datastore(),
                                    'config',
                                    optype)

        root = self._create_preamble(entity, root)

        self._encode_epilogue(entity, root, optype)

        if not operation_is_create_or_update(optype):
            self._attach_tag(root, entity, optype)

        return root

    def _encode_read_request(self, root, entity, optype, only_config):
        get_str = 'get'
        source = None
        source_ds = None
        if only_config:
            get_str = 'get-config'
            source = 'source'
            source_ds = 'running'

        root = self._create_element(root,
                                    get_str,
                                    source,
                                    source_ds,
                                    'filter',
                                    optype)
        root.set('type', "subtree")
        root = self._create_preamble(entity, root)
        XmlEncoder().encode_filter(entity, root, optype)
        return root

    def _encode_rpc_request(self, root, rpc):
        XmlEncoder().encode_to_xml(rpc, root, '')
        return root

    def _create_element(self, root, oper, target, candidate, config_or_filter, optype):
        root = etree.SubElement(root, oper)
        if target is not None:
            target = etree.SubElement(root, target)
        if candidate is not None:
            if target is not None:
                candidate = etree.SubElement(target, candidate)
            else:
                candidate = etree.SubElement(root, candidate)
        if operation_is_edit(optype):
            NSMAP = {"xc": "urn:ietf:params:xml:ns:netconf:base:1.0"}
            root = etree.SubElement(root, 'config', nsmap=NSMAP)
        elif optype == 'EVENT_SUBSCRIBE':
            root = etree.SubElement(candidate, config_or_filter)
            root.set('xmlns', "urn:ietf:params:xml:ns:netconf:base:1.0")
        elif optype == 'READ':
            root = etree.SubElement(root, config_or_filter)
            root.set('type', "subtree")
        else:
            NSMAP = {"xc", "urn:ietf:params:xml:ns:netconf:base:1.0"}
            root = etree.SubElement(root, config_or_filter, nsmap=NSMAP)
        return root

    def _create_preamble(self, entity, root):
        if type(entity) == YLeafList or type(entity) == YListItem:
            # escape current level
            entity = entity.parent
        elif type(entity) == YList:
            entity = entity[0]
        parent_meta_tuple_list = self._get_parent_tuple_list(entity, entity._meta_info())
        parent_ns = self._get_parent_namespace(root)
        return self._encode_parents_of_root(root, parent_meta_tuple_list, parent_ns)

    def _encode_parents_of_root(self, root, parent_meta_tuple_list, parent_ns):
        for meta_info, parent in reversed(parent_meta_tuple_list):
            root = etree.SubElement(root,
                                   meta_info.yang_name)
            ns = meta_info.namespace
            if ns is not None and parent_ns != ns:
                root.set('xmlns', ns)
                parent_ns = ns
            root = self._encode_items(root, parent, meta_info)
        return root

    def _entity_is_abstract(self, entity, meta_info):
        return meta_info.is_abstract and entity.parent is None

    def _entity_has_no_keys(self, entity, meta_info):
        return entity is None and len(meta_info.key_members()) > 0

    def _is_rpc(self, rpc):
        return hasattr(rpc, 'is_rpc') and rpc.is_rpc

    def _raise_parent_hierarchy_error(self):
        self.netconf_sp_logger.error(YPYErrorCode.INVALID_HIERARCHY_PARENT)
        raise YPYServiceProviderError(error_code=YPYErrorCode.INVALID_HIERARCHY_PARENT)

    def _raise_key_missing_error(self):
        self.netconf_sp_logger.error(YPYErrorCode.INVALID_HIERARCHY_KEY)
        raise YPYServiceProviderError(error_code=YPYErrorCode.INVALID_HIERARCHY_KEY)

    def _raise_read_only_edit_error(self):
        self.netconf_sp_logger.error(YPYErrorCode.INVALID_MODIFY)
        raise YPYServiceProviderError(error_code=YPYErrorCode.INVALID_MODIFY)

    def _raise_non_rpc_error(self):
        self.netconf_sp_logger.error(YPYErrorCode.INVALID_RPC)
        raise YPYServiceProviderError(error_code=YPYErrorCode.INVALID_RPC)

    def _encode_items(self, root, entity, meta_info):
        if entity is None:
            return root
        for key in meta_info.key_members():
            self._encode_key(root, entity, meta_info, key)
        for member in meta_info.meta_info_class_members:
            value = getattr(entity, member.presentation_name)
            if isinstance(value, Empty) and member.ptype == 'Empty':
                self._encode_empty(root, entity, member)
        return root

    def _encode_empty(self, root, entity, member):
        entity_ns = entity.i_meta.namespaces
        empty_ns = _yang_ns._namespaces[member.module_name]
        NSMAP = {}
        if entity_ns is not None and entity_ns != empty_ns:
            NSMAP[None] = empty_ns
        etree.SubElement(root, member.name, nsmap=NSMAP)

    def _encode_key(self, root, entity, meta_info, key):
        key_value = getattr(entity, key.presentation_name)
        if key_value is None:
            self._raise_key_missing_error()
            return
        if key.mtype == REFERENCE_IDENTITY_CLASS:
            # encode an identity
            NSMAP = {'idx' : _yang_ns._namespaces[key_value._meta_info().module_name]}
            member_elem = etree.SubElement(root, key.name, nsmap=NSMAP)
            member_elem.text = 'idx:%s' % key_value._meta_info().yang_name
        else:
            member_elem = etree.SubElement(root, key.name)
            if key.mtype == REFERENCE_ENUM_CLASS:
                key_value = key_value.name.replace('_', '-').lower()
            member_elem.text = str(key_value)

    def _get_current_tuple_list(self, current_parent, current_meta_info):
        parent_meta_tuple_list = [(current_meta_info, current_parent)]
        while hasattr(current_meta_info, 'parent'):
            current_meta_info = current_meta_info.parent
            if current_parent is not None:
                current_parent = current_parent.parent
            if self._entity_is_abstract(current_parent, current_meta_info) or \
                    self._entity_has_no_keys(current_parent, current_meta_info):
                self._raise_parent_hierarchy_error()
                return []
            parent_meta_tuple_list.append((current_meta_info, current_parent))
        return parent_meta_tuple_list

    def _get_parent_tuple_list(self, current_parent, current_meta_info):
        parent_meta_tuple_list = []
        while hasattr(current_meta_info, 'parent'):
            current_meta_info = current_meta_info.parent
            if current_parent is not None:
                current_parent = current_parent.parent
            if self._entity_is_abstract(current_parent, current_meta_info) or \
                    self._entity_has_no_keys(current_parent, current_meta_info):
                self._raise_parent_hierarchy_error()
                return []
            parent_meta_tuple_list.append((current_meta_info, current_parent))
        return parent_meta_tuple_list

    def _get_parent_namespace(self, current_parent):
        parent_ns = None
        while current_parent is not None and parent_ns is None:
            parent_ns = current_parent.get('xmlns')
            current_parent = current_parent.getparent()
        return parent_ns

    def _is_rpc_reply(self, top_entity):
        return hasattr(top_entity, 'is_rpc') and top_entity.is_rpc

    def _is_rpc_reply_with_output_data(self, top_entity):
        return hasattr(top_entity, 'is_rpc') and top_entity.is_rpc and hasattr(top_entity, 'output') and top_entity.output is not None


def operation_is_edit(operation):
    return operation in ('CREATE', 'UPDATE', 'DELETE')


def operation_is_create_or_update(operation):
    return operation in ('CREATE', 'UPDATE')


def confirmed_commit_supported(capabilities):
#     capabilities = session_manager.server_capabilities
    confirmed_1_0 = 'urn:ietf:params:netconf:capability:confirmed-commit:1.0'
    confirmed_1_1 = 'urn:ietf:params:netconf:capability:confirmed-commit:1.1'
    return confirmed_1_0 in capabilities or confirmed_1_1 in capabilities


def check_errors(payload):
    err = False
    payload = payload.replace('xmlns=', 'xmlnamespace=')
    p = etree.XMLParser(remove_blank_text=True)
    pathlist = []
    elem = etree.XML(payload.encode('utf-8'), parser=p)
    payload = etree.tostring(elem, encoding='utf-8').decode('utf-8')
    tree = etree.fromstring(payload.encode('utf-8'))
    root = etree.ElementTree(tree)
    for e in root.iter():
        if e.text is not None:
            path = root.getpath(e)
            path1 = path.split('/')
            path2 = []
            error_info_detected = False
            for x in path1:
                if x == 'rpc-error':
                    err = True
                if x != 'rpc-reply' and x != 'data'and x != 'ok':
                    path2.append(x)
                    if x == 'error-info':
                        error_info_detected = True

            if error_info_detected is True:
                path = '/'.join(path2)
                path3 = (path, e.text)
                pathlist.append(path3)

    return err, pathlist


def _get_pretty(string):
    parser = etree.XMLParser(remove_blank_text=True)
    element = etree.XML(string.encode('UTF-8'), parser)
    return etree.tostring(element, encoding='UTF-8', pretty_print=True).decode('UTF-8')

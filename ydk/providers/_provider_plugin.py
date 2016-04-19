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

""" providers.py 
 
   Service Providers module. Current implementation supports the NetconfServiceProvider which
   uses ncclient (a Netconf client library) to provide CRUD services.
   
"""
from lxml import etree

from ncclient import manager
from ncclient.operations import RPC, RPCReply

from ydk._core._dm_meta_info import REFERENCE_IDENTITY_CLASS
from ydk.errors import YPYDataValidationError, YPYError, YPYErrorCode
from ydk.types import Empty, DELETE, READ, Decimal64, YList

from ._decoder import XmlDecoder
from ._encoder import XmlEncoder
from ._ydk_types import _SessionTransportMode

import abc
import logging
import ydk.models._yang_ns as _yang_ns


class _SPPlugin(object):
    __metaclass__ = abc.ABCMeta

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


class _NCClientSPPlugin(_SPPlugin):

    def __init__(self, service_protocol_name='Netconf protocol'):
        self._service_protocol_name = service_protocol_name
        self.head = None
        self._nc_manager = None
        self.netconf_sp_logger = logging.getLogger('ydk.providers.NetconfServiceProvider')
        self.separator = '*' * 28

    def encode(self, entity, optype, only_config=False):
        root = self._create_root()
        if operation_is_edit(optype):
            root = self._encode_edit_request(root, entity, optype)
        else:
            root = self._encode_read_request(root, entity, optype, only_config)
        payload = etree.tostring(self.head, method='xml', pretty_print='True')
        return payload

    def encode_rpc(self, rpc):
        if not self._is_rpc(rpc):
            self._raise_non_rpc_error()
        root = self._create_root()
        self._encode_rpc_request(root, rpc)
        payload = etree.tostring(self.head, method='xml', pretty_print='True')
        return payload

    def decode(self, payload, read_filter):
        # In order to figure out which fields are the
        # ones we are interested find the field list
        entity = self._create_top_level_entity_from_read_filter(read_filter)
        XmlDecoder._bind_to_object(payload, entity, self._nc_manager.server_capabilities)
        # drill down to figure out the field access expression
        # that matches the entity or entities to be returned
        # not the argument passed in as a filter might have
        # incomplete key paths, in which case what is returned
        # will be the entity whose common path can be determined

        suffix_field_names = []
        current_entity = read_filter
        if isinstance(current_entity, YList):
            suffix_field_names.append(current_entity.name)
            current_entity = current_entity.parent

        current = entity
        yang_nodes = []
        yang_nodes.extend([ s for s in current_entity._common_path.split('/') if ':' in s])
        yang_nodes = yang_nodes[1:]

        for seg in yang_nodes:
            if '[' in seg:
                seg = seg.split('[')[0]
            _, yang_node_name = seg.split(':')

            found = False
            for member in current._meta_info().meta_info_class_members:
                if member.name == yang_node_name:
                    found = True
                    current = eval('current.%s' % member.presentation_name)
                    if current is None:
                        return None
                    if isinstance(current, YList):
                        if len(current) == 0:
                            return None
                        if len(current) > 2:
                            return current
                        if len(current) == 1:
                            current = current[0]

                    break

            if not found:
                self.crud_logger.error('Error determing what needs to be returned')
                raise YPYError('Error determining what needs to be returned')

        for field in suffix_field_names:
            current = eval('current.%s' % field)

        return current


    def _create_top_level_entity_from_read_filter(self, read_filter):
        non_list_filter = read_filter

        while isinstance(non_list_filter, YList):
            non_list_filter = non_list_filter.parent

        if non_list_filter is None:
            self.crud_logger.error('Cannot determine hierarchy for entity. Please set the parent reference')
            raise YPYError('Cannot determine hierarchy for entity. Please set the parent reference')

        top_entity_meta_info = non_list_filter._meta_info()

        while hasattr(top_entity_meta_info, 'parent') and top_entity_meta_info.parent is not None:
            # need to find the member that has
            top_entity_meta_info = top_entity_meta_info.parent

        exec_import = 'from ' + top_entity_meta_info.pmodule_name + ' import ' + top_entity_meta_info.name.split('.')[0]
        exec exec_import
        entity = eval(top_entity_meta_info.name + '()')
        return entity

    def execute_operation(self, session_manager, optype, payload, options=None):
        '''
            Raises exception on error, else returns result
        '''
        service_provider_rpc = self._create_rpc_instance(session_manager)
        reply_str = "FAILED!"
        if len(payload) == 0:
            return reply_str
        payload = payload.replace("101", service_provider_rpc._id, 1)
        self.netconf_sp_logger.debug('\n%s\n%s', self.separator, payload)
        reply_str = service_provider_rpc._request(payload)
        return self._handle_rpc_reply(session_manager, optype, payload, reply_str)

    def _create_rpc_instance(self, session_manager):
        class _SP_RPC(RPC):
            def _wrap(self, subele):
                return subele

        class _SP_REPLY_CLS(RPCReply):
            def parse(self):
                self._parsed = True
                return True

        RPC.REPLY_CLS = _SP_REPLY_CLS
        return _SP_RPC(session_manager._session, session_manager._device_handler)

    def _handle_rpc_reply(self, session_manager, optype, payload, reply_str):
        err, pathlist = check_errors(reply_str.xml)
        if err:
            self._handle_rpc_error(session_manager, payload, reply_str, pathlist)
        else:
            self._handle_rpc_ok(session_manager, optype, payload, reply_str)

        root = etree.fromstring(reply_str.xml)
        payload = etree.tostring(root, method='xml', pretty_print='True')
        return payload

    def _handle_rpc_ok(self, session_manager, optype, payload, reply_str):
        if operation_is_edit(optype) and confirmed_commit_supported(session_manager.server_capabilities):
            self.netconf_sp_logger.debug('\n%s' , reply_str)
            self._handle_commit(session_manager, payload, reply_str)
        else:
            self.netconf_sp_logger.debug('\n%s\n%s' , reply_str, self.separator)

    def _handle_rpc_error(self, session_manager, payload, reply_str, pathlist):
        self.netconf_sp_logger.error('%s\n%s\n%s\n%s' , self.separator, payload, reply_str.xml, self.separator)
        raise YPYError(YPYErrorCode.SERVER_REJ, reply_str)

    def _handle_commit(self, session_manager, payload, reply_str):
        self.netconf_sp_logger.debug('\n<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="101">\n  <commit/>\n</rpc>')
        commit = session_manager.commit()
        if 'ok' not in commit.xml:
            self.netconf_sp_logger.error('%s\n%s\n%s\ncommit-reply\n%s\n%s', self.separator,
                                    payload, reply_str.xml, commit.xml, self.separator)
            raise YPYError(YPYErrorCode.SERVER_COMMIT_ERR, reply_str)
        else:
            self.netconf_sp_logger.debug('\n%s\n%s' , reply_str, self.separator)

    def _connect(self, session_config, port):
        if (session_config.transportMode == _SessionTransportMode.SSH):
            self._nc_manager = manager.connect(
                host=session_config.hostname,
                port=session_config.port,
                username=session_config.username,
                password=session_config.password,
                look_for_keys=False,
                allow_agent=False,
                hostkey_verify=False)
        elif (session_config.transportMode == _SessionTransportMode.TCP):
            self._nc_manager = manager.connect(
                host=session_config.hostname,
                port=session_config.port,
                transport='tcp')
        return self._nc_manager

    def _disconnect(self):
        self._session_manager.close_session()

    def _get_target_datastore(self):
        target_ds = 'candidate'
        if not confirmed_commit_supported(self._nc_manager.server_capabilities):
            target_ds = 'running'
        return target_ds

    def _create_root(self):
        NSMAP = {'xmlns': 'urn:ietf:params:xml:ns:netconf:base:1.0'}
        self.head = etree.Element('rpc', NSMAP)
        self.head.set('message-id', '101')
        return self.head

    def _encode_edit_request(self, root, entity, optype):
        if not entity.is_config():
            self._raise_read_only_edit_error()
        root = self._create_element(root,
                                    'edit-config',
                                    'target',
                                    self._get_target_datastore(),
                                    'config',
                                    optype)
        root = self._create_preamble(entity, root)

        if operation_is_create_or_update(optype):
            XmlEncoder().encode_to_xml(entity, root, optype)
        else:
            # this is delete
            # To do revisit
            root = self._encode_delete_request(root, entity)
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

    def _encode_delete_request(self, root, entity):
        meta_info = entity._meta_info()
        if self._entity_is_abstract(entity, meta_info):
            self._raise_parent_hierarchy_error()
            return
        NSMAP = { None: meta_info.namespace}
        root = etree.SubElement(root, meta_info.yang_name, nsmap=NSMAP)
        root.set('{urn:ietf:params:xml:ns:netconf:base:1.0}operation', 'delete')
        # are there keys
        root = self._encode_keys(root, entity, meta_info)
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
            root = self._encode_keys(root, parent, meta_info)
        return root

    def _entity_is_abstract(self, entity, meta_info):
        return meta_info.is_abstract and entity.parent is None

    def _entity_has_no_keys(self, entity, meta_info):
        return entity is None and len(meta_info.key_members()) > 0

    def _is_rpc(self, rpc):
        return hasattr(rpc, 'is_rpc') and rpc.is_rpc

    def _raise_parent_hierarchy_error(self):
        self.netconf_sp_logger.error(YPYErrorCode.INVALID_HIERARCHY_PARENT)
        raise YPYError(YPYErrorCode.INVALID_HIERARCHY_PARENT)

    def _raise_key_missing_error(self):
        self.netconf_sp_logger.error(YPYErrorCode.INVALID_HIERARCHY_KEY)
        raise YPYError(YPYErrorCode.INVALID_HIERARCHY_KEY)

    def _raise_read_only_edit_error(self):
        self.netconf_sp_logger.error(YPYErrorCode.INVALID_MODIFY)
        raise YPYError(YPYErrorCode.INVALID_MODIFY)

    def _raise_non_rpc_error(self):
        self.netconf_sp_logger.error(YPYErrorCode.INVALID_RPC)
        raise YPYError(YPYErrorCode.INVALID_RPC)
    
    def _encode_keys(self, root, entity, meta_info):
        for key in meta_info.key_members():
            self._encode_key(root, entity, meta_info, key)
        return root

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
            member_elem.text = str(key_value)
        
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


def operation_is_edit(operation):
    return operation in ('CREATE', 'UPDATE', 'DELETE')


def operation_is_create_or_update(operation):
    return operation in ('CREATE', 'UPDATE')


def confirmed_commit_supported(capabilities):
    confirmed_1_0 = 'urn:ietf:params:netconf:capability:confirmed-commit:1.0'
    confirmed_1_1 = 'urn:ietf:params:netconf:capability:confirmed-commit:1.1'
    return confirmed_1_0 in capabilities or confirmed_1_1 in capabilities


def check_errors(payload):
    err = False
    payload = payload.replace('xmlns=', 'xmlnamespace=')
    p = etree.XMLParser(remove_blank_text=True)
    pathlist = []
    elem = etree.XML(payload, parser=p)
    payload = etree.tostring(elem)
    tree = etree.fromstring(payload)
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

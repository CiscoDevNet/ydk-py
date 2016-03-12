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
from ydk.errors import YPYDataValidationError, YPYError
from ydk.types import Empty, DELETE, READ, Decimal64
from ._encoder import _NetconfEncodeDecodeService
from ._ydk_types import _SessionTransportMode
import abc
import logging


class _SPPlugin(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, service_protocol_name):
        self.service_protocol_name = service_protocol_name

    @abc.abstractmethod
    def encode(self, entity, optype):
        pass

    @abc.abstractmethod
    def execute_operation(self, session, payload, options=None):
        pass


class _NCClientSPPlugin(_SPPlugin):

    def __init__(self, service_protocol_name='Netconf protocol'):
        self._service_protocol_name = service_protocol_name
        self.head = None
        self._nc_manager = None

    def _create_element(self, root, oper, target, candidate, config, optype):

        from lxml import etree

        root = etree.SubElement(root, oper)
        if target is not None:
            target = etree.SubElement(root, target)
        if candidate is not None:
            if target is not None:
                candidate = etree.SubElement(target, candidate)
            else:
                candidate = etree.SubElement(root, candidate)
        if optype == 'DELETE' or optype == 'CREATE' or optype == 'UPDATE':
            # xc = "urn:ietf:params:xml:ns:netconf:base:1.0"
            # operation = "delete"
            NSMAP = {"xc": "urn:ietf:params:xml:ns:netconf:base:1.0"}

            root = etree.SubElement(root, 'config', nsmap=NSMAP)
        elif optype == 'EVENT_SUBSCRIBE':
            root = etree.SubElement(candidate, config)
            root.set('xmlns', "urn:ietf:params:xml:ns:netconf:base:1.0")
        elif optype == 'READ':
            root = etree.SubElement(root, config)
            root.set('type', "subtree")
        else:
            NSMAP = {"xc", "urn:ietf:params:xml:ns:netconf:base:1.0"}
            root = etree.SubElement(root, config, nsmap=NSMAP)


        return root

    def _create_xml(self, root, pathlist, optype, namespace):
        from lxml import etree

        value = []
        for string in pathlist:
            root1 = root
            path, val = string[0], string[1:]
            path = path.split('/')
            if '' in path:
                path.remove('')

            for x in path:
                log = []
                key = None
                if '[' in x:
                    index = x.index('[')
                    element = x[:index]
                    index1 = x.index(']')
                    key = x[index + 1:index1]

                else:
                    element = x
                log = root1.xpath(element)
                if log == []:
                    root1 = etree.SubElement(root1, element)

                    if len(val) > 1:
                        root1.set('xmlns', string[2])
                    # Check for delete flag and only add operation delete for last element
                    if(optype == 'DELETE' and (x == path[-1]) and (val[1] is True or val[2] is True)):
                        xc = 'urn:ietf:params:xml:ns:netconf:base:1.0'
                        if optype == 'DELETE':

                            if val[0] != '':
                                root1.getparent().set(
                                                      '{' + xc + '}operation',
                                                      "delete")
                            else:
                                root1.set('{' + xc + '}operation', "delete")
                        elif optype == 'CREATE':
                            if val[0] != '':
                                root1.getparent().set(
                                                      '{' + xc + '}operation',
                                                      "create")
                            else:
                                root1.set('{' + xc + '}operation', "create")
                else:
                    if x in value:
                        if key is not None:
                            root1 = log[int(key) - 1]
                        else:
                            root1 = log[0]
                    else:
                        root1 = etree.SubElement(root1, element)
                        if len(val) > 1:
                            root1.set('xmlns', val[1])

                if x not in value:
                    value.append(x)
            if val[0] != '':
                if root1.text is not None:
                    to_add = etree.Element(root1.tag)
                    to_add.text = val[0]
                    root1.addnext(to_add)
                else:
                    root1.text = val[0]
        payload = etree.tostring(self.head, method='xml', pretty_print='True')

        return payload

    def _create_preamble(self, entity, root):

        import ydk.models._yang_ns as _yang_ns
        from lxml import etree
        from ydk._core._dm_meta_info import REFERENCE_IDENTITY_CLASS

        netconf_sp_logger = logging.getLogger('ydk.providers.NetconfServiceProvider')
        parent_meta_tuple_list = []
        current_meta_info = entity._meta_info()
        current_parent = entity

        while hasattr(current_meta_info, 'parent'):
            current_meta_info = current_meta_info.parent
            if current_parent is not None:
                current_parent = current_parent.parent

            if current_meta_info.is_abstract:
                if current_parent is None:
                    netconf_sp_logger.error('Parent is not set. Parent hierarchy cannot be determined')
                    raise YPYError('parent is not set. Parent Hierarchy cannot be determined')

            if current_parent is None and len(current_meta_info.key_members()) > 0:
                netconf_sp_logger.error('Parent is not set. Parent hierarchy cannot be determined')
                raise YPYError('parent is not set. Parent Hierarchy cannot be determined')
            parent_meta_tuple_list.append((current_meta_info, current_parent))

        parent_ns = None
        current_parent = root
        while current_parent != None and parent_ns is None:
            parent_ns = current_parent.get('xmlns')
            current_parent = current_parent.getparent()

        for meta_info, parent in reversed(parent_meta_tuple_list):
            root = etree.SubElement(root,
                                   meta_info.yang_name)
            ns = meta_info.namespace
            if ns is not None and parent_ns != ns:
                root.set('xmlns', ns)
                parent_ns = ns


            for key in meta_info.key_members():
                key_value = getattr(parent, key.presentation_name)
                if key_value is None:
                    netconf_sp_logger.error('Key value is not set. Parent hierarchy cannot be constructed')
                    raise YPYError('Key value is not set. Parent hierarchy cannot be constructed')

                if key.mtype == REFERENCE_IDENTITY_CLASS:
                    # encode an identity
                    NSMAP = {'idx' : _yang_ns._namespaces[key_value._meta_info().module_name]}
                    member_elem = etree.SubElement(root, key.name, nsmap=NSMAP)
                    member_elem.text = 'idx:%s' % key_value._meta_info().yang_name
                else:
                    member_elem = etree.SubElement(root, key.name)
                    member_elem.text = str(key_value)

        return root


    def encode(self, entity, optype, only_config=False):

        import ydk.models._yang_ns as _yang_ns
        from lxml import etree
        from ydk._core._dm_meta_info import REFERENCE_IDENTITY_CLASS

        netconf_sp_logger = logging.getLogger('ydk.providers.NetconfServiceProvider')

        NSMAP = {'xmlns': 'urn:ietf:params:xml:ns:netconf:base:1.0'}
        target_ds = 'candidate'
        confirmed_1_0 = 'urn:ietf:params:netconf:capability:confirmed-commit:1.0'
        confirmed_1_1 = 'urn:ietf:params:netconf:capability:confirmed-commit:1.1'
        if not confirmed_1_0  in self._nc_manager.server_capabilities \
        and not confirmed_1_1 in self._nc_manager.server_capabilities:
            target_ds = 'running'
        self.head = etree.Element('rpc', NSMAP)
        self.head.set('message-id', '101')
        root = self.head

        if optype in ('CREATE', 'UPDATE', 'DELETE'):
            if not entity.is_config():
                netconf_sp_logger.error('Attempt to modify a read-only entity was made')
                raise YPYDataValidationError('Entity is not modifiable')
            root = self._create_element(
                                        root,
                                        'edit-config',
                                        'target',
                                        target_ds,
                                        'config',
                                        optype)


            root = self._create_preamble(entity, root)
            if optype in ('CREATE', 'UPDATE'):

                _NetconfEncodeDecodeService()._encode(entity, root, optype)
            else:
                # this is delete
                # To do revisit
                meta_info = entity._meta_info()
                if meta_info.is_abstract and entity.parent is None:
                    netconf_sp_logger.error('parent is not set. Parent Hierarchy cannot be determined')
                    raise YPYError('parent is not set. Parent Hierarchy cannot be determined')
                NSMAP = {}
                if not meta_info.is_abstract:
                    NSMAP = { None: meta_info.namespace}

                root = etree.SubElement(root, meta_info.yang_name, nsmap=NSMAP)
                root.set('{urn:ietf:params:xml:ns:netconf:base:1.0}operation', 'delete')
                # are there keys
                for key in meta_info.key_members():

                    key_value = getattr(entity, key.presentation_name)
                    if key_value is None:
                        netconf_sp_logger.error('Key value is not set. Cannot identify element to delete')
                        raise YPYError('Key value is not set. Cannot identify element to delete')
                    if key.mtype == REFERENCE_IDENTITY_CLASS:
                        # encode an identity
                        NSMAP = {'idx' : _yang_ns._namespaces[key_value._meta_info().module_name]}
                        member_elem = etree.SubElement(root, key.name, nsmap=NSMAP)
                        member_elem.text = 'idx:%s' % key_value._meta_info().yang_name
                    else:
                        member_elem = etree.SubElement(root, key.name)
                        member_elem.text = str(key_value)

        elif optype == 'READ_OPER' or optype == 'READ':
            get_str = 'get-config' if only_config else 'get'
            source = 'source' if only_config else None
            source_ds = 'running' if only_config else None
            root = self._create_element(
                                        root,
                                        get_str,
                                        source,
                                        source_ds,
                                        'filter',
                                        optype)
            root.set('type', "subtree")

            root = self._create_preamble(entity, root)

            _NetconfEncodeDecodeService()._encode_filter(entity, root, optype)

        payload = etree.tostring(self.head, method='xml', pretty_print='True')
        return payload

    def encode_rpc(self, rpc):
        # TODO
        return ''

    # raises exeception on error, else result
    def execute_operation(self, session_manager, payload, options=None):
        from ncclient.operations import RPC, RPCReply
        from ydk._core._dmtree import DmTree, check_errors
        from lxml import etree

        netconf_sp_logger = logging.getLogger('ydk.providers.NetconfServiceProvider')

        class _SP_RPC(RPC):

            def _wrap(self, subele):
                return subele


        class _SP_REPLY_CLS(RPCReply):

            def parse(self):
                self._parsed = True
                return True

        RPC.REPLY_CLS = _SP_REPLY_CLS
        sp_rpc = _SP_RPC(session_manager._session, session_manager._device_handler)
        reply_str = "FAILED!"
        if len(payload) == 0:
            return reply_str
        payload = payload.replace("101", sp_rpc._id, 1)
        # print request

        reply_str = sp_rpc._request(payload)
        separator = '*' * 28

        err, pathlist = check_errors(reply_str.xml)
        if err:
            netconf_sp_logger.error('%s\n%s\n%s\n%s' , separator, payload, reply_str.xml, separator)
            raise YPYError('Server rejected request')
        else:
            cc_1_0 = 'urn:ietf:params:netconf:capability:confirmed-commit:1.0'
            cc_1_1 = 'urn:ietf:params:netconf:capability:confirmed-commit:1.1'
            capabilities = session_manager.server_capabilities
            if cc_1_0 in capabilities or cc_1_1 in capabilities:
                commit = session_manager.commit()
                if 'ok' not in commit.xml:
                    netconf_sp_logger.error('%s\n%s\n%s\ncommit-reply\n%s\n%s', separator,
                                            payload, reply_str.xml, commit.xml, separator)
                    raise YPYError('Server reported an error while commiting change!')
                else:
                    netconf_sp_logger.debug('%s\n%s\n%s\n\ncommit-reply\n%s\n%s', separator,
                                            payload, reply_str.xml, commit.xml, separator)
            else:
                netconf_sp_logger.debug('%s\n%s\n%s\n%s' , separator, payload, reply_str.xml, separator)

        root = etree.fromstring(reply_str.xml)
        payload = etree.tostring(root, method='xml', pretty_print='True')
        return payload

    def _connect(self, session_config, port):
        from ncclient import manager
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

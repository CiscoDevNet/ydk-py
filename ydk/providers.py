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

import abc

from enum import Enum

from ydk.errors import YPYDataValidationError, YPYError
from ydk.types import Empty, DELETE, READ, Decimal64
import logging
logging.getLogger('ydk').addHandler(logging.NullHandler())


class _SPP_OPTYPE(Enum):
    CREATE = 0
    UPDATE = 1
    DELETE = 2
    READ = 3
    READ_OPER = 4
    RPC = 5
    EVENT_SUBSCRIBE = 6


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

def validate_entity(entity):
    i_errors = []
    validate_entity_delegate(entity, i_errors)
    if len(i_errors) > 0:
        _i_errors = map((lambda t: ': '.join(t)), i_errors)
        errmsg = '\n'.join(_i_errors)
        raise YPYDataValidationError(errmsg)


def validate_entity_delegate(entity, i_errors):
    """ Validates the given entity.
    
        This function validates the given entity and it's children. If an entity class
        has any errors , the errors will available in the injected member i_errors ,
        which is a list of tuples of form (<name of the class member>, <error messsage>)
        
        Note this method will raise ydk.errors.YPYDataValidationError if validation fails
    """
    from ydk._core._dm_meta_info import _dm_validate_value
    from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_ENUM_CLASS
    
    for member in entity._meta_info().meta_info_class_members:
        # print member.mtype, member.name
        value = eval('entity.%s'%member.presentation_name)
        if isinstance(value, READ):
            continue

        if value is None:
            continue
            
        #bits
        if hasattr(value, '_has_data') and not value._has_data():
            continue

        # if value is not None:
        if  member.mtype in (ATTRIBUTE, REFERENCE_ENUM_CLASS):
        # if  member.mtype==ATTRIBUTE:
            _dm_validate_value(member, value, entity, i_errors)

class _NetconfEncodeDecodeService(object):
    def __init__(self):
        pass
    
    def _encode_filter(self, filter, root):
        self._encode(filter, root, True)

    
    def _encode_value(self, member, member_elem, NSMAP, value):
        
        import ydk.models._yang_ns as _yang_ns
        from ydk._core._dm_meta_info import REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS
    
        encoded = True
        if member.mtype == REFERENCE_IDENTITY_CLASS:
            exec 'from %s import %s'%(member.pmodule_name, member.clazz_name.split('.')[0])
            
            if issubclass(type(value), eval(member.clazz_name)):
                identity_inst = value
                if _yang_ns._namespaces[member.module_name] == _yang_ns._namespaces[identity_inst._meta_info().module_name]:
                    #no need for prefix in this case
                    member_elem.text = identity_inst._meta_info().yang_name
                else:
                    NSMAP['idx'] = _yang_ns._namespaces[identity_inst._meta_info().module_name]
                    member_elem.text = 'idx:%s'%identity_inst._meta_info().yang_name
            else:
                encoded = False

        elif member.mtype == REFERENCE_BITS:
            exec 'from %s import %s'%(member.pmodule_name, member.clazz_name.split('.')[0])
            
            if isinstance(value, eval(member.clazz_name)):
                bits_value = value
                value = " ".join([k for k in bits_value._dictionary if bits_value._dictionary[k] == True])
                if (len(value)  > 1):
                    member_elem.text = value
                else:
                    encoded = False
            else:
                encoded = False     
        elif member.mtype == REFERENCE_ENUM_CLASS:
            enum_value = value
            exec_import = 'from ' + member.pmodule_name + ' import ' + member.clazz_name.split('.')[0]
            exec exec_import
            enum_clazz = eval(member.clazz_name)
            literal_map = enum_clazz._meta_info().literal_map
            enum_found = False
            for yang_enum_name in literal_map:
                literal = literal_map[yang_enum_name]
                if enum_value == getattr(enum_clazz, literal) \
                    or enum_value == literal:
                    member_elem.text = yang_enum_name
                    enum_found = True
                    break
            if not enum_found:
                encoded = False
        elif member.ptype == 'bool' and isinstance(value, bool):
            if value is True:
                member_elem.text = 'true'
            else:
                member_elem.text = 'false'
        elif member.ptype == 'Empty' and isinstance(value, Empty):
            pass
        elif member.ptype == 'Decimal64' and isinstance(value, Decimal64):
            member_elem.text=value.s
        elif member.ptype == 'str' and isinstance(value, str):
            member_elem.text = value
        elif member.ptype == 'int' and isinstance(value, int):
            member_elem.text = str(value)
        elif member.ptype == 'long' and isinstance(value, long):
            member_elem.text = str(value)
        else:
            encoded = False
        
        return encoded
            
        
    def _encode(self, entity, root, is_filter=False):
        import ydk.models._yang_ns as _yang_ns
        from lxml import etree
        from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_LIST , REFERENCE_LEAFLIST, REFERENCE_UNION
        
        ''' Convert the entity to an xml payload '''
        #if the entity has a parent hierarchy use that to get 
        # the parent related envelope that we need
        if not is_filter and hasattr(entity, '_has_data') and not entity._has_data():
            return

        validate_entity(entity)
        
        elem = etree.SubElement(root, entity._meta_info().yang_name)
        parent_ns = None
        current_parent = root
        while current_parent != None and parent_ns is None:
            parent_ns = current_parent.get('xmlns')
            current_parent = current_parent.getparent()
            
        if entity._meta_info().namespace is not None and parent_ns != entity._meta_info().namespace:
            elem.set('xmlns', entity._meta_info().namespace)

        for member in entity._meta_info().meta_info_class_members:
            value = eval('entity.%s'%member.presentation_name)
            if value is None or isinstance(value, list) and value == []:
                continue
            #bits
            if hasattr(value, '_has_data') and not value._has_data():
                continue
            
            member_elem = None
            NSMAP = {}
            if member.mtype not in [REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST] or isinstance(value, DELETE) or isinstance(value, READ):
                member_elem = etree.SubElement(elem, member.name, nsmap=NSMAP)
                if entity._meta_info().namespace is not None and entity._meta_info().namespace != _yang_ns._namespaces[member.module_name]:
                    NSMAP[None] = _yang_ns._namespaces[member.module_name]
            
            if isinstance(value, DELETE) and not is_filter:
                xc = 'urn:ietf:params:xml:ns:netconf:base:1.0'
                member_elem.set('{' + xc + '}operation', 'delete')
            elif isinstance(value, READ):
                continue
            elif member.mtype == REFERENCE_CLASS:
                self._encode(value, elem)
            elif member.mtype == REFERENCE_LIST:
                child_list = value
                for child in child_list:
                    self._encode(child, elem)
            elif member.mtype == REFERENCE_LEAFLIST and isinstance(value, list):
                for child in value:
                    member_elem = etree.SubElement(elem, member.name, nsmap=NSMAP)
                    if entity._meta_info().namespace is not None and entity._meta_info().namespace != _yang_ns._namespaces[member.module_name]:
                        NSMAP[None] = _yang_ns._namespaces[member.module_name]
                    self._encode_value(member, member_elem, NSMAP, child)
            elif member.mtype == REFERENCE_UNION:
                for contained_member in member.members:
                    #determine what kind of encoding is needed here
                    if self._encode_value(contained_member, member_elem, NSMAP, value):
                        break
                # if not encoded:
                #     raise YPYError('Cannot translate union value')
            else:
                if not self._encode_value(member, member_elem, NSMAP, value):
                    # raise YPYError('Cannot encode value')
                    pass


class _NCClientSPPlugin(_SPPlugin):

    def __init__(self, service_protocol_name='Netconf protocol'):
        self._service_protocol_name = service_protocol_name
        self.head = None
        self._nc_manager = None


    def _validate(self, optype, namespace=None):
        flag = 1
        for member in _SPP_OPTYPE:
            if member.name == optype:
                flag = 0
                break
            else:
                flag = 1
        if flag == 1:
            raise TypeError("operation type invalid")
        if namespace is not None and not isinstance(namespace, str):
            raise TypeError("namespace type invalid")

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
            #xc = "urn:ietf:params:xml:ns:netconf:base:1.0"
            #operation = "delete"
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
                    #Check for delete flag and only add operation delete for last element
                    if( optype == 'DELETE' and (x == path[-1]) and (val[1] is True or val[2] is True) ): 
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
                    #encode an identity
                    NSMAP = {'idx' : _yang_ns._namespaces[key_value._meta_info().module_name]}
                    member_elem = etree.SubElement(root, key.name, nsmap=NSMAP)
                    member_elem.text = 'idx:%s'%key_value._meta_info().yang_name
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
                
                _NetconfEncodeDecodeService()._encode(entity, root)
            else:
                #this is delete 
                #To do revisit
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
                        #encode an identity
                        NSMAP = {'idx' : _yang_ns._namespaces[key_value._meta_info().module_name]}
                        member_elem = etree.SubElement(root, key.name, nsmap=NSMAP)
                        member_elem.text = 'idx:%s'%key_value._meta_info().yang_name
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

            _NetconfEncodeDecodeService()._encode_filter(entity, root)

        payload = etree.tostring(self.head, method='xml', pretty_print='True')
        return payload

    def encode_rpc(self, rpc):
        # TODO
        return ''

    def commit(self):
        
        from lxml import etree
        
        payload = '<rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0"><commit/></rpc>'
        root = etree.fromstring(payload)
        payload = etree.tostring(root, method='xml', pretty_print='True')
        return payload

    def decode(self, payload):
        
        from lxml import etree
        
        payload = payload.replace('xmlns', 'xmlnamespace')
        p = etree.XMLParser(remove_blank_text=True)
        pathlist = []
        #xml_dict = {}
        elem = etree.XML(payload, parser=p)
        payload = etree.tostring(elem)
        tree = etree.fromstring(payload)
        root = etree.ElementTree(tree)
        for e in root.iter():
            if e.tag == 'rpc-error':
                raise Exception(
                    'Encountered error in %s : %s' %
                    (e.find('error-type').text, e.find('error-tag').text))

            nm = e.attrib.get('xmlnamespace')
            if nm is not None:
                if e.tag in ['', 'rpc-reply']:
                    #print("ignoring '' or rpc-reply tag")
                    nm = None
            if nm is None and e.text is None and e != root.getroot():
                path = (root.getpath(e), '', '')
                pathlist.append(path)

            if nm is not None or e.text is not None:
                path = root.getpath(e)
                path1 = path.split('/')
                path2 = []
                for x in path1:
                    if x != 'rpc-reply' and x != 'data'and x != 'ok':
                        path2.append(x)
                path = '/'.join(path2)
                v = e.text
                if e.text == None:
                    v = ''
                if path == '' and v =='':
                    continue
                if nm is None:
                    nm = ''
                path3 = (path, v, nm)
                #if nm is not None:
                #    path3 = (path, v, nm)
                pathlist.append(path3)
        return pathlist

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
        #print request
        
        reply_str = sp_rpc._request(payload)
        separator = '*' * 28

        err, pathlist = check_errors(reply_str.xml)
        if err:
            netconf_sp_logger.error('%s\n%s\n%s\n%s' ,separator, payload, reply_str.xml, separator)
            raise YPYError('Server rejected request')
        else:
            cc_1_0 = 'urn:ietf:params:netconf:capability:confirmed-commit:1.0'
            cc_1_1 = 'urn:ietf:params:netconf:capability:confirmed-commit:1.1'
            capabilities = session_manager.server_capabilities
            if cc_1_0 in capabilities or cc_1_1 in capabilities:
                commit = session_manager.commit()
                if 'ok' not in commit.xml:
                    netconf_sp_logger.error('%s\n%s\n%s\ncommit-reply\n%s\n%s', separator, 
                                            payload, reply_str.xml,commit.xml, separator)     
                    raise YPYError('Server reported an error while commiting change!')
                else:
                    netconf_sp_logger.debug('%s\n%s\n%s\n\ncommit-reply\n%s\n%s', separator, 
                                            payload, reply_str.xml,commit.xml, separator)     
            else:
                netconf_sp_logger.debug('%s\n%s\n%s\n%s' ,separator, payload, reply_str.xml, separator)
            
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

class ServiceProvider(object):
    """Base class for Service Providers"""
    

    def close(self):
        """ Base method to close service provider instance session """
        pass



class NetconfServiceProvider(ServiceProvider):
    """ NCClient based Netconf ServiceProvider 
    
        Initialization parameter of NetconfServiceProvider
        
        kwargs:
            - address - The address of the netconf server
            - port  - The port to use default is 830
            - username - The name of the user
            - password - The password to use
            - protocol - one of either ssh or tcp    
    """

    def __init__(self, **kwargs):
        self.address = kwargs.get('address', '127.0.0.1')
        self.port = kwargs.get('port', 830)
        self.username = kwargs.get('username', 'admin')
        self.password = kwargs.get('password', 'admin')
        self.protocol = kwargs.get('protocol', 'ssh')
        
        if self.protocol == 'tcp':
            self.session_config = _SessionConfig(
                                                 _SessionTransportMode.TCP,
                                                 self.address,
                                                 self.port,
                                                 self.username,
                                                 self.password)
        else:
            self._session_config = _SessionConfig(
                                           _SessionTransportMode.SSH,
                                           self.address,
                                           self.port,
                                           self.username,
                                           self.password)
        
        self.ne = _NetworkElement(
                                  self._session_config,
                                  _ServiceProtocolName.NETCONF)

        netconf_sp_logger = logging.getLogger('ydk.providers.NetconfServiceProvider')
        self.ne.connect()
        netconf_sp_logger.info('NetconfServiceProvider connected to %s:%s using %s' 
                               %(self.address, self.port, self.protocol))

        self.sp_instance = self.ne.sp_instance
        self.payload_log = self.ne.payload_log
        self.encode_format = self.ne.encode_format
    
    def close(self):
        """ Closes the netconf session """
        self.ne.disconnect()

class _SessionConfig(object):

    '''
    SessionConfig contains the configuration that will be used
    for connecting to the network element.

    SessionConfig provides a means to configure session attributes
    prior to connecting to a NetworkElement.

    The SessionConfig object is required only if the defaults need to
    be overridden. Passing a null for the SessionConfig in the
    connect() call will result in a SSH connection between the application
    and the network element using default values. See specific setter APIs
    for the defaults for each attribute.
    '''

    def __init__(self, transport, hostname, port, username, password):
        '''
        Constructor

        Keyword argument:
        transport
            One of the options in SessionConfig.SessionTransportMode
            defaults to SessionConfig.SessionTransportMode.SSH
        hostname
           The hostname/ip address of the endpoint
        port
            The port to connect to on the endpoint
        username
           The username
        password
           The password used for connecting

        '''
        if transport is None:
            self.transportMode = self.DEFAULT_TRANSPORT_MODE
        else:
            self.transportMode = transport

        if hostname is None:
            self.hostname = "localhost"
        else:
            self.hostname = hostname
            
        if port is None:
            self.port = "830"
        else:
            self.port = port
            
        self.username = username
        self.password = password
 
    def __init___0(self, other):
        '''
        Keyword argument:
        other -- The SessionConfig object to copy from

        '''
        self.serviceType = other.serviceType
        self.transportMode = other.transportMode
        self.port = other.port

    def _set_transport_mode(self, transportMode):
        if transportMode is None:
            transportMode = self.DEFAULT_TRANSPORT_MODE
        self._transportMode = transportMode

    def _get_transport_mode(self):
        return self._transportMode

    _doc_transport_mode = '''
    Transport type to be used for the session. If the value is None,
    the default transport type will be used. The default transport is
    SessionConfig.SessionTransportMode.SSH
    '''
    transportMode = property(
        _get_transport_mode,
        _set_transport_mode,
        None,
        _doc_transport_mode)

    def _set_service_type(self, serviceType):
        if serviceType is None:
            serviceType = self.DEFAULT_SERVICE_TYPE
        self._serviceType = serviceType

    def _get_service_type(self):
        return self._serviceType

    _doc_service_type = '''
    Service type to be used for the session. If the value is None,
    the default service type will be used. The default transport is
    SessionConfig.SessionServiceType.NETCONF
    '''
    serviceType = property(
        _get_service_type,
        _set_service_type,
        None,
        _doc_service_type)

#
#  * Transport mode to be used for a session.
#  *
#  *  SSH:    Secure Shell
#  *  TLS:    Secured TLS socket
#  *  TIPC:   TIPC socket
#  *  TCP:    Plain Socket
class _SessionTransportMode(Enum):
    SSH = 1
    TLS = 2
    TIPC = 3
    TCP = 4


#
#      * Default transport mode is SSH in production environment.
#
_DEFAULT_TRANSPORT_MODE = _SessionTransportMode.SSH

class _NetworkElement(object):

    def __init__(self, session_config, service_protocol_type, encode_format = None,port=None):

        self.session_config = session_config

        if service_protocol_type is None:
            self.service_protocol_type = self.DEFAULT_SERVICE_TYPE
        else:
            self.service_protocol_type = service_protocol_type
        if encode_format == None:
            self.encode_format = _DEFAULT_ENCODING_FORMAT
        else:
            self.encode_format = encode_format
        if port is None:
            self.port = _DEFAULT_NC_PORT
        else:
            self.port = port

        self.sp_instance = None

    def connect(self):
        netconf_client = _NCClientSPPlugin('Netconf Protocol')
        self.sp_instance = netconf_client
        netconf_client._connect(self.session_config, self.port)
        self._pfo = open('netconf.log', 'wb')
        self._pfo.write("Connected to ncserver...\n")
        return True

    def disconnect(self):
        self.sp_instance._nc_manager.close_session()
        self._pfo.close()
        print("Operations service protocol packets log can be found in : netconf.log")
        return True

    def payload_log(self, p): 
        self._pfo.write(p)
    #
    #      * Service Protocol Type to be used for a session.
    #      *
    #
class _ServiceProtocolName(Enum):
    NETCONF = 1
    ONEP = 2
    RESTCONF = 3

class _Encoding_Format(Enum):
    XML = 1
    JSON = 2

#
#      * Default Service type is NETCONF in production environment.
#
_DEFAULT_SERVICE_TYPE = _ServiceProtocolName.NETCONF
_DEFAULT_ENCODING_FORMAT = _Encoding_Format.XML
_DEFAULT_NC_PORT = 830


""" Cisco_IOS_XR_sysadmin_tacacs_tacacs_server 

This module contains definitions
for the Calvados model objects.

This module defines the TACACS+ data model.

Copyright (c) 2012\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class TacacsServer(_Entity_):
    """
    
    
    .. attribute:: host
    
    	
    	**type**\: list of  		 :py:class:`Host <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_tacacs_tacacs_server.TacacsServer.Host>`
    
    .. attribute:: timeout
    
    	
    	**type**\: int
    
    	**range:** 1..1000
    
    .. attribute:: key
    
    	
    	**type**\: str
    
    .. attribute:: test_authentication
    
    	
    	**type**\:  :py:class:`TestAuthentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_tacacs_tacacs_server.TacacsServer.TestAuthentication>`
    
    	**presence node**\: True
    
    	**config**\: False
    
    .. attribute:: test_authorization
    
    	
    	**type**\:  :py:class:`TestAuthorization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_tacacs_tacacs_server.TacacsServer.TestAuthorization>`
    
    	**presence node**\: True
    
    	**config**\: False
    
    .. attribute:: test_accounting
    
    	
    	**type**\:  :py:class:`TestAccounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_tacacs_tacacs_server.TacacsServer.TestAccounting>`
    
    	**presence node**\: True
    
    	**config**\: False
    
    .. attribute:: requests
    
    	
    	**type**\:  :py:class:`Requests <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_tacacs_tacacs_server.TacacsServer.Requests>`
    
    	**config**\: False
    
    

    """

    _prefix = 'tacacs-server'
    _revision = '2017-05-10'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(TacacsServer, self).__init__()
        self._top_entity = None

        self.yang_name = "tacacs-server"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-tacacs-tacacs-server"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("host", ("host", TacacsServer.Host)), ("Cisco-IOS-XR-sysadmin-tacacs-test-tacacs:test-authentication", ("test_authentication", TacacsServer.TestAuthentication)), ("Cisco-IOS-XR-sysadmin-tacacs-test-tacacs:test-authorization", ("test_authorization", TacacsServer.TestAuthorization)), ("Cisco-IOS-XR-sysadmin-tacacs-test-tacacs:test-accounting", ("test_accounting", TacacsServer.TestAccounting)), ("Cisco-IOS-XR-sysadmin-tacacs-show-tacacs:requests", ("requests", TacacsServer.Requests))])
        self._leafs = OrderedDict([
            ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
            ('key', (YLeaf(YType.str, 'key'), ['str'])),
        ])
        self.timeout = None
        self.key = None

        self.test_authentication = None
        self._children_name_map["test_authentication"] = "Cisco-IOS-XR-sysadmin-tacacs-test-tacacs:test-authentication"

        self.test_authorization = None
        self._children_name_map["test_authorization"] = "Cisco-IOS-XR-sysadmin-tacacs-test-tacacs:test-authorization"

        self.test_accounting = None
        self._children_name_map["test_accounting"] = "Cisco-IOS-XR-sysadmin-tacacs-test-tacacs:test-accounting"

        self.requests = TacacsServer.Requests()
        self.requests.parent = self
        self._children_name_map["requests"] = "Cisco-IOS-XR-sysadmin-tacacs-show-tacacs:requests"

        self.host = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-tacacs-tacacs-server:tacacs-server"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(TacacsServer, ['timeout', 'key'], name, value)


    class Host(_Entity_):
        """
        
        
        .. attribute:: ip  (key)
        
        	
        	**type**\: union of the below types:
        
        		**type**\: str
        
        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        		**type**\: str
        
        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: port  (key)
        
        	
        	**type**\: int
        
        	**range:** 1..65535
        
        .. attribute:: timeout
        
        	
        	**type**\: int
        
        	**range:** 1..1000
        
        .. attribute:: key
        
        	
        	**type**\: str
        
        

        """

        _prefix = 'tacacs-server'
        _revision = '2017-05-10'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(TacacsServer.Host, self).__init__()

            self.yang_name = "host"
            self.yang_parent_name = "tacacs-server"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['ip','port']
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ip', (YLeaf(YType.str, 'ip'), ['str','str'])),
                ('port', (YLeaf(YType.uint16, 'port'), ['int'])),
                ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                ('key', (YLeaf(YType.str, 'key'), ['str'])),
            ])
            self.ip = None
            self.port = None
            self.timeout = None
            self.key = None
            self._segment_path = lambda: "host" + "[ip='" + str(self.ip) + "']" + "[port='" + str(self.port) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-tacacs-tacacs-server:tacacs-server/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(TacacsServer.Host, ['ip', 'port', 'timeout', 'key'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_tacacs_tacacs_server as meta
            return meta._meta_table['TacacsServer.Host']['meta_info']


    class TestAuthentication(_Entity_):
        """
        
        
        .. attribute:: authentication
        
        	Authentication
        	**type**\: str
        
        	**config**\: False
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'test_tacacs'
        _revision = '2017-05-10'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(TacacsServer.TestAuthentication, self).__init__()

            self.yang_name = "test-authentication"
            self.yang_parent_name = "tacacs-server"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('authentication', (YLeaf(YType.str, 'authentication'), ['str'])),
            ])
            self.authentication = None
            self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-tacacs-test-tacacs:test-authentication"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-tacacs-tacacs-server:tacacs-server/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(TacacsServer.TestAuthentication, ['authentication'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_tacacs_tacacs_server as meta
            return meta._meta_table['TacacsServer.TestAuthentication']['meta_info']


    class TestAuthorization(_Entity_):
        """
        
        
        .. attribute:: authorization
        
        	Authorization
        	**type**\: str
        
        	**config**\: False
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'test_tacacs'
        _revision = '2017-05-10'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(TacacsServer.TestAuthorization, self).__init__()

            self.yang_name = "test-authorization"
            self.yang_parent_name = "tacacs-server"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('authorization', (YLeaf(YType.str, 'authorization'), ['str'])),
            ])
            self.authorization = None
            self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-tacacs-test-tacacs:test-authorization"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-tacacs-tacacs-server:tacacs-server/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(TacacsServer.TestAuthorization, ['authorization'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_tacacs_tacacs_server as meta
            return meta._meta_table['TacacsServer.TestAuthorization']['meta_info']


    class TestAccounting(_Entity_):
        """
        
        
        .. attribute:: accounting
        
        	Accounting
        	**type**\: str
        
        	**config**\: False
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'test_tacacs'
        _revision = '2017-05-10'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(TacacsServer.TestAccounting, self).__init__()

            self.yang_name = "test-accounting"
            self.yang_parent_name = "tacacs-server"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('accounting', (YLeaf(YType.str, 'accounting'), ['str'])),
            ])
            self.accounting = None
            self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-tacacs-test-tacacs:test-accounting"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-tacacs-tacacs-server:tacacs-server/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(TacacsServer.TestAccounting, ['accounting'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_tacacs_tacacs_server as meta
            return meta._meta_table['TacacsServer.TestAccounting']['meta_info']


    class Requests(_Entity_):
        """
        
        
        .. attribute:: ipv4
        
        	
        	**type**\: list of  		 :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_tacacs_tacacs_server.TacacsServer.Requests.Ipv4>`
        
        	**config**\: False
        
        

        """

        _prefix = 'show_tacacs'
        _revision = '2017-05-10'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(TacacsServer.Requests, self).__init__()

            self.yang_name = "requests"
            self.yang_parent_name = "tacacs-server"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ipv4", ("ipv4", TacacsServer.Requests.Ipv4))])
            self._leafs = OrderedDict()

            self.ipv4 = YList(self)
            self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-tacacs-show-tacacs:requests"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-tacacs-tacacs-server:tacacs-server/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(TacacsServer.Requests, [], name, value)


        class Ipv4(_Entity_):
            """
            
            
            .. attribute:: addr  (key)
            
            	Server IPv4 address
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            		**type**\: str
            
            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            	**config**\: False
            
            .. attribute:: port  (key)
            
            	Server Port
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: opens
            
            	Socket open count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: closes
            
            	Socket close count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: aborts
            
            	Socket abort count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: errors
            
            	Socket error count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: packets_in
            
            	Packets received count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: packets_out
            
            	Packets transmitted count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'show_tacacs'
            _revision = '2017-05-10'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(TacacsServer.Requests.Ipv4, self).__init__()

                self.yang_name = "ipv4"
                self.yang_parent_name = "requests"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['addr','port']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('addr', (YLeaf(YType.str, 'addr'), ['str','str'])),
                    ('port', (YLeaf(YType.uint16, 'port'), ['int'])),
                    ('opens', (YLeaf(YType.uint32, 'opens'), ['int'])),
                    ('closes', (YLeaf(YType.uint32, 'closes'), ['int'])),
                    ('aborts', (YLeaf(YType.uint32, 'aborts'), ['int'])),
                    ('errors', (YLeaf(YType.uint32, 'errors'), ['int'])),
                    ('packets_in', (YLeaf(YType.uint32, 'packets_in'), ['int'])),
                    ('packets_out', (YLeaf(YType.uint32, 'packets_out'), ['int'])),
                ])
                self.addr = None
                self.port = None
                self.opens = None
                self.closes = None
                self.aborts = None
                self.errors = None
                self.packets_in = None
                self.packets_out = None
                self._segment_path = lambda: "ipv4" + "[addr='" + str(self.addr) + "']" + "[port='" + str(self.port) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-tacacs-tacacs-server:tacacs-server/Cisco-IOS-XR-sysadmin-tacacs-show-tacacs:requests/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(TacacsServer.Requests.Ipv4, ['addr', 'port', 'opens', 'closes', 'aborts', 'errors', 'packets_in', 'packets_out'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_tacacs_tacacs_server as meta
                return meta._meta_table['TacacsServer.Requests.Ipv4']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_tacacs_tacacs_server as meta
            return meta._meta_table['TacacsServer.Requests']['meta_info']

    def clone_ptr(self):
        self._top_entity = TacacsServer()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_tacacs_tacacs_server as meta
        return meta._meta_table['TacacsServer']['meta_info']



""" Cisco_IOS_XR_aaa_protocol_radius_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR aaa\-protocol\-radius package operational data.

This module contains definitions
for the following management objects\:
  radius\: RADIUS operational data

This YANG module augments the
  Cisco\-IOS\-XR\-aaa\-locald\-oper
module with state data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Radius(Entity):
    """
    RADIUS operational data
    
    .. attribute:: nodes
    
    	Contains all the nodes
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes>`
    
    

    """

    _prefix = 'aaa-protocol-radius-oper'
    _revision = '2017-11-13'

    def __init__(self):
        super(Radius, self).__init__()
        self._top_entity = None

        self.yang_name = "radius"
        self.yang_parent_name = "Cisco-IOS-XR-aaa-protocol-radius-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", Radius.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = Radius.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-aaa-protocol-radius-oper:radius"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Radius, [], name, value)


    class Nodes(Entity):
        """
        Contains all the nodes
        
        .. attribute:: node
        
        	RADIUS operational data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node>`
        
        

        """

        _prefix = 'aaa-protocol-radius-oper'
        _revision = '2017-11-13'

        def __init__(self):
            super(Radius.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "radius"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", Radius.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-protocol-radius-oper:radius/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Radius.Nodes, [], name, value)


        class Node(Entity):
            """
            RADIUS operational data for a particular node
            
            .. attribute:: node_name  (key)
            
            	Node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: client
            
            	RADIUS client data
            	**type**\:  :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.Client>`
            
            .. attribute:: dead_criteria
            
            	RADIUS dead criteria information
            	**type**\:  :py:class:`DeadCriteria <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.DeadCriteria>`
            
            .. attribute:: authentication
            
            	RADIUS authentication data
            	**type**\:  :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.Authentication>`
            
            .. attribute:: accounting
            
            	RADIUS accounting data
            	**type**\:  :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.Accounting>`
            
            .. attribute:: dynamic_authorization_clients
            
            	Dynamic authorization client data
            	**type**\:  :py:class:`DynamicAuthorizationClients <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.DynamicAuthorizationClients>`
            
            .. attribute:: server_groups
            
            	RADIUS server group table
            	**type**\:  :py:class:`ServerGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.ServerGroups>`
            
            .. attribute:: dynamic_authorization
            
            	Dynamic authorization data
            	**type**\:  :py:class:`DynamicAuthorization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.DynamicAuthorization>`
            
            

            """

            _prefix = 'aaa-protocol-radius-oper'
            _revision = '2017-11-13'

            def __init__(self):
                super(Radius.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("client", ("client", Radius.Nodes.Node.Client)), ("dead-criteria", ("dead_criteria", Radius.Nodes.Node.DeadCriteria)), ("authentication", ("authentication", Radius.Nodes.Node.Authentication)), ("accounting", ("accounting", Radius.Nodes.Node.Accounting)), ("dynamic-authorization-clients", ("dynamic_authorization_clients", Radius.Nodes.Node.DynamicAuthorizationClients)), ("server-groups", ("server_groups", Radius.Nodes.Node.ServerGroups)), ("dynamic-authorization", ("dynamic_authorization", Radius.Nodes.Node.DynamicAuthorization))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.client = Radius.Nodes.Node.Client()
                self.client.parent = self
                self._children_name_map["client"] = "client"

                self.dead_criteria = Radius.Nodes.Node.DeadCriteria()
                self.dead_criteria.parent = self
                self._children_name_map["dead_criteria"] = "dead-criteria"

                self.authentication = Radius.Nodes.Node.Authentication()
                self.authentication.parent = self
                self._children_name_map["authentication"] = "authentication"

                self.accounting = Radius.Nodes.Node.Accounting()
                self.accounting.parent = self
                self._children_name_map["accounting"] = "accounting"

                self.dynamic_authorization_clients = Radius.Nodes.Node.DynamicAuthorizationClients()
                self.dynamic_authorization_clients.parent = self
                self._children_name_map["dynamic_authorization_clients"] = "dynamic-authorization-clients"

                self.server_groups = Radius.Nodes.Node.ServerGroups()
                self.server_groups.parent = self
                self._children_name_map["server_groups"] = "server-groups"

                self.dynamic_authorization = Radius.Nodes.Node.DynamicAuthorization()
                self.dynamic_authorization.parent = self
                self._children_name_map["dynamic_authorization"] = "dynamic-authorization"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-protocol-radius-oper:radius/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Radius.Nodes.Node, ['node_name'], name, value)


            class Client(Entity):
                """
                RADIUS client data
                
                .. attribute:: unknown_authentication_responses
                
                	Number of RADIUS access responses packets received from unknown addresses
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: authentication_nas_id
                
                	NAS\-Identifier of the RADIUS authentication client
                	**type**\: str
                
                .. attribute:: unknown_accounting_responses
                
                	Number of RADIUS accounting responses packets received from unknown addresses
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'aaa-protocol-radius-oper'
                _revision = '2017-11-13'

                def __init__(self):
                    super(Radius.Nodes.Node.Client, self).__init__()

                    self.yang_name = "client"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('unknown_authentication_responses', (YLeaf(YType.uint32, 'unknown-authentication-responses'), ['int'])),
                        ('authentication_nas_id', (YLeaf(YType.str, 'authentication-nas-id'), ['str'])),
                        ('unknown_accounting_responses', (YLeaf(YType.uint32, 'unknown-accounting-responses'), ['int'])),
                    ])
                    self.unknown_authentication_responses = None
                    self.authentication_nas_id = None
                    self.unknown_accounting_responses = None
                    self._segment_path = lambda: "client"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Radius.Nodes.Node.Client, [u'unknown_authentication_responses', u'authentication_nas_id', u'unknown_accounting_responses'], name, value)


            class DeadCriteria(Entity):
                """
                RADIUS dead criteria information
                
                .. attribute:: hosts
                
                	RADIUS server dead criteria host table
                	**type**\:  :py:class:`Hosts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.DeadCriteria.Hosts>`
                
                

                """

                _prefix = 'aaa-protocol-radius-oper'
                _revision = '2017-11-13'

                def __init__(self):
                    super(Radius.Nodes.Node.DeadCriteria, self).__init__()

                    self.yang_name = "dead-criteria"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("hosts", ("hosts", Radius.Nodes.Node.DeadCriteria.Hosts))])
                    self._leafs = OrderedDict()

                    self.hosts = Radius.Nodes.Node.DeadCriteria.Hosts()
                    self.hosts.parent = self
                    self._children_name_map["hosts"] = "hosts"
                    self._segment_path = lambda: "dead-criteria"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Radius.Nodes.Node.DeadCriteria, [], name, value)


                class Hosts(Entity):
                    """
                    RADIUS server dead criteria host table
                    
                    .. attribute:: host
                    
                    	RADIUS Server
                    	**type**\: list of  		 :py:class:`Host <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.DeadCriteria.Hosts.Host>`
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-oper'
                    _revision = '2017-11-13'

                    def __init__(self):
                        super(Radius.Nodes.Node.DeadCriteria.Hosts, self).__init__()

                        self.yang_name = "hosts"
                        self.yang_parent_name = "dead-criteria"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("host", ("host", Radius.Nodes.Node.DeadCriteria.Hosts.Host))])
                        self._leafs = OrderedDict()

                        self.host = YList(self)
                        self._segment_path = lambda: "hosts"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Radius.Nodes.Node.DeadCriteria.Hosts, [], name, value)


                    class Host(Entity):
                        """
                        RADIUS Server
                        
                        .. attribute:: ip_address
                        
                        	IP address of RADIUS server
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: auth_port_number
                        
                        	Authentication Port number (standard port 1645)
                        	**type**\: int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: acct_port_number
                        
                        	Accounting Port number (standard port 1646)
                        	**type**\: int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: time
                        
                        	Time in seconds
                        	**type**\:  :py:class:`Time <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.DeadCriteria.Hosts.Host.Time>`
                        
                        .. attribute:: tries
                        
                        	Number of tries
                        	**type**\:  :py:class:`Tries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.DeadCriteria.Hosts.Host.Tries>`
                        
                        

                        """

                        _prefix = 'aaa-protocol-radius-oper'
                        _revision = '2017-11-13'

                        def __init__(self):
                            super(Radius.Nodes.Node.DeadCriteria.Hosts.Host, self).__init__()

                            self.yang_name = "host"
                            self.yang_parent_name = "hosts"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("time", ("time", Radius.Nodes.Node.DeadCriteria.Hosts.Host.Time)), ("tries", ("tries", Radius.Nodes.Node.DeadCriteria.Hosts.Host.Tries))])
                            self._leafs = OrderedDict([
                                ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str','str'])),
                                ('auth_port_number', (YLeaf(YType.uint32, 'auth-port-number'), ['int'])),
                                ('acct_port_number', (YLeaf(YType.uint32, 'acct-port-number'), ['int'])),
                            ])
                            self.ip_address = None
                            self.auth_port_number = None
                            self.acct_port_number = None

                            self.time = Radius.Nodes.Node.DeadCriteria.Hosts.Host.Time()
                            self.time.parent = self
                            self._children_name_map["time"] = "time"

                            self.tries = Radius.Nodes.Node.DeadCriteria.Hosts.Host.Tries()
                            self.tries.parent = self
                            self._children_name_map["tries"] = "tries"
                            self._segment_path = lambda: "host"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Radius.Nodes.Node.DeadCriteria.Hosts.Host, ['ip_address', 'auth_port_number', 'acct_port_number'], name, value)


                        class Time(Entity):
                            """
                            Time in seconds
                            
                            .. attribute:: value
                            
                            	Value for time or tries
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: is_computed
                            
                            	True if computed; false if not
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'aaa-protocol-radius-oper'
                            _revision = '2017-11-13'

                            def __init__(self):
                                super(Radius.Nodes.Node.DeadCriteria.Hosts.Host.Time, self).__init__()

                                self.yang_name = "time"
                                self.yang_parent_name = "host"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                    ('is_computed', (YLeaf(YType.boolean, 'is-computed'), ['bool'])),
                                ])
                                self.value = None
                                self.is_computed = None
                                self._segment_path = lambda: "time"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Radius.Nodes.Node.DeadCriteria.Hosts.Host.Time, [u'value', u'is_computed'], name, value)


                        class Tries(Entity):
                            """
                            Number of tries
                            
                            .. attribute:: value
                            
                            	Value for time or tries
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: is_computed
                            
                            	True if computed; false if not
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'aaa-protocol-radius-oper'
                            _revision = '2017-11-13'

                            def __init__(self):
                                super(Radius.Nodes.Node.DeadCriteria.Hosts.Host.Tries, self).__init__()

                                self.yang_name = "tries"
                                self.yang_parent_name = "host"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                    ('is_computed', (YLeaf(YType.boolean, 'is-computed'), ['bool'])),
                                ])
                                self.value = None
                                self.is_computed = None
                                self._segment_path = lambda: "tries"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Radius.Nodes.Node.DeadCriteria.Hosts.Host.Tries, [u'value', u'is_computed'], name, value)


            class Authentication(Entity):
                """
                RADIUS authentication data
                
                .. attribute:: authentication_group
                
                	List of authentication groups
                	**type**\: list of  		 :py:class:`AuthenticationGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.Authentication.AuthenticationGroup>`
                
                

                """

                _prefix = 'aaa-protocol-radius-oper'
                _revision = '2017-11-13'

                def __init__(self):
                    super(Radius.Nodes.Node.Authentication, self).__init__()

                    self.yang_name = "authentication"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("authentication-group", ("authentication_group", Radius.Nodes.Node.Authentication.AuthenticationGroup))])
                    self._leafs = OrderedDict()

                    self.authentication_group = YList(self)
                    self._segment_path = lambda: "authentication"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Radius.Nodes.Node.Authentication, [], name, value)


                class AuthenticationGroup(Entity):
                    """
                    List of authentication groups
                    
                    .. attribute:: authentication
                    
                    	Authentication data
                    	**type**\:  :py:class:`Authentication_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.Authentication.AuthenticationGroup.Authentication_>`
                    
                    .. attribute:: server_address
                    
                    	IP address of RADIUS server
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: port
                    
                    	Authentication port number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ip_address
                    
                    	IP address buffer
                    	**type**\: str
                    
                    .. attribute:: family
                    
                    	IP address Family
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-oper'
                    _revision = '2017-11-13'

                    def __init__(self):
                        super(Radius.Nodes.Node.Authentication.AuthenticationGroup, self).__init__()

                        self.yang_name = "authentication-group"
                        self.yang_parent_name = "authentication"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("authentication", ("authentication", Radius.Nodes.Node.Authentication.AuthenticationGroup.Authentication_))])
                        self._leafs = OrderedDict([
                            ('server_address', (YLeaf(YType.str, 'server-address'), ['str'])),
                            ('port', (YLeaf(YType.uint32, 'port'), ['int'])),
                            ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str'])),
                            ('family', (YLeaf(YType.str, 'family'), ['str'])),
                        ])
                        self.server_address = None
                        self.port = None
                        self.ip_address = None
                        self.family = None

                        self.authentication = Radius.Nodes.Node.Authentication.AuthenticationGroup.Authentication_()
                        self.authentication.parent = self
                        self._children_name_map["authentication"] = "authentication"
                        self._segment_path = lambda: "authentication-group"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Radius.Nodes.Node.Authentication.AuthenticationGroup, [u'server_address', u'port', u'ip_address', u'family'], name, value)


                    class Authentication_(Entity):
                        """
                        Authentication data
                        
                        .. attribute:: access_requests
                        
                        	Number of access requests
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: pending_access_requests
                        
                        	Number of pending access requests
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: access_request_retransmits
                        
                        	Number of retransmitted access requests
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: access_accepts
                        
                        	Number of access accepts
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: access_rejects
                        
                        	Number of access rejects
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: access_challenges
                        
                        	Number of access challenges
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: access_timeouts
                        
                        	Number of access packets timed out
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_access_responses
                        
                        	Number of bad access responses
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_access_authenticators
                        
                        	Number of bad access authenticators
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unknown_access_types
                        
                        	Number of packets received with unknown type from authentication server
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dropped_access_responses
                        
                        	Number of access responses dropped
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: rtt
                        
                        	Round trip time for authentication in milliseconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: millisecond
                        
                        .. attribute:: authen_response_time
                        
                        	Average response time for authentication requests
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: authen_transaction_successess
                        
                        	Number of succeeded authentication transactions
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: authen_transaction_failure
                        
                        	Number of failed authentication transactions
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: authen_unexpected_responses
                        
                        	Number of unexpected authentication responses
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: authen_server_error_responses
                        
                        	Number of server error authentication responses
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: authen_incorrect_responses
                        
                        	Number of incorrect authentication responses
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'aaa-protocol-radius-oper'
                        _revision = '2017-11-13'

                        def __init__(self):
                            super(Radius.Nodes.Node.Authentication.AuthenticationGroup.Authentication_, self).__init__()

                            self.yang_name = "authentication"
                            self.yang_parent_name = "authentication-group"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('access_requests', (YLeaf(YType.uint32, 'access-requests'), ['int'])),
                                ('pending_access_requests', (YLeaf(YType.uint32, 'pending-access-requests'), ['int'])),
                                ('access_request_retransmits', (YLeaf(YType.uint32, 'access-request-retransmits'), ['int'])),
                                ('access_accepts', (YLeaf(YType.uint32, 'access-accepts'), ['int'])),
                                ('access_rejects', (YLeaf(YType.uint32, 'access-rejects'), ['int'])),
                                ('access_challenges', (YLeaf(YType.uint32, 'access-challenges'), ['int'])),
                                ('access_timeouts', (YLeaf(YType.uint32, 'access-timeouts'), ['int'])),
                                ('bad_access_responses', (YLeaf(YType.uint32, 'bad-access-responses'), ['int'])),
                                ('bad_access_authenticators', (YLeaf(YType.uint32, 'bad-access-authenticators'), ['int'])),
                                ('unknown_access_types', (YLeaf(YType.uint32, 'unknown-access-types'), ['int'])),
                                ('dropped_access_responses', (YLeaf(YType.uint32, 'dropped-access-responses'), ['int'])),
                                ('rtt', (YLeaf(YType.uint32, 'rtt'), ['int'])),
                                ('authen_response_time', (YLeaf(YType.uint32, 'authen-response-time'), ['int'])),
                                ('authen_transaction_successess', (YLeaf(YType.uint32, 'authen-transaction-successess'), ['int'])),
                                ('authen_transaction_failure', (YLeaf(YType.uint32, 'authen-transaction-failure'), ['int'])),
                                ('authen_unexpected_responses', (YLeaf(YType.uint32, 'authen-unexpected-responses'), ['int'])),
                                ('authen_server_error_responses', (YLeaf(YType.uint32, 'authen-server-error-responses'), ['int'])),
                                ('authen_incorrect_responses', (YLeaf(YType.uint32, 'authen-incorrect-responses'), ['int'])),
                            ])
                            self.access_requests = None
                            self.pending_access_requests = None
                            self.access_request_retransmits = None
                            self.access_accepts = None
                            self.access_rejects = None
                            self.access_challenges = None
                            self.access_timeouts = None
                            self.bad_access_responses = None
                            self.bad_access_authenticators = None
                            self.unknown_access_types = None
                            self.dropped_access_responses = None
                            self.rtt = None
                            self.authen_response_time = None
                            self.authen_transaction_successess = None
                            self.authen_transaction_failure = None
                            self.authen_unexpected_responses = None
                            self.authen_server_error_responses = None
                            self.authen_incorrect_responses = None
                            self._segment_path = lambda: "authentication"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Radius.Nodes.Node.Authentication.AuthenticationGroup.Authentication_, [u'access_requests', u'pending_access_requests', u'access_request_retransmits', u'access_accepts', u'access_rejects', u'access_challenges', u'access_timeouts', u'bad_access_responses', u'bad_access_authenticators', u'unknown_access_types', u'dropped_access_responses', u'rtt', u'authen_response_time', u'authen_transaction_successess', u'authen_transaction_failure', u'authen_unexpected_responses', u'authen_server_error_responses', u'authen_incorrect_responses'], name, value)


            class Accounting(Entity):
                """
                RADIUS accounting data
                
                .. attribute:: accounting_group
                
                	List of accounting groups
                	**type**\: list of  		 :py:class:`AccountingGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.Accounting.AccountingGroup>`
                
                

                """

                _prefix = 'aaa-protocol-radius-oper'
                _revision = '2017-11-13'

                def __init__(self):
                    super(Radius.Nodes.Node.Accounting, self).__init__()

                    self.yang_name = "accounting"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("accounting-group", ("accounting_group", Radius.Nodes.Node.Accounting.AccountingGroup))])
                    self._leafs = OrderedDict()

                    self.accounting_group = YList(self)
                    self._segment_path = lambda: "accounting"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Radius.Nodes.Node.Accounting, [], name, value)


                class AccountingGroup(Entity):
                    """
                    List of accounting groups
                    
                    .. attribute:: accounting
                    
                    	Accounting data
                    	**type**\:  :py:class:`Accounting_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.Accounting.AccountingGroup.Accounting_>`
                    
                    .. attribute:: server_address
                    
                    	IP address of RADIUS server
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: port
                    
                    	Accounting port number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ip_address
                    
                    	IP address buffer
                    	**type**\: str
                    
                    .. attribute:: family
                    
                    	IP address Family
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-oper'
                    _revision = '2017-11-13'

                    def __init__(self):
                        super(Radius.Nodes.Node.Accounting.AccountingGroup, self).__init__()

                        self.yang_name = "accounting-group"
                        self.yang_parent_name = "accounting"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("accounting", ("accounting", Radius.Nodes.Node.Accounting.AccountingGroup.Accounting_))])
                        self._leafs = OrderedDict([
                            ('server_address', (YLeaf(YType.str, 'server-address'), ['str'])),
                            ('port', (YLeaf(YType.uint32, 'port'), ['int'])),
                            ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str'])),
                            ('family', (YLeaf(YType.str, 'family'), ['str'])),
                        ])
                        self.server_address = None
                        self.port = None
                        self.ip_address = None
                        self.family = None

                        self.accounting = Radius.Nodes.Node.Accounting.AccountingGroup.Accounting_()
                        self.accounting.parent = self
                        self._children_name_map["accounting"] = "accounting"
                        self._segment_path = lambda: "accounting-group"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Radius.Nodes.Node.Accounting.AccountingGroup, [u'server_address', u'port', u'ip_address', u'family'], name, value)


                    class Accounting_(Entity):
                        """
                        Accounting data
                        
                        .. attribute:: requests
                        
                        	Number of accounting requests
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: pending_requests
                        
                        	Number of pending accounting requests
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: retransmits
                        
                        	Number of retransmitted accounting requests
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: responses
                        
                        	Number of accounting responses
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: timeouts
                        
                        	Number of accounting packets timed\-out
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_responses
                        
                        	Number of bad accounting responses
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_authenticators
                        
                        	Number of bad accounting authenticators
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unknown_packet_types
                        
                        	Number of packets received with unknown type from accounting server
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dropped_responses
                        
                        	Number of accounting responses dropped
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: rtt
                        
                        	Round trip time for accounting in milliseconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: millisecond
                        
                        .. attribute:: acct_unexpected_responses
                        
                        	Number of unexpected accounting responses
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: acct_server_error_responses
                        
                        	Number of server error accounting responses
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: acct_incorrect_responses
                        
                        	Number of incorrect accounting responses
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: acct_response_time
                        
                        	Average response time for authentication requests
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: acct_transaction_successess
                        
                        	Number of succeeded authentication transactions
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: acct_transaction_failure
                        
                        	Number of failed authentication transactions
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'aaa-protocol-radius-oper'
                        _revision = '2017-11-13'

                        def __init__(self):
                            super(Radius.Nodes.Node.Accounting.AccountingGroup.Accounting_, self).__init__()

                            self.yang_name = "accounting"
                            self.yang_parent_name = "accounting-group"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('requests', (YLeaf(YType.uint32, 'requests'), ['int'])),
                                ('pending_requests', (YLeaf(YType.uint32, 'pending-requests'), ['int'])),
                                ('retransmits', (YLeaf(YType.uint32, 'retransmits'), ['int'])),
                                ('responses', (YLeaf(YType.uint32, 'responses'), ['int'])),
                                ('timeouts', (YLeaf(YType.uint32, 'timeouts'), ['int'])),
                                ('bad_responses', (YLeaf(YType.uint32, 'bad-responses'), ['int'])),
                                ('bad_authenticators', (YLeaf(YType.uint32, 'bad-authenticators'), ['int'])),
                                ('unknown_packet_types', (YLeaf(YType.uint32, 'unknown-packet-types'), ['int'])),
                                ('dropped_responses', (YLeaf(YType.uint32, 'dropped-responses'), ['int'])),
                                ('rtt', (YLeaf(YType.uint32, 'rtt'), ['int'])),
                                ('acct_unexpected_responses', (YLeaf(YType.uint32, 'acct-unexpected-responses'), ['int'])),
                                ('acct_server_error_responses', (YLeaf(YType.uint32, 'acct-server-error-responses'), ['int'])),
                                ('acct_incorrect_responses', (YLeaf(YType.uint32, 'acct-incorrect-responses'), ['int'])),
                                ('acct_response_time', (YLeaf(YType.uint32, 'acct-response-time'), ['int'])),
                                ('acct_transaction_successess', (YLeaf(YType.uint32, 'acct-transaction-successess'), ['int'])),
                                ('acct_transaction_failure', (YLeaf(YType.uint32, 'acct-transaction-failure'), ['int'])),
                            ])
                            self.requests = None
                            self.pending_requests = None
                            self.retransmits = None
                            self.responses = None
                            self.timeouts = None
                            self.bad_responses = None
                            self.bad_authenticators = None
                            self.unknown_packet_types = None
                            self.dropped_responses = None
                            self.rtt = None
                            self.acct_unexpected_responses = None
                            self.acct_server_error_responses = None
                            self.acct_incorrect_responses = None
                            self.acct_response_time = None
                            self.acct_transaction_successess = None
                            self.acct_transaction_failure = None
                            self._segment_path = lambda: "accounting"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Radius.Nodes.Node.Accounting.AccountingGroup.Accounting_, [u'requests', u'pending_requests', u'retransmits', u'responses', u'timeouts', u'bad_responses', u'bad_authenticators', u'unknown_packet_types', u'dropped_responses', u'rtt', u'acct_unexpected_responses', u'acct_server_error_responses', u'acct_incorrect_responses', u'acct_response_time', u'acct_transaction_successess', u'acct_transaction_failure'], name, value)


            class DynamicAuthorizationClients(Entity):
                """
                Dynamic authorization client data
                
                .. attribute:: dynamic_author_client
                
                	List of dynamic author clients
                	**type**\: list of  		 :py:class:`DynamicAuthorClient <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.DynamicAuthorizationClients.DynamicAuthorClient>`
                
                

                """

                _prefix = 'aaa-protocol-radius-oper'
                _revision = '2017-11-13'

                def __init__(self):
                    super(Radius.Nodes.Node.DynamicAuthorizationClients, self).__init__()

                    self.yang_name = "dynamic-authorization-clients"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("dynamic-author-client", ("dynamic_author_client", Radius.Nodes.Node.DynamicAuthorizationClients.DynamicAuthorClient))])
                    self._leafs = OrderedDict()

                    self.dynamic_author_client = YList(self)
                    self._segment_path = lambda: "dynamic-authorization-clients"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Radius.Nodes.Node.DynamicAuthorizationClients, [], name, value)


                class DynamicAuthorClient(Entity):
                    """
                    List of dynamic author clients
                    
                    .. attribute:: client_address
                    
                    	Client's Internet address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: disc_reqs
                    
                    	Number of RADIUS Disconnect\-Requestsreceived from the client
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: disc_acks
                    
                    	Number of RADIUS Disconnect\-ACKs sent to the client
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: disc_naks
                    
                    	Number of RADIUS Disconnect\-NAKs sent to the client
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: disc_bad_auth
                    
                    	Number of RADIUS Disconnect\-Requests received from the client containing an invalid Authenticator
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: drop_disc_reqs
                    
                    	Number of RADIUS Disconnect\-Requests received from the client that were silently discarded
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: coa_reqs
                    
                    	Number of RADIUS CoA\-Requests received from the client
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: coa_acks
                    
                    	Number of RADIUS CoA\-ACKs sent to the client
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: coa_naks
                    
                    	Number of RADIUS CoA\-NAKs sent to the client
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: coa_bad_auth
                    
                    	Number of RADIUS CoA\-Requests received from the client containing an invalid Authenticator
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: drop_coa_reqs
                    
                    	Number of RADIUS CoA\-Requests received from the client that were silently discarded
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_types
                    
                    	Number of incoming packets of unknown types that were received from the client
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: internal_error
                    
                    	Number of packets dropped due to internal error
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pak_decode_fail
                    
                    	Number of packets dropped due to failure in radius packet decoding
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vrf_parse_fail_err
                    
                    	Number of requests which encountered vrf parse fail error
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_vsa_error
                    
                    	Number of requests which encountered unknown vsa error
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: send_msg_failed
                    
                    	Number of response packets which failed to be send
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: radius_to_ch
                    
                    	Number of requests sent to command handler
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ch_to_radius
                    
                    	Number of responses received from command handler
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: service_parse_fail
                    
                    	Number of requests which encountered service parse fail error
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: multi_subs_error
                    
                    	Number of requests which encountered multiple subscribers not allowed error
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: service_not_present
                    
                    	Number of requests which has missing service name attribute
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: send_to_ch_fail
                    
                    	Number of requests which failed to be sent to command handler
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vrf_name
                    
                    	VRF of RADIUS dynamic authorization client
                    	**type**\: str
                    
                    .. attribute:: addr_buf
                    
                    	Address Buffer
                    	**type**\: str
                    
                    	**length:** 0..46
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-oper'
                    _revision = '2017-11-13'

                    def __init__(self):
                        super(Radius.Nodes.Node.DynamicAuthorizationClients.DynamicAuthorClient, self).__init__()

                        self.yang_name = "dynamic-author-client"
                        self.yang_parent_name = "dynamic-authorization-clients"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('client_address', (YLeaf(YType.str, 'client-address'), ['str'])),
                            ('disc_reqs', (YLeaf(YType.uint32, 'disc-reqs'), ['int'])),
                            ('disc_acks', (YLeaf(YType.uint32, 'disc-acks'), ['int'])),
                            ('disc_naks', (YLeaf(YType.uint32, 'disc-naks'), ['int'])),
                            ('disc_bad_auth', (YLeaf(YType.uint32, 'disc-bad-auth'), ['int'])),
                            ('drop_disc_reqs', (YLeaf(YType.uint32, 'drop-disc-reqs'), ['int'])),
                            ('coa_reqs', (YLeaf(YType.uint32, 'coa-reqs'), ['int'])),
                            ('coa_acks', (YLeaf(YType.uint32, 'coa-acks'), ['int'])),
                            ('coa_naks', (YLeaf(YType.uint32, 'coa-naks'), ['int'])),
                            ('coa_bad_auth', (YLeaf(YType.uint32, 'coa-bad-auth'), ['int'])),
                            ('drop_coa_reqs', (YLeaf(YType.uint32, 'drop-coa-reqs'), ['int'])),
                            ('unknown_types', (YLeaf(YType.uint32, 'unknown-types'), ['int'])),
                            ('internal_error', (YLeaf(YType.uint32, 'internal-error'), ['int'])),
                            ('pak_decode_fail', (YLeaf(YType.uint32, 'pak-decode-fail'), ['int'])),
                            ('vrf_parse_fail_err', (YLeaf(YType.uint32, 'vrf-parse-fail-err'), ['int'])),
                            ('unknown_vsa_error', (YLeaf(YType.uint32, 'unknown-vsa-error'), ['int'])),
                            ('send_msg_failed', (YLeaf(YType.uint32, 'send-msg-failed'), ['int'])),
                            ('radius_to_ch', (YLeaf(YType.uint32, 'radius-to-ch'), ['int'])),
                            ('ch_to_radius', (YLeaf(YType.uint32, 'ch-to-radius'), ['int'])),
                            ('service_parse_fail', (YLeaf(YType.uint32, 'service-parse-fail'), ['int'])),
                            ('multi_subs_error', (YLeaf(YType.uint32, 'multi-subs-error'), ['int'])),
                            ('service_not_present', (YLeaf(YType.uint32, 'service-not-present'), ['int'])),
                            ('send_to_ch_fail', (YLeaf(YType.uint32, 'send-to-ch-fail'), ['int'])),
                            ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                            ('addr_buf', (YLeaf(YType.str, 'addr-buf'), ['str'])),
                        ])
                        self.client_address = None
                        self.disc_reqs = None
                        self.disc_acks = None
                        self.disc_naks = None
                        self.disc_bad_auth = None
                        self.drop_disc_reqs = None
                        self.coa_reqs = None
                        self.coa_acks = None
                        self.coa_naks = None
                        self.coa_bad_auth = None
                        self.drop_coa_reqs = None
                        self.unknown_types = None
                        self.internal_error = None
                        self.pak_decode_fail = None
                        self.vrf_parse_fail_err = None
                        self.unknown_vsa_error = None
                        self.send_msg_failed = None
                        self.radius_to_ch = None
                        self.ch_to_radius = None
                        self.service_parse_fail = None
                        self.multi_subs_error = None
                        self.service_not_present = None
                        self.send_to_ch_fail = None
                        self.vrf_name = None
                        self.addr_buf = None
                        self._segment_path = lambda: "dynamic-author-client"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Radius.Nodes.Node.DynamicAuthorizationClients.DynamicAuthorClient, [u'client_address', u'disc_reqs', u'disc_acks', u'disc_naks', u'disc_bad_auth', u'drop_disc_reqs', u'coa_reqs', u'coa_acks', u'coa_naks', u'coa_bad_auth', u'drop_coa_reqs', u'unknown_types', u'internal_error', u'pak_decode_fail', u'vrf_parse_fail_err', u'unknown_vsa_error', u'send_msg_failed', u'radius_to_ch', u'ch_to_radius', u'service_parse_fail', u'multi_subs_error', u'service_not_present', u'send_to_ch_fail', u'vrf_name', u'addr_buf'], name, value)


            class ServerGroups(Entity):
                """
                RADIUS server group table
                
                .. attribute:: server_group
                
                	RADIUS server group data
                	**type**\: list of  		 :py:class:`ServerGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.ServerGroups.ServerGroup>`
                
                

                """

                _prefix = 'aaa-protocol-radius-oper'
                _revision = '2017-11-13'

                def __init__(self):
                    super(Radius.Nodes.Node.ServerGroups, self).__init__()

                    self.yang_name = "server-groups"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("server-group", ("server_group", Radius.Nodes.Node.ServerGroups.ServerGroup))])
                    self._leafs = OrderedDict()

                    self.server_group = YList(self)
                    self._segment_path = lambda: "server-groups"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Radius.Nodes.Node.ServerGroups, [], name, value)


                class ServerGroup(Entity):
                    """
                    RADIUS server group data
                    
                    .. attribute:: server_group_name  (key)
                    
                    	Group name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: groups
                    
                    	Number of groups
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vrf_name
                    
                    	VRF name
                    	**type**\: str
                    
                    .. attribute:: dead_time
                    
                    	Dead time in minutes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: minute
                    
                    .. attribute:: servers
                    
                    	Number of servers
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: server_group
                    
                    	Server groups
                    	**type**\: list of  		 :py:class:`ServerGroup_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_>`
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-oper'
                    _revision = '2017-11-13'

                    def __init__(self):
                        super(Radius.Nodes.Node.ServerGroups.ServerGroup, self).__init__()

                        self.yang_name = "server-group"
                        self.yang_parent_name = "server-groups"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['server_group_name']
                        self._child_classes = OrderedDict([("server-group", ("server_group", Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_))])
                        self._leafs = OrderedDict([
                            ('server_group_name', (YLeaf(YType.str, 'server-group-name'), ['str'])),
                            ('groups', (YLeaf(YType.uint32, 'groups'), ['int'])),
                            ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                            ('dead_time', (YLeaf(YType.uint32, 'dead-time'), ['int'])),
                            ('servers', (YLeaf(YType.uint32, 'servers'), ['int'])),
                        ])
                        self.server_group_name = None
                        self.groups = None
                        self.vrf_name = None
                        self.dead_time = None
                        self.servers = None

                        self.server_group = YList(self)
                        self._segment_path = lambda: "server-group" + "[server-group-name='" + str(self.server_group_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Radius.Nodes.Node.ServerGroups.ServerGroup, ['server_group_name', u'groups', u'vrf_name', u'dead_time', u'servers'], name, value)


                    class ServerGroup_(Entity):
                        """
                        Server groups
                        
                        .. attribute:: accounting
                        
                        	Accounting data
                        	**type**\:  :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_.Accounting>`
                        
                        .. attribute:: authentication
                        
                        	Authentication data
                        	**type**\:  :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_.Authentication>`
                        
                        .. attribute:: authorization
                        
                        	Authorization data
                        	**type**\:  :py:class:`Authorization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_.Authorization>`
                        
                        .. attribute:: server_address
                        
                        	Server address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: authentication_port
                        
                        	Authentication port
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: accounting_port
                        
                        	Accounting port
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_private
                        
                        	True if private
                        	**type**\: bool
                        
                        .. attribute:: ip_address
                        
                        	IP address buffer
                        	**type**\: str
                        
                        .. attribute:: family
                        
                        	IP address Family
                        	**type**\: str
                        
                        .. attribute:: redirected_requests
                        
                        	Redirected Requests
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'aaa-protocol-radius-oper'
                        _revision = '2017-11-13'

                        def __init__(self):
                            super(Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_, self).__init__()

                            self.yang_name = "server-group"
                            self.yang_parent_name = "server-group"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("accounting", ("accounting", Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_.Accounting)), ("authentication", ("authentication", Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_.Authentication)), ("authorization", ("authorization", Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_.Authorization))])
                            self._leafs = OrderedDict([
                                ('server_address', (YLeaf(YType.str, 'server-address'), ['str'])),
                                ('authentication_port', (YLeaf(YType.uint32, 'authentication-port'), ['int'])),
                                ('accounting_port', (YLeaf(YType.uint32, 'accounting-port'), ['int'])),
                                ('is_private', (YLeaf(YType.boolean, 'is-private'), ['bool'])),
                                ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str'])),
                                ('family', (YLeaf(YType.str, 'family'), ['str'])),
                                ('redirected_requests', (YLeaf(YType.uint32, 'redirected-requests'), ['int'])),
                            ])
                            self.server_address = None
                            self.authentication_port = None
                            self.accounting_port = None
                            self.is_private = None
                            self.ip_address = None
                            self.family = None
                            self.redirected_requests = None

                            self.accounting = Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_.Accounting()
                            self.accounting.parent = self
                            self._children_name_map["accounting"] = "accounting"

                            self.authentication = Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_.Authentication()
                            self.authentication.parent = self
                            self._children_name_map["authentication"] = "authentication"

                            self.authorization = Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_.Authorization()
                            self.authorization.parent = self
                            self._children_name_map["authorization"] = "authorization"
                            self._segment_path = lambda: "server-group"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_, [u'server_address', u'authentication_port', u'accounting_port', u'is_private', u'ip_address', u'family', u'redirected_requests'], name, value)


                        class Accounting(Entity):
                            """
                            Accounting data
                            
                            .. attribute:: requests
                            
                            	Number of accounting requests
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: pending_requests
                            
                            	Number of pending accounting requests
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: retransmits
                            
                            	Number of retransmitted accounting requests
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: responses
                            
                            	Number of accounting responses
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: timeouts
                            
                            	Number of accounting packets timed\-out
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bad_responses
                            
                            	Number of bad accounting responses
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bad_authenticators
                            
                            	Number of bad accounting authenticators
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unknown_packet_types
                            
                            	Number of packets received with unknown type from accounting server
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: dropped_responses
                            
                            	Number of accounting responses dropped
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rtt
                            
                            	Round trip time for accounting in milliseconds
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: millisecond
                            
                            .. attribute:: acct_unexpected_responses
                            
                            	Number of unexpected accounting responses
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: acct_server_error_responses
                            
                            	Number of server error accounting responses
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: acct_incorrect_responses
                            
                            	Number of incorrect accounting responses
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: acct_response_time
                            
                            	Average response time for authentication requests
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: acct_transaction_successess
                            
                            	Number of succeeded authentication transactions
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: acct_transaction_failure
                            
                            	Number of failed authentication transactions
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'aaa-protocol-radius-oper'
                            _revision = '2017-11-13'

                            def __init__(self):
                                super(Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_.Accounting, self).__init__()

                                self.yang_name = "accounting"
                                self.yang_parent_name = "server-group"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('requests', (YLeaf(YType.uint32, 'requests'), ['int'])),
                                    ('pending_requests', (YLeaf(YType.uint32, 'pending-requests'), ['int'])),
                                    ('retransmits', (YLeaf(YType.uint32, 'retransmits'), ['int'])),
                                    ('responses', (YLeaf(YType.uint32, 'responses'), ['int'])),
                                    ('timeouts', (YLeaf(YType.uint32, 'timeouts'), ['int'])),
                                    ('bad_responses', (YLeaf(YType.uint32, 'bad-responses'), ['int'])),
                                    ('bad_authenticators', (YLeaf(YType.uint32, 'bad-authenticators'), ['int'])),
                                    ('unknown_packet_types', (YLeaf(YType.uint32, 'unknown-packet-types'), ['int'])),
                                    ('dropped_responses', (YLeaf(YType.uint32, 'dropped-responses'), ['int'])),
                                    ('rtt', (YLeaf(YType.uint32, 'rtt'), ['int'])),
                                    ('acct_unexpected_responses', (YLeaf(YType.uint32, 'acct-unexpected-responses'), ['int'])),
                                    ('acct_server_error_responses', (YLeaf(YType.uint32, 'acct-server-error-responses'), ['int'])),
                                    ('acct_incorrect_responses', (YLeaf(YType.uint32, 'acct-incorrect-responses'), ['int'])),
                                    ('acct_response_time', (YLeaf(YType.uint32, 'acct-response-time'), ['int'])),
                                    ('acct_transaction_successess', (YLeaf(YType.uint32, 'acct-transaction-successess'), ['int'])),
                                    ('acct_transaction_failure', (YLeaf(YType.uint32, 'acct-transaction-failure'), ['int'])),
                                ])
                                self.requests = None
                                self.pending_requests = None
                                self.retransmits = None
                                self.responses = None
                                self.timeouts = None
                                self.bad_responses = None
                                self.bad_authenticators = None
                                self.unknown_packet_types = None
                                self.dropped_responses = None
                                self.rtt = None
                                self.acct_unexpected_responses = None
                                self.acct_server_error_responses = None
                                self.acct_incorrect_responses = None
                                self.acct_response_time = None
                                self.acct_transaction_successess = None
                                self.acct_transaction_failure = None
                                self._segment_path = lambda: "accounting"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_.Accounting, [u'requests', u'pending_requests', u'retransmits', u'responses', u'timeouts', u'bad_responses', u'bad_authenticators', u'unknown_packet_types', u'dropped_responses', u'rtt', u'acct_unexpected_responses', u'acct_server_error_responses', u'acct_incorrect_responses', u'acct_response_time', u'acct_transaction_successess', u'acct_transaction_failure'], name, value)


                        class Authentication(Entity):
                            """
                            Authentication data
                            
                            .. attribute:: access_requests
                            
                            	Number of access requests
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: pending_access_requests
                            
                            	Number of pending access requests
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: access_request_retransmits
                            
                            	Number of retransmitted access requests
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: access_accepts
                            
                            	Number of access accepts
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: access_rejects
                            
                            	Number of access rejects
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: access_challenges
                            
                            	Number of access challenges
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: access_timeouts
                            
                            	Number of access packets timed out
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bad_access_responses
                            
                            	Number of bad access responses
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bad_access_authenticators
                            
                            	Number of bad access authenticators
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unknown_access_types
                            
                            	Number of packets received with unknown type from authentication server
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: dropped_access_responses
                            
                            	Number of access responses dropped
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rtt
                            
                            	Round trip time for authentication in milliseconds
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: millisecond
                            
                            .. attribute:: authen_response_time
                            
                            	Average response time for authentication requests
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: authen_transaction_successess
                            
                            	Number of succeeded authentication transactions
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: authen_transaction_failure
                            
                            	Number of failed authentication transactions
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: authen_unexpected_responses
                            
                            	Number of unexpected authentication responses
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: authen_server_error_responses
                            
                            	Number of server error authentication responses
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: authen_incorrect_responses
                            
                            	Number of incorrect authentication responses
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'aaa-protocol-radius-oper'
                            _revision = '2017-11-13'

                            def __init__(self):
                                super(Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_.Authentication, self).__init__()

                                self.yang_name = "authentication"
                                self.yang_parent_name = "server-group"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('access_requests', (YLeaf(YType.uint32, 'access-requests'), ['int'])),
                                    ('pending_access_requests', (YLeaf(YType.uint32, 'pending-access-requests'), ['int'])),
                                    ('access_request_retransmits', (YLeaf(YType.uint32, 'access-request-retransmits'), ['int'])),
                                    ('access_accepts', (YLeaf(YType.uint32, 'access-accepts'), ['int'])),
                                    ('access_rejects', (YLeaf(YType.uint32, 'access-rejects'), ['int'])),
                                    ('access_challenges', (YLeaf(YType.uint32, 'access-challenges'), ['int'])),
                                    ('access_timeouts', (YLeaf(YType.uint32, 'access-timeouts'), ['int'])),
                                    ('bad_access_responses', (YLeaf(YType.uint32, 'bad-access-responses'), ['int'])),
                                    ('bad_access_authenticators', (YLeaf(YType.uint32, 'bad-access-authenticators'), ['int'])),
                                    ('unknown_access_types', (YLeaf(YType.uint32, 'unknown-access-types'), ['int'])),
                                    ('dropped_access_responses', (YLeaf(YType.uint32, 'dropped-access-responses'), ['int'])),
                                    ('rtt', (YLeaf(YType.uint32, 'rtt'), ['int'])),
                                    ('authen_response_time', (YLeaf(YType.uint32, 'authen-response-time'), ['int'])),
                                    ('authen_transaction_successess', (YLeaf(YType.uint32, 'authen-transaction-successess'), ['int'])),
                                    ('authen_transaction_failure', (YLeaf(YType.uint32, 'authen-transaction-failure'), ['int'])),
                                    ('authen_unexpected_responses', (YLeaf(YType.uint32, 'authen-unexpected-responses'), ['int'])),
                                    ('authen_server_error_responses', (YLeaf(YType.uint32, 'authen-server-error-responses'), ['int'])),
                                    ('authen_incorrect_responses', (YLeaf(YType.uint32, 'authen-incorrect-responses'), ['int'])),
                                ])
                                self.access_requests = None
                                self.pending_access_requests = None
                                self.access_request_retransmits = None
                                self.access_accepts = None
                                self.access_rejects = None
                                self.access_challenges = None
                                self.access_timeouts = None
                                self.bad_access_responses = None
                                self.bad_access_authenticators = None
                                self.unknown_access_types = None
                                self.dropped_access_responses = None
                                self.rtt = None
                                self.authen_response_time = None
                                self.authen_transaction_successess = None
                                self.authen_transaction_failure = None
                                self.authen_unexpected_responses = None
                                self.authen_server_error_responses = None
                                self.authen_incorrect_responses = None
                                self._segment_path = lambda: "authentication"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_.Authentication, [u'access_requests', u'pending_access_requests', u'access_request_retransmits', u'access_accepts', u'access_rejects', u'access_challenges', u'access_timeouts', u'bad_access_responses', u'bad_access_authenticators', u'unknown_access_types', u'dropped_access_responses', u'rtt', u'authen_response_time', u'authen_transaction_successess', u'authen_transaction_failure', u'authen_unexpected_responses', u'authen_server_error_responses', u'authen_incorrect_responses'], name, value)


                        class Authorization(Entity):
                            """
                            Authorization data
                            
                            .. attribute:: author_requests
                            
                            	Number of access requests
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: author_request_timeouts
                            
                            	Number of access packets timed out
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: author_unexpected_responses
                            
                            	Number of unexpected authorization responses
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: author_server_error_responses
                            
                            	Number of server error authorization responses
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: author_incorrect_responses
                            
                            	Number of incorrect authorization responses
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: author_response_time
                            
                            	Average response time for authorization requests
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: author_transaction_successess
                            
                            	Number of succeeded authorization transactions
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: author_transaction_failure
                            
                            	Number of failed authorization transactions
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'aaa-protocol-radius-oper'
                            _revision = '2017-11-13'

                            def __init__(self):
                                super(Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_.Authorization, self).__init__()

                                self.yang_name = "authorization"
                                self.yang_parent_name = "server-group"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('author_requests', (YLeaf(YType.uint32, 'author-requests'), ['int'])),
                                    ('author_request_timeouts', (YLeaf(YType.uint32, 'author-request-timeouts'), ['int'])),
                                    ('author_unexpected_responses', (YLeaf(YType.uint32, 'author-unexpected-responses'), ['int'])),
                                    ('author_server_error_responses', (YLeaf(YType.uint32, 'author-server-error-responses'), ['int'])),
                                    ('author_incorrect_responses', (YLeaf(YType.uint32, 'author-incorrect-responses'), ['int'])),
                                    ('author_response_time', (YLeaf(YType.uint32, 'author-response-time'), ['int'])),
                                    ('author_transaction_successess', (YLeaf(YType.uint32, 'author-transaction-successess'), ['int'])),
                                    ('author_transaction_failure', (YLeaf(YType.uint32, 'author-transaction-failure'), ['int'])),
                                ])
                                self.author_requests = None
                                self.author_request_timeouts = None
                                self.author_unexpected_responses = None
                                self.author_server_error_responses = None
                                self.author_incorrect_responses = None
                                self.author_response_time = None
                                self.author_transaction_successess = None
                                self.author_transaction_failure = None
                                self._segment_path = lambda: "authorization"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_.Authorization, [u'author_requests', u'author_request_timeouts', u'author_unexpected_responses', u'author_server_error_responses', u'author_incorrect_responses', u'author_response_time', u'author_transaction_successess', u'author_transaction_failure'], name, value)


            class DynamicAuthorization(Entity):
                """
                Dynamic authorization data
                
                .. attribute:: disconnected_invalid_requests
                
                	Invalid disconnected requests
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: invalid_coa_requests
                
                	Invalid change of authorization requests
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: radius_context_not_found
                
                	Radius context not found
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: client_context_not_found
                
                	Client context not found
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'aaa-protocol-radius-oper'
                _revision = '2017-11-13'

                def __init__(self):
                    super(Radius.Nodes.Node.DynamicAuthorization, self).__init__()

                    self.yang_name = "dynamic-authorization"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('disconnected_invalid_requests', (YLeaf(YType.uint32, 'disconnected-invalid-requests'), ['int'])),
                        ('invalid_coa_requests', (YLeaf(YType.uint32, 'invalid-coa-requests'), ['int'])),
                        ('radius_context_not_found', (YLeaf(YType.uint32, 'radius-context-not-found'), ['int'])),
                        ('client_context_not_found', (YLeaf(YType.uint32, 'client-context-not-found'), ['int'])),
                    ])
                    self.disconnected_invalid_requests = None
                    self.invalid_coa_requests = None
                    self.radius_context_not_found = None
                    self.client_context_not_found = None
                    self._segment_path = lambda: "dynamic-authorization"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Radius.Nodes.Node.DynamicAuthorization, [u'disconnected_invalid_requests', u'invalid_coa_requests', u'radius_context_not_found', u'client_context_not_found'], name, value)

    def clone_ptr(self):
        self._top_entity = Radius()
        return self._top_entity


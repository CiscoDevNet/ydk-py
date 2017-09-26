""" Cisco_IOS_XR_aaa_protocol_radius_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR aaa\-protocol\-radius package operational data.

This module contains definitions
for the following management objects\:
  radius\: RADIUS operational data

This YANG module augments the
  Cisco\-IOS\-XR\-aaa\-locald\-oper
module with state data.

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Radius(Entity):
    """
    RADIUS operational data
    
    .. attribute:: nodes
    
    	Contains all the nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes>`
    
    

    """

    _prefix = 'aaa-protocol-radius-oper'
    _revision = '2017-05-01'

    def __init__(self):
        super(Radius, self).__init__()
        self._top_entity = None

        self.yang_name = "radius"
        self.yang_parent_name = "Cisco-IOS-XR-aaa-protocol-radius-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"nodes" : ("nodes", Radius.Nodes)}
        self._child_list_classes = {}

        self.nodes = Radius.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-aaa-protocol-radius-oper:radius"


    class Nodes(Entity):
        """
        Contains all the nodes
        
        .. attribute:: node
        
        	RADIUS operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node>`
        
        

        """

        _prefix = 'aaa-protocol-radius-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(Radius.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "radius"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"node" : ("node", Radius.Nodes.Node)}

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-protocol-radius-oper:radius/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Radius.Nodes, [], name, value)


        class Node(Entity):
            """
            RADIUS operational data for a particular node
            
            .. attribute:: node_name  <key>
            
            	Node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: accounting
            
            	RADIUS accounting data
            	**type**\:   :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.Accounting>`
            
            .. attribute:: authentication
            
            	RADIUS authentication data
            	**type**\:   :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.Authentication>`
            
            .. attribute:: client
            
            	RADIUS client data
            	**type**\:   :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.Client>`
            
            .. attribute:: dead_criteria
            
            	RADIUS dead criteria information
            	**type**\:   :py:class:`DeadCriteria <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.DeadCriteria>`
            
            .. attribute:: dynamic_authorization
            
            	Dynamic authorization data
            	**type**\:   :py:class:`DynamicAuthorization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.DynamicAuthorization>`
            
            .. attribute:: server_groups
            
            	RADIUS server group table
            	**type**\:   :py:class:`ServerGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.ServerGroups>`
            
            

            """

            _prefix = 'aaa-protocol-radius-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Radius.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"accounting" : ("accounting", Radius.Nodes.Node.Accounting), "authentication" : ("authentication", Radius.Nodes.Node.Authentication), "client" : ("client", Radius.Nodes.Node.Client), "dead-criteria" : ("dead_criteria", Radius.Nodes.Node.DeadCriteria), "dynamic-authorization" : ("dynamic_authorization", Radius.Nodes.Node.DynamicAuthorization), "server-groups" : ("server_groups", Radius.Nodes.Node.ServerGroups)}
                self._child_list_classes = {}

                self.node_name = YLeaf(YType.str, "node-name")

                self.accounting = Radius.Nodes.Node.Accounting()
                self.accounting.parent = self
                self._children_name_map["accounting"] = "accounting"
                self._children_yang_names.add("accounting")

                self.authentication = Radius.Nodes.Node.Authentication()
                self.authentication.parent = self
                self._children_name_map["authentication"] = "authentication"
                self._children_yang_names.add("authentication")

                self.client = Radius.Nodes.Node.Client()
                self.client.parent = self
                self._children_name_map["client"] = "client"
                self._children_yang_names.add("client")

                self.dead_criteria = Radius.Nodes.Node.DeadCriteria()
                self.dead_criteria.parent = self
                self._children_name_map["dead_criteria"] = "dead-criteria"
                self._children_yang_names.add("dead-criteria")

                self.dynamic_authorization = Radius.Nodes.Node.DynamicAuthorization()
                self.dynamic_authorization.parent = self
                self._children_name_map["dynamic_authorization"] = "dynamic-authorization"
                self._children_yang_names.add("dynamic-authorization")

                self.server_groups = Radius.Nodes.Node.ServerGroups()
                self.server_groups.parent = self
                self._children_name_map["server_groups"] = "server-groups"
                self._children_yang_names.add("server-groups")
                self._segment_path = lambda: "node" + "[node-name='" + self.node_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-protocol-radius-oper:radius/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Radius.Nodes.Node, ['node_name'], name, value)


            class Accounting(Entity):
                """
                RADIUS accounting data
                
                .. attribute:: accounting_group
                
                	List of accounting groups
                	**type**\: list of    :py:class:`AccountingGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.Accounting.AccountingGroup>`
                
                

                """

                _prefix = 'aaa-protocol-radius-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Radius.Nodes.Node.Accounting, self).__init__()

                    self.yang_name = "accounting"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"accounting-group" : ("accounting_group", Radius.Nodes.Node.Accounting.AccountingGroup)}

                    self.accounting_group = YList(self)
                    self._segment_path = lambda: "accounting"

                def __setattr__(self, name, value):
                    self._perform_setattr(Radius.Nodes.Node.Accounting, [], name, value)


                class AccountingGroup(Entity):
                    """
                    List of accounting groups
                    
                    .. attribute:: accounting
                    
                    	Accounting data
                    	**type**\:   :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.Accounting.AccountingGroup.Accounting>`
                    
                    .. attribute:: family
                    
                    	IP address Family
                    	**type**\:  str
                    
                    .. attribute:: ip_address
                    
                    	IP address buffer
                    	**type**\:  str
                    
                    .. attribute:: port
                    
                    	Accounting port number
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: server_address
                    
                    	IP address of RADIUS server
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Radius.Nodes.Node.Accounting.AccountingGroup, self).__init__()

                        self.yang_name = "accounting-group"
                        self.yang_parent_name = "accounting"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"accounting" : ("accounting", Radius.Nodes.Node.Accounting.AccountingGroup.Accounting)}
                        self._child_list_classes = {}

                        self.family = YLeaf(YType.str, "family")

                        self.ip_address = YLeaf(YType.str, "ip-address")

                        self.port = YLeaf(YType.uint32, "port")

                        self.server_address = YLeaf(YType.str, "server-address")

                        self.accounting = Radius.Nodes.Node.Accounting.AccountingGroup.Accounting()
                        self.accounting.parent = self
                        self._children_name_map["accounting"] = "accounting"
                        self._children_yang_names.add("accounting")
                        self._segment_path = lambda: "accounting-group"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Radius.Nodes.Node.Accounting.AccountingGroup, ['family', 'ip_address', 'port', 'server_address'], name, value)


                    class Accounting(Entity):
                        """
                        Accounting data
                        
                        .. attribute:: acct_incorrect_responses
                        
                        	Number of incorrect accounting responses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: acct_response_time
                        
                        	Average response time for authentication requests
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: acct_server_error_responses
                        
                        	Number of server error accounting responses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: acct_transaction_failure
                        
                        	Number of failed authentication transactions
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: acct_transaction_successess
                        
                        	Number of succeeded authentication transactions
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: acct_unexpected_responses
                        
                        	Number of unexpected accounting responses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_authenticators
                        
                        	Number of bad accounting authenticators
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_responses
                        
                        	Number of bad accounting responses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dropped_responses
                        
                        	Number of accounting responses dropped
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: pending_requests
                        
                        	Number of pending accounting requests
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: requests
                        
                        	Number of accounting requests
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: responses
                        
                        	Number of accounting responses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: retransmits
                        
                        	Number of retransmitted accounting requests
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: rtt
                        
                        	Round trip time for accounting in milliseconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: millisecond
                        
                        .. attribute:: timeouts
                        
                        	Number of accounting packets timed\-out
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unknown_packet_types
                        
                        	Number of packets received with unknown type from accounting server
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'aaa-protocol-radius-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Radius.Nodes.Node.Accounting.AccountingGroup.Accounting, self).__init__()

                            self.yang_name = "accounting"
                            self.yang_parent_name = "accounting-group"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.acct_incorrect_responses = YLeaf(YType.uint32, "acct-incorrect-responses")

                            self.acct_response_time = YLeaf(YType.uint32, "acct-response-time")

                            self.acct_server_error_responses = YLeaf(YType.uint32, "acct-server-error-responses")

                            self.acct_transaction_failure = YLeaf(YType.uint32, "acct-transaction-failure")

                            self.acct_transaction_successess = YLeaf(YType.uint32, "acct-transaction-successess")

                            self.acct_unexpected_responses = YLeaf(YType.uint32, "acct-unexpected-responses")

                            self.bad_authenticators = YLeaf(YType.uint32, "bad-authenticators")

                            self.bad_responses = YLeaf(YType.uint32, "bad-responses")

                            self.dropped_responses = YLeaf(YType.uint32, "dropped-responses")

                            self.pending_requests = YLeaf(YType.uint32, "pending-requests")

                            self.requests = YLeaf(YType.uint32, "requests")

                            self.responses = YLeaf(YType.uint32, "responses")

                            self.retransmits = YLeaf(YType.uint32, "retransmits")

                            self.rtt = YLeaf(YType.uint32, "rtt")

                            self.timeouts = YLeaf(YType.uint32, "timeouts")

                            self.unknown_packet_types = YLeaf(YType.uint32, "unknown-packet-types")
                            self._segment_path = lambda: "accounting"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Radius.Nodes.Node.Accounting.AccountingGroup.Accounting, ['acct_incorrect_responses', 'acct_response_time', 'acct_server_error_responses', 'acct_transaction_failure', 'acct_transaction_successess', 'acct_unexpected_responses', 'bad_authenticators', 'bad_responses', 'dropped_responses', 'pending_requests', 'requests', 'responses', 'retransmits', 'rtt', 'timeouts', 'unknown_packet_types'], name, value)


            class Authentication(Entity):
                """
                RADIUS authentication data
                
                .. attribute:: authentication_group
                
                	List of authentication groups
                	**type**\: list of    :py:class:`AuthenticationGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.Authentication.AuthenticationGroup>`
                
                

                """

                _prefix = 'aaa-protocol-radius-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Radius.Nodes.Node.Authentication, self).__init__()

                    self.yang_name = "authentication"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"authentication-group" : ("authentication_group", Radius.Nodes.Node.Authentication.AuthenticationGroup)}

                    self.authentication_group = YList(self)
                    self._segment_path = lambda: "authentication"

                def __setattr__(self, name, value):
                    self._perform_setattr(Radius.Nodes.Node.Authentication, [], name, value)


                class AuthenticationGroup(Entity):
                    """
                    List of authentication groups
                    
                    .. attribute:: authentication
                    
                    	Authentication data
                    	**type**\:   :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.Authentication.AuthenticationGroup.Authentication>`
                    
                    .. attribute:: family
                    
                    	IP address Family
                    	**type**\:  str
                    
                    .. attribute:: ip_address
                    
                    	IP address buffer
                    	**type**\:  str
                    
                    .. attribute:: port
                    
                    	Authentication port number
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: server_address
                    
                    	IP address of RADIUS server
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Radius.Nodes.Node.Authentication.AuthenticationGroup, self).__init__()

                        self.yang_name = "authentication-group"
                        self.yang_parent_name = "authentication"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"authentication" : ("authentication", Radius.Nodes.Node.Authentication.AuthenticationGroup.Authentication)}
                        self._child_list_classes = {}

                        self.family = YLeaf(YType.str, "family")

                        self.ip_address = YLeaf(YType.str, "ip-address")

                        self.port = YLeaf(YType.uint32, "port")

                        self.server_address = YLeaf(YType.str, "server-address")

                        self.authentication = Radius.Nodes.Node.Authentication.AuthenticationGroup.Authentication()
                        self.authentication.parent = self
                        self._children_name_map["authentication"] = "authentication"
                        self._children_yang_names.add("authentication")
                        self._segment_path = lambda: "authentication-group"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Radius.Nodes.Node.Authentication.AuthenticationGroup, ['family', 'ip_address', 'port', 'server_address'], name, value)


                    class Authentication(Entity):
                        """
                        Authentication data
                        
                        .. attribute:: access_accepts
                        
                        	Number of access accepts
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: access_challenges
                        
                        	Number of access challenges
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: access_rejects
                        
                        	Number of access rejects
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: access_request_retransmits
                        
                        	Number of retransmitted access requests
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: access_requests
                        
                        	Number of access requests
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: access_timeouts
                        
                        	Number of access packets timed out
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: authen_incorrect_responses
                        
                        	Number of incorrect authentication responses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: authen_response_time
                        
                        	Average response time for authentication requests
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: authen_server_error_responses
                        
                        	Number of server error authentication responses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: authen_transaction_failure
                        
                        	Number of failed authentication transactions
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: authen_transaction_successess
                        
                        	Number of succeeded authentication transactions
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: authen_unexpected_responses
                        
                        	Number of unexpected authentication responses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_access_authenticators
                        
                        	Number of bad access authenticators
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_access_responses
                        
                        	Number of bad access responses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dropped_access_responses
                        
                        	Number of access responses dropped
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: pending_access_requests
                        
                        	Number of pending access requests
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: rtt
                        
                        	Round trip time for authentication in milliseconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: millisecond
                        
                        .. attribute:: unknown_access_types
                        
                        	Number of packets received with unknown type from authentication server
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'aaa-protocol-radius-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Radius.Nodes.Node.Authentication.AuthenticationGroup.Authentication, self).__init__()

                            self.yang_name = "authentication"
                            self.yang_parent_name = "authentication-group"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.access_accepts = YLeaf(YType.uint32, "access-accepts")

                            self.access_challenges = YLeaf(YType.uint32, "access-challenges")

                            self.access_rejects = YLeaf(YType.uint32, "access-rejects")

                            self.access_request_retransmits = YLeaf(YType.uint32, "access-request-retransmits")

                            self.access_requests = YLeaf(YType.uint32, "access-requests")

                            self.access_timeouts = YLeaf(YType.uint32, "access-timeouts")

                            self.authen_incorrect_responses = YLeaf(YType.uint32, "authen-incorrect-responses")

                            self.authen_response_time = YLeaf(YType.uint32, "authen-response-time")

                            self.authen_server_error_responses = YLeaf(YType.uint32, "authen-server-error-responses")

                            self.authen_transaction_failure = YLeaf(YType.uint32, "authen-transaction-failure")

                            self.authen_transaction_successess = YLeaf(YType.uint32, "authen-transaction-successess")

                            self.authen_unexpected_responses = YLeaf(YType.uint32, "authen-unexpected-responses")

                            self.bad_access_authenticators = YLeaf(YType.uint32, "bad-access-authenticators")

                            self.bad_access_responses = YLeaf(YType.uint32, "bad-access-responses")

                            self.dropped_access_responses = YLeaf(YType.uint32, "dropped-access-responses")

                            self.pending_access_requests = YLeaf(YType.uint32, "pending-access-requests")

                            self.rtt = YLeaf(YType.uint32, "rtt")

                            self.unknown_access_types = YLeaf(YType.uint32, "unknown-access-types")
                            self._segment_path = lambda: "authentication"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Radius.Nodes.Node.Authentication.AuthenticationGroup.Authentication, ['access_accepts', 'access_challenges', 'access_rejects', 'access_request_retransmits', 'access_requests', 'access_timeouts', 'authen_incorrect_responses', 'authen_response_time', 'authen_server_error_responses', 'authen_transaction_failure', 'authen_transaction_successess', 'authen_unexpected_responses', 'bad_access_authenticators', 'bad_access_responses', 'dropped_access_responses', 'pending_access_requests', 'rtt', 'unknown_access_types'], name, value)


            class Client(Entity):
                """
                RADIUS client data
                
                .. attribute:: authentication_nas_id
                
                	NAS\-Identifier of the RADIUS authentication client
                	**type**\:  str
                
                .. attribute:: unknown_accounting_responses
                
                	Number of RADIUS accounting responses packets received from unknown addresses
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: unknown_authentication_responses
                
                	Number of RADIUS access responses packets received from unknown addresses
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'aaa-protocol-radius-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Radius.Nodes.Node.Client, self).__init__()

                    self.yang_name = "client"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.authentication_nas_id = YLeaf(YType.str, "authentication-nas-id")

                    self.unknown_accounting_responses = YLeaf(YType.uint32, "unknown-accounting-responses")

                    self.unknown_authentication_responses = YLeaf(YType.uint32, "unknown-authentication-responses")
                    self._segment_path = lambda: "client"

                def __setattr__(self, name, value):
                    self._perform_setattr(Radius.Nodes.Node.Client, ['authentication_nas_id', 'unknown_accounting_responses', 'unknown_authentication_responses'], name, value)


            class DeadCriteria(Entity):
                """
                RADIUS dead criteria information
                
                .. attribute:: hosts
                
                	RADIUS server dead criteria host table
                	**type**\:   :py:class:`Hosts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.DeadCriteria.Hosts>`
                
                

                """

                _prefix = 'aaa-protocol-radius-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Radius.Nodes.Node.DeadCriteria, self).__init__()

                    self.yang_name = "dead-criteria"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"hosts" : ("hosts", Radius.Nodes.Node.DeadCriteria.Hosts)}
                    self._child_list_classes = {}

                    self.hosts = Radius.Nodes.Node.DeadCriteria.Hosts()
                    self.hosts.parent = self
                    self._children_name_map["hosts"] = "hosts"
                    self._children_yang_names.add("hosts")
                    self._segment_path = lambda: "dead-criteria"


                class Hosts(Entity):
                    """
                    RADIUS server dead criteria host table
                    
                    .. attribute:: host
                    
                    	RADIUS Server
                    	**type**\: list of    :py:class:`Host <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.DeadCriteria.Hosts.Host>`
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Radius.Nodes.Node.DeadCriteria.Hosts, self).__init__()

                        self.yang_name = "hosts"
                        self.yang_parent_name = "dead-criteria"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"host" : ("host", Radius.Nodes.Node.DeadCriteria.Hosts.Host)}

                        self.host = YList(self)
                        self._segment_path = lambda: "hosts"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Radius.Nodes.Node.DeadCriteria.Hosts, [], name, value)


                    class Host(Entity):
                        """
                        RADIUS Server
                        
                        .. attribute:: acct_port_number
                        
                        	Accounting Port number (standard port 1646)
                        	**type**\:  int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: auth_port_number
                        
                        	Authentication Port number (standard port 1645)
                        	**type**\:  int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: ip_address
                        
                        	IP address of RADIUS server
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: time
                        
                        	Time in seconds
                        	**type**\:   :py:class:`Time <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.DeadCriteria.Hosts.Host.Time>`
                        
                        .. attribute:: tries
                        
                        	Number of tries
                        	**type**\:   :py:class:`Tries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.DeadCriteria.Hosts.Host.Tries>`
                        
                        

                        """

                        _prefix = 'aaa-protocol-radius-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Radius.Nodes.Node.DeadCriteria.Hosts.Host, self).__init__()

                            self.yang_name = "host"
                            self.yang_parent_name = "hosts"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"time" : ("time", Radius.Nodes.Node.DeadCriteria.Hosts.Host.Time), "tries" : ("tries", Radius.Nodes.Node.DeadCriteria.Hosts.Host.Tries)}
                            self._child_list_classes = {}

                            self.acct_port_number = YLeaf(YType.uint32, "acct-port-number")

                            self.auth_port_number = YLeaf(YType.uint32, "auth-port-number")

                            self.ip_address = YLeaf(YType.str, "ip-address")

                            self.time = Radius.Nodes.Node.DeadCriteria.Hosts.Host.Time()
                            self.time.parent = self
                            self._children_name_map["time"] = "time"
                            self._children_yang_names.add("time")

                            self.tries = Radius.Nodes.Node.DeadCriteria.Hosts.Host.Tries()
                            self.tries.parent = self
                            self._children_name_map["tries"] = "tries"
                            self._children_yang_names.add("tries")
                            self._segment_path = lambda: "host"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Radius.Nodes.Node.DeadCriteria.Hosts.Host, ['acct_port_number', 'auth_port_number', 'ip_address'], name, value)


                        class Time(Entity):
                            """
                            Time in seconds
                            
                            .. attribute:: is_computed
                            
                            	True if computed; false if not
                            	**type**\:  bool
                            
                            .. attribute:: value
                            
                            	Value for time or tries
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'aaa-protocol-radius-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Radius.Nodes.Node.DeadCriteria.Hosts.Host.Time, self).__init__()

                                self.yang_name = "time"
                                self.yang_parent_name = "host"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.is_computed = YLeaf(YType.boolean, "is-computed")

                                self.value = YLeaf(YType.uint32, "value")
                                self._segment_path = lambda: "time"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Radius.Nodes.Node.DeadCriteria.Hosts.Host.Time, ['is_computed', 'value'], name, value)


                        class Tries(Entity):
                            """
                            Number of tries
                            
                            .. attribute:: is_computed
                            
                            	True if computed; false if not
                            	**type**\:  bool
                            
                            .. attribute:: value
                            
                            	Value for time or tries
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'aaa-protocol-radius-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Radius.Nodes.Node.DeadCriteria.Hosts.Host.Tries, self).__init__()

                                self.yang_name = "tries"
                                self.yang_parent_name = "host"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.is_computed = YLeaf(YType.boolean, "is-computed")

                                self.value = YLeaf(YType.uint32, "value")
                                self._segment_path = lambda: "tries"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Radius.Nodes.Node.DeadCriteria.Hosts.Host.Tries, ['is_computed', 'value'], name, value)


            class DynamicAuthorization(Entity):
                """
                Dynamic authorization data
                
                .. attribute:: disconnected_invalid_requests
                
                	Invalid disconnected requests
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: invalid_coa_requests
                
                	Invalid change of authorization requests
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'aaa-protocol-radius-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Radius.Nodes.Node.DynamicAuthorization, self).__init__()

                    self.yang_name = "dynamic-authorization"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.disconnected_invalid_requests = YLeaf(YType.uint32, "disconnected-invalid-requests")

                    self.invalid_coa_requests = YLeaf(YType.uint32, "invalid-coa-requests")
                    self._segment_path = lambda: "dynamic-authorization"

                def __setattr__(self, name, value):
                    self._perform_setattr(Radius.Nodes.Node.DynamicAuthorization, ['disconnected_invalid_requests', 'invalid_coa_requests'], name, value)


            class ServerGroups(Entity):
                """
                RADIUS server group table
                
                .. attribute:: server_group
                
                	RADIUS server group data
                	**type**\: list of    :py:class:`ServerGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.ServerGroups.ServerGroup>`
                
                

                """

                _prefix = 'aaa-protocol-radius-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Radius.Nodes.Node.ServerGroups, self).__init__()

                    self.yang_name = "server-groups"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"server-group" : ("server_group", Radius.Nodes.Node.ServerGroups.ServerGroup)}

                    self.server_group = YList(self)
                    self._segment_path = lambda: "server-groups"

                def __setattr__(self, name, value):
                    self._perform_setattr(Radius.Nodes.Node.ServerGroups, [], name, value)


                class ServerGroup(Entity):
                    """
                    RADIUS server group data
                    
                    .. attribute:: server_group_name  <key>
                    
                    	Group name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: dead_time
                    
                    	Dead time in minutes
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: minute
                    
                    .. attribute:: groups
                    
                    	Number of groups
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: server_group
                    
                    	Server groups
                    	**type**\: list of    :py:class:`ServerGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup>`
                    
                    .. attribute:: servers
                    
                    	Number of servers
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vrf_name
                    
                    	VRF name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Radius.Nodes.Node.ServerGroups.ServerGroup, self).__init__()

                        self.yang_name = "server-group"
                        self.yang_parent_name = "server-groups"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"server-group" : ("server_group", Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup)}

                        self.server_group_name = YLeaf(YType.str, "server-group-name")

                        self.dead_time = YLeaf(YType.uint32, "dead-time")

                        self.groups = YLeaf(YType.uint32, "groups")

                        self.servers = YLeaf(YType.uint32, "servers")

                        self.vrf_name = YLeaf(YType.str, "vrf-name")

                        self.server_group = YList(self)
                        self._segment_path = lambda: "server-group" + "[server-group-name='" + self.server_group_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Radius.Nodes.Node.ServerGroups.ServerGroup, ['server_group_name', 'dead_time', 'groups', 'servers', 'vrf_name'], name, value)


                    class ServerGroup(Entity):
                        """
                        Server groups
                        
                        .. attribute:: accounting
                        
                        	Accounting data
                        	**type**\:   :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup.Accounting>`
                        
                        .. attribute:: accounting_port
                        
                        	Accounting port
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: authentication
                        
                        	Authentication data
                        	**type**\:   :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup.Authentication>`
                        
                        .. attribute:: authentication_port
                        
                        	Authentication port
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: authorization
                        
                        	Authorization data
                        	**type**\:   :py:class:`Authorization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup.Authorization>`
                        
                        .. attribute:: family
                        
                        	IP address Family
                        	**type**\:  str
                        
                        .. attribute:: ip_address
                        
                        	IP address buffer
                        	**type**\:  str
                        
                        .. attribute:: is_private
                        
                        	True if private
                        	**type**\:  bool
                        
                        .. attribute:: server_address
                        
                        	Server address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'aaa-protocol-radius-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup, self).__init__()

                            self.yang_name = "server-group"
                            self.yang_parent_name = "server-group"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"accounting" : ("accounting", Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup.Accounting), "authentication" : ("authentication", Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup.Authentication), "authorization" : ("authorization", Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup.Authorization)}
                            self._child_list_classes = {}

                            self.accounting_port = YLeaf(YType.uint32, "accounting-port")

                            self.authentication_port = YLeaf(YType.uint32, "authentication-port")

                            self.family = YLeaf(YType.str, "family")

                            self.ip_address = YLeaf(YType.str, "ip-address")

                            self.is_private = YLeaf(YType.boolean, "is-private")

                            self.server_address = YLeaf(YType.str, "server-address")

                            self.accounting = Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup.Accounting()
                            self.accounting.parent = self
                            self._children_name_map["accounting"] = "accounting"
                            self._children_yang_names.add("accounting")

                            self.authentication = Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup.Authentication()
                            self.authentication.parent = self
                            self._children_name_map["authentication"] = "authentication"
                            self._children_yang_names.add("authentication")

                            self.authorization = Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup.Authorization()
                            self.authorization.parent = self
                            self._children_name_map["authorization"] = "authorization"
                            self._children_yang_names.add("authorization")
                            self._segment_path = lambda: "server-group"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup, ['accounting_port', 'authentication_port', 'family', 'ip_address', 'is_private', 'server_address'], name, value)


                        class Accounting(Entity):
                            """
                            Accounting data
                            
                            .. attribute:: acct_incorrect_responses
                            
                            	Number of incorrect accounting responses
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: acct_response_time
                            
                            	Average response time for authentication requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: acct_server_error_responses
                            
                            	Number of server error accounting responses
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: acct_transaction_failure
                            
                            	Number of failed authentication transactions
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: acct_transaction_successess
                            
                            	Number of succeeded authentication transactions
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: acct_unexpected_responses
                            
                            	Number of unexpected accounting responses
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bad_authenticators
                            
                            	Number of bad accounting authenticators
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bad_responses
                            
                            	Number of bad accounting responses
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: dropped_responses
                            
                            	Number of accounting responses dropped
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: pending_requests
                            
                            	Number of pending accounting requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: requests
                            
                            	Number of accounting requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: responses
                            
                            	Number of accounting responses
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: retransmits
                            
                            	Number of retransmitted accounting requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rtt
                            
                            	Round trip time for accounting in milliseconds
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: millisecond
                            
                            .. attribute:: timeouts
                            
                            	Number of accounting packets timed\-out
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unknown_packet_types
                            
                            	Number of packets received with unknown type from accounting server
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'aaa-protocol-radius-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup.Accounting, self).__init__()

                                self.yang_name = "accounting"
                                self.yang_parent_name = "server-group"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.acct_incorrect_responses = YLeaf(YType.uint32, "acct-incorrect-responses")

                                self.acct_response_time = YLeaf(YType.uint32, "acct-response-time")

                                self.acct_server_error_responses = YLeaf(YType.uint32, "acct-server-error-responses")

                                self.acct_transaction_failure = YLeaf(YType.uint32, "acct-transaction-failure")

                                self.acct_transaction_successess = YLeaf(YType.uint32, "acct-transaction-successess")

                                self.acct_unexpected_responses = YLeaf(YType.uint32, "acct-unexpected-responses")

                                self.bad_authenticators = YLeaf(YType.uint32, "bad-authenticators")

                                self.bad_responses = YLeaf(YType.uint32, "bad-responses")

                                self.dropped_responses = YLeaf(YType.uint32, "dropped-responses")

                                self.pending_requests = YLeaf(YType.uint32, "pending-requests")

                                self.requests = YLeaf(YType.uint32, "requests")

                                self.responses = YLeaf(YType.uint32, "responses")

                                self.retransmits = YLeaf(YType.uint32, "retransmits")

                                self.rtt = YLeaf(YType.uint32, "rtt")

                                self.timeouts = YLeaf(YType.uint32, "timeouts")

                                self.unknown_packet_types = YLeaf(YType.uint32, "unknown-packet-types")
                                self._segment_path = lambda: "accounting"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup.Accounting, ['acct_incorrect_responses', 'acct_response_time', 'acct_server_error_responses', 'acct_transaction_failure', 'acct_transaction_successess', 'acct_unexpected_responses', 'bad_authenticators', 'bad_responses', 'dropped_responses', 'pending_requests', 'requests', 'responses', 'retransmits', 'rtt', 'timeouts', 'unknown_packet_types'], name, value)


                        class Authentication(Entity):
                            """
                            Authentication data
                            
                            .. attribute:: access_accepts
                            
                            	Number of access accepts
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: access_challenges
                            
                            	Number of access challenges
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: access_rejects
                            
                            	Number of access rejects
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: access_request_retransmits
                            
                            	Number of retransmitted access requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: access_requests
                            
                            	Number of access requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: access_timeouts
                            
                            	Number of access packets timed out
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: authen_incorrect_responses
                            
                            	Number of incorrect authentication responses
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: authen_response_time
                            
                            	Average response time for authentication requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: authen_server_error_responses
                            
                            	Number of server error authentication responses
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: authen_transaction_failure
                            
                            	Number of failed authentication transactions
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: authen_transaction_successess
                            
                            	Number of succeeded authentication transactions
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: authen_unexpected_responses
                            
                            	Number of unexpected authentication responses
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bad_access_authenticators
                            
                            	Number of bad access authenticators
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bad_access_responses
                            
                            	Number of bad access responses
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: dropped_access_responses
                            
                            	Number of access responses dropped
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: pending_access_requests
                            
                            	Number of pending access requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rtt
                            
                            	Round trip time for authentication in milliseconds
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: millisecond
                            
                            .. attribute:: unknown_access_types
                            
                            	Number of packets received with unknown type from authentication server
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'aaa-protocol-radius-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup.Authentication, self).__init__()

                                self.yang_name = "authentication"
                                self.yang_parent_name = "server-group"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.access_accepts = YLeaf(YType.uint32, "access-accepts")

                                self.access_challenges = YLeaf(YType.uint32, "access-challenges")

                                self.access_rejects = YLeaf(YType.uint32, "access-rejects")

                                self.access_request_retransmits = YLeaf(YType.uint32, "access-request-retransmits")

                                self.access_requests = YLeaf(YType.uint32, "access-requests")

                                self.access_timeouts = YLeaf(YType.uint32, "access-timeouts")

                                self.authen_incorrect_responses = YLeaf(YType.uint32, "authen-incorrect-responses")

                                self.authen_response_time = YLeaf(YType.uint32, "authen-response-time")

                                self.authen_server_error_responses = YLeaf(YType.uint32, "authen-server-error-responses")

                                self.authen_transaction_failure = YLeaf(YType.uint32, "authen-transaction-failure")

                                self.authen_transaction_successess = YLeaf(YType.uint32, "authen-transaction-successess")

                                self.authen_unexpected_responses = YLeaf(YType.uint32, "authen-unexpected-responses")

                                self.bad_access_authenticators = YLeaf(YType.uint32, "bad-access-authenticators")

                                self.bad_access_responses = YLeaf(YType.uint32, "bad-access-responses")

                                self.dropped_access_responses = YLeaf(YType.uint32, "dropped-access-responses")

                                self.pending_access_requests = YLeaf(YType.uint32, "pending-access-requests")

                                self.rtt = YLeaf(YType.uint32, "rtt")

                                self.unknown_access_types = YLeaf(YType.uint32, "unknown-access-types")
                                self._segment_path = lambda: "authentication"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup.Authentication, ['access_accepts', 'access_challenges', 'access_rejects', 'access_request_retransmits', 'access_requests', 'access_timeouts', 'authen_incorrect_responses', 'authen_response_time', 'authen_server_error_responses', 'authen_transaction_failure', 'authen_transaction_successess', 'authen_unexpected_responses', 'bad_access_authenticators', 'bad_access_responses', 'dropped_access_responses', 'pending_access_requests', 'rtt', 'unknown_access_types'], name, value)


                        class Authorization(Entity):
                            """
                            Authorization data
                            
                            .. attribute:: author_incorrect_responses
                            
                            	Number of incorrect authorization responses
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: author_request_timeouts
                            
                            	Number of access packets timed out
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: author_requests
                            
                            	Number of access requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: author_response_time
                            
                            	Average response time for authorization requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: author_server_error_responses
                            
                            	Number of server error authorization responses
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: author_transaction_failure
                            
                            	Number of failed authorization transactions
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: author_transaction_successess
                            
                            	Number of succeeded authorization transactions
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: author_unexpected_responses
                            
                            	Number of unexpected authorization responses
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'aaa-protocol-radius-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup.Authorization, self).__init__()

                                self.yang_name = "authorization"
                                self.yang_parent_name = "server-group"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.author_incorrect_responses = YLeaf(YType.uint32, "author-incorrect-responses")

                                self.author_request_timeouts = YLeaf(YType.uint32, "author-request-timeouts")

                                self.author_requests = YLeaf(YType.uint32, "author-requests")

                                self.author_response_time = YLeaf(YType.uint32, "author-response-time")

                                self.author_server_error_responses = YLeaf(YType.uint32, "author-server-error-responses")

                                self.author_transaction_failure = YLeaf(YType.uint32, "author-transaction-failure")

                                self.author_transaction_successess = YLeaf(YType.uint32, "author-transaction-successess")

                                self.author_unexpected_responses = YLeaf(YType.uint32, "author-unexpected-responses")
                                self._segment_path = lambda: "authorization"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup.Authorization, ['author_incorrect_responses', 'author_request_timeouts', 'author_requests', 'author_response_time', 'author_server_error_responses', 'author_transaction_failure', 'author_transaction_successess', 'author_unexpected_responses'], name, value)

    def clone_ptr(self):
        self._top_entity = Radius()
        return self._top_entity


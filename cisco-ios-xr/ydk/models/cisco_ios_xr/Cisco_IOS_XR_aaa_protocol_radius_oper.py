""" Cisco_IOS_XR_aaa_protocol_radius_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR aaa\-protocol\-radius package operational data.

This module contains definitions
for the following management objects\:
  radius\: RADIUS operational data

This YANG module augments the
  Cisco\-IOS\-XR\-aaa\-locald\-oper
module with state data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Radius(object):
    """
    RADIUS operational data
    
    .. attribute:: nodes
    
    	Contains all the nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes>`
    
    

    """

    _prefix = 'aaa-protocol-radius-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = Radius.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        Contains all the nodes
        
        .. attribute:: node
        
        	RADIUS operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node>`
        
        

        """

        _prefix = 'aaa-protocol-radius-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
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
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.accounting = Radius.Nodes.Node.Accounting()
                self.accounting.parent = self
                self.authentication = Radius.Nodes.Node.Authentication()
                self.authentication.parent = self
                self.client = Radius.Nodes.Node.Client()
                self.client.parent = self
                self.dead_criteria = Radius.Nodes.Node.DeadCriteria()
                self.dead_criteria.parent = self
                self.dynamic_authorization = Radius.Nodes.Node.DynamicAuthorization()
                self.dynamic_authorization.parent = self
                self.server_groups = Radius.Nodes.Node.ServerGroups()
                self.server_groups.parent = self


            class Client(object):
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
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.authentication_nas_id = None
                    self.unknown_accounting_responses = None
                    self.unknown_authentication_responses = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-aaa-protocol-radius-oper:client'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.authentication_nas_id is not None:
                        return True

                    if self.unknown_accounting_responses is not None:
                        return True

                    if self.unknown_authentication_responses is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_protocol_radius_oper as meta
                    return meta._meta_table['Radius.Nodes.Node.Client']['meta_info']


            class DeadCriteria(object):
                """
                RADIUS dead criteria information
                
                .. attribute:: hosts
                
                	RADIUS server dead criteria host table
                	**type**\:   :py:class:`Hosts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.DeadCriteria.Hosts>`
                
                

                """

                _prefix = 'aaa-protocol-radius-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.hosts = Radius.Nodes.Node.DeadCriteria.Hosts()
                    self.hosts.parent = self


                class Hosts(object):
                    """
                    RADIUS server dead criteria host table
                    
                    .. attribute:: host
                    
                    	RADIUS Server
                    	**type**\: list of    :py:class:`Host <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.DeadCriteria.Hosts.Host>`
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.host = YList()
                        self.host.parent = self
                        self.host.name = 'host'


                    class Host(object):
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
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.acct_port_number = None
                            self.auth_port_number = None
                            self.ip_address = None
                            self.time = Radius.Nodes.Node.DeadCriteria.Hosts.Host.Time()
                            self.time.parent = self
                            self.tries = Radius.Nodes.Node.DeadCriteria.Hosts.Host.Tries()
                            self.tries.parent = self


                        class Time(object):
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
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.is_computed = None
                                self.value = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-aaa-protocol-radius-oper:time'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.is_computed is not None:
                                    return True

                                if self.value is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_protocol_radius_oper as meta
                                return meta._meta_table['Radius.Nodes.Node.DeadCriteria.Hosts.Host.Time']['meta_info']


                        class Tries(object):
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
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.is_computed = None
                                self.value = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-aaa-protocol-radius-oper:tries'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.is_computed is not None:
                                    return True

                                if self.value is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_protocol_radius_oper as meta
                                return meta._meta_table['Radius.Nodes.Node.DeadCriteria.Hosts.Host.Tries']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-aaa-protocol-radius-oper:host'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.acct_port_number is not None:
                                return True

                            if self.auth_port_number is not None:
                                return True

                            if self.ip_address is not None:
                                return True

                            if self.time is not None and self.time._has_data():
                                return True

                            if self.tries is not None and self.tries._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_protocol_radius_oper as meta
                            return meta._meta_table['Radius.Nodes.Node.DeadCriteria.Hosts.Host']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-aaa-protocol-radius-oper:hosts'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.host is not None:
                            for child_ref in self.host:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_protocol_radius_oper as meta
                        return meta._meta_table['Radius.Nodes.Node.DeadCriteria.Hosts']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-aaa-protocol-radius-oper:dead-criteria'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.hosts is not None and self.hosts._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_protocol_radius_oper as meta
                    return meta._meta_table['Radius.Nodes.Node.DeadCriteria']['meta_info']


            class Authentication(object):
                """
                RADIUS authentication data
                
                .. attribute:: authentication_group
                
                	List of authentication groups
                	**type**\: list of    :py:class:`AuthenticationGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.Authentication.AuthenticationGroup>`
                
                

                """

                _prefix = 'aaa-protocol-radius-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.authentication_group = YList()
                    self.authentication_group.parent = self
                    self.authentication_group.name = 'authentication_group'


                class AuthenticationGroup(object):
                    """
                    List of authentication groups
                    
                    .. attribute:: authentication
                    
                    	Authentication data
                    	**type**\:   :py:class:`Authentication_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.Authentication.AuthenticationGroup.Authentication_>`
                    
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
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.authentication = Radius.Nodes.Node.Authentication.AuthenticationGroup.Authentication_()
                        self.authentication.parent = self
                        self.family = None
                        self.ip_address = None
                        self.port = None
                        self.server_address = None


                    class Authentication_(object):
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
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.access_accepts = None
                            self.access_challenges = None
                            self.access_rejects = None
                            self.access_request_retransmits = None
                            self.access_requests = None
                            self.access_timeouts = None
                            self.authen_incorrect_responses = None
                            self.authen_response_time = None
                            self.authen_server_error_responses = None
                            self.authen_transaction_failure = None
                            self.authen_transaction_successess = None
                            self.authen_unexpected_responses = None
                            self.bad_access_authenticators = None
                            self.bad_access_responses = None
                            self.dropped_access_responses = None
                            self.pending_access_requests = None
                            self.rtt = None
                            self.unknown_access_types = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-aaa-protocol-radius-oper:authentication'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.access_accepts is not None:
                                return True

                            if self.access_challenges is not None:
                                return True

                            if self.access_rejects is not None:
                                return True

                            if self.access_request_retransmits is not None:
                                return True

                            if self.access_requests is not None:
                                return True

                            if self.access_timeouts is not None:
                                return True

                            if self.authen_incorrect_responses is not None:
                                return True

                            if self.authen_response_time is not None:
                                return True

                            if self.authen_server_error_responses is not None:
                                return True

                            if self.authen_transaction_failure is not None:
                                return True

                            if self.authen_transaction_successess is not None:
                                return True

                            if self.authen_unexpected_responses is not None:
                                return True

                            if self.bad_access_authenticators is not None:
                                return True

                            if self.bad_access_responses is not None:
                                return True

                            if self.dropped_access_responses is not None:
                                return True

                            if self.pending_access_requests is not None:
                                return True

                            if self.rtt is not None:
                                return True

                            if self.unknown_access_types is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_protocol_radius_oper as meta
                            return meta._meta_table['Radius.Nodes.Node.Authentication.AuthenticationGroup.Authentication_']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-aaa-protocol-radius-oper:authentication-group'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.authentication is not None and self.authentication._has_data():
                            return True

                        if self.family is not None:
                            return True

                        if self.ip_address is not None:
                            return True

                        if self.port is not None:
                            return True

                        if self.server_address is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_protocol_radius_oper as meta
                        return meta._meta_table['Radius.Nodes.Node.Authentication.AuthenticationGroup']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-aaa-protocol-radius-oper:authentication'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.authentication_group is not None:
                        for child_ref in self.authentication_group:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_protocol_radius_oper as meta
                    return meta._meta_table['Radius.Nodes.Node.Authentication']['meta_info']


            class Accounting(object):
                """
                RADIUS accounting data
                
                .. attribute:: accounting_group
                
                	List of accounting groups
                	**type**\: list of    :py:class:`AccountingGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.Accounting.AccountingGroup>`
                
                

                """

                _prefix = 'aaa-protocol-radius-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.accounting_group = YList()
                    self.accounting_group.parent = self
                    self.accounting_group.name = 'accounting_group'


                class AccountingGroup(object):
                    """
                    List of accounting groups
                    
                    .. attribute:: accounting
                    
                    	Accounting data
                    	**type**\:   :py:class:`Accounting_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.Accounting.AccountingGroup.Accounting_>`
                    
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
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.accounting = Radius.Nodes.Node.Accounting.AccountingGroup.Accounting_()
                        self.accounting.parent = self
                        self.family = None
                        self.ip_address = None
                        self.port = None
                        self.server_address = None


                    class Accounting_(object):
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
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.acct_incorrect_responses = None
                            self.acct_response_time = None
                            self.acct_server_error_responses = None
                            self.acct_transaction_failure = None
                            self.acct_transaction_successess = None
                            self.acct_unexpected_responses = None
                            self.bad_authenticators = None
                            self.bad_responses = None
                            self.dropped_responses = None
                            self.pending_requests = None
                            self.requests = None
                            self.responses = None
                            self.retransmits = None
                            self.rtt = None
                            self.timeouts = None
                            self.unknown_packet_types = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-aaa-protocol-radius-oper:accounting'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.acct_incorrect_responses is not None:
                                return True

                            if self.acct_response_time is not None:
                                return True

                            if self.acct_server_error_responses is not None:
                                return True

                            if self.acct_transaction_failure is not None:
                                return True

                            if self.acct_transaction_successess is not None:
                                return True

                            if self.acct_unexpected_responses is not None:
                                return True

                            if self.bad_authenticators is not None:
                                return True

                            if self.bad_responses is not None:
                                return True

                            if self.dropped_responses is not None:
                                return True

                            if self.pending_requests is not None:
                                return True

                            if self.requests is not None:
                                return True

                            if self.responses is not None:
                                return True

                            if self.retransmits is not None:
                                return True

                            if self.rtt is not None:
                                return True

                            if self.timeouts is not None:
                                return True

                            if self.unknown_packet_types is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_protocol_radius_oper as meta
                            return meta._meta_table['Radius.Nodes.Node.Accounting.AccountingGroup.Accounting_']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-aaa-protocol-radius-oper:accounting-group'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.accounting is not None and self.accounting._has_data():
                            return True

                        if self.family is not None:
                            return True

                        if self.ip_address is not None:
                            return True

                        if self.port is not None:
                            return True

                        if self.server_address is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_protocol_radius_oper as meta
                        return meta._meta_table['Radius.Nodes.Node.Accounting.AccountingGroup']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-aaa-protocol-radius-oper:accounting'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.accounting_group is not None:
                        for child_ref in self.accounting_group:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_protocol_radius_oper as meta
                    return meta._meta_table['Radius.Nodes.Node.Accounting']['meta_info']


            class ServerGroups(object):
                """
                RADIUS server group table
                
                .. attribute:: server_group
                
                	RADIUS server group data
                	**type**\: list of    :py:class:`ServerGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.ServerGroups.ServerGroup>`
                
                

                """

                _prefix = 'aaa-protocol-radius-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.server_group = YList()
                    self.server_group.parent = self
                    self.server_group.name = 'server_group'


                class ServerGroup(object):
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
                    	**type**\: list of    :py:class:`ServerGroup_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_>`
                    
                    .. attribute:: servers
                    
                    	Number of servers
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vrf_name
                    
                    	VRF name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.server_group_name = None
                        self.dead_time = None
                        self.groups = None
                        self.server_group = YList()
                        self.server_group.parent = self
                        self.server_group.name = 'server_group'
                        self.servers = None
                        self.vrf_name = None


                    class ServerGroup_(object):
                        """
                        Server groups
                        
                        .. attribute:: accounting
                        
                        	Accounting data
                        	**type**\:   :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_.Accounting>`
                        
                        .. attribute:: accounting_port
                        
                        	Accounting port
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: authentication
                        
                        	Authentication data
                        	**type**\:   :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_.Authentication>`
                        
                        .. attribute:: authentication_port
                        
                        	Authentication port
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: authorization
                        
                        	Authorization data
                        	**type**\:   :py:class:`Authorization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_.Authorization>`
                        
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
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.accounting = Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_.Accounting()
                            self.accounting.parent = self
                            self.accounting_port = None
                            self.authentication = Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_.Authentication()
                            self.authentication.parent = self
                            self.authentication_port = None
                            self.authorization = Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_.Authorization()
                            self.authorization.parent = self
                            self.family = None
                            self.ip_address = None
                            self.is_private = None
                            self.server_address = None


                        class Accounting(object):
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
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.acct_incorrect_responses = None
                                self.acct_response_time = None
                                self.acct_server_error_responses = None
                                self.acct_transaction_failure = None
                                self.acct_transaction_successess = None
                                self.acct_unexpected_responses = None
                                self.bad_authenticators = None
                                self.bad_responses = None
                                self.dropped_responses = None
                                self.pending_requests = None
                                self.requests = None
                                self.responses = None
                                self.retransmits = None
                                self.rtt = None
                                self.timeouts = None
                                self.unknown_packet_types = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-aaa-protocol-radius-oper:accounting'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.acct_incorrect_responses is not None:
                                    return True

                                if self.acct_response_time is not None:
                                    return True

                                if self.acct_server_error_responses is not None:
                                    return True

                                if self.acct_transaction_failure is not None:
                                    return True

                                if self.acct_transaction_successess is not None:
                                    return True

                                if self.acct_unexpected_responses is not None:
                                    return True

                                if self.bad_authenticators is not None:
                                    return True

                                if self.bad_responses is not None:
                                    return True

                                if self.dropped_responses is not None:
                                    return True

                                if self.pending_requests is not None:
                                    return True

                                if self.requests is not None:
                                    return True

                                if self.responses is not None:
                                    return True

                                if self.retransmits is not None:
                                    return True

                                if self.rtt is not None:
                                    return True

                                if self.timeouts is not None:
                                    return True

                                if self.unknown_packet_types is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_protocol_radius_oper as meta
                                return meta._meta_table['Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_.Accounting']['meta_info']


                        class Authentication(object):
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
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.access_accepts = None
                                self.access_challenges = None
                                self.access_rejects = None
                                self.access_request_retransmits = None
                                self.access_requests = None
                                self.access_timeouts = None
                                self.authen_incorrect_responses = None
                                self.authen_response_time = None
                                self.authen_server_error_responses = None
                                self.authen_transaction_failure = None
                                self.authen_transaction_successess = None
                                self.authen_unexpected_responses = None
                                self.bad_access_authenticators = None
                                self.bad_access_responses = None
                                self.dropped_access_responses = None
                                self.pending_access_requests = None
                                self.rtt = None
                                self.unknown_access_types = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-aaa-protocol-radius-oper:authentication'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.access_accepts is not None:
                                    return True

                                if self.access_challenges is not None:
                                    return True

                                if self.access_rejects is not None:
                                    return True

                                if self.access_request_retransmits is not None:
                                    return True

                                if self.access_requests is not None:
                                    return True

                                if self.access_timeouts is not None:
                                    return True

                                if self.authen_incorrect_responses is not None:
                                    return True

                                if self.authen_response_time is not None:
                                    return True

                                if self.authen_server_error_responses is not None:
                                    return True

                                if self.authen_transaction_failure is not None:
                                    return True

                                if self.authen_transaction_successess is not None:
                                    return True

                                if self.authen_unexpected_responses is not None:
                                    return True

                                if self.bad_access_authenticators is not None:
                                    return True

                                if self.bad_access_responses is not None:
                                    return True

                                if self.dropped_access_responses is not None:
                                    return True

                                if self.pending_access_requests is not None:
                                    return True

                                if self.rtt is not None:
                                    return True

                                if self.unknown_access_types is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_protocol_radius_oper as meta
                                return meta._meta_table['Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_.Authentication']['meta_info']


                        class Authorization(object):
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
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.author_incorrect_responses = None
                                self.author_request_timeouts = None
                                self.author_requests = None
                                self.author_response_time = None
                                self.author_server_error_responses = None
                                self.author_transaction_failure = None
                                self.author_transaction_successess = None
                                self.author_unexpected_responses = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-aaa-protocol-radius-oper:authorization'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.author_incorrect_responses is not None:
                                    return True

                                if self.author_request_timeouts is not None:
                                    return True

                                if self.author_requests is not None:
                                    return True

                                if self.author_response_time is not None:
                                    return True

                                if self.author_server_error_responses is not None:
                                    return True

                                if self.author_transaction_failure is not None:
                                    return True

                                if self.author_transaction_successess is not None:
                                    return True

                                if self.author_unexpected_responses is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_protocol_radius_oper as meta
                                return meta._meta_table['Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_.Authorization']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-aaa-protocol-radius-oper:server-group'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.accounting is not None and self.accounting._has_data():
                                return True

                            if self.accounting_port is not None:
                                return True

                            if self.authentication is not None and self.authentication._has_data():
                                return True

                            if self.authentication_port is not None:
                                return True

                            if self.authorization is not None and self.authorization._has_data():
                                return True

                            if self.family is not None:
                                return True

                            if self.ip_address is not None:
                                return True

                            if self.is_private is not None:
                                return True

                            if self.server_address is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_protocol_radius_oper as meta
                            return meta._meta_table['Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.server_group_name is None:
                            raise YPYModelError('Key property server_group_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-aaa-protocol-radius-oper:server-group[Cisco-IOS-XR-aaa-protocol-radius-oper:server-group-name = ' + str(self.server_group_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.server_group_name is not None:
                            return True

                        if self.dead_time is not None:
                            return True

                        if self.groups is not None:
                            return True

                        if self.server_group is not None:
                            for child_ref in self.server_group:
                                if child_ref._has_data():
                                    return True

                        if self.servers is not None:
                            return True

                        if self.vrf_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_protocol_radius_oper as meta
                        return meta._meta_table['Radius.Nodes.Node.ServerGroups.ServerGroup']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-aaa-protocol-radius-oper:server-groups'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.server_group is not None:
                        for child_ref in self.server_group:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_protocol_radius_oper as meta
                    return meta._meta_table['Radius.Nodes.Node.ServerGroups']['meta_info']


            class DynamicAuthorization(object):
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
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.disconnected_invalid_requests = None
                    self.invalid_coa_requests = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-aaa-protocol-radius-oper:dynamic-authorization'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.disconnected_invalid_requests is not None:
                        return True

                    if self.invalid_coa_requests is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_protocol_radius_oper as meta
                    return meta._meta_table['Radius.Nodes.Node.DynamicAuthorization']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-aaa-protocol-radius-oper:radius/Cisco-IOS-XR-aaa-protocol-radius-oper:nodes/Cisco-IOS-XR-aaa-protocol-radius-oper:node[Cisco-IOS-XR-aaa-protocol-radius-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.accounting is not None and self.accounting._has_data():
                    return True

                if self.authentication is not None and self.authentication._has_data():
                    return True

                if self.client is not None and self.client._has_data():
                    return True

                if self.dead_criteria is not None and self.dead_criteria._has_data():
                    return True

                if self.dynamic_authorization is not None and self.dynamic_authorization._has_data():
                    return True

                if self.server_groups is not None and self.server_groups._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_protocol_radius_oper as meta
                return meta._meta_table['Radius.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-aaa-protocol-radius-oper:radius/Cisco-IOS-XR-aaa-protocol-radius-oper:nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.node is not None:
                for child_ref in self.node:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_protocol_radius_oper as meta
            return meta._meta_table['Radius.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-aaa-protocol-radius-oper:radius'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_protocol_radius_oper as meta
        return meta._meta_table['Radius']['meta_info']



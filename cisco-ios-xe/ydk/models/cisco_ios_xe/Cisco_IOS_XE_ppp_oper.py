""" Cisco_IOS_XE_ppp_oper 

This module contains a collection of YANG definitions
for PPP and PPPoE operational data.
Copyright (c) 2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class PppIosAuthType(Enum):
    """
    PppIosAuthType (Enum Class)

    Authentication type for the PPP session

    .. data:: ppp_ios_auth_none = 0

    	No authentication.

    .. data:: ppp_ios_auth_chap = 1

    	Challenge Handshake Authentication (CHAP).

    .. data:: ppp_ios_auth_pap = 2

    	Password Authentication Protocol (PAP).

    .. data:: ppp_ios_auth_mschap = 3

    	Microsoft CHAP (MS CHAP).

    .. data:: ppp_ios_auth_mschap_v2 = 4

    	Microsoft CHAP, Version 2 (MS CHAP V2).

    .. data:: ppp_ios_auth_eap = 5

    	Extensible Authentication Protocol (EAP).

    """

    ppp_ios_auth_none = Enum.YLeaf(0, "ppp-ios-auth-none")

    ppp_ios_auth_chap = Enum.YLeaf(1, "ppp-ios-auth-chap")

    ppp_ios_auth_pap = Enum.YLeaf(2, "ppp-ios-auth-pap")

    ppp_ios_auth_mschap = Enum.YLeaf(3, "ppp-ios-auth-mschap")

    ppp_ios_auth_mschap_v2 = Enum.YLeaf(4, "ppp-ios-auth-mschap-v2")

    ppp_ios_auth_eap = Enum.YLeaf(5, "ppp-ios-auth-eap")


class PppoeOperationalRole(Enum):
    """
    PppoeOperationalRole (Enum Class)

    The role that this PPPoE session is in

    .. data:: pppoe_client = 0

    	PPPoE device role is a client

    .. data:: pppoe_server = 1

    	PPPoE device role is a server

    """

    pppoe_client = Enum.YLeaf(0, "pppoe-client")

    pppoe_server = Enum.YLeaf(1, "pppoe-server")



class PppData(Entity):
    """
    Operational state of PPP
    
    .. attribute:: ppp_interface
    
    	A list of the PPP information
    	**type**\: list of  		 :py:class:`PppInterface <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ppp_oper.PppData.PppInterface>`
    
    .. attribute:: ppp_statistics
    
    	The PPP statistics
    	**type**\:  :py:class:`PppStatistics <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ppp_oper.PppData.PppStatistics>`
    
    	**presence node**\: True
    
    .. attribute:: pppoe
    
    	The PPPoE operation information
    	**type**\:  :py:class:`Pppoe <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ppp_oper.PppData.Pppoe>`
    
    	**presence node**\: True
    
    

    """

    _prefix = 'ppp-ios-xe-oper'
    _revision = '2017-11-01'

    def __init__(self):
        super(PppData, self).__init__()
        self._top_entity = None

        self.yang_name = "ppp-data"
        self.yang_parent_name = "Cisco-IOS-XE-ppp-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("ppp-statistics", ("ppp_statistics", PppData.PppStatistics)), ("pppoe", ("pppoe", PppData.Pppoe))])
        self._child_list_classes = OrderedDict([("ppp-interface", ("ppp_interface", PppData.PppInterface))])
        self._leafs = OrderedDict()

        self.ppp_statistics = None
        self._children_name_map["ppp_statistics"] = "ppp-statistics"
        self._children_yang_names.add("ppp-statistics")

        self.pppoe = None
        self._children_name_map["pppoe"] = "pppoe"
        self._children_yang_names.add("pppoe")

        self.ppp_interface = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-ppp-oper:ppp-data"

    def __setattr__(self, name, value):
        self._perform_setattr(PppData, [], name, value)


    class PppInterface(Entity):
        """
        A list of the PPP information
        
        .. attribute:: phy_ifname  (key)
        
        	Ifname of Physical Access (Parent) Interface 
        	**type**\: str
        
        .. attribute:: ppp_va
        
        	List of PPPoE sessions on ifname Physical access interface
        	**type**\: list of  		 :py:class:`PppVa <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ppp_oper.PppData.PppInterface.PppVa>`
        
        

        """

        _prefix = 'ppp-ios-xe-oper'
        _revision = '2017-11-01'

        def __init__(self):
            super(PppData.PppInterface, self).__init__()

            self.yang_name = "ppp-interface"
            self.yang_parent_name = "ppp-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['phy_ifname']
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ppp-va", ("ppp_va", PppData.PppInterface.PppVa))])
            self._leafs = OrderedDict([
                ('phy_ifname', YLeaf(YType.str, 'phy-ifname')),
            ])
            self.phy_ifname = None

            self.ppp_va = YList(self)
            self._segment_path = lambda: "ppp-interface" + "[phy-ifname='" + str(self.phy_ifname) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-ppp-oper:ppp-data/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(PppData.PppInterface, ['phy_ifname'], name, value)


        class PppVa(Entity):
            """
            List of PPPoE sessions on ifname Physical access interface
            
            .. attribute:: va_ifname
            
            	PPP Virtual Access Interface Name
            	**type**\: str
            
            .. attribute:: vrf_name
            
            	VRF of Virtual Access Interface
            	**type**\: str
            
            .. attribute:: interface_ip
            
            	IP Address assigned/negotiated by PPP
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            		**type**\: str
            
            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: gateway_ip
            
            	Gateway IP Address assigned/negotiated by PPP
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            		**type**\: str
            
            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: primary_dns_ip
            
            	Primary DNS IP Address assigned/negotiated by PPP
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            		**type**\: str
            
            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: secondary_dns_ip
            
            	Secondary DNS IP Address assigned/negotiated by PPP
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            		**type**\: str
            
            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: mtu
            
            	MTU for PPP interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: auth_type
            
            	Authentication type for PPP interface
            	**type**\:  :py:class:`PppIosAuthType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ppp_oper.PppIosAuthType>`
            
            

            """

            _prefix = 'ppp-ios-xe-oper'
            _revision = '2017-11-01'

            def __init__(self):
                super(PppData.PppInterface.PppVa, self).__init__()

                self.yang_name = "ppp-va"
                self.yang_parent_name = "ppp-interface"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('va_ifname', YLeaf(YType.str, 'va-ifname')),
                    ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                    ('interface_ip', YLeaf(YType.str, 'interface-ip')),
                    ('gateway_ip', YLeaf(YType.str, 'gateway-ip')),
                    ('primary_dns_ip', YLeaf(YType.str, 'primary-dns-ip')),
                    ('secondary_dns_ip', YLeaf(YType.str, 'secondary-dns-ip')),
                    ('mtu', YLeaf(YType.uint32, 'mtu')),
                    ('auth_type', YLeaf(YType.enumeration, 'auth-type')),
                ])
                self.va_ifname = None
                self.vrf_name = None
                self.interface_ip = None
                self.gateway_ip = None
                self.primary_dns_ip = None
                self.secondary_dns_ip = None
                self.mtu = None
                self.auth_type = None
                self._segment_path = lambda: "ppp-va"

            def __setattr__(self, name, value):
                self._perform_setattr(PppData.PppInterface.PppVa, ['va_ifname', 'vrf_name', 'interface_ip', 'gateway_ip', 'primary_dns_ip', 'secondary_dns_ip', 'mtu', 'auth_type'], name, value)


    class PppStatistics(Entity):
        """
        The PPP statistics
        
        .. attribute:: ppp_lcp_pkts
        
        	number of PPP LCP pkts
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ppp_ipcp_pkts
        
        	number of PPP NCP/IPCP pkts
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ppp_ccp_pkts
        
        	number of PPP CCP pkts
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ppp-ios-xe-oper'
        _revision = '2017-11-01'

        def __init__(self):
            super(PppData.PppStatistics, self).__init__()

            self.yang_name = "ppp-statistics"
            self.yang_parent_name = "ppp-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('ppp_lcp_pkts', YLeaf(YType.uint32, 'ppp-lcp-pkts')),
                ('ppp_ipcp_pkts', YLeaf(YType.uint32, 'ppp-ipcp-pkts')),
                ('ppp_ccp_pkts', YLeaf(YType.uint32, 'ppp-ccp-pkts')),
            ])
            self.ppp_lcp_pkts = None
            self.ppp_ipcp_pkts = None
            self.ppp_ccp_pkts = None
            self._segment_path = lambda: "ppp-statistics"
            self._absolute_path = lambda: "Cisco-IOS-XE-ppp-oper:ppp-data/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(PppData.PppStatistics, ['ppp_lcp_pkts', 'ppp_ipcp_pkts', 'ppp_ccp_pkts'], name, value)


    class Pppoe(Entity):
        """
        The PPPoE operation information
        
        .. attribute:: role
        
        	The current PPPoE role
        	**type**\:  :py:class:`PppoeOperationalRole <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ppp_oper.PppoeOperationalRole>`
        
        .. attribute:: pppoe_session_list
        
        	PPPoE session list
        	**type**\: list of  		 :py:class:`PppoeSessionList <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ppp_oper.PppData.Pppoe.PppoeSessionList>`
        
        .. attribute:: pppoe_statistics
        
        	PPPoE statistics
        	**type**\:  :py:class:`PppoeStatistics <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ppp_oper.PppData.Pppoe.PppoeStatistics>`
        
        	**presence node**\: True
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ppp-ios-xe-oper'
        _revision = '2017-11-01'

        def __init__(self):
            super(PppData.Pppoe, self).__init__()

            self.yang_name = "pppoe"
            self.yang_parent_name = "ppp-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("pppoe-statistics", ("pppoe_statistics", PppData.Pppoe.PppoeStatistics))])
            self._child_list_classes = OrderedDict([("pppoe-session-list", ("pppoe_session_list", PppData.Pppoe.PppoeSessionList))])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('role', YLeaf(YType.enumeration, 'role')),
            ])
            self.role = None

            self.pppoe_statistics = None
            self._children_name_map["pppoe_statistics"] = "pppoe-statistics"
            self._children_yang_names.add("pppoe-statistics")

            self.pppoe_session_list = YList(self)
            self._segment_path = lambda: "pppoe"
            self._absolute_path = lambda: "Cisco-IOS-XE-ppp-oper:ppp-data/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(PppData.Pppoe, ['role'], name, value)


        class PppoeSessionList(Entity):
            """
            PPPoE session list
            
            .. attribute:: ifname  (key)
            
            	Ifname of Physical Access (Parent) Interface
            	**type**\: str
            
            .. attribute:: session
            
            	List of PPPoE session on ifname Physical access interface
            	**type**\: list of  		 :py:class:`Session <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ppp_oper.PppData.Pppoe.PppoeSessionList.Session>`
            
            

            """

            _prefix = 'ppp-ios-xe-oper'
            _revision = '2017-11-01'

            def __init__(self):
                super(PppData.Pppoe.PppoeSessionList, self).__init__()

                self.yang_name = "pppoe-session-list"
                self.yang_parent_name = "pppoe"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifname']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("session", ("session", PppData.Pppoe.PppoeSessionList.Session))])
                self._leafs = OrderedDict([
                    ('ifname', YLeaf(YType.str, 'ifname')),
                ])
                self.ifname = None

                self.session = YList(self)
                self._segment_path = lambda: "pppoe-session-list" + "[ifname='" + str(self.ifname) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XE-ppp-oper:ppp-data/pppoe/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(PppData.Pppoe.PppoeSessionList, ['ifname'], name, value)


            class Session(Entity):
                """
                List of PPPoE session on ifname Physical access interface
                
                .. attribute:: session_id
                
                	Session Id of PPPoE sessions
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: lmac
                
                	Local MAC Address
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: rmac
                
                	Peer MAC Address
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: va_ifname
                
                	Ifname of Virtual Access Interface
                	**type**\: str
                
                .. attribute:: vrf_name
                
                	VRF of Virtual Access Interface 
                	**type**\: str
                
                .. attribute:: dot1q_qinq_outer_vlan
                
                	PPPoE session VLAN/QinQ ID  Outer VLAN (QinQ) or only VLAN ID
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: dot1q_qinq_inner_vlan
                
                	PPPoE session VLAN/QinQ ID  Inner VLAN ID (QinQ) (if valid)
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: service_name
                
                	PPPoE service tag name
                	**type**\: str
                
                .. attribute:: in_packet
                
                	Number of packets received over session
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_packet
                
                	Number of packets sent over session
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_bytes
                
                	Number of bytes received over session
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: out_bytes
                
                	Number of bytes sent over session
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'ppp-ios-xe-oper'
                _revision = '2017-11-01'

                def __init__(self):
                    super(PppData.Pppoe.PppoeSessionList.Session, self).__init__()

                    self.yang_name = "session"
                    self.yang_parent_name = "pppoe-session-list"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('session_id', YLeaf(YType.uint16, 'session-id')),
                        ('lmac', YLeaf(YType.str, 'lmac')),
                        ('rmac', YLeaf(YType.str, 'rmac')),
                        ('va_ifname', YLeaf(YType.str, 'va-ifname')),
                        ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                        ('dot1q_qinq_outer_vlan', YLeaf(YType.uint16, 'dot1q-qinq-outer-vlan')),
                        ('dot1q_qinq_inner_vlan', YLeaf(YType.uint16, 'dot1q-qinq-inner-vlan')),
                        ('service_name', YLeaf(YType.str, 'service-name')),
                        ('in_packet', YLeaf(YType.uint32, 'in-packet')),
                        ('out_packet', YLeaf(YType.uint32, 'out-packet')),
                        ('in_bytes', YLeaf(YType.uint64, 'in-bytes')),
                        ('out_bytes', YLeaf(YType.uint64, 'out-bytes')),
                    ])
                    self.session_id = None
                    self.lmac = None
                    self.rmac = None
                    self.va_ifname = None
                    self.vrf_name = None
                    self.dot1q_qinq_outer_vlan = None
                    self.dot1q_qinq_inner_vlan = None
                    self.service_name = None
                    self.in_packet = None
                    self.out_packet = None
                    self.in_bytes = None
                    self.out_bytes = None
                    self._segment_path = lambda: "session"

                def __setattr__(self, name, value):
                    self._perform_setattr(PppData.Pppoe.PppoeSessionList.Session, ['session_id', 'lmac', 'rmac', 'va_ifname', 'vrf_name', 'dot1q_qinq_outer_vlan', 'dot1q_qinq_inner_vlan', 'service_name', 'in_packet', 'out_packet', 'in_bytes', 'out_bytes'], name, value)


        class PppoeStatistics(Entity):
            """
            PPPoE statistics
            
            .. attribute:: pppoe_padi_pkts
            
            	PPPoE active discovery initiation pkts
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: pppoe_pado_pkts
            
            	PPPoE active discovery offer pkts
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: pppoe_padr_pkts
            
            	PPPoE active discovery response pkts
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: pppoe_pads_pkts
            
            	PPPoE active discovery session pkts
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'ppp-ios-xe-oper'
            _revision = '2017-11-01'

            def __init__(self):
                super(PppData.Pppoe.PppoeStatistics, self).__init__()

                self.yang_name = "pppoe-statistics"
                self.yang_parent_name = "pppoe"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self.is_presence_container = True
                self._leafs = OrderedDict([
                    ('pppoe_padi_pkts', YLeaf(YType.uint32, 'pppoe-padi-pkts')),
                    ('pppoe_pado_pkts', YLeaf(YType.uint32, 'pppoe-pado-pkts')),
                    ('pppoe_padr_pkts', YLeaf(YType.uint32, 'pppoe-padr-pkts')),
                    ('pppoe_pads_pkts', YLeaf(YType.uint32, 'pppoe-pads-pkts')),
                ])
                self.pppoe_padi_pkts = None
                self.pppoe_pado_pkts = None
                self.pppoe_padr_pkts = None
                self.pppoe_pads_pkts = None
                self._segment_path = lambda: "pppoe-statistics"
                self._absolute_path = lambda: "Cisco-IOS-XE-ppp-oper:ppp-data/pppoe/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(PppData.Pppoe.PppoeStatistics, ['pppoe_padi_pkts', 'pppoe_pado_pkts', 'pppoe_padr_pkts', 'pppoe_pads_pkts'], name, value)

    def clone_ptr(self):
        self._top_entity = PppData()
        return self._top_entity


""" Cisco_IOS_XE_aaa_oper 

This module contains a collection of YANG definitions
for AAA operational data.
Copyright (c) 2017\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class AaaSessProtType(Enum):
    """
    AaaSessProtType (Enum Class)

    AAA protocol type is used by clients to indicate how

    the session is established.

    .. data:: aaa_sess_proto_type_none = 0

    	No Protocol type

    .. data:: aaa_sess_proto_type_invalid = 1

    	Invalid Protocol type 

    .. data:: aaa_sess_proto_type_lcp = 2

    	LCP Protocol type 

    .. data:: aaa_sess_proto_type_ip = 3

    	IP Protocol type 

    .. data:: aaa_sess_proto_type_ipsec = 4

    	IPSEC Protocol type 

    .. data:: aaa_sess_proto_type_ipx = 5

    	IPX Protocol type 

    .. data:: aaa_sess_proto_type_atalk = 6

    	ATALK Protocol type 

    .. data:: aaa_sess_proto_type_xremote = 7

    	XREMOTE Protocol type 

    .. data:: aaa_sess_proto_type_tn3270 = 8

    	TN3270 Protocol type 

    .. data:: aaa_sess_proto_type_telnet = 9

    	TELNET Protocol type 

    .. data:: aaa_sess_proto_type_tcp_clear = 10

    	TCP_CLEAR Protocol type 

    .. data:: aaa_sess_proto_type_rlogin = 11

    	RLOGIN Protocol type 

    .. data:: aaa_sess_proto_type_lat = 12

    	LAT Protocol type 

    .. data:: aaa_sess_proto_type_pad = 13

    	PAD Protocol type 

    .. data:: aaa_sess_proto_type_osicp = 14

    	OSICP Protocol type 

    .. data:: aaa_sess_proto_type_tagcp = 15

    	TAGCP Protocol type 

    .. data:: aaa_sess_proto_type_bacp = 16

    	BACP Protocol type 

    .. data:: aaa_sess_proto_type_decnet = 17

    	DECNET Protocol type 

    .. data:: aaa_sess_proto_type_ccp = 18

    	CCP Protocol type 

    .. data:: aaa_sess_proto_type_cdp = 19

    	CDP Protocol type 

    .. data:: aaa_sess_proto_type_bridging = 20

    	BRIDGING Protocol type 

    .. data:: aaa_sess_proto_type_nbf = 21

    	NBF Protocol type 

    .. data:: aaa_sess_proto_type_bap = 22

    	BAP Protocol type 

    .. data:: aaa_sess_proto_type_multilink = 23

    	MULTILINK Protocol type 

    .. data:: aaa_sess_proto_type_h323 = 24

    	H323 Protocol type 

    .. data:: aaa_sess_proto_type_unknown = 25

    	UNKNOWN Protocol type 

    .. data:: aaa_sess_proto_type_call_accept = 26

    	CALL ACCEPT Protocol type 

    .. data:: aaa_sess_proto_type_vpdn_session = 27

    	VPDN SESSION Protocol type 

    .. data:: aaa_sess_proto_type_rm_call_status = 28

    	RM CALL STATUS Protocol type 

    .. data:: aaa_sess_proto_type_rm_nas_status = 29

    	RM NAS STATUS Protocol type 

    .. data:: aaa_sess_proto_type_dial_in = 30

    	DIAL IN Protocol type 

    .. data:: aaa_sess_proto_type_dial_out = 31

    	DIAL OUT Protocol type 

    .. data:: aaa_sess_proto_type_ss7 = 32

    	SS7 Protocol type 

    .. data:: aaa_sess_proto_type_rms_stop = 33

    	RMS STOP Protocol type 

    .. data:: aaa_sess_proto_type_rms_start = 34

    	RMS START Protocol type 

    .. data:: aaa_sess_proto_type_vpdn = 35

    	VPDN Protocol type 

    .. data:: aaa_sess_proto_type_sss = 36

    	SSS Protocol type 

    .. data:: aaa_sess_proto_type_subscriber = 37

    	SUBSCRIBER Protocol type 

    .. data:: aaa_sess_proto_type_atm = 38

    	ATM Protocol type 

    .. data:: aaa_sess_proto_type_ssh = 39

    	SSH Protocol type 

    .. data:: aaa_sess_proto_type_ipv6 = 40

    	IPV6 Protocol type 

    .. data:: aaa_sess_proto_type_aironet = 41

    	AIRONET Protocol type 

    .. data:: aaa_sess_proto_type_pppoe = 42

    	PPOE Protocol type 

    .. data:: aaa_sess_proto_type_entity = 43

    	ENTITY Protocol type 

    .. data:: aaa_sess_proto_type_cdma = 44

    	CDMA Protocol type 

    .. data:: aaa_sess_proto_type_crb = 45

    	CRB Protocol type 

    .. data:: aaa_sess_proto_type_template = 46

    	TEMPLATE Protocol type 

    .. data:: aaa_sess_proto_type_aaa = 47

    	AAA Protocol type 

    .. data:: aaa_sess_proto_type_epd = 48

    	EPD Protocol type 

    .. data:: aaa_sess_proto_type_mac = 49

    	MAC Protocol type 

    .. data:: aaa_sess_proto_type_leap = 50

    	LEAP Protocol type 

    .. data:: aaa_sess_proto_type_igmp = 51

    	IGMP Protocol type 

    .. data:: aaa_sess_proto_type_webvpn = 52

    	WEBVPN Protocol type 

    .. data:: aaa_sess_proto_type_cts = 53

    	CTS Protocol type 

    .. data:: aaa_sess_proto_type_radius = 54

    	RADIUS Protocol type 

    .. data:: aaa_sess_proto_type_evc = 55

    	EVC Protocol type 

    .. data:: aaa_sess_proto_type_elmi = 56

    	ELMI Protocol type 

    .. data:: aaa_sess_proto_type_dot1x = 57

    	DOT1X Protocol type 

    .. data:: aaa_sess_proto_type_dtp = 58

    	DTP Protocol type 

    .. data:: aaa_sess_proto_type_lacp = 59

    	LACP Protocol type 

    .. data:: aaa_sess_proto_type_pagp = 60

    	PAGP Protocol type 

    .. data:: aaa_sess_proto_type_stp = 61

    	STP Protocol type 

    .. data:: aaa_sess_proto_type_vtp = 62

    	VTP Protocol type 

    .. data:: aaa_sess_proto_type_ethernet_mac_tunnel = 63

    	ETHERNET MAC TUNNEL Protocol type 

    .. data:: aaa_sess_proto_type_bridge_domain = 64

    	BRIDGE DOMAIN Protocol type 

    .. data:: aaa_sess_proto_type_ethernet_cfm = 65

    	ETHERNET CFM Protocol type 

    .. data:: aaa_sess_proto_type_ethernet_service_instance = 66

    	ETHERNET SERVICE INSTANCE Protocol type 

    .. data:: aaa_sess_proto_type_service_group = 67

    	SERVICE GROUP Protocol type 

    .. data:: aaa_sess_proto_type_ip_dhcp_snooping = 68

    	IP DHCP SNOOPING Protocol type 

    .. data:: aaa_sess_proto_type_ip_source_guard = 69

    	IP SOURCE GUARD Protocol type 

    .. data:: aaa_sess_proto_type_error_disable = 70

    	ERROR DISABLE Protocol type 

    .. data:: aaa_sess_proto_type_cmac_bridge_domain = 71

    	CMAC BRIDGE DOMAIN Protocol type 

    .. data:: aaa_sess_proto_type_mac_in_mac_tunnel = 72

    	MAC IN MAC TUNNEL Protocol type 

    .. data:: aaa_sess_proto_type_l2vpn = 73

    	L2VPN Protocol type 

    .. data:: aaa_sess_proto_type_snmp = 74

    	SNMP Protocol type 

    """

    aaa_sess_proto_type_none = Enum.YLeaf(0, "aaa-sess-proto-type-none")

    aaa_sess_proto_type_invalid = Enum.YLeaf(1, "aaa-sess-proto-type-invalid")

    aaa_sess_proto_type_lcp = Enum.YLeaf(2, "aaa-sess-proto-type-lcp")

    aaa_sess_proto_type_ip = Enum.YLeaf(3, "aaa-sess-proto-type-ip")

    aaa_sess_proto_type_ipsec = Enum.YLeaf(4, "aaa-sess-proto-type-ipsec")

    aaa_sess_proto_type_ipx = Enum.YLeaf(5, "aaa-sess-proto-type-ipx")

    aaa_sess_proto_type_atalk = Enum.YLeaf(6, "aaa-sess-proto-type-atalk")

    aaa_sess_proto_type_xremote = Enum.YLeaf(7, "aaa-sess-proto-type-xremote")

    aaa_sess_proto_type_tn3270 = Enum.YLeaf(8, "aaa-sess-proto-type-tn3270")

    aaa_sess_proto_type_telnet = Enum.YLeaf(9, "aaa-sess-proto-type-telnet")

    aaa_sess_proto_type_tcp_clear = Enum.YLeaf(10, "aaa-sess-proto-type-tcp-clear")

    aaa_sess_proto_type_rlogin = Enum.YLeaf(11, "aaa-sess-proto-type-rlogin")

    aaa_sess_proto_type_lat = Enum.YLeaf(12, "aaa-sess-proto-type-lat")

    aaa_sess_proto_type_pad = Enum.YLeaf(13, "aaa-sess-proto-type-pad")

    aaa_sess_proto_type_osicp = Enum.YLeaf(14, "aaa-sess-proto-type-osicp")

    aaa_sess_proto_type_tagcp = Enum.YLeaf(15, "aaa-sess-proto-type-tagcp")

    aaa_sess_proto_type_bacp = Enum.YLeaf(16, "aaa-sess-proto-type-bacp")

    aaa_sess_proto_type_decnet = Enum.YLeaf(17, "aaa-sess-proto-type-decnet")

    aaa_sess_proto_type_ccp = Enum.YLeaf(18, "aaa-sess-proto-type-ccp")

    aaa_sess_proto_type_cdp = Enum.YLeaf(19, "aaa-sess-proto-type-cdp")

    aaa_sess_proto_type_bridging = Enum.YLeaf(20, "aaa-sess-proto-type-bridging")

    aaa_sess_proto_type_nbf = Enum.YLeaf(21, "aaa-sess-proto-type-nbf")

    aaa_sess_proto_type_bap = Enum.YLeaf(22, "aaa-sess-proto-type-bap")

    aaa_sess_proto_type_multilink = Enum.YLeaf(23, "aaa-sess-proto-type-multilink")

    aaa_sess_proto_type_h323 = Enum.YLeaf(24, "aaa-sess-proto-type-h323")

    aaa_sess_proto_type_unknown = Enum.YLeaf(25, "aaa-sess-proto-type-unknown")

    aaa_sess_proto_type_call_accept = Enum.YLeaf(26, "aaa-sess-proto-type-call-accept")

    aaa_sess_proto_type_vpdn_session = Enum.YLeaf(27, "aaa-sess-proto-type-vpdn-session")

    aaa_sess_proto_type_rm_call_status = Enum.YLeaf(28, "aaa-sess-proto-type-rm-call-status")

    aaa_sess_proto_type_rm_nas_status = Enum.YLeaf(29, "aaa-sess-proto-type-rm-nas-status")

    aaa_sess_proto_type_dial_in = Enum.YLeaf(30, "aaa-sess-proto-type-dial-in")

    aaa_sess_proto_type_dial_out = Enum.YLeaf(31, "aaa-sess-proto-type-dial-out")

    aaa_sess_proto_type_ss7 = Enum.YLeaf(32, "aaa-sess-proto-type-ss7")

    aaa_sess_proto_type_rms_stop = Enum.YLeaf(33, "aaa-sess-proto-type-rms-stop")

    aaa_sess_proto_type_rms_start = Enum.YLeaf(34, "aaa-sess-proto-type-rms-start")

    aaa_sess_proto_type_vpdn = Enum.YLeaf(35, "aaa-sess-proto-type-vpdn")

    aaa_sess_proto_type_sss = Enum.YLeaf(36, "aaa-sess-proto-type-sss")

    aaa_sess_proto_type_subscriber = Enum.YLeaf(37, "aaa-sess-proto-type-subscriber")

    aaa_sess_proto_type_atm = Enum.YLeaf(38, "aaa-sess-proto-type-atm")

    aaa_sess_proto_type_ssh = Enum.YLeaf(39, "aaa-sess-proto-type-ssh")

    aaa_sess_proto_type_ipv6 = Enum.YLeaf(40, "aaa-sess-proto-type-ipv6")

    aaa_sess_proto_type_aironet = Enum.YLeaf(41, "aaa-sess-proto-type-aironet")

    aaa_sess_proto_type_pppoe = Enum.YLeaf(42, "aaa-sess-proto-type-pppoe")

    aaa_sess_proto_type_entity = Enum.YLeaf(43, "aaa-sess-proto-type-entity")

    aaa_sess_proto_type_cdma = Enum.YLeaf(44, "aaa-sess-proto-type-cdma")

    aaa_sess_proto_type_crb = Enum.YLeaf(45, "aaa-sess-proto-type-crb")

    aaa_sess_proto_type_template = Enum.YLeaf(46, "aaa-sess-proto-type-template")

    aaa_sess_proto_type_aaa = Enum.YLeaf(47, "aaa-sess-proto-type-aaa")

    aaa_sess_proto_type_epd = Enum.YLeaf(48, "aaa-sess-proto-type-epd")

    aaa_sess_proto_type_mac = Enum.YLeaf(49, "aaa-sess-proto-type-mac")

    aaa_sess_proto_type_leap = Enum.YLeaf(50, "aaa-sess-proto-type-leap")

    aaa_sess_proto_type_igmp = Enum.YLeaf(51, "aaa-sess-proto-type-igmp")

    aaa_sess_proto_type_webvpn = Enum.YLeaf(52, "aaa-sess-proto-type-webvpn")

    aaa_sess_proto_type_cts = Enum.YLeaf(53, "aaa-sess-proto-type-cts")

    aaa_sess_proto_type_radius = Enum.YLeaf(54, "aaa-sess-proto-type-radius")

    aaa_sess_proto_type_evc = Enum.YLeaf(55, "aaa-sess-proto-type-evc")

    aaa_sess_proto_type_elmi = Enum.YLeaf(56, "aaa-sess-proto-type-elmi")

    aaa_sess_proto_type_dot1x = Enum.YLeaf(57, "aaa-sess-proto-type-dot1x")

    aaa_sess_proto_type_dtp = Enum.YLeaf(58, "aaa-sess-proto-type-dtp")

    aaa_sess_proto_type_lacp = Enum.YLeaf(59, "aaa-sess-proto-type-lacp")

    aaa_sess_proto_type_pagp = Enum.YLeaf(60, "aaa-sess-proto-type-pagp")

    aaa_sess_proto_type_stp = Enum.YLeaf(61, "aaa-sess-proto-type-stp")

    aaa_sess_proto_type_vtp = Enum.YLeaf(62, "aaa-sess-proto-type-vtp")

    aaa_sess_proto_type_ethernet_mac_tunnel = Enum.YLeaf(63, "aaa-sess-proto-type-ethernet-mac-tunnel")

    aaa_sess_proto_type_bridge_domain = Enum.YLeaf(64, "aaa-sess-proto-type-bridge-domain")

    aaa_sess_proto_type_ethernet_cfm = Enum.YLeaf(65, "aaa-sess-proto-type-ethernet-cfm")

    aaa_sess_proto_type_ethernet_service_instance = Enum.YLeaf(66, "aaa-sess-proto-type-ethernet-service-instance")

    aaa_sess_proto_type_service_group = Enum.YLeaf(67, "aaa-sess-proto-type-service-group")

    aaa_sess_proto_type_ip_dhcp_snooping = Enum.YLeaf(68, "aaa-sess-proto-type-ip-dhcp-snooping")

    aaa_sess_proto_type_ip_source_guard = Enum.YLeaf(69, "aaa-sess-proto-type-ip-source-guard")

    aaa_sess_proto_type_error_disable = Enum.YLeaf(70, "aaa-sess-proto-type-error-disable")

    aaa_sess_proto_type_cmac_bridge_domain = Enum.YLeaf(71, "aaa-sess-proto-type-cmac-bridge-domain")

    aaa_sess_proto_type_mac_in_mac_tunnel = Enum.YLeaf(72, "aaa-sess-proto-type-mac-in-mac-tunnel")

    aaa_sess_proto_type_l2vpn = Enum.YLeaf(73, "aaa-sess-proto-type-l2vpn")

    aaa_sess_proto_type_snmp = Enum.YLeaf(74, "aaa-sess-proto-type-snmp")



class AaaData(Entity):
    """
    Operational state of AAA
    
    .. attribute:: aaa_users
    
    	List of current users
    	**type**\: list of  		 :py:class:`AaaUsers <ydk.models.cisco_ios_xe.Cisco_IOS_XE_aaa_oper.AaaData.AaaUsers>`
    
    

    """

    _prefix = 'aaa-ios-xe-oper'
    _revision = '2017-11-01'

    def __init__(self):
        super(AaaData, self).__init__()
        self._top_entity = None

        self.yang_name = "aaa-data"
        self.yang_parent_name = "Cisco-IOS-XE-aaa-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([("aaa-users", ("aaa_users", AaaData.AaaUsers))])
        self._leafs = OrderedDict()

        self.aaa_users = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-aaa-oper:aaa-data"

    def __setattr__(self, name, value):
        self._perform_setattr(AaaData, [], name, value)


    class AaaUsers(Entity):
        """
        List of current users
        
        .. attribute:: username  (key)
        
        	The username used to logged into the device
        	**type**\: str
        
        .. attribute:: aaa_sessions
        
        	Sessions associated with the users
        	**type**\: list of  		 :py:class:`AaaSessions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_aaa_oper.AaaData.AaaUsers.AaaSessions>`
        
        

        """

        _prefix = 'aaa-ios-xe-oper'
        _revision = '2017-11-01'

        def __init__(self):
            super(AaaData.AaaUsers, self).__init__()

            self.yang_name = "aaa-users"
            self.yang_parent_name = "aaa-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['username']
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("aaa-sessions", ("aaa_sessions", AaaData.AaaUsers.AaaSessions))])
            self._leafs = OrderedDict([
                ('username', YLeaf(YType.str, 'username')),
            ])
            self.username = None

            self.aaa_sessions = YList(self)
            self._segment_path = lambda: "aaa-users" + "[username='" + str(self.username) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-aaa-oper:aaa-data/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(AaaData.AaaUsers, ['username'], name, value)


        class AaaSessions(Entity):
            """
            Sessions associated with the users
            
            .. attribute:: aaa_uid  (key)
            
            	AAA Unique ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: session_id
            
            	AAA Session ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ip_addr
            
            	Source IP address that initiated the session
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            		**type**\: str
            
            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: protocol
            
            	AAA protocol type Protocol used in this session
            	**type**\:  :py:class:`AaaSessProtType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_aaa_oper.AaaSessProtType>`
            
            .. attribute:: login_time
            
            	Login\-time for this session present in aaa code
            	**type**\: str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            

            """

            _prefix = 'aaa-ios-xe-oper'
            _revision = '2017-11-01'

            def __init__(self):
                super(AaaData.AaaUsers.AaaSessions, self).__init__()

                self.yang_name = "aaa-sessions"
                self.yang_parent_name = "aaa-users"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['aaa_uid']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('aaa_uid', YLeaf(YType.uint32, 'aaa-uid')),
                    ('session_id', YLeaf(YType.uint32, 'session-id')),
                    ('ip_addr', YLeaf(YType.str, 'ip-addr')),
                    ('protocol', YLeaf(YType.enumeration, 'protocol')),
                    ('login_time', YLeaf(YType.str, 'login-time')),
                ])
                self.aaa_uid = None
                self.session_id = None
                self.ip_addr = None
                self.protocol = None
                self.login_time = None
                self._segment_path = lambda: "aaa-sessions" + "[aaa-uid='" + str(self.aaa_uid) + "']"

            def __setattr__(self, name, value):
                self._perform_setattr(AaaData.AaaUsers.AaaSessions, ['aaa_uid', 'session_id', 'ip_addr', 'protocol', 'login_time'], name, value)

    def clone_ptr(self):
        self._top_entity = AaaData()
        return self._top_entity


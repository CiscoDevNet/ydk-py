""" Cisco_IOS_XE_ntp_oper 

This module contains a collection of YANG definitions
for NTP operational data.
Copyright (c) 2017\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class KissCodeType(Enum):
    """
    KissCodeType (Enum Class)

    Kiss code is used for debug or maintenance purposes in devices in stratum 0 or 16

    .. data:: ntp_ref_acst = 0

    	The association belongs to a unicast server

    .. data:: ntp_ref_auth = 1

    	Server authentication failed

    .. data:: ntp_ref_auto = 2

    	Autokey sequence failed

    .. data:: ntp_ref_bcst = 3

    	The association belongs to a broadcast server

    .. data:: ntp_ref_cryp = 4

    	Cryptographic authentication or identification failed

    .. data:: ntp_ref_deny = 5

    	Access denied by remote server

    .. data:: ntp_ref_drop = 6

    	Lost peer in symmetric mode

    .. data:: ntp_ref_rstr = 7

    	Access denied due to local policy

    .. data:: ntp_ref_init = 8

    	The association has not synchronized for the first time

    .. data:: ntp_ref_mcst = 9

    	The association belongs to a dynamically discovered server

    .. data:: ntp_ref_nkey = 10

    	No key found. Either the key was never installed or not trusted

    .. data:: ntp_ref_rate = 11

    	The server has temporarily denied access because

    	the client exceeded the rate threshold

    .. data:: ntp_ref_rmot = 12

    	Alteration of association from a remote host running ntpdc

    .. data:: ntp_ref_step = 13

    	STEP means the offset is less than the panic threshold but greater than the step threshold of 125 ms

    """

    ntp_ref_acst = Enum.YLeaf(0, "ntp-ref-acst")

    ntp_ref_auth = Enum.YLeaf(1, "ntp-ref-auth")

    ntp_ref_auto = Enum.YLeaf(2, "ntp-ref-auto")

    ntp_ref_bcst = Enum.YLeaf(3, "ntp-ref-bcst")

    ntp_ref_cryp = Enum.YLeaf(4, "ntp-ref-cryp")

    ntp_ref_deny = Enum.YLeaf(5, "ntp-ref-deny")

    ntp_ref_drop = Enum.YLeaf(6, "ntp-ref-drop")

    ntp_ref_rstr = Enum.YLeaf(7, "ntp-ref-rstr")

    ntp_ref_init = Enum.YLeaf(8, "ntp-ref-init")

    ntp_ref_mcst = Enum.YLeaf(9, "ntp-ref-mcst")

    ntp_ref_nkey = Enum.YLeaf(10, "ntp-ref-nkey")

    ntp_ref_rate = Enum.YLeaf(11, "ntp-ref-rate")

    ntp_ref_rmot = Enum.YLeaf(12, "ntp-ref-rmot")

    ntp_ref_step = Enum.YLeaf(13, "ntp-ref-step")


class PeerAuthStatus(Enum):
    """
    PeerAuthStatus (Enum Class)

    Status of authenticating switch with peer or server

    .. data:: ntp_auth_ok = 0

    	The NTP client or server packet has MAC  

    	field and authentication succeded

    .. data:: ntp_auth_bad_auth = 1

    	The NTP client or server packet has MAC  

    	and decryption failed with AUTH_ERROR 

    .. data:: ntp_auth_auth_not_configured = 2

    	The NTP client or server is not configured with authenication

    	with server or client

    .. data:: ntp_auth_status_not_available = 3

    	The NTP client or server authentication stautus is not available

    	 as now

    .. data:: ntp_auth_none = 4

    	The NTP client or server packet has no MAC  

    	with server or peer

    .. data:: ntp_auth_crypto = 5

    	crypto-NAK. The MAC has four octets only and could not  

    	determine authentication status with peer

    """

    ntp_auth_ok = Enum.YLeaf(0, "ntp-auth-ok")

    ntp_auth_bad_auth = Enum.YLeaf(1, "ntp-auth-bad-auth")

    ntp_auth_auth_not_configured = Enum.YLeaf(2, "ntp-auth-auth-not-configured")

    ntp_auth_status_not_available = Enum.YLeaf(3, "ntp-auth-status-not-available")

    ntp_auth_none = Enum.YLeaf(4, "ntp-auth-none")

    ntp_auth_crypto = Enum.YLeaf(5, "ntp-auth-crypto")


class PeerEvent(Enum):
    """
    PeerEvent (Enum Class)

    Event received by switch or router and sent by peer

    .. data:: ntp_peer_event_mobilize = 0

    	This event is used to allocate resources and 

    	initialize defaults or values when a NTP association is setup

    .. data:: ntp_peer_event_demobilize = 1

    	This event is used to tear down the resources

    	associated with a NTP association

    .. data:: ntp_peer_event_unreachable = 2

    	This event indicates that the NTP peer is 

    	unreachable

    .. data:: ntp_peer_event_reachable = 3

    	This event indicates that the peer is reachable

    .. data:: ntp_peer_event_restart = 4

    	Event to indicate that the NTP process restart

    	is now complete

    .. data:: ntp_peer_event_reply = 5

    	NTP peer or server reply event in response to a 

    	get time request from the client

    .. data:: ntp_peer_event_rate = 6

    	This event is used to synchronize the client 

    	and peer or server through a flow contol mechanism

    .. data:: ntp_peer_event_deny = 7

    	Event from peer that indicates denial of access to the 

    	switch or router

    .. data:: ntp_peer_disarmed = 8

    	This event clears or resets the NTP flag after the

    	leap second event so that the system is now ready to receive the next

    	leap second event

    .. data:: ntp_peer_armed = 9

    	Peer event armed means that the event for delaying

    	the clock increment by one second for a leap year will be scheduled 

    	next month

    .. data:: ntp_peer_event_newpeer = 10

    	New peer added to association

    .. data:: ntp_peer_event_clock = 11

    	This event indicates clock tick errors

    .. data:: ntp_peer_event_auth = 12

    	Event indicating status of authenticating switch

    	or router with peer

    .. data:: ntp_peer_event_popcorn = 13

    	Popcorn event indicates a delayed NTP packet due

    	to congestion in the network

    .. data:: ntp_peer_event_xleave = 14

    	Event for NTP peer or server leaving the 

    	association

    .. data:: ntp_peer_event_xerr = 15

    	NTP event for an error message received from 

    	peer or server

    .. data:: ntp_peer_event_tai = 16

    	Event for incorporating correction for 

    	International Atomic Time based on offsets from UTC

    """

    ntp_peer_event_mobilize = Enum.YLeaf(0, "ntp-peer-event-mobilize")

    ntp_peer_event_demobilize = Enum.YLeaf(1, "ntp-peer-event-demobilize")

    ntp_peer_event_unreachable = Enum.YLeaf(2, "ntp-peer-event-unreachable")

    ntp_peer_event_reachable = Enum.YLeaf(3, "ntp-peer-event-reachable")

    ntp_peer_event_restart = Enum.YLeaf(4, "ntp-peer-event-restart")

    ntp_peer_event_reply = Enum.YLeaf(5, "ntp-peer-event-reply")

    ntp_peer_event_rate = Enum.YLeaf(6, "ntp-peer-event-rate")

    ntp_peer_event_deny = Enum.YLeaf(7, "ntp-peer-event-deny")

    ntp_peer_disarmed = Enum.YLeaf(8, "ntp-peer-disarmed")

    ntp_peer_armed = Enum.YLeaf(9, "ntp-peer-armed")

    ntp_peer_event_newpeer = Enum.YLeaf(10, "ntp-peer-event-newpeer")

    ntp_peer_event_clock = Enum.YLeaf(11, "ntp-peer-event-clock")

    ntp_peer_event_auth = Enum.YLeaf(12, "ntp-peer-event-auth")

    ntp_peer_event_popcorn = Enum.YLeaf(13, "ntp-peer-event-popcorn")

    ntp_peer_event_xleave = Enum.YLeaf(14, "ntp-peer-event-xleave")

    ntp_peer_event_xerr = Enum.YLeaf(15, "ntp-peer-event-xerr")

    ntp_peer_event_tai = Enum.YLeaf(16, "ntp-peer-event-tai")


class PeerSelectStatus(Enum):
    """
    PeerSelectStatus (Enum Class)

    Selection status of peer

    .. data:: ntp_peer_as_backup = 0

    	The peer is a survivor but not among the first 

    	six peers

    .. data:: ntp_peer_rejected = 1

    	The peer was rejected due to a loop or due

    	to becoming unreachable or due to bad synchronization distance

    .. data:: ntp_peer_false_ticker = 2

    	The peer or server is discarded due to false tick

    	or clock errors

    .. data:: ntp_peer_excess = 3

    	The peer is discarded as it is not among the 

    	first ten peers sorted by synchronization distance

    .. data:: ntp_peer_outlier = 4

    	NTP server or peer rejected as outlier

    .. data:: ntp_peer_candidate = 5

    	Possible candidate for selection as time server

    .. data:: ntp_peer_sys_peer = 6

    	Peer or server selected as time server

    .. data:: ntp_peer_pps_peer = 7

    	Peer or server selected as time server. In this 

    	case the Pulse Per Second signal is used to synchronize the client and

    	server or peer

    """

    ntp_peer_as_backup = Enum.YLeaf(0, "ntp-peer-as-backup")

    ntp_peer_rejected = Enum.YLeaf(1, "ntp-peer-rejected")

    ntp_peer_false_ticker = Enum.YLeaf(2, "ntp-peer-false-ticker")

    ntp_peer_excess = Enum.YLeaf(3, "ntp-peer-excess")

    ntp_peer_outlier = Enum.YLeaf(4, "ntp-peer-outlier")

    ntp_peer_candidate = Enum.YLeaf(5, "ntp-peer-candidate")

    ntp_peer_sys_peer = Enum.YLeaf(6, "ntp-peer-sys-peer")

    ntp_peer_pps_peer = Enum.YLeaf(7, "ntp-peer-pps-peer")


class PeerStatusWord(Enum):
    """
    PeerStatusWord (Enum Class)

    Peer status word or crypto of ntp server or ntp peer

    .. data:: crypto_flag_sig = 0

    	In autokey[public key ntp authentication protocol ], this flag is 

    	set when host certificate is signed by server.This is not implemented/supported as of now 

    .. data:: crypto_flag_leap = 1

    	In autokey, this flag is set when leap second values

    	are received and validated

    .. data:: crypto_flag_vrfy = 2

    	In autokey,this flag is set when the trusted host identity

    	credentials are  confirmed 

    .. data:: crypto_flag_cook = 3

    	In autokey, this flag is set when the cookie is received  and validated

    	when set, keylists with  nonzero cookies are generated, 

    	when reset cookie is zero

    .. data:: crypto_flag_auto = 4

    	In autokey, this flag is set when autokey values are received and validated,

    	when set client can validate packets without extension field 

    	according to the autokey sequence

    .. data:: crypto_flag_cert = 5

    	In autokey, this flag is set when trusted host certificate and public key are verified

    """

    crypto_flag_sig = Enum.YLeaf(0, "crypto-flag-sig")

    crypto_flag_leap = Enum.YLeaf(1, "crypto-flag-leap")

    crypto_flag_vrfy = Enum.YLeaf(2, "crypto-flag-vrfy")

    crypto_flag_cook = Enum.YLeaf(3, "crypto-flag-cook")

    crypto_flag_auto = Enum.YLeaf(4, "crypto-flag-auto")

    crypto_flag_cert = Enum.YLeaf(5, "crypto-flag-cert")


class RefClockSourceType(Enum):
    """
    RefClockSourceType (Enum Class)

    Clock source type for NTP

    .. data:: ntp_ref_goes = 0

    	Geosynchronous Orbit Environment Satellite

    .. data:: ntp_ref_gps = 1

    	Global Position System

    .. data:: ntp_ref_gal = 2

    	Galileo Positioning System

    .. data:: ntp_ref_pps = 3

    	Generic pulse-per-second

    .. data:: ntp_ref_irig = 4

    	Inter-Range Instrumentation Group

    .. data:: ntp_ref_wwvb = 5

    	LF Radio WWVB Ft. Collins

    .. data:: ntp_ref_dcf = 6

    	LF Radio DCF77 Mainflingen

    .. data:: ntp_ref_hbg = 7

    	LF Radio HBG Prangins

    .. data:: ntp_ref_msf = 8

    	LF Radio MSF Anthorn

    .. data:: ntp_ref_jjy = 9

    	LF Radio JJY Fukushima

    .. data:: ntp_ref_lorc = 10

    	MF Radio LORAN C station

    .. data:: ntp_ref_tdf = 11

    	MF Radio Allouis

    .. data:: ntp_ref_chu = 12

    	HF Radio CHU Ottawa

    .. data:: ntp_ref_wwv = 13

    	HF Radio WWV Ft. Collins

    .. data:: ntp_ref_wwvh = 14

    	HF Radio WWVH Kauai

    .. data:: ntp_ref_nist = 15

    	NIST telephone modem

    .. data:: ntp_ref_acts = 16

    	NIST telephone modem

    .. data:: ntp_ref_usno = 17

    	USNO telephone modem

    .. data:: ntp_ref_ptb = 18

    	European telephone modem

    """

    ntp_ref_goes = Enum.YLeaf(0, "ntp-ref-goes")

    ntp_ref_gps = Enum.YLeaf(1, "ntp-ref-gps")

    ntp_ref_gal = Enum.YLeaf(2, "ntp-ref-gal")

    ntp_ref_pps = Enum.YLeaf(3, "ntp-ref-pps")

    ntp_ref_irig = Enum.YLeaf(4, "ntp-ref-irig")

    ntp_ref_wwvb = Enum.YLeaf(5, "ntp-ref-wwvb")

    ntp_ref_dcf = Enum.YLeaf(6, "ntp-ref-dcf")

    ntp_ref_hbg = Enum.YLeaf(7, "ntp-ref-hbg")

    ntp_ref_msf = Enum.YLeaf(8, "ntp-ref-msf")

    ntp_ref_jjy = Enum.YLeaf(9, "ntp-ref-jjy")

    ntp_ref_lorc = Enum.YLeaf(10, "ntp-ref-lorc")

    ntp_ref_tdf = Enum.YLeaf(11, "ntp-ref-tdf")

    ntp_ref_chu = Enum.YLeaf(12, "ntp-ref-chu")

    ntp_ref_wwv = Enum.YLeaf(13, "ntp-ref-wwv")

    ntp_ref_wwvh = Enum.YLeaf(14, "ntp-ref-wwvh")

    ntp_ref_nist = Enum.YLeaf(15, "ntp-ref-nist")

    ntp_ref_acts = Enum.YLeaf(16, "ntp-ref-acts")

    ntp_ref_usno = Enum.YLeaf(17, "ntp-ref-usno")

    ntp_ref_ptb = Enum.YLeaf(18, "ntp-ref-ptb")


class RefidPktTypeInfo(Enum):
    """
    RefidPktTypeInfo (Enum Class)

    The type of information stored in the refid

    .. data:: ntp_ref_state_kod = 0

    	Kiss of Death code or KOD contains debug or maintenance code. Refid is set to these codes in stratums 0 and 16 (unspec,invalid, unsync)

    .. data:: ntp_ref_state_resolved_with_clk_source = 1

    	CLK Source type occurs for all primary time servers in stratum 1

    .. data:: ntp_ref_state_resolved_with_ip_addr = 2

    	IP address occurs for clients in stratums >= 2 and  <=15 

    .. data:: ntp_ref_state_bad_state = 3

    	Bad state which serves as a default criterion for  a complete mismatch with all cases

    """

    ntp_ref_state_kod = Enum.YLeaf(0, "ntp-ref-state-kod")

    ntp_ref_state_resolved_with_clk_source = Enum.YLeaf(1, "ntp-ref-state-resolved-with-clk-source")

    ntp_ref_state_resolved_with_ip_addr = Enum.YLeaf(2, "ntp-ref-state-resolved-with-ip-addr")

    ntp_ref_state_bad_state = Enum.YLeaf(3, "ntp-ref-state-bad-state")


class ServerType(Enum):
    """
    ServerType (Enum Class)

    Status of remote entity whether server or peer

    .. data:: ntp_peer = 0

    	Remote entity is a NTP peer

    .. data:: ntp_server = 1

    	Remote NTP is a NTP server

    .. data:: ntp_unknown_type = 2

    	Status of remote entity could not be found

    """

    ntp_peer = Enum.YLeaf(0, "ntp-peer")

    ntp_server = Enum.YLeaf(1, "ntp-server")

    ntp_unknown_type = Enum.YLeaf(2, "ntp-unknown-type")



class NtpOperData(Entity):
    """
    NTP operational data
    
    .. attribute:: ntp_status_info
    
    	Contains ntp status info for the queried switch or router  which includes reference identifier, reference time, stratum  delay and other details
    	**type**\:  :py:class:`NtpStatusInfo <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ntp_oper.NtpOperData.NtpStatusInfo>`
    
    	**presence node**\: True
    
    	**config**\: False
    
    

    """

    _prefix = 'ntp-ios-xe-oper'
    _revision = '2018-01-16'

    def __init__(self):
        super(NtpOperData, self).__init__()
        self._top_entity = None

        self.yang_name = "ntp-oper-data"
        self.yang_parent_name = "Cisco-IOS-XE-ntp-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("ntp-status-info", ("ntp_status_info", NtpOperData.NtpStatusInfo))])
        self._leafs = OrderedDict()

        self.ntp_status_info = None
        self._children_name_map["ntp_status_info"] = "ntp-status-info"
        self._segment_path = lambda: "Cisco-IOS-XE-ntp-oper:ntp-oper-data"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(NtpOperData, [], name, value)


    class NtpStatusInfo(Entity):
        """
        Contains ntp status info for the queried switch or router 
        which includes reference identifier, reference time, stratum 
        delay and other details
        
        .. attribute:: refid
        
        	Reference id can either be a KOD code or a clock source or an IP address
        	**type**\:  :py:class:`Refid <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ntp_oper.NtpOperData.NtpStatusInfo.Refid>`
        
        	**config**\: False
        
        .. attribute:: reftime
        
        	Unix calendar time
        	**type**\: str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        	**config**\: False
        
        .. attribute:: sys_poll
        
        	Frequency or periodicity of NTP polling in seconds expressed as a power of two as per model and rfc
        	**type**\: int
        
        	**range:** 0..255
        
        	**config**\: False
        
        .. attribute:: stratum
        
        	How far away the current switch is in term of hops  from the primary time source of the subnet or from the root of the subnet
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: root_delay
        
        	Round trip delay with respect to the primary time server
        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
        
        	**range:** \-92233720368547758.08..92233720368547758.07
        
        	**config**\: False
        
        .. attribute:: root_disp
        
        	Deviation of offset with respect to time. All measurements are between the current switch and the root of the subnet
        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
        
        	**range:** \-92233720368547758.08..92233720368547758.07
        
        	**config**\: False
        
        .. attribute:: offset
        
        	Difference in time between current switch and peer and server clock
        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
        
        	**range:** \-92233720368547758.08..92233720368547758.07
        
        	**config**\: False
        
        .. attribute:: ntp_associations
        
        	Table of NTP associations with servers and peers
        	**type**\: list of  		 :py:class:`NtpAssociations <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ntp_oper.NtpOperData.NtpStatusInfo.NtpAssociations>`
        
        	**config**\: False
        
        .. attribute:: freq_drift_ppm
        
        	The second derivative of offset with time. In NTP version 4, this is always 0
        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
        
        	**range:** \-92233720368547758.08..92233720368547758.07
        
        	**config**\: False
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ntp-ios-xe-oper'
        _revision = '2018-01-16'

        def __init__(self):
            super(NtpOperData.NtpStatusInfo, self).__init__()

            self.yang_name = "ntp-status-info"
            self.yang_parent_name = "ntp-oper-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("refid", ("refid", NtpOperData.NtpStatusInfo.Refid)), ("ntp-associations", ("ntp_associations", NtpOperData.NtpStatusInfo.NtpAssociations))])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('reftime', (YLeaf(YType.str, 'reftime'), ['str'])),
                ('sys_poll', (YLeaf(YType.uint8, 'sys-poll'), ['int'])),
                ('stratum', (YLeaf(YType.uint32, 'stratum'), ['int'])),
                ('root_delay', (YLeaf(YType.str, 'root-delay'), ['Decimal64'])),
                ('root_disp', (YLeaf(YType.str, 'root-disp'), ['Decimal64'])),
                ('offset', (YLeaf(YType.str, 'offset'), ['Decimal64'])),
                ('freq_drift_ppm', (YLeaf(YType.str, 'freq-drift-ppm'), ['Decimal64'])),
            ])
            self.reftime = None
            self.sys_poll = None
            self.stratum = None
            self.root_delay = None
            self.root_disp = None
            self.offset = None
            self.freq_drift_ppm = None

            self.refid = NtpOperData.NtpStatusInfo.Refid()
            self.refid.parent = self
            self._children_name_map["refid"] = "refid"

            self.ntp_associations = YList(self)
            self._segment_path = lambda: "ntp-status-info"
            self._absolute_path = lambda: "Cisco-IOS-XE-ntp-oper:ntp-oper-data/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(NtpOperData.NtpStatusInfo, ['reftime', 'sys_poll', 'stratum', 'root_delay', 'root_disp', 'offset', 'freq_drift_ppm'], name, value)


        class Refid(Entity):
            """
            Reference id can either be a KOD code or a clock source or an IP address
            
            .. attribute:: ip_addr
            
            	IPV4 or IPV6 ip address
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            		**type**\: str
            
            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            	**config**\: False
            
            .. attribute:: kod_data
            
            	Container for KOD type eg INIT ACTS
            	**type**\:  :py:class:`KodData <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ntp_oper.NtpOperData.NtpStatusInfo.Refid.KodData>`
            
            	**config**\: False
            
            .. attribute:: ref_clk_src_data
            
            	Container for clock data. GPS is the only source supported by Cisco currrently
            	**type**\:  :py:class:`RefClkSrcData <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ntp_oper.NtpOperData.NtpStatusInfo.Refid.RefClkSrcData>`
            
            	**config**\: False
            
            .. attribute:: exception_code
            
            	Bad stat or exception code in case the 3 criteria of ip, clock and kod don't match
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'ntp-ios-xe-oper'
            _revision = '2018-01-16'

            def __init__(self):
                super(NtpOperData.NtpStatusInfo.Refid, self).__init__()

                self.yang_name = "refid"
                self.yang_parent_name = "ntp-status-info"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("kod-data", ("kod_data", NtpOperData.NtpStatusInfo.Refid.KodData)), ("ref-clk-src-data", ("ref_clk_src_data", NtpOperData.NtpStatusInfo.Refid.RefClkSrcData))])
                self._leafs = OrderedDict([
                    ('ip_addr', (YLeaf(YType.str, 'ip-addr'), ['str','str'])),
                    ('exception_code', (YLeaf(YType.uint32, 'exception-code'), ['int'])),
                ])
                self.ip_addr = None
                self.exception_code = None

                self.kod_data = NtpOperData.NtpStatusInfo.Refid.KodData()
                self.kod_data.parent = self
                self._children_name_map["kod_data"] = "kod-data"

                self.ref_clk_src_data = NtpOperData.NtpStatusInfo.Refid.RefClkSrcData()
                self.ref_clk_src_data.parent = self
                self._children_name_map["ref_clk_src_data"] = "ref-clk-src-data"
                self._segment_path = lambda: "refid"
                self._absolute_path = lambda: "Cisco-IOS-XE-ntp-oper:ntp-oper-data/ntp-status-info/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(NtpOperData.NtpStatusInfo.Refid, ['ip_addr', 'exception_code'], name, value)


            class KodData(Entity):
                """
                Container for KOD type eg INIT ACTS
                
                .. attribute:: kod_type
                
                	KOD types could be any of  the enums including INIT   ACTS etc
                	**type**\:  :py:class:`KissCodeType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ntp_oper.KissCodeType>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ntp-ios-xe-oper'
                _revision = '2018-01-16'

                def __init__(self):
                    super(NtpOperData.NtpStatusInfo.Refid.KodData, self).__init__()

                    self.yang_name = "kod-data"
                    self.yang_parent_name = "refid"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('kod_type', (YLeaf(YType.enumeration, 'kod-type'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_ntp_oper', 'KissCodeType', '')])),
                    ])
                    self.kod_type = None
                    self._segment_path = lambda: "kod-data"
                    self._absolute_path = lambda: "Cisco-IOS-XE-ntp-oper:ntp-oper-data/ntp-status-info/refid/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(NtpOperData.NtpStatusInfo.Refid.KodData, ['kod_type'], name, value)



            class RefClkSrcData(Entity):
                """
                Container for clock data. GPS is the only source supported by Cisco currrently
                
                .. attribute:: ref_clk_src_type
                
                	Contains clock source type specifics eg GPS and container extensions
                	**type**\:  :py:class:`RefClockSourceType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ntp_oper.RefClockSourceType>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ntp-ios-xe-oper'
                _revision = '2018-01-16'

                def __init__(self):
                    super(NtpOperData.NtpStatusInfo.Refid.RefClkSrcData, self).__init__()

                    self.yang_name = "ref-clk-src-data"
                    self.yang_parent_name = "refid"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('ref_clk_src_type', (YLeaf(YType.enumeration, 'ref-clk-src-type'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_ntp_oper', 'RefClockSourceType', '')])),
                    ])
                    self.ref_clk_src_type = None
                    self._segment_path = lambda: "ref-clk-src-data"
                    self._absolute_path = lambda: "Cisco-IOS-XE-ntp-oper:ntp-oper-data/ntp-status-info/refid/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(NtpOperData.NtpStatusInfo.Refid.RefClkSrcData, ['ref_clk_src_type'], name, value)




        class NtpAssociations(Entity):
            """
            Table of NTP associations with servers and peers
            
            .. attribute:: assoc_id  (key)
            
            	Association id is a descriptor which describes the association between two NTP entities whether client and peer or client and server
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: peer_reach
            
            	The status of the last 8 NTP packet exchanges with peers. 1 is encoded in the bitmask for a successful attempt and 0 is encoded for failure. If all the last 8 transactions with peers or messages sent to peers are successful the encoding becomes 0xff
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: peer_stratum
            
            	Stratum in which the peer exists
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: refid
            
            	refid refers to either an IP address or a clock source or KOD type code
            	**type**\:  :py:class:`Refid <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ntp_oper.NtpOperData.NtpStatusInfo.NtpAssociations.Refid>`
            
            	**config**\: False
            
            .. attribute:: reftime
            
            	Reference UNIX calendar time
            	**type**\: str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            	**config**\: False
            
            .. attribute:: last_poll_time
            
            	The time of  the last NTP poll or update that happened in seconds. How many seconds back did the last update happen or when did the last NTP update happen ?
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: poll
            
            	Maximum poll time of NTP in seconds expressed as a power of two as per model and RFC
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: delay
            
            	Round trip delay of reaching the peer and returning
            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
            
            	**range:** \-92233720368547758.08..92233720368547758.07
            
            	**config**\: False
            
            .. attribute:: offset
            
            	Difference in ms between server time and local time. offset with respect to the peer/server clock
            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
            
            	**range:** \-92233720368547758.08..92233720368547758.07
            
            	**config**\: False
            
            .. attribute:: jitter
            
            	Jitter in ms refers to short\-term variations in frequency of components greater than 10 hz
            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
            
            	**range:** \-92233720368547758.08..92233720368547758.07
            
            	**config**\: False
            
            .. attribute:: ntp_address
            
            	NTP address consists of an IP address and a VRF name
            	**type**\:  :py:class:`NtpAddress <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ntp_oper.NtpOperData.NtpStatusInfo.NtpAssociations.NtpAddress>`
            
            	**config**\: False
            
            .. attribute:: num_events
            
            	Count of number of error events received from peer
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: last_peer_event
            
            	Last event received from peer
            	**type**\:  :py:class:`PeerEvent <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ntp_oper.PeerEvent>`
            
            	**config**\: False
            
            .. attribute:: peer_selection_status
            
            	Status of peer selection based on the NTP selection  algorithm
            	**type**\:  :py:class:`PeerSelectStatus <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ntp_oper.PeerSelectStatus>`
            
            	**config**\: False
            
            .. attribute:: peer_authentication_status
            
            	Status of authentication of switch or router by peer
            	**type**\:  :py:class:`PeerAuthStatus <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ntp_oper.PeerAuthStatus>`
            
            	**config**\: False
            
            .. attribute:: serv_type
            
            	Whether the remote NTP device is a server or peer
            	**type**\:  :py:class:`ServerType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ntp_oper.ServerType>`
            
            	**config**\: False
            
            .. attribute:: psw_crypto
            
            	Peer status word of ntp server or peer when authentication configured
            	**type**\:  :py:class:`PeerStatusWord <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ntp_oper.PeerStatusWord>`
            
            	**config**\: False
            
            

            """

            _prefix = 'ntp-ios-xe-oper'
            _revision = '2018-01-16'

            def __init__(self):
                super(NtpOperData.NtpStatusInfo.NtpAssociations, self).__init__()

                self.yang_name = "ntp-associations"
                self.yang_parent_name = "ntp-status-info"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['assoc_id']
                self._child_classes = OrderedDict([("refid", ("refid", NtpOperData.NtpStatusInfo.NtpAssociations.Refid)), ("ntp-address", ("ntp_address", NtpOperData.NtpStatusInfo.NtpAssociations.NtpAddress))])
                self._leafs = OrderedDict([
                    ('assoc_id', (YLeaf(YType.uint16, 'assoc-id'), ['int'])),
                    ('peer_reach', (YLeaf(YType.uint8, 'peer-reach'), ['int'])),
                    ('peer_stratum', (YLeaf(YType.uint32, 'peer-stratum'), ['int'])),
                    ('reftime', (YLeaf(YType.str, 'reftime'), ['str'])),
                    ('last_poll_time', (YLeaf(YType.uint64, 'last-poll-time'), ['int'])),
                    ('poll', (YLeaf(YType.uint32, 'poll'), ['int'])),
                    ('delay', (YLeaf(YType.str, 'delay'), ['Decimal64'])),
                    ('offset', (YLeaf(YType.str, 'offset'), ['Decimal64'])),
                    ('jitter', (YLeaf(YType.str, 'jitter'), ['Decimal64'])),
                    ('num_events', (YLeaf(YType.uint8, 'num-events'), ['int'])),
                    ('last_peer_event', (YLeaf(YType.enumeration, 'last-peer-event'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_ntp_oper', 'PeerEvent', '')])),
                    ('peer_selection_status', (YLeaf(YType.enumeration, 'peer-selection-status'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_ntp_oper', 'PeerSelectStatus', '')])),
                    ('peer_authentication_status', (YLeaf(YType.enumeration, 'peer-authentication-status'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_ntp_oper', 'PeerAuthStatus', '')])),
                    ('serv_type', (YLeaf(YType.enumeration, 'serv-type'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_ntp_oper', 'ServerType', '')])),
                    ('psw_crypto', (YLeaf(YType.enumeration, 'psw-crypto'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_ntp_oper', 'PeerStatusWord', '')])),
                ])
                self.assoc_id = None
                self.peer_reach = None
                self.peer_stratum = None
                self.reftime = None
                self.last_poll_time = None
                self.poll = None
                self.delay = None
                self.offset = None
                self.jitter = None
                self.num_events = None
                self.last_peer_event = None
                self.peer_selection_status = None
                self.peer_authentication_status = None
                self.serv_type = None
                self.psw_crypto = None

                self.refid = NtpOperData.NtpStatusInfo.NtpAssociations.Refid()
                self.refid.parent = self
                self._children_name_map["refid"] = "refid"

                self.ntp_address = NtpOperData.NtpStatusInfo.NtpAssociations.NtpAddress()
                self.ntp_address.parent = self
                self._children_name_map["ntp_address"] = "ntp-address"
                self._segment_path = lambda: "ntp-associations" + "[assoc-id='" + str(self.assoc_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XE-ntp-oper:ntp-oper-data/ntp-status-info/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(NtpOperData.NtpStatusInfo.NtpAssociations, ['assoc_id', 'peer_reach', 'peer_stratum', 'reftime', 'last_poll_time', 'poll', 'delay', 'offset', 'jitter', 'num_events', 'last_peer_event', 'peer_selection_status', 'peer_authentication_status', 'serv_type', 'psw_crypto'], name, value)


            class Refid(Entity):
                """
                refid refers to either an IP address or a clock source or KOD type code
                
                .. attribute:: ip_addr
                
                	IPV4 or IPV6 ip address
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                	**config**\: False
                
                .. attribute:: kod_data
                
                	Container for KOD type eg INIT ACTS
                	**type**\:  :py:class:`KodData <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ntp_oper.NtpOperData.NtpStatusInfo.NtpAssociations.Refid.KodData>`
                
                	**config**\: False
                
                .. attribute:: ref_clk_src_data
                
                	Container for clock data. GPS is the only source supported by Cisco currrently
                	**type**\:  :py:class:`RefClkSrcData <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ntp_oper.NtpOperData.NtpStatusInfo.NtpAssociations.Refid.RefClkSrcData>`
                
                	**config**\: False
                
                .. attribute:: exception_code
                
                	Bad stat or exception code in case the 3 criteria of ip, clock and kod don't match
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'ntp-ios-xe-oper'
                _revision = '2018-01-16'

                def __init__(self):
                    super(NtpOperData.NtpStatusInfo.NtpAssociations.Refid, self).__init__()

                    self.yang_name = "refid"
                    self.yang_parent_name = "ntp-associations"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("kod-data", ("kod_data", NtpOperData.NtpStatusInfo.NtpAssociations.Refid.KodData)), ("ref-clk-src-data", ("ref_clk_src_data", NtpOperData.NtpStatusInfo.NtpAssociations.Refid.RefClkSrcData))])
                    self._leafs = OrderedDict([
                        ('ip_addr', (YLeaf(YType.str, 'ip-addr'), ['str','str'])),
                        ('exception_code', (YLeaf(YType.uint32, 'exception-code'), ['int'])),
                    ])
                    self.ip_addr = None
                    self.exception_code = None

                    self.kod_data = NtpOperData.NtpStatusInfo.NtpAssociations.Refid.KodData()
                    self.kod_data.parent = self
                    self._children_name_map["kod_data"] = "kod-data"

                    self.ref_clk_src_data = NtpOperData.NtpStatusInfo.NtpAssociations.Refid.RefClkSrcData()
                    self.ref_clk_src_data.parent = self
                    self._children_name_map["ref_clk_src_data"] = "ref-clk-src-data"
                    self._segment_path = lambda: "refid"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(NtpOperData.NtpStatusInfo.NtpAssociations.Refid, ['ip_addr', 'exception_code'], name, value)


                class KodData(Entity):
                    """
                    Container for KOD type eg INIT ACTS
                    
                    .. attribute:: kod_type
                    
                    	KOD types could be any of  the enums including INIT   ACTS etc
                    	**type**\:  :py:class:`KissCodeType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ntp_oper.KissCodeType>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ntp-ios-xe-oper'
                    _revision = '2018-01-16'

                    def __init__(self):
                        super(NtpOperData.NtpStatusInfo.NtpAssociations.Refid.KodData, self).__init__()

                        self.yang_name = "kod-data"
                        self.yang_parent_name = "refid"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('kod_type', (YLeaf(YType.enumeration, 'kod-type'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_ntp_oper', 'KissCodeType', '')])),
                        ])
                        self.kod_type = None
                        self._segment_path = lambda: "kod-data"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(NtpOperData.NtpStatusInfo.NtpAssociations.Refid.KodData, ['kod_type'], name, value)



                class RefClkSrcData(Entity):
                    """
                    Container for clock data. GPS is the only source supported by Cisco currrently
                    
                    .. attribute:: ref_clk_src_type
                    
                    	Contains clock source type specifics eg GPS and container extensions
                    	**type**\:  :py:class:`RefClockSourceType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ntp_oper.RefClockSourceType>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ntp-ios-xe-oper'
                    _revision = '2018-01-16'

                    def __init__(self):
                        super(NtpOperData.NtpStatusInfo.NtpAssociations.Refid.RefClkSrcData, self).__init__()

                        self.yang_name = "ref-clk-src-data"
                        self.yang_parent_name = "refid"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('ref_clk_src_type', (YLeaf(YType.enumeration, 'ref-clk-src-type'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_ntp_oper', 'RefClockSourceType', '')])),
                        ])
                        self.ref_clk_src_type = None
                        self._segment_path = lambda: "ref-clk-src-data"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(NtpOperData.NtpStatusInfo.NtpAssociations.Refid.RefClkSrcData, ['ref_clk_src_type'], name, value)




            class NtpAddress(Entity):
                """
                NTP address consists of an IP address and a VRF name
                
                .. attribute:: ip_addr
                
                	IP address is the IP address of  the NTP server or peer
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                	**config**\: False
                
                .. attribute:: vrf_name
                
                	VRF name is the virtual routing instance through which we can find the ntp server or peer
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'ntp-ios-xe-oper'
                _revision = '2018-01-16'

                def __init__(self):
                    super(NtpOperData.NtpStatusInfo.NtpAssociations.NtpAddress, self).__init__()

                    self.yang_name = "ntp-address"
                    self.yang_parent_name = "ntp-associations"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('ip_addr', (YLeaf(YType.str, 'ip-addr'), ['str','str'])),
                        ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                    ])
                    self.ip_addr = None
                    self.vrf_name = None
                    self._segment_path = lambda: "ntp-address"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(NtpOperData.NtpStatusInfo.NtpAssociations.NtpAddress, ['ip_addr', 'vrf_name'], name, value)




    def clone_ptr(self):
        self._top_entity = NtpOperData()
        return self._top_entity




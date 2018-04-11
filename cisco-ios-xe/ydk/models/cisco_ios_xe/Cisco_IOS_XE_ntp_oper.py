""" Cisco_IOS_XE_ntp_oper 

This module contains a collection of YANG definitions
for NTP operational data.
Copyright (c) 2017 by Cisco Systems, Inc.
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



class NtpOperData(Entity):
    """
    NTP operational data
    
    .. attribute:: ntp_status_info
    
    	Contains ntp status info for the queried switch or router  which includes reference identifier, reference time, stratum  delay and other details
    	**type**\:  :py:class:`NtpStatusInfo <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ntp_oper.NtpOperData.NtpStatusInfo>`
    
    	**presence node**\: True
    
    

    """

    _prefix = 'ntp-ios-xe-oper'
    _revision = '2017-11-01'

    def __init__(self):
        super(NtpOperData, self).__init__()
        self._top_entity = None

        self.yang_name = "ntp-oper-data"
        self.yang_parent_name = "Cisco-IOS-XE-ntp-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("ntp-status-info", ("ntp_status_info", NtpOperData.NtpStatusInfo))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.ntp_status_info = None
        self._children_name_map["ntp_status_info"] = "ntp-status-info"
        self._children_yang_names.add("ntp-status-info")
        self._segment_path = lambda: "Cisco-IOS-XE-ntp-oper:ntp-oper-data"


    class NtpStatusInfo(Entity):
        """
        Contains ntp status info for the queried switch or router 
        which includes reference identifier, reference time, stratum 
        delay and other details
        
        .. attribute:: refid
        
        	Reference id can either be a KOD code or a clock source or an IP address
        	**type**\:  :py:class:`Refid <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ntp_oper.NtpOperData.NtpStatusInfo.Refid>`
        
        .. attribute:: reftime
        
        	Unix calendar time
        	**type**\: str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: sys_poll
        
        	Frequency or periodicity of NTP polling in seconds
        	**type**\: int
        
        	**range:** 0..255
        
        .. attribute:: stratum
        
        	How far away the current switch is in term of hops  from the primary time source of the subnet or from the root of the subnet
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: root_delay
        
        	Round trip delay with respect to the primary time server
        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
        
        	**range:** \-92233720368547758.08..92233720368547758.07
        
        .. attribute:: root_disp
        
        	Deviation of offset with respect to time. All measurements are between the current switch and the root of the subnet
        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
        
        	**range:** \-92233720368547758.08..92233720368547758.07
        
        .. attribute:: offset
        
        	Difference in time between current switch and peer and server clock
        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
        
        	**range:** \-92233720368547758.08..92233720368547758.07
        
        .. attribute:: ntp_associations
        
        	Table of NTP associations with servers and peers
        	**type**\: list of  		 :py:class:`NtpAssociations <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ntp_oper.NtpOperData.NtpStatusInfo.NtpAssociations>`
        
        .. attribute:: freq_drift_ppm
        
        	The second derivative of offset with time. In NTP version 4, this is always 0
        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
        
        	**range:** \-92233720368547758.08..92233720368547758.07
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ntp-ios-xe-oper'
        _revision = '2017-11-01'

        def __init__(self):
            super(NtpOperData.NtpStatusInfo, self).__init__()

            self.yang_name = "ntp-status-info"
            self.yang_parent_name = "ntp-oper-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("refid", ("refid", NtpOperData.NtpStatusInfo.Refid))])
            self._child_list_classes = OrderedDict([("ntp-associations", ("ntp_associations", NtpOperData.NtpStatusInfo.NtpAssociations))])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('reftime', YLeaf(YType.str, 'reftime')),
                ('sys_poll', YLeaf(YType.uint8, 'sys-poll')),
                ('stratum', YLeaf(YType.uint32, 'stratum')),
                ('root_delay', YLeaf(YType.str, 'root-delay')),
                ('root_disp', YLeaf(YType.str, 'root-disp')),
                ('offset', YLeaf(YType.str, 'offset')),
                ('freq_drift_ppm', YLeaf(YType.str, 'freq-drift-ppm')),
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
            self._children_yang_names.add("refid")

            self.ntp_associations = YList(self)
            self._segment_path = lambda: "ntp-status-info"
            self._absolute_path = lambda: "Cisco-IOS-XE-ntp-oper:ntp-oper-data/%s" % self._segment_path()

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
            
            .. attribute:: kod_data
            
            	Container for KOD type eg INIT ACTS
            	**type**\:  :py:class:`KodData <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ntp_oper.NtpOperData.NtpStatusInfo.Refid.KodData>`
            
            .. attribute:: ref_clk_src_data
            
            	Container for clock data. GPS is the only source supported by Cisco currrently
            	**type**\:  :py:class:`RefClkSrcData <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ntp_oper.NtpOperData.NtpStatusInfo.Refid.RefClkSrcData>`
            
            .. attribute:: exception_code
            
            	Bad stat or exception code in case the 3 criteria of ip, clock and kod don't match
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'ntp-ios-xe-oper'
            _revision = '2017-11-01'

            def __init__(self):
                super(NtpOperData.NtpStatusInfo.Refid, self).__init__()

                self.yang_name = "refid"
                self.yang_parent_name = "ntp-status-info"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("kod-data", ("kod_data", NtpOperData.NtpStatusInfo.Refid.KodData)), ("ref-clk-src-data", ("ref_clk_src_data", NtpOperData.NtpStatusInfo.Refid.RefClkSrcData))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ip_addr', YLeaf(YType.str, 'ip-addr')),
                    ('exception_code', YLeaf(YType.uint32, 'exception-code')),
                ])
                self.ip_addr = None
                self.exception_code = None

                self.kod_data = NtpOperData.NtpStatusInfo.Refid.KodData()
                self.kod_data.parent = self
                self._children_name_map["kod_data"] = "kod-data"
                self._children_yang_names.add("kod-data")

                self.ref_clk_src_data = NtpOperData.NtpStatusInfo.Refid.RefClkSrcData()
                self.ref_clk_src_data.parent = self
                self._children_name_map["ref_clk_src_data"] = "ref-clk-src-data"
                self._children_yang_names.add("ref-clk-src-data")
                self._segment_path = lambda: "refid"
                self._absolute_path = lambda: "Cisco-IOS-XE-ntp-oper:ntp-oper-data/ntp-status-info/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(NtpOperData.NtpStatusInfo.Refid, ['ip_addr', 'exception_code'], name, value)


            class KodData(Entity):
                """
                Container for KOD type eg INIT ACTS
                
                .. attribute:: kod_type
                
                	KOD types could be any of  the enums including INIT   ACTS etc
                	**type**\:  :py:class:`KissCodeType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ntp_oper.KissCodeType>`
                
                

                """

                _prefix = 'ntp-ios-xe-oper'
                _revision = '2017-11-01'

                def __init__(self):
                    super(NtpOperData.NtpStatusInfo.Refid.KodData, self).__init__()

                    self.yang_name = "kod-data"
                    self.yang_parent_name = "refid"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('kod_type', YLeaf(YType.enumeration, 'kod-type')),
                    ])
                    self.kod_type = None
                    self._segment_path = lambda: "kod-data"
                    self._absolute_path = lambda: "Cisco-IOS-XE-ntp-oper:ntp-oper-data/ntp-status-info/refid/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(NtpOperData.NtpStatusInfo.Refid.KodData, ['kod_type'], name, value)


            class RefClkSrcData(Entity):
                """
                Container for clock data. GPS is the only source supported by Cisco currrently
                
                .. attribute:: ref_clk_src_type
                
                	Contains clock source type specifics eg GPS and container extensions
                	**type**\:  :py:class:`RefClockSourceType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ntp_oper.RefClockSourceType>`
                
                

                """

                _prefix = 'ntp-ios-xe-oper'
                _revision = '2017-11-01'

                def __init__(self):
                    super(NtpOperData.NtpStatusInfo.Refid.RefClkSrcData, self).__init__()

                    self.yang_name = "ref-clk-src-data"
                    self.yang_parent_name = "refid"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('ref_clk_src_type', YLeaf(YType.enumeration, 'ref-clk-src-type')),
                    ])
                    self.ref_clk_src_type = None
                    self._segment_path = lambda: "ref-clk-src-data"
                    self._absolute_path = lambda: "Cisco-IOS-XE-ntp-oper:ntp-oper-data/ntp-status-info/refid/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(NtpOperData.NtpStatusInfo.Refid.RefClkSrcData, ['ref_clk_src_type'], name, value)


        class NtpAssociations(Entity):
            """
            Table of NTP associations with servers and peers
            
            .. attribute:: assoc_id  (key)
            
            	Association id is a descriptor which describes the association between two NTP entities whether client and peer or client and server
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: peer_reach
            
            	The status of the last 8 NTP packet exchanges with peers. 1 is encoded in the bitmask for a successful attempt and 0 is encoded for failure. If all the last 8 transactions with peers or messages sent to peers are successful the encoding becomes 0xff
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: peer_stratum
            
            	Stratum in which the peer exists
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: refid
            
            	refid refers to either an IP address or a clock source or KOD type code
            	**type**\:  :py:class:`Refid <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ntp_oper.NtpOperData.NtpStatusInfo.NtpAssociations.Refid>`
            
            .. attribute:: reftime
            
            	Reference UNIX calendar time
            	**type**\: str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            .. attribute:: last_poll_time
            
            	The time of  the last NTP poll or update that happened in seconds. How many seconds back did the last update happen or when did the last NTP update happen ?
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: poll
            
            	Maximum poll time of NTP in seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: delay
            
            	Round trip delay of reaching the peer and returning
            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
            
            	**range:** \-92233720368547758.08..92233720368547758.07
            
            .. attribute:: offset
            
            	Difference in ms between server time and local time. offset with respect to the peer/server clock
            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
            
            	**range:** \-92233720368547758.08..92233720368547758.07
            
            .. attribute:: jitter
            
            	Jitter in ms refers to short\-term variations in frequency of components greater than 10 hz
            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
            
            	**range:** \-92233720368547758.08..92233720368547758.07
            
            

            """

            _prefix = 'ntp-ios-xe-oper'
            _revision = '2017-11-01'

            def __init__(self):
                super(NtpOperData.NtpStatusInfo.NtpAssociations, self).__init__()

                self.yang_name = "ntp-associations"
                self.yang_parent_name = "ntp-status-info"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['assoc_id']
                self._child_container_classes = OrderedDict([("refid", ("refid", NtpOperData.NtpStatusInfo.NtpAssociations.Refid))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('assoc_id', YLeaf(YType.uint16, 'assoc-id')),
                    ('peer_reach', YLeaf(YType.uint8, 'peer-reach')),
                    ('peer_stratum', YLeaf(YType.uint32, 'peer-stratum')),
                    ('reftime', YLeaf(YType.str, 'reftime')),
                    ('last_poll_time', YLeaf(YType.uint64, 'last-poll-time')),
                    ('poll', YLeaf(YType.uint32, 'poll')),
                    ('delay', YLeaf(YType.str, 'delay')),
                    ('offset', YLeaf(YType.str, 'offset')),
                    ('jitter', YLeaf(YType.str, 'jitter')),
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

                self.refid = NtpOperData.NtpStatusInfo.NtpAssociations.Refid()
                self.refid.parent = self
                self._children_name_map["refid"] = "refid"
                self._children_yang_names.add("refid")
                self._segment_path = lambda: "ntp-associations" + "[assoc-id='" + str(self.assoc_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XE-ntp-oper:ntp-oper-data/ntp-status-info/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(NtpOperData.NtpStatusInfo.NtpAssociations, ['assoc_id', 'peer_reach', 'peer_stratum', 'reftime', 'last_poll_time', 'poll', 'delay', 'offset', 'jitter'], name, value)


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
                
                .. attribute:: kod_data
                
                	Container for KOD type eg INIT ACTS
                	**type**\:  :py:class:`KodData <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ntp_oper.NtpOperData.NtpStatusInfo.NtpAssociations.Refid.KodData>`
                
                .. attribute:: ref_clk_src_data
                
                	Container for clock data. GPS is the only source supported by Cisco currrently
                	**type**\:  :py:class:`RefClkSrcData <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ntp_oper.NtpOperData.NtpStatusInfo.NtpAssociations.Refid.RefClkSrcData>`
                
                .. attribute:: exception_code
                
                	Bad stat or exception code in case the 3 criteria of ip, clock and kod don't match
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ntp-ios-xe-oper'
                _revision = '2017-11-01'

                def __init__(self):
                    super(NtpOperData.NtpStatusInfo.NtpAssociations.Refid, self).__init__()

                    self.yang_name = "refid"
                    self.yang_parent_name = "ntp-associations"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("kod-data", ("kod_data", NtpOperData.NtpStatusInfo.NtpAssociations.Refid.KodData)), ("ref-clk-src-data", ("ref_clk_src_data", NtpOperData.NtpStatusInfo.NtpAssociations.Refid.RefClkSrcData))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('ip_addr', YLeaf(YType.str, 'ip-addr')),
                        ('exception_code', YLeaf(YType.uint32, 'exception-code')),
                    ])
                    self.ip_addr = None
                    self.exception_code = None

                    self.kod_data = NtpOperData.NtpStatusInfo.NtpAssociations.Refid.KodData()
                    self.kod_data.parent = self
                    self._children_name_map["kod_data"] = "kod-data"
                    self._children_yang_names.add("kod-data")

                    self.ref_clk_src_data = NtpOperData.NtpStatusInfo.NtpAssociations.Refid.RefClkSrcData()
                    self.ref_clk_src_data.parent = self
                    self._children_name_map["ref_clk_src_data"] = "ref-clk-src-data"
                    self._children_yang_names.add("ref-clk-src-data")
                    self._segment_path = lambda: "refid"

                def __setattr__(self, name, value):
                    self._perform_setattr(NtpOperData.NtpStatusInfo.NtpAssociations.Refid, ['ip_addr', 'exception_code'], name, value)


                class KodData(Entity):
                    """
                    Container for KOD type eg INIT ACTS
                    
                    .. attribute:: kod_type
                    
                    	KOD types could be any of  the enums including INIT   ACTS etc
                    	**type**\:  :py:class:`KissCodeType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ntp_oper.KissCodeType>`
                    
                    

                    """

                    _prefix = 'ntp-ios-xe-oper'
                    _revision = '2017-11-01'

                    def __init__(self):
                        super(NtpOperData.NtpStatusInfo.NtpAssociations.Refid.KodData, self).__init__()

                        self.yang_name = "kod-data"
                        self.yang_parent_name = "refid"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('kod_type', YLeaf(YType.enumeration, 'kod-type')),
                        ])
                        self.kod_type = None
                        self._segment_path = lambda: "kod-data"

                    def __setattr__(self, name, value):
                        self._perform_setattr(NtpOperData.NtpStatusInfo.NtpAssociations.Refid.KodData, ['kod_type'], name, value)


                class RefClkSrcData(Entity):
                    """
                    Container for clock data. GPS is the only source supported by Cisco currrently
                    
                    .. attribute:: ref_clk_src_type
                    
                    	Contains clock source type specifics eg GPS and container extensions
                    	**type**\:  :py:class:`RefClockSourceType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ntp_oper.RefClockSourceType>`
                    
                    

                    """

                    _prefix = 'ntp-ios-xe-oper'
                    _revision = '2017-11-01'

                    def __init__(self):
                        super(NtpOperData.NtpStatusInfo.NtpAssociations.Refid.RefClkSrcData, self).__init__()

                        self.yang_name = "ref-clk-src-data"
                        self.yang_parent_name = "refid"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('ref_clk_src_type', YLeaf(YType.enumeration, 'ref-clk-src-type')),
                        ])
                        self.ref_clk_src_type = None
                        self._segment_path = lambda: "ref-clk-src-data"

                    def __setattr__(self, name, value):
                        self._perform_setattr(NtpOperData.NtpStatusInfo.NtpAssociations.Refid.RefClkSrcData, ['ref_clk_src_type'], name, value)

    def clone_ptr(self):
        self._top_entity = NtpOperData()
        return self._top_entity


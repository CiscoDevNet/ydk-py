""" Cisco_IOS_XR_ip_ntp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-ntp package operational data.

This module contains definitions
for the following management objects\:
  ntp\: NTP operational data

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class ClockUpdateNodeEnum(Enum):
    """
    ClockUpdateNodeEnum

    Mode of Clock Update

    .. data:: CLK_NEVER_UPDATED = 0

    	 clock is never updated

    .. data:: CLK_UPDATED = 1

    	 clock is updated

    .. data:: CLK_NO_UPDATE_INFO = 2

    	 clock has no update info

    """

    CLK_NEVER_UPDATED = 0

    CLK_UPDATED = 1

    CLK_NO_UPDATE_INFO = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
        return meta._meta_table['ClockUpdateNodeEnum']


class NtpLeapEnum(Enum):
    """
    NtpLeapEnum

    Type of leap

    .. data:: NTP_LEAP_NO_WARNING = 0

    	Normal, no leap second warning

    .. data:: NTP_LEAP_ADDSE_COND = 1

    	Last minute of day has 61 seconds

    .. data:: NTP_LEAP_DELSE_COND = 2

    	Last minute of day has 59 seconds

    .. data:: NTP_LEAP_NOT_IN_SYNC = 3

    	Overload, clock is free running

    """

    NTP_LEAP_NO_WARNING = 0

    NTP_LEAP_ADDSE_COND = 1

    NTP_LEAP_DELSE_COND = 2

    NTP_LEAP_NOT_IN_SYNC = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
        return meta._meta_table['NtpLeapEnum']


class NtpLoopFilterStateEnum(Enum):
    """
    NtpLoopFilterStateEnum

    Loop filter state

    .. data:: NTP_LOOP_FLT_N_SET = 0

    	 never set

    .. data:: NTP_LOOP_FLT_F_SET = 1

    	 drift set from file

    .. data:: NTP_LOOP_FLT_SPIK = 2

    	 spike

    .. data:: NTP_LOOP_FLT_FREQ = 3

    	 drift being measured

    .. data:: NTP_LOOP_FLT_SYNC = 4

    	 normal controlled loop

    .. data:: NTP_LOOP_FLT_UNKN = 5

    	 unknown

    """

    NTP_LOOP_FLT_N_SET = 0

    NTP_LOOP_FLT_F_SET = 1

    NTP_LOOP_FLT_SPIK = 2

    NTP_LOOP_FLT_FREQ = 3

    NTP_LOOP_FLT_SYNC = 4

    NTP_LOOP_FLT_UNKN = 5


    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
        return meta._meta_table['NtpLoopFilterStateEnum']


class NtpModeEnum(Enum):
    """
    NtpModeEnum

    Type of mode

    .. data:: NTP_MODE_UNSPEC = 0

    	Unspecified probably old NTP version

    .. data:: NTP_MODE_SYMETRIC_ACTIVE = 1

    	Symmetric active

    .. data:: NTP_MODE_SYMETRIC_PASSIVE = 2

    	Symmetric passive

    .. data:: NTP_MODE_CLIENT = 3

    	Client mode

    .. data:: NTP_MODE_SERVER = 4

    	Server mode

    .. data:: NTP_MODE_XCAST_SERVER = 5

    	Broadcast mode

    .. data:: NTP_MODE_CONTROL = 6

    	Control mode packet

    .. data:: NTP_MODE_PRIVATE = 7

    	Implementation defined function

    .. data:: NTP_MODE_XCAST_CLIENT = 8

    	A broadcast client mode

    """

    NTP_MODE_UNSPEC = 0

    NTP_MODE_SYMETRIC_ACTIVE = 1

    NTP_MODE_SYMETRIC_PASSIVE = 2

    NTP_MODE_CLIENT = 3

    NTP_MODE_SERVER = 4

    NTP_MODE_XCAST_SERVER = 5

    NTP_MODE_CONTROL = 6

    NTP_MODE_PRIVATE = 7

    NTP_MODE_XCAST_CLIENT = 8


    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
        return meta._meta_table['NtpModeEnum']


class NtpPeerStatusEnum(Enum):
    """
    NtpPeerStatusEnum

    Type of peer status

    .. data:: NTP_CTL_PST_SEL_REJECT = 0

    	   reject

    .. data:: NTP_CTL_PST_SEL_SANE = 1

    	 x falsetick

    .. data:: NTP_CTL_PST_SEL_CORRECT = 2

    	 . excess 

    .. data:: NTP_CTL_PST_SEL_SELCAND = 3

    	 - outlyer

    .. data:: NTP_CTL_PST_SEL_SYNC_CAND = 4

    	 + candidate

    .. data:: NTP_CTL_PST_SEL_DISTSYS_PEER = 5

    	 # selected

    .. data:: NTP_CTL_PST_SEL_SYS_PEER = 6

    	 * sys peer

    .. data:: NTP_CTL_PST_SEL_PPS = 7

    	 o pps peer

    """

    NTP_CTL_PST_SEL_REJECT = 0

    NTP_CTL_PST_SEL_SANE = 1

    NTP_CTL_PST_SEL_CORRECT = 2

    NTP_CTL_PST_SEL_SELCAND = 3

    NTP_CTL_PST_SEL_SYNC_CAND = 4

    NTP_CTL_PST_SEL_DISTSYS_PEER = 5

    NTP_CTL_PST_SEL_SYS_PEER = 6

    NTP_CTL_PST_SEL_PPS = 7


    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
        return meta._meta_table['NtpPeerStatusEnum']



class Ntp(object):
    """
    NTP operational data
    
    .. attribute:: nodes
    
    	Node\-specific NTP operational data
    	**type**\: :py:class:`Nodes <ydk.models.ip.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes>`
    
    

    """

    _prefix = 'ip-ntp-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = Ntp.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        Node\-specific NTP operational data
        
        .. attribute:: node
        
        	NTP operational data for a particular node
        	**type**\: list of :py:class:`Node <ydk.models.ip.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node>`
        
        

        """

        _prefix = 'ip-ntp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            NTP operational data for a particular node
            
            .. attribute:: node
            
            	The node identifier
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: associations
            
            	NTP Associations information
            	**type**\: :py:class:`Associations <ydk.models.ip.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.Associations>`
            
            .. attribute:: associations_detail
            
            	NTP Associations Detail information
            	**type**\: :py:class:`AssociationsDetail <ydk.models.ip.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail>`
            
            .. attribute:: status
            
            	Status of NTP peer(s)
            	**type**\: :py:class:`Status <ydk.models.ip.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.Status>`
            
            

            """

            _prefix = 'ip-ntp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node = None
                self.associations = Ntp.Nodes.Node.Associations()
                self.associations.parent = self
                self.associations_detail = Ntp.Nodes.Node.AssociationsDetail()
                self.associations_detail.parent = self
                self.status = Ntp.Nodes.Node.Status()
                self.status.parent = self


            class Associations(object):
                """
                NTP Associations information
                
                .. attribute:: is_ntp_enabled
                
                	Is NTP enabled
                	**type**\: bool
                
                .. attribute:: peer_summary_info
                
                	Peer info
                	**type**\: list of :py:class:`PeerSummaryInfo <ydk.models.ip.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.Associations.PeerSummaryInfo>`
                
                .. attribute:: sys_leap
                
                	Leap
                	**type**\: :py:class:`NtpLeapEnum <ydk.models.ip.Cisco_IOS_XR_ip_ntp_oper.NtpLeapEnum>`
                
                

                """

                _prefix = 'ip-ntp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.is_ntp_enabled = None
                    self.peer_summary_info = YList()
                    self.peer_summary_info.parent = self
                    self.peer_summary_info.name = 'peer_summary_info'
                    self.sys_leap = None


                class PeerSummaryInfo(object):
                    """
                    Peer info
                    
                    .. attribute:: peer_info_common
                    
                    	Common peer info
                    	**type**\: :py:class:`PeerInfoCommon <ydk.models.ip.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.Associations.PeerSummaryInfo.PeerInfoCommon>`
                    
                    .. attribute:: time_since
                    
                    	Time since last frame received (\-1=none)
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'ip-ntp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.peer_info_common = Ntp.Nodes.Node.Associations.PeerSummaryInfo.PeerInfoCommon()
                        self.peer_info_common.parent = self
                        self.time_since = None


                    class PeerInfoCommon(object):
                        """
                        Common peer info
                        
                        .. attribute:: address
                        
                        	Peer Address
                        	**type**\: str
                        
                        .. attribute:: delay
                        
                        	Peer delay
                        	**type**\: str
                        
                        .. attribute:: dispersion
                        
                        	Peer dispersion
                        	**type**\: str
                        
                        .. attribute:: host_mode
                        
                        	Association mode with this peer
                        	**type**\: :py:class:`NtpModeEnum <ydk.models.ip.Cisco_IOS_XR_ip_ntp_oper.NtpModeEnum>`
                        
                        .. attribute:: host_poll
                        
                        	Host poll
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: is_configured
                        
                        	Is configured
                        	**type**\: bool
                        
                        .. attribute:: is_sys_peer
                        
                        	Indicates whether this is syspeer
                        	**type**\: bool
                        
                        .. attribute:: offset
                        
                        	Peer offset
                        	**type**\: str
                        
                        .. attribute:: reachability
                        
                        	Reachability
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: reference_id
                        
                        	Peer reference ID
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: status
                        
                        	Peer status
                        	**type**\: :py:class:`NtpPeerStatusEnum <ydk.models.ip.Cisco_IOS_XR_ip_ntp_oper.NtpPeerStatusEnum>`
                        
                        .. attribute:: stratum
                        
                        	Peer stratum
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'ip-ntp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.address = None
                            self.delay = None
                            self.dispersion = None
                            self.host_mode = None
                            self.host_poll = None
                            self.is_configured = None
                            self.is_sys_peer = None
                            self.offset = None
                            self.reachability = None
                            self.reference_id = None
                            self.status = None
                            self.stratum = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-ntp-oper:peer-info-common'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.address is not None:
                                return True

                            if self.delay is not None:
                                return True

                            if self.dispersion is not None:
                                return True

                            if self.host_mode is not None:
                                return True

                            if self.host_poll is not None:
                                return True

                            if self.is_configured is not None:
                                return True

                            if self.is_sys_peer is not None:
                                return True

                            if self.offset is not None:
                                return True

                            if self.reachability is not None:
                                return True

                            if self.reference_id is not None:
                                return True

                            if self.status is not None:
                                return True

                            if self.stratum is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                            return meta._meta_table['Ntp.Nodes.Node.Associations.PeerSummaryInfo.PeerInfoCommon']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-ntp-oper:peer-summary-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.peer_info_common is not None and self.peer_info_common._has_data():
                            return True

                        if self.time_since is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                        return meta._meta_table['Ntp.Nodes.Node.Associations.PeerSummaryInfo']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-ntp-oper:associations'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_ntp_enabled is not None:
                        return True

                    if self.peer_summary_info is not None:
                        for child_ref in self.peer_summary_info:
                            if child_ref._has_data():
                                return True

                    if self.sys_leap is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ip._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                    return meta._meta_table['Ntp.Nodes.Node.Associations']['meta_info']


            class AssociationsDetail(object):
                """
                NTP Associations Detail information
                
                .. attribute:: is_ntp_enabled
                
                	Is NTP enabled
                	**type**\: bool
                
                .. attribute:: peer_detail_info
                
                	Peer info
                	**type**\: list of :py:class:`PeerDetailInfo <ydk.models.ip.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo>`
                
                .. attribute:: sys_leap
                
                	Leap
                	**type**\: :py:class:`NtpLeapEnum <ydk.models.ip.Cisco_IOS_XR_ip_ntp_oper.NtpLeapEnum>`
                
                

                """

                _prefix = 'ip-ntp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.is_ntp_enabled = None
                    self.peer_detail_info = YList()
                    self.peer_detail_info.parent = self
                    self.peer_detail_info.name = 'peer_detail_info'
                    self.sys_leap = None


                class PeerDetailInfo(object):
                    """
                    Peer info
                    
                    .. attribute:: filter_detail
                    
                    	Filter Details
                    	**type**\: list of :py:class:`FilterDetail <ydk.models.ip.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.FilterDetail>`
                    
                    .. attribute:: filter_index
                    
                    	Index into filter shift register
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: is_authenticated
                    
                    	Is authenticated
                    	**type**\: bool
                    
                    .. attribute:: is_ref_clock
                    
                    	Is refclock
                    	**type**\: bool
                    
                    .. attribute:: leap
                    
                    	Leap
                    	**type**\: :py:class:`NtpLeapEnum <ydk.models.ip.Cisco_IOS_XR_ip_ntp_oper.NtpLeapEnum>`
                    
                    .. attribute:: originate_time
                    
                    	Originate timestamp
                    	**type**\: :py:class:`OriginateTime <ydk.models.ip.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime>`
                    
                    .. attribute:: peer_info_common
                    
                    	Common peer info
                    	**type**\: :py:class:`PeerInfoCommon <ydk.models.ip.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.PeerInfoCommon>`
                    
                    .. attribute:: peer_mode
                    
                    	Peer's association mode
                    	**type**\: :py:class:`NtpModeEnum <ydk.models.ip.Cisco_IOS_XR_ip_ntp_oper.NtpModeEnum>`
                    
                    .. attribute:: poll_interval
                    
                    	Peer poll interval
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: precision
                    
                    	Precision
                    	**type**\: int
                    
                    	**range:** \-128..127
                    
                    .. attribute:: receive_time
                    
                    	Receive timestamp
                    	**type**\: :py:class:`ReceiveTime <ydk.models.ip.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime>`
                    
                    .. attribute:: ref_time
                    
                    	Reference time
                    	**type**\: :py:class:`RefTime <ydk.models.ip.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime>`
                    
                    .. attribute:: root_delay
                    
                    	Root delay
                    	**type**\: str
                    
                    .. attribute:: root_dispersion
                    
                    	Root dispersion
                    	**type**\: str
                    
                    .. attribute:: synch_distance
                    
                    	Synch distance
                    	**type**\: str
                    
                    .. attribute:: transmit_time
                    
                    	Transmit timestamp
                    	**type**\: :py:class:`TransmitTime <ydk.models.ip.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime>`
                    
                    .. attribute:: version
                    
                    	NTP version
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'ip-ntp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.filter_detail = YList()
                        self.filter_detail.parent = self
                        self.filter_detail.name = 'filter_detail'
                        self.filter_index = None
                        self.is_authenticated = None
                        self.is_ref_clock = None
                        self.leap = None
                        self.originate_time = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime()
                        self.originate_time.parent = self
                        self.peer_info_common = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.PeerInfoCommon()
                        self.peer_info_common.parent = self
                        self.peer_mode = None
                        self.poll_interval = None
                        self.precision = None
                        self.receive_time = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime()
                        self.receive_time.parent = self
                        self.ref_time = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime()
                        self.ref_time.parent = self
                        self.root_delay = None
                        self.root_dispersion = None
                        self.synch_distance = None
                        self.transmit_time = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime()
                        self.transmit_time.parent = self
                        self.version = None


                    class FilterDetail(object):
                        """
                        Filter Details
                        
                        .. attribute:: filter_delay
                        
                        	filter delay
                        	**type**\: str
                        
                        .. attribute:: filter_disp
                        
                        	filter disp
                        	**type**\: str
                        
                        .. attribute:: filter_offset
                        
                        	filter offset
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'ip-ntp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.filter_delay = None
                            self.filter_disp = None
                            self.filter_offset = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-ntp-oper:filter-detail'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.filter_delay is not None:
                                return True

                            if self.filter_disp is not None:
                                return True

                            if self.filter_offset is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                            return meta._meta_table['Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.FilterDetail']['meta_info']


                    class OriginateTime(object):
                        """
                        Originate timestamp
                        
                        .. attribute:: frac_secs
                        
                        	Fractional part in 64\-bit NTP timestamp
                        	**type**\: :py:class:`FracSecs <ydk.models.ip.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime.FracSecs>`
                        
                        .. attribute:: sec
                        
                        	Second part in 64\-bit NTP timestamp
                        	**type**\: :py:class:`Sec <ydk.models.ip.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime.Sec>`
                        
                        

                        """

                        _prefix = 'ip-ntp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.frac_secs = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime.FracSecs()
                            self.frac_secs.parent = self
                            self.sec = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime.Sec()
                            self.sec.parent = self


                        class FracSecs(object):
                            """
                            Fractional part in 64\-bit NTP timestamp
                            
                            .. attribute:: frac
                            
                            	Fractional format in NTP reference code
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-ntp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.frac = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-ntp-oper:frac-secs'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.frac is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                                return meta._meta_table['Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime.FracSecs']['meta_info']


                        class Sec(object):
                            """
                            Second part in 64\-bit NTP timestamp
                            
                            .. attribute:: int
                            
                            	Integer format in NTP reference code
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-ntp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.int = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-ntp-oper:sec'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.int is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                                return meta._meta_table['Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime.Sec']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-ntp-oper:originate-time'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.frac_secs is not None and self.frac_secs._has_data():
                                return True

                            if self.sec is not None and self.sec._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                            return meta._meta_table['Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime']['meta_info']


                    class PeerInfoCommon(object):
                        """
                        Common peer info
                        
                        .. attribute:: address
                        
                        	Peer Address
                        	**type**\: str
                        
                        .. attribute:: delay
                        
                        	Peer delay
                        	**type**\: str
                        
                        .. attribute:: dispersion
                        
                        	Peer dispersion
                        	**type**\: str
                        
                        .. attribute:: host_mode
                        
                        	Association mode with this peer
                        	**type**\: :py:class:`NtpModeEnum <ydk.models.ip.Cisco_IOS_XR_ip_ntp_oper.NtpModeEnum>`
                        
                        .. attribute:: host_poll
                        
                        	Host poll
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: is_configured
                        
                        	Is configured
                        	**type**\: bool
                        
                        .. attribute:: is_sys_peer
                        
                        	Indicates whether this is syspeer
                        	**type**\: bool
                        
                        .. attribute:: offset
                        
                        	Peer offset
                        	**type**\: str
                        
                        .. attribute:: reachability
                        
                        	Reachability
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: reference_id
                        
                        	Peer reference ID
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: status
                        
                        	Peer status
                        	**type**\: :py:class:`NtpPeerStatusEnum <ydk.models.ip.Cisco_IOS_XR_ip_ntp_oper.NtpPeerStatusEnum>`
                        
                        .. attribute:: stratum
                        
                        	Peer stratum
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'ip-ntp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.address = None
                            self.delay = None
                            self.dispersion = None
                            self.host_mode = None
                            self.host_poll = None
                            self.is_configured = None
                            self.is_sys_peer = None
                            self.offset = None
                            self.reachability = None
                            self.reference_id = None
                            self.status = None
                            self.stratum = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-ntp-oper:peer-info-common'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.address is not None:
                                return True

                            if self.delay is not None:
                                return True

                            if self.dispersion is not None:
                                return True

                            if self.host_mode is not None:
                                return True

                            if self.host_poll is not None:
                                return True

                            if self.is_configured is not None:
                                return True

                            if self.is_sys_peer is not None:
                                return True

                            if self.offset is not None:
                                return True

                            if self.reachability is not None:
                                return True

                            if self.reference_id is not None:
                                return True

                            if self.status is not None:
                                return True

                            if self.stratum is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                            return meta._meta_table['Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.PeerInfoCommon']['meta_info']


                    class ReceiveTime(object):
                        """
                        Receive timestamp
                        
                        .. attribute:: frac_secs
                        
                        	Fractional part in 64\-bit NTP timestamp
                        	**type**\: :py:class:`FracSecs <ydk.models.ip.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime.FracSecs>`
                        
                        .. attribute:: sec
                        
                        	Second part in 64\-bit NTP timestamp
                        	**type**\: :py:class:`Sec <ydk.models.ip.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime.Sec>`
                        
                        

                        """

                        _prefix = 'ip-ntp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.frac_secs = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime.FracSecs()
                            self.frac_secs.parent = self
                            self.sec = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime.Sec()
                            self.sec.parent = self


                        class FracSecs(object):
                            """
                            Fractional part in 64\-bit NTP timestamp
                            
                            .. attribute:: frac
                            
                            	Fractional format in NTP reference code
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-ntp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.frac = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-ntp-oper:frac-secs'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.frac is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                                return meta._meta_table['Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime.FracSecs']['meta_info']


                        class Sec(object):
                            """
                            Second part in 64\-bit NTP timestamp
                            
                            .. attribute:: int
                            
                            	Integer format in NTP reference code
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-ntp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.int = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-ntp-oper:sec'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.int is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                                return meta._meta_table['Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime.Sec']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-ntp-oper:receive-time'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.frac_secs is not None and self.frac_secs._has_data():
                                return True

                            if self.sec is not None and self.sec._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                            return meta._meta_table['Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime']['meta_info']


                    class RefTime(object):
                        """
                        Reference time
                        
                        .. attribute:: frac_secs
                        
                        	Fractional part in 64\-bit NTP timestamp
                        	**type**\: :py:class:`FracSecs <ydk.models.ip.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime.FracSecs>`
                        
                        .. attribute:: sec
                        
                        	Second part in 64\-bit NTP timestamp
                        	**type**\: :py:class:`Sec <ydk.models.ip.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime.Sec>`
                        
                        

                        """

                        _prefix = 'ip-ntp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.frac_secs = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime.FracSecs()
                            self.frac_secs.parent = self
                            self.sec = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime.Sec()
                            self.sec.parent = self


                        class FracSecs(object):
                            """
                            Fractional part in 64\-bit NTP timestamp
                            
                            .. attribute:: frac
                            
                            	Fractional format in NTP reference code
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-ntp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.frac = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-ntp-oper:frac-secs'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.frac is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                                return meta._meta_table['Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime.FracSecs']['meta_info']


                        class Sec(object):
                            """
                            Second part in 64\-bit NTP timestamp
                            
                            .. attribute:: int
                            
                            	Integer format in NTP reference code
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-ntp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.int = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-ntp-oper:sec'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.int is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                                return meta._meta_table['Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime.Sec']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-ntp-oper:ref-time'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.frac_secs is not None and self.frac_secs._has_data():
                                return True

                            if self.sec is not None and self.sec._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                            return meta._meta_table['Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime']['meta_info']


                    class TransmitTime(object):
                        """
                        Transmit timestamp
                        
                        .. attribute:: frac_secs
                        
                        	Fractional part in 64\-bit NTP timestamp
                        	**type**\: :py:class:`FracSecs <ydk.models.ip.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime.FracSecs>`
                        
                        .. attribute:: sec
                        
                        	Second part in 64\-bit NTP timestamp
                        	**type**\: :py:class:`Sec <ydk.models.ip.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime.Sec>`
                        
                        

                        """

                        _prefix = 'ip-ntp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.frac_secs = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime.FracSecs()
                            self.frac_secs.parent = self
                            self.sec = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime.Sec()
                            self.sec.parent = self


                        class FracSecs(object):
                            """
                            Fractional part in 64\-bit NTP timestamp
                            
                            .. attribute:: frac
                            
                            	Fractional format in NTP reference code
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-ntp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.frac = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-ntp-oper:frac-secs'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.frac is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                                return meta._meta_table['Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime.FracSecs']['meta_info']


                        class Sec(object):
                            """
                            Second part in 64\-bit NTP timestamp
                            
                            .. attribute:: int
                            
                            	Integer format in NTP reference code
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-ntp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.int = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-ntp-oper:sec'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.int is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                                return meta._meta_table['Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime.Sec']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-ntp-oper:transmit-time'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.frac_secs is not None and self.frac_secs._has_data():
                                return True

                            if self.sec is not None and self.sec._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                            return meta._meta_table['Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-ntp-oper:peer-detail-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.filter_detail is not None:
                            for child_ref in self.filter_detail:
                                if child_ref._has_data():
                                    return True

                        if self.filter_index is not None:
                            return True

                        if self.is_authenticated is not None:
                            return True

                        if self.is_ref_clock is not None:
                            return True

                        if self.leap is not None:
                            return True

                        if self.originate_time is not None and self.originate_time._has_data():
                            return True

                        if self.peer_info_common is not None and self.peer_info_common._has_data():
                            return True

                        if self.peer_mode is not None:
                            return True

                        if self.poll_interval is not None:
                            return True

                        if self.precision is not None:
                            return True

                        if self.receive_time is not None and self.receive_time._has_data():
                            return True

                        if self.ref_time is not None and self.ref_time._has_data():
                            return True

                        if self.root_delay is not None:
                            return True

                        if self.root_dispersion is not None:
                            return True

                        if self.synch_distance is not None:
                            return True

                        if self.transmit_time is not None and self.transmit_time._has_data():
                            return True

                        if self.version is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                        return meta._meta_table['Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-ntp-oper:associations-detail'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_ntp_enabled is not None:
                        return True

                    if self.peer_detail_info is not None:
                        for child_ref in self.peer_detail_info:
                            if child_ref._has_data():
                                return True

                    if self.sys_leap is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ip._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                    return meta._meta_table['Ntp.Nodes.Node.AssociationsDetail']['meta_info']


            class Status(object):
                """
                Status of NTP peer(s)
                
                .. attribute:: clock_period
                
                	Clock period in nanosecs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_ntp_enabled
                
                	Is NTP enabled
                	**type**\: bool
                
                .. attribute:: is_updated
                
                	Is clock updated
                	**type**\: :py:class:`ClockUpdateNodeEnum <ydk.models.ip.Cisco_IOS_XR_ip_ntp_oper.ClockUpdateNodeEnum>`
                
                .. attribute:: last_update
                
                	Last Update
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: loop_filter_state
                
                	Loop Filter State
                	**type**\: :py:class:`NtpLoopFilterStateEnum <ydk.models.ip.Cisco_IOS_XR_ip_ntp_oper.NtpLoopFilterStateEnum>`
                
                .. attribute:: poll_interval
                
                	Peer poll interval
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: sys_dispersion
                
                	Peer dispersion
                	**type**\: str
                
                .. attribute:: sys_drift
                
                	System Drift
                	**type**\: :py:class:`SysDrift <ydk.models.ip.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.Status.SysDrift>`
                
                .. attribute:: sys_leap
                
                	leap
                	**type**\: :py:class:`NtpLeapEnum <ydk.models.ip.Cisco_IOS_XR_ip_ntp_oper.NtpLeapEnum>`
                
                .. attribute:: sys_offset
                
                	Clock offset
                	**type**\: str
                
                .. attribute:: sys_precision
                
                	Precision
                	**type**\: int
                
                	**range:** \-128..127
                
                .. attribute:: sys_ref_id
                
                	Reference clock ID
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: sys_ref_time
                
                	Reference time
                	**type**\: :py:class:`SysRefTime <ydk.models.ip.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.Status.SysRefTime>`
                
                .. attribute:: sys_root_delay
                
                	Root delay
                	**type**\: str
                
                .. attribute:: sys_root_dispersion
                
                	Root dispersion
                	**type**\: str
                
                .. attribute:: sys_stratum
                
                	Stratum
                	**type**\: int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'ip-ntp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.clock_period = None
                    self.is_ntp_enabled = None
                    self.is_updated = None
                    self.last_update = None
                    self.loop_filter_state = None
                    self.poll_interval = None
                    self.sys_dispersion = None
                    self.sys_drift = Ntp.Nodes.Node.Status.SysDrift()
                    self.sys_drift.parent = self
                    self.sys_leap = None
                    self.sys_offset = None
                    self.sys_precision = None
                    self.sys_ref_id = None
                    self.sys_ref_time = Ntp.Nodes.Node.Status.SysRefTime()
                    self.sys_ref_time.parent = self
                    self.sys_root_delay = None
                    self.sys_root_dispersion = None
                    self.sys_stratum = None


                class SysDrift(object):
                    """
                    System Drift
                    
                    .. attribute:: frac_secs
                    
                    	Fractional part in 64\-bit NTP timestamp
                    	**type**\: :py:class:`FracSecs <ydk.models.ip.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.Status.SysDrift.FracSecs>`
                    
                    .. attribute:: sec
                    
                    	Second part in 64\-bit NTP timestamp
                    	**type**\: :py:class:`Sec <ydk.models.ip.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.Status.SysDrift.Sec>`
                    
                    

                    """

                    _prefix = 'ip-ntp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.frac_secs = Ntp.Nodes.Node.Status.SysDrift.FracSecs()
                        self.frac_secs.parent = self
                        self.sec = Ntp.Nodes.Node.Status.SysDrift.Sec()
                        self.sec.parent = self


                    class FracSecs(object):
                        """
                        Fractional part in 64\-bit NTP timestamp
                        
                        .. attribute:: frac
                        
                        	Fractional format in NTP reference code
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-ntp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.frac = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-ntp-oper:frac-secs'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.frac is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                            return meta._meta_table['Ntp.Nodes.Node.Status.SysDrift.FracSecs']['meta_info']


                    class Sec(object):
                        """
                        Second part in 64\-bit NTP timestamp
                        
                        .. attribute:: int
                        
                        	Integer format in NTP reference code
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-ntp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.int = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-ntp-oper:sec'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.int is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                            return meta._meta_table['Ntp.Nodes.Node.Status.SysDrift.Sec']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-ntp-oper:sys-drift'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.frac_secs is not None and self.frac_secs._has_data():
                            return True

                        if self.sec is not None and self.sec._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                        return meta._meta_table['Ntp.Nodes.Node.Status.SysDrift']['meta_info']


                class SysRefTime(object):
                    """
                    Reference time
                    
                    .. attribute:: frac_secs
                    
                    	Fractional part in 64\-bit NTP timestamp
                    	**type**\: :py:class:`FracSecs <ydk.models.ip.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.Status.SysRefTime.FracSecs>`
                    
                    .. attribute:: sec
                    
                    	Second part in 64\-bit NTP timestamp
                    	**type**\: :py:class:`Sec <ydk.models.ip.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.Status.SysRefTime.Sec>`
                    
                    

                    """

                    _prefix = 'ip-ntp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.frac_secs = Ntp.Nodes.Node.Status.SysRefTime.FracSecs()
                        self.frac_secs.parent = self
                        self.sec = Ntp.Nodes.Node.Status.SysRefTime.Sec()
                        self.sec.parent = self


                    class FracSecs(object):
                        """
                        Fractional part in 64\-bit NTP timestamp
                        
                        .. attribute:: frac
                        
                        	Fractional format in NTP reference code
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-ntp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.frac = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-ntp-oper:frac-secs'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.frac is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                            return meta._meta_table['Ntp.Nodes.Node.Status.SysRefTime.FracSecs']['meta_info']


                    class Sec(object):
                        """
                        Second part in 64\-bit NTP timestamp
                        
                        .. attribute:: int
                        
                        	Integer format in NTP reference code
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-ntp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.int = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-ntp-oper:sec'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.int is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                            return meta._meta_table['Ntp.Nodes.Node.Status.SysRefTime.Sec']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-ntp-oper:sys-ref-time'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.frac_secs is not None and self.frac_secs._has_data():
                            return True

                        if self.sec is not None and self.sec._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                        return meta._meta_table['Ntp.Nodes.Node.Status.SysRefTime']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-ntp-oper:status'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.clock_period is not None:
                        return True

                    if self.is_ntp_enabled is not None:
                        return True

                    if self.is_updated is not None:
                        return True

                    if self.last_update is not None:
                        return True

                    if self.loop_filter_state is not None:
                        return True

                    if self.poll_interval is not None:
                        return True

                    if self.sys_dispersion is not None:
                        return True

                    if self.sys_drift is not None and self.sys_drift._has_data():
                        return True

                    if self.sys_leap is not None:
                        return True

                    if self.sys_offset is not None:
                        return True

                    if self.sys_precision is not None:
                        return True

                    if self.sys_ref_id is not None:
                        return True

                    if self.sys_ref_time is not None and self.sys_ref_time._has_data():
                        return True

                    if self.sys_root_delay is not None:
                        return True

                    if self.sys_root_dispersion is not None:
                        return True

                    if self.sys_stratum is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ip._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                    return meta._meta_table['Ntp.Nodes.Node.Status']['meta_info']

            @property
            def _common_path(self):
                if self.node is None:
                    raise YPYDataValidationError('Key property node is None')

                return '/Cisco-IOS-XR-ip-ntp-oper:ntp/Cisco-IOS-XR-ip-ntp-oper:nodes/Cisco-IOS-XR-ip-ntp-oper:node[Cisco-IOS-XR-ip-ntp-oper:node = ' + str(self.node) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.node is not None:
                    return True

                if self.associations is not None and self.associations._has_data():
                    return True

                if self.associations_detail is not None and self.associations_detail._has_data():
                    return True

                if self.status is not None and self.status._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                return meta._meta_table['Ntp.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-ntp-oper:ntp/Cisco-IOS-XR-ip-ntp-oper:nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.node is not None:
                for child_ref in self.node:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
            return meta._meta_table['Ntp.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ip-ntp-oper:ntp'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
        return meta._meta_table['Ntp']['meta_info']



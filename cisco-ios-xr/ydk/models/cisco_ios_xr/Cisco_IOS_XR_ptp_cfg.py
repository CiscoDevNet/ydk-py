""" Cisco_IOS_XR_ptp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ptp package configuration.

This module contains definitions
for the following management objects\:
  ptp\: PTP global configuration

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Ptp(Entity):
    """
    PTP global configuration
    
    .. attribute:: clock
    
    	PTP local clock configuration
    	**type**\:  :py:class:`Clock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Clock>`
    
    .. attribute:: profiles
    
    	Table for profile configuration
    	**type**\:  :py:class:`Profiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Profiles>`
    
    .. attribute:: utc_offset
    
    	UTC offset configuration
    	**type**\:  :py:class:`UtcOffset <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.UtcOffset>`
    
    .. attribute:: logging
    
    	PTP logging configuration
    	**type**\:  :py:class:`Logging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Logging>`
    
    .. attribute:: uncalibrated_clock_class
    
    	Clock class to be used while acquiring phase\-lock to a parent clock. Note that this is deprecated and should not be  used
    	**type**\: int
    
    	**range:** 0..255
    
    .. attribute:: uncalibrated_clock_class2
    
    	Clock class to be used while acquiring phase\-lock to a parent clock
    	**type**\:  :py:class:`UncalibratedClockClass2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.UncalibratedClockClass2>`
    
    	**presence node**\: True
    
    .. attribute:: transparent_clock
    
    	Transparent clock configuration
    	**type**\:  :py:class:`TransparentClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.TransparentClock>`
    
    .. attribute:: virtual_port
    
    	PTP virtual port configuration
    	**type**\:  :py:class:`VirtualPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.VirtualPort>`
    
    .. attribute:: time_of_day_priority
    
    	Time\-of\-day priority
    	**type**\: int
    
    	**range:** 1..254
    
    	**default value**\: 100
    
    .. attribute:: frequency_priority
    
    	Frequency priority
    	**type**\: int
    
    	**range:** 1..254
    
    	**default value**\: 254
    
    .. attribute:: startup_clock_class
    
    	Startup clock class value
    	**type**\: int
    
    	**range:** 0..255
    
    .. attribute:: enable
    
    	Enable the precision time protocol
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: min_clock_class
    
    	Clocks with a clock\-class higher than the minimum clock class will not be considered for selection as a parent clock
    	**type**\: int
    
    	**range:** 0..255
    
    .. attribute:: physical_layer_frequency
    
    	Disable PTP as a source for frequency as only physical layer frequency sources are used
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: freerun_clock_class
    
    	Freerun clock class value
    	**type**\: int
    
    	**range:** 0..255
    
    

    """

    _prefix = 'ptp-cfg'
    _revision = '2017-02-02'

    def __init__(self):
        super(Ptp, self).__init__()
        self._top_entity = None

        self.yang_name = "ptp"
        self.yang_parent_name = "Cisco-IOS-XR-ptp-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("clock", ("clock", Ptp.Clock)), ("profiles", ("profiles", Ptp.Profiles)), ("utc-offset", ("utc_offset", Ptp.UtcOffset)), ("logging", ("logging", Ptp.Logging)), ("uncalibrated-clock-class2", ("uncalibrated_clock_class2", Ptp.UncalibratedClockClass2)), ("transparent-clock", ("transparent_clock", Ptp.TransparentClock)), ("virtual-port", ("virtual_port", Ptp.VirtualPort))])
        self._leafs = OrderedDict([
            ('uncalibrated_clock_class', (YLeaf(YType.uint32, 'uncalibrated-clock-class'), ['int'])),
            ('time_of_day_priority', (YLeaf(YType.uint32, 'time-of-day-priority'), ['int'])),
            ('frequency_priority', (YLeaf(YType.uint32, 'frequency-priority'), ['int'])),
            ('startup_clock_class', (YLeaf(YType.uint32, 'startup-clock-class'), ['int'])),
            ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
            ('min_clock_class', (YLeaf(YType.uint32, 'min-clock-class'), ['int'])),
            ('physical_layer_frequency', (YLeaf(YType.empty, 'physical-layer-frequency'), ['Empty'])),
            ('freerun_clock_class', (YLeaf(YType.uint32, 'freerun-clock-class'), ['int'])),
        ])
        self.uncalibrated_clock_class = None
        self.time_of_day_priority = None
        self.frequency_priority = None
        self.startup_clock_class = None
        self.enable = None
        self.min_clock_class = None
        self.physical_layer_frequency = None
        self.freerun_clock_class = None

        self.clock = Ptp.Clock()
        self.clock.parent = self
        self._children_name_map["clock"] = "clock"

        self.profiles = Ptp.Profiles()
        self.profiles.parent = self
        self._children_name_map["profiles"] = "profiles"

        self.utc_offset = Ptp.UtcOffset()
        self.utc_offset.parent = self
        self._children_name_map["utc_offset"] = "utc-offset"

        self.logging = Ptp.Logging()
        self.logging.parent = self
        self._children_name_map["logging"] = "logging"

        self.uncalibrated_clock_class2 = None
        self._children_name_map["uncalibrated_clock_class2"] = "uncalibrated-clock-class2"

        self.transparent_clock = Ptp.TransparentClock()
        self.transparent_clock.parent = self
        self._children_name_map["transparent_clock"] = "transparent-clock"

        self.virtual_port = Ptp.VirtualPort()
        self.virtual_port.parent = self
        self._children_name_map["virtual_port"] = "virtual-port"
        self._segment_path = lambda: "Cisco-IOS-XR-ptp-cfg:ptp"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Ptp, ['uncalibrated_clock_class', 'time_of_day_priority', 'frequency_priority', 'startup_clock_class', 'enable', 'min_clock_class', 'physical_layer_frequency', 'freerun_clock_class'], name, value)


    class Clock(Entity):
        """
        PTP local clock configuration
        
        .. attribute:: profile
        
        	Local clock PTP profile
        	**type**\:  :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Clock.Profile>`
        
        .. attribute:: identity
        
        	Local clock identity
        	**type**\:  :py:class:`Identity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Clock.Identity>`
        
        .. attribute:: timescale
        
        	Local clock timescale
        	**type**\:  :py:class:`PtpTimescale <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpTimescale>`
        
        .. attribute:: domain
        
        	Local clock domain
        	**type**\: int
        
        	**range:** 0..255
        
        	**default value**\: 0
        
        .. attribute:: priority2
        
        	Local clock priority2
        	**type**\: int
        
        	**range:** 0..255
        
        	**default value**\: 128
        
        .. attribute:: time_source
        
        	Local clock time source
        	**type**\:  :py:class:`PtpTimeSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpTimeSource>`
        
        .. attribute:: priority1
        
        	Local clock priority1
        	**type**\: int
        
        	**range:** 0..255
        
        	**default value**\: 128
        
        .. attribute:: clock_class
        
        	Local clock class
        	**type**\: int
        
        	**range:** 0..255
        
        	**default value**\: 0
        
        

        """

        _prefix = 'ptp-cfg'
        _revision = '2017-02-02'

        def __init__(self):
            super(Ptp.Clock, self).__init__()

            self.yang_name = "clock"
            self.yang_parent_name = "ptp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("profile", ("profile", Ptp.Clock.Profile)), ("identity", ("identity", Ptp.Clock.Identity))])
            self._leafs = OrderedDict([
                ('timescale', (YLeaf(YType.enumeration, 'timescale'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes', 'PtpTimescale', '')])),
                ('domain', (YLeaf(YType.uint32, 'domain'), ['int'])),
                ('priority2', (YLeaf(YType.uint32, 'priority2'), ['int'])),
                ('time_source', (YLeaf(YType.enumeration, 'time-source'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes', 'PtpTimeSource', '')])),
                ('priority1', (YLeaf(YType.uint32, 'priority1'), ['int'])),
                ('clock_class', (YLeaf(YType.uint32, 'clock-class'), ['int'])),
            ])
            self.timescale = None
            self.domain = None
            self.priority2 = None
            self.time_source = None
            self.priority1 = None
            self.clock_class = None

            self.profile = Ptp.Clock.Profile()
            self.profile.parent = self
            self._children_name_map["profile"] = "profile"

            self.identity = Ptp.Clock.Identity()
            self.identity.parent = self
            self._children_name_map["identity"] = "identity"
            self._segment_path = lambda: "clock"
            self._absolute_path = lambda: "Cisco-IOS-XR-ptp-cfg:ptp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ptp.Clock, ['timescale', 'domain', 'priority2', 'time_source', 'priority1', 'clock_class'], name, value)


        class Profile(Entity):
            """
            Local clock PTP profile
            
            .. attribute:: clock_profile
            
            	Clock profile
            	**type**\:  :py:class:`PtpClockProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpClockProfile>`
            
            	**default value**\: default
            
            .. attribute:: telecom_clock_type
            
            	Telecom clock type
            	**type**\:  :py:class:`PtpTelecomClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpTelecomClock>`
            
            

            """

            _prefix = 'ptp-cfg'
            _revision = '2017-02-02'

            def __init__(self):
                super(Ptp.Clock.Profile, self).__init__()

                self.yang_name = "profile"
                self.yang_parent_name = "clock"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('clock_profile', (YLeaf(YType.enumeration, 'clock-profile'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes', 'PtpClockProfile', '')])),
                    ('telecom_clock_type', (YLeaf(YType.enumeration, 'telecom-clock-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes', 'PtpTelecomClock', '')])),
                ])
                self.clock_profile = None
                self.telecom_clock_type = None
                self._segment_path = lambda: "profile"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-cfg:ptp/clock/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.Clock.Profile, ['clock_profile', 'telecom_clock_type'], name, value)


        class Identity(Entity):
            """
            Local clock identity
            
            .. attribute:: clock_id_type
            
            	Clock identity type
            	**type**\:  :py:class:`PtpClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpClockId>`
            
            	**default value**\: router-mac
            
            .. attribute:: mac_address
            
            	MAC Address
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: eui
            
            	EUI\-64 number
            	**type**\: str
            
            

            """

            _prefix = 'ptp-cfg'
            _revision = '2017-02-02'

            def __init__(self):
                super(Ptp.Clock.Identity, self).__init__()

                self.yang_name = "identity"
                self.yang_parent_name = "clock"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('clock_id_type', (YLeaf(YType.enumeration, 'clock-id-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes', 'PtpClockId', '')])),
                    ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                    ('eui', (YLeaf(YType.str, 'eui'), ['str'])),
                ])
                self.clock_id_type = None
                self.mac_address = None
                self.eui = None
                self._segment_path = lambda: "identity"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-cfg:ptp/clock/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.Clock.Identity, ['clock_id_type', 'mac_address', 'eui'], name, value)


    class Profiles(Entity):
        """
        Table for profile configuration
        
        .. attribute:: profile
        
        	Profile configuration
        	**type**\: list of  		 :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Profiles.Profile>`
        
        

        """

        _prefix = 'ptp-cfg'
        _revision = '2017-02-02'

        def __init__(self):
            super(Ptp.Profiles, self).__init__()

            self.yang_name = "profiles"
            self.yang_parent_name = "ptp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("profile", ("profile", Ptp.Profiles.Profile))])
            self._leafs = OrderedDict()

            self.profile = YList(self)
            self._segment_path = lambda: "profiles"
            self._absolute_path = lambda: "Cisco-IOS-XR-ptp-cfg:ptp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ptp.Profiles, [], name, value)


        class Profile(Entity):
            """
            Profile configuration
            
            .. attribute:: profile_name  (key)
            
            	Profile
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: announce_interval
            
            	Announce interval
            	**type**\:  :py:class:`AnnounceInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Profiles.Profile.AnnounceInterval>`
            
            .. attribute:: interop
            
            	Table for interop configuration
            	**type**\:  :py:class:`Interop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Profiles.Profile.Interop>`
            
            .. attribute:: source_ipv4_address
            
            	Source IPv4 Address
            	**type**\:  :py:class:`SourceIpv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Profiles.Profile.SourceIpv4Address>`
            
            .. attribute:: slaves
            
            	Table for slave configuration
            	**type**\:  :py:class:`Slaves <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Profiles.Profile.Slaves>`
            
            .. attribute:: sync_interval
            
            	Sync interval
            	**type**\:  :py:class:`SyncInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Profiles.Profile.SyncInterval>`
            
            .. attribute:: masters
            
            	Table for master configuration
            	**type**\:  :py:class:`Masters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Profiles.Profile.Masters>`
            
            .. attribute:: communication
            
            	Communication model
            	**type**\:  :py:class:`Communication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Profiles.Profile.Communication>`
            
            .. attribute:: delay_request_minimum_interval
            
            	Minimum delay request interval
            	**type**\:  :py:class:`DelayRequestMinimumInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Profiles.Profile.DelayRequestMinimumInterval>`
            
            .. attribute:: source_ipv6_address
            
            	Source IPv6 Address
            	**type**\:  :py:class:`SourceIpv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Profiles.Profile.SourceIpv6Address>`
            
            .. attribute:: sync_grant_duration
            
            	Sync unicast grant duration, in seconds
            	**type**\: int
            
            	**range:** 60..1000
            
            	**units**\: second
            
            	**default value**\: 300
            
            .. attribute:: general_cos
            
            	General COS
            	**type**\: int
            
            	**range:** 0..7
            
            	**default value**\: 6
            
            .. attribute:: sync_timeout
            
            	Sync timeout, in milliseconds
            	**type**\: int
            
            	**range:** 100..100000
            
            	**units**\: millisecond
            
            	**default value**\: 5000
            
            .. attribute:: transport
            
            	Transport
            	**type**\:  :py:class:`PtpEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpEncap>`
            
            	**default value**\: ipv4
            
            .. attribute:: announce_timeout
            
            	Announce Timeout
            	**type**\: int
            
            	**range:** 2..10
            
            	**default value**\: 3
            
            .. attribute:: cos
            
            	COS
            	**type**\: int
            
            	**range:** 0..7
            
            	**default value**\: 6
            
            .. attribute:: ipv4ttl
            
            	IPv4 TTL
            	**type**\: int
            
            	**range:** 1..255
            
            	**default value**\: 255
            
            .. attribute:: port_state
            
            	Port state restriction
            	**type**\:  :py:class:`PtpPortState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpPortState>`
            
            	**default value**\: any
            
            .. attribute:: delay_response_timeout
            
            	Delay\-Response timeout, in milliseconds
            	**type**\: int
            
            	**range:** 100..100000
            
            	**units**\: millisecond
            
            	**default value**\: 5000
            
            .. attribute:: delay_response_grant_duration
            
            	Delay\-Response unicast grant duration, in seconds
            	**type**\: int
            
            	**range:** 60..1000
            
            	**units**\: second
            
            	**default value**\: 300
            
            .. attribute:: event_cos
            
            	Event COS
            	**type**\: int
            
            	**range:** 0..7
            
            	**default value**\: 6
            
            .. attribute:: dscp
            
            	DSCP
            	**type**\: int
            
            	**range:** 0..63
            
            	**default value**\: 46
            
            .. attribute:: ipv6_hop_limit
            
            	IPv6 Hop Limit
            	**type**\: int
            
            	**range:** 1..255
            
            	**default value**\: 255
            
            .. attribute:: general_dscp
            
            	General DSCP
            	**type**\: int
            
            	**range:** 0..63
            
            	**default value**\: 46
            
            .. attribute:: clock_operation
            
            	Clock Operation
            	**type**\:  :py:class:`PtpClockOperation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpClockOperation>`
            
            	**default value**\: two-step
            
            .. attribute:: announce_grant_duration
            
            	Announce unicast grant duration, in seconds
            	**type**\: int
            
            	**range:** 60..1000
            
            	**units**\: second
            
            	**default value**\: 300
            
            .. attribute:: unicast_grant_invalid_request
            
            	Invalid unicast grant request response
            	**type**\:  :py:class:`PtpInvalidUnicastGrantRequestResponse <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpInvalidUnicastGrantRequestResponse>`
            
            	**default value**\: reduce
            
            .. attribute:: event_dscp
            
            	Event DSCP
            	**type**\: int
            
            	**range:** 0..63
            
            	**default value**\: 46
            
            

            """

            _prefix = 'ptp-cfg'
            _revision = '2017-02-02'

            def __init__(self):
                super(Ptp.Profiles.Profile, self).__init__()

                self.yang_name = "profile"
                self.yang_parent_name = "profiles"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['profile_name']
                self._child_classes = OrderedDict([("announce-interval", ("announce_interval", Ptp.Profiles.Profile.AnnounceInterval)), ("interop", ("interop", Ptp.Profiles.Profile.Interop)), ("source-ipv4-address", ("source_ipv4_address", Ptp.Profiles.Profile.SourceIpv4Address)), ("slaves", ("slaves", Ptp.Profiles.Profile.Slaves)), ("sync-interval", ("sync_interval", Ptp.Profiles.Profile.SyncInterval)), ("masters", ("masters", Ptp.Profiles.Profile.Masters)), ("communication", ("communication", Ptp.Profiles.Profile.Communication)), ("delay-request-minimum-interval", ("delay_request_minimum_interval", Ptp.Profiles.Profile.DelayRequestMinimumInterval)), ("source-ipv6-address", ("source_ipv6_address", Ptp.Profiles.Profile.SourceIpv6Address))])
                self._leafs = OrderedDict([
                    ('profile_name', (YLeaf(YType.str, 'profile-name'), ['str'])),
                    ('sync_grant_duration', (YLeaf(YType.uint32, 'sync-grant-duration'), ['int'])),
                    ('general_cos', (YLeaf(YType.uint32, 'general-cos'), ['int'])),
                    ('sync_timeout', (YLeaf(YType.uint32, 'sync-timeout'), ['int'])),
                    ('transport', (YLeaf(YType.enumeration, 'transport'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes', 'PtpEncap', '')])),
                    ('announce_timeout', (YLeaf(YType.uint32, 'announce-timeout'), ['int'])),
                    ('cos', (YLeaf(YType.uint32, 'cos'), ['int'])),
                    ('ipv4ttl', (YLeaf(YType.uint32, 'ipv4ttl'), ['int'])),
                    ('port_state', (YLeaf(YType.enumeration, 'port-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes', 'PtpPortState', '')])),
                    ('delay_response_timeout', (YLeaf(YType.uint32, 'delay-response-timeout'), ['int'])),
                    ('delay_response_grant_duration', (YLeaf(YType.uint32, 'delay-response-grant-duration'), ['int'])),
                    ('event_cos', (YLeaf(YType.uint32, 'event-cos'), ['int'])),
                    ('dscp', (YLeaf(YType.uint32, 'dscp'), ['int'])),
                    ('ipv6_hop_limit', (YLeaf(YType.uint32, 'ipv6-hop-limit'), ['int'])),
                    ('general_dscp', (YLeaf(YType.uint32, 'general-dscp'), ['int'])),
                    ('clock_operation', (YLeaf(YType.enumeration, 'clock-operation'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes', 'PtpClockOperation', '')])),
                    ('announce_grant_duration', (YLeaf(YType.uint32, 'announce-grant-duration'), ['int'])),
                    ('unicast_grant_invalid_request', (YLeaf(YType.enumeration, 'unicast-grant-invalid-request'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes', 'PtpInvalidUnicastGrantRequestResponse', '')])),
                    ('event_dscp', (YLeaf(YType.uint32, 'event-dscp'), ['int'])),
                ])
                self.profile_name = None
                self.sync_grant_duration = None
                self.general_cos = None
                self.sync_timeout = None
                self.transport = None
                self.announce_timeout = None
                self.cos = None
                self.ipv4ttl = None
                self.port_state = None
                self.delay_response_timeout = None
                self.delay_response_grant_duration = None
                self.event_cos = None
                self.dscp = None
                self.ipv6_hop_limit = None
                self.general_dscp = None
                self.clock_operation = None
                self.announce_grant_duration = None
                self.unicast_grant_invalid_request = None
                self.event_dscp = None

                self.announce_interval = Ptp.Profiles.Profile.AnnounceInterval()
                self.announce_interval.parent = self
                self._children_name_map["announce_interval"] = "announce-interval"

                self.interop = Ptp.Profiles.Profile.Interop()
                self.interop.parent = self
                self._children_name_map["interop"] = "interop"

                self.source_ipv4_address = Ptp.Profiles.Profile.SourceIpv4Address()
                self.source_ipv4_address.parent = self
                self._children_name_map["source_ipv4_address"] = "source-ipv4-address"

                self.slaves = Ptp.Profiles.Profile.Slaves()
                self.slaves.parent = self
                self._children_name_map["slaves"] = "slaves"

                self.sync_interval = Ptp.Profiles.Profile.SyncInterval()
                self.sync_interval.parent = self
                self._children_name_map["sync_interval"] = "sync-interval"

                self.masters = Ptp.Profiles.Profile.Masters()
                self.masters.parent = self
                self._children_name_map["masters"] = "masters"

                self.communication = Ptp.Profiles.Profile.Communication()
                self.communication.parent = self
                self._children_name_map["communication"] = "communication"

                self.delay_request_minimum_interval = Ptp.Profiles.Profile.DelayRequestMinimumInterval()
                self.delay_request_minimum_interval.parent = self
                self._children_name_map["delay_request_minimum_interval"] = "delay-request-minimum-interval"

                self.source_ipv6_address = Ptp.Profiles.Profile.SourceIpv6Address()
                self.source_ipv6_address.parent = self
                self._children_name_map["source_ipv6_address"] = "source-ipv6-address"
                self._segment_path = lambda: "profile" + "[profile-name='" + str(self.profile_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-cfg:ptp/profiles/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.Profiles.Profile, ['profile_name', 'sync_grant_duration', 'general_cos', 'sync_timeout', 'transport', 'announce_timeout', 'cos', 'ipv4ttl', 'port_state', 'delay_response_timeout', 'delay_response_grant_duration', 'event_cos', 'dscp', 'ipv6_hop_limit', 'general_dscp', 'clock_operation', 'announce_grant_duration', 'unicast_grant_invalid_request', 'event_dscp'], name, value)


            class AnnounceInterval(Entity):
                """
                Announce interval
                
                .. attribute:: time_type
                
                	Interval or Frequency
                	**type**\:  :py:class:`PtpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpTime>`
                
                	**default value**\: interval
                
                .. attribute:: time_period
                
                	Time Period
                	**type**\:  :py:class:`PtpTimePeriod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpTimePeriod>`
                
                	**default value**\: 2
                
                

                """

                _prefix = 'ptp-cfg'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.Profiles.Profile.AnnounceInterval, self).__init__()

                    self.yang_name = "announce-interval"
                    self.yang_parent_name = "profile"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('time_type', (YLeaf(YType.enumeration, 'time-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes', 'PtpTime', '')])),
                        ('time_period', (YLeaf(YType.enumeration, 'time-period'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes', 'PtpTimePeriod', '')])),
                    ])
                    self.time_type = None
                    self.time_period = None
                    self._segment_path = lambda: "announce-interval"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Profiles.Profile.AnnounceInterval, ['time_type', 'time_period'], name, value)


            class Interop(Entity):
                """
                Table for interop configuration
                
                .. attribute:: egress_conversion
                
                	Iteroperation configuration to be used on egress
                	**type**\:  :py:class:`EgressConversion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Profiles.Profile.Interop.EgressConversion>`
                
                .. attribute:: ingress_conversion
                
                	Iteroperation configuration to be used on ingress
                	**type**\:  :py:class:`IngressConversion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Profiles.Profile.Interop.IngressConversion>`
                
                .. attribute:: profile
                
                	Profile to interoperate with
                	**type**\:  :py:class:`PtpClockProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpClockProfile>`
                
                .. attribute:: domain
                
                	Domain number of the peer clock
                	**type**\: int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'ptp-cfg'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.Profiles.Profile.Interop, self).__init__()

                    self.yang_name = "interop"
                    self.yang_parent_name = "profile"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("egress-conversion", ("egress_conversion", Ptp.Profiles.Profile.Interop.EgressConversion)), ("ingress-conversion", ("ingress_conversion", Ptp.Profiles.Profile.Interop.IngressConversion))])
                    self._leafs = OrderedDict([
                        ('profile', (YLeaf(YType.enumeration, 'profile'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes', 'PtpClockProfile', '')])),
                        ('domain', (YLeaf(YType.uint32, 'domain'), ['int'])),
                    ])
                    self.profile = None
                    self.domain = None

                    self.egress_conversion = Ptp.Profiles.Profile.Interop.EgressConversion()
                    self.egress_conversion.parent = self
                    self._children_name_map["egress_conversion"] = "egress-conversion"

                    self.ingress_conversion = Ptp.Profiles.Profile.Interop.IngressConversion()
                    self.ingress_conversion.parent = self
                    self._children_name_map["ingress_conversion"] = "ingress-conversion"
                    self._segment_path = lambda: "interop"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Profiles.Profile.Interop, ['profile', 'domain'], name, value)


                class EgressConversion(Entity):
                    """
                    Iteroperation configuration to be used on
                    egress
                    
                    .. attribute:: clock_class_mappings
                    
                    	Table for specific mappings for given clock class values
                    	**type**\:  :py:class:`ClockClassMappings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Profiles.Profile.Interop.EgressConversion.ClockClassMappings>`
                    
                    .. attribute:: clock_accuracy
                    
                    	Clock Accuracy value to use for the peer clock
                    	**type**\: int
                    
                    	**range:** 0..254
                    
                    .. attribute:: priority2
                    
                    	Priority2 value to use for the peer clock
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: clock_class_default
                    
                    	Default clock class to use when a more specific mapping is not available
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: offset_scaled_log_variance
                    
                    	OSLV value to use for the peer clock
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: priority1
                    
                    	Priority1 value to use for the peer clock
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'ptp-cfg'
                    _revision = '2017-02-02'

                    def __init__(self):
                        super(Ptp.Profiles.Profile.Interop.EgressConversion, self).__init__()

                        self.yang_name = "egress-conversion"
                        self.yang_parent_name = "interop"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("clock-class-mappings", ("clock_class_mappings", Ptp.Profiles.Profile.Interop.EgressConversion.ClockClassMappings))])
                        self._leafs = OrderedDict([
                            ('clock_accuracy', (YLeaf(YType.uint32, 'clock-accuracy'), ['int'])),
                            ('priority2', (YLeaf(YType.uint32, 'priority2'), ['int'])),
                            ('clock_class_default', (YLeaf(YType.uint32, 'clock-class-default'), ['int'])),
                            ('offset_scaled_log_variance', (YLeaf(YType.uint32, 'offset-scaled-log-variance'), ['int'])),
                            ('priority1', (YLeaf(YType.uint32, 'priority1'), ['int'])),
                        ])
                        self.clock_accuracy = None
                        self.priority2 = None
                        self.clock_class_default = None
                        self.offset_scaled_log_variance = None
                        self.priority1 = None

                        self.clock_class_mappings = Ptp.Profiles.Profile.Interop.EgressConversion.ClockClassMappings()
                        self.clock_class_mappings.parent = self
                        self._children_name_map["clock_class_mappings"] = "clock-class-mappings"
                        self._segment_path = lambda: "egress-conversion"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.Profiles.Profile.Interop.EgressConversion, ['clock_accuracy', 'priority2', 'clock_class_default', 'offset_scaled_log_variance', 'priority1'], name, value)


                    class ClockClassMappings(Entity):
                        """
                        Table for specific mappings for given clock
                        class values
                        
                        .. attribute:: clock_class_mapping
                        
                        	Mapping for a given clock class value
                        	**type**\: list of  		 :py:class:`ClockClassMapping <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Profiles.Profile.Interop.EgressConversion.ClockClassMappings.ClockClassMapping>`
                        
                        

                        """

                        _prefix = 'ptp-cfg'
                        _revision = '2017-02-02'

                        def __init__(self):
                            super(Ptp.Profiles.Profile.Interop.EgressConversion.ClockClassMappings, self).__init__()

                            self.yang_name = "clock-class-mappings"
                            self.yang_parent_name = "egress-conversion"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("clock-class-mapping", ("clock_class_mapping", Ptp.Profiles.Profile.Interop.EgressConversion.ClockClassMappings.ClockClassMapping))])
                            self._leafs = OrderedDict()

                            self.clock_class_mapping = YList(self)
                            self._segment_path = lambda: "clock-class-mappings"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.Profiles.Profile.Interop.EgressConversion.ClockClassMappings, [], name, value)


                        class ClockClassMapping(Entity):
                            """
                            Mapping for a given clock class value
                            
                            .. attribute:: clock_class_from  (key)
                            
                            	Clock Class to map from
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: clock_class_to
                            
                            	Clock class to map to
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'ptp-cfg'
                            _revision = '2017-02-02'

                            def __init__(self):
                                super(Ptp.Profiles.Profile.Interop.EgressConversion.ClockClassMappings.ClockClassMapping, self).__init__()

                                self.yang_name = "clock-class-mapping"
                                self.yang_parent_name = "clock-class-mappings"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['clock_class_from']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('clock_class_from', (YLeaf(YType.uint32, 'clock-class-from'), ['int'])),
                                    ('clock_class_to', (YLeaf(YType.uint32, 'clock-class-to'), ['int'])),
                                ])
                                self.clock_class_from = None
                                self.clock_class_to = None
                                self._segment_path = lambda: "clock-class-mapping" + "[clock-class-from='" + str(self.clock_class_from) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ptp.Profiles.Profile.Interop.EgressConversion.ClockClassMappings.ClockClassMapping, ['clock_class_from', 'clock_class_to'], name, value)


                class IngressConversion(Entity):
                    """
                    Iteroperation configuration to be used on
                    ingress
                    
                    .. attribute:: clock_class_mappings
                    
                    	Table for specific mappings for given clock class values
                    	**type**\:  :py:class:`ClockClassMappings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Profiles.Profile.Interop.IngressConversion.ClockClassMappings>`
                    
                    .. attribute:: clock_accuracy
                    
                    	Clock Accuracy value to use for the peer clock
                    	**type**\: int
                    
                    	**range:** 0..254
                    
                    .. attribute:: priority2
                    
                    	Priority2 value to use for the peer clock
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: clock_class_default
                    
                    	Default clock class to use when a more specific mapping is not available
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: offset_scaled_log_variance
                    
                    	OSLV value to use for the peer clock
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: priority1
                    
                    	Priority1 value to use for the peer clock
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'ptp-cfg'
                    _revision = '2017-02-02'

                    def __init__(self):
                        super(Ptp.Profiles.Profile.Interop.IngressConversion, self).__init__()

                        self.yang_name = "ingress-conversion"
                        self.yang_parent_name = "interop"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("clock-class-mappings", ("clock_class_mappings", Ptp.Profiles.Profile.Interop.IngressConversion.ClockClassMappings))])
                        self._leafs = OrderedDict([
                            ('clock_accuracy', (YLeaf(YType.uint32, 'clock-accuracy'), ['int'])),
                            ('priority2', (YLeaf(YType.uint32, 'priority2'), ['int'])),
                            ('clock_class_default', (YLeaf(YType.uint32, 'clock-class-default'), ['int'])),
                            ('offset_scaled_log_variance', (YLeaf(YType.uint32, 'offset-scaled-log-variance'), ['int'])),
                            ('priority1', (YLeaf(YType.uint32, 'priority1'), ['int'])),
                        ])
                        self.clock_accuracy = None
                        self.priority2 = None
                        self.clock_class_default = None
                        self.offset_scaled_log_variance = None
                        self.priority1 = None

                        self.clock_class_mappings = Ptp.Profiles.Profile.Interop.IngressConversion.ClockClassMappings()
                        self.clock_class_mappings.parent = self
                        self._children_name_map["clock_class_mappings"] = "clock-class-mappings"
                        self._segment_path = lambda: "ingress-conversion"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.Profiles.Profile.Interop.IngressConversion, ['clock_accuracy', 'priority2', 'clock_class_default', 'offset_scaled_log_variance', 'priority1'], name, value)


                    class ClockClassMappings(Entity):
                        """
                        Table for specific mappings for given clock
                        class values
                        
                        .. attribute:: clock_class_mapping
                        
                        	Mapping for a given clock class value
                        	**type**\: list of  		 :py:class:`ClockClassMapping <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Profiles.Profile.Interop.IngressConversion.ClockClassMappings.ClockClassMapping>`
                        
                        

                        """

                        _prefix = 'ptp-cfg'
                        _revision = '2017-02-02'

                        def __init__(self):
                            super(Ptp.Profiles.Profile.Interop.IngressConversion.ClockClassMappings, self).__init__()

                            self.yang_name = "clock-class-mappings"
                            self.yang_parent_name = "ingress-conversion"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("clock-class-mapping", ("clock_class_mapping", Ptp.Profiles.Profile.Interop.IngressConversion.ClockClassMappings.ClockClassMapping))])
                            self._leafs = OrderedDict()

                            self.clock_class_mapping = YList(self)
                            self._segment_path = lambda: "clock-class-mappings"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.Profiles.Profile.Interop.IngressConversion.ClockClassMappings, [], name, value)


                        class ClockClassMapping(Entity):
                            """
                            Mapping for a given clock class value
                            
                            .. attribute:: clock_class_from  (key)
                            
                            	Clock Class to map from
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: clock_class_to
                            
                            	Clock class to map to
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'ptp-cfg'
                            _revision = '2017-02-02'

                            def __init__(self):
                                super(Ptp.Profiles.Profile.Interop.IngressConversion.ClockClassMappings.ClockClassMapping, self).__init__()

                                self.yang_name = "clock-class-mapping"
                                self.yang_parent_name = "clock-class-mappings"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['clock_class_from']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('clock_class_from', (YLeaf(YType.uint32, 'clock-class-from'), ['int'])),
                                    ('clock_class_to', (YLeaf(YType.uint32, 'clock-class-to'), ['int'])),
                                ])
                                self.clock_class_from = None
                                self.clock_class_to = None
                                self._segment_path = lambda: "clock-class-mapping" + "[clock-class-from='" + str(self.clock_class_from) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ptp.Profiles.Profile.Interop.IngressConversion.ClockClassMappings.ClockClassMapping, ['clock_class_from', 'clock_class_to'], name, value)


            class SourceIpv4Address(Entity):
                """
                Source IPv4 Address
                
                .. attribute:: enable
                
                	Enable source IP address
                	**type**\: bool
                
                .. attribute:: source_ip
                
                	Source IP address to use
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'ptp-cfg'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.Profiles.Profile.SourceIpv4Address, self).__init__()

                    self.yang_name = "source-ipv4-address"
                    self.yang_parent_name = "profile"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                        ('source_ip', (YLeaf(YType.str, 'source-ip'), ['str'])),
                    ])
                    self.enable = None
                    self.source_ip = None
                    self._segment_path = lambda: "source-ipv4-address"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Profiles.Profile.SourceIpv4Address, ['enable', 'source_ip'], name, value)


            class Slaves(Entity):
                """
                Table for slave configuration
                
                .. attribute:: slave
                
                	Slave configuration
                	**type**\: list of  		 :py:class:`Slave <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Profiles.Profile.Slaves.Slave>`
                
                

                """

                _prefix = 'ptp-cfg'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.Profiles.Profile.Slaves, self).__init__()

                    self.yang_name = "slaves"
                    self.yang_parent_name = "profile"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("slave", ("slave", Ptp.Profiles.Profile.Slaves.Slave))])
                    self._leafs = OrderedDict()

                    self.slave = YList(self)
                    self._segment_path = lambda: "slaves"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Profiles.Profile.Slaves, [], name, value)


                class Slave(Entity):
                    """
                    Slave configuration
                    
                    .. attribute:: transport  (key)
                    
                    	Slave Transport Type
                    	**type**\:  :py:class:`PtpEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpEncap>`
                    
                    .. attribute:: ethernet
                    
                    	ethernet
                    	**type**\: list of  		 :py:class:`Ethernet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Profiles.Profile.Slaves.Slave.Ethernet>`
                    
                    .. attribute:: ipv4_or_ipv6
                    
                    	ipv4 or ipv6
                    	**type**\: list of  		 :py:class:`Ipv4OrIpv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Profiles.Profile.Slaves.Slave.Ipv4OrIpv6>`
                    
                    

                    """

                    _prefix = 'ptp-cfg'
                    _revision = '2017-02-02'

                    def __init__(self):
                        super(Ptp.Profiles.Profile.Slaves.Slave, self).__init__()

                        self.yang_name = "slave"
                        self.yang_parent_name = "slaves"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['transport']
                        self._child_classes = OrderedDict([("ethernet", ("ethernet", Ptp.Profiles.Profile.Slaves.Slave.Ethernet)), ("ipv4-or-ipv6", ("ipv4_or_ipv6", Ptp.Profiles.Profile.Slaves.Slave.Ipv4OrIpv6))])
                        self._leafs = OrderedDict([
                            ('transport', (YLeaf(YType.enumeration, 'transport'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes', 'PtpEncap', '')])),
                        ])
                        self.transport = None

                        self.ethernet = YList(self)
                        self.ipv4_or_ipv6 = YList(self)
                        self._segment_path = lambda: "slave" + "[transport='" + str(self.transport) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.Profiles.Profile.Slaves.Slave, ['transport'], name, value)


                    class Ethernet(Entity):
                        """
                        ethernet
                        
                        .. attribute:: slave_mac_address  (key)
                        
                        	Slave MAC Address
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: non_negotiated
                        
                        	Enable non\-negotiated unicast on this interface
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'ptp-cfg'
                        _revision = '2017-02-02'

                        def __init__(self):
                            super(Ptp.Profiles.Profile.Slaves.Slave.Ethernet, self).__init__()

                            self.yang_name = "ethernet"
                            self.yang_parent_name = "slave"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['slave_mac_address']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('slave_mac_address', (YLeaf(YType.str, 'slave-mac-address'), ['str'])),
                                ('non_negotiated', (YLeaf(YType.boolean, 'non-negotiated'), ['bool'])),
                            ])
                            self.slave_mac_address = None
                            self.non_negotiated = None
                            self._segment_path = lambda: "ethernet" + "[slave-mac-address='" + str(self.slave_mac_address) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.Profiles.Profile.Slaves.Slave.Ethernet, ['slave_mac_address', 'non_negotiated'], name, value)


                    class Ipv4OrIpv6(Entity):
                        """
                        ipv4 or ipv6
                        
                        .. attribute:: slave_ip_address  (key)
                        
                        	Slave IP Address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: non_negotiated
                        
                        	Enable non\-negotiated unicast on this interface
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'ptp-cfg'
                        _revision = '2017-02-02'

                        def __init__(self):
                            super(Ptp.Profiles.Profile.Slaves.Slave.Ipv4OrIpv6, self).__init__()

                            self.yang_name = "ipv4-or-ipv6"
                            self.yang_parent_name = "slave"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['slave_ip_address']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('slave_ip_address', (YLeaf(YType.str, 'slave-ip-address'), ['str','str'])),
                                ('non_negotiated', (YLeaf(YType.boolean, 'non-negotiated'), ['bool'])),
                            ])
                            self.slave_ip_address = None
                            self.non_negotiated = None
                            self._segment_path = lambda: "ipv4-or-ipv6" + "[slave-ip-address='" + str(self.slave_ip_address) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.Profiles.Profile.Slaves.Slave.Ipv4OrIpv6, ['slave_ip_address', 'non_negotiated'], name, value)


            class SyncInterval(Entity):
                """
                Sync interval
                
                .. attribute:: time_type
                
                	Interval or Frequency
                	**type**\:  :py:class:`PtpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpTime>`
                
                	**default value**\: interval
                
                .. attribute:: time_period
                
                	Time Period
                	**type**\:  :py:class:`PtpTimePeriod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpTimePeriod>`
                
                	**default value**\: 1
                
                

                """

                _prefix = 'ptp-cfg'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.Profiles.Profile.SyncInterval, self).__init__()

                    self.yang_name = "sync-interval"
                    self.yang_parent_name = "profile"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('time_type', (YLeaf(YType.enumeration, 'time-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes', 'PtpTime', '')])),
                        ('time_period', (YLeaf(YType.enumeration, 'time-period'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes', 'PtpTimePeriod', '')])),
                    ])
                    self.time_type = None
                    self.time_period = None
                    self._segment_path = lambda: "sync-interval"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Profiles.Profile.SyncInterval, ['time_type', 'time_period'], name, value)


            class Masters(Entity):
                """
                Table for master configuration
                
                .. attribute:: master
                
                	Master configuration
                	**type**\: list of  		 :py:class:`Master <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Profiles.Profile.Masters.Master>`
                
                

                """

                _prefix = 'ptp-cfg'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.Profiles.Profile.Masters, self).__init__()

                    self.yang_name = "masters"
                    self.yang_parent_name = "profile"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("master", ("master", Ptp.Profiles.Profile.Masters.Master))])
                    self._leafs = OrderedDict()

                    self.master = YList(self)
                    self._segment_path = lambda: "masters"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Profiles.Profile.Masters, [], name, value)


                class Master(Entity):
                    """
                    Master configuration
                    
                    .. attribute:: transport  (key)
                    
                    	Master Transport Type
                    	**type**\:  :py:class:`PtpEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpEncap>`
                    
                    .. attribute:: ethernet
                    
                    	ethernet
                    	**type**\: list of  		 :py:class:`Ethernet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Profiles.Profile.Masters.Master.Ethernet>`
                    
                    .. attribute:: ipv4_or_ipv6
                    
                    	ipv4 or ipv6
                    	**type**\: list of  		 :py:class:`Ipv4OrIpv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Profiles.Profile.Masters.Master.Ipv4OrIpv6>`
                    
                    

                    """

                    _prefix = 'ptp-cfg'
                    _revision = '2017-02-02'

                    def __init__(self):
                        super(Ptp.Profiles.Profile.Masters.Master, self).__init__()

                        self.yang_name = "master"
                        self.yang_parent_name = "masters"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['transport']
                        self._child_classes = OrderedDict([("ethernet", ("ethernet", Ptp.Profiles.Profile.Masters.Master.Ethernet)), ("ipv4-or-ipv6", ("ipv4_or_ipv6", Ptp.Profiles.Profile.Masters.Master.Ipv4OrIpv6))])
                        self._leafs = OrderedDict([
                            ('transport', (YLeaf(YType.enumeration, 'transport'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes', 'PtpEncap', '')])),
                        ])
                        self.transport = None

                        self.ethernet = YList(self)
                        self.ipv4_or_ipv6 = YList(self)
                        self._segment_path = lambda: "master" + "[transport='" + str(self.transport) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.Profiles.Profile.Masters.Master, ['transport'], name, value)


                    class Ethernet(Entity):
                        """
                        ethernet
                        
                        .. attribute:: master_mac_address  (key)
                        
                        	Master MAC Address \- only used if Transport is Ethernet
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: delay_asymmetry
                        
                        	The delay asymmetry for this master
                        	**type**\:  :py:class:`DelayAsymmetry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Profiles.Profile.Masters.Master.Ethernet.DelayAsymmetry>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: master_clock_class
                        
                        	Master clock class
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: non_negotiated
                        
                        	Enable non\-negotiated unicast on this interface
                        	**type**\: bool
                        
                        .. attribute:: priority
                        
                        	Master priority
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: communication
                        
                        	Communication Model
                        	**type**\:  :py:class:`PtpTransport <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpTransport>`
                        
                        	**default value**\: unicast
                        
                        

                        """

                        _prefix = 'ptp-cfg'
                        _revision = '2017-02-02'

                        def __init__(self):
                            super(Ptp.Profiles.Profile.Masters.Master.Ethernet, self).__init__()

                            self.yang_name = "ethernet"
                            self.yang_parent_name = "master"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['master_mac_address']
                            self._child_classes = OrderedDict([("delay-asymmetry", ("delay_asymmetry", Ptp.Profiles.Profile.Masters.Master.Ethernet.DelayAsymmetry))])
                            self._leafs = OrderedDict([
                                ('master_mac_address', (YLeaf(YType.str, 'master-mac-address'), ['str'])),
                                ('master_clock_class', (YLeaf(YType.uint32, 'master-clock-class'), ['int'])),
                                ('non_negotiated', (YLeaf(YType.boolean, 'non-negotiated'), ['bool'])),
                                ('priority', (YLeaf(YType.uint32, 'priority'), ['int'])),
                                ('communication', (YLeaf(YType.enumeration, 'communication'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes', 'PtpTransport', '')])),
                            ])
                            self.master_mac_address = None
                            self.master_clock_class = None
                            self.non_negotiated = None
                            self.priority = None
                            self.communication = None

                            self.delay_asymmetry = None
                            self._children_name_map["delay_asymmetry"] = "delay-asymmetry"
                            self._segment_path = lambda: "ethernet" + "[master-mac-address='" + str(self.master_mac_address) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.Profiles.Profile.Masters.Master.Ethernet, ['master_mac_address', 'master_clock_class', 'non_negotiated', 'priority', 'communication'], name, value)


                        class DelayAsymmetry(Entity):
                            """
                            The delay asymmetry for this master
                            
                            .. attribute:: magnitude
                            
                            	How much longer the master to slave path takes than the reverse
                            	**type**\: int
                            
                            	**range:** \-500000000..500000000
                            
                            	**mandatory**\: True
                            
                            .. attribute:: units
                            
                            	The units to use for the delay asymmetry
                            	**type**\:  :py:class:`PtpDelayAsymmetryUnits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpDelayAsymmetryUnits>`
                            
                            	**mandatory**\: True
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'ptp-cfg'
                            _revision = '2017-02-02'

                            def __init__(self):
                                super(Ptp.Profiles.Profile.Masters.Master.Ethernet.DelayAsymmetry, self).__init__()

                                self.yang_name = "delay-asymmetry"
                                self.yang_parent_name = "ethernet"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self.is_presence_container = True
                                self._leafs = OrderedDict([
                                    ('magnitude', (YLeaf(YType.int32, 'magnitude'), ['int'])),
                                    ('units', (YLeaf(YType.enumeration, 'units'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes', 'PtpDelayAsymmetryUnits', '')])),
                                ])
                                self.magnitude = None
                                self.units = None
                                self._segment_path = lambda: "delay-asymmetry"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ptp.Profiles.Profile.Masters.Master.Ethernet.DelayAsymmetry, ['magnitude', 'units'], name, value)


                    class Ipv4OrIpv6(Entity):
                        """
                        ipv4 or ipv6
                        
                        .. attribute:: master_ip_address  (key)
                        
                        	Master IP Address \- used if Transport is not Ethernet
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: delay_asymmetry
                        
                        	The delay asymmetry for this master
                        	**type**\:  :py:class:`DelayAsymmetry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Profiles.Profile.Masters.Master.Ipv4OrIpv6.DelayAsymmetry>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: master_clock_class
                        
                        	Master clock class
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: non_negotiated
                        
                        	Enable non\-negotiated unicast on this interface
                        	**type**\: bool
                        
                        .. attribute:: priority
                        
                        	Master priority
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: communication
                        
                        	Communication Model
                        	**type**\:  :py:class:`PtpTransport <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpTransport>`
                        
                        	**default value**\: unicast
                        
                        

                        """

                        _prefix = 'ptp-cfg'
                        _revision = '2017-02-02'

                        def __init__(self):
                            super(Ptp.Profiles.Profile.Masters.Master.Ipv4OrIpv6, self).__init__()

                            self.yang_name = "ipv4-or-ipv6"
                            self.yang_parent_name = "master"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['master_ip_address']
                            self._child_classes = OrderedDict([("delay-asymmetry", ("delay_asymmetry", Ptp.Profiles.Profile.Masters.Master.Ipv4OrIpv6.DelayAsymmetry))])
                            self._leafs = OrderedDict([
                                ('master_ip_address', (YLeaf(YType.str, 'master-ip-address'), ['str','str'])),
                                ('master_clock_class', (YLeaf(YType.uint32, 'master-clock-class'), ['int'])),
                                ('non_negotiated', (YLeaf(YType.boolean, 'non-negotiated'), ['bool'])),
                                ('priority', (YLeaf(YType.uint32, 'priority'), ['int'])),
                                ('communication', (YLeaf(YType.enumeration, 'communication'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes', 'PtpTransport', '')])),
                            ])
                            self.master_ip_address = None
                            self.master_clock_class = None
                            self.non_negotiated = None
                            self.priority = None
                            self.communication = None

                            self.delay_asymmetry = None
                            self._children_name_map["delay_asymmetry"] = "delay-asymmetry"
                            self._segment_path = lambda: "ipv4-or-ipv6" + "[master-ip-address='" + str(self.master_ip_address) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.Profiles.Profile.Masters.Master.Ipv4OrIpv6, ['master_ip_address', 'master_clock_class', 'non_negotiated', 'priority', 'communication'], name, value)


                        class DelayAsymmetry(Entity):
                            """
                            The delay asymmetry for this master
                            
                            .. attribute:: magnitude
                            
                            	How much longer the master to slave path takes than the reverse
                            	**type**\: int
                            
                            	**range:** \-500000000..500000000
                            
                            	**mandatory**\: True
                            
                            .. attribute:: units
                            
                            	The units to use for the delay asymmetry
                            	**type**\:  :py:class:`PtpDelayAsymmetryUnits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpDelayAsymmetryUnits>`
                            
                            	**mandatory**\: True
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'ptp-cfg'
                            _revision = '2017-02-02'

                            def __init__(self):
                                super(Ptp.Profiles.Profile.Masters.Master.Ipv4OrIpv6.DelayAsymmetry, self).__init__()

                                self.yang_name = "delay-asymmetry"
                                self.yang_parent_name = "ipv4-or-ipv6"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self.is_presence_container = True
                                self._leafs = OrderedDict([
                                    ('magnitude', (YLeaf(YType.int32, 'magnitude'), ['int'])),
                                    ('units', (YLeaf(YType.enumeration, 'units'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes', 'PtpDelayAsymmetryUnits', '')])),
                                ])
                                self.magnitude = None
                                self.units = None
                                self._segment_path = lambda: "delay-asymmetry"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ptp.Profiles.Profile.Masters.Master.Ipv4OrIpv6.DelayAsymmetry, ['magnitude', 'units'], name, value)


            class Communication(Entity):
                """
                Communication model
                
                .. attribute:: model
                
                	Communication Model
                	**type**\:  :py:class:`PtpTransport <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpTransport>`
                
                	**default value**\: unicast
                
                .. attribute:: target_address_set
                
                	Target address set
                	**type**\: bool
                
                	**default value**\: false
                
                .. attribute:: target_address
                
                	Target address
                	**type**\: str
                
                

                """

                _prefix = 'ptp-cfg'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.Profiles.Profile.Communication, self).__init__()

                    self.yang_name = "communication"
                    self.yang_parent_name = "profile"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('model', (YLeaf(YType.enumeration, 'model'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes', 'PtpTransport', '')])),
                        ('target_address_set', (YLeaf(YType.boolean, 'target-address-set'), ['bool'])),
                        ('target_address', (YLeaf(YType.str, 'target-address'), ['str'])),
                    ])
                    self.model = None
                    self.target_address_set = None
                    self.target_address = None
                    self._segment_path = lambda: "communication"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Profiles.Profile.Communication, ['model', 'target_address_set', 'target_address'], name, value)


            class DelayRequestMinimumInterval(Entity):
                """
                Minimum delay request interval
                
                .. attribute:: time_type
                
                	Interval or Frequency
                	**type**\:  :py:class:`PtpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpTime>`
                
                	**default value**\: interval
                
                .. attribute:: time_period
                
                	Time Period
                	**type**\:  :py:class:`PtpTimePeriod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpTimePeriod>`
                
                	**default value**\: 1
                
                

                """

                _prefix = 'ptp-cfg'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.Profiles.Profile.DelayRequestMinimumInterval, self).__init__()

                    self.yang_name = "delay-request-minimum-interval"
                    self.yang_parent_name = "profile"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('time_type', (YLeaf(YType.enumeration, 'time-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes', 'PtpTime', '')])),
                        ('time_period', (YLeaf(YType.enumeration, 'time-period'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes', 'PtpTimePeriod', '')])),
                    ])
                    self.time_type = None
                    self.time_period = None
                    self._segment_path = lambda: "delay-request-minimum-interval"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Profiles.Profile.DelayRequestMinimumInterval, ['time_type', 'time_period'], name, value)


            class SourceIpv6Address(Entity):
                """
                Source IPv6 Address
                
                .. attribute:: enable
                
                	Enable source IPv6 address
                	**type**\: bool
                
                .. attribute:: source_ipv6
                
                	Source IPv6 address to use
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'ptp-cfg'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.Profiles.Profile.SourceIpv6Address, self).__init__()

                    self.yang_name = "source-ipv6-address"
                    self.yang_parent_name = "profile"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                        ('source_ipv6', (YLeaf(YType.str, 'source-ipv6'), ['str'])),
                    ])
                    self.enable = None
                    self.source_ipv6 = None
                    self._segment_path = lambda: "source-ipv6-address"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Profiles.Profile.SourceIpv6Address, ['enable', 'source_ipv6'], name, value)


    class UtcOffset(Entity):
        """
        UTC offset configuration
        
        .. attribute:: leap_second_file
        
        	Source file containing leap second information
        	**type**\:  :py:class:`LeapSecondFile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.UtcOffset.LeapSecondFile>`
        
        	**presence node**\: True
        
        .. attribute:: scheduled_offsets
        
        	Table for scheduled UTC offset configuration
        	**type**\:  :py:class:`ScheduledOffsets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.UtcOffset.ScheduledOffsets>`
        
        .. attribute:: base_offset
        
        	Base UTC offset configuration
        	**type**\: int
        
        	**range:** 0..32767
        
        	**units**\: second
        
        

        """

        _prefix = 'ptp-cfg'
        _revision = '2017-02-02'

        def __init__(self):
            super(Ptp.UtcOffset, self).__init__()

            self.yang_name = "utc-offset"
            self.yang_parent_name = "ptp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("leap-second-file", ("leap_second_file", Ptp.UtcOffset.LeapSecondFile)), ("scheduled-offsets", ("scheduled_offsets", Ptp.UtcOffset.ScheduledOffsets))])
            self._leafs = OrderedDict([
                ('base_offset', (YLeaf(YType.uint32, 'base-offset'), ['int'])),
            ])
            self.base_offset = None

            self.leap_second_file = None
            self._children_name_map["leap_second_file"] = "leap-second-file"

            self.scheduled_offsets = Ptp.UtcOffset.ScheduledOffsets()
            self.scheduled_offsets.parent = self
            self._children_name_map["scheduled_offsets"] = "scheduled-offsets"
            self._segment_path = lambda: "utc-offset"
            self._absolute_path = lambda: "Cisco-IOS-XR-ptp-cfg:ptp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ptp.UtcOffset, ['base_offset'], name, value)


        class LeapSecondFile(Entity):
            """
            Source file containing leap second information
            
            .. attribute:: source_url
            
            	URL of source file
            	**type**\: str
            
            	**mandatory**\: True
            
            .. attribute:: polling_frequency
            
            	Polling frequency, in days
            	**type**\: int
            
            	**range:** 1..365
            
            	**units**\: day
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'ptp-cfg'
            _revision = '2017-02-02'

            def __init__(self):
                super(Ptp.UtcOffset.LeapSecondFile, self).__init__()

                self.yang_name = "leap-second-file"
                self.yang_parent_name = "utc-offset"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self.is_presence_container = True
                self._leafs = OrderedDict([
                    ('source_url', (YLeaf(YType.str, 'source-url'), ['str'])),
                    ('polling_frequency', (YLeaf(YType.uint32, 'polling-frequency'), ['int'])),
                ])
                self.source_url = None
                self.polling_frequency = None
                self._segment_path = lambda: "leap-second-file"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-cfg:ptp/utc-offset/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.UtcOffset.LeapSecondFile, ['source_url', 'polling_frequency'], name, value)


        class ScheduledOffsets(Entity):
            """
            Table for scheduled UTC offset configuration
            
            .. attribute:: scheduled_offset
            
            	Scheduled UTC offset configuration
            	**type**\: list of  		 :py:class:`ScheduledOffset <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.UtcOffset.ScheduledOffsets.ScheduledOffset>`
            
            

            """

            _prefix = 'ptp-cfg'
            _revision = '2017-02-02'

            def __init__(self):
                super(Ptp.UtcOffset.ScheduledOffsets, self).__init__()

                self.yang_name = "scheduled-offsets"
                self.yang_parent_name = "utc-offset"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("scheduled-offset", ("scheduled_offset", Ptp.UtcOffset.ScheduledOffsets.ScheduledOffset))])
                self._leafs = OrderedDict()

                self.scheduled_offset = YList(self)
                self._segment_path = lambda: "scheduled-offsets"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-cfg:ptp/utc-offset/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.UtcOffset.ScheduledOffsets, [], name, value)


            class ScheduledOffset(Entity):
                """
                Scheduled UTC offset configuration
                
                .. attribute:: date  (key)
                
                	Offset application date, in ISO\-8601 format (YYYY\-MM\-DD)
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: offset
                
                	UTC offset, in seconds
                	**type**\: int
                
                	**range:** 0..32767
                
                	**mandatory**\: True
                
                	**units**\: second
                
                

                """

                _prefix = 'ptp-cfg'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.UtcOffset.ScheduledOffsets.ScheduledOffset, self).__init__()

                    self.yang_name = "scheduled-offset"
                    self.yang_parent_name = "scheduled-offsets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['date']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('date', (YLeaf(YType.str, 'date'), ['str'])),
                        ('offset', (YLeaf(YType.uint32, 'offset'), ['int'])),
                    ])
                    self.date = None
                    self.offset = None
                    self._segment_path = lambda: "scheduled-offset" + "[date='" + str(self.date) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-cfg:ptp/utc-offset/scheduled-offsets/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.UtcOffset.ScheduledOffsets.ScheduledOffset, ['date', 'offset'], name, value)


    class Logging(Entity):
        """
        PTP logging configuration
        
        .. attribute:: best_master_clock
        
        	PTP best master clock logging configuration
        	**type**\:  :py:class:`BestMasterClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Logging.BestMasterClock>`
        
        

        """

        _prefix = 'ptp-cfg'
        _revision = '2017-02-02'

        def __init__(self):
            super(Ptp.Logging, self).__init__()

            self.yang_name = "logging"
            self.yang_parent_name = "ptp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("best-master-clock", ("best_master_clock", Ptp.Logging.BestMasterClock))])
            self._leafs = OrderedDict()

            self.best_master_clock = Ptp.Logging.BestMasterClock()
            self.best_master_clock.parent = self
            self._children_name_map["best_master_clock"] = "best-master-clock"
            self._segment_path = lambda: "logging"
            self._absolute_path = lambda: "Cisco-IOS-XR-ptp-cfg:ptp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ptp.Logging, [], name, value)


        class BestMasterClock(Entity):
            """
            PTP best master clock logging configuration
            
            .. attribute:: changes
            
            	Enable best master clock changes logging
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ptp-cfg'
            _revision = '2017-02-02'

            def __init__(self):
                super(Ptp.Logging.BestMasterClock, self).__init__()

                self.yang_name = "best-master-clock"
                self.yang_parent_name = "logging"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('changes', (YLeaf(YType.empty, 'changes'), ['Empty'])),
                ])
                self.changes = None
                self._segment_path = lambda: "best-master-clock"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-cfg:ptp/logging/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.Logging.BestMasterClock, ['changes'], name, value)


    class UncalibratedClockClass2(Entity):
        """
        Clock class to be used while acquiring
        phase\-lock to a parent clock.
        
        .. attribute:: clock_class
        
        	Clock Class
        	**type**\: int
        
        	**range:** 0..255
        
        	**mandatory**\: True
        
        .. attribute:: unless_from_holdover
        
        	Unless from holdover flag
        	**type**\: bool
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ptp-cfg'
        _revision = '2017-02-02'

        def __init__(self):
            super(Ptp.UncalibratedClockClass2, self).__init__()

            self.yang_name = "uncalibrated-clock-class2"
            self.yang_parent_name = "ptp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('clock_class', (YLeaf(YType.uint32, 'clock-class'), ['int'])),
                ('unless_from_holdover', (YLeaf(YType.boolean, 'unless-from-holdover'), ['bool'])),
            ])
            self.clock_class = None
            self.unless_from_holdover = None
            self._segment_path = lambda: "uncalibrated-clock-class2"
            self._absolute_path = lambda: "Cisco-IOS-XR-ptp-cfg:ptp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ptp.UncalibratedClockClass2, ['clock_class', 'unless_from_holdover'], name, value)


    class TransparentClock(Entity):
        """
        Transparent clock configuration
        
        .. attribute:: domains
        
        	Table of domains containing transparent clock configuration
        	**type**\:  :py:class:`Domains <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.TransparentClock.Domains>`
        
        

        """

        _prefix = 'ptp-cfg'
        _revision = '2017-02-02'

        def __init__(self):
            super(Ptp.TransparentClock, self).__init__()

            self.yang_name = "transparent-clock"
            self.yang_parent_name = "ptp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("domains", ("domains", Ptp.TransparentClock.Domains))])
            self._leafs = OrderedDict()

            self.domains = Ptp.TransparentClock.Domains()
            self.domains.parent = self
            self._children_name_map["domains"] = "domains"
            self._segment_path = lambda: "transparent-clock"
            self._absolute_path = lambda: "Cisco-IOS-XR-ptp-cfg:ptp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ptp.TransparentClock, [], name, value)


        class Domains(Entity):
            """
            Table of domains containing transparent clock
            configuration
            
            .. attribute:: domain
            
            	Transparent clock domain configuration
            	**type**\: list of  		 :py:class:`Domain <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.TransparentClock.Domains.Domain>`
            
            

            """

            _prefix = 'ptp-cfg'
            _revision = '2017-02-02'

            def __init__(self):
                super(Ptp.TransparentClock.Domains, self).__init__()

                self.yang_name = "domains"
                self.yang_parent_name = "transparent-clock"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("domain", ("domain", Ptp.TransparentClock.Domains.Domain))])
                self._leafs = OrderedDict()

                self.domain = YList(self)
                self._segment_path = lambda: "domains"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-cfg:ptp/transparent-clock/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.TransparentClock.Domains, [], name, value)


            class Domain(Entity):
                """
                Transparent clock domain configuration
                
                .. attribute:: domain  (key)
                
                	Domain
                	**type**\: str
                
                	**pattern:** (all)
                
                

                """

                _prefix = 'ptp-cfg'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.TransparentClock.Domains.Domain, self).__init__()

                    self.yang_name = "domain"
                    self.yang_parent_name = "domains"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['domain']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('domain', (YLeaf(YType.str, 'domain'), ['str'])),
                    ])
                    self.domain = None
                    self._segment_path = lambda: "domain" + "[domain='" + str(self.domain) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-cfg:ptp/transparent-clock/domains/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.TransparentClock.Domains.Domain, ['domain'], name, value)


    class VirtualPort(Entity):
        """
        PTP virtual port configuration
        
        .. attribute:: clock_accuracy
        
        	Virtual port clock accuracy
        	**type**\: int
        
        	**range:** 0..254
        
        .. attribute:: enable
        
        	Enable the PTP Virtual Port
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: priority2
        
        	Virtual port priority2
        	**type**\: int
        
        	**range:** 0..255
        
        .. attribute:: local_priority
        
        	Virtual port local priority
        	**type**\: int
        
        	**range:** 1..255
        
        .. attribute:: offset_scaled_log_variance
        
        	Virtual port OSLV
        	**type**\: int
        
        	**range:** 0..65535
        
        .. attribute:: priority1
        
        	Virtual port priority1
        	**type**\: int
        
        	**range:** 0..255
        
        .. attribute:: clock_class
        
        	Virtual port clock class
        	**type**\: int
        
        	**range:** 0..255
        
        

        """

        _prefix = 'ptp-cfg'
        _revision = '2017-02-02'

        def __init__(self):
            super(Ptp.VirtualPort, self).__init__()

            self.yang_name = "virtual-port"
            self.yang_parent_name = "ptp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('clock_accuracy', (YLeaf(YType.uint32, 'clock-accuracy'), ['int'])),
                ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                ('priority2', (YLeaf(YType.uint32, 'priority2'), ['int'])),
                ('local_priority', (YLeaf(YType.uint32, 'local-priority'), ['int'])),
                ('offset_scaled_log_variance', (YLeaf(YType.uint32, 'offset-scaled-log-variance'), ['int'])),
                ('priority1', (YLeaf(YType.uint32, 'priority1'), ['int'])),
                ('clock_class', (YLeaf(YType.uint32, 'clock-class'), ['int'])),
            ])
            self.clock_accuracy = None
            self.enable = None
            self.priority2 = None
            self.local_priority = None
            self.offset_scaled_log_variance = None
            self.priority1 = None
            self.clock_class = None
            self._segment_path = lambda: "virtual-port"
            self._absolute_path = lambda: "Cisco-IOS-XR-ptp-cfg:ptp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ptp.VirtualPort, ['clock_accuracy', 'enable', 'priority2', 'local_priority', 'offset_scaled_log_variance', 'priority1', 'clock_class'], name, value)

    def clone_ptr(self):
        self._top_entity = Ptp()
        return self._top_entity


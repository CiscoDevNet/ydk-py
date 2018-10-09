""" CISCO_IP_URPF_MIB 

Unicast Reverse Path Forwarding (URPF) is a function that
checks the validity of the source address of IP packets
received on an interface. This in an attempt to prevent
Denial of Service attacks based on IP address spoofing.

URPF checks validity of a source address by determining
whether the packet would be successfully routed as a
destination address. 
Based on configuration, the check made
can be for existence of any route for the address, or more
strictly for a route out the interface on which the packet
was received by the device. When a violating packet is
detected, it can be dropped. 
This MIB allows detection of
spoofingevents.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class UnicastRpfType(Enum):
    """
    UnicastRpfType (Enum Class)

    An enumerated integer\-value describing the type of

    unicast Reverse Path Forwarding (RPF) a system applies to

    traffic received on an interface. UnicastRpfTypes 'strict' and 

    'loose' RPF methods are defined in RFC3704.

    'disabled'

        The system does not perform unicast RPF on packets received

        by the interface.

    'strict'

        The system performs strict unicast RPF on packets received

        by the interface.

    'loose'

        The system performs loose unicast RPF on packets received by

        the interface.

    .. data:: strict = 1

    .. data:: loose = 2

    .. data:: disabled = 3

    """

    strict = Enum.YLeaf(1, "strict")

    loose = Enum.YLeaf(2, "loose")

    disabled = Enum.YLeaf(3, "disabled")



class CISCOIPURPFMIB(Entity):
    """
    
    
    .. attribute:: cipurpfscalar
    
    	
    	**type**\:  :py:class:`CipUrpfScalar <ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB.CISCOIPURPFMIB.CipUrpfScalar>`
    
    .. attribute:: cipurpftable
    
    	This table contains summary information for the managed device on URPF dropping
    	**type**\:  :py:class:`CipUrpfTable <ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB.CISCOIPURPFMIB.CipUrpfTable>`
    
    .. attribute:: cipurpfifmontable
    
    	This table contains information on URPF dropping on an interface
    	**type**\:  :py:class:`CipUrpfIfMonTable <ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB.CISCOIPURPFMIB.CipUrpfIfMonTable>`
    
    .. attribute:: cipurpfvrfiftable
    
    	This table contains statistics information for interfaces performing URPF using VRF table to determine reachability
    	**type**\:  :py:class:`CipUrpfVrfIfTable <ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB.CISCOIPURPFMIB.CipUrpfVrfIfTable>`
    
    .. attribute:: cipurpfvrftable
    
    	This table enables indexing URPF drop statistics by Virtual Routing and Forwarding instances
    	**type**\:  :py:class:`CipUrpfVrfTable <ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB.CISCOIPURPFMIB.CipUrpfVrfTable>`
    
    

    """

    _prefix = 'CISCO-IP-URPF-MIB'
    _revision = '2011-12-29'

    def __init__(self):
        super(CISCOIPURPFMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IP-URPF-MIB"
        self.yang_parent_name = "CISCO-IP-URPF-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("cipUrpfScalar", ("cipurpfscalar", CISCOIPURPFMIB.CipUrpfScalar)), ("cipUrpfTable", ("cipurpftable", CISCOIPURPFMIB.CipUrpfTable)), ("cipUrpfIfMonTable", ("cipurpfifmontable", CISCOIPURPFMIB.CipUrpfIfMonTable)), ("cipUrpfVrfIfTable", ("cipurpfvrfiftable", CISCOIPURPFMIB.CipUrpfVrfIfTable)), ("cipUrpfVrfTable", ("cipurpfvrftable", CISCOIPURPFMIB.CipUrpfVrfTable))])
        self._leafs = OrderedDict()

        self.cipurpfscalar = CISCOIPURPFMIB.CipUrpfScalar()
        self.cipurpfscalar.parent = self
        self._children_name_map["cipurpfscalar"] = "cipUrpfScalar"

        self.cipurpftable = CISCOIPURPFMIB.CipUrpfTable()
        self.cipurpftable.parent = self
        self._children_name_map["cipurpftable"] = "cipUrpfTable"

        self.cipurpfifmontable = CISCOIPURPFMIB.CipUrpfIfMonTable()
        self.cipurpfifmontable.parent = self
        self._children_name_map["cipurpfifmontable"] = "cipUrpfIfMonTable"

        self.cipurpfvrfiftable = CISCOIPURPFMIB.CipUrpfVrfIfTable()
        self.cipurpfvrfiftable.parent = self
        self._children_name_map["cipurpfvrfiftable"] = "cipUrpfVrfIfTable"

        self.cipurpfvrftable = CISCOIPURPFMIB.CipUrpfVrfTable()
        self.cipurpfvrftable.parent = self
        self._children_name_map["cipurpfvrftable"] = "cipUrpfVrfTable"
        self._segment_path = lambda: "CISCO-IP-URPF-MIB:CISCO-IP-URPF-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCOIPURPFMIB, [], name, value)


    class CipUrpfScalar(Entity):
        """
        
        
        .. attribute:: cipurpfdropratewindow
        
        	The window of time in the recent past over which the drop count used in the drop rate computation is collected.  This global value applies for the computation of all URPF  rates, global and per\-interface.   Once the period over which computations have been  performed exceeds cipUrpfDropRateWindow, every time a  computation is performed, the window slides up to end  at the current time and start at cipUrpfDropRateWindow  seconds before.   The cipUrpfDropRateWindow must be greater than or equal to the interval between computations  (cipUrpfComputeInterval).  Since the agent must save the drop count values for each compute interval in order to slide the window, the number of counts saved is the quotient of cipUrpfDropRateWindow divided by cipUrpfComputeInterval
        	**type**\: int
        
        	**range:** 1..600
        
        	**units**\: seconds
        
        .. attribute:: cipurpfcomputeinterval
        
        	The time between rate computations. This global value applies for the computation of all URPF rates, global and per\-interface.  When the value of cipUrpfComputeInterval is changed, the interval in\-progress proceeds as though the value had not changed. The change will apply to the length of subsequent intervals.  The cipUrpfComputeInterval must be less than or equal  to the cipUrpfDropRateWindow
        	**type**\: int
        
        	**range:** 1..120
        
        	**units**\: seconds
        
        .. attribute:: cipurpfdropnotifyholddowntime
        
        	The minimum time between issuance of cipUrpfIfDropRateNotify notifications for a  particular interface and packet forwarding type.  Notifications are generated for each interface and packet forwarding type that exceeds the drop\-rate.  When a Notify is sent because the drop\-rate is  exceeded for a particular interface and forwarding type, the time specified by this object is used to  specify the minimum time that must elapse before  another Notify can be sent for that interface and forwarding type. The time is specified globally but  used individually
        	**type**\: int
        
        	**range:** 1..1000
        
        	**units**\: seconds
        
        

        """

        _prefix = 'CISCO-IP-URPF-MIB'
        _revision = '2011-12-29'

        def __init__(self):
            super(CISCOIPURPFMIB.CipUrpfScalar, self).__init__()

            self.yang_name = "cipUrpfScalar"
            self.yang_parent_name = "CISCO-IP-URPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cipurpfdropratewindow', (YLeaf(YType.int32, 'cipUrpfDropRateWindow'), ['int'])),
                ('cipurpfcomputeinterval', (YLeaf(YType.int32, 'cipUrpfComputeInterval'), ['int'])),
                ('cipurpfdropnotifyholddowntime', (YLeaf(YType.int32, 'cipUrpfDropNotifyHoldDownTime'), ['int'])),
            ])
            self.cipurpfdropratewindow = None
            self.cipurpfcomputeinterval = None
            self.cipurpfdropnotifyholddowntime = None
            self._segment_path = lambda: "cipUrpfScalar"
            self._absolute_path = lambda: "CISCO-IP-URPF-MIB:CISCO-IP-URPF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPURPFMIB.CipUrpfScalar, ['cipurpfdropratewindow', 'cipurpfcomputeinterval', 'cipurpfdropnotifyholddowntime'], name, value)


    class CipUrpfTable(Entity):
        """
        This table contains summary information for the
        managed device on URPF dropping.
        
        .. attribute:: cipurpfentry
        
        	If the managed device supports URPF dropping, a row exists for each IP version type (v4 and v6). A row contains summary information on URPF dropping over the entire managed device
        	**type**\: list of  		 :py:class:`CipUrpfEntry <ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB.CISCOIPURPFMIB.CipUrpfTable.CipUrpfEntry>`
        
        

        """

        _prefix = 'CISCO-IP-URPF-MIB'
        _revision = '2011-12-29'

        def __init__(self):
            super(CISCOIPURPFMIB.CipUrpfTable, self).__init__()

            self.yang_name = "cipUrpfTable"
            self.yang_parent_name = "CISCO-IP-URPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cipUrpfEntry", ("cipurpfentry", CISCOIPURPFMIB.CipUrpfTable.CipUrpfEntry))])
            self._leafs = OrderedDict()

            self.cipurpfentry = YList(self)
            self._segment_path = lambda: "cipUrpfTable"
            self._absolute_path = lambda: "CISCO-IP-URPF-MIB:CISCO-IP-URPF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPURPFMIB.CipUrpfTable, [], name, value)


        class CipUrpfEntry(Entity):
            """
            If the managed device supports URPF dropping,
            a row exists for each IP version type (v4 and v6).
            A row contains summary information on URPF
            dropping over the entire managed device.
            
            .. attribute:: cipurpfipversion  (key)
            
            	Specifies the version of IP forwarding on an interface to which the table row URPF counts, rates, and configuration apply
            	**type**\:  :py:class:`CipUrpfIpVersion <ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB.CISCOIPURPFMIB.CipUrpfTable.CipUrpfEntry.CipUrpfIpVersion>`
            
            .. attribute:: cipurpfdrops
            
            	Sum of dropped IP version cipUrpfIpVersion packets failing a URPF check. This value is the sum of drops of packets  received on all interfaces of the managed device
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cipurpfdroprate
            
            	The rate of packet drops of IP version cipUrpfIpVersion packets due to URPF for the managed device. The per\-interface drop rate notification is issued on rates exceeding a limit (rising rate). This dropping may indicate an security attack on the network. To determine whether the attack/event is over, the NMS must consult the managed device. This object can be polled to determine the recent drop rate for the managed device as a whole, in addition to querying particular interface objects.  This object is the average rate of dropping over the most recent window of time. The rate is computed by dividing the number of packets dropped over a window by the window time in seconds. The window time is specified by cipUrpfDropRateWindow. Each time the drop rate is computed, and at system startup, a snapshot is taken of the latest value of cipUrpfDrops. Subtracting from this the snapshot of cipUrpfDrops at the start of the current window of time gives the number of packets dropped. The drop rate is computed every cipUrpfComputeInterval seconds. As an example, let cipUrpfDropRateWindow be 300 seconds, and cipUrpfComputeInterval 30 seconds. Every 30 seconds, the drop count five minutes previous is subtracted from the current drop count, and the result is divided by 300 to arrive at the drop rate.  At device start\-up, until the device has been up more than cipUrpfDropRateWindow, when drop rate is computed, the value of cipUrpfDrops is divided by the time the device has been up.  After the device has been up for cipUrpfDropRateWindow, when drop rate is computed, the number of packet drops counted from interval start time to the computation time is divided by cipUrpfDropRateWindow.  Changes to cipUrpfDropRateWindow are not reflected in this object until the next computation time.  The rate from the most recent computation is the value fetched until the subsequent computation is performed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: packets per second
            
            

            """

            _prefix = 'CISCO-IP-URPF-MIB'
            _revision = '2011-12-29'

            def __init__(self):
                super(CISCOIPURPFMIB.CipUrpfTable.CipUrpfEntry, self).__init__()

                self.yang_name = "cipUrpfEntry"
                self.yang_parent_name = "cipUrpfTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cipurpfipversion']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cipurpfipversion', (YLeaf(YType.enumeration, 'cipUrpfIpVersion'), [('ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB', 'CISCOIPURPFMIB', 'CipUrpfTable.CipUrpfEntry.CipUrpfIpVersion')])),
                    ('cipurpfdrops', (YLeaf(YType.uint32, 'cipUrpfDrops'), ['int'])),
                    ('cipurpfdroprate', (YLeaf(YType.uint32, 'cipUrpfDropRate'), ['int'])),
                ])
                self.cipurpfipversion = None
                self.cipurpfdrops = None
                self.cipurpfdroprate = None
                self._segment_path = lambda: "cipUrpfEntry" + "[cipUrpfIpVersion='" + str(self.cipurpfipversion) + "']"
                self._absolute_path = lambda: "CISCO-IP-URPF-MIB:CISCO-IP-URPF-MIB/cipUrpfTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPURPFMIB.CipUrpfTable.CipUrpfEntry, ['cipurpfipversion', 'cipurpfdrops', 'cipurpfdroprate'], name, value)

            class CipUrpfIpVersion(Enum):
                """
                CipUrpfIpVersion (Enum Class)

                Specifies the version of IP forwarding on an interface

                to which the table row URPF counts, rates, and

                configuration apply.

                .. data:: ipv4 = 1

                .. data:: ipv6 = 2

                """

                ipv4 = Enum.YLeaf(1, "ipv4")

                ipv6 = Enum.YLeaf(2, "ipv6")



    class CipUrpfIfMonTable(Entity):
        """
        This table contains information on URPF dropping on
        an interface.
        
        .. attribute:: cipurpfifmonentry
        
        	If IPv4 packet forwarding is configured on an interface, and is configured to perform URPF checking, a row appears in this table with indices [ifIndex][ipv4]. If IPv4 packet forwarding is deconfigured, or URPF checking is deconfigured, the row disappears.  If IPv6 packet forwarding is configured on an interface, and is configured to perform URPF checking, a row appears in the table with indices [ifIndex][ipv6].  If IPv6 packet forwarding is deconfigured, or URPF checking is deconfigured, the row disappears
        	**type**\: list of  		 :py:class:`CipUrpfIfMonEntry <ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB.CISCOIPURPFMIB.CipUrpfIfMonTable.CipUrpfIfMonEntry>`
        
        

        """

        _prefix = 'CISCO-IP-URPF-MIB'
        _revision = '2011-12-29'

        def __init__(self):
            super(CISCOIPURPFMIB.CipUrpfIfMonTable, self).__init__()

            self.yang_name = "cipUrpfIfMonTable"
            self.yang_parent_name = "CISCO-IP-URPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cipUrpfIfMonEntry", ("cipurpfifmonentry", CISCOIPURPFMIB.CipUrpfIfMonTable.CipUrpfIfMonEntry))])
            self._leafs = OrderedDict()

            self.cipurpfifmonentry = YList(self)
            self._segment_path = lambda: "cipUrpfIfMonTable"
            self._absolute_path = lambda: "CISCO-IP-URPF-MIB:CISCO-IP-URPF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPURPFMIB.CipUrpfIfMonTable, [], name, value)


        class CipUrpfIfMonEntry(Entity):
            """
            If IPv4 packet forwarding is configured on an interface,
            and is configured to perform URPF checking, a row appears
            in this table with indices [ifIndex][ipv4]. If IPv4
            packet forwarding is deconfigured, or URPF checking
            is deconfigured, the row disappears.
            
            If IPv6 packet forwarding is configured on an interface,
            and is configured to perform URPF checking, a row appears
            in the table with indices [ifIndex][ipv6].  If IPv6
            packet forwarding is deconfigured, or URPF checking
            is deconfigured, the row disappears.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: cipurpfifipversion  (key)
            
            	Specifies the version of IP forwarding on an interface to which the table row URPF counts, rates, and  configuration apply
            	**type**\:  :py:class:`CipUrpfIfIpVersion <ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB.CISCOIPURPFMIB.CipUrpfIfMonTable.CipUrpfIfMonEntry.CipUrpfIfIpVersion>`
            
            .. attribute:: cipurpfifdrops
            
            	The number of IP packets of version cipUrpfIfIpVersion failing the URPF check and dropped by the managed device on a particular interface.  Discontinuities in the value of this variable can occur  at re\-initialization of the management system, and at  other times as indicated by the values of  cipUrpfIfDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cipurpfifsuppresseddrops
            
            	The number of IP packets of version cipUrpfIfIpVersion failing the URPF check but given a reprieve and not  dropped by the managed device. Depending on the  device configuration and capabilities, the following  cases may cause incrementing of the counter\:  \- if the managed device is configured to allow self\-pings    and the managed device pings itself. \- if the managed device is configured for loose URPF (if any   interface has a route to the source), and the strict   case fails while the loose case passes. \- DHCP Request packets (src 0.0.0.0 dst 255.255.255.255)    will pass after initially being marked for drop. \- RIP routing on unnumbered interfaces will pass after    initially being marked for drop. \- multicast packets will pass after initially being marked    for drop \- ACL's can be applied to permit packets after initially    being marked for drop.  Discontinuities in the value of this variable can occur  at re\-initialization of the management system, and at  other times as indicated by the values of  cipUrpfIfDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cipurpfifdroprate
            
            	The rate of packet drops of IP version cipUrpfIfIpVersion packets due to URPF on the interface.   This object is the average rate of dropping over the most  recent interval of time. The rate is computed by dividing the number of packets dropped over an interval by the  interval time in seconds. Each time the drop rate is computed, and at system startup, a snapshot is taken of the latest value of cipUrpfIfDrops. Subtracting from this the snapshot of cipUrpfIfDrops at the start of the current interval of time gives the number of packets dropped. The drop rate is computed every cipUrpfComputeInterval seconds.  When drop rate is computed, if time since the creation of  a row in cipUrpfIfMonTable is less than  cipUrpfDropRateWindow, the value of cipUrpfIfDrops is  divided by the time since row was created.  After the row has been in existence for  cipUrpfDropRateWindow, when drop rate is computed, the  number of packet drops counted on the interface from  interval start time to the computation time is divided  by cipUrpfDropRateWindow.  Changes to cipUrpfDropRateWindow are not reflected in this object until the next computation time.  The rate from the  most recent computation is the value  fetched until the subsequent computation is performed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: packets/second
            
            .. attribute:: cipurpfifdiscontinuitytime
            
            	The value of sysUpTime on the most recent occasion at which this interface's  counters suffered  a discontinuity. If no such discontinuities have occurred since the last re\-initialization of the local management subsystem, then this object contains a value of zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipurpfifdropratenotifyenable
            
            	This object specifies whether the system produces the cipUrpfIfDropRateNotify notification as a result of URPF  dropping of version cipUrpfIfIpVersion IP packets on this  interface. A false value prevents such notifications from  being generated by this system
            	**type**\: bool
            
            .. attribute:: cipurpfifnotifydropratethreshold
            
            	When the calculated rate of URPF packet drops (cipUrpfIfDropRate) meets or exceeds the value  specified by this object, a cipUrpfIfDropRateNotify  notification is sent if cipUrpfIfDropRateNotifyEnable  is set to true, and no such notification for the IP version has been sent for this interface for the  hold\-down period.  Note that due to the calculation used for drop rate,  if there are less than n drop events in an n\-second period the notification will not be generated. To allow for the detection of a small number of drop events, the value 0 (zero) is used to indicate that if any drop events occur during the interval, a notification is generated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: packets/second
            
            .. attribute:: cipurpfifnotifydrholddownreset
            
            	Setting this object to true causes the five\-minute hold\-down timer for emitting URPF drop rate  notifications for IP version cipUrpfIfIpVersion on  the interface to be short\-circuited.  If a notification  is due and would be emitted for the interface if the  five\-minutes elapsed, setting this object will cause  the notification to be sent.  This is a trigger, and doesn't hold information. It is set and an action is performed. Therefore a get for  this object always returns false
            	**type**\: bool
            
            .. attribute:: cipurpfifcheckstrict
            
            	Interface configuration indicating the strictness of the reachability check performed  on the interface. \- strict\: check that source addr is reachable via            the interface it came in on. \- loose \: check that source addr is reachable via            some interface on the device
            	**type**\:  :py:class:`CipUrpfIfCheckStrict <ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB.CISCOIPURPFMIB.CipUrpfIfMonTable.CipUrpfIfMonEntry.CipUrpfIfCheckStrict>`
            
            .. attribute:: cipurpfifwhichroutetableid
            
            	Interface configuration indicating the routing table consulted for the reachability check\: \- default\: the non\-private routing table for of the             managed system. \- vrf   \: a particular VPN routing table
            	**type**\:  :py:class:`CipUrpfIfWhichRouteTableID <ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB.CISCOIPURPFMIB.CipUrpfIfMonTable.CipUrpfIfMonEntry.CipUrpfIfWhichRouteTableID>`
            
            .. attribute:: cipurpfifvrfname
            
            	If the value of cipUrpfIfWhichRouteTableID is 'vrf', the name of the VRF Table. Otherwise a zero\-length string
            	**type**\: str
            
            	**length:** 0..32
            
            

            """

            _prefix = 'CISCO-IP-URPF-MIB'
            _revision = '2011-12-29'

            def __init__(self):
                super(CISCOIPURPFMIB.CipUrpfIfMonTable.CipUrpfIfMonEntry, self).__init__()

                self.yang_name = "cipUrpfIfMonEntry"
                self.yang_parent_name = "cipUrpfIfMonTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','cipurpfifipversion']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('cipurpfifipversion', (YLeaf(YType.enumeration, 'cipUrpfIfIpVersion'), [('ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB', 'CISCOIPURPFMIB', 'CipUrpfIfMonTable.CipUrpfIfMonEntry.CipUrpfIfIpVersion')])),
                    ('cipurpfifdrops', (YLeaf(YType.uint32, 'cipUrpfIfDrops'), ['int'])),
                    ('cipurpfifsuppresseddrops', (YLeaf(YType.uint32, 'cipUrpfIfSuppressedDrops'), ['int'])),
                    ('cipurpfifdroprate', (YLeaf(YType.uint32, 'cipUrpfIfDropRate'), ['int'])),
                    ('cipurpfifdiscontinuitytime', (YLeaf(YType.uint32, 'cipUrpfIfDiscontinuityTime'), ['int'])),
                    ('cipurpfifdropratenotifyenable', (YLeaf(YType.boolean, 'cipUrpfIfDropRateNotifyEnable'), ['bool'])),
                    ('cipurpfifnotifydropratethreshold', (YLeaf(YType.uint32, 'cipUrpfIfNotifyDropRateThreshold'), ['int'])),
                    ('cipurpfifnotifydrholddownreset', (YLeaf(YType.boolean, 'cipUrpfIfNotifyDrHoldDownReset'), ['bool'])),
                    ('cipurpfifcheckstrict', (YLeaf(YType.enumeration, 'cipUrpfIfCheckStrict'), [('ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB', 'CISCOIPURPFMIB', 'CipUrpfIfMonTable.CipUrpfIfMonEntry.CipUrpfIfCheckStrict')])),
                    ('cipurpfifwhichroutetableid', (YLeaf(YType.enumeration, 'cipUrpfIfWhichRouteTableID'), [('ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB', 'CISCOIPURPFMIB', 'CipUrpfIfMonTable.CipUrpfIfMonEntry.CipUrpfIfWhichRouteTableID')])),
                    ('cipurpfifvrfname', (YLeaf(YType.str, 'cipUrpfIfVrfName'), ['str'])),
                ])
                self.ifindex = None
                self.cipurpfifipversion = None
                self.cipurpfifdrops = None
                self.cipurpfifsuppresseddrops = None
                self.cipurpfifdroprate = None
                self.cipurpfifdiscontinuitytime = None
                self.cipurpfifdropratenotifyenable = None
                self.cipurpfifnotifydropratethreshold = None
                self.cipurpfifnotifydrholddownreset = None
                self.cipurpfifcheckstrict = None
                self.cipurpfifwhichroutetableid = None
                self.cipurpfifvrfname = None
                self._segment_path = lambda: "cipUrpfIfMonEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[cipUrpfIfIpVersion='" + str(self.cipurpfifipversion) + "']"
                self._absolute_path = lambda: "CISCO-IP-URPF-MIB:CISCO-IP-URPF-MIB/cipUrpfIfMonTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPURPFMIB.CipUrpfIfMonTable.CipUrpfIfMonEntry, ['ifindex', 'cipurpfifipversion', 'cipurpfifdrops', 'cipurpfifsuppresseddrops', 'cipurpfifdroprate', 'cipurpfifdiscontinuitytime', 'cipurpfifdropratenotifyenable', 'cipurpfifnotifydropratethreshold', 'cipurpfifnotifydrholddownreset', 'cipurpfifcheckstrict', 'cipurpfifwhichroutetableid', 'cipurpfifvrfname'], name, value)

            class CipUrpfIfCheckStrict(Enum):
                """
                CipUrpfIfCheckStrict (Enum Class)

                Interface configuration indicating the strictness of

                the reachability check performed 

                on the interface.

                \- strict\: check that source addr is reachable via 

                          the interface it came in on.

                \- loose \: check that source addr is reachable via 

                          some interface on the device.

                .. data:: strict = 1

                .. data:: loose = 2

                """

                strict = Enum.YLeaf(1, "strict")

                loose = Enum.YLeaf(2, "loose")


            class CipUrpfIfIpVersion(Enum):
                """
                CipUrpfIfIpVersion (Enum Class)

                Specifies the version of IP forwarding on an interface

                to which the table row URPF counts, rates, and 

                configuration apply.

                .. data:: ipv4 = 1

                .. data:: ipv6 = 2

                """

                ipv4 = Enum.YLeaf(1, "ipv4")

                ipv6 = Enum.YLeaf(2, "ipv6")


            class CipUrpfIfWhichRouteTableID(Enum):
                """
                CipUrpfIfWhichRouteTableID (Enum Class)

                Interface configuration indicating the routing table

                consulted for the reachability check\:

                \- default\: the non\-private routing table for of the 

                           managed system.

                \- vrf   \: a particular VPN routing table.

                .. data:: default = 1

                .. data:: vrf = 2

                """

                default = Enum.YLeaf(1, "default")

                vrf = Enum.YLeaf(2, "vrf")



    class CipUrpfVrfIfTable(Entity):
        """
        This table contains statistics information for interfaces
        performing URPF using VRF table to determine reachability.
        
        .. attribute:: cipurpfvrfifentry
        
        	An entry exists for a VRF and interface if and only if the VRF associated with the interface is configured  to perform IP URPF checking using the routing  table for the VRF
        	**type**\: list of  		 :py:class:`CipUrpfVrfIfEntry <ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB.CISCOIPURPFMIB.CipUrpfVrfIfTable.CipUrpfVrfIfEntry>`
        
        

        """

        _prefix = 'CISCO-IP-URPF-MIB'
        _revision = '2011-12-29'

        def __init__(self):
            super(CISCOIPURPFMIB.CipUrpfVrfIfTable, self).__init__()

            self.yang_name = "cipUrpfVrfIfTable"
            self.yang_parent_name = "CISCO-IP-URPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cipUrpfVrfIfEntry", ("cipurpfvrfifentry", CISCOIPURPFMIB.CipUrpfVrfIfTable.CipUrpfVrfIfEntry))])
            self._leafs = OrderedDict()

            self.cipurpfvrfifentry = YList(self)
            self._segment_path = lambda: "cipUrpfVrfIfTable"
            self._absolute_path = lambda: "CISCO-IP-URPF-MIB:CISCO-IP-URPF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPURPFMIB.CipUrpfVrfIfTable, [], name, value)


        class CipUrpfVrfIfEntry(Entity):
            """
            An entry exists for a VRF and interface if and only
            if the VRF associated with the interface is configured 
            to perform IP URPF checking using the routing 
            table for the VRF.
            
            .. attribute:: cipurpfvrfname  (key)
            
            	
            	**type**\: str
            
            	**length:** 0..32
            
            	**refers to**\:  :py:class:`cipurpfvrfname <ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB.CISCOIPURPFMIB.CipUrpfVrfTable.CipUrpfVrfEntry>`
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: cipurpfvrfifdrops
            
            	The number of packets failing the URPF check for a VRF on the interface and dropped by the managed device.  Discontinuities in the value of this variable can occur  at re\-initialization of the management system, and at  other times as indicated by the values of  cipUrpfVrfIfDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cipurpfvrfifdiscontinuitytime
            
            	The value of sysUpTime on the most recent occasion at which the URPF counters for this VRF on this interface  suffered  a discontinuity.  If no such discontinuities  have occurred since the last re\-initialization of the local management subsystem, then this object contains a  value of zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IP-URPF-MIB'
            _revision = '2011-12-29'

            def __init__(self):
                super(CISCOIPURPFMIB.CipUrpfVrfIfTable.CipUrpfVrfIfEntry, self).__init__()

                self.yang_name = "cipUrpfVrfIfEntry"
                self.yang_parent_name = "cipUrpfVrfIfTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cipurpfvrfname','ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cipurpfvrfname', (YLeaf(YType.str, 'cipUrpfVrfName'), ['str'])),
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('cipurpfvrfifdrops', (YLeaf(YType.uint32, 'cipUrpfVrfIfDrops'), ['int'])),
                    ('cipurpfvrfifdiscontinuitytime', (YLeaf(YType.uint32, 'cipUrpfVrfIfDiscontinuityTime'), ['int'])),
                ])
                self.cipurpfvrfname = None
                self.ifindex = None
                self.cipurpfvrfifdrops = None
                self.cipurpfvrfifdiscontinuitytime = None
                self._segment_path = lambda: "cipUrpfVrfIfEntry" + "[cipUrpfVrfName='" + str(self.cipurpfvrfname) + "']" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-IP-URPF-MIB:CISCO-IP-URPF-MIB/cipUrpfVrfIfTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPURPFMIB.CipUrpfVrfIfTable.CipUrpfVrfIfEntry, ['cipurpfvrfname', 'ifindex', 'cipurpfvrfifdrops', 'cipurpfvrfifdiscontinuitytime'], name, value)


    class CipUrpfVrfTable(Entity):
        """
        This table enables indexing URPF drop statistics
        by Virtual Routing and Forwarding instances.
        
        .. attribute:: cipurpfvrfentry
        
        	An entry exists for a VRF if and only if the VRF is associated with an interface that is configured to perform IP URPF checking using the routing table  for that VRF
        	**type**\: list of  		 :py:class:`CipUrpfVrfEntry <ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB.CISCOIPURPFMIB.CipUrpfVrfTable.CipUrpfVrfEntry>`
        
        

        """

        _prefix = 'CISCO-IP-URPF-MIB'
        _revision = '2011-12-29'

        def __init__(self):
            super(CISCOIPURPFMIB.CipUrpfVrfTable, self).__init__()

            self.yang_name = "cipUrpfVrfTable"
            self.yang_parent_name = "CISCO-IP-URPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cipUrpfVrfEntry", ("cipurpfvrfentry", CISCOIPURPFMIB.CipUrpfVrfTable.CipUrpfVrfEntry))])
            self._leafs = OrderedDict()

            self.cipurpfvrfentry = YList(self)
            self._segment_path = lambda: "cipUrpfVrfTable"
            self._absolute_path = lambda: "CISCO-IP-URPF-MIB:CISCO-IP-URPF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPURPFMIB.CipUrpfVrfTable, [], name, value)


        class CipUrpfVrfEntry(Entity):
            """
            An entry exists for a VRF if and only if the VRF
            is associated with an interface that is configured
            to perform IP URPF checking using the routing table 
            for that VRF.
            
            .. attribute:: cipurpfvrfname  (key)
            
            	This field is used to specify the VRF Table name
            	**type**\: str
            
            	**length:** 0..32
            
            

            """

            _prefix = 'CISCO-IP-URPF-MIB'
            _revision = '2011-12-29'

            def __init__(self):
                super(CISCOIPURPFMIB.CipUrpfVrfTable.CipUrpfVrfEntry, self).__init__()

                self.yang_name = "cipUrpfVrfEntry"
                self.yang_parent_name = "cipUrpfVrfTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cipurpfvrfname']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cipurpfvrfname', (YLeaf(YType.str, 'cipUrpfVrfName'), ['str'])),
                ])
                self.cipurpfvrfname = None
                self._segment_path = lambda: "cipUrpfVrfEntry" + "[cipUrpfVrfName='" + str(self.cipurpfvrfname) + "']"
                self._absolute_path = lambda: "CISCO-IP-URPF-MIB:CISCO-IP-URPF-MIB/cipUrpfVrfTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPURPFMIB.CipUrpfVrfTable.CipUrpfVrfEntry, ['cipurpfvrfname'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOIPURPFMIB()
        return self._top_entity


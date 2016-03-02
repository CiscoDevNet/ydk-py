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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class UnicastRpfType_Enum(Enum):
    """
    UnicastRpfType_Enum

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

    """

    STRICT = 1

    LOOSE = 2

    DISABLED = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _CISCO_IP_URPF_MIB as meta
        return meta._meta_table['UnicastRpfType_Enum']


class UnicastRpfOptions_Bits(FixedBitsDict):
    """
    UnicastRpfOptions_Bits

    A bit string describing unicast Reverse Path Forwarding (RPF)
    options\:
    
    'allowDefault'
        Allows the use of the default route for RPF verification.
    
    'allowSelfPing'
        Allows a router to ping its own interface or interfaces.
    Keys are:- allowSelfPing , allowDefault

    """

    def __init__(self):
        self._dictionary = { 
            'allowSelfPing':False,
            'allowDefault':False,
        }
        self._pos_map = { 
            'allowSelfPing':1,
            'allowDefault':0,
        }


class CISCOIPURPFMIB(object):
    """
    
    
    .. attribute:: cipurpfifmontable
    
    	This table contains information on URPF dropping on an interface
    	**type**\: :py:class:`CipUrpfIfMonTable <ydk.models.ip.CISCO_IP_URPF_MIB.CISCOIPURPFMIB.CipUrpfIfMonTable>`
    
    .. attribute:: cipurpfscalar
    
    	
    	**type**\: :py:class:`CipUrpfScalar <ydk.models.ip.CISCO_IP_URPF_MIB.CISCOIPURPFMIB.CipUrpfScalar>`
    
    .. attribute:: cipurpftable
    
    	This table contains summary information for the managed device on URPF dropping
    	**type**\: :py:class:`CipUrpfTable <ydk.models.ip.CISCO_IP_URPF_MIB.CISCOIPURPFMIB.CipUrpfTable>`
    
    .. attribute:: cipurpfvrfiftable
    
    	This table contains statistics information for interfaces performing URPF using VRF table to determine reachability
    	**type**\: :py:class:`CipUrpfVrfIfTable <ydk.models.ip.CISCO_IP_URPF_MIB.CISCOIPURPFMIB.CipUrpfVrfIfTable>`
    
    .. attribute:: cipurpfvrftable
    
    	This table enables indexing URPF drop statistics by Virtual Routing and Forwarding instances
    	**type**\: :py:class:`CipUrpfVrfTable <ydk.models.ip.CISCO_IP_URPF_MIB.CISCOIPURPFMIB.CipUrpfVrfTable>`
    
    

    """

    _prefix = 'cisco-ip'
    _revision = '2011-12-29'

    def __init__(self):
        self.cipurpfifmontable = CISCOIPURPFMIB.CipUrpfIfMonTable()
        self.cipurpfifmontable.parent = self
        self.cipurpfscalar = CISCOIPURPFMIB.CipUrpfScalar()
        self.cipurpfscalar.parent = self
        self.cipurpftable = CISCOIPURPFMIB.CipUrpfTable()
        self.cipurpftable.parent = self
        self.cipurpfvrfiftable = CISCOIPURPFMIB.CipUrpfVrfIfTable()
        self.cipurpfvrfiftable.parent = self
        self.cipurpfvrftable = CISCOIPURPFMIB.CipUrpfVrfTable()
        self.cipurpfvrftable.parent = self


    class CipUrpfIfMonTable(object):
        """
        This table contains information on URPF dropping on
        an interface.
        
        .. attribute:: cipurpfifmonentry
        
        	If IPv4 packet forwarding is configured on an interface, and is configured to perform URPF checking, a row appears in this table with indices [ifIndex][ipv4]. If IPv4 packet forwarding is deconfigured, or URPF checking is deconfigured, the row disappears.  If IPv6 packet forwarding is configured on an interface, and is configured to perform URPF checking, a row appears in the table with indices [ifIndex][ipv6].  If IPv6 packet forwarding is deconfigured, or URPF checking is deconfigured, the row disappears
        	**type**\: list of :py:class:`CipUrpfIfMonEntry <ydk.models.ip.CISCO_IP_URPF_MIB.CISCOIPURPFMIB.CipUrpfIfMonTable.CipUrpfIfMonEntry>`
        
        

        """

        _prefix = 'cisco-ip'
        _revision = '2011-12-29'

        def __init__(self):
            self.parent = None
            self.cipurpfifmonentry = YList()
            self.cipurpfifmonentry.parent = self
            self.cipurpfifmonentry.name = 'cipurpfifmonentry'


        class CipUrpfIfMonEntry(object):
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
            
            .. attribute:: cipurpfifipversion
            
            	Specifies the version of IP forwarding on an interface to which the table row URPF counts, rates, and  configuration apply
            	**type**\: :py:class:`CipUrpfIfIpVersion_Enum <ydk.models.ip.CISCO_IP_URPF_MIB.CISCOIPURPFMIB.CipUrpfIfMonTable.CipUrpfIfMonEntry.CipUrpfIfIpVersion_Enum>`
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipurpfifcheckstrict
            
            	Interface configuration indicating the strictness of the reachability check performed  on the interface. \- strict\: check that source addr is reachable via            the interface it came in on. \- loose \: check that source addr is reachable via            some interface on the device
            	**type**\: :py:class:`CipUrpfIfCheckStrict_Enum <ydk.models.ip.CISCO_IP_URPF_MIB.CISCOIPURPFMIB.CipUrpfIfMonTable.CipUrpfIfMonEntry.CipUrpfIfCheckStrict_Enum>`
            
            .. attribute:: cipurpfifdiscontinuitytime
            
            	The value of sysUpTime on the most recent occasion at which this interface's  counters suffered  a discontinuity. If no such discontinuities have occurred since the last re\-initialization of the local management subsystem, then this object contains a value of zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipurpfifdroprate
            
            	The rate of packet drops of IP version cipUrpfIfIpVersion packets due to URPF on the interface.   This object is the average rate of dropping over the most  recent interval of time. The rate is computed by dividing the number of packets dropped over an interval by the  interval time in seconds. Each time the drop rate is computed, and at system startup, a snapshot is taken of the latest value of cipUrpfIfDrops. Subtracting from this the snapshot of cipUrpfIfDrops at the start of the current interval of time gives the number of packets dropped. The drop rate is computed every cipUrpfComputeInterval seconds.  When drop rate is computed, if time since the creation of  a row in cipUrpfIfMonTable is less than  cipUrpfDropRateWindow, the value of cipUrpfIfDrops is  divided by the time since row was created.  After the row has been in existence for  cipUrpfDropRateWindow, when drop rate is computed, the  number of packet drops counted on the interface from  interval start time to the computation time is divided  by cipUrpfDropRateWindow.  Changes to cipUrpfDropRateWindow are not reflected in this object until the next computation time.  The rate from the  most recent computation is the value  fetched until the subsequent computation is performed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipurpfifdropratenotifyenable
            
            	This object specifies whether the system produces the cipUrpfIfDropRateNotify notification as a result of URPF  dropping of version cipUrpfIfIpVersion IP packets on this  interface. A false value prevents such notifications from  being generated by this system
            	**type**\: bool
            
            .. attribute:: cipurpfifdrops
            
            	The number of IP packets of version cipUrpfIfIpVersion failing the URPF check and dropped by the managed device on a particular interface.  Discontinuities in the value of this variable can occur  at re\-initialization of the management system, and at  other times as indicated by the values of  cipUrpfIfDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipurpfifnotifydrholddownreset
            
            	Setting this object to true causes the five\-minute hold\-down timer for emitting URPF drop rate  notifications for IP version cipUrpfIfIpVersion on  the interface to be short\-circuited.  If a notification  is due and would be emitted for the interface if the  five\-minutes elapsed, setting this object will cause  the notification to be sent.  This is a trigger, and doesn't hold information. It is set and an action is performed. Therefore a get for  this object always returns false
            	**type**\: bool
            
            .. attribute:: cipurpfifnotifydropratethreshold
            
            	When the calculated rate of URPF packet drops (cipUrpfIfDropRate) meets or exceeds the value  specified by this object, a cipUrpfIfDropRateNotify  notification is sent if cipUrpfIfDropRateNotifyEnable  is set to true, and no such notification for the IP version has been sent for this interface for the  hold\-down period.  Note that due to the calculation used for drop rate,  if there are less than n drop events in an n\-second period the notification will not be generated. To allow for the detection of a small number of drop events, the value 0 (zero) is used to indicate that if any drop events occur during the interval, a notification is generated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipurpfifsuppresseddrops
            
            	The number of IP packets of version cipUrpfIfIpVersion failing the URPF check but given a reprieve and not  dropped by the managed device. Depending on the  device configuration and capabilities, the following  cases may cause incrementing of the counter\:  \- if the managed device is configured to allow self\-pings    and the managed device pings itself. \- if the managed device is configured for loose URPF (if any   interface has a route to the source), and the strict   case fails while the loose case passes. \- DHCP Request packets (src 0.0.0.0 dst 255.255.255.255)    will pass after initially being marked for drop. \- RIP routing on unnumbered interfaces will pass after    initially being marked for drop. \- multicast packets will pass after initially being marked    for drop \- ACL's can be applied to permit packets after initially    being marked for drop.  Discontinuities in the value of this variable can occur  at re\-initialization of the management system, and at  other times as indicated by the values of  cipUrpfIfDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipurpfifvrfname
            
            	If the value of cipUrpfIfWhichRouteTableID is 'vrf', the name of the VRF Table. Otherwise a zero\-length string
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: cipurpfifwhichroutetableid
            
            	Interface configuration indicating the routing table consulted for the reachability check\: \- default\: the non\-private routing table for of the             managed system. \- vrf   \: a particular VPN routing table
            	**type**\: :py:class:`CipUrpfIfWhichRouteTableID_Enum <ydk.models.ip.CISCO_IP_URPF_MIB.CISCOIPURPFMIB.CipUrpfIfMonTable.CipUrpfIfMonEntry.CipUrpfIfWhichRouteTableID_Enum>`
            
            

            """

            _prefix = 'cisco-ip'
            _revision = '2011-12-29'

            def __init__(self):
                self.parent = None
                self.cipurpfifipversion = None
                self.ifindex = None
                self.cipurpfifcheckstrict = None
                self.cipurpfifdiscontinuitytime = None
                self.cipurpfifdroprate = None
                self.cipurpfifdropratenotifyenable = None
                self.cipurpfifdrops = None
                self.cipurpfifnotifydrholddownreset = None
                self.cipurpfifnotifydropratethreshold = None
                self.cipurpfifsuppresseddrops = None
                self.cipurpfifvrfname = None
                self.cipurpfifwhichroutetableid = None

            class CipUrpfIfCheckStrict_Enum(Enum):
                """
                CipUrpfIfCheckStrict_Enum

                Interface configuration indicating the strictness of
                the reachability check performed 
                on the interface.
                \- strict\: check that source addr is reachable via 
                          the interface it came in on.
                \- loose \: check that source addr is reachable via 
                          some interface on the device.

                """

                STRICT = 1

                LOOSE = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.ip._meta import _CISCO_IP_URPF_MIB as meta
                    return meta._meta_table['CISCOIPURPFMIB.CipUrpfIfMonTable.CipUrpfIfMonEntry.CipUrpfIfCheckStrict_Enum']


            class CipUrpfIfIpVersion_Enum(Enum):
                """
                CipUrpfIfIpVersion_Enum

                Specifies the version of IP forwarding on an interface
                to which the table row URPF counts, rates, and 
                configuration apply.

                """

                IPV4 = 1

                IPV6 = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.ip._meta import _CISCO_IP_URPF_MIB as meta
                    return meta._meta_table['CISCOIPURPFMIB.CipUrpfIfMonTable.CipUrpfIfMonEntry.CipUrpfIfIpVersion_Enum']


            class CipUrpfIfWhichRouteTableID_Enum(Enum):
                """
                CipUrpfIfWhichRouteTableID_Enum

                Interface configuration indicating the routing table
                consulted for the reachability check\:
                \- default\: the non\-private routing table for of the 
                           managed system.
                \- vrf   \: a particular VPN routing table.

                """

                DEFAULT = 1

                VRF = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.ip._meta import _CISCO_IP_URPF_MIB as meta
                    return meta._meta_table['CISCOIPURPFMIB.CipUrpfIfMonTable.CipUrpfIfMonEntry.CipUrpfIfWhichRouteTableID_Enum']


            @property
            def _common_path(self):
                if self.cipurpfifipversion is None:
                    raise YPYDataValidationError('Key property cipurpfifipversion is None')
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-IP-URPF-MIB:CISCO-IP-URPF-MIB/CISCO-IP-URPF-MIB:cipUrpfIfMonTable/CISCO-IP-URPF-MIB:cipUrpfIfMonEntry[CISCO-IP-URPF-MIB:cipUrpfIfIpVersion = ' + str(self.cipurpfifipversion) + '][CISCO-IP-URPF-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cipurpfifipversion is not None:
                    return True

                if self.ifindex is not None:
                    return True

                if self.cipurpfifcheckstrict is not None:
                    return True

                if self.cipurpfifdiscontinuitytime is not None:
                    return True

                if self.cipurpfifdroprate is not None:
                    return True

                if self.cipurpfifdropratenotifyenable is not None:
                    return True

                if self.cipurpfifdrops is not None:
                    return True

                if self.cipurpfifnotifydrholddownreset is not None:
                    return True

                if self.cipurpfifnotifydropratethreshold is not None:
                    return True

                if self.cipurpfifsuppresseddrops is not None:
                    return True

                if self.cipurpfifvrfname is not None:
                    return True

                if self.cipurpfifwhichroutetableid is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ip._meta import _CISCO_IP_URPF_MIB as meta
                return meta._meta_table['CISCOIPURPFMIB.CipUrpfIfMonTable.CipUrpfIfMonEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IP-URPF-MIB:CISCO-IP-URPF-MIB/CISCO-IP-URPF-MIB:cipUrpfIfMonTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cipurpfifmonentry is not None:
                for child_ref in self.cipurpfifmonentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ip._meta import _CISCO_IP_URPF_MIB as meta
            return meta._meta_table['CISCOIPURPFMIB.CipUrpfIfMonTable']['meta_info']


    class CipUrpfScalar(object):
        """
        
        
        .. attribute:: cipurpfcomputeinterval
        
        	The time between rate computations. This global value applies for the computation of all URPF rates, global and per\-interface.  When the value of cipUrpfComputeInterval is changed, the interval in\-progress proceeds as though the value had not changed. The change will apply to the length of subsequent intervals.  The cipUrpfComputeInterval must be less than or equal  to the cipUrpfDropRateWindow
        	**type**\: int
        
        	**range:** 1..120
        
        .. attribute:: cipurpfdropnotifyholddowntime
        
        	The minimum time between issuance of cipUrpfIfDropRateNotify notifications for a  particular interface and packet forwarding type.  Notifications are generated for each interface and packet forwarding type that exceeds the drop\-rate.  When a Notify is sent because the drop\-rate is  exceeded for a particular interface and forwarding type, the time specified by this object is used to  specify the minimum time that must elapse before  another Notify can be sent for that interface and forwarding type. The time is specified globally but  used individually
        	**type**\: int
        
        	**range:** 1..1000
        
        .. attribute:: cipurpfdropratewindow
        
        	The window of time in the recent past over which the drop count used in the drop rate computation is collected.  This global value applies for the computation of all URPF  rates, global and per\-interface.   Once the period over which computations have been  performed exceeds cipUrpfDropRateWindow, every time a  computation is performed, the window slides up to end  at the current time and start at cipUrpfDropRateWindow  seconds before.   The cipUrpfDropRateWindow must be greater than or equal to the interval between computations  (cipUrpfComputeInterval).  Since the agent must save the drop count values for each compute interval in order to slide the window, the number of counts saved is the quotient of cipUrpfDropRateWindow divided by cipUrpfComputeInterval
        	**type**\: int
        
        	**range:** 1..600
        
        

        """

        _prefix = 'cisco-ip'
        _revision = '2011-12-29'

        def __init__(self):
            self.parent = None
            self.cipurpfcomputeinterval = None
            self.cipurpfdropnotifyholddowntime = None
            self.cipurpfdropratewindow = None

        @property
        def _common_path(self):

            return '/CISCO-IP-URPF-MIB:CISCO-IP-URPF-MIB/CISCO-IP-URPF-MIB:cipUrpfScalar'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cipurpfcomputeinterval is not None:
                return True

            if self.cipurpfdropnotifyholddowntime is not None:
                return True

            if self.cipurpfdropratewindow is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ip._meta import _CISCO_IP_URPF_MIB as meta
            return meta._meta_table['CISCOIPURPFMIB.CipUrpfScalar']['meta_info']


    class CipUrpfTable(object):
        """
        This table contains summary information for the
        managed device on URPF dropping.
        
        .. attribute:: cipurpfentry
        
        	If the managed device supports URPF dropping, a row exists for each IP version type (v4 and v6). A row contains summary information on URPF dropping over the entire managed device
        	**type**\: list of :py:class:`CipUrpfEntry <ydk.models.ip.CISCO_IP_URPF_MIB.CISCOIPURPFMIB.CipUrpfTable.CipUrpfEntry>`
        
        

        """

        _prefix = 'cisco-ip'
        _revision = '2011-12-29'

        def __init__(self):
            self.parent = None
            self.cipurpfentry = YList()
            self.cipurpfentry.parent = self
            self.cipurpfentry.name = 'cipurpfentry'


        class CipUrpfEntry(object):
            """
            If the managed device supports URPF dropping,
            a row exists for each IP version type (v4 and v6).
            A row contains summary information on URPF
            dropping over the entire managed device.
            
            .. attribute:: cipurpfipversion
            
            	Specifies the version of IP forwarding on an interface to which the table row URPF counts, rates, and configuration apply
            	**type**\: :py:class:`CipUrpfIpVersion_Enum <ydk.models.ip.CISCO_IP_URPF_MIB.CISCOIPURPFMIB.CipUrpfTable.CipUrpfEntry.CipUrpfIpVersion_Enum>`
            
            .. attribute:: cipurpfdroprate
            
            	The rate of packet drops of IP version cipUrpfIpVersion packets due to URPF for the managed device. The per\-interface drop rate notification is issued on rates exceeding a limit (rising rate). This dropping may indicate an security attack on the network. To determine whether the attack/event is over, the NMS must consult the managed device. This object can be polled to determine the recent drop rate for the managed device as a whole, in addition to querying particular interface objects.  This object is the average rate of dropping over the most recent window of time. The rate is computed by dividing the number of packets dropped over a window by the window time in seconds. The window time is specified by cipUrpfDropRateWindow. Each time the drop rate is computed, and at system startup, a snapshot is taken of the latest value of cipUrpfDrops. Subtracting from this the snapshot of cipUrpfDrops at the start of the current window of time gives the number of packets dropped. The drop rate is computed every cipUrpfComputeInterval seconds. As an example, let cipUrpfDropRateWindow be 300 seconds, and cipUrpfComputeInterval 30 seconds. Every 30 seconds, the drop count five minutes previous is subtracted from the current drop count, and the result is divided by 300 to arrive at the drop rate.  At device start\-up, until the device has been up more than cipUrpfDropRateWindow, when drop rate is computed, the value of cipUrpfDrops is divided by the time the device has been up.  After the device has been up for cipUrpfDropRateWindow, when drop rate is computed, the number of packet drops counted from interval start time to the computation time is divided by cipUrpfDropRateWindow.  Changes to cipUrpfDropRateWindow are not reflected in this object until the next computation time.  The rate from the most recent computation is the value fetched until the subsequent computation is performed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipurpfdrops
            
            	Sum of dropped IP version cipUrpfIpVersion packets failing a URPF check. This value is the sum of drops of packets  received on all interfaces of the managed device
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-ip'
            _revision = '2011-12-29'

            def __init__(self):
                self.parent = None
                self.cipurpfipversion = None
                self.cipurpfdroprate = None
                self.cipurpfdrops = None

            class CipUrpfIpVersion_Enum(Enum):
                """
                CipUrpfIpVersion_Enum

                Specifies the version of IP forwarding on an interface
                to which the table row URPF counts, rates, and
                configuration apply.

                """

                IPV4 = 1

                IPV6 = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.ip._meta import _CISCO_IP_URPF_MIB as meta
                    return meta._meta_table['CISCOIPURPFMIB.CipUrpfTable.CipUrpfEntry.CipUrpfIpVersion_Enum']


            @property
            def _common_path(self):
                if self.cipurpfipversion is None:
                    raise YPYDataValidationError('Key property cipurpfipversion is None')

                return '/CISCO-IP-URPF-MIB:CISCO-IP-URPF-MIB/CISCO-IP-URPF-MIB:cipUrpfTable/CISCO-IP-URPF-MIB:cipUrpfEntry[CISCO-IP-URPF-MIB:cipUrpfIpVersion = ' + str(self.cipurpfipversion) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cipurpfipversion is not None:
                    return True

                if self.cipurpfdroprate is not None:
                    return True

                if self.cipurpfdrops is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ip._meta import _CISCO_IP_URPF_MIB as meta
                return meta._meta_table['CISCOIPURPFMIB.CipUrpfTable.CipUrpfEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IP-URPF-MIB:CISCO-IP-URPF-MIB/CISCO-IP-URPF-MIB:cipUrpfTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cipurpfentry is not None:
                for child_ref in self.cipurpfentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ip._meta import _CISCO_IP_URPF_MIB as meta
            return meta._meta_table['CISCOIPURPFMIB.CipUrpfTable']['meta_info']


    class CipUrpfVrfIfTable(object):
        """
        This table contains statistics information for interfaces
        performing URPF using VRF table to determine reachability.
        
        .. attribute:: cipurpfvrfifentry
        
        	An entry exists for a VRF and interface if and only if the VRF associated with the interface is configured  to perform IP URPF checking using the routing  table for the VRF
        	**type**\: list of :py:class:`CipUrpfVrfIfEntry <ydk.models.ip.CISCO_IP_URPF_MIB.CISCOIPURPFMIB.CipUrpfVrfIfTable.CipUrpfVrfIfEntry>`
        
        

        """

        _prefix = 'cisco-ip'
        _revision = '2011-12-29'

        def __init__(self):
            self.parent = None
            self.cipurpfvrfifentry = YList()
            self.cipurpfvrfifentry.parent = self
            self.cipurpfvrfifentry.name = 'cipurpfvrfifentry'


        class CipUrpfVrfIfEntry(object):
            """
            An entry exists for a VRF and interface if and only
            if the VRF associated with the interface is configured 
            to perform IP URPF checking using the routing 
            table for the VRF.
            
            .. attribute:: cipurpfvrfname
            
            	
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipurpfvrfifdiscontinuitytime
            
            	The value of sysUpTime on the most recent occasion at which the URPF counters for this VRF on this interface  suffered  a discontinuity.  If no such discontinuities  have occurred since the last re\-initialization of the local management subsystem, then this object contains a  value of zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipurpfvrfifdrops
            
            	The number of packets failing the URPF check for a VRF on the interface and dropped by the managed device.  Discontinuities in the value of this variable can occur  at re\-initialization of the management system, and at  other times as indicated by the values of  cipUrpfVrfIfDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-ip'
            _revision = '2011-12-29'

            def __init__(self):
                self.parent = None
                self.cipurpfvrfname = None
                self.ifindex = None
                self.cipurpfvrfifdiscontinuitytime = None
                self.cipurpfvrfifdrops = None

            @property
            def _common_path(self):
                if self.cipurpfvrfname is None:
                    raise YPYDataValidationError('Key property cipurpfvrfname is None')
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-IP-URPF-MIB:CISCO-IP-URPF-MIB/CISCO-IP-URPF-MIB:cipUrpfVrfIfTable/CISCO-IP-URPF-MIB:cipUrpfVrfIfEntry[CISCO-IP-URPF-MIB:cipUrpfVrfName = ' + str(self.cipurpfvrfname) + '][CISCO-IP-URPF-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cipurpfvrfname is not None:
                    return True

                if self.ifindex is not None:
                    return True

                if self.cipurpfvrfifdiscontinuitytime is not None:
                    return True

                if self.cipurpfvrfifdrops is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ip._meta import _CISCO_IP_URPF_MIB as meta
                return meta._meta_table['CISCOIPURPFMIB.CipUrpfVrfIfTable.CipUrpfVrfIfEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IP-URPF-MIB:CISCO-IP-URPF-MIB/CISCO-IP-URPF-MIB:cipUrpfVrfIfTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cipurpfvrfifentry is not None:
                for child_ref in self.cipurpfvrfifentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ip._meta import _CISCO_IP_URPF_MIB as meta
            return meta._meta_table['CISCOIPURPFMIB.CipUrpfVrfIfTable']['meta_info']


    class CipUrpfVrfTable(object):
        """
        This table enables indexing URPF drop statistics
        by Virtual Routing and Forwarding instances.
        
        .. attribute:: cipurpfvrfentry
        
        	An entry exists for a VRF if and only if the VRF is associated with an interface that is configured to perform IP URPF checking using the routing table  for that VRF
        	**type**\: list of :py:class:`CipUrpfVrfEntry <ydk.models.ip.CISCO_IP_URPF_MIB.CISCOIPURPFMIB.CipUrpfVrfTable.CipUrpfVrfEntry>`
        
        

        """

        _prefix = 'cisco-ip'
        _revision = '2011-12-29'

        def __init__(self):
            self.parent = None
            self.cipurpfvrfentry = YList()
            self.cipurpfvrfentry.parent = self
            self.cipurpfvrfentry.name = 'cipurpfvrfentry'


        class CipUrpfVrfEntry(object):
            """
            An entry exists for a VRF if and only if the VRF
            is associated with an interface that is configured
            to perform IP URPF checking using the routing table 
            for that VRF.
            
            .. attribute:: cipurpfvrfname
            
            	This field is used to specify the VRF Table name
            	**type**\: str
            
            	**range:** 0..32
            
            

            """

            _prefix = 'cisco-ip'
            _revision = '2011-12-29'

            def __init__(self):
                self.parent = None
                self.cipurpfvrfname = None

            @property
            def _common_path(self):
                if self.cipurpfvrfname is None:
                    raise YPYDataValidationError('Key property cipurpfvrfname is None')

                return '/CISCO-IP-URPF-MIB:CISCO-IP-URPF-MIB/CISCO-IP-URPF-MIB:cipUrpfVrfTable/CISCO-IP-URPF-MIB:cipUrpfVrfEntry[CISCO-IP-URPF-MIB:cipUrpfVrfName = ' + str(self.cipurpfvrfname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cipurpfvrfname is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ip._meta import _CISCO_IP_URPF_MIB as meta
                return meta._meta_table['CISCOIPURPFMIB.CipUrpfVrfTable.CipUrpfVrfEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IP-URPF-MIB:CISCO-IP-URPF-MIB/CISCO-IP-URPF-MIB:cipUrpfVrfTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cipurpfvrfentry is not None:
                for child_ref in self.cipurpfvrfentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ip._meta import _CISCO_IP_URPF_MIB as meta
            return meta._meta_table['CISCOIPURPFMIB.CipUrpfVrfTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-IP-URPF-MIB:CISCO-IP-URPF-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.cipurpfifmontable is not None and self.cipurpfifmontable._has_data():
            return True

        if self.cipurpfifmontable is not None and self.cipurpfifmontable.is_presence():
            return True

        if self.cipurpfscalar is not None and self.cipurpfscalar._has_data():
            return True

        if self.cipurpfscalar is not None and self.cipurpfscalar.is_presence():
            return True

        if self.cipurpftable is not None and self.cipurpftable._has_data():
            return True

        if self.cipurpftable is not None and self.cipurpftable.is_presence():
            return True

        if self.cipurpfvrfiftable is not None and self.cipurpfvrfiftable._has_data():
            return True

        if self.cipurpfvrfiftable is not None and self.cipurpfvrfiftable.is_presence():
            return True

        if self.cipurpfvrftable is not None and self.cipurpfvrftable._has_data():
            return True

        if self.cipurpfvrftable is not None and self.cipurpfvrftable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _CISCO_IP_URPF_MIB as meta
        return meta._meta_table['CISCOIPURPFMIB']['meta_info']



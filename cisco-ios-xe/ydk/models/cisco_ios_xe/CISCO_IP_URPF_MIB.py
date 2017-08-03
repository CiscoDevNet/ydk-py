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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Unicastrpftype(Enum):
    """
    Unicastrpftype

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


class Unicastrpfoptions(Bits):
    """
    Unicastrpfoptions

    A bit string describing unicast Reverse Path Forwarding (RPF)
    options\:
    
    'allowDefault'
        Allows the use of the default route for RPF verification.
    
    'allowSelfPing'
        Allows a router to ping its own interface or interfaces.
    Keys are:- allowDefault , allowSelfPing

    """

    def __init__(self):
        super(Unicastrpfoptions, self).__init__()


class CiscoIpUrpfMib(Entity):
    """
    
    
    .. attribute:: cipurpfifmontable
    
    	This table contains information on URPF dropping on an interface
    	**type**\:   :py:class:`Cipurpfifmontable <ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB.CiscoIpUrpfMib.Cipurpfifmontable>`
    
    .. attribute:: cipurpfscalar
    
    	
    	**type**\:   :py:class:`Cipurpfscalar <ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB.CiscoIpUrpfMib.Cipurpfscalar>`
    
    .. attribute:: cipurpftable
    
    	This table contains summary information for the managed device on URPF dropping
    	**type**\:   :py:class:`Cipurpftable <ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB.CiscoIpUrpfMib.Cipurpftable>`
    
    .. attribute:: cipurpfvrfiftable
    
    	This table contains statistics information for interfaces performing URPF using VRF table to determine reachability
    	**type**\:   :py:class:`Cipurpfvrfiftable <ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB.CiscoIpUrpfMib.Cipurpfvrfiftable>`
    
    .. attribute:: cipurpfvrftable
    
    	This table enables indexing URPF drop statistics by Virtual Routing and Forwarding instances
    	**type**\:   :py:class:`Cipurpfvrftable <ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB.CiscoIpUrpfMib.Cipurpfvrftable>`
    
    

    """

    _prefix = 'CISCO-IP-URPF-MIB'
    _revision = '2011-12-29'

    def __init__(self):
        super(CiscoIpUrpfMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IP-URPF-MIB"
        self.yang_parent_name = "CISCO-IP-URPF-MIB"

        self.cipurpfifmontable = CiscoIpUrpfMib.Cipurpfifmontable()
        self.cipurpfifmontable.parent = self
        self._children_name_map["cipurpfifmontable"] = "cipUrpfIfMonTable"
        self._children_yang_names.add("cipUrpfIfMonTable")

        self.cipurpfscalar = CiscoIpUrpfMib.Cipurpfscalar()
        self.cipurpfscalar.parent = self
        self._children_name_map["cipurpfscalar"] = "cipUrpfScalar"
        self._children_yang_names.add("cipUrpfScalar")

        self.cipurpftable = CiscoIpUrpfMib.Cipurpftable()
        self.cipurpftable.parent = self
        self._children_name_map["cipurpftable"] = "cipUrpfTable"
        self._children_yang_names.add("cipUrpfTable")

        self.cipurpfvrfiftable = CiscoIpUrpfMib.Cipurpfvrfiftable()
        self.cipurpfvrfiftable.parent = self
        self._children_name_map["cipurpfvrfiftable"] = "cipUrpfVrfIfTable"
        self._children_yang_names.add("cipUrpfVrfIfTable")

        self.cipurpfvrftable = CiscoIpUrpfMib.Cipurpfvrftable()
        self.cipurpfvrftable.parent = self
        self._children_name_map["cipurpfvrftable"] = "cipUrpfVrfTable"
        self._children_yang_names.add("cipUrpfVrfTable")


    class Cipurpfscalar(Entity):
        """
        
        
        .. attribute:: cipurpfcomputeinterval
        
        	The time between rate computations. This global value applies for the computation of all URPF rates, global and per\-interface.  When the value of cipUrpfComputeInterval is changed, the interval in\-progress proceeds as though the value had not changed. The change will apply to the length of subsequent intervals.  The cipUrpfComputeInterval must be less than or equal  to the cipUrpfDropRateWindow
        	**type**\:  int
        
        	**range:** 1..120
        
        	**units**\: seconds
        
        .. attribute:: cipurpfdropnotifyholddowntime
        
        	The minimum time between issuance of cipUrpfIfDropRateNotify notifications for a  particular interface and packet forwarding type.  Notifications are generated for each interface and packet forwarding type that exceeds the drop\-rate.  When a Notify is sent because the drop\-rate is  exceeded for a particular interface and forwarding type, the time specified by this object is used to  specify the minimum time that must elapse before  another Notify can be sent for that interface and forwarding type. The time is specified globally but  used individually
        	**type**\:  int
        
        	**range:** 1..1000
        
        	**units**\: seconds
        
        .. attribute:: cipurpfdropratewindow
        
        	The window of time in the recent past over which the drop count used in the drop rate computation is collected.  This global value applies for the computation of all URPF  rates, global and per\-interface.   Once the period over which computations have been  performed exceeds cipUrpfDropRateWindow, every time a  computation is performed, the window slides up to end  at the current time and start at cipUrpfDropRateWindow  seconds before.   The cipUrpfDropRateWindow must be greater than or equal to the interval between computations  (cipUrpfComputeInterval).  Since the agent must save the drop count values for each compute interval in order to slide the window, the number of counts saved is the quotient of cipUrpfDropRateWindow divided by cipUrpfComputeInterval
        	**type**\:  int
        
        	**range:** 1..600
        
        	**units**\: seconds
        
        

        """

        _prefix = 'CISCO-IP-URPF-MIB'
        _revision = '2011-12-29'

        def __init__(self):
            super(CiscoIpUrpfMib.Cipurpfscalar, self).__init__()

            self.yang_name = "cipUrpfScalar"
            self.yang_parent_name = "CISCO-IP-URPF-MIB"

            self.cipurpfcomputeinterval = YLeaf(YType.int32, "cipUrpfComputeInterval")

            self.cipurpfdropnotifyholddowntime = YLeaf(YType.int32, "cipUrpfDropNotifyHoldDownTime")

            self.cipurpfdropratewindow = YLeaf(YType.int32, "cipUrpfDropRateWindow")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cipurpfcomputeinterval",
                            "cipurpfdropnotifyholddowntime",
                            "cipurpfdropratewindow") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoIpUrpfMib.Cipurpfscalar, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpUrpfMib.Cipurpfscalar, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.cipurpfcomputeinterval.is_set or
                self.cipurpfdropnotifyholddowntime.is_set or
                self.cipurpfdropratewindow.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cipurpfcomputeinterval.yfilter != YFilter.not_set or
                self.cipurpfdropnotifyholddowntime.yfilter != YFilter.not_set or
                self.cipurpfdropratewindow.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cipUrpfScalar" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IP-URPF-MIB:CISCO-IP-URPF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cipurpfcomputeinterval.is_set or self.cipurpfcomputeinterval.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipurpfcomputeinterval.get_name_leafdata())
            if (self.cipurpfdropnotifyholddowntime.is_set or self.cipurpfdropnotifyholddowntime.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipurpfdropnotifyholddowntime.get_name_leafdata())
            if (self.cipurpfdropratewindow.is_set or self.cipurpfdropratewindow.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipurpfdropratewindow.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cipUrpfComputeInterval" or name == "cipUrpfDropNotifyHoldDownTime" or name == "cipUrpfDropRateWindow"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cipUrpfComputeInterval"):
                self.cipurpfcomputeinterval = value
                self.cipurpfcomputeinterval.value_namespace = name_space
                self.cipurpfcomputeinterval.value_namespace_prefix = name_space_prefix
            if(value_path == "cipUrpfDropNotifyHoldDownTime"):
                self.cipurpfdropnotifyholddowntime = value
                self.cipurpfdropnotifyholddowntime.value_namespace = name_space
                self.cipurpfdropnotifyholddowntime.value_namespace_prefix = name_space_prefix
            if(value_path == "cipUrpfDropRateWindow"):
                self.cipurpfdropratewindow = value
                self.cipurpfdropratewindow.value_namespace = name_space
                self.cipurpfdropratewindow.value_namespace_prefix = name_space_prefix


    class Cipurpftable(Entity):
        """
        This table contains summary information for the
        managed device on URPF dropping.
        
        .. attribute:: cipurpfentry
        
        	If the managed device supports URPF dropping, a row exists for each IP version type (v4 and v6). A row contains summary information on URPF dropping over the entire managed device
        	**type**\: list of    :py:class:`Cipurpfentry <ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB.CiscoIpUrpfMib.Cipurpftable.Cipurpfentry>`
        
        

        """

        _prefix = 'CISCO-IP-URPF-MIB'
        _revision = '2011-12-29'

        def __init__(self):
            super(CiscoIpUrpfMib.Cipurpftable, self).__init__()

            self.yang_name = "cipUrpfTable"
            self.yang_parent_name = "CISCO-IP-URPF-MIB"

            self.cipurpfentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoIpUrpfMib.Cipurpftable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpUrpfMib.Cipurpftable, self).__setattr__(name, value)


        class Cipurpfentry(Entity):
            """
            If the managed device supports URPF dropping,
            a row exists for each IP version type (v4 and v6).
            A row contains summary information on URPF
            dropping over the entire managed device.
            
            .. attribute:: cipurpfipversion  <key>
            
            	Specifies the version of IP forwarding on an interface to which the table row URPF counts, rates, and configuration apply
            	**type**\:   :py:class:`Cipurpfipversion <ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB.CiscoIpUrpfMib.Cipurpftable.Cipurpfentry.Cipurpfipversion>`
            
            .. attribute:: cipurpfdroprate
            
            	The rate of packet drops of IP version cipUrpfIpVersion packets due to URPF for the managed device. The per\-interface drop rate notification is issued on rates exceeding a limit (rising rate). This dropping may indicate an security attack on the network. To determine whether the attack/event is over, the NMS must consult the managed device. This object can be polled to determine the recent drop rate for the managed device as a whole, in addition to querying particular interface objects.  This object is the average rate of dropping over the most recent window of time. The rate is computed by dividing the number of packets dropped over a window by the window time in seconds. The window time is specified by cipUrpfDropRateWindow. Each time the drop rate is computed, and at system startup, a snapshot is taken of the latest value of cipUrpfDrops. Subtracting from this the snapshot of cipUrpfDrops at the start of the current window of time gives the number of packets dropped. The drop rate is computed every cipUrpfComputeInterval seconds. As an example, let cipUrpfDropRateWindow be 300 seconds, and cipUrpfComputeInterval 30 seconds. Every 30 seconds, the drop count five minutes previous is subtracted from the current drop count, and the result is divided by 300 to arrive at the drop rate.  At device start\-up, until the device has been up more than cipUrpfDropRateWindow, when drop rate is computed, the value of cipUrpfDrops is divided by the time the device has been up.  After the device has been up for cipUrpfDropRateWindow, when drop rate is computed, the number of packet drops counted from interval start time to the computation time is divided by cipUrpfDropRateWindow.  Changes to cipUrpfDropRateWindow are not reflected in this object until the next computation time.  The rate from the most recent computation is the value fetched until the subsequent computation is performed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets per second
            
            .. attribute:: cipurpfdrops
            
            	Sum of dropped IP version cipUrpfIpVersion packets failing a URPF check. This value is the sum of drops of packets  received on all interfaces of the managed device
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            

            """

            _prefix = 'CISCO-IP-URPF-MIB'
            _revision = '2011-12-29'

            def __init__(self):
                super(CiscoIpUrpfMib.Cipurpftable.Cipurpfentry, self).__init__()

                self.yang_name = "cipUrpfEntry"
                self.yang_parent_name = "cipUrpfTable"

                self.cipurpfipversion = YLeaf(YType.enumeration, "cipUrpfIpVersion")

                self.cipurpfdroprate = YLeaf(YType.uint32, "cipUrpfDropRate")

                self.cipurpfdrops = YLeaf(YType.uint32, "cipUrpfDrops")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cipurpfipversion",
                                "cipurpfdroprate",
                                "cipurpfdrops") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIpUrpfMib.Cipurpftable.Cipurpfentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIpUrpfMib.Cipurpftable.Cipurpfentry, self).__setattr__(name, value)

            class Cipurpfipversion(Enum):
                """
                Cipurpfipversion

                Specifies the version of IP forwarding on an interface

                to which the table row URPF counts, rates, and

                configuration apply.

                .. data:: ipv4 = 1

                .. data:: ipv6 = 2

                """

                ipv4 = Enum.YLeaf(1, "ipv4")

                ipv6 = Enum.YLeaf(2, "ipv6")


            def has_data(self):
                return (
                    self.cipurpfipversion.is_set or
                    self.cipurpfdroprate.is_set or
                    self.cipurpfdrops.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cipurpfipversion.yfilter != YFilter.not_set or
                    self.cipurpfdroprate.yfilter != YFilter.not_set or
                    self.cipurpfdrops.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cipUrpfEntry" + "[cipUrpfIpVersion='" + self.cipurpfipversion.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IP-URPF-MIB:CISCO-IP-URPF-MIB/cipUrpfTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cipurpfipversion.is_set or self.cipurpfipversion.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipurpfipversion.get_name_leafdata())
                if (self.cipurpfdroprate.is_set or self.cipurpfdroprate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipurpfdroprate.get_name_leafdata())
                if (self.cipurpfdrops.is_set or self.cipurpfdrops.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipurpfdrops.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cipUrpfIpVersion" or name == "cipUrpfDropRate" or name == "cipUrpfDrops"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cipUrpfIpVersion"):
                    self.cipurpfipversion = value
                    self.cipurpfipversion.value_namespace = name_space
                    self.cipurpfipversion.value_namespace_prefix = name_space_prefix
                if(value_path == "cipUrpfDropRate"):
                    self.cipurpfdroprate = value
                    self.cipurpfdroprate.value_namespace = name_space
                    self.cipurpfdroprate.value_namespace_prefix = name_space_prefix
                if(value_path == "cipUrpfDrops"):
                    self.cipurpfdrops = value
                    self.cipurpfdrops.value_namespace = name_space
                    self.cipurpfdrops.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cipurpfentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cipurpfentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cipUrpfTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IP-URPF-MIB:CISCO-IP-URPF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cipUrpfEntry"):
                for c in self.cipurpfentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIpUrpfMib.Cipurpftable.Cipurpfentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cipurpfentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cipUrpfEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cipurpfifmontable(Entity):
        """
        This table contains information on URPF dropping on
        an interface.
        
        .. attribute:: cipurpfifmonentry
        
        	If IPv4 packet forwarding is configured on an interface, and is configured to perform URPF checking, a row appears in this table with indices [ifIndex][ipv4]. If IPv4 packet forwarding is deconfigured, or URPF checking is deconfigured, the row disappears.  If IPv6 packet forwarding is configured on an interface, and is configured to perform URPF checking, a row appears in the table with indices [ifIndex][ipv6].  If IPv6 packet forwarding is deconfigured, or URPF checking is deconfigured, the row disappears
        	**type**\: list of    :py:class:`Cipurpfifmonentry <ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB.CiscoIpUrpfMib.Cipurpfifmontable.Cipurpfifmonentry>`
        
        

        """

        _prefix = 'CISCO-IP-URPF-MIB'
        _revision = '2011-12-29'

        def __init__(self):
            super(CiscoIpUrpfMib.Cipurpfifmontable, self).__init__()

            self.yang_name = "cipUrpfIfMonTable"
            self.yang_parent_name = "CISCO-IP-URPF-MIB"

            self.cipurpfifmonentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoIpUrpfMib.Cipurpfifmontable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpUrpfMib.Cipurpfifmontable, self).__setattr__(name, value)


        class Cipurpfifmonentry(Entity):
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
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: cipurpfifipversion  <key>
            
            	Specifies the version of IP forwarding on an interface to which the table row URPF counts, rates, and  configuration apply
            	**type**\:   :py:class:`Cipurpfifipversion <ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB.CiscoIpUrpfMib.Cipurpfifmontable.Cipurpfifmonentry.Cipurpfifipversion>`
            
            .. attribute:: cipurpfifcheckstrict
            
            	Interface configuration indicating the strictness of the reachability check performed  on the interface. \- strict\: check that source addr is reachable via            the interface it came in on. \- loose \: check that source addr is reachable via            some interface on the device
            	**type**\:   :py:class:`Cipurpfifcheckstrict <ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB.CiscoIpUrpfMib.Cipurpfifmontable.Cipurpfifmonentry.Cipurpfifcheckstrict>`
            
            .. attribute:: cipurpfifdiscontinuitytime
            
            	The value of sysUpTime on the most recent occasion at which this interface's  counters suffered  a discontinuity. If no such discontinuities have occurred since the last re\-initialization of the local management subsystem, then this object contains a value of zero
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipurpfifdroprate
            
            	The rate of packet drops of IP version cipUrpfIfIpVersion packets due to URPF on the interface.   This object is the average rate of dropping over the most  recent interval of time. The rate is computed by dividing the number of packets dropped over an interval by the  interval time in seconds. Each time the drop rate is computed, and at system startup, a snapshot is taken of the latest value of cipUrpfIfDrops. Subtracting from this the snapshot of cipUrpfIfDrops at the start of the current interval of time gives the number of packets dropped. The drop rate is computed every cipUrpfComputeInterval seconds.  When drop rate is computed, if time since the creation of  a row in cipUrpfIfMonTable is less than  cipUrpfDropRateWindow, the value of cipUrpfIfDrops is  divided by the time since row was created.  After the row has been in existence for  cipUrpfDropRateWindow, when drop rate is computed, the  number of packet drops counted on the interface from  interval start time to the computation time is divided  by cipUrpfDropRateWindow.  Changes to cipUrpfDropRateWindow are not reflected in this object until the next computation time.  The rate from the  most recent computation is the value  fetched until the subsequent computation is performed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets/second
            
            .. attribute:: cipurpfifdropratenotifyenable
            
            	This object specifies whether the system produces the cipUrpfIfDropRateNotify notification as a result of URPF  dropping of version cipUrpfIfIpVersion IP packets on this  interface. A false value prevents such notifications from  being generated by this system
            	**type**\:  bool
            
            .. attribute:: cipurpfifdrops
            
            	The number of IP packets of version cipUrpfIfIpVersion failing the URPF check and dropped by the managed device on a particular interface.  Discontinuities in the value of this variable can occur  at re\-initialization of the management system, and at  other times as indicated by the values of  cipUrpfIfDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cipurpfifnotifydrholddownreset
            
            	Setting this object to true causes the five\-minute hold\-down timer for emitting URPF drop rate  notifications for IP version cipUrpfIfIpVersion on  the interface to be short\-circuited.  If a notification  is due and would be emitted for the interface if the  five\-minutes elapsed, setting this object will cause  the notification to be sent.  This is a trigger, and doesn't hold information. It is set and an action is performed. Therefore a get for  this object always returns false
            	**type**\:  bool
            
            .. attribute:: cipurpfifnotifydropratethreshold
            
            	When the calculated rate of URPF packet drops (cipUrpfIfDropRate) meets or exceeds the value  specified by this object, a cipUrpfIfDropRateNotify  notification is sent if cipUrpfIfDropRateNotifyEnable  is set to true, and no such notification for the IP version has been sent for this interface for the  hold\-down period.  Note that due to the calculation used for drop rate,  if there are less than n drop events in an n\-second period the notification will not be generated. To allow for the detection of a small number of drop events, the value 0 (zero) is used to indicate that if any drop events occur during the interval, a notification is generated
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets/second
            
            .. attribute:: cipurpfifsuppresseddrops
            
            	The number of IP packets of version cipUrpfIfIpVersion failing the URPF check but given a reprieve and not  dropped by the managed device. Depending on the  device configuration and capabilities, the following  cases may cause incrementing of the counter\:  \- if the managed device is configured to allow self\-pings    and the managed device pings itself. \- if the managed device is configured for loose URPF (if any   interface has a route to the source), and the strict   case fails while the loose case passes. \- DHCP Request packets (src 0.0.0.0 dst 255.255.255.255)    will pass after initially being marked for drop. \- RIP routing on unnumbered interfaces will pass after    initially being marked for drop. \- multicast packets will pass after initially being marked    for drop \- ACL's can be applied to permit packets after initially    being marked for drop.  Discontinuities in the value of this variable can occur  at re\-initialization of the management system, and at  other times as indicated by the values of  cipUrpfIfDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cipurpfifvrfname
            
            	If the value of cipUrpfIfWhichRouteTableID is 'vrf', the name of the VRF Table. Otherwise a zero\-length string
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: cipurpfifwhichroutetableid
            
            	Interface configuration indicating the routing table consulted for the reachability check\: \- default\: the non\-private routing table for of the             managed system. \- vrf   \: a particular VPN routing table
            	**type**\:   :py:class:`Cipurpfifwhichroutetableid <ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB.CiscoIpUrpfMib.Cipurpfifmontable.Cipurpfifmonentry.Cipurpfifwhichroutetableid>`
            
            

            """

            _prefix = 'CISCO-IP-URPF-MIB'
            _revision = '2011-12-29'

            def __init__(self):
                super(CiscoIpUrpfMib.Cipurpfifmontable.Cipurpfifmonentry, self).__init__()

                self.yang_name = "cipUrpfIfMonEntry"
                self.yang_parent_name = "cipUrpfIfMonTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.cipurpfifipversion = YLeaf(YType.enumeration, "cipUrpfIfIpVersion")

                self.cipurpfifcheckstrict = YLeaf(YType.enumeration, "cipUrpfIfCheckStrict")

                self.cipurpfifdiscontinuitytime = YLeaf(YType.uint32, "cipUrpfIfDiscontinuityTime")

                self.cipurpfifdroprate = YLeaf(YType.uint32, "cipUrpfIfDropRate")

                self.cipurpfifdropratenotifyenable = YLeaf(YType.boolean, "cipUrpfIfDropRateNotifyEnable")

                self.cipurpfifdrops = YLeaf(YType.uint32, "cipUrpfIfDrops")

                self.cipurpfifnotifydrholddownreset = YLeaf(YType.boolean, "cipUrpfIfNotifyDrHoldDownReset")

                self.cipurpfifnotifydropratethreshold = YLeaf(YType.uint32, "cipUrpfIfNotifyDropRateThreshold")

                self.cipurpfifsuppresseddrops = YLeaf(YType.uint32, "cipUrpfIfSuppressedDrops")

                self.cipurpfifvrfname = YLeaf(YType.str, "cipUrpfIfVrfName")

                self.cipurpfifwhichroutetableid = YLeaf(YType.enumeration, "cipUrpfIfWhichRouteTableID")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ifindex",
                                "cipurpfifipversion",
                                "cipurpfifcheckstrict",
                                "cipurpfifdiscontinuitytime",
                                "cipurpfifdroprate",
                                "cipurpfifdropratenotifyenable",
                                "cipurpfifdrops",
                                "cipurpfifnotifydrholddownreset",
                                "cipurpfifnotifydropratethreshold",
                                "cipurpfifsuppresseddrops",
                                "cipurpfifvrfname",
                                "cipurpfifwhichroutetableid") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIpUrpfMib.Cipurpfifmontable.Cipurpfifmonentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIpUrpfMib.Cipurpfifmontable.Cipurpfifmonentry, self).__setattr__(name, value)

            class Cipurpfifcheckstrict(Enum):
                """
                Cipurpfifcheckstrict

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


            class Cipurpfifipversion(Enum):
                """
                Cipurpfifipversion

                Specifies the version of IP forwarding on an interface

                to which the table row URPF counts, rates, and 

                configuration apply.

                .. data:: ipv4 = 1

                .. data:: ipv6 = 2

                """

                ipv4 = Enum.YLeaf(1, "ipv4")

                ipv6 = Enum.YLeaf(2, "ipv6")


            class Cipurpfifwhichroutetableid(Enum):
                """
                Cipurpfifwhichroutetableid

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


            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.cipurpfifipversion.is_set or
                    self.cipurpfifcheckstrict.is_set or
                    self.cipurpfifdiscontinuitytime.is_set or
                    self.cipurpfifdroprate.is_set or
                    self.cipurpfifdropratenotifyenable.is_set or
                    self.cipurpfifdrops.is_set or
                    self.cipurpfifnotifydrholddownreset.is_set or
                    self.cipurpfifnotifydropratethreshold.is_set or
                    self.cipurpfifsuppresseddrops.is_set or
                    self.cipurpfifvrfname.is_set or
                    self.cipurpfifwhichroutetableid.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.cipurpfifipversion.yfilter != YFilter.not_set or
                    self.cipurpfifcheckstrict.yfilter != YFilter.not_set or
                    self.cipurpfifdiscontinuitytime.yfilter != YFilter.not_set or
                    self.cipurpfifdroprate.yfilter != YFilter.not_set or
                    self.cipurpfifdropratenotifyenable.yfilter != YFilter.not_set or
                    self.cipurpfifdrops.yfilter != YFilter.not_set or
                    self.cipurpfifnotifydrholddownreset.yfilter != YFilter.not_set or
                    self.cipurpfifnotifydropratethreshold.yfilter != YFilter.not_set or
                    self.cipurpfifsuppresseddrops.yfilter != YFilter.not_set or
                    self.cipurpfifvrfname.yfilter != YFilter.not_set or
                    self.cipurpfifwhichroutetableid.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cipUrpfIfMonEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[cipUrpfIfIpVersion='" + self.cipurpfifipversion.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IP-URPF-MIB:CISCO-IP-URPF-MIB/cipUrpfIfMonTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.cipurpfifipversion.is_set or self.cipurpfifipversion.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipurpfifipversion.get_name_leafdata())
                if (self.cipurpfifcheckstrict.is_set or self.cipurpfifcheckstrict.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipurpfifcheckstrict.get_name_leafdata())
                if (self.cipurpfifdiscontinuitytime.is_set or self.cipurpfifdiscontinuitytime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipurpfifdiscontinuitytime.get_name_leafdata())
                if (self.cipurpfifdroprate.is_set or self.cipurpfifdroprate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipurpfifdroprate.get_name_leafdata())
                if (self.cipurpfifdropratenotifyenable.is_set or self.cipurpfifdropratenotifyenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipurpfifdropratenotifyenable.get_name_leafdata())
                if (self.cipurpfifdrops.is_set or self.cipurpfifdrops.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipurpfifdrops.get_name_leafdata())
                if (self.cipurpfifnotifydrholddownreset.is_set or self.cipurpfifnotifydrholddownreset.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipurpfifnotifydrholddownreset.get_name_leafdata())
                if (self.cipurpfifnotifydropratethreshold.is_set or self.cipurpfifnotifydropratethreshold.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipurpfifnotifydropratethreshold.get_name_leafdata())
                if (self.cipurpfifsuppresseddrops.is_set or self.cipurpfifsuppresseddrops.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipurpfifsuppresseddrops.get_name_leafdata())
                if (self.cipurpfifvrfname.is_set or self.cipurpfifvrfname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipurpfifvrfname.get_name_leafdata())
                if (self.cipurpfifwhichroutetableid.is_set or self.cipurpfifwhichroutetableid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipurpfifwhichroutetableid.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "cipUrpfIfIpVersion" or name == "cipUrpfIfCheckStrict" or name == "cipUrpfIfDiscontinuityTime" or name == "cipUrpfIfDropRate" or name == "cipUrpfIfDropRateNotifyEnable" or name == "cipUrpfIfDrops" or name == "cipUrpfIfNotifyDrHoldDownReset" or name == "cipUrpfIfNotifyDropRateThreshold" or name == "cipUrpfIfSuppressedDrops" or name == "cipUrpfIfVrfName" or name == "cipUrpfIfWhichRouteTableID"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cipUrpfIfIpVersion"):
                    self.cipurpfifipversion = value
                    self.cipurpfifipversion.value_namespace = name_space
                    self.cipurpfifipversion.value_namespace_prefix = name_space_prefix
                if(value_path == "cipUrpfIfCheckStrict"):
                    self.cipurpfifcheckstrict = value
                    self.cipurpfifcheckstrict.value_namespace = name_space
                    self.cipurpfifcheckstrict.value_namespace_prefix = name_space_prefix
                if(value_path == "cipUrpfIfDiscontinuityTime"):
                    self.cipurpfifdiscontinuitytime = value
                    self.cipurpfifdiscontinuitytime.value_namespace = name_space
                    self.cipurpfifdiscontinuitytime.value_namespace_prefix = name_space_prefix
                if(value_path == "cipUrpfIfDropRate"):
                    self.cipurpfifdroprate = value
                    self.cipurpfifdroprate.value_namespace = name_space
                    self.cipurpfifdroprate.value_namespace_prefix = name_space_prefix
                if(value_path == "cipUrpfIfDropRateNotifyEnable"):
                    self.cipurpfifdropratenotifyenable = value
                    self.cipurpfifdropratenotifyenable.value_namespace = name_space
                    self.cipurpfifdropratenotifyenable.value_namespace_prefix = name_space_prefix
                if(value_path == "cipUrpfIfDrops"):
                    self.cipurpfifdrops = value
                    self.cipurpfifdrops.value_namespace = name_space
                    self.cipurpfifdrops.value_namespace_prefix = name_space_prefix
                if(value_path == "cipUrpfIfNotifyDrHoldDownReset"):
                    self.cipurpfifnotifydrholddownreset = value
                    self.cipurpfifnotifydrholddownreset.value_namespace = name_space
                    self.cipurpfifnotifydrholddownreset.value_namespace_prefix = name_space_prefix
                if(value_path == "cipUrpfIfNotifyDropRateThreshold"):
                    self.cipurpfifnotifydropratethreshold = value
                    self.cipurpfifnotifydropratethreshold.value_namespace = name_space
                    self.cipurpfifnotifydropratethreshold.value_namespace_prefix = name_space_prefix
                if(value_path == "cipUrpfIfSuppressedDrops"):
                    self.cipurpfifsuppresseddrops = value
                    self.cipurpfifsuppresseddrops.value_namespace = name_space
                    self.cipurpfifsuppresseddrops.value_namespace_prefix = name_space_prefix
                if(value_path == "cipUrpfIfVrfName"):
                    self.cipurpfifvrfname = value
                    self.cipurpfifvrfname.value_namespace = name_space
                    self.cipurpfifvrfname.value_namespace_prefix = name_space_prefix
                if(value_path == "cipUrpfIfWhichRouteTableID"):
                    self.cipurpfifwhichroutetableid = value
                    self.cipurpfifwhichroutetableid.value_namespace = name_space
                    self.cipurpfifwhichroutetableid.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cipurpfifmonentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cipurpfifmonentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cipUrpfIfMonTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IP-URPF-MIB:CISCO-IP-URPF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cipUrpfIfMonEntry"):
                for c in self.cipurpfifmonentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIpUrpfMib.Cipurpfifmontable.Cipurpfifmonentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cipurpfifmonentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cipUrpfIfMonEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cipurpfvrfiftable(Entity):
        """
        This table contains statistics information for interfaces
        performing URPF using VRF table to determine reachability.
        
        .. attribute:: cipurpfvrfifentry
        
        	An entry exists for a VRF and interface if and only if the VRF associated with the interface is configured  to perform IP URPF checking using the routing  table for the VRF
        	**type**\: list of    :py:class:`Cipurpfvrfifentry <ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB.CiscoIpUrpfMib.Cipurpfvrfiftable.Cipurpfvrfifentry>`
        
        

        """

        _prefix = 'CISCO-IP-URPF-MIB'
        _revision = '2011-12-29'

        def __init__(self):
            super(CiscoIpUrpfMib.Cipurpfvrfiftable, self).__init__()

            self.yang_name = "cipUrpfVrfIfTable"
            self.yang_parent_name = "CISCO-IP-URPF-MIB"

            self.cipurpfvrfifentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoIpUrpfMib.Cipurpfvrfiftable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpUrpfMib.Cipurpfvrfiftable, self).__setattr__(name, value)


        class Cipurpfvrfifentry(Entity):
            """
            An entry exists for a VRF and interface if and only
            if the VRF associated with the interface is configured 
            to perform IP URPF checking using the routing 
            table for the VRF.
            
            .. attribute:: cipurpfvrfname  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..32
            
            	**refers to**\:  :py:class:`cipurpfvrfname <ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB.CiscoIpUrpfMib.Cipurpfvrftable.Cipurpfvrfentry>`
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: cipurpfvrfifdiscontinuitytime
            
            	The value of sysUpTime on the most recent occasion at which the URPF counters for this VRF on this interface  suffered  a discontinuity.  If no such discontinuities  have occurred since the last re\-initialization of the local management subsystem, then this object contains a  value of zero
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipurpfvrfifdrops
            
            	The number of packets failing the URPF check for a VRF on the interface and dropped by the managed device.  Discontinuities in the value of this variable can occur  at re\-initialization of the management system, and at  other times as indicated by the values of  cipUrpfVrfIfDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            

            """

            _prefix = 'CISCO-IP-URPF-MIB'
            _revision = '2011-12-29'

            def __init__(self):
                super(CiscoIpUrpfMib.Cipurpfvrfiftable.Cipurpfvrfifentry, self).__init__()

                self.yang_name = "cipUrpfVrfIfEntry"
                self.yang_parent_name = "cipUrpfVrfIfTable"

                self.cipurpfvrfname = YLeaf(YType.str, "cipUrpfVrfName")

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.cipurpfvrfifdiscontinuitytime = YLeaf(YType.uint32, "cipUrpfVrfIfDiscontinuityTime")

                self.cipurpfvrfifdrops = YLeaf(YType.uint32, "cipUrpfVrfIfDrops")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cipurpfvrfname",
                                "ifindex",
                                "cipurpfvrfifdiscontinuitytime",
                                "cipurpfvrfifdrops") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIpUrpfMib.Cipurpfvrfiftable.Cipurpfvrfifentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIpUrpfMib.Cipurpfvrfiftable.Cipurpfvrfifentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cipurpfvrfname.is_set or
                    self.ifindex.is_set or
                    self.cipurpfvrfifdiscontinuitytime.is_set or
                    self.cipurpfvrfifdrops.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cipurpfvrfname.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.cipurpfvrfifdiscontinuitytime.yfilter != YFilter.not_set or
                    self.cipurpfvrfifdrops.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cipUrpfVrfIfEntry" + "[cipUrpfVrfName='" + self.cipurpfvrfname.get() + "']" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IP-URPF-MIB:CISCO-IP-URPF-MIB/cipUrpfVrfIfTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cipurpfvrfname.is_set or self.cipurpfvrfname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipurpfvrfname.get_name_leafdata())
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.cipurpfvrfifdiscontinuitytime.is_set or self.cipurpfvrfifdiscontinuitytime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipurpfvrfifdiscontinuitytime.get_name_leafdata())
                if (self.cipurpfvrfifdrops.is_set or self.cipurpfvrfifdrops.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipurpfvrfifdrops.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cipUrpfVrfName" or name == "ifIndex" or name == "cipUrpfVrfIfDiscontinuityTime" or name == "cipUrpfVrfIfDrops"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cipUrpfVrfName"):
                    self.cipurpfvrfname = value
                    self.cipurpfvrfname.value_namespace = name_space
                    self.cipurpfvrfname.value_namespace_prefix = name_space_prefix
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cipUrpfVrfIfDiscontinuityTime"):
                    self.cipurpfvrfifdiscontinuitytime = value
                    self.cipurpfvrfifdiscontinuitytime.value_namespace = name_space
                    self.cipurpfvrfifdiscontinuitytime.value_namespace_prefix = name_space_prefix
                if(value_path == "cipUrpfVrfIfDrops"):
                    self.cipurpfvrfifdrops = value
                    self.cipurpfvrfifdrops.value_namespace = name_space
                    self.cipurpfvrfifdrops.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cipurpfvrfifentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cipurpfvrfifentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cipUrpfVrfIfTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IP-URPF-MIB:CISCO-IP-URPF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cipUrpfVrfIfEntry"):
                for c in self.cipurpfvrfifentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIpUrpfMib.Cipurpfvrfiftable.Cipurpfvrfifentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cipurpfvrfifentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cipUrpfVrfIfEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cipurpfvrftable(Entity):
        """
        This table enables indexing URPF drop statistics
        by Virtual Routing and Forwarding instances.
        
        .. attribute:: cipurpfvrfentry
        
        	An entry exists for a VRF if and only if the VRF is associated with an interface that is configured to perform IP URPF checking using the routing table  for that VRF
        	**type**\: list of    :py:class:`Cipurpfvrfentry <ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB.CiscoIpUrpfMib.Cipurpfvrftable.Cipurpfvrfentry>`
        
        

        """

        _prefix = 'CISCO-IP-URPF-MIB'
        _revision = '2011-12-29'

        def __init__(self):
            super(CiscoIpUrpfMib.Cipurpfvrftable, self).__init__()

            self.yang_name = "cipUrpfVrfTable"
            self.yang_parent_name = "CISCO-IP-URPF-MIB"

            self.cipurpfvrfentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoIpUrpfMib.Cipurpfvrftable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpUrpfMib.Cipurpfvrftable, self).__setattr__(name, value)


        class Cipurpfvrfentry(Entity):
            """
            An entry exists for a VRF if and only if the VRF
            is associated with an interface that is configured
            to perform IP URPF checking using the routing table 
            for that VRF.
            
            .. attribute:: cipurpfvrfname  <key>
            
            	This field is used to specify the VRF Table name
            	**type**\:  str
            
            	**length:** 0..32
            
            

            """

            _prefix = 'CISCO-IP-URPF-MIB'
            _revision = '2011-12-29'

            def __init__(self):
                super(CiscoIpUrpfMib.Cipurpfvrftable.Cipurpfvrfentry, self).__init__()

                self.yang_name = "cipUrpfVrfEntry"
                self.yang_parent_name = "cipUrpfVrfTable"

                self.cipurpfvrfname = YLeaf(YType.str, "cipUrpfVrfName")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cipurpfvrfname") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIpUrpfMib.Cipurpfvrftable.Cipurpfvrfentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIpUrpfMib.Cipurpfvrftable.Cipurpfvrfentry, self).__setattr__(name, value)

            def has_data(self):
                return self.cipurpfvrfname.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cipurpfvrfname.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cipUrpfVrfEntry" + "[cipUrpfVrfName='" + self.cipurpfvrfname.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IP-URPF-MIB:CISCO-IP-URPF-MIB/cipUrpfVrfTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cipurpfvrfname.is_set or self.cipurpfvrfname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipurpfvrfname.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cipUrpfVrfName"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cipUrpfVrfName"):
                    self.cipurpfvrfname = value
                    self.cipurpfvrfname.value_namespace = name_space
                    self.cipurpfvrfname.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cipurpfvrfentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cipurpfvrfentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cipUrpfVrfTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IP-URPF-MIB:CISCO-IP-URPF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cipUrpfVrfEntry"):
                for c in self.cipurpfvrfentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIpUrpfMib.Cipurpfvrftable.Cipurpfvrfentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cipurpfvrfentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cipUrpfVrfEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.cipurpfifmontable is not None and self.cipurpfifmontable.has_data()) or
            (self.cipurpfscalar is not None and self.cipurpfscalar.has_data()) or
            (self.cipurpftable is not None and self.cipurpftable.has_data()) or
            (self.cipurpfvrfiftable is not None and self.cipurpfvrfiftable.has_data()) or
            (self.cipurpfvrftable is not None and self.cipurpfvrftable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cipurpfifmontable is not None and self.cipurpfifmontable.has_operation()) or
            (self.cipurpfscalar is not None and self.cipurpfscalar.has_operation()) or
            (self.cipurpftable is not None and self.cipurpftable.has_operation()) or
            (self.cipurpfvrfiftable is not None and self.cipurpfvrfiftable.has_operation()) or
            (self.cipurpfvrftable is not None and self.cipurpfvrftable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-IP-URPF-MIB:CISCO-IP-URPF-MIB" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "cipUrpfIfMonTable"):
            if (self.cipurpfifmontable is None):
                self.cipurpfifmontable = CiscoIpUrpfMib.Cipurpfifmontable()
                self.cipurpfifmontable.parent = self
                self._children_name_map["cipurpfifmontable"] = "cipUrpfIfMonTable"
            return self.cipurpfifmontable

        if (child_yang_name == "cipUrpfScalar"):
            if (self.cipurpfscalar is None):
                self.cipurpfscalar = CiscoIpUrpfMib.Cipurpfscalar()
                self.cipurpfscalar.parent = self
                self._children_name_map["cipurpfscalar"] = "cipUrpfScalar"
            return self.cipurpfscalar

        if (child_yang_name == "cipUrpfTable"):
            if (self.cipurpftable is None):
                self.cipurpftable = CiscoIpUrpfMib.Cipurpftable()
                self.cipurpftable.parent = self
                self._children_name_map["cipurpftable"] = "cipUrpfTable"
            return self.cipurpftable

        if (child_yang_name == "cipUrpfVrfIfTable"):
            if (self.cipurpfvrfiftable is None):
                self.cipurpfvrfiftable = CiscoIpUrpfMib.Cipurpfvrfiftable()
                self.cipurpfvrfiftable.parent = self
                self._children_name_map["cipurpfvrfiftable"] = "cipUrpfVrfIfTable"
            return self.cipurpfvrfiftable

        if (child_yang_name == "cipUrpfVrfTable"):
            if (self.cipurpfvrftable is None):
                self.cipurpfvrftable = CiscoIpUrpfMib.Cipurpfvrftable()
                self.cipurpfvrftable.parent = self
                self._children_name_map["cipurpfvrftable"] = "cipUrpfVrfTable"
            return self.cipurpfvrftable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cipUrpfIfMonTable" or name == "cipUrpfScalar" or name == "cipUrpfTable" or name == "cipUrpfVrfIfTable" or name == "cipUrpfVrfTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoIpUrpfMib()
        return self._top_entity


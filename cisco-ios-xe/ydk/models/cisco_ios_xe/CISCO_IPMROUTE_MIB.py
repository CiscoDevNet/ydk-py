""" CISCO_IPMROUTE_MIB 

The MIB module for management of IP Multicast routing,
but independent of the specific multicast routing protocol
in use.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoIpmrouteMib(Entity):
    """
    
    
    .. attribute:: ciscoipmroute
    
    	
    	**type**\:   :py:class:`Ciscoipmroute <ydk.models.cisco_ios_xe.CISCO_IPMROUTE_MIB.CiscoIpmrouteMib.Ciscoipmroute>`
    
    .. attribute:: ciscoipmrouteheartbeattable
    
    	The (conceptual) table listing sets of IP Multicast heartbeat parameters.  If no IP Multicast heartbeat is configured, this table would be empty
    	**type**\:   :py:class:`Ciscoipmrouteheartbeattable <ydk.models.cisco_ios_xe.CISCO_IPMROUTE_MIB.CiscoIpmrouteMib.Ciscoipmrouteheartbeattable>`
    
    

    """

    _prefix = 'CISCO-IPMROUTE-MIB'
    _revision = '2005-03-07'

    def __init__(self):
        super(CiscoIpmrouteMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IPMROUTE-MIB"
        self.yang_parent_name = "CISCO-IPMROUTE-MIB"

        self.ciscoipmroute = CiscoIpmrouteMib.Ciscoipmroute()
        self.ciscoipmroute.parent = self
        self._children_name_map["ciscoipmroute"] = "ciscoIpMRoute"
        self._children_yang_names.add("ciscoIpMRoute")

        self.ciscoipmrouteheartbeattable = CiscoIpmrouteMib.Ciscoipmrouteheartbeattable()
        self.ciscoipmrouteheartbeattable.parent = self
        self._children_name_map["ciscoipmrouteheartbeattable"] = "ciscoIpMRouteHeartBeatTable"
        self._children_yang_names.add("ciscoIpMRouteHeartBeatTable")


    class Ciscoipmroute(Entity):
        """
        
        
        .. attribute:: ciscoipmroutenumberofentries
        
        	Maintains a count of the number of entries in the ipMRouteTable
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-IPMROUTE-MIB'
        _revision = '2005-03-07'

        def __init__(self):
            super(CiscoIpmrouteMib.Ciscoipmroute, self).__init__()

            self.yang_name = "ciscoIpMRoute"
            self.yang_parent_name = "CISCO-IPMROUTE-MIB"

            self.ciscoipmroutenumberofentries = YLeaf(YType.uint32, "ciscoIpMRouteNumberOfEntries")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("ciscoipmroutenumberofentries") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoIpmrouteMib.Ciscoipmroute, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpmrouteMib.Ciscoipmroute, self).__setattr__(name, value)

        def has_data(self):
            return self.ciscoipmroutenumberofentries.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.ciscoipmroutenumberofentries.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ciscoIpMRoute" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IPMROUTE-MIB:CISCO-IPMROUTE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.ciscoipmroutenumberofentries.is_set or self.ciscoipmroutenumberofentries.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ciscoipmroutenumberofentries.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ciscoIpMRouteNumberOfEntries"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "ciscoIpMRouteNumberOfEntries"):
                self.ciscoipmroutenumberofentries = value
                self.ciscoipmroutenumberofentries.value_namespace = name_space
                self.ciscoipmroutenumberofentries.value_namespace_prefix = name_space_prefix


    class Ciscoipmrouteheartbeattable(Entity):
        """
        The (conceptual) table listing sets of IP Multicast
        heartbeat parameters.  If no IP Multicast heartbeat is
        configured, this table would be empty.
        
        .. attribute:: ciscoipmrouteheartbeatentry
        
        	An entry (conceptual row) representing a set of IP Multicast heartbeat parameters
        	**type**\: list of    :py:class:`Ciscoipmrouteheartbeatentry <ydk.models.cisco_ios_xe.CISCO_IPMROUTE_MIB.CiscoIpmrouteMib.Ciscoipmrouteheartbeattable.Ciscoipmrouteheartbeatentry>`
        
        

        """

        _prefix = 'CISCO-IPMROUTE-MIB'
        _revision = '2005-03-07'

        def __init__(self):
            super(CiscoIpmrouteMib.Ciscoipmrouteheartbeattable, self).__init__()

            self.yang_name = "ciscoIpMRouteHeartBeatTable"
            self.yang_parent_name = "CISCO-IPMROUTE-MIB"

            self.ciscoipmrouteheartbeatentry = YList(self)

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
                        super(CiscoIpmrouteMib.Ciscoipmrouteheartbeattable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpmrouteMib.Ciscoipmrouteheartbeattable, self).__setattr__(name, value)


        class Ciscoipmrouteheartbeatentry(Entity):
            """
            An entry (conceptual row) representing a set of IP
            Multicast heartbeat parameters.
            
            .. attribute:: ciscoipmrouteheartbeatgroupaddr  <key>
            
            	Multicast group address used to receive heartbeat packets
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ciscoipmrouteheartbeatalerttime
            
            	The value of sysUpTime on the most recent occasion at which a missing IP multicast heartbeat condition occured for the group address specified in this entry.  If no such condition have occurred since the last re\-initialization of the local management subsystem, then this object contains a zero value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscoipmrouteheartbeatcount
            
            	Number of time intervals where multicast packets were received in the last ciscoIpMRouteHeartBeatWindowSize intervals
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscoipmrouteheartbeatinterval
            
            	Number of seconds in which a Cisco multicast router expects a valid heartBeat packet from a source.  This value must be a multiple of 10
            	**type**\:  int
            
            	**range:** 10..3600
            
            	**units**\: seconds
            
            .. attribute:: ciscoipmrouteheartbeatminimum
            
            	The minimal number of heartbeat packets expected in the last ciscoIpMRouteHeartBeatWindowSize intervals. If ciscoIpMRouteHeartBeatCount falls below this value, an SNMP trap/notification, if configured, will be sent to the NMS
            	**type**\:  int
            
            	**range:** 1..100
            
            .. attribute:: ciscoipmrouteheartbeatsourceaddr
            
            	Source address of the last multicast heartbeat packet received
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ciscoipmrouteheartbeatstatus
            
            	This object is used to create a new row or delete an existing row in this table
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: ciscoipmrouteheartbeatwindowsize
            
            	Number of ciscoIpMRouteHeartBeatInterval intervals a Cisco multicast router waits before checking if expected number of heartbeat packets are received or not
            	**type**\:  int
            
            	**range:** 1..100
            
            

            """

            _prefix = 'CISCO-IPMROUTE-MIB'
            _revision = '2005-03-07'

            def __init__(self):
                super(CiscoIpmrouteMib.Ciscoipmrouteheartbeattable.Ciscoipmrouteheartbeatentry, self).__init__()

                self.yang_name = "ciscoIpMRouteHeartBeatEntry"
                self.yang_parent_name = "ciscoIpMRouteHeartBeatTable"

                self.ciscoipmrouteheartbeatgroupaddr = YLeaf(YType.str, "ciscoIpMRouteHeartBeatGroupAddr")

                self.ciscoipmrouteheartbeatalerttime = YLeaf(YType.uint32, "ciscoIpMRouteHeartBeatAlertTime")

                self.ciscoipmrouteheartbeatcount = YLeaf(YType.uint32, "ciscoIpMRouteHeartBeatCount")

                self.ciscoipmrouteheartbeatinterval = YLeaf(YType.int32, "ciscoIpMRouteHeartBeatInterval")

                self.ciscoipmrouteheartbeatminimum = YLeaf(YType.int32, "ciscoIpMRouteHeartBeatMinimum")

                self.ciscoipmrouteheartbeatsourceaddr = YLeaf(YType.str, "ciscoIpMRouteHeartBeatSourceAddr")

                self.ciscoipmrouteheartbeatstatus = YLeaf(YType.enumeration, "ciscoIpMRouteHeartBeatStatus")

                self.ciscoipmrouteheartbeatwindowsize = YLeaf(YType.int32, "ciscoIpMRouteHeartBeatWindowSize")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ciscoipmrouteheartbeatgroupaddr",
                                "ciscoipmrouteheartbeatalerttime",
                                "ciscoipmrouteheartbeatcount",
                                "ciscoipmrouteheartbeatinterval",
                                "ciscoipmrouteheartbeatminimum",
                                "ciscoipmrouteheartbeatsourceaddr",
                                "ciscoipmrouteheartbeatstatus",
                                "ciscoipmrouteheartbeatwindowsize") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIpmrouteMib.Ciscoipmrouteheartbeattable.Ciscoipmrouteheartbeatentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIpmrouteMib.Ciscoipmrouteheartbeattable.Ciscoipmrouteheartbeatentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ciscoipmrouteheartbeatgroupaddr.is_set or
                    self.ciscoipmrouteheartbeatalerttime.is_set or
                    self.ciscoipmrouteheartbeatcount.is_set or
                    self.ciscoipmrouteheartbeatinterval.is_set or
                    self.ciscoipmrouteheartbeatminimum.is_set or
                    self.ciscoipmrouteheartbeatsourceaddr.is_set or
                    self.ciscoipmrouteheartbeatstatus.is_set or
                    self.ciscoipmrouteheartbeatwindowsize.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ciscoipmrouteheartbeatgroupaddr.yfilter != YFilter.not_set or
                    self.ciscoipmrouteheartbeatalerttime.yfilter != YFilter.not_set or
                    self.ciscoipmrouteheartbeatcount.yfilter != YFilter.not_set or
                    self.ciscoipmrouteheartbeatinterval.yfilter != YFilter.not_set or
                    self.ciscoipmrouteheartbeatminimum.yfilter != YFilter.not_set or
                    self.ciscoipmrouteheartbeatsourceaddr.yfilter != YFilter.not_set or
                    self.ciscoipmrouteheartbeatstatus.yfilter != YFilter.not_set or
                    self.ciscoipmrouteheartbeatwindowsize.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ciscoIpMRouteHeartBeatEntry" + "[ciscoIpMRouteHeartBeatGroupAddr='" + self.ciscoipmrouteheartbeatgroupaddr.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IPMROUTE-MIB:CISCO-IPMROUTE-MIB/ciscoIpMRouteHeartBeatTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ciscoipmrouteheartbeatgroupaddr.is_set or self.ciscoipmrouteheartbeatgroupaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoipmrouteheartbeatgroupaddr.get_name_leafdata())
                if (self.ciscoipmrouteheartbeatalerttime.is_set or self.ciscoipmrouteheartbeatalerttime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoipmrouteheartbeatalerttime.get_name_leafdata())
                if (self.ciscoipmrouteheartbeatcount.is_set or self.ciscoipmrouteheartbeatcount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoipmrouteheartbeatcount.get_name_leafdata())
                if (self.ciscoipmrouteheartbeatinterval.is_set or self.ciscoipmrouteheartbeatinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoipmrouteheartbeatinterval.get_name_leafdata())
                if (self.ciscoipmrouteheartbeatminimum.is_set or self.ciscoipmrouteheartbeatminimum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoipmrouteheartbeatminimum.get_name_leafdata())
                if (self.ciscoipmrouteheartbeatsourceaddr.is_set or self.ciscoipmrouteheartbeatsourceaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoipmrouteheartbeatsourceaddr.get_name_leafdata())
                if (self.ciscoipmrouteheartbeatstatus.is_set or self.ciscoipmrouteheartbeatstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoipmrouteheartbeatstatus.get_name_leafdata())
                if (self.ciscoipmrouteheartbeatwindowsize.is_set or self.ciscoipmrouteheartbeatwindowsize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoipmrouteheartbeatwindowsize.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ciscoIpMRouteHeartBeatGroupAddr" or name == "ciscoIpMRouteHeartBeatAlertTime" or name == "ciscoIpMRouteHeartBeatCount" or name == "ciscoIpMRouteHeartBeatInterval" or name == "ciscoIpMRouteHeartBeatMinimum" or name == "ciscoIpMRouteHeartBeatSourceAddr" or name == "ciscoIpMRouteHeartBeatStatus" or name == "ciscoIpMRouteHeartBeatWindowSize"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ciscoIpMRouteHeartBeatGroupAddr"):
                    self.ciscoipmrouteheartbeatgroupaddr = value
                    self.ciscoipmrouteheartbeatgroupaddr.value_namespace = name_space
                    self.ciscoipmrouteheartbeatgroupaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoIpMRouteHeartBeatAlertTime"):
                    self.ciscoipmrouteheartbeatalerttime = value
                    self.ciscoipmrouteheartbeatalerttime.value_namespace = name_space
                    self.ciscoipmrouteheartbeatalerttime.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoIpMRouteHeartBeatCount"):
                    self.ciscoipmrouteheartbeatcount = value
                    self.ciscoipmrouteheartbeatcount.value_namespace = name_space
                    self.ciscoipmrouteheartbeatcount.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoIpMRouteHeartBeatInterval"):
                    self.ciscoipmrouteheartbeatinterval = value
                    self.ciscoipmrouteheartbeatinterval.value_namespace = name_space
                    self.ciscoipmrouteheartbeatinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoIpMRouteHeartBeatMinimum"):
                    self.ciscoipmrouteheartbeatminimum = value
                    self.ciscoipmrouteheartbeatminimum.value_namespace = name_space
                    self.ciscoipmrouteheartbeatminimum.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoIpMRouteHeartBeatSourceAddr"):
                    self.ciscoipmrouteheartbeatsourceaddr = value
                    self.ciscoipmrouteheartbeatsourceaddr.value_namespace = name_space
                    self.ciscoipmrouteheartbeatsourceaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoIpMRouteHeartBeatStatus"):
                    self.ciscoipmrouteheartbeatstatus = value
                    self.ciscoipmrouteheartbeatstatus.value_namespace = name_space
                    self.ciscoipmrouteheartbeatstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoIpMRouteHeartBeatWindowSize"):
                    self.ciscoipmrouteheartbeatwindowsize = value
                    self.ciscoipmrouteheartbeatwindowsize.value_namespace = name_space
                    self.ciscoipmrouteheartbeatwindowsize.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ciscoipmrouteheartbeatentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ciscoipmrouteheartbeatentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ciscoIpMRouteHeartBeatTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IPMROUTE-MIB:CISCO-IPMROUTE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ciscoIpMRouteHeartBeatEntry"):
                for c in self.ciscoipmrouteheartbeatentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIpmrouteMib.Ciscoipmrouteheartbeattable.Ciscoipmrouteheartbeatentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ciscoipmrouteheartbeatentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ciscoIpMRouteHeartBeatEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.ciscoipmroute is not None and self.ciscoipmroute.has_data()) or
            (self.ciscoipmrouteheartbeattable is not None and self.ciscoipmrouteheartbeattable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.ciscoipmroute is not None and self.ciscoipmroute.has_operation()) or
            (self.ciscoipmrouteheartbeattable is not None and self.ciscoipmrouteheartbeattable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-IPMROUTE-MIB:CISCO-IPMROUTE-MIB" + path_buffer

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

        if (child_yang_name == "ciscoIpMRoute"):
            if (self.ciscoipmroute is None):
                self.ciscoipmroute = CiscoIpmrouteMib.Ciscoipmroute()
                self.ciscoipmroute.parent = self
                self._children_name_map["ciscoipmroute"] = "ciscoIpMRoute"
            return self.ciscoipmroute

        if (child_yang_name == "ciscoIpMRouteHeartBeatTable"):
            if (self.ciscoipmrouteheartbeattable is None):
                self.ciscoipmrouteheartbeattable = CiscoIpmrouteMib.Ciscoipmrouteheartbeattable()
                self.ciscoipmrouteheartbeattable.parent = self
                self._children_name_map["ciscoipmrouteheartbeattable"] = "ciscoIpMRouteHeartBeatTable"
            return self.ciscoipmrouteheartbeattable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "ciscoIpMRoute" or name == "ciscoIpMRouteHeartBeatTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoIpmrouteMib()
        return self._top_entity


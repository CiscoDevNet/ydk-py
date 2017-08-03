""" CISCO_CDP_MIB 

The MIB module for management of the Cisco Discovery
Protocol in Cisco devices.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoCdpMib(Entity):
    """
    
    
    .. attribute:: cdpcachetable
    
    	The (conceptual) table containing the cached information obtained via receiving CDP messages
    	**type**\:   :py:class:`Cdpcachetable <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CiscoCdpMib.Cdpcachetable>`
    
    .. attribute:: cdpctaddresstable
    
    	The (conceptual) table containing the list of  network\-layer addresses of a neighbor interface, as reported in the Address TLV of the most recently received CDP message. The first address included in the Address TLV is saved in cdpCacheAddress.  This table contains the remainder of the addresses in the Address TLV
    	**type**\:   :py:class:`Cdpctaddresstable <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CiscoCdpMib.Cdpctaddresstable>`
    
    .. attribute:: cdpglobal
    
    	
    	**type**\:   :py:class:`Cdpglobal <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CiscoCdpMib.Cdpglobal>`
    
    .. attribute:: cdpinterfaceexttable
    
    	This table contains the additional CDP configuration on the device's interfaces
    	**type**\:   :py:class:`Cdpinterfaceexttable <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CiscoCdpMib.Cdpinterfaceexttable>`
    
    .. attribute:: cdpinterfacetable
    
    	The (conceptual) table containing the status of CDP on the device's interfaces
    	**type**\:   :py:class:`Cdpinterfacetable <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CiscoCdpMib.Cdpinterfacetable>`
    
    

    """

    _prefix = 'CISCO-CDP-MIB'
    _revision = '2005-03-21'

    def __init__(self):
        super(CiscoCdpMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-CDP-MIB"
        self.yang_parent_name = "CISCO-CDP-MIB"

        self.cdpcachetable = CiscoCdpMib.Cdpcachetable()
        self.cdpcachetable.parent = self
        self._children_name_map["cdpcachetable"] = "cdpCacheTable"
        self._children_yang_names.add("cdpCacheTable")

        self.cdpctaddresstable = CiscoCdpMib.Cdpctaddresstable()
        self.cdpctaddresstable.parent = self
        self._children_name_map["cdpctaddresstable"] = "cdpCtAddressTable"
        self._children_yang_names.add("cdpCtAddressTable")

        self.cdpglobal = CiscoCdpMib.Cdpglobal()
        self.cdpglobal.parent = self
        self._children_name_map["cdpglobal"] = "cdpGlobal"
        self._children_yang_names.add("cdpGlobal")

        self.cdpinterfaceexttable = CiscoCdpMib.Cdpinterfaceexttable()
        self.cdpinterfaceexttable.parent = self
        self._children_name_map["cdpinterfaceexttable"] = "cdpInterfaceExtTable"
        self._children_yang_names.add("cdpInterfaceExtTable")

        self.cdpinterfacetable = CiscoCdpMib.Cdpinterfacetable()
        self.cdpinterfacetable.parent = self
        self._children_name_map["cdpinterfacetable"] = "cdpInterfaceTable"
        self._children_yang_names.add("cdpInterfaceTable")


    class Cdpglobal(Entity):
        """
        
        
        .. attribute:: cdpglobaldeviceid
        
        	The device ID advertised by this device. The format of this device id is characterized by the value of  cdpGlobalDeviceIdFormat object
        	**type**\:  str
        
        .. attribute:: cdpglobaldeviceidformat
        
        	An indication of the format of Device\-Id contained in the corresponding instance of cdpGlobalDeviceId. User can only specify the formats that the device is capable of as denoted in cdpGlobalDeviceIdFormatCpb object.  serialNumber(1) indicates that the value of cdpGlobalDeviceId  object is in the form of an ASCII string contain the device serial number.   macAddress(2) indicates that the value of cdpGlobalDeviceId  object is in the form of Layer 2 MAC address.  other(3) indicates that the value of cdpGlobalDeviceId object is in the form of a platform specific ASCII string contain info that identifies the device. For example\: ASCII string contains serialNumber appended/prepened with system name
        	**type**\:   :py:class:`Cdpglobaldeviceidformat <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CiscoCdpMib.Cdpglobal.Cdpglobaldeviceidformat>`
        
        .. attribute:: cdpglobaldeviceidformatcpb
        
        	Indicate the Device\-Id format capability of the device.  serialNumber(0) indicates that the device supports using serial number as the format for its DeviceId.  macAddress(1) indicates that the device supports using layer 2 MAC address as the format for its DeviceId.  other(2) indicates that the device supports using its platform specific format as the format for its DeviceId
        	**type**\:   :py:class:`Cdpglobaldeviceidformatcpb <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CiscoCdpMib.Cdpglobal.Cdpglobaldeviceidformatcpb>`
        
        .. attribute:: cdpglobalholdtime
        
        	The time for the receiving device holds CDP message. The default value is 180 seconds
        	**type**\:  int
        
        	**range:** 10..255
        
        	**units**\: seconds
        
        .. attribute:: cdpgloballastchange
        
        	Indicates the time when the cache table was last changed. It is the most recent time at which any row was last created, modified or deleted
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cdpglobalmessageinterval
        
        	The interval at which CDP messages are to be generated. The default value is 60 seconds
        	**type**\:  int
        
        	**range:** 5..254
        
        	**units**\: seconds
        
        .. attribute:: cdpglobalrun
        
        	An indication of whether the Cisco Discovery Protocol is currently running.  Entries in cdpCacheTable are deleted when CDP is disabled
        	**type**\:  bool
        
        

        """

        _prefix = 'CISCO-CDP-MIB'
        _revision = '2005-03-21'

        def __init__(self):
            super(CiscoCdpMib.Cdpglobal, self).__init__()

            self.yang_name = "cdpGlobal"
            self.yang_parent_name = "CISCO-CDP-MIB"

            self.cdpglobaldeviceid = YLeaf(YType.str, "cdpGlobalDeviceId")

            self.cdpglobaldeviceidformat = YLeaf(YType.enumeration, "cdpGlobalDeviceIdFormat")

            self.cdpglobaldeviceidformatcpb = YLeaf(YType.bits, "cdpGlobalDeviceIdFormatCpb")

            self.cdpglobalholdtime = YLeaf(YType.int32, "cdpGlobalHoldTime")

            self.cdpgloballastchange = YLeaf(YType.uint32, "cdpGlobalLastChange")

            self.cdpglobalmessageinterval = YLeaf(YType.int32, "cdpGlobalMessageInterval")

            self.cdpglobalrun = YLeaf(YType.boolean, "cdpGlobalRun")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cdpglobaldeviceid",
                            "cdpglobaldeviceidformat",
                            "cdpglobaldeviceidformatcpb",
                            "cdpglobalholdtime",
                            "cdpgloballastchange",
                            "cdpglobalmessageinterval",
                            "cdpglobalrun") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoCdpMib.Cdpglobal, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoCdpMib.Cdpglobal, self).__setattr__(name, value)

        class Cdpglobaldeviceidformat(Enum):
            """
            Cdpglobaldeviceidformat

            An indication of the format of Device\-Id contained in the

            corresponding instance of cdpGlobalDeviceId. User can only

            specify the formats that the device is capable of as

            denoted in cdpGlobalDeviceIdFormatCpb object.

            serialNumber(1) indicates that the value of cdpGlobalDeviceId 

            object is in the form of an ASCII string contain the device

            serial number. 

            macAddress(2) indicates that the value of cdpGlobalDeviceId 

            object is in the form of Layer 2 MAC address.

            other(3) indicates that the value of cdpGlobalDeviceId object

            is in the form of a platform specific ASCII string contain

            info that identifies the device. For example\: ASCII string

            contains serialNumber appended/prepened with system name.

            .. data:: serialNumber = 1

            .. data:: macAddress = 2

            .. data:: other = 3

            """

            serialNumber = Enum.YLeaf(1, "serialNumber")

            macAddress = Enum.YLeaf(2, "macAddress")

            other = Enum.YLeaf(3, "other")


        def has_data(self):
            return (
                self.cdpglobaldeviceid.is_set or
                self.cdpglobaldeviceidformat.is_set or
                self.cdpglobaldeviceidformatcpb.is_set or
                self.cdpglobalholdtime.is_set or
                self.cdpgloballastchange.is_set or
                self.cdpglobalmessageinterval.is_set or
                self.cdpglobalrun.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cdpglobaldeviceid.yfilter != YFilter.not_set or
                self.cdpglobaldeviceidformat.yfilter != YFilter.not_set or
                self.cdpglobaldeviceidformatcpb.yfilter != YFilter.not_set or
                self.cdpglobalholdtime.yfilter != YFilter.not_set or
                self.cdpgloballastchange.yfilter != YFilter.not_set or
                self.cdpglobalmessageinterval.yfilter != YFilter.not_set or
                self.cdpglobalrun.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cdpGlobal" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-CDP-MIB:CISCO-CDP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cdpglobaldeviceid.is_set or self.cdpglobaldeviceid.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cdpglobaldeviceid.get_name_leafdata())
            if (self.cdpglobaldeviceidformat.is_set or self.cdpglobaldeviceidformat.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cdpglobaldeviceidformat.get_name_leafdata())
            if (self.cdpglobaldeviceidformatcpb.is_set or self.cdpglobaldeviceidformatcpb.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cdpglobaldeviceidformatcpb.get_name_leafdata())
            if (self.cdpglobalholdtime.is_set or self.cdpglobalholdtime.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cdpglobalholdtime.get_name_leafdata())
            if (self.cdpgloballastchange.is_set or self.cdpgloballastchange.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cdpgloballastchange.get_name_leafdata())
            if (self.cdpglobalmessageinterval.is_set or self.cdpglobalmessageinterval.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cdpglobalmessageinterval.get_name_leafdata())
            if (self.cdpglobalrun.is_set or self.cdpglobalrun.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cdpglobalrun.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cdpGlobalDeviceId" or name == "cdpGlobalDeviceIdFormat" or name == "cdpGlobalDeviceIdFormatCpb" or name == "cdpGlobalHoldTime" or name == "cdpGlobalLastChange" or name == "cdpGlobalMessageInterval" or name == "cdpGlobalRun"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cdpGlobalDeviceId"):
                self.cdpglobaldeviceid = value
                self.cdpglobaldeviceid.value_namespace = name_space
                self.cdpglobaldeviceid.value_namespace_prefix = name_space_prefix
            if(value_path == "cdpGlobalDeviceIdFormat"):
                self.cdpglobaldeviceidformat = value
                self.cdpglobaldeviceidformat.value_namespace = name_space
                self.cdpglobaldeviceidformat.value_namespace_prefix = name_space_prefix
            if(value_path == "cdpGlobalDeviceIdFormatCpb"):
                self.cdpglobaldeviceidformatcpb[value] = True
            if(value_path == "cdpGlobalHoldTime"):
                self.cdpglobalholdtime = value
                self.cdpglobalholdtime.value_namespace = name_space
                self.cdpglobalholdtime.value_namespace_prefix = name_space_prefix
            if(value_path == "cdpGlobalLastChange"):
                self.cdpgloballastchange = value
                self.cdpgloballastchange.value_namespace = name_space
                self.cdpgloballastchange.value_namespace_prefix = name_space_prefix
            if(value_path == "cdpGlobalMessageInterval"):
                self.cdpglobalmessageinterval = value
                self.cdpglobalmessageinterval.value_namespace = name_space
                self.cdpglobalmessageinterval.value_namespace_prefix = name_space_prefix
            if(value_path == "cdpGlobalRun"):
                self.cdpglobalrun = value
                self.cdpglobalrun.value_namespace = name_space
                self.cdpglobalrun.value_namespace_prefix = name_space_prefix


    class Cdpinterfacetable(Entity):
        """
        The (conceptual) table containing the status of CDP on
        the device's interfaces.
        
        .. attribute:: cdpinterfaceentry
        
        	An entry (conceptual row) in the cdpInterfaceTable, containing the status of CDP on an interface
        	**type**\: list of    :py:class:`Cdpinterfaceentry <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CiscoCdpMib.Cdpinterfacetable.Cdpinterfaceentry>`
        
        

        """

        _prefix = 'CISCO-CDP-MIB'
        _revision = '2005-03-21'

        def __init__(self):
            super(CiscoCdpMib.Cdpinterfacetable, self).__init__()

            self.yang_name = "cdpInterfaceTable"
            self.yang_parent_name = "CISCO-CDP-MIB"

            self.cdpinterfaceentry = YList(self)

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
                        super(CiscoCdpMib.Cdpinterfacetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoCdpMib.Cdpinterfacetable, self).__setattr__(name, value)


        class Cdpinterfaceentry(Entity):
            """
            An entry (conceptual row) in the cdpInterfaceTable,
            containing the status of CDP on an interface.
            
            .. attribute:: cdpinterfaceifindex  <key>
            
            	The ifIndex value of the local interface.  For 802.3 Repeaters on which the repeater ports do not have ifIndex values assigned, this value is a unique value for the port, and greater than any ifIndex value supported by the repeater; in this case, the specific port is indicated by corresponding values of cdpInterfaceGroup and cdpInterfacePort, where these values correspond to the group number and port number values of RFC 1516
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cdpinterfaceenable
            
            	An indication of whether the Cisco Discovery Protocol is currently running on this interface.  This variable has no effect when CDP is disabled (cdpGlobalRun = FALSE)
            	**type**\:  bool
            
            .. attribute:: cdpinterfacegroup
            
            	This object is only relevant to interfaces which are repeater ports on 802.3 repeaters.  In this situation, it indicates the RFC1516 group number of the repeater port which corresponds to this interface
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cdpinterfacemessageinterval
            
            	The interval at which CDP messages are to be generated on this interface.  The default value is 60 seconds
            	**type**\:  int
            
            	**range:** 0..254
            
            	**units**\: seconds
            
            	**status**\: obsolete
            
            .. attribute:: cdpinterfacename
            
            	The name of the local interface as advertised by CDP in the Port\-ID TLV
            	**type**\:  str
            
            .. attribute:: cdpinterfaceport
            
            	This object is only relevant to interfaces which are repeater ports on 802.3 repeaters.  In this situation, it indicates the RFC1516 port number of the repeater port which corresponds to this interface
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'CISCO-CDP-MIB'
            _revision = '2005-03-21'

            def __init__(self):
                super(CiscoCdpMib.Cdpinterfacetable.Cdpinterfaceentry, self).__init__()

                self.yang_name = "cdpInterfaceEntry"
                self.yang_parent_name = "cdpInterfaceTable"

                self.cdpinterfaceifindex = YLeaf(YType.int32, "cdpInterfaceIfIndex")

                self.cdpinterfaceenable = YLeaf(YType.boolean, "cdpInterfaceEnable")

                self.cdpinterfacegroup = YLeaf(YType.int32, "cdpInterfaceGroup")

                self.cdpinterfacemessageinterval = YLeaf(YType.int32, "cdpInterfaceMessageInterval")

                self.cdpinterfacename = YLeaf(YType.str, "cdpInterfaceName")

                self.cdpinterfaceport = YLeaf(YType.int32, "cdpInterfacePort")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cdpinterfaceifindex",
                                "cdpinterfaceenable",
                                "cdpinterfacegroup",
                                "cdpinterfacemessageinterval",
                                "cdpinterfacename",
                                "cdpinterfaceport") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoCdpMib.Cdpinterfacetable.Cdpinterfaceentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoCdpMib.Cdpinterfacetable.Cdpinterfaceentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cdpinterfaceifindex.is_set or
                    self.cdpinterfaceenable.is_set or
                    self.cdpinterfacegroup.is_set or
                    self.cdpinterfacemessageinterval.is_set or
                    self.cdpinterfacename.is_set or
                    self.cdpinterfaceport.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cdpinterfaceifindex.yfilter != YFilter.not_set or
                    self.cdpinterfaceenable.yfilter != YFilter.not_set or
                    self.cdpinterfacegroup.yfilter != YFilter.not_set or
                    self.cdpinterfacemessageinterval.yfilter != YFilter.not_set or
                    self.cdpinterfacename.yfilter != YFilter.not_set or
                    self.cdpinterfaceport.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cdpInterfaceEntry" + "[cdpInterfaceIfIndex='" + self.cdpinterfaceifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-CDP-MIB:CISCO-CDP-MIB/cdpInterfaceTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cdpinterfaceifindex.is_set or self.cdpinterfaceifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdpinterfaceifindex.get_name_leafdata())
                if (self.cdpinterfaceenable.is_set or self.cdpinterfaceenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdpinterfaceenable.get_name_leafdata())
                if (self.cdpinterfacegroup.is_set or self.cdpinterfacegroup.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdpinterfacegroup.get_name_leafdata())
                if (self.cdpinterfacemessageinterval.is_set or self.cdpinterfacemessageinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdpinterfacemessageinterval.get_name_leafdata())
                if (self.cdpinterfacename.is_set or self.cdpinterfacename.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdpinterfacename.get_name_leafdata())
                if (self.cdpinterfaceport.is_set or self.cdpinterfaceport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdpinterfaceport.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cdpInterfaceIfIndex" or name == "cdpInterfaceEnable" or name == "cdpInterfaceGroup" or name == "cdpInterfaceMessageInterval" or name == "cdpInterfaceName" or name == "cdpInterfacePort"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cdpInterfaceIfIndex"):
                    self.cdpinterfaceifindex = value
                    self.cdpinterfaceifindex.value_namespace = name_space
                    self.cdpinterfaceifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cdpInterfaceEnable"):
                    self.cdpinterfaceenable = value
                    self.cdpinterfaceenable.value_namespace = name_space
                    self.cdpinterfaceenable.value_namespace_prefix = name_space_prefix
                if(value_path == "cdpInterfaceGroup"):
                    self.cdpinterfacegroup = value
                    self.cdpinterfacegroup.value_namespace = name_space
                    self.cdpinterfacegroup.value_namespace_prefix = name_space_prefix
                if(value_path == "cdpInterfaceMessageInterval"):
                    self.cdpinterfacemessageinterval = value
                    self.cdpinterfacemessageinterval.value_namespace = name_space
                    self.cdpinterfacemessageinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "cdpInterfaceName"):
                    self.cdpinterfacename = value
                    self.cdpinterfacename.value_namespace = name_space
                    self.cdpinterfacename.value_namespace_prefix = name_space_prefix
                if(value_path == "cdpInterfacePort"):
                    self.cdpinterfaceport = value
                    self.cdpinterfaceport.value_namespace = name_space
                    self.cdpinterfaceport.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cdpinterfaceentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cdpinterfaceentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cdpInterfaceTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-CDP-MIB:CISCO-CDP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cdpInterfaceEntry"):
                for c in self.cdpinterfaceentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoCdpMib.Cdpinterfacetable.Cdpinterfaceentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cdpinterfaceentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cdpInterfaceEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cdpinterfaceexttable(Entity):
        """
        This table contains the additional CDP configuration on
        the device's interfaces.
        
        .. attribute:: cdpinterfaceextentry
        
        	An entry in the cdpInterfaceExtTable contains the values configured for Extented Trust TLV and COS (Class of Service) for Untrusted Ports TLV on an interface which supports the sending of these TLVs
        	**type**\: list of    :py:class:`Cdpinterfaceextentry <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CiscoCdpMib.Cdpinterfaceexttable.Cdpinterfaceextentry>`
        
        

        """

        _prefix = 'CISCO-CDP-MIB'
        _revision = '2005-03-21'

        def __init__(self):
            super(CiscoCdpMib.Cdpinterfaceexttable, self).__init__()

            self.yang_name = "cdpInterfaceExtTable"
            self.yang_parent_name = "CISCO-CDP-MIB"

            self.cdpinterfaceextentry = YList(self)

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
                        super(CiscoCdpMib.Cdpinterfaceexttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoCdpMib.Cdpinterfaceexttable, self).__setattr__(name, value)


        class Cdpinterfaceextentry(Entity):
            """
            An entry in the cdpInterfaceExtTable contains the values
            configured for Extented Trust TLV and COS (Class of Service)
            for Untrusted Ports TLV on an interface which supports the
            sending of these TLVs.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: cdpinterfacecosforuntrustedport
            
            	Indicates the value to be sent by COS for Untrusted Ports TLV
            	**type**\:  int
            
            	**range:** 0..7
            
            .. attribute:: cdpinterfaceextendedtrust
            
            	Indicates the value to be sent by Extended Trust TLV.  If trusted(1) is configured, the value of Extended Trust TLV is one byte in length with its least significant bit equal to 1 to indicate extended trust. All other bits are 0.  If noTrust(2) is configured, the value of Extended Trust TLV is one byte in length with its least significant bit equal to 0 to indicate no extended trust. All other bits are 0
            	**type**\:   :py:class:`Cdpinterfaceextendedtrust <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CiscoCdpMib.Cdpinterfaceexttable.Cdpinterfaceextentry.Cdpinterfaceextendedtrust>`
            
            

            """

            _prefix = 'CISCO-CDP-MIB'
            _revision = '2005-03-21'

            def __init__(self):
                super(CiscoCdpMib.Cdpinterfaceexttable.Cdpinterfaceextentry, self).__init__()

                self.yang_name = "cdpInterfaceExtEntry"
                self.yang_parent_name = "cdpInterfaceExtTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.cdpinterfacecosforuntrustedport = YLeaf(YType.uint32, "cdpInterfaceCosForUntrustedPort")

                self.cdpinterfaceextendedtrust = YLeaf(YType.enumeration, "cdpInterfaceExtendedTrust")

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
                                "cdpinterfacecosforuntrustedport",
                                "cdpinterfaceextendedtrust") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoCdpMib.Cdpinterfaceexttable.Cdpinterfaceextentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoCdpMib.Cdpinterfaceexttable.Cdpinterfaceextentry, self).__setattr__(name, value)

            class Cdpinterfaceextendedtrust(Enum):
                """
                Cdpinterfaceextendedtrust

                Indicates the value to be sent by Extended Trust TLV.

                If trusted(1) is configured, the value of Extended Trust TLV

                is one byte in length with its least significant bit equal to

                1 to indicate extended trust. All other bits are 0.

                If noTrust(2) is configured, the value of Extended Trust TLV

                is one byte in length with its least significant bit equal to

                0 to indicate no extended trust. All other bits are 0.

                .. data:: trusted = 1

                .. data:: noTrust = 2

                """

                trusted = Enum.YLeaf(1, "trusted")

                noTrust = Enum.YLeaf(2, "noTrust")


            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.cdpinterfacecosforuntrustedport.is_set or
                    self.cdpinterfaceextendedtrust.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.cdpinterfacecosforuntrustedport.yfilter != YFilter.not_set or
                    self.cdpinterfaceextendedtrust.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cdpInterfaceExtEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-CDP-MIB:CISCO-CDP-MIB/cdpInterfaceExtTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.cdpinterfacecosforuntrustedport.is_set or self.cdpinterfacecosforuntrustedport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdpinterfacecosforuntrustedport.get_name_leafdata())
                if (self.cdpinterfaceextendedtrust.is_set or self.cdpinterfaceextendedtrust.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdpinterfaceextendedtrust.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "cdpInterfaceCosForUntrustedPort" or name == "cdpInterfaceExtendedTrust"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cdpInterfaceCosForUntrustedPort"):
                    self.cdpinterfacecosforuntrustedport = value
                    self.cdpinterfacecosforuntrustedport.value_namespace = name_space
                    self.cdpinterfacecosforuntrustedport.value_namespace_prefix = name_space_prefix
                if(value_path == "cdpInterfaceExtendedTrust"):
                    self.cdpinterfaceextendedtrust = value
                    self.cdpinterfaceextendedtrust.value_namespace = name_space
                    self.cdpinterfaceextendedtrust.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cdpinterfaceextentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cdpinterfaceextentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cdpInterfaceExtTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-CDP-MIB:CISCO-CDP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cdpInterfaceExtEntry"):
                for c in self.cdpinterfaceextentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoCdpMib.Cdpinterfaceexttable.Cdpinterfaceextentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cdpinterfaceextentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cdpInterfaceExtEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cdpcachetable(Entity):
        """
        The (conceptual) table containing the cached
        information obtained via receiving CDP messages.
        
        .. attribute:: cdpcacheentry
        
        	An entry (conceptual row) in the cdpCacheTable, containing the information received via CDP on one interface from one device.  Entries appear when a CDP advertisement is received from a neighbor device.  Entries disappear when CDP is disabled on the interface, or globally
        	**type**\: list of    :py:class:`Cdpcacheentry <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CiscoCdpMib.Cdpcachetable.Cdpcacheentry>`
        
        

        """

        _prefix = 'CISCO-CDP-MIB'
        _revision = '2005-03-21'

        def __init__(self):
            super(CiscoCdpMib.Cdpcachetable, self).__init__()

            self.yang_name = "cdpCacheTable"
            self.yang_parent_name = "CISCO-CDP-MIB"

            self.cdpcacheentry = YList(self)

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
                        super(CiscoCdpMib.Cdpcachetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoCdpMib.Cdpcachetable, self).__setattr__(name, value)


        class Cdpcacheentry(Entity):
            """
            An entry (conceptual row) in the cdpCacheTable,
            containing the information received via CDP on one
            interface from one device.  Entries appear when
            a CDP advertisement is received from a neighbor
            device.  Entries disappear when CDP is disabled
            on the interface, or globally.
            
            .. attribute:: cdpcacheifindex  <key>
            
            	Normally, the ifIndex value of the local interface. For 802.3 Repeaters for which the repeater ports do not have ifIndex values assigned, this value is a unique value for the port, and greater than any ifIndex value supported by the repeater; the specific port number in this case, is given by the corresponding value of cdpInterfacePort
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cdpcachedeviceindex  <key>
            
            	A unique value for each device from which CDP messages are being received
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cdpcacheaddress
            
            	The (first) network\-layer address of the device as reported in the Address TLV of the most recently received CDP message.  For example, if the corresponding instance of cacheAddressType had the value 'ip(1)', then this object  would be an IPv4\-address.  If the neighbor device is  SNMP\-manageable, it is supposed to generate its CDP messages such that this address is one at which it will receive SNMP messages. Use cdpCtAddressTable to extract the remaining addresses from the Address TLV received most recently
            	**type**\:  str
            
            .. attribute:: cdpcacheaddresstype
            
            	An indication of the type of address contained in the corresponding instance of cdpCacheAddress
            	**type**\:   :py:class:`Cisconetworkprotocol <ydk.models.cisco_ios_xe.CISCO_TC.Cisconetworkprotocol>`
            
            .. attribute:: cdpcacheapplianceid
            
            	The remote device's Appliance ID, as reported in the  most recent CDP message. This object is not instantiated if no Appliance VLAN\-ID field (TLV) was reported in the most recently received CDP message
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cdpcachecapabilities
            
            	The Device's Functional Capabilities as reported in the most recent CDP message.  For latest set of specific values, see the latest version of the CDP specification. The zero\-length string indicates no Capabilities field (TLV) was reported in the most recent CDP message
            	**type**\:  str
            
            	**length:** 0..4
            
            .. attribute:: cdpcachedeviceid
            
            	The Device\-ID string as reported in the most recent CDP message.  The zero\-length string indicates no Device\-ID field (TLV) was reported in the most recent CDP message
            	**type**\:  str
            
            .. attribute:: cdpcachedeviceport
            
            	The Port\-ID string as reported in the most recent CDP message.  This will typically be the value of the ifName object (e.g., 'Ethernet0').  The zero\-length string indicates no Port\-ID field (TLV) was reported in the most recent CDP message
            	**type**\:  str
            
            .. attribute:: cdpcacheduplex
            
            	The remote device's interface's duplex mode, as reported in the  most recent CDP message.  The value unknown(1) indicates no duplex mode field (TLV) was reported in the most recent CDP message
            	**type**\:   :py:class:`Cdpcacheduplex <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CiscoCdpMib.Cdpcachetable.Cdpcacheentry.Cdpcacheduplex>`
            
            .. attribute:: cdpcachelastchange
            
            	Indicates the time when this cache entry was last changed. This object is initialised to the current time when the entry gets created and updated to the current time whenever the value of any (other) object instance in the corresponding row is modified
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cdpcachemtu
            
            	Indicates the size of the largest datagram that can be sent/received by remote device, as reported in the most recent CDP message. This object is not instantiated if no MTU field (TLV) was reported in the most recently received CDP message
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cdpcachenativevlan
            
            	The remote device's interface's native VLAN, as reported in the  most recent CDP message.  The value 0 indicates no native VLAN field (TLV) was reported in the most recent CDP message
            	**type**\:  int
            
            	**range:** 0..4095
            
            .. attribute:: cdpcachephyslocation
            
            	Indicates the physical location, as reported by the most recent CDP message, of a connector which is on, or physically connected to, the remote device's interface over which the CDP packet is sent. This object is not instantiated if no Physical Location field (TLV) was reported by the most recently received CDP message
            	**type**\:  str
            
            .. attribute:: cdpcacheplatform
            
            	The Device's Hardware Platform as reported in the most recent CDP message.  The zero\-length string indicates that no Platform field (TLV) was reported in the most recent CDP message
            	**type**\:  str
            
            .. attribute:: cdpcachepowerconsumption
            
            	The amount of power consumed by remote device, as reported in the most recent CDP message. This object is not instantiated if no Power Consumption field (TLV) was reported in the most recently received CDP message
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliwatts
            
            .. attribute:: cdpcacheprimarymgmtaddr
            
            	This object indicates the (first) network layer address at which the device will accept SNMP messages as reported in the first address in the  Management\-Address TLV of the most recently received CDP message.  If the corresponding instance of  cdpCachePrimaryMgmtAddrType has the value 'ip(1)', then this object would be an IP\-address. If the  remote device is not currently manageable via any  network protocol, then it reports the special value  of the IPv4 address 0.0.0.0, and that address is  recorded in this object.  If the most recently received CDP message did not contain the Management\-Address TLV, then this object is not instanstiated
            	**type**\:  str
            
            .. attribute:: cdpcacheprimarymgmtaddrtype
            
            	An indication of the type of address contained in the corresponding instance of cdpCachePrimaryMgmtAddress
            	**type**\:   :py:class:`Cisconetworkprotocol <ydk.models.cisco_ios_xe.CISCO_TC.Cisconetworkprotocol>`
            
            .. attribute:: cdpcachesecondarymgmtaddr
            
            	This object indicates the alternate network layer address at which the device will accept SNMP messages as reported in the second address in the  Management\-Address TLV of the most recently received CDP message.  If the corresponding instance of cdpCacheSecondaryMgmtAddrType has the value 'ip(1)', then this object would be an IP\-address. If the  remote device reports the special value of the  IPv4 address 0.0.0.0, that address is recorded in  this object.  If the most recently received CDP message did not contain the Management\-Address TLV, or if that TLV contained only one address, then this object is not instanstiated
            	**type**\:  str
            
            .. attribute:: cdpcachesecondarymgmtaddrtype
            
            	An indication of the type of address contained in the corresponding instance of cdpCacheSecondaryMgmtAddress
            	**type**\:   :py:class:`Cisconetworkprotocol <ydk.models.cisco_ios_xe.CISCO_TC.Cisconetworkprotocol>`
            
            .. attribute:: cdpcachesysname
            
            	Indicates the value of the remote device's sysName MIB object. By convention, it is the device's fully qualified domain name. This object is not instantiated if no sysName field (TLV) was reported in the most recently received CDP message
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cdpcachesysobjectid
            
            	Indicates the value of the remote device's sysObjectID MIB object. This object is not instantiated if no sysObjectID field (TLV) was reported in the most recently received CDP message
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: cdpcacheversion
            
            	The Version string as reported in the most recent CDP message.  The zero\-length string indicates no Version field (TLV) was reported in the most recent CDP message
            	**type**\:  str
            
            .. attribute:: cdpcachevlanid
            
            	The remote device's VoIP VLAN ID, as reported in the  most recent CDP message. This object is not instantiated if no Appliance VLAN\-ID field (TLV) was reported in the most recently received CDP message
            	**type**\:  int
            
            	**range:** 0..4095
            
            .. attribute:: cdpcachevtpmgmtdomain
            
            	The VTP Management Domain for the remote device's interface,  as reported in the most recently received CDP message. This object is not instantiated if no VTP Management Domain field (TLV) was reported in the most recently received CDP message
            	**type**\:  str
            
            	**length:** 0..32
            
            

            """

            _prefix = 'CISCO-CDP-MIB'
            _revision = '2005-03-21'

            def __init__(self):
                super(CiscoCdpMib.Cdpcachetable.Cdpcacheentry, self).__init__()

                self.yang_name = "cdpCacheEntry"
                self.yang_parent_name = "cdpCacheTable"

                self.cdpcacheifindex = YLeaf(YType.int32, "cdpCacheIfIndex")

                self.cdpcachedeviceindex = YLeaf(YType.int32, "cdpCacheDeviceIndex")

                self.cdpcacheaddress = YLeaf(YType.str, "cdpCacheAddress")

                self.cdpcacheaddresstype = YLeaf(YType.enumeration, "cdpCacheAddressType")

                self.cdpcacheapplianceid = YLeaf(YType.uint32, "cdpCacheApplianceID")

                self.cdpcachecapabilities = YLeaf(YType.str, "cdpCacheCapabilities")

                self.cdpcachedeviceid = YLeaf(YType.str, "cdpCacheDeviceId")

                self.cdpcachedeviceport = YLeaf(YType.str, "cdpCacheDevicePort")

                self.cdpcacheduplex = YLeaf(YType.enumeration, "cdpCacheDuplex")

                self.cdpcachelastchange = YLeaf(YType.uint32, "cdpCacheLastChange")

                self.cdpcachemtu = YLeaf(YType.uint32, "cdpCacheMTU")

                self.cdpcachenativevlan = YLeaf(YType.int32, "cdpCacheNativeVLAN")

                self.cdpcachephyslocation = YLeaf(YType.str, "cdpCachePhysLocation")

                self.cdpcacheplatform = YLeaf(YType.str, "cdpCachePlatform")

                self.cdpcachepowerconsumption = YLeaf(YType.uint32, "cdpCachePowerConsumption")

                self.cdpcacheprimarymgmtaddr = YLeaf(YType.str, "cdpCachePrimaryMgmtAddr")

                self.cdpcacheprimarymgmtaddrtype = YLeaf(YType.enumeration, "cdpCachePrimaryMgmtAddrType")

                self.cdpcachesecondarymgmtaddr = YLeaf(YType.str, "cdpCacheSecondaryMgmtAddr")

                self.cdpcachesecondarymgmtaddrtype = YLeaf(YType.enumeration, "cdpCacheSecondaryMgmtAddrType")

                self.cdpcachesysname = YLeaf(YType.str, "cdpCacheSysName")

                self.cdpcachesysobjectid = YLeaf(YType.str, "cdpCacheSysObjectID")

                self.cdpcacheversion = YLeaf(YType.str, "cdpCacheVersion")

                self.cdpcachevlanid = YLeaf(YType.uint32, "cdpCacheVlanID")

                self.cdpcachevtpmgmtdomain = YLeaf(YType.str, "cdpCacheVTPMgmtDomain")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cdpcacheifindex",
                                "cdpcachedeviceindex",
                                "cdpcacheaddress",
                                "cdpcacheaddresstype",
                                "cdpcacheapplianceid",
                                "cdpcachecapabilities",
                                "cdpcachedeviceid",
                                "cdpcachedeviceport",
                                "cdpcacheduplex",
                                "cdpcachelastchange",
                                "cdpcachemtu",
                                "cdpcachenativevlan",
                                "cdpcachephyslocation",
                                "cdpcacheplatform",
                                "cdpcachepowerconsumption",
                                "cdpcacheprimarymgmtaddr",
                                "cdpcacheprimarymgmtaddrtype",
                                "cdpcachesecondarymgmtaddr",
                                "cdpcachesecondarymgmtaddrtype",
                                "cdpcachesysname",
                                "cdpcachesysobjectid",
                                "cdpcacheversion",
                                "cdpcachevlanid",
                                "cdpcachevtpmgmtdomain") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoCdpMib.Cdpcachetable.Cdpcacheentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoCdpMib.Cdpcachetable.Cdpcacheentry, self).__setattr__(name, value)

            class Cdpcacheduplex(Enum):
                """
                Cdpcacheduplex

                The remote device's interface's duplex mode, as reported in the 

                most recent CDP message.  The value unknown(1) indicates

                no duplex mode field (TLV) was reported in the most

                recent CDP message.

                .. data:: unknown = 1

                .. data:: halfduplex = 2

                .. data:: fullduplex = 3

                """

                unknown = Enum.YLeaf(1, "unknown")

                halfduplex = Enum.YLeaf(2, "halfduplex")

                fullduplex = Enum.YLeaf(3, "fullduplex")


            def has_data(self):
                return (
                    self.cdpcacheifindex.is_set or
                    self.cdpcachedeviceindex.is_set or
                    self.cdpcacheaddress.is_set or
                    self.cdpcacheaddresstype.is_set or
                    self.cdpcacheapplianceid.is_set or
                    self.cdpcachecapabilities.is_set or
                    self.cdpcachedeviceid.is_set or
                    self.cdpcachedeviceport.is_set or
                    self.cdpcacheduplex.is_set or
                    self.cdpcachelastchange.is_set or
                    self.cdpcachemtu.is_set or
                    self.cdpcachenativevlan.is_set or
                    self.cdpcachephyslocation.is_set or
                    self.cdpcacheplatform.is_set or
                    self.cdpcachepowerconsumption.is_set or
                    self.cdpcacheprimarymgmtaddr.is_set or
                    self.cdpcacheprimarymgmtaddrtype.is_set or
                    self.cdpcachesecondarymgmtaddr.is_set or
                    self.cdpcachesecondarymgmtaddrtype.is_set or
                    self.cdpcachesysname.is_set or
                    self.cdpcachesysobjectid.is_set or
                    self.cdpcacheversion.is_set or
                    self.cdpcachevlanid.is_set or
                    self.cdpcachevtpmgmtdomain.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cdpcacheifindex.yfilter != YFilter.not_set or
                    self.cdpcachedeviceindex.yfilter != YFilter.not_set or
                    self.cdpcacheaddress.yfilter != YFilter.not_set or
                    self.cdpcacheaddresstype.yfilter != YFilter.not_set or
                    self.cdpcacheapplianceid.yfilter != YFilter.not_set or
                    self.cdpcachecapabilities.yfilter != YFilter.not_set or
                    self.cdpcachedeviceid.yfilter != YFilter.not_set or
                    self.cdpcachedeviceport.yfilter != YFilter.not_set or
                    self.cdpcacheduplex.yfilter != YFilter.not_set or
                    self.cdpcachelastchange.yfilter != YFilter.not_set or
                    self.cdpcachemtu.yfilter != YFilter.not_set or
                    self.cdpcachenativevlan.yfilter != YFilter.not_set or
                    self.cdpcachephyslocation.yfilter != YFilter.not_set or
                    self.cdpcacheplatform.yfilter != YFilter.not_set or
                    self.cdpcachepowerconsumption.yfilter != YFilter.not_set or
                    self.cdpcacheprimarymgmtaddr.yfilter != YFilter.not_set or
                    self.cdpcacheprimarymgmtaddrtype.yfilter != YFilter.not_set or
                    self.cdpcachesecondarymgmtaddr.yfilter != YFilter.not_set or
                    self.cdpcachesecondarymgmtaddrtype.yfilter != YFilter.not_set or
                    self.cdpcachesysname.yfilter != YFilter.not_set or
                    self.cdpcachesysobjectid.yfilter != YFilter.not_set or
                    self.cdpcacheversion.yfilter != YFilter.not_set or
                    self.cdpcachevlanid.yfilter != YFilter.not_set or
                    self.cdpcachevtpmgmtdomain.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cdpCacheEntry" + "[cdpCacheIfIndex='" + self.cdpcacheifindex.get() + "']" + "[cdpCacheDeviceIndex='" + self.cdpcachedeviceindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-CDP-MIB:CISCO-CDP-MIB/cdpCacheTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cdpcacheifindex.is_set or self.cdpcacheifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdpcacheifindex.get_name_leafdata())
                if (self.cdpcachedeviceindex.is_set or self.cdpcachedeviceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdpcachedeviceindex.get_name_leafdata())
                if (self.cdpcacheaddress.is_set or self.cdpcacheaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdpcacheaddress.get_name_leafdata())
                if (self.cdpcacheaddresstype.is_set or self.cdpcacheaddresstype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdpcacheaddresstype.get_name_leafdata())
                if (self.cdpcacheapplianceid.is_set or self.cdpcacheapplianceid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdpcacheapplianceid.get_name_leafdata())
                if (self.cdpcachecapabilities.is_set or self.cdpcachecapabilities.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdpcachecapabilities.get_name_leafdata())
                if (self.cdpcachedeviceid.is_set or self.cdpcachedeviceid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdpcachedeviceid.get_name_leafdata())
                if (self.cdpcachedeviceport.is_set or self.cdpcachedeviceport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdpcachedeviceport.get_name_leafdata())
                if (self.cdpcacheduplex.is_set or self.cdpcacheduplex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdpcacheduplex.get_name_leafdata())
                if (self.cdpcachelastchange.is_set or self.cdpcachelastchange.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdpcachelastchange.get_name_leafdata())
                if (self.cdpcachemtu.is_set or self.cdpcachemtu.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdpcachemtu.get_name_leafdata())
                if (self.cdpcachenativevlan.is_set or self.cdpcachenativevlan.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdpcachenativevlan.get_name_leafdata())
                if (self.cdpcachephyslocation.is_set or self.cdpcachephyslocation.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdpcachephyslocation.get_name_leafdata())
                if (self.cdpcacheplatform.is_set or self.cdpcacheplatform.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdpcacheplatform.get_name_leafdata())
                if (self.cdpcachepowerconsumption.is_set or self.cdpcachepowerconsumption.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdpcachepowerconsumption.get_name_leafdata())
                if (self.cdpcacheprimarymgmtaddr.is_set or self.cdpcacheprimarymgmtaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdpcacheprimarymgmtaddr.get_name_leafdata())
                if (self.cdpcacheprimarymgmtaddrtype.is_set or self.cdpcacheprimarymgmtaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdpcacheprimarymgmtaddrtype.get_name_leafdata())
                if (self.cdpcachesecondarymgmtaddr.is_set or self.cdpcachesecondarymgmtaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdpcachesecondarymgmtaddr.get_name_leafdata())
                if (self.cdpcachesecondarymgmtaddrtype.is_set or self.cdpcachesecondarymgmtaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdpcachesecondarymgmtaddrtype.get_name_leafdata())
                if (self.cdpcachesysname.is_set or self.cdpcachesysname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdpcachesysname.get_name_leafdata())
                if (self.cdpcachesysobjectid.is_set or self.cdpcachesysobjectid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdpcachesysobjectid.get_name_leafdata())
                if (self.cdpcacheversion.is_set or self.cdpcacheversion.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdpcacheversion.get_name_leafdata())
                if (self.cdpcachevlanid.is_set or self.cdpcachevlanid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdpcachevlanid.get_name_leafdata())
                if (self.cdpcachevtpmgmtdomain.is_set or self.cdpcachevtpmgmtdomain.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdpcachevtpmgmtdomain.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cdpCacheIfIndex" or name == "cdpCacheDeviceIndex" or name == "cdpCacheAddress" or name == "cdpCacheAddressType" or name == "cdpCacheApplianceID" or name == "cdpCacheCapabilities" or name == "cdpCacheDeviceId" or name == "cdpCacheDevicePort" or name == "cdpCacheDuplex" or name == "cdpCacheLastChange" or name == "cdpCacheMTU" or name == "cdpCacheNativeVLAN" or name == "cdpCachePhysLocation" or name == "cdpCachePlatform" or name == "cdpCachePowerConsumption" or name == "cdpCachePrimaryMgmtAddr" or name == "cdpCachePrimaryMgmtAddrType" or name == "cdpCacheSecondaryMgmtAddr" or name == "cdpCacheSecondaryMgmtAddrType" or name == "cdpCacheSysName" or name == "cdpCacheSysObjectID" or name == "cdpCacheVersion" or name == "cdpCacheVlanID" or name == "cdpCacheVTPMgmtDomain"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cdpCacheIfIndex"):
                    self.cdpcacheifindex = value
                    self.cdpcacheifindex.value_namespace = name_space
                    self.cdpcacheifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cdpCacheDeviceIndex"):
                    self.cdpcachedeviceindex = value
                    self.cdpcachedeviceindex.value_namespace = name_space
                    self.cdpcachedeviceindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cdpCacheAddress"):
                    self.cdpcacheaddress = value
                    self.cdpcacheaddress.value_namespace = name_space
                    self.cdpcacheaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "cdpCacheAddressType"):
                    self.cdpcacheaddresstype = value
                    self.cdpcacheaddresstype.value_namespace = name_space
                    self.cdpcacheaddresstype.value_namespace_prefix = name_space_prefix
                if(value_path == "cdpCacheApplianceID"):
                    self.cdpcacheapplianceid = value
                    self.cdpcacheapplianceid.value_namespace = name_space
                    self.cdpcacheapplianceid.value_namespace_prefix = name_space_prefix
                if(value_path == "cdpCacheCapabilities"):
                    self.cdpcachecapabilities = value
                    self.cdpcachecapabilities.value_namespace = name_space
                    self.cdpcachecapabilities.value_namespace_prefix = name_space_prefix
                if(value_path == "cdpCacheDeviceId"):
                    self.cdpcachedeviceid = value
                    self.cdpcachedeviceid.value_namespace = name_space
                    self.cdpcachedeviceid.value_namespace_prefix = name_space_prefix
                if(value_path == "cdpCacheDevicePort"):
                    self.cdpcachedeviceport = value
                    self.cdpcachedeviceport.value_namespace = name_space
                    self.cdpcachedeviceport.value_namespace_prefix = name_space_prefix
                if(value_path == "cdpCacheDuplex"):
                    self.cdpcacheduplex = value
                    self.cdpcacheduplex.value_namespace = name_space
                    self.cdpcacheduplex.value_namespace_prefix = name_space_prefix
                if(value_path == "cdpCacheLastChange"):
                    self.cdpcachelastchange = value
                    self.cdpcachelastchange.value_namespace = name_space
                    self.cdpcachelastchange.value_namespace_prefix = name_space_prefix
                if(value_path == "cdpCacheMTU"):
                    self.cdpcachemtu = value
                    self.cdpcachemtu.value_namespace = name_space
                    self.cdpcachemtu.value_namespace_prefix = name_space_prefix
                if(value_path == "cdpCacheNativeVLAN"):
                    self.cdpcachenativevlan = value
                    self.cdpcachenativevlan.value_namespace = name_space
                    self.cdpcachenativevlan.value_namespace_prefix = name_space_prefix
                if(value_path == "cdpCachePhysLocation"):
                    self.cdpcachephyslocation = value
                    self.cdpcachephyslocation.value_namespace = name_space
                    self.cdpcachephyslocation.value_namespace_prefix = name_space_prefix
                if(value_path == "cdpCachePlatform"):
                    self.cdpcacheplatform = value
                    self.cdpcacheplatform.value_namespace = name_space
                    self.cdpcacheplatform.value_namespace_prefix = name_space_prefix
                if(value_path == "cdpCachePowerConsumption"):
                    self.cdpcachepowerconsumption = value
                    self.cdpcachepowerconsumption.value_namespace = name_space
                    self.cdpcachepowerconsumption.value_namespace_prefix = name_space_prefix
                if(value_path == "cdpCachePrimaryMgmtAddr"):
                    self.cdpcacheprimarymgmtaddr = value
                    self.cdpcacheprimarymgmtaddr.value_namespace = name_space
                    self.cdpcacheprimarymgmtaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cdpCachePrimaryMgmtAddrType"):
                    self.cdpcacheprimarymgmtaddrtype = value
                    self.cdpcacheprimarymgmtaddrtype.value_namespace = name_space
                    self.cdpcacheprimarymgmtaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "cdpCacheSecondaryMgmtAddr"):
                    self.cdpcachesecondarymgmtaddr = value
                    self.cdpcachesecondarymgmtaddr.value_namespace = name_space
                    self.cdpcachesecondarymgmtaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cdpCacheSecondaryMgmtAddrType"):
                    self.cdpcachesecondarymgmtaddrtype = value
                    self.cdpcachesecondarymgmtaddrtype.value_namespace = name_space
                    self.cdpcachesecondarymgmtaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "cdpCacheSysName"):
                    self.cdpcachesysname = value
                    self.cdpcachesysname.value_namespace = name_space
                    self.cdpcachesysname.value_namespace_prefix = name_space_prefix
                if(value_path == "cdpCacheSysObjectID"):
                    self.cdpcachesysobjectid = value
                    self.cdpcachesysobjectid.value_namespace = name_space
                    self.cdpcachesysobjectid.value_namespace_prefix = name_space_prefix
                if(value_path == "cdpCacheVersion"):
                    self.cdpcacheversion = value
                    self.cdpcacheversion.value_namespace = name_space
                    self.cdpcacheversion.value_namespace_prefix = name_space_prefix
                if(value_path == "cdpCacheVlanID"):
                    self.cdpcachevlanid = value
                    self.cdpcachevlanid.value_namespace = name_space
                    self.cdpcachevlanid.value_namespace_prefix = name_space_prefix
                if(value_path == "cdpCacheVTPMgmtDomain"):
                    self.cdpcachevtpmgmtdomain = value
                    self.cdpcachevtpmgmtdomain.value_namespace = name_space
                    self.cdpcachevtpmgmtdomain.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cdpcacheentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cdpcacheentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cdpCacheTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-CDP-MIB:CISCO-CDP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cdpCacheEntry"):
                for c in self.cdpcacheentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoCdpMib.Cdpcachetable.Cdpcacheentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cdpcacheentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cdpCacheEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cdpctaddresstable(Entity):
        """
        The (conceptual) table containing the list of 
        network\-layer addresses of a neighbor interface,
        as reported in the Address TLV of the most recently
        received CDP message. The first address included in
        the Address TLV is saved in cdpCacheAddress.  This
        table contains the remainder of the addresses in the
        Address TLV.
        
        .. attribute:: cdpctaddressentry
        
        	An entry (conceptual row) in the cdpCtAddressTable, containing the information on one address received via CDP  on one interface from one device.  Entries appear  when a CDP advertisement is received from a neighbor device, with an Address TLV.  Entries disappear when CDP is disabled on the interface, or globally. An entry  or entries would also disappear if the most recently received CDP packet contain fewer address entries in the Address TLV, than are currently present in the CDP cache
        	**type**\: list of    :py:class:`Cdpctaddressentry <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CiscoCdpMib.Cdpctaddresstable.Cdpctaddressentry>`
        
        

        """

        _prefix = 'CISCO-CDP-MIB'
        _revision = '2005-03-21'

        def __init__(self):
            super(CiscoCdpMib.Cdpctaddresstable, self).__init__()

            self.yang_name = "cdpCtAddressTable"
            self.yang_parent_name = "CISCO-CDP-MIB"

            self.cdpctaddressentry = YList(self)

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
                        super(CiscoCdpMib.Cdpctaddresstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoCdpMib.Cdpctaddresstable, self).__setattr__(name, value)


        class Cdpctaddressentry(Entity):
            """
            An entry (conceptual row) in the cdpCtAddressTable,
            containing the information on one address received via CDP 
            on one interface from one device.  Entries appear 
            when a CDP advertisement is received from a neighbor
            device, with an Address TLV.  Entries disappear when
            CDP is disabled on the interface, or globally. An entry 
            or entries would also disappear if the most recently
            received CDP packet contain fewer address entries in the
            Address TLV, than are currently present in the CDP cache.
            
            .. attribute:: cdpcacheifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**refers to**\:  :py:class:`cdpcacheifindex <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CiscoCdpMib.Cdpcachetable.Cdpcacheentry>`
            
            .. attribute:: cdpcachedeviceindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**refers to**\:  :py:class:`cdpcachedeviceindex <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CiscoCdpMib.Cdpcachetable.Cdpcacheentry>`
            
            .. attribute:: cdpctaddressindex  <key>
            
            	The index of the address entry for a given  cdpCacheIfIndex,cdpCacheDeviceIndex pair. It has the value N\-1 for the N\-th address in the Address TLV
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: cdpctaddress
            
            	The N\-th network\-layer address of the device as reported in the most recent CDP message's Address TLV, where N\-1 is given by the value of cdpCtAddressIndex. For example, if the the corresponding instance of cdpCtAddressType had the value 'ip(1)', then this object would be an IPv4\-address. NOTE \- The 1st address received in the Address TLV is        available using cdpCacheAddress
            	**type**\:  str
            
            .. attribute:: cdpctaddresstype
            
            	An indication of the type of address contained in the corresponding instance of cdpCtAddress
            	**type**\:   :py:class:`Cisconetworkprotocol <ydk.models.cisco_ios_xe.CISCO_TC.Cisconetworkprotocol>`
            
            

            """

            _prefix = 'CISCO-CDP-MIB'
            _revision = '2005-03-21'

            def __init__(self):
                super(CiscoCdpMib.Cdpctaddresstable.Cdpctaddressentry, self).__init__()

                self.yang_name = "cdpCtAddressEntry"
                self.yang_parent_name = "cdpCtAddressTable"

                self.cdpcacheifindex = YLeaf(YType.str, "cdpCacheIfIndex")

                self.cdpcachedeviceindex = YLeaf(YType.str, "cdpCacheDeviceIndex")

                self.cdpctaddressindex = YLeaf(YType.int32, "cdpCtAddressIndex")

                self.cdpctaddress = YLeaf(YType.str, "cdpCtAddress")

                self.cdpctaddresstype = YLeaf(YType.enumeration, "cdpCtAddressType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cdpcacheifindex",
                                "cdpcachedeviceindex",
                                "cdpctaddressindex",
                                "cdpctaddress",
                                "cdpctaddresstype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoCdpMib.Cdpctaddresstable.Cdpctaddressentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoCdpMib.Cdpctaddresstable.Cdpctaddressentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cdpcacheifindex.is_set or
                    self.cdpcachedeviceindex.is_set or
                    self.cdpctaddressindex.is_set or
                    self.cdpctaddress.is_set or
                    self.cdpctaddresstype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cdpcacheifindex.yfilter != YFilter.not_set or
                    self.cdpcachedeviceindex.yfilter != YFilter.not_set or
                    self.cdpctaddressindex.yfilter != YFilter.not_set or
                    self.cdpctaddress.yfilter != YFilter.not_set or
                    self.cdpctaddresstype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cdpCtAddressEntry" + "[cdpCacheIfIndex='" + self.cdpcacheifindex.get() + "']" + "[cdpCacheDeviceIndex='" + self.cdpcachedeviceindex.get() + "']" + "[cdpCtAddressIndex='" + self.cdpctaddressindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-CDP-MIB:CISCO-CDP-MIB/cdpCtAddressTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cdpcacheifindex.is_set or self.cdpcacheifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdpcacheifindex.get_name_leafdata())
                if (self.cdpcachedeviceindex.is_set or self.cdpcachedeviceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdpcachedeviceindex.get_name_leafdata())
                if (self.cdpctaddressindex.is_set or self.cdpctaddressindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdpctaddressindex.get_name_leafdata())
                if (self.cdpctaddress.is_set or self.cdpctaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdpctaddress.get_name_leafdata())
                if (self.cdpctaddresstype.is_set or self.cdpctaddresstype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdpctaddresstype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cdpCacheIfIndex" or name == "cdpCacheDeviceIndex" or name == "cdpCtAddressIndex" or name == "cdpCtAddress" or name == "cdpCtAddressType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cdpCacheIfIndex"):
                    self.cdpcacheifindex = value
                    self.cdpcacheifindex.value_namespace = name_space
                    self.cdpcacheifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cdpCacheDeviceIndex"):
                    self.cdpcachedeviceindex = value
                    self.cdpcachedeviceindex.value_namespace = name_space
                    self.cdpcachedeviceindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cdpCtAddressIndex"):
                    self.cdpctaddressindex = value
                    self.cdpctaddressindex.value_namespace = name_space
                    self.cdpctaddressindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cdpCtAddress"):
                    self.cdpctaddress = value
                    self.cdpctaddress.value_namespace = name_space
                    self.cdpctaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "cdpCtAddressType"):
                    self.cdpctaddresstype = value
                    self.cdpctaddresstype.value_namespace = name_space
                    self.cdpctaddresstype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cdpctaddressentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cdpctaddressentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cdpCtAddressTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-CDP-MIB:CISCO-CDP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cdpCtAddressEntry"):
                for c in self.cdpctaddressentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoCdpMib.Cdpctaddresstable.Cdpctaddressentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cdpctaddressentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cdpCtAddressEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.cdpcachetable is not None and self.cdpcachetable.has_data()) or
            (self.cdpctaddresstable is not None and self.cdpctaddresstable.has_data()) or
            (self.cdpglobal is not None and self.cdpglobal.has_data()) or
            (self.cdpinterfaceexttable is not None and self.cdpinterfaceexttable.has_data()) or
            (self.cdpinterfacetable is not None and self.cdpinterfacetable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cdpcachetable is not None and self.cdpcachetable.has_operation()) or
            (self.cdpctaddresstable is not None and self.cdpctaddresstable.has_operation()) or
            (self.cdpglobal is not None and self.cdpglobal.has_operation()) or
            (self.cdpinterfaceexttable is not None and self.cdpinterfaceexttable.has_operation()) or
            (self.cdpinterfacetable is not None and self.cdpinterfacetable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-CDP-MIB:CISCO-CDP-MIB" + path_buffer

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

        if (child_yang_name == "cdpCacheTable"):
            if (self.cdpcachetable is None):
                self.cdpcachetable = CiscoCdpMib.Cdpcachetable()
                self.cdpcachetable.parent = self
                self._children_name_map["cdpcachetable"] = "cdpCacheTable"
            return self.cdpcachetable

        if (child_yang_name == "cdpCtAddressTable"):
            if (self.cdpctaddresstable is None):
                self.cdpctaddresstable = CiscoCdpMib.Cdpctaddresstable()
                self.cdpctaddresstable.parent = self
                self._children_name_map["cdpctaddresstable"] = "cdpCtAddressTable"
            return self.cdpctaddresstable

        if (child_yang_name == "cdpGlobal"):
            if (self.cdpglobal is None):
                self.cdpglobal = CiscoCdpMib.Cdpglobal()
                self.cdpglobal.parent = self
                self._children_name_map["cdpglobal"] = "cdpGlobal"
            return self.cdpglobal

        if (child_yang_name == "cdpInterfaceExtTable"):
            if (self.cdpinterfaceexttable is None):
                self.cdpinterfaceexttable = CiscoCdpMib.Cdpinterfaceexttable()
                self.cdpinterfaceexttable.parent = self
                self._children_name_map["cdpinterfaceexttable"] = "cdpInterfaceExtTable"
            return self.cdpinterfaceexttable

        if (child_yang_name == "cdpInterfaceTable"):
            if (self.cdpinterfacetable is None):
                self.cdpinterfacetable = CiscoCdpMib.Cdpinterfacetable()
                self.cdpinterfacetable.parent = self
                self._children_name_map["cdpinterfacetable"] = "cdpInterfaceTable"
            return self.cdpinterfacetable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cdpCacheTable" or name == "cdpCtAddressTable" or name == "cdpGlobal" or name == "cdpInterfaceExtTable" or name == "cdpInterfaceTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoCdpMib()
        return self._top_entity


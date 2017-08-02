""" MPLS_L3VPN_STD_MIB 

This MIB contains managed object definitions for the
Layer\-3 Multiprotocol Label Switching Virtual
Private Networks.

Copyright (C) The Internet Society (2006).  This
version of this MIB module is part of RFC4382; see
the RFC itself for full legal notices.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Mplsl3Vpnrttype(Enum):
    """
    Mplsl3Vpnrttype

    Used to define the type of a route target usage.

    Route targets can be specified to be imported,

    exported, or both.  For a complete definition of a

    route target, see [RFC4364].

    .. data:: import_ = 1

    .. data:: export = 2

    .. data:: both = 3

    """

    import_ = Enum.YLeaf(1, "import")

    export = Enum.YLeaf(2, "export")

    both = Enum.YLeaf(3, "both")



class MplsL3VpnStdMib(Entity):
    """
    
    
    .. attribute:: mplsl3vpnifconftable
    
    	This table specifies per\-interface MPLS capability and associated information
    	**type**\:   :py:class:`Mplsl3Vpnifconftable <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MplsL3VpnStdMib.Mplsl3Vpnifconftable>`
    
    .. attribute:: mplsl3vpnscalars
    
    	
    	**type**\:   :py:class:`Mplsl3Vpnscalars <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MplsL3VpnStdMib.Mplsl3Vpnscalars>`
    
    .. attribute:: mplsl3vpnvrfrtetable
    
    	This table specifies per\-interface MPLS L3VPN VRF Table routing information.  Entries in this table define VRF routing entries associated with the specified MPLS/VPN interfaces.  Note  that this table contains both BGP and Interior Gateway Protocol IGP routes, as both may appear in the same VRF
    	**type**\:   :py:class:`Mplsl3Vpnvrfrtetable <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MplsL3VpnStdMib.Mplsl3Vpnvrfrtetable>`
    
    .. attribute:: mplsl3vpnvrfrttable
    
    	This table specifies per\-VRF route target association. Each entry identifies a connectivity policy supported as part of a VPN
    	**type**\:   :py:class:`Mplsl3Vpnvrfrttable <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MplsL3VpnStdMib.Mplsl3Vpnvrfrttable>`
    
    .. attribute:: mplsl3vpnvrftable
    
    	This table specifies per\-interface MPLS L3VPN VRF Table capability and associated information. Entries in this table define VRF routing instances associated with MPLS/VPN interfaces.  Note that multiple interfaces can belong to the same VRF instance.  The collection of all VRF instances comprises an actual VPN
    	**type**\:   :py:class:`Mplsl3Vpnvrftable <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MplsL3VpnStdMib.Mplsl3Vpnvrftable>`
    
    

    """

    _prefix = 'MPLS-L3VPN-STD-MIB'
    _revision = '2006-01-23'

    def __init__(self):
        super(MplsL3VpnStdMib, self).__init__()
        self._top_entity = None

        self.yang_name = "MPLS-L3VPN-STD-MIB"
        self.yang_parent_name = "MPLS-L3VPN-STD-MIB"

        self.mplsl3vpnifconftable = MplsL3VpnStdMib.Mplsl3Vpnifconftable()
        self.mplsl3vpnifconftable.parent = self
        self._children_name_map["mplsl3vpnifconftable"] = "mplsL3VpnIfConfTable"
        self._children_yang_names.add("mplsL3VpnIfConfTable")

        self.mplsl3vpnscalars = MplsL3VpnStdMib.Mplsl3Vpnscalars()
        self.mplsl3vpnscalars.parent = self
        self._children_name_map["mplsl3vpnscalars"] = "mplsL3VpnScalars"
        self._children_yang_names.add("mplsL3VpnScalars")

        self.mplsl3vpnvrfrtetable = MplsL3VpnStdMib.Mplsl3Vpnvrfrtetable()
        self.mplsl3vpnvrfrtetable.parent = self
        self._children_name_map["mplsl3vpnvrfrtetable"] = "mplsL3VpnVrfRteTable"
        self._children_yang_names.add("mplsL3VpnVrfRteTable")

        self.mplsl3vpnvrfrttable = MplsL3VpnStdMib.Mplsl3Vpnvrfrttable()
        self.mplsl3vpnvrfrttable.parent = self
        self._children_name_map["mplsl3vpnvrfrttable"] = "mplsL3VpnVrfRTTable"
        self._children_yang_names.add("mplsL3VpnVrfRTTable")

        self.mplsl3vpnvrftable = MplsL3VpnStdMib.Mplsl3Vpnvrftable()
        self.mplsl3vpnvrftable.parent = self
        self._children_name_map["mplsl3vpnvrftable"] = "mplsL3VpnVrfTable"
        self._children_yang_names.add("mplsL3VpnVrfTable")


    class Mplsl3Vpnscalars(Entity):
        """
        
        
        .. attribute:: mplsl3vpnactivevrfs
        
        	The number of VRFs that are active on this node. That is, those VRFs whose corresponding mplsL3VpnVrfOperStatus object value is equal to operational (1)
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: mplsl3vpnconfiguredvrfs
        
        	The number of VRFs that are configured on this node
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: mplsl3vpnconnectedinterfaces
        
        	Total number of interfaces connected to a VRF
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: mplsl3vpnilllblrcvthrsh
        
        	The number of illegally received labels above which the mplsNumVrfSecIllglLblThrshExcd notification is issued.  The persistence of this value mimics that of the device's configuration
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: mplsl3vpnnotificationenable
        
        	If this object is true, then it enables the generation of all notifications defined in this MIB.  This object's value should be preserved across agent reboots
        	**type**\:  bool
        
        .. attribute:: mplsl3vpnvrfconfmaxpossrts
        
        	Denotes maximum number of routes that the device will allow all VRFs jointly to hold.  If this value is set to 0, this indicates that the device is unable to determine the absolute maximum.  In this case, the configured maximum MAY not actually be allowed by the device
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: mplsl3vpnvrfconfrtemxthrshtime
        
        	Denotes the interval in seconds, at which the route max threshold notification may be reissued after the maximum value has been exceeded (or has been reached if mplsL3VpnVrfConfMaxRoutes and mplsL3VpnVrfConfHighRteThresh are equal) and the initial notification has been issued.  This value is intended to prevent continuous generation of notifications by an agent in the event that routes are continually added to a VRF after it has reached its maximum value.  If this value is set to 0, the agent should only issue a single notification at the time that the maximum threshold has been reached, and should not issue any more notifications until the value of routes has fallen below the configured threshold value.  This is the recommended default behavior
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: seconds
        
        

        """

        _prefix = 'MPLS-L3VPN-STD-MIB'
        _revision = '2006-01-23'

        def __init__(self):
            super(MplsL3VpnStdMib.Mplsl3Vpnscalars, self).__init__()

            self.yang_name = "mplsL3VpnScalars"
            self.yang_parent_name = "MPLS-L3VPN-STD-MIB"

            self.mplsl3vpnactivevrfs = YLeaf(YType.uint32, "mplsL3VpnActiveVrfs")

            self.mplsl3vpnconfiguredvrfs = YLeaf(YType.uint32, "mplsL3VpnConfiguredVrfs")

            self.mplsl3vpnconnectedinterfaces = YLeaf(YType.uint32, "mplsL3VpnConnectedInterfaces")

            self.mplsl3vpnilllblrcvthrsh = YLeaf(YType.uint32, "mplsL3VpnIllLblRcvThrsh")

            self.mplsl3vpnnotificationenable = YLeaf(YType.boolean, "mplsL3VpnNotificationEnable")

            self.mplsl3vpnvrfconfmaxpossrts = YLeaf(YType.uint32, "mplsL3VpnVrfConfMaxPossRts")

            self.mplsl3vpnvrfconfrtemxthrshtime = YLeaf(YType.uint32, "mplsL3VpnVrfConfRteMxThrshTime")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("mplsl3vpnactivevrfs",
                            "mplsl3vpnconfiguredvrfs",
                            "mplsl3vpnconnectedinterfaces",
                            "mplsl3vpnilllblrcvthrsh",
                            "mplsl3vpnnotificationenable",
                            "mplsl3vpnvrfconfmaxpossrts",
                            "mplsl3vpnvrfconfrtemxthrshtime") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(MplsL3VpnStdMib.Mplsl3Vpnscalars, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsL3VpnStdMib.Mplsl3Vpnscalars, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.mplsl3vpnactivevrfs.is_set or
                self.mplsl3vpnconfiguredvrfs.is_set or
                self.mplsl3vpnconnectedinterfaces.is_set or
                self.mplsl3vpnilllblrcvthrsh.is_set or
                self.mplsl3vpnnotificationenable.is_set or
                self.mplsl3vpnvrfconfmaxpossrts.is_set or
                self.mplsl3vpnvrfconfrtemxthrshtime.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.mplsl3vpnactivevrfs.yfilter != YFilter.not_set or
                self.mplsl3vpnconfiguredvrfs.yfilter != YFilter.not_set or
                self.mplsl3vpnconnectedinterfaces.yfilter != YFilter.not_set or
                self.mplsl3vpnilllblrcvthrsh.yfilter != YFilter.not_set or
                self.mplsl3vpnnotificationenable.yfilter != YFilter.not_set or
                self.mplsl3vpnvrfconfmaxpossrts.yfilter != YFilter.not_set or
                self.mplsl3vpnvrfconfrtemxthrshtime.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mplsL3VpnScalars" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "MPLS-L3VPN-STD-MIB:MPLS-L3VPN-STD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.mplsl3vpnactivevrfs.is_set or self.mplsl3vpnactivevrfs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mplsl3vpnactivevrfs.get_name_leafdata())
            if (self.mplsl3vpnconfiguredvrfs.is_set or self.mplsl3vpnconfiguredvrfs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mplsl3vpnconfiguredvrfs.get_name_leafdata())
            if (self.mplsl3vpnconnectedinterfaces.is_set or self.mplsl3vpnconnectedinterfaces.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mplsl3vpnconnectedinterfaces.get_name_leafdata())
            if (self.mplsl3vpnilllblrcvthrsh.is_set or self.mplsl3vpnilllblrcvthrsh.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mplsl3vpnilllblrcvthrsh.get_name_leafdata())
            if (self.mplsl3vpnnotificationenable.is_set or self.mplsl3vpnnotificationenable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mplsl3vpnnotificationenable.get_name_leafdata())
            if (self.mplsl3vpnvrfconfmaxpossrts.is_set or self.mplsl3vpnvrfconfmaxpossrts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mplsl3vpnvrfconfmaxpossrts.get_name_leafdata())
            if (self.mplsl3vpnvrfconfrtemxthrshtime.is_set or self.mplsl3vpnvrfconfrtemxthrshtime.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mplsl3vpnvrfconfrtemxthrshtime.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mplsL3VpnActiveVrfs" or name == "mplsL3VpnConfiguredVrfs" or name == "mplsL3VpnConnectedInterfaces" or name == "mplsL3VpnIllLblRcvThrsh" or name == "mplsL3VpnNotificationEnable" or name == "mplsL3VpnVrfConfMaxPossRts" or name == "mplsL3VpnVrfConfRteMxThrshTime"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "mplsL3VpnActiveVrfs"):
                self.mplsl3vpnactivevrfs = value
                self.mplsl3vpnactivevrfs.value_namespace = name_space
                self.mplsl3vpnactivevrfs.value_namespace_prefix = name_space_prefix
            if(value_path == "mplsL3VpnConfiguredVrfs"):
                self.mplsl3vpnconfiguredvrfs = value
                self.mplsl3vpnconfiguredvrfs.value_namespace = name_space
                self.mplsl3vpnconfiguredvrfs.value_namespace_prefix = name_space_prefix
            if(value_path == "mplsL3VpnConnectedInterfaces"):
                self.mplsl3vpnconnectedinterfaces = value
                self.mplsl3vpnconnectedinterfaces.value_namespace = name_space
                self.mplsl3vpnconnectedinterfaces.value_namespace_prefix = name_space_prefix
            if(value_path == "mplsL3VpnIllLblRcvThrsh"):
                self.mplsl3vpnilllblrcvthrsh = value
                self.mplsl3vpnilllblrcvthrsh.value_namespace = name_space
                self.mplsl3vpnilllblrcvthrsh.value_namespace_prefix = name_space_prefix
            if(value_path == "mplsL3VpnNotificationEnable"):
                self.mplsl3vpnnotificationenable = value
                self.mplsl3vpnnotificationenable.value_namespace = name_space
                self.mplsl3vpnnotificationenable.value_namespace_prefix = name_space_prefix
            if(value_path == "mplsL3VpnVrfConfMaxPossRts"):
                self.mplsl3vpnvrfconfmaxpossrts = value
                self.mplsl3vpnvrfconfmaxpossrts.value_namespace = name_space
                self.mplsl3vpnvrfconfmaxpossrts.value_namespace_prefix = name_space_prefix
            if(value_path == "mplsL3VpnVrfConfRteMxThrshTime"):
                self.mplsl3vpnvrfconfrtemxthrshtime = value
                self.mplsl3vpnvrfconfrtemxthrshtime.value_namespace = name_space
                self.mplsl3vpnvrfconfrtemxthrshtime.value_namespace_prefix = name_space_prefix


    class Mplsl3Vpnifconftable(Entity):
        """
        This table specifies per\-interface MPLS capability
        and associated information.
        
        .. attribute:: mplsl3vpnifconfentry
        
        	An entry in this table is created by an LSR for every interface capable of supporting MPLS L3VPN. Each entry in this table is meant to correspond to an entry in the Interfaces Table
        	**type**\: list of    :py:class:`Mplsl3Vpnifconfentry <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MplsL3VpnStdMib.Mplsl3Vpnifconftable.Mplsl3Vpnifconfentry>`
        
        

        """

        _prefix = 'MPLS-L3VPN-STD-MIB'
        _revision = '2006-01-23'

        def __init__(self):
            super(MplsL3VpnStdMib.Mplsl3Vpnifconftable, self).__init__()

            self.yang_name = "mplsL3VpnIfConfTable"
            self.yang_parent_name = "MPLS-L3VPN-STD-MIB"

            self.mplsl3vpnifconfentry = YList(self)

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
                        super(MplsL3VpnStdMib.Mplsl3Vpnifconftable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsL3VpnStdMib.Mplsl3Vpnifconftable, self).__setattr__(name, value)


        class Mplsl3Vpnifconfentry(Entity):
            """
            An entry in this table is created by an LSR for
            every interface capable of supporting MPLS L3VPN.
            Each entry in this table is meant to correspond to
            an entry in the Interfaces Table.
            
            .. attribute:: mplsl3vpnvrfname  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..31
            
            	**refers to**\:  :py:class:`mplsl3vpnvrfname <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MplsL3VpnStdMib.Mplsl3Vpnvrftable.Mplsl3Vpnvrfentry>`
            
            .. attribute:: mplsl3vpnifconfindex  <key>
            
            	This is a unique index for an entry in the mplsL3VpnIfConfTable.  A non\-zero index for an entry indicates the ifIndex for the corresponding interface entry in the MPLS\-VPN\-layer in the ifTable. Note that this table does not necessarily correspond one\-to\-one with all entries in the Interface MIB having an ifType of MPLS\-layer; rather, only those that are enabled for MPLS L3VPN functionality
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: mplsl3vpnifconfrowstatus
            
            	This variable is used to create, modify, and/or delete a row in this table.  Rows in this table signify that the specified interface is associated with this VRF.  If the row creation operation succeeds, the interface will have been associated with the specified VRF, otherwise the agent MUST not allow the association.  If the agent only allows read\-only operations on this table, it MUST create entries in this table as they are created on the device.  When a row in this table is in active(1) state, no objects in that row can be modified except mplsL3VpnIfConfStorageType and mplsL3VpnIfConfRowStatus
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: mplsl3vpnifconfstoragetype
            
            	The storage type for this VPN If entry. Conceptual rows having the value 'permanent' need not allow write access to any columnar objects in the row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            .. attribute:: mplsl3vpnifvpnclassification
            
            	Denotes whether this link participates in a carrier's carrier, enterprise, or inter\-provider scenario
            	**type**\:   :py:class:`Mplsl3Vpnifvpnclassification <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MplsL3VpnStdMib.Mplsl3Vpnifconftable.Mplsl3Vpnifconfentry.Mplsl3Vpnifvpnclassification>`
            
            .. attribute:: mplsl3vpnifvpnroutedistprotocol
            
            	Denotes the route distribution protocol across the PE\-CE link.  Note that more than one routing protocol may be enabled at the same time; thus, this object is specified as a bitmask.  For example, static(5) and ospf(2) are a typical configuration
            	**type**\:   :py:class:`Mplsl3Vpnifvpnroutedistprotocol <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MplsL3VpnStdMib.Mplsl3Vpnifconftable.Mplsl3Vpnifconfentry.Mplsl3Vpnifvpnroutedistprotocol>`
            
            

            """

            _prefix = 'MPLS-L3VPN-STD-MIB'
            _revision = '2006-01-23'

            def __init__(self):
                super(MplsL3VpnStdMib.Mplsl3Vpnifconftable.Mplsl3Vpnifconfentry, self).__init__()

                self.yang_name = "mplsL3VpnIfConfEntry"
                self.yang_parent_name = "mplsL3VpnIfConfTable"

                self.mplsl3vpnvrfname = YLeaf(YType.str, "mplsL3VpnVrfName")

                self.mplsl3vpnifconfindex = YLeaf(YType.int32, "mplsL3VpnIfConfIndex")

                self.mplsl3vpnifconfrowstatus = YLeaf(YType.enumeration, "mplsL3VpnIfConfRowStatus")

                self.mplsl3vpnifconfstoragetype = YLeaf(YType.enumeration, "mplsL3VpnIfConfStorageType")

                self.mplsl3vpnifvpnclassification = YLeaf(YType.enumeration, "mplsL3VpnIfVpnClassification")

                self.mplsl3vpnifvpnroutedistprotocol = YLeaf(YType.bits, "mplsL3VpnIfVpnRouteDistProtocol")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("mplsl3vpnvrfname",
                                "mplsl3vpnifconfindex",
                                "mplsl3vpnifconfrowstatus",
                                "mplsl3vpnifconfstoragetype",
                                "mplsl3vpnifvpnclassification",
                                "mplsl3vpnifvpnroutedistprotocol") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsL3VpnStdMib.Mplsl3Vpnifconftable.Mplsl3Vpnifconfentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsL3VpnStdMib.Mplsl3Vpnifconftable.Mplsl3Vpnifconfentry, self).__setattr__(name, value)

            class Mplsl3Vpnifvpnclassification(Enum):
                """
                Mplsl3Vpnifvpnclassification

                Denotes whether this link participates in a

                carrier's carrier, enterprise, or inter\-provider

                scenario.

                .. data:: carrierOfCarrier = 1

                .. data:: enterprise = 2

                .. data:: interProvider = 3

                """

                carrierOfCarrier = Enum.YLeaf(1, "carrierOfCarrier")

                enterprise = Enum.YLeaf(2, "enterprise")

                interProvider = Enum.YLeaf(3, "interProvider")


            def has_data(self):
                return (
                    self.mplsl3vpnvrfname.is_set or
                    self.mplsl3vpnifconfindex.is_set or
                    self.mplsl3vpnifconfrowstatus.is_set or
                    self.mplsl3vpnifconfstoragetype.is_set or
                    self.mplsl3vpnifvpnclassification.is_set or
                    self.mplsl3vpnifvpnroutedistprotocol.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfname.yfilter != YFilter.not_set or
                    self.mplsl3vpnifconfindex.yfilter != YFilter.not_set or
                    self.mplsl3vpnifconfrowstatus.yfilter != YFilter.not_set or
                    self.mplsl3vpnifconfstoragetype.yfilter != YFilter.not_set or
                    self.mplsl3vpnifvpnclassification.yfilter != YFilter.not_set or
                    self.mplsl3vpnifvpnroutedistprotocol.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mplsL3VpnIfConfEntry" + "[mplsL3VpnVrfName='" + self.mplsl3vpnvrfname.get() + "']" + "[mplsL3VpnIfConfIndex='" + self.mplsl3vpnifconfindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "MPLS-L3VPN-STD-MIB:MPLS-L3VPN-STD-MIB/mplsL3VpnIfConfTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.mplsl3vpnvrfname.is_set or self.mplsl3vpnvrfname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfname.get_name_leafdata())
                if (self.mplsl3vpnifconfindex.is_set or self.mplsl3vpnifconfindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnifconfindex.get_name_leafdata())
                if (self.mplsl3vpnifconfrowstatus.is_set or self.mplsl3vpnifconfrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnifconfrowstatus.get_name_leafdata())
                if (self.mplsl3vpnifconfstoragetype.is_set or self.mplsl3vpnifconfstoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnifconfstoragetype.get_name_leafdata())
                if (self.mplsl3vpnifvpnclassification.is_set or self.mplsl3vpnifvpnclassification.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnifvpnclassification.get_name_leafdata())
                if (self.mplsl3vpnifvpnroutedistprotocol.is_set or self.mplsl3vpnifvpnroutedistprotocol.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnifvpnroutedistprotocol.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mplsL3VpnVrfName" or name == "mplsL3VpnIfConfIndex" or name == "mplsL3VpnIfConfRowStatus" or name == "mplsL3VpnIfConfStorageType" or name == "mplsL3VpnIfVpnClassification" or name == "mplsL3VpnIfVpnRouteDistProtocol"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "mplsL3VpnVrfName"):
                    self.mplsl3vpnvrfname = value
                    self.mplsl3vpnvrfname.value_namespace = name_space
                    self.mplsl3vpnvrfname.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnIfConfIndex"):
                    self.mplsl3vpnifconfindex = value
                    self.mplsl3vpnifconfindex.value_namespace = name_space
                    self.mplsl3vpnifconfindex.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnIfConfRowStatus"):
                    self.mplsl3vpnifconfrowstatus = value
                    self.mplsl3vpnifconfrowstatus.value_namespace = name_space
                    self.mplsl3vpnifconfrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnIfConfStorageType"):
                    self.mplsl3vpnifconfstoragetype = value
                    self.mplsl3vpnifconfstoragetype.value_namespace = name_space
                    self.mplsl3vpnifconfstoragetype.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnIfVpnClassification"):
                    self.mplsl3vpnifvpnclassification = value
                    self.mplsl3vpnifvpnclassification.value_namespace = name_space
                    self.mplsl3vpnifvpnclassification.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnIfVpnRouteDistProtocol"):
                    self.mplsl3vpnifvpnroutedistprotocol[value] = True

        def has_data(self):
            for c in self.mplsl3vpnifconfentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.mplsl3vpnifconfentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mplsL3VpnIfConfTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "MPLS-L3VPN-STD-MIB:MPLS-L3VPN-STD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mplsL3VpnIfConfEntry"):
                for c in self.mplsl3vpnifconfentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = MplsL3VpnStdMib.Mplsl3Vpnifconftable.Mplsl3Vpnifconfentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mplsl3vpnifconfentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mplsL3VpnIfConfEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Mplsl3Vpnvrftable(Entity):
        """
        This table specifies per\-interface MPLS L3VPN
        VRF Table capability and associated information.
        Entries in this table define VRF routing instances
        associated with MPLS/VPN interfaces.  Note that
        multiple interfaces can belong to the same VRF
        instance.  The collection of all VRF instances
        comprises an actual VPN.
        
        .. attribute:: mplsl3vpnvrfentry
        
        	An entry in this table is created by an LSR for every VRF capable of supporting MPLS L3VPN.  The indexing provides an ordering of VRFs per\-VPN interface
        	**type**\: list of    :py:class:`Mplsl3Vpnvrfentry <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MplsL3VpnStdMib.Mplsl3Vpnvrftable.Mplsl3Vpnvrfentry>`
        
        

        """

        _prefix = 'MPLS-L3VPN-STD-MIB'
        _revision = '2006-01-23'

        def __init__(self):
            super(MplsL3VpnStdMib.Mplsl3Vpnvrftable, self).__init__()

            self.yang_name = "mplsL3VpnVrfTable"
            self.yang_parent_name = "MPLS-L3VPN-STD-MIB"

            self.mplsl3vpnvrfentry = YList(self)

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
                        super(MplsL3VpnStdMib.Mplsl3Vpnvrftable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsL3VpnStdMib.Mplsl3Vpnvrftable, self).__setattr__(name, value)


        class Mplsl3Vpnvrfentry(Entity):
            """
            An entry in this table is created by an LSR for
            every VRF capable of supporting MPLS L3VPN.  The
            indexing provides an ordering of VRFs per\-VPN
            interface.
            
            .. attribute:: mplsl3vpnvrfname  <key>
            
            	The human\-readable name of this VPN.  This MAY be equivalent to the [RFC2685] VPN\-ID, but may also vary.  If it is set to the VPN ID, it MUST be equivalent to the value of mplsL3VpnVrfVpnId. It is strongly recommended that all sites supporting VRFs that are part of the same VPN use the same naming convention for VRFs as well as the same VPN ID
            	**type**\:  str
            
            	**length:** 0..31
            
            .. attribute:: mplsl3vpnvrfactiveinterfaces
            
            	Total number of interfaces connected to this VRF with ifOperStatus = up(1).  This value should increase when an interface is associated with the corresponding VRF and its corresponding ifOperStatus is equal to up(1).  If an interface is associated whose ifOperStatus is not up(1), then the value is not incremented until such time as it transitions to this state.  This value should be decremented when an interface is disassociated with a VRF or the corresponding ifOperStatus transitions out of the up(1) state to any other state
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsl3vpnvrfassociatedinterfaces
            
            	Total number of interfaces connected to this VRF (independent of ifOperStatus type)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsl3vpnvrfconfadminstatus
            
            	Indicates the desired operational status of this VRF
            	**type**\:   :py:class:`Mplsl3Vpnvrfconfadminstatus <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MplsL3VpnStdMib.Mplsl3Vpnvrftable.Mplsl3Vpnvrfentry.Mplsl3Vpnvrfconfadminstatus>`
            
            .. attribute:: mplsl3vpnvrfconfhighrtethresh
            
            	Denotes high\-level water marker for the number of routes that this VRF may hold
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsl3vpnvrfconflastchanged
            
            	The value of sysUpTime at the time of the last change of this table entry, which includes changes of VRF parameters defined in this table or addition or deletion of interfaces associated with this VRF
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsl3vpnvrfconfmaxroutes
            
            	Denotes maximum number of routes that this VRF is configured to hold.  This value MUST be less than or equal to mplsL3VpnVrfConfMaxPossRts unless it is set to 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsl3vpnvrfconfmidrtethresh
            
            	Denotes mid\-level water marker for the number of routes that this VRF may hold
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsl3vpnvrfconfrowstatus
            
            	This variable is used to create, modify, and/or delete a row in this table.  When a row in this table is in active(1) state, no objects in that row can be modified except mplsL3VpnVrfConfAdminStatus, mplsL3VpnVrfConfRowStatus, and mplsL3VpnVrfConfStorageType
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: mplsl3vpnvrfconfstoragetype
            
            	The storage type for this VPN VRF entry. Conceptual rows having the value 'permanent' need not allow write access to any columnar objects in the row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            .. attribute:: mplsl3vpnvrfcreationtime
            
            	The time at which this VRF entry was created
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsl3vpnvrfdescription
            
            	The human\-readable description of this VRF
            	**type**\:  str
            
            .. attribute:: mplsl3vpnvrfoperstatus
            
            	Denotes whether or not a VRF is operational.  A VRF is up(1) when there is at least one interface associated with the VRF whose ifOperStatus is up(1).  A VRF is down(2) when\: a. There does not exist at least one interface whose    ifOperStatus is up(1). b. There are no interfaces associated with the VRF
            	**type**\:   :py:class:`Mplsl3Vpnvrfoperstatus <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MplsL3VpnStdMib.Mplsl3Vpnvrftable.Mplsl3Vpnvrfentry.Mplsl3Vpnvrfoperstatus>`
            
            .. attribute:: mplsl3vpnvrfperfcurrnumroutes
            
            	Indicates the number of routes currently used by this VRF
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsl3vpnvrfperfdisctime
            
            	The value of sysUpTime on the most recent occasion at which any one or more of this entry's counters suffered a discontinuity.  If no such discontinuities have occurred since the last re\-initialization of the local management subsystem, then this object contains a zero value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsl3vpnvrfperfroutesadded
            
            	Indicates the number of routes added to this VPN/VRF since the last discontinuity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsL3VpnVrfPerfDiscTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsl3vpnvrfperfroutesdeleted
            
            	Indicates the number of routes removed from this VPN/VRF.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsL3VpnVrfPerfDiscTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsl3vpnvrfperfroutesdropped
            
            	This counter should be incremented when the number of routes contained by the specified VRF exceeds or attempts to exceed the maximum allowed value as indicated by mplsL3VpnVrfMaxRouteThreshold.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsL3VpnVrfPerfDiscTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsl3vpnvrfrd
            
            	The route distinguisher for this VRF
            	**type**\:  str
            
            	**length:** 0..256
            
            .. attribute:: mplsl3vpnvrfsecdiscontinuitytime
            
            	The value of sysUpTime on the most recent occasion at which any one or more of this entry's counters suffered a discontinuity.  If no such discontinuities have occurred since the last re\-initialization of the local management subsystem, then this object contains a zero value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsl3vpnvrfsecillegallblvltns
            
            	Indicates the number of illegally received labels on this VPN/VRF.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsL3VpnVrfSecDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsl3vpnvrfvpnid
            
            	The VPN ID as specified in [RFC2685].  If a VPN ID has not been specified for this VRF, then this variable SHOULD be set to a zero\-length OCTET STRING
            	**type**\:  str
            
            	**length:** 0 \| 7
            
            

            """

            _prefix = 'MPLS-L3VPN-STD-MIB'
            _revision = '2006-01-23'

            def __init__(self):
                super(MplsL3VpnStdMib.Mplsl3Vpnvrftable.Mplsl3Vpnvrfentry, self).__init__()

                self.yang_name = "mplsL3VpnVrfEntry"
                self.yang_parent_name = "mplsL3VpnVrfTable"

                self.mplsl3vpnvrfname = YLeaf(YType.str, "mplsL3VpnVrfName")

                self.mplsl3vpnvrfactiveinterfaces = YLeaf(YType.uint32, "mplsL3VpnVrfActiveInterfaces")

                self.mplsl3vpnvrfassociatedinterfaces = YLeaf(YType.uint32, "mplsL3VpnVrfAssociatedInterfaces")

                self.mplsl3vpnvrfconfadminstatus = YLeaf(YType.enumeration, "mplsL3VpnVrfConfAdminStatus")

                self.mplsl3vpnvrfconfhighrtethresh = YLeaf(YType.uint32, "mplsL3VpnVrfConfHighRteThresh")

                self.mplsl3vpnvrfconflastchanged = YLeaf(YType.uint32, "mplsL3VpnVrfConfLastChanged")

                self.mplsl3vpnvrfconfmaxroutes = YLeaf(YType.uint32, "mplsL3VpnVrfConfMaxRoutes")

                self.mplsl3vpnvrfconfmidrtethresh = YLeaf(YType.uint32, "mplsL3VpnVrfConfMidRteThresh")

                self.mplsl3vpnvrfconfrowstatus = YLeaf(YType.enumeration, "mplsL3VpnVrfConfRowStatus")

                self.mplsl3vpnvrfconfstoragetype = YLeaf(YType.enumeration, "mplsL3VpnVrfConfStorageType")

                self.mplsl3vpnvrfcreationtime = YLeaf(YType.uint32, "mplsL3VpnVrfCreationTime")

                self.mplsl3vpnvrfdescription = YLeaf(YType.str, "mplsL3VpnVrfDescription")

                self.mplsl3vpnvrfoperstatus = YLeaf(YType.enumeration, "mplsL3VpnVrfOperStatus")

                self.mplsl3vpnvrfperfcurrnumroutes = YLeaf(YType.uint32, "mplsL3VpnVrfPerfCurrNumRoutes")

                self.mplsl3vpnvrfperfdisctime = YLeaf(YType.uint32, "mplsL3VpnVrfPerfDiscTime")

                self.mplsl3vpnvrfperfroutesadded = YLeaf(YType.uint32, "mplsL3VpnVrfPerfRoutesAdded")

                self.mplsl3vpnvrfperfroutesdeleted = YLeaf(YType.uint32, "mplsL3VpnVrfPerfRoutesDeleted")

                self.mplsl3vpnvrfperfroutesdropped = YLeaf(YType.uint32, "mplsL3VpnVrfPerfRoutesDropped")

                self.mplsl3vpnvrfrd = YLeaf(YType.str, "mplsL3VpnVrfRD")

                self.mplsl3vpnvrfsecdiscontinuitytime = YLeaf(YType.uint32, "mplsL3VpnVrfSecDiscontinuityTime")

                self.mplsl3vpnvrfsecillegallblvltns = YLeaf(YType.uint32, "mplsL3VpnVrfSecIllegalLblVltns")

                self.mplsl3vpnvrfvpnid = YLeaf(YType.str, "mplsL3VpnVrfVpnId")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("mplsl3vpnvrfname",
                                "mplsl3vpnvrfactiveinterfaces",
                                "mplsl3vpnvrfassociatedinterfaces",
                                "mplsl3vpnvrfconfadminstatus",
                                "mplsl3vpnvrfconfhighrtethresh",
                                "mplsl3vpnvrfconflastchanged",
                                "mplsl3vpnvrfconfmaxroutes",
                                "mplsl3vpnvrfconfmidrtethresh",
                                "mplsl3vpnvrfconfrowstatus",
                                "mplsl3vpnvrfconfstoragetype",
                                "mplsl3vpnvrfcreationtime",
                                "mplsl3vpnvrfdescription",
                                "mplsl3vpnvrfoperstatus",
                                "mplsl3vpnvrfperfcurrnumroutes",
                                "mplsl3vpnvrfperfdisctime",
                                "mplsl3vpnvrfperfroutesadded",
                                "mplsl3vpnvrfperfroutesdeleted",
                                "mplsl3vpnvrfperfroutesdropped",
                                "mplsl3vpnvrfrd",
                                "mplsl3vpnvrfsecdiscontinuitytime",
                                "mplsl3vpnvrfsecillegallblvltns",
                                "mplsl3vpnvrfvpnid") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsL3VpnStdMib.Mplsl3Vpnvrftable.Mplsl3Vpnvrfentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsL3VpnStdMib.Mplsl3Vpnvrftable.Mplsl3Vpnvrfentry, self).__setattr__(name, value)

            class Mplsl3Vpnvrfconfadminstatus(Enum):
                """
                Mplsl3Vpnvrfconfadminstatus

                Indicates the desired operational status of this

                VRF.

                .. data:: up = 1

                .. data:: down = 2

                .. data:: testing = 3

                """

                up = Enum.YLeaf(1, "up")

                down = Enum.YLeaf(2, "down")

                testing = Enum.YLeaf(3, "testing")


            class Mplsl3Vpnvrfoperstatus(Enum):
                """
                Mplsl3Vpnvrfoperstatus

                Denotes whether or not a VRF is operational.  A VRF is

                up(1) when there is at least one interface associated

                with the VRF whose ifOperStatus is up(1).  A VRF is

                down(2) when\:

                a. There does not exist at least one interface whose

                   ifOperStatus is up(1).

                b. There are no interfaces associated with the VRF.

                .. data:: up = 1

                .. data:: down = 2

                """

                up = Enum.YLeaf(1, "up")

                down = Enum.YLeaf(2, "down")


            def has_data(self):
                return (
                    self.mplsl3vpnvrfname.is_set or
                    self.mplsl3vpnvrfactiveinterfaces.is_set or
                    self.mplsl3vpnvrfassociatedinterfaces.is_set or
                    self.mplsl3vpnvrfconfadminstatus.is_set or
                    self.mplsl3vpnvrfconfhighrtethresh.is_set or
                    self.mplsl3vpnvrfconflastchanged.is_set or
                    self.mplsl3vpnvrfconfmaxroutes.is_set or
                    self.mplsl3vpnvrfconfmidrtethresh.is_set or
                    self.mplsl3vpnvrfconfrowstatus.is_set or
                    self.mplsl3vpnvrfconfstoragetype.is_set or
                    self.mplsl3vpnvrfcreationtime.is_set or
                    self.mplsl3vpnvrfdescription.is_set or
                    self.mplsl3vpnvrfoperstatus.is_set or
                    self.mplsl3vpnvrfperfcurrnumroutes.is_set or
                    self.mplsl3vpnvrfperfdisctime.is_set or
                    self.mplsl3vpnvrfperfroutesadded.is_set or
                    self.mplsl3vpnvrfperfroutesdeleted.is_set or
                    self.mplsl3vpnvrfperfroutesdropped.is_set or
                    self.mplsl3vpnvrfrd.is_set or
                    self.mplsl3vpnvrfsecdiscontinuitytime.is_set or
                    self.mplsl3vpnvrfsecillegallblvltns.is_set or
                    self.mplsl3vpnvrfvpnid.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfname.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfactiveinterfaces.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfassociatedinterfaces.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfconfadminstatus.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfconfhighrtethresh.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfconflastchanged.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfconfmaxroutes.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfconfmidrtethresh.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfconfrowstatus.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfconfstoragetype.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfcreationtime.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfdescription.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfoperstatus.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfperfcurrnumroutes.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfperfdisctime.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfperfroutesadded.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfperfroutesdeleted.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfperfroutesdropped.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfrd.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfsecdiscontinuitytime.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfsecillegallblvltns.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfvpnid.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mplsL3VpnVrfEntry" + "[mplsL3VpnVrfName='" + self.mplsl3vpnvrfname.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "MPLS-L3VPN-STD-MIB:MPLS-L3VPN-STD-MIB/mplsL3VpnVrfTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.mplsl3vpnvrfname.is_set or self.mplsl3vpnvrfname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfname.get_name_leafdata())
                if (self.mplsl3vpnvrfactiveinterfaces.is_set or self.mplsl3vpnvrfactiveinterfaces.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfactiveinterfaces.get_name_leafdata())
                if (self.mplsl3vpnvrfassociatedinterfaces.is_set or self.mplsl3vpnvrfassociatedinterfaces.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfassociatedinterfaces.get_name_leafdata())
                if (self.mplsl3vpnvrfconfadminstatus.is_set or self.mplsl3vpnvrfconfadminstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfconfadminstatus.get_name_leafdata())
                if (self.mplsl3vpnvrfconfhighrtethresh.is_set or self.mplsl3vpnvrfconfhighrtethresh.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfconfhighrtethresh.get_name_leafdata())
                if (self.mplsl3vpnvrfconflastchanged.is_set or self.mplsl3vpnvrfconflastchanged.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfconflastchanged.get_name_leafdata())
                if (self.mplsl3vpnvrfconfmaxroutes.is_set or self.mplsl3vpnvrfconfmaxroutes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfconfmaxroutes.get_name_leafdata())
                if (self.mplsl3vpnvrfconfmidrtethresh.is_set or self.mplsl3vpnvrfconfmidrtethresh.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfconfmidrtethresh.get_name_leafdata())
                if (self.mplsl3vpnvrfconfrowstatus.is_set or self.mplsl3vpnvrfconfrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfconfrowstatus.get_name_leafdata())
                if (self.mplsl3vpnvrfconfstoragetype.is_set or self.mplsl3vpnvrfconfstoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfconfstoragetype.get_name_leafdata())
                if (self.mplsl3vpnvrfcreationtime.is_set or self.mplsl3vpnvrfcreationtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfcreationtime.get_name_leafdata())
                if (self.mplsl3vpnvrfdescription.is_set or self.mplsl3vpnvrfdescription.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfdescription.get_name_leafdata())
                if (self.mplsl3vpnvrfoperstatus.is_set or self.mplsl3vpnvrfoperstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfoperstatus.get_name_leafdata())
                if (self.mplsl3vpnvrfperfcurrnumroutes.is_set or self.mplsl3vpnvrfperfcurrnumroutes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfperfcurrnumroutes.get_name_leafdata())
                if (self.mplsl3vpnvrfperfdisctime.is_set or self.mplsl3vpnvrfperfdisctime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfperfdisctime.get_name_leafdata())
                if (self.mplsl3vpnvrfperfroutesadded.is_set or self.mplsl3vpnvrfperfroutesadded.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfperfroutesadded.get_name_leafdata())
                if (self.mplsl3vpnvrfperfroutesdeleted.is_set or self.mplsl3vpnvrfperfroutesdeleted.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfperfroutesdeleted.get_name_leafdata())
                if (self.mplsl3vpnvrfperfroutesdropped.is_set or self.mplsl3vpnvrfperfroutesdropped.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfperfroutesdropped.get_name_leafdata())
                if (self.mplsl3vpnvrfrd.is_set or self.mplsl3vpnvrfrd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfrd.get_name_leafdata())
                if (self.mplsl3vpnvrfsecdiscontinuitytime.is_set or self.mplsl3vpnvrfsecdiscontinuitytime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfsecdiscontinuitytime.get_name_leafdata())
                if (self.mplsl3vpnvrfsecillegallblvltns.is_set or self.mplsl3vpnvrfsecillegallblvltns.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfsecillegallblvltns.get_name_leafdata())
                if (self.mplsl3vpnvrfvpnid.is_set or self.mplsl3vpnvrfvpnid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfvpnid.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mplsL3VpnVrfName" or name == "mplsL3VpnVrfActiveInterfaces" or name == "mplsL3VpnVrfAssociatedInterfaces" or name == "mplsL3VpnVrfConfAdminStatus" or name == "mplsL3VpnVrfConfHighRteThresh" or name == "mplsL3VpnVrfConfLastChanged" or name == "mplsL3VpnVrfConfMaxRoutes" or name == "mplsL3VpnVrfConfMidRteThresh" or name == "mplsL3VpnVrfConfRowStatus" or name == "mplsL3VpnVrfConfStorageType" or name == "mplsL3VpnVrfCreationTime" or name == "mplsL3VpnVrfDescription" or name == "mplsL3VpnVrfOperStatus" or name == "mplsL3VpnVrfPerfCurrNumRoutes" or name == "mplsL3VpnVrfPerfDiscTime" or name == "mplsL3VpnVrfPerfRoutesAdded" or name == "mplsL3VpnVrfPerfRoutesDeleted" or name == "mplsL3VpnVrfPerfRoutesDropped" or name == "mplsL3VpnVrfRD" or name == "mplsL3VpnVrfSecDiscontinuityTime" or name == "mplsL3VpnVrfSecIllegalLblVltns" or name == "mplsL3VpnVrfVpnId"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "mplsL3VpnVrfName"):
                    self.mplsl3vpnvrfname = value
                    self.mplsl3vpnvrfname.value_namespace = name_space
                    self.mplsl3vpnvrfname.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfActiveInterfaces"):
                    self.mplsl3vpnvrfactiveinterfaces = value
                    self.mplsl3vpnvrfactiveinterfaces.value_namespace = name_space
                    self.mplsl3vpnvrfactiveinterfaces.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfAssociatedInterfaces"):
                    self.mplsl3vpnvrfassociatedinterfaces = value
                    self.mplsl3vpnvrfassociatedinterfaces.value_namespace = name_space
                    self.mplsl3vpnvrfassociatedinterfaces.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfConfAdminStatus"):
                    self.mplsl3vpnvrfconfadminstatus = value
                    self.mplsl3vpnvrfconfadminstatus.value_namespace = name_space
                    self.mplsl3vpnvrfconfadminstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfConfHighRteThresh"):
                    self.mplsl3vpnvrfconfhighrtethresh = value
                    self.mplsl3vpnvrfconfhighrtethresh.value_namespace = name_space
                    self.mplsl3vpnvrfconfhighrtethresh.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfConfLastChanged"):
                    self.mplsl3vpnvrfconflastchanged = value
                    self.mplsl3vpnvrfconflastchanged.value_namespace = name_space
                    self.mplsl3vpnvrfconflastchanged.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfConfMaxRoutes"):
                    self.mplsl3vpnvrfconfmaxroutes = value
                    self.mplsl3vpnvrfconfmaxroutes.value_namespace = name_space
                    self.mplsl3vpnvrfconfmaxroutes.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfConfMidRteThresh"):
                    self.mplsl3vpnvrfconfmidrtethresh = value
                    self.mplsl3vpnvrfconfmidrtethresh.value_namespace = name_space
                    self.mplsl3vpnvrfconfmidrtethresh.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfConfRowStatus"):
                    self.mplsl3vpnvrfconfrowstatus = value
                    self.mplsl3vpnvrfconfrowstatus.value_namespace = name_space
                    self.mplsl3vpnvrfconfrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfConfStorageType"):
                    self.mplsl3vpnvrfconfstoragetype = value
                    self.mplsl3vpnvrfconfstoragetype.value_namespace = name_space
                    self.mplsl3vpnvrfconfstoragetype.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfCreationTime"):
                    self.mplsl3vpnvrfcreationtime = value
                    self.mplsl3vpnvrfcreationtime.value_namespace = name_space
                    self.mplsl3vpnvrfcreationtime.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfDescription"):
                    self.mplsl3vpnvrfdescription = value
                    self.mplsl3vpnvrfdescription.value_namespace = name_space
                    self.mplsl3vpnvrfdescription.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfOperStatus"):
                    self.mplsl3vpnvrfoperstatus = value
                    self.mplsl3vpnvrfoperstatus.value_namespace = name_space
                    self.mplsl3vpnvrfoperstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfPerfCurrNumRoutes"):
                    self.mplsl3vpnvrfperfcurrnumroutes = value
                    self.mplsl3vpnvrfperfcurrnumroutes.value_namespace = name_space
                    self.mplsl3vpnvrfperfcurrnumroutes.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfPerfDiscTime"):
                    self.mplsl3vpnvrfperfdisctime = value
                    self.mplsl3vpnvrfperfdisctime.value_namespace = name_space
                    self.mplsl3vpnvrfperfdisctime.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfPerfRoutesAdded"):
                    self.mplsl3vpnvrfperfroutesadded = value
                    self.mplsl3vpnvrfperfroutesadded.value_namespace = name_space
                    self.mplsl3vpnvrfperfroutesadded.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfPerfRoutesDeleted"):
                    self.mplsl3vpnvrfperfroutesdeleted = value
                    self.mplsl3vpnvrfperfroutesdeleted.value_namespace = name_space
                    self.mplsl3vpnvrfperfroutesdeleted.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfPerfRoutesDropped"):
                    self.mplsl3vpnvrfperfroutesdropped = value
                    self.mplsl3vpnvrfperfroutesdropped.value_namespace = name_space
                    self.mplsl3vpnvrfperfroutesdropped.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfRD"):
                    self.mplsl3vpnvrfrd = value
                    self.mplsl3vpnvrfrd.value_namespace = name_space
                    self.mplsl3vpnvrfrd.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfSecDiscontinuityTime"):
                    self.mplsl3vpnvrfsecdiscontinuitytime = value
                    self.mplsl3vpnvrfsecdiscontinuitytime.value_namespace = name_space
                    self.mplsl3vpnvrfsecdiscontinuitytime.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfSecIllegalLblVltns"):
                    self.mplsl3vpnvrfsecillegallblvltns = value
                    self.mplsl3vpnvrfsecillegallblvltns.value_namespace = name_space
                    self.mplsl3vpnvrfsecillegallblvltns.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfVpnId"):
                    self.mplsl3vpnvrfvpnid = value
                    self.mplsl3vpnvrfvpnid.value_namespace = name_space
                    self.mplsl3vpnvrfvpnid.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.mplsl3vpnvrfentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.mplsl3vpnvrfentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mplsL3VpnVrfTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "MPLS-L3VPN-STD-MIB:MPLS-L3VPN-STD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mplsL3VpnVrfEntry"):
                for c in self.mplsl3vpnvrfentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = MplsL3VpnStdMib.Mplsl3Vpnvrftable.Mplsl3Vpnvrfentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mplsl3vpnvrfentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mplsL3VpnVrfEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Mplsl3Vpnvrfrttable(Entity):
        """
        This table specifies per\-VRF route target association.
        Each entry identifies a connectivity policy supported
        as part of a VPN.
        
        .. attribute:: mplsl3vpnvrfrtentry
        
        	An entry in this table is created by an LSR for each route target configured for a VRF supporting a MPLS L3VPN instance.  The indexing provides an ordering per\-VRF instance.  See [RFC4364] for a complete definition of a route target
        	**type**\: list of    :py:class:`Mplsl3Vpnvrfrtentry <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MplsL3VpnStdMib.Mplsl3Vpnvrfrttable.Mplsl3Vpnvrfrtentry>`
        
        

        """

        _prefix = 'MPLS-L3VPN-STD-MIB'
        _revision = '2006-01-23'

        def __init__(self):
            super(MplsL3VpnStdMib.Mplsl3Vpnvrfrttable, self).__init__()

            self.yang_name = "mplsL3VpnVrfRTTable"
            self.yang_parent_name = "MPLS-L3VPN-STD-MIB"

            self.mplsl3vpnvrfrtentry = YList(self)

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
                        super(MplsL3VpnStdMib.Mplsl3Vpnvrfrttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsL3VpnStdMib.Mplsl3Vpnvrfrttable, self).__setattr__(name, value)


        class Mplsl3Vpnvrfrtentry(Entity):
            """
            An entry in this table is created by an LSR for
            each route target configured for a VRF supporting
            a MPLS L3VPN instance.  The indexing provides an
            ordering per\-VRF instance.  See [RFC4364] for a
            complete definition of a route target.
            
            .. attribute:: mplsl3vpnvrfname  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..31
            
            	**refers to**\:  :py:class:`mplsl3vpnvrfname <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MplsL3VpnStdMib.Mplsl3Vpnvrftable.Mplsl3Vpnvrfentry>`
            
            .. attribute:: mplsl3vpnvrfrtindex  <key>
            
            	Auxiliary index for route targets configured for a particular VRF
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: mplsl3vpnvrfrttype  <key>
            
            	The route target distribution type
            	**type**\:   :py:class:`Mplsl3Vpnrttype <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.Mplsl3Vpnrttype>`
            
            .. attribute:: mplsl3vpnvrfrt
            
            	The route target distribution policy
            	**type**\:  str
            
            	**length:** 0..256
            
            .. attribute:: mplsl3vpnvrfrtdescr
            
            	Description of the route target
            	**type**\:  str
            
            .. attribute:: mplsl3vpnvrfrtrowstatus
            
            	This variable is used to create, modify, and/or delete a row in this table.  When a row in this table is in active(1) state, no objects in that row can be modified except mplsL3VpnVrfRTRowStatus
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: mplsl3vpnvrfrtstoragetype
            
            	The storage type for this VPN route target (RT) entry. Conceptual rows having the value 'permanent' need not allow write access to any columnar objects in the row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            

            """

            _prefix = 'MPLS-L3VPN-STD-MIB'
            _revision = '2006-01-23'

            def __init__(self):
                super(MplsL3VpnStdMib.Mplsl3Vpnvrfrttable.Mplsl3Vpnvrfrtentry, self).__init__()

                self.yang_name = "mplsL3VpnVrfRTEntry"
                self.yang_parent_name = "mplsL3VpnVrfRTTable"

                self.mplsl3vpnvrfname = YLeaf(YType.str, "mplsL3VpnVrfName")

                self.mplsl3vpnvrfrtindex = YLeaf(YType.uint32, "mplsL3VpnVrfRTIndex")

                self.mplsl3vpnvrfrttype = YLeaf(YType.enumeration, "mplsL3VpnVrfRTType")

                self.mplsl3vpnvrfrt = YLeaf(YType.str, "mplsL3VpnVrfRT")

                self.mplsl3vpnvrfrtdescr = YLeaf(YType.str, "mplsL3VpnVrfRTDescr")

                self.mplsl3vpnvrfrtrowstatus = YLeaf(YType.enumeration, "mplsL3VpnVrfRTRowStatus")

                self.mplsl3vpnvrfrtstoragetype = YLeaf(YType.enumeration, "mplsL3VpnVrfRTStorageType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("mplsl3vpnvrfname",
                                "mplsl3vpnvrfrtindex",
                                "mplsl3vpnvrfrttype",
                                "mplsl3vpnvrfrt",
                                "mplsl3vpnvrfrtdescr",
                                "mplsl3vpnvrfrtrowstatus",
                                "mplsl3vpnvrfrtstoragetype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsL3VpnStdMib.Mplsl3Vpnvrfrttable.Mplsl3Vpnvrfrtentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsL3VpnStdMib.Mplsl3Vpnvrfrttable.Mplsl3Vpnvrfrtentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.mplsl3vpnvrfname.is_set or
                    self.mplsl3vpnvrfrtindex.is_set or
                    self.mplsl3vpnvrfrttype.is_set or
                    self.mplsl3vpnvrfrt.is_set or
                    self.mplsl3vpnvrfrtdescr.is_set or
                    self.mplsl3vpnvrfrtrowstatus.is_set or
                    self.mplsl3vpnvrfrtstoragetype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfname.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfrtindex.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfrttype.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfrt.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfrtdescr.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfrtrowstatus.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfrtstoragetype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mplsL3VpnVrfRTEntry" + "[mplsL3VpnVrfName='" + self.mplsl3vpnvrfname.get() + "']" + "[mplsL3VpnVrfRTIndex='" + self.mplsl3vpnvrfrtindex.get() + "']" + "[mplsL3VpnVrfRTType='" + self.mplsl3vpnvrfrttype.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "MPLS-L3VPN-STD-MIB:MPLS-L3VPN-STD-MIB/mplsL3VpnVrfRTTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.mplsl3vpnvrfname.is_set or self.mplsl3vpnvrfname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfname.get_name_leafdata())
                if (self.mplsl3vpnvrfrtindex.is_set or self.mplsl3vpnvrfrtindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfrtindex.get_name_leafdata())
                if (self.mplsl3vpnvrfrttype.is_set or self.mplsl3vpnvrfrttype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfrttype.get_name_leafdata())
                if (self.mplsl3vpnvrfrt.is_set or self.mplsl3vpnvrfrt.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfrt.get_name_leafdata())
                if (self.mplsl3vpnvrfrtdescr.is_set or self.mplsl3vpnvrfrtdescr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfrtdescr.get_name_leafdata())
                if (self.mplsl3vpnvrfrtrowstatus.is_set or self.mplsl3vpnvrfrtrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfrtrowstatus.get_name_leafdata())
                if (self.mplsl3vpnvrfrtstoragetype.is_set or self.mplsl3vpnvrfrtstoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfrtstoragetype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mplsL3VpnVrfName" or name == "mplsL3VpnVrfRTIndex" or name == "mplsL3VpnVrfRTType" or name == "mplsL3VpnVrfRT" or name == "mplsL3VpnVrfRTDescr" or name == "mplsL3VpnVrfRTRowStatus" or name == "mplsL3VpnVrfRTStorageType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "mplsL3VpnVrfName"):
                    self.mplsl3vpnvrfname = value
                    self.mplsl3vpnvrfname.value_namespace = name_space
                    self.mplsl3vpnvrfname.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfRTIndex"):
                    self.mplsl3vpnvrfrtindex = value
                    self.mplsl3vpnvrfrtindex.value_namespace = name_space
                    self.mplsl3vpnvrfrtindex.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfRTType"):
                    self.mplsl3vpnvrfrttype = value
                    self.mplsl3vpnvrfrttype.value_namespace = name_space
                    self.mplsl3vpnvrfrttype.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfRT"):
                    self.mplsl3vpnvrfrt = value
                    self.mplsl3vpnvrfrt.value_namespace = name_space
                    self.mplsl3vpnvrfrt.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfRTDescr"):
                    self.mplsl3vpnvrfrtdescr = value
                    self.mplsl3vpnvrfrtdescr.value_namespace = name_space
                    self.mplsl3vpnvrfrtdescr.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfRTRowStatus"):
                    self.mplsl3vpnvrfrtrowstatus = value
                    self.mplsl3vpnvrfrtrowstatus.value_namespace = name_space
                    self.mplsl3vpnvrfrtrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfRTStorageType"):
                    self.mplsl3vpnvrfrtstoragetype = value
                    self.mplsl3vpnvrfrtstoragetype.value_namespace = name_space
                    self.mplsl3vpnvrfrtstoragetype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.mplsl3vpnvrfrtentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.mplsl3vpnvrfrtentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mplsL3VpnVrfRTTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "MPLS-L3VPN-STD-MIB:MPLS-L3VPN-STD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mplsL3VpnVrfRTEntry"):
                for c in self.mplsl3vpnvrfrtentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = MplsL3VpnStdMib.Mplsl3Vpnvrfrttable.Mplsl3Vpnvrfrtentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mplsl3vpnvrfrtentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mplsL3VpnVrfRTEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Mplsl3Vpnvrfrtetable(Entity):
        """
        This table specifies per\-interface MPLS L3VPN VRF Table
        routing information.  Entries in this table define VRF routing
        entries associated with the specified MPLS/VPN interfaces.  Note
        
        that this table contains both BGP and Interior Gateway Protocol
        IGP routes, as both may appear in the same VRF.
        
        .. attribute:: mplsl3vpnvrfrteentry
        
        	An entry in this table is created by an LSR for every route present configured (either dynamically or statically) within the context of a specific VRF capable of supporting MPLS/BGP VPN.  The indexing provides an ordering of VRFs per\-VPN interface.  Implementers need to be aware that there are quite a few index objects that together can exceed the size allowed for an Object Identifier (OID).  So implementers must make sure that OIDs of column instances in this table will have no more than 128 sub\-identifiers, otherwise they cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3
        	**type**\: list of    :py:class:`Mplsl3Vpnvrfrteentry <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MplsL3VpnStdMib.Mplsl3Vpnvrfrtetable.Mplsl3Vpnvrfrteentry>`
        
        

        """

        _prefix = 'MPLS-L3VPN-STD-MIB'
        _revision = '2006-01-23'

        def __init__(self):
            super(MplsL3VpnStdMib.Mplsl3Vpnvrfrtetable, self).__init__()

            self.yang_name = "mplsL3VpnVrfRteTable"
            self.yang_parent_name = "MPLS-L3VPN-STD-MIB"

            self.mplsl3vpnvrfrteentry = YList(self)

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
                        super(MplsL3VpnStdMib.Mplsl3Vpnvrfrtetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsL3VpnStdMib.Mplsl3Vpnvrfrtetable, self).__setattr__(name, value)


        class Mplsl3Vpnvrfrteentry(Entity):
            """
            An entry in this table is created by an LSR for every route
            present configured (either dynamically or statically) within
            the context of a specific VRF capable of supporting MPLS/BGP
            VPN.  The indexing provides an ordering of VRFs per\-VPN
            interface.
            
            Implementers need to be aware that there are quite a few
            index objects that together can exceed the size allowed
            for an Object Identifier (OID).  So implementers must make
            sure that OIDs of column instances in this table will have
            no more than 128 sub\-identifiers, otherwise they cannot be
            accessed using SNMPv1, SNMPv2c, or SNMPv3.
            
            .. attribute:: mplsl3vpnvrfname  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..31
            
            	**refers to**\:  :py:class:`mplsl3vpnvrfname <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MplsL3VpnStdMib.Mplsl3Vpnvrftable.Mplsl3Vpnvrfentry>`
            
            .. attribute:: mplsl3vpnvrfrteinetcidrdesttype  <key>
            
            	The type of the mplsL3VpnVrfRteInetCidrDest address, as defined in the InetAddress MIB.  Only those address types that may appear in an actual routing table are allowed as values of this object
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: mplsl3vpnvrfrteinetcidrdest  <key>
            
            	The destination IP address of this route.  The type of this address is determined by the value of the mplsL3VpnVrfRteInetCidrDestType object.  The values for the index objects mplsL3VpnVrfRteInetCidrDest and mplsL3VpnVrfRteInetCidrPfxLen must be consistent.  When the value of mplsL3VpnVrfRteInetCidrDest is x, then the bitwise logical\-AND of x with the value of the mask formed from the corresponding index object mplsL3VpnVrfRteInetCidrPfxLen MUST be equal to x.  If not, then the index pair is not consistent and an inconsistentName error must be returned on SET or CREATE requests
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: mplsl3vpnvrfrteinetcidrpfxlen  <key>
            
            	Indicates the number of leading one bits that form the  mask to be logical\-ANDed with the destination address before being compared to the value in the mplsL3VpnVrfRteInetCidrDest field.  The values for the index objects mplsL3VpnVrfRteInetCidrDest and mplsL3VpnVrfRteInetCidrPfxLen must be consistent.  When the value of mplsL3VpnVrfRteInetCidrDest is x, then the bitwise logical\-AND of x with the value of the mask formed from the corresponding index object mplsL3VpnVrfRteInetCidrPfxLen MUST be equal to x.  If not, then the index pair is not consistent and an inconsistentName error must be returned on SET or CREATE requests
            	**type**\:  int
            
            	**range:** 0..128
            
            .. attribute:: mplsl3vpnvrfrteinetcidrpolicy  <key>
            
            	This object is an opaque object without any defined semantics.  Its purpose is to serve as an additional index that may delineate between multiple entries to the same destination.  The value { 0 0 } shall be used as the default value for this object
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: mplsl3vpnvrfrteinetcidrnhoptype  <key>
            
            	The type of the mplsL3VpnVrfRteInetCidrNextHop address, as defined in the InetAddress MIB.  Value should be set to unknown(0) for non\-remote routes.  Only those address types that may appear in an actual routing table are allowed as values of this object
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: mplsl3vpnvrfrteinetcidrnexthop  <key>
            
            	On remote routes, the address of the next system en route.  For non\-remote routes, a zero\-length string. The type of this address is determined by the value of the mplsL3VpnVrfRteInetCidrNHopType object
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: mplsl3vpnvrfrteinetcidrage
            
            	The number of seconds since this route was last updated or otherwise determined to be correct.  Note that no semantics of 'too old' can be implied except through knowledge of the routing protocol by which the route was learned
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsl3vpnvrfrteinetcidrifindex
            
            	The ifIndex value that identifies the local interface through which the next hop of this route should be reached.  A value of 0 is valid and represents the scenario where no interface is specified
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: mplsl3vpnvrfrteinetcidrmetric1
            
            	The primary routing metric for this route.  The semantics of this metric are determined by the  routing protocol specified in the route's mplsL3VpnVrfRteInetCidrProto value.  If this metric is not used, its value should be set to \-1
            	**type**\:  int
            
            	**range:** \-1..2147483647
            
            .. attribute:: mplsl3vpnvrfrteinetcidrmetric2
            
            	An alternate routing metric for this route.  The semantics of this metric are determined by the routing protocol specified in the route's mplsL3VpnVrfRteInetCidrProto value.  If this metric is not used, its value should be set to \-1
            	**type**\:  int
            
            	**range:** \-1..2147483647
            
            .. attribute:: mplsl3vpnvrfrteinetcidrmetric3
            
            	An alternate routing metric for this route.  The semantics of this metric are determined by the routing protocol specified in the route's mplsL3VpnVrfRteInetCidrProto value.  If this metric is not used, its value should be set to \-1
            	**type**\:  int
            
            	**range:** \-1..2147483647
            
            .. attribute:: mplsl3vpnvrfrteinetcidrmetric4
            
            	An alternate routing metric for this route.  The semantics of this metric are determined by the routing protocol specified in the route's mplsL3VpnVrfRteInetCidrProto value.  If this metric is not used, its value should be set to \-1
            	**type**\:  int
            
            	**range:** \-1..2147483647
            
            .. attribute:: mplsl3vpnvrfrteinetcidrmetric5
            
            	An alternate routing metric for this route.  The semantics of this metric are determined by the routing protocol specified in the route's mplsL3VpnVrfRteInetCidrProto value.  If this metric is not used, its value should be set to \-1
            	**type**\:  int
            
            	**range:** \-1..2147483647
            
            .. attribute:: mplsl3vpnvrfrteinetcidrnexthopas
            
            	The Autonomous System Number of the next hop.  The semantics of this object are determined by the routing protocol specified in the route's mplsL3VpnVrfRteInetCidrProto value.  When this object is unknown or not relevant, its value should be set to zero
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsl3vpnvrfrteinetcidrproto
            
            	The routing mechanism via which this route was learned. Inclusion of values for gateway routing protocols is not intended to imply that hosts should support those protocols
            	**type**\:   :py:class:`Ianaiprouteprotocol <ydk.models.cisco_ios_xe.IANA_RTPROTO_MIB.Ianaiprouteprotocol>`
            
            .. attribute:: mplsl3vpnvrfrteinetcidrstatus
            
            	The row status variable, used according to row installation and removal conventions.  A row entry cannot be modified when the status is marked as active(1)
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: mplsl3vpnvrfrteinetcidrtype
            
            	The type of route.  Note that local(3) refers to a route for which the next hop is the final destination; remote(4) refers to a route for which the next hop is not the final destination.  Routes that do not result in traffic forwarding or rejection should not be displayed even if the implementation keeps them stored internally.  reject(2) refers to a route that, if matched, discards the message as unreachable and returns a notification (e.g., ICMP error) to the message sender.  This is used in some protocols as a means of correctly aggregating routes.  blackhole(5) refers to a route that, if matched, discards the message silently
            	**type**\:   :py:class:`Mplsl3Vpnvrfrteinetcidrtype <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MplsL3VpnStdMib.Mplsl3Vpnvrfrtetable.Mplsl3Vpnvrfrteentry.Mplsl3Vpnvrfrteinetcidrtype>`
            
            .. attribute:: mplsl3vpnvrfrtexcpointer
            
            	Index into mplsXCTable that identifies which cross\- connect entry is associated with this VRF route entry by containing the mplsXCIndex of that cross\-connect entry. The string containing the single\-octet 0x00 indicates that a label stack is not associated with this route entry.  This can be the case because the label bindings have not yet been established, or because some change in the agent has removed them.  When the label stack associated with this VRF route is created, it MUST establish the associated cross\-connect entry in the mplsXCTable and then set that index to the value of this object.  Changes to the cross\-connect object in the mplsXCTable MUST automatically be reflected in the value of this object.  If this object represents a static routing entry, then the manager must ensure that this entry is maintained consistently in the corresponding mplsXCTable as well
            	**type**\:  str
            
            	**length:** 1..24
            
            

            """

            _prefix = 'MPLS-L3VPN-STD-MIB'
            _revision = '2006-01-23'

            def __init__(self):
                super(MplsL3VpnStdMib.Mplsl3Vpnvrfrtetable.Mplsl3Vpnvrfrteentry, self).__init__()

                self.yang_name = "mplsL3VpnVrfRteEntry"
                self.yang_parent_name = "mplsL3VpnVrfRteTable"

                self.mplsl3vpnvrfname = YLeaf(YType.str, "mplsL3VpnVrfName")

                self.mplsl3vpnvrfrteinetcidrdesttype = YLeaf(YType.enumeration, "mplsL3VpnVrfRteInetCidrDestType")

                self.mplsl3vpnvrfrteinetcidrdest = YLeaf(YType.str, "mplsL3VpnVrfRteInetCidrDest")

                self.mplsl3vpnvrfrteinetcidrpfxlen = YLeaf(YType.uint32, "mplsL3VpnVrfRteInetCidrPfxLen")

                self.mplsl3vpnvrfrteinetcidrpolicy = YLeaf(YType.str, "mplsL3VpnVrfRteInetCidrPolicy")

                self.mplsl3vpnvrfrteinetcidrnhoptype = YLeaf(YType.enumeration, "mplsL3VpnVrfRteInetCidrNHopType")

                self.mplsl3vpnvrfrteinetcidrnexthop = YLeaf(YType.str, "mplsL3VpnVrfRteInetCidrNextHop")

                self.mplsl3vpnvrfrteinetcidrage = YLeaf(YType.uint32, "mplsL3VpnVrfRteInetCidrAge")

                self.mplsl3vpnvrfrteinetcidrifindex = YLeaf(YType.int32, "mplsL3VpnVrfRteInetCidrIfIndex")

                self.mplsl3vpnvrfrteinetcidrmetric1 = YLeaf(YType.int32, "mplsL3VpnVrfRteInetCidrMetric1")

                self.mplsl3vpnvrfrteinetcidrmetric2 = YLeaf(YType.int32, "mplsL3VpnVrfRteInetCidrMetric2")

                self.mplsl3vpnvrfrteinetcidrmetric3 = YLeaf(YType.int32, "mplsL3VpnVrfRteInetCidrMetric3")

                self.mplsl3vpnvrfrteinetcidrmetric4 = YLeaf(YType.int32, "mplsL3VpnVrfRteInetCidrMetric4")

                self.mplsl3vpnvrfrteinetcidrmetric5 = YLeaf(YType.int32, "mplsL3VpnVrfRteInetCidrMetric5")

                self.mplsl3vpnvrfrteinetcidrnexthopas = YLeaf(YType.uint32, "mplsL3VpnVrfRteInetCidrNextHopAS")

                self.mplsl3vpnvrfrteinetcidrproto = YLeaf(YType.enumeration, "mplsL3VpnVrfRteInetCidrProto")

                self.mplsl3vpnvrfrteinetcidrstatus = YLeaf(YType.enumeration, "mplsL3VpnVrfRteInetCidrStatus")

                self.mplsl3vpnvrfrteinetcidrtype = YLeaf(YType.enumeration, "mplsL3VpnVrfRteInetCidrType")

                self.mplsl3vpnvrfrtexcpointer = YLeaf(YType.str, "mplsL3VpnVrfRteXCPointer")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("mplsl3vpnvrfname",
                                "mplsl3vpnvrfrteinetcidrdesttype",
                                "mplsl3vpnvrfrteinetcidrdest",
                                "mplsl3vpnvrfrteinetcidrpfxlen",
                                "mplsl3vpnvrfrteinetcidrpolicy",
                                "mplsl3vpnvrfrteinetcidrnhoptype",
                                "mplsl3vpnvrfrteinetcidrnexthop",
                                "mplsl3vpnvrfrteinetcidrage",
                                "mplsl3vpnvrfrteinetcidrifindex",
                                "mplsl3vpnvrfrteinetcidrmetric1",
                                "mplsl3vpnvrfrteinetcidrmetric2",
                                "mplsl3vpnvrfrteinetcidrmetric3",
                                "mplsl3vpnvrfrteinetcidrmetric4",
                                "mplsl3vpnvrfrteinetcidrmetric5",
                                "mplsl3vpnvrfrteinetcidrnexthopas",
                                "mplsl3vpnvrfrteinetcidrproto",
                                "mplsl3vpnvrfrteinetcidrstatus",
                                "mplsl3vpnvrfrteinetcidrtype",
                                "mplsl3vpnvrfrtexcpointer") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsL3VpnStdMib.Mplsl3Vpnvrfrtetable.Mplsl3Vpnvrfrteentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsL3VpnStdMib.Mplsl3Vpnvrfrtetable.Mplsl3Vpnvrfrteentry, self).__setattr__(name, value)

            class Mplsl3Vpnvrfrteinetcidrtype(Enum):
                """
                Mplsl3Vpnvrfrteinetcidrtype

                The type of route.  Note that local(3) refers to a

                route for which the next hop is the final destination;

                remote(4) refers to a route for which the next hop is

                not the final destination.

                Routes that do not result in traffic forwarding or

                rejection should not be displayed even if the

                implementation keeps them stored internally.

                reject(2) refers to a route that, if matched, discards

                the message as unreachable and returns a notification

                (e.g., ICMP error) to the message sender.  This is used

                in some protocols as a means of correctly aggregating

                routes.

                blackhole(5) refers to a route that, if matched,

                discards the message silently.

                .. data:: other = 1

                .. data:: reject = 2

                .. data:: local = 3

                .. data:: remote = 4

                .. data:: blackhole = 5

                """

                other = Enum.YLeaf(1, "other")

                reject = Enum.YLeaf(2, "reject")

                local = Enum.YLeaf(3, "local")

                remote = Enum.YLeaf(4, "remote")

                blackhole = Enum.YLeaf(5, "blackhole")


            def has_data(self):
                return (
                    self.mplsl3vpnvrfname.is_set or
                    self.mplsl3vpnvrfrteinetcidrdesttype.is_set or
                    self.mplsl3vpnvrfrteinetcidrdest.is_set or
                    self.mplsl3vpnvrfrteinetcidrpfxlen.is_set or
                    self.mplsl3vpnvrfrteinetcidrpolicy.is_set or
                    self.mplsl3vpnvrfrteinetcidrnhoptype.is_set or
                    self.mplsl3vpnvrfrteinetcidrnexthop.is_set or
                    self.mplsl3vpnvrfrteinetcidrage.is_set or
                    self.mplsl3vpnvrfrteinetcidrifindex.is_set or
                    self.mplsl3vpnvrfrteinetcidrmetric1.is_set or
                    self.mplsl3vpnvrfrteinetcidrmetric2.is_set or
                    self.mplsl3vpnvrfrteinetcidrmetric3.is_set or
                    self.mplsl3vpnvrfrteinetcidrmetric4.is_set or
                    self.mplsl3vpnvrfrteinetcidrmetric5.is_set or
                    self.mplsl3vpnvrfrteinetcidrnexthopas.is_set or
                    self.mplsl3vpnvrfrteinetcidrproto.is_set or
                    self.mplsl3vpnvrfrteinetcidrstatus.is_set or
                    self.mplsl3vpnvrfrteinetcidrtype.is_set or
                    self.mplsl3vpnvrfrtexcpointer.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfname.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfrteinetcidrdesttype.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfrteinetcidrdest.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfrteinetcidrpfxlen.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfrteinetcidrpolicy.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfrteinetcidrnhoptype.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfrteinetcidrnexthop.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfrteinetcidrage.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfrteinetcidrifindex.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfrteinetcidrmetric1.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfrteinetcidrmetric2.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfrteinetcidrmetric3.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfrteinetcidrmetric4.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfrteinetcidrmetric5.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfrteinetcidrnexthopas.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfrteinetcidrproto.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfrteinetcidrstatus.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfrteinetcidrtype.yfilter != YFilter.not_set or
                    self.mplsl3vpnvrfrtexcpointer.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mplsL3VpnVrfRteEntry" + "[mplsL3VpnVrfName='" + self.mplsl3vpnvrfname.get() + "']" + "[mplsL3VpnVrfRteInetCidrDestType='" + self.mplsl3vpnvrfrteinetcidrdesttype.get() + "']" + "[mplsL3VpnVrfRteInetCidrDest='" + self.mplsl3vpnvrfrteinetcidrdest.get() + "']" + "[mplsL3VpnVrfRteInetCidrPfxLen='" + self.mplsl3vpnvrfrteinetcidrpfxlen.get() + "']" + "[mplsL3VpnVrfRteInetCidrPolicy='" + self.mplsl3vpnvrfrteinetcidrpolicy.get() + "']" + "[mplsL3VpnVrfRteInetCidrNHopType='" + self.mplsl3vpnvrfrteinetcidrnhoptype.get() + "']" + "[mplsL3VpnVrfRteInetCidrNextHop='" + self.mplsl3vpnvrfrteinetcidrnexthop.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "MPLS-L3VPN-STD-MIB:MPLS-L3VPN-STD-MIB/mplsL3VpnVrfRteTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.mplsl3vpnvrfname.is_set or self.mplsl3vpnvrfname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfname.get_name_leafdata())
                if (self.mplsl3vpnvrfrteinetcidrdesttype.is_set or self.mplsl3vpnvrfrteinetcidrdesttype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfrteinetcidrdesttype.get_name_leafdata())
                if (self.mplsl3vpnvrfrteinetcidrdest.is_set or self.mplsl3vpnvrfrteinetcidrdest.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfrteinetcidrdest.get_name_leafdata())
                if (self.mplsl3vpnvrfrteinetcidrpfxlen.is_set or self.mplsl3vpnvrfrteinetcidrpfxlen.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfrteinetcidrpfxlen.get_name_leafdata())
                if (self.mplsl3vpnvrfrteinetcidrpolicy.is_set or self.mplsl3vpnvrfrteinetcidrpolicy.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfrteinetcidrpolicy.get_name_leafdata())
                if (self.mplsl3vpnvrfrteinetcidrnhoptype.is_set or self.mplsl3vpnvrfrteinetcidrnhoptype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfrteinetcidrnhoptype.get_name_leafdata())
                if (self.mplsl3vpnvrfrteinetcidrnexthop.is_set or self.mplsl3vpnvrfrteinetcidrnexthop.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfrteinetcidrnexthop.get_name_leafdata())
                if (self.mplsl3vpnvrfrteinetcidrage.is_set or self.mplsl3vpnvrfrteinetcidrage.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfrteinetcidrage.get_name_leafdata())
                if (self.mplsl3vpnvrfrteinetcidrifindex.is_set or self.mplsl3vpnvrfrteinetcidrifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfrteinetcidrifindex.get_name_leafdata())
                if (self.mplsl3vpnvrfrteinetcidrmetric1.is_set or self.mplsl3vpnvrfrteinetcidrmetric1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfrteinetcidrmetric1.get_name_leafdata())
                if (self.mplsl3vpnvrfrteinetcidrmetric2.is_set or self.mplsl3vpnvrfrteinetcidrmetric2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfrteinetcidrmetric2.get_name_leafdata())
                if (self.mplsl3vpnvrfrteinetcidrmetric3.is_set or self.mplsl3vpnvrfrteinetcidrmetric3.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfrteinetcidrmetric3.get_name_leafdata())
                if (self.mplsl3vpnvrfrteinetcidrmetric4.is_set or self.mplsl3vpnvrfrteinetcidrmetric4.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfrteinetcidrmetric4.get_name_leafdata())
                if (self.mplsl3vpnvrfrteinetcidrmetric5.is_set or self.mplsl3vpnvrfrteinetcidrmetric5.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfrteinetcidrmetric5.get_name_leafdata())
                if (self.mplsl3vpnvrfrteinetcidrnexthopas.is_set or self.mplsl3vpnvrfrteinetcidrnexthopas.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfrteinetcidrnexthopas.get_name_leafdata())
                if (self.mplsl3vpnvrfrteinetcidrproto.is_set or self.mplsl3vpnvrfrteinetcidrproto.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfrteinetcidrproto.get_name_leafdata())
                if (self.mplsl3vpnvrfrteinetcidrstatus.is_set or self.mplsl3vpnvrfrteinetcidrstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfrteinetcidrstatus.get_name_leafdata())
                if (self.mplsl3vpnvrfrteinetcidrtype.is_set or self.mplsl3vpnvrfrteinetcidrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfrteinetcidrtype.get_name_leafdata())
                if (self.mplsl3vpnvrfrtexcpointer.is_set or self.mplsl3vpnvrfrtexcpointer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsl3vpnvrfrtexcpointer.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mplsL3VpnVrfName" or name == "mplsL3VpnVrfRteInetCidrDestType" or name == "mplsL3VpnVrfRteInetCidrDest" or name == "mplsL3VpnVrfRteInetCidrPfxLen" or name == "mplsL3VpnVrfRteInetCidrPolicy" or name == "mplsL3VpnVrfRteInetCidrNHopType" or name == "mplsL3VpnVrfRteInetCidrNextHop" or name == "mplsL3VpnVrfRteInetCidrAge" or name == "mplsL3VpnVrfRteInetCidrIfIndex" or name == "mplsL3VpnVrfRteInetCidrMetric1" or name == "mplsL3VpnVrfRteInetCidrMetric2" or name == "mplsL3VpnVrfRteInetCidrMetric3" or name == "mplsL3VpnVrfRteInetCidrMetric4" or name == "mplsL3VpnVrfRteInetCidrMetric5" or name == "mplsL3VpnVrfRteInetCidrNextHopAS" or name == "mplsL3VpnVrfRteInetCidrProto" or name == "mplsL3VpnVrfRteInetCidrStatus" or name == "mplsL3VpnVrfRteInetCidrType" or name == "mplsL3VpnVrfRteXCPointer"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "mplsL3VpnVrfName"):
                    self.mplsl3vpnvrfname = value
                    self.mplsl3vpnvrfname.value_namespace = name_space
                    self.mplsl3vpnvrfname.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfRteInetCidrDestType"):
                    self.mplsl3vpnvrfrteinetcidrdesttype = value
                    self.mplsl3vpnvrfrteinetcidrdesttype.value_namespace = name_space
                    self.mplsl3vpnvrfrteinetcidrdesttype.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfRteInetCidrDest"):
                    self.mplsl3vpnvrfrteinetcidrdest = value
                    self.mplsl3vpnvrfrteinetcidrdest.value_namespace = name_space
                    self.mplsl3vpnvrfrteinetcidrdest.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfRteInetCidrPfxLen"):
                    self.mplsl3vpnvrfrteinetcidrpfxlen = value
                    self.mplsl3vpnvrfrteinetcidrpfxlen.value_namespace = name_space
                    self.mplsl3vpnvrfrteinetcidrpfxlen.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfRteInetCidrPolicy"):
                    self.mplsl3vpnvrfrteinetcidrpolicy = value
                    self.mplsl3vpnvrfrteinetcidrpolicy.value_namespace = name_space
                    self.mplsl3vpnvrfrteinetcidrpolicy.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfRteInetCidrNHopType"):
                    self.mplsl3vpnvrfrteinetcidrnhoptype = value
                    self.mplsl3vpnvrfrteinetcidrnhoptype.value_namespace = name_space
                    self.mplsl3vpnvrfrteinetcidrnhoptype.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfRteInetCidrNextHop"):
                    self.mplsl3vpnvrfrteinetcidrnexthop = value
                    self.mplsl3vpnvrfrteinetcidrnexthop.value_namespace = name_space
                    self.mplsl3vpnvrfrteinetcidrnexthop.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfRteInetCidrAge"):
                    self.mplsl3vpnvrfrteinetcidrage = value
                    self.mplsl3vpnvrfrteinetcidrage.value_namespace = name_space
                    self.mplsl3vpnvrfrteinetcidrage.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfRteInetCidrIfIndex"):
                    self.mplsl3vpnvrfrteinetcidrifindex = value
                    self.mplsl3vpnvrfrteinetcidrifindex.value_namespace = name_space
                    self.mplsl3vpnvrfrteinetcidrifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfRteInetCidrMetric1"):
                    self.mplsl3vpnvrfrteinetcidrmetric1 = value
                    self.mplsl3vpnvrfrteinetcidrmetric1.value_namespace = name_space
                    self.mplsl3vpnvrfrteinetcidrmetric1.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfRteInetCidrMetric2"):
                    self.mplsl3vpnvrfrteinetcidrmetric2 = value
                    self.mplsl3vpnvrfrteinetcidrmetric2.value_namespace = name_space
                    self.mplsl3vpnvrfrteinetcidrmetric2.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfRteInetCidrMetric3"):
                    self.mplsl3vpnvrfrteinetcidrmetric3 = value
                    self.mplsl3vpnvrfrteinetcidrmetric3.value_namespace = name_space
                    self.mplsl3vpnvrfrteinetcidrmetric3.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfRteInetCidrMetric4"):
                    self.mplsl3vpnvrfrteinetcidrmetric4 = value
                    self.mplsl3vpnvrfrteinetcidrmetric4.value_namespace = name_space
                    self.mplsl3vpnvrfrteinetcidrmetric4.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfRteInetCidrMetric5"):
                    self.mplsl3vpnvrfrteinetcidrmetric5 = value
                    self.mplsl3vpnvrfrteinetcidrmetric5.value_namespace = name_space
                    self.mplsl3vpnvrfrteinetcidrmetric5.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfRteInetCidrNextHopAS"):
                    self.mplsl3vpnvrfrteinetcidrnexthopas = value
                    self.mplsl3vpnvrfrteinetcidrnexthopas.value_namespace = name_space
                    self.mplsl3vpnvrfrteinetcidrnexthopas.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfRteInetCidrProto"):
                    self.mplsl3vpnvrfrteinetcidrproto = value
                    self.mplsl3vpnvrfrteinetcidrproto.value_namespace = name_space
                    self.mplsl3vpnvrfrteinetcidrproto.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfRteInetCidrStatus"):
                    self.mplsl3vpnvrfrteinetcidrstatus = value
                    self.mplsl3vpnvrfrteinetcidrstatus.value_namespace = name_space
                    self.mplsl3vpnvrfrteinetcidrstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfRteInetCidrType"):
                    self.mplsl3vpnvrfrteinetcidrtype = value
                    self.mplsl3vpnvrfrteinetcidrtype.value_namespace = name_space
                    self.mplsl3vpnvrfrteinetcidrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsL3VpnVrfRteXCPointer"):
                    self.mplsl3vpnvrfrtexcpointer = value
                    self.mplsl3vpnvrfrtexcpointer.value_namespace = name_space
                    self.mplsl3vpnvrfrtexcpointer.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.mplsl3vpnvrfrteentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.mplsl3vpnvrfrteentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mplsL3VpnVrfRteTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "MPLS-L3VPN-STD-MIB:MPLS-L3VPN-STD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mplsL3VpnVrfRteEntry"):
                for c in self.mplsl3vpnvrfrteentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = MplsL3VpnStdMib.Mplsl3Vpnvrfrtetable.Mplsl3Vpnvrfrteentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mplsl3vpnvrfrteentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mplsL3VpnVrfRteEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.mplsl3vpnifconftable is not None and self.mplsl3vpnifconftable.has_data()) or
            (self.mplsl3vpnscalars is not None and self.mplsl3vpnscalars.has_data()) or
            (self.mplsl3vpnvrfrtetable is not None and self.mplsl3vpnvrfrtetable.has_data()) or
            (self.mplsl3vpnvrfrttable is not None and self.mplsl3vpnvrfrttable.has_data()) or
            (self.mplsl3vpnvrftable is not None and self.mplsl3vpnvrftable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.mplsl3vpnifconftable is not None and self.mplsl3vpnifconftable.has_operation()) or
            (self.mplsl3vpnscalars is not None and self.mplsl3vpnscalars.has_operation()) or
            (self.mplsl3vpnvrfrtetable is not None and self.mplsl3vpnvrfrtetable.has_operation()) or
            (self.mplsl3vpnvrfrttable is not None and self.mplsl3vpnvrfrttable.has_operation()) or
            (self.mplsl3vpnvrftable is not None and self.mplsl3vpnvrftable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "MPLS-L3VPN-STD-MIB:MPLS-L3VPN-STD-MIB" + path_buffer

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

        if (child_yang_name == "mplsL3VpnIfConfTable"):
            if (self.mplsl3vpnifconftable is None):
                self.mplsl3vpnifconftable = MplsL3VpnStdMib.Mplsl3Vpnifconftable()
                self.mplsl3vpnifconftable.parent = self
                self._children_name_map["mplsl3vpnifconftable"] = "mplsL3VpnIfConfTable"
            return self.mplsl3vpnifconftable

        if (child_yang_name == "mplsL3VpnScalars"):
            if (self.mplsl3vpnscalars is None):
                self.mplsl3vpnscalars = MplsL3VpnStdMib.Mplsl3Vpnscalars()
                self.mplsl3vpnscalars.parent = self
                self._children_name_map["mplsl3vpnscalars"] = "mplsL3VpnScalars"
            return self.mplsl3vpnscalars

        if (child_yang_name == "mplsL3VpnVrfRteTable"):
            if (self.mplsl3vpnvrfrtetable is None):
                self.mplsl3vpnvrfrtetable = MplsL3VpnStdMib.Mplsl3Vpnvrfrtetable()
                self.mplsl3vpnvrfrtetable.parent = self
                self._children_name_map["mplsl3vpnvrfrtetable"] = "mplsL3VpnVrfRteTable"
            return self.mplsl3vpnvrfrtetable

        if (child_yang_name == "mplsL3VpnVrfRTTable"):
            if (self.mplsl3vpnvrfrttable is None):
                self.mplsl3vpnvrfrttable = MplsL3VpnStdMib.Mplsl3Vpnvrfrttable()
                self.mplsl3vpnvrfrttable.parent = self
                self._children_name_map["mplsl3vpnvrfrttable"] = "mplsL3VpnVrfRTTable"
            return self.mplsl3vpnvrfrttable

        if (child_yang_name == "mplsL3VpnVrfTable"):
            if (self.mplsl3vpnvrftable is None):
                self.mplsl3vpnvrftable = MplsL3VpnStdMib.Mplsl3Vpnvrftable()
                self.mplsl3vpnvrftable.parent = self
                self._children_name_map["mplsl3vpnvrftable"] = "mplsL3VpnVrfTable"
            return self.mplsl3vpnvrftable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "mplsL3VpnIfConfTable" or name == "mplsL3VpnScalars" or name == "mplsL3VpnVrfRteTable" or name == "mplsL3VpnVrfRTTable" or name == "mplsL3VpnVrfTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = MplsL3VpnStdMib()
        return self._top_entity


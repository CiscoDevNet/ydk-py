""" MPLS_VPN_MIB 

This MIB contains managed object definitions for the
Multiprotocol Label Switching (MPLS)/Border Gateway


Protocol (BGP) Virtual Private Networks (VPNs) as
defined in \: Rosen, E., Viswanathan, A., and R.
Callon, Multiprotocol Label Switching Architecture,
RFC3031, January 2001.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class MplsVpnMib(Entity):
    """
    
    
    .. attribute:: mplsvpninterfaceconftable
    
    	This table specifies per\-interface MPLS capability and associated information
    	**type**\:   :py:class:`Mplsvpninterfaceconftable <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpninterfaceconftable>`
    
    .. attribute:: mplsvpnscalars
    
    	
    	**type**\:   :py:class:`Mplsvpnscalars <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnscalars>`
    
    .. attribute:: mplsvpnvrfbgpnbraddrtable
    
    	Each entry in this table specifies a per\-interface  MPLS/EBGP neighbor
    	**type**\:   :py:class:`Mplsvpnvrfbgpnbraddrtable <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrfbgpnbraddrtable>`
    
    .. attribute:: mplsvpnvrfbgpnbrprefixtable
    
    	This table specifies per\-VRF vpnv4 multi\-protocol prefixes supported by BGP
    	**type**\:   :py:class:`Mplsvpnvrfbgpnbrprefixtable <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrfbgpnbrprefixtable>`
    
    .. attribute:: mplsvpnvrfroutetable
    
    	This table specifies per\-interface MPLS/BGP VPN VRF Table routing information. Entries in this table define VRF routing entries associated with the specified MPLS/VPN interfaces. Note that this table contains both BGP and IGP routes, as both may appear in the same VRF
    	**type**\:   :py:class:`Mplsvpnvrfroutetable <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrfroutetable>`
    
    .. attribute:: mplsvpnvrfroutetargettable
    
    	This table specifies per\-VRF route target association. Each entry identifies a connectivity policy supported as part of a VPN
    	**type**\:   :py:class:`Mplsvpnvrfroutetargettable <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrfroutetargettable>`
    
    .. attribute:: mplsvpnvrftable
    
    	This table specifies per\-interface MPLS/BGP VPN VRF Table capability and associated information. Entries in this table define VRF routing instances associated with MPLS/VPN interfaces. Note that multiple interfaces can belong to the same VRF instance. The collection of all VRF instances comprises an actual VPN
    	**type**\:   :py:class:`Mplsvpnvrftable <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrftable>`
    
    

    """

    _prefix = 'MPLS-VPN-MIB'
    _revision = '2001-10-15'

    def __init__(self):
        super(MplsVpnMib, self).__init__()
        self._top_entity = None

        self.yang_name = "MPLS-VPN-MIB"
        self.yang_parent_name = "MPLS-VPN-MIB"

        self.mplsvpninterfaceconftable = MplsVpnMib.Mplsvpninterfaceconftable()
        self.mplsvpninterfaceconftable.parent = self
        self._children_name_map["mplsvpninterfaceconftable"] = "mplsVpnInterfaceConfTable"
        self._children_yang_names.add("mplsVpnInterfaceConfTable")

        self.mplsvpnscalars = MplsVpnMib.Mplsvpnscalars()
        self.mplsvpnscalars.parent = self
        self._children_name_map["mplsvpnscalars"] = "mplsVpnScalars"
        self._children_yang_names.add("mplsVpnScalars")

        self.mplsvpnvrfbgpnbraddrtable = MplsVpnMib.Mplsvpnvrfbgpnbraddrtable()
        self.mplsvpnvrfbgpnbraddrtable.parent = self
        self._children_name_map["mplsvpnvrfbgpnbraddrtable"] = "mplsVpnVrfBgpNbrAddrTable"
        self._children_yang_names.add("mplsVpnVrfBgpNbrAddrTable")

        self.mplsvpnvrfbgpnbrprefixtable = MplsVpnMib.Mplsvpnvrfbgpnbrprefixtable()
        self.mplsvpnvrfbgpnbrprefixtable.parent = self
        self._children_name_map["mplsvpnvrfbgpnbrprefixtable"] = "mplsVpnVrfBgpNbrPrefixTable"
        self._children_yang_names.add("mplsVpnVrfBgpNbrPrefixTable")

        self.mplsvpnvrfroutetable = MplsVpnMib.Mplsvpnvrfroutetable()
        self.mplsvpnvrfroutetable.parent = self
        self._children_name_map["mplsvpnvrfroutetable"] = "mplsVpnVrfRouteTable"
        self._children_yang_names.add("mplsVpnVrfRouteTable")

        self.mplsvpnvrfroutetargettable = MplsVpnMib.Mplsvpnvrfroutetargettable()
        self.mplsvpnvrfroutetargettable.parent = self
        self._children_name_map["mplsvpnvrfroutetargettable"] = "mplsVpnVrfRouteTargetTable"
        self._children_yang_names.add("mplsVpnVrfRouteTargetTable")

        self.mplsvpnvrftable = MplsVpnMib.Mplsvpnvrftable()
        self.mplsvpnvrftable.parent = self
        self._children_name_map["mplsvpnvrftable"] = "mplsVpnVrfTable"
        self._children_yang_names.add("mplsVpnVrfTable")


    class Mplsvpnscalars(Entity):
        """
        
        
        .. attribute:: mplsvpnactivevrfs
        
        	The number of VRFs which are active on this node. That is, those VRFs whose corresponding mplsVpnVrfOperStatus  object value is equal to operational (1)
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: mplsvpnconfiguredvrfs
        
        	The number of VRFs which are configured on this node
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: mplsvpnconnectedinterfaces
        
        	Total number of interfaces connected to a VRF
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: mplsvpnnotificationenable
        
        	If this object is true, then it enables the generation of all notifications defined in  this MIB
        	**type**\:  bool
        
        .. attribute:: mplsvpnvrfconfmaxpossibleroutes
        
        	Denotes maximum number of routes which the device will allow all VRFs jointly to hold. If this value is set to 0, this indicates that the device is  unable to determine the absolute maximum. In this case, the configured maximum MAY not actually be allowed by the device
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'MPLS-VPN-MIB'
        _revision = '2001-10-15'

        def __init__(self):
            super(MplsVpnMib.Mplsvpnscalars, self).__init__()

            self.yang_name = "mplsVpnScalars"
            self.yang_parent_name = "MPLS-VPN-MIB"

            self.mplsvpnactivevrfs = YLeaf(YType.uint32, "mplsVpnActiveVrfs")

            self.mplsvpnconfiguredvrfs = YLeaf(YType.uint32, "mplsVpnConfiguredVrfs")

            self.mplsvpnconnectedinterfaces = YLeaf(YType.uint32, "mplsVpnConnectedInterfaces")

            self.mplsvpnnotificationenable = YLeaf(YType.boolean, "mplsVpnNotificationEnable")

            self.mplsvpnvrfconfmaxpossibleroutes = YLeaf(YType.uint32, "mplsVpnVrfConfMaxPossibleRoutes")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("mplsvpnactivevrfs",
                            "mplsvpnconfiguredvrfs",
                            "mplsvpnconnectedinterfaces",
                            "mplsvpnnotificationenable",
                            "mplsvpnvrfconfmaxpossibleroutes") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(MplsVpnMib.Mplsvpnscalars, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsVpnMib.Mplsvpnscalars, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.mplsvpnactivevrfs.is_set or
                self.mplsvpnconfiguredvrfs.is_set or
                self.mplsvpnconnectedinterfaces.is_set or
                self.mplsvpnnotificationenable.is_set or
                self.mplsvpnvrfconfmaxpossibleroutes.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.mplsvpnactivevrfs.yfilter != YFilter.not_set or
                self.mplsvpnconfiguredvrfs.yfilter != YFilter.not_set or
                self.mplsvpnconnectedinterfaces.yfilter != YFilter.not_set or
                self.mplsvpnnotificationenable.yfilter != YFilter.not_set or
                self.mplsvpnvrfconfmaxpossibleroutes.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mplsVpnScalars" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "MPLS-VPN-MIB:MPLS-VPN-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.mplsvpnactivevrfs.is_set or self.mplsvpnactivevrfs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mplsvpnactivevrfs.get_name_leafdata())
            if (self.mplsvpnconfiguredvrfs.is_set or self.mplsvpnconfiguredvrfs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mplsvpnconfiguredvrfs.get_name_leafdata())
            if (self.mplsvpnconnectedinterfaces.is_set or self.mplsvpnconnectedinterfaces.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mplsvpnconnectedinterfaces.get_name_leafdata())
            if (self.mplsvpnnotificationenable.is_set or self.mplsvpnnotificationenable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mplsvpnnotificationenable.get_name_leafdata())
            if (self.mplsvpnvrfconfmaxpossibleroutes.is_set or self.mplsvpnvrfconfmaxpossibleroutes.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mplsvpnvrfconfmaxpossibleroutes.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mplsVpnActiveVrfs" or name == "mplsVpnConfiguredVrfs" or name == "mplsVpnConnectedInterfaces" or name == "mplsVpnNotificationEnable" or name == "mplsVpnVrfConfMaxPossibleRoutes"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "mplsVpnActiveVrfs"):
                self.mplsvpnactivevrfs = value
                self.mplsvpnactivevrfs.value_namespace = name_space
                self.mplsvpnactivevrfs.value_namespace_prefix = name_space_prefix
            if(value_path == "mplsVpnConfiguredVrfs"):
                self.mplsvpnconfiguredvrfs = value
                self.mplsvpnconfiguredvrfs.value_namespace = name_space
                self.mplsvpnconfiguredvrfs.value_namespace_prefix = name_space_prefix
            if(value_path == "mplsVpnConnectedInterfaces"):
                self.mplsvpnconnectedinterfaces = value
                self.mplsvpnconnectedinterfaces.value_namespace = name_space
                self.mplsvpnconnectedinterfaces.value_namespace_prefix = name_space_prefix
            if(value_path == "mplsVpnNotificationEnable"):
                self.mplsvpnnotificationenable = value
                self.mplsvpnnotificationenable.value_namespace = name_space
                self.mplsvpnnotificationenable.value_namespace_prefix = name_space_prefix
            if(value_path == "mplsVpnVrfConfMaxPossibleRoutes"):
                self.mplsvpnvrfconfmaxpossibleroutes = value
                self.mplsvpnvrfconfmaxpossibleroutes.value_namespace = name_space
                self.mplsvpnvrfconfmaxpossibleroutes.value_namespace_prefix = name_space_prefix


    class Mplsvpninterfaceconftable(Entity):
        """
        This table specifies per\-interface MPLS capability
        and associated information.
        
        .. attribute:: mplsvpninterfaceconfentry
        
        	An entry in this table is created by an LSR for every interface capable of supporting MPLS/BGP VPN.   Each entry in this table is meant to correspond to an entry in the Interfaces Table
        	**type**\: list of    :py:class:`Mplsvpninterfaceconfentry <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpninterfaceconftable.Mplsvpninterfaceconfentry>`
        
        

        """

        _prefix = 'MPLS-VPN-MIB'
        _revision = '2001-10-15'

        def __init__(self):
            super(MplsVpnMib.Mplsvpninterfaceconftable, self).__init__()

            self.yang_name = "mplsVpnInterfaceConfTable"
            self.yang_parent_name = "MPLS-VPN-MIB"

            self.mplsvpninterfaceconfentry = YList(self)

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
                        super(MplsVpnMib.Mplsvpninterfaceconftable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsVpnMib.Mplsvpninterfaceconftable, self).__setattr__(name, value)


        class Mplsvpninterfaceconfentry(Entity):
            """
            An entry in this table is created by an LSR for
            every interface capable of supporting MPLS/BGP VPN.
            
            
            Each entry in this table is meant to correspond to
            an entry in the Interfaces Table.
            
            .. attribute:: mplsvpnvrfname  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..31
            
            	**refers to**\:  :py:class:`mplsvpnvrfname <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrftable.Mplsvpnvrfentry>`
            
            .. attribute:: mplsvpninterfaceconfindex  <key>
            
            	This is a unique index for an entry in the MplsVPNInterfaceConfTable. A non\-zero index for an entry indicates the ifIndex for the corresponding interface entry in the MPLS\-VPN\-layer in the ifTable. Note that this table does not necessarily correspond one\-to\-one with all entries in the Interface MIB having an ifType of MPLS\-layer; rather, only those which are enabled for MPLS/BGP VPN functionality
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: mplsvpninterfaceconfrowstatus
            
            	The row status for this entry. This value is used to create a row in this table, signifying that the specified interface is to be associated with the specified interface. If this operation succeeds, the interface will have been associated, otherwise the agent would not allow the association.  If the agent only allows read\-only operations on this table, it will create entries in this table as they are created
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: mplsvpninterfaceconfstoragetype
            
            	The storage type for this entry
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            .. attribute:: mplsvpninterfacelabeledgetype
            
            	Either the providerEdge(0) (PE) or customerEdge(1) (CE) bit MUST be set
            	**type**\:   :py:class:`Mplsvpninterfacelabeledgetype <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpninterfaceconftable.Mplsvpninterfaceconfentry.Mplsvpninterfacelabeledgetype>`
            
            .. attribute:: mplsvpninterfacevpnclassification
            
            	Denotes whether this link participates in a carrier\-of\-carrier's, enterprise, or inter\-provider scenario
            	**type**\:   :py:class:`Mplsvpninterfacevpnclassification <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpninterfaceconftable.Mplsvpninterfaceconfentry.Mplsvpninterfacevpnclassification>`
            
            .. attribute:: mplsvpninterfacevpnroutedistprotocol
            
            	Denotes the route distribution protocol across the PE\-CE link. Note that more than one routing protocol may be enabled at the same time
            	**type**\:   :py:class:`Mplsvpninterfacevpnroutedistprotocol <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpninterfaceconftable.Mplsvpninterfaceconfentry.Mplsvpninterfacevpnroutedistprotocol>`
            
            

            """

            _prefix = 'MPLS-VPN-MIB'
            _revision = '2001-10-15'

            def __init__(self):
                super(MplsVpnMib.Mplsvpninterfaceconftable.Mplsvpninterfaceconfentry, self).__init__()

                self.yang_name = "mplsVpnInterfaceConfEntry"
                self.yang_parent_name = "mplsVpnInterfaceConfTable"

                self.mplsvpnvrfname = YLeaf(YType.str, "mplsVpnVrfName")

                self.mplsvpninterfaceconfindex = YLeaf(YType.int32, "mplsVpnInterfaceConfIndex")

                self.mplsvpninterfaceconfrowstatus = YLeaf(YType.enumeration, "mplsVpnInterfaceConfRowStatus")

                self.mplsvpninterfaceconfstoragetype = YLeaf(YType.enumeration, "mplsVpnInterfaceConfStorageType")

                self.mplsvpninterfacelabeledgetype = YLeaf(YType.enumeration, "mplsVpnInterfaceLabelEdgeType")

                self.mplsvpninterfacevpnclassification = YLeaf(YType.enumeration, "mplsVpnInterfaceVpnClassification")

                self.mplsvpninterfacevpnroutedistprotocol = YLeaf(YType.bits, "mplsVpnInterfaceVpnRouteDistProtocol")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("mplsvpnvrfname",
                                "mplsvpninterfaceconfindex",
                                "mplsvpninterfaceconfrowstatus",
                                "mplsvpninterfaceconfstoragetype",
                                "mplsvpninterfacelabeledgetype",
                                "mplsvpninterfacevpnclassification",
                                "mplsvpninterfacevpnroutedistprotocol") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsVpnMib.Mplsvpninterfaceconftable.Mplsvpninterfaceconfentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsVpnMib.Mplsvpninterfaceconftable.Mplsvpninterfaceconfentry, self).__setattr__(name, value)

            class Mplsvpninterfacelabeledgetype(Enum):
                """
                Mplsvpninterfacelabeledgetype

                Either the providerEdge(0) (PE) or customerEdge(1)

                (CE) bit MUST be set.

                .. data:: providerEdge = 1

                .. data:: customerEdge = 2

                """

                providerEdge = Enum.YLeaf(1, "providerEdge")

                customerEdge = Enum.YLeaf(2, "customerEdge")


            class Mplsvpninterfacevpnclassification(Enum):
                """
                Mplsvpninterfacevpnclassification

                Denotes whether this link participates in a

                carrier\-of\-carrier's, enterprise, or inter\-provider

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
                    self.mplsvpnvrfname.is_set or
                    self.mplsvpninterfaceconfindex.is_set or
                    self.mplsvpninterfaceconfrowstatus.is_set or
                    self.mplsvpninterfaceconfstoragetype.is_set or
                    self.mplsvpninterfacelabeledgetype.is_set or
                    self.mplsvpninterfacevpnclassification.is_set or
                    self.mplsvpninterfacevpnroutedistprotocol.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mplsvpnvrfname.yfilter != YFilter.not_set or
                    self.mplsvpninterfaceconfindex.yfilter != YFilter.not_set or
                    self.mplsvpninterfaceconfrowstatus.yfilter != YFilter.not_set or
                    self.mplsvpninterfaceconfstoragetype.yfilter != YFilter.not_set or
                    self.mplsvpninterfacelabeledgetype.yfilter != YFilter.not_set or
                    self.mplsvpninterfacevpnclassification.yfilter != YFilter.not_set or
                    self.mplsvpninterfacevpnroutedistprotocol.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mplsVpnInterfaceConfEntry" + "[mplsVpnVrfName='" + self.mplsvpnvrfname.get() + "']" + "[mplsVpnInterfaceConfIndex='" + self.mplsvpninterfaceconfindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "MPLS-VPN-MIB:MPLS-VPN-MIB/mplsVpnInterfaceConfTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.mplsvpnvrfname.is_set or self.mplsvpnvrfname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfname.get_name_leafdata())
                if (self.mplsvpninterfaceconfindex.is_set or self.mplsvpninterfaceconfindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpninterfaceconfindex.get_name_leafdata())
                if (self.mplsvpninterfaceconfrowstatus.is_set or self.mplsvpninterfaceconfrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpninterfaceconfrowstatus.get_name_leafdata())
                if (self.mplsvpninterfaceconfstoragetype.is_set or self.mplsvpninterfaceconfstoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpninterfaceconfstoragetype.get_name_leafdata())
                if (self.mplsvpninterfacelabeledgetype.is_set or self.mplsvpninterfacelabeledgetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpninterfacelabeledgetype.get_name_leafdata())
                if (self.mplsvpninterfacevpnclassification.is_set or self.mplsvpninterfacevpnclassification.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpninterfacevpnclassification.get_name_leafdata())
                if (self.mplsvpninterfacevpnroutedistprotocol.is_set or self.mplsvpninterfacevpnroutedistprotocol.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpninterfacevpnroutedistprotocol.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mplsVpnVrfName" or name == "mplsVpnInterfaceConfIndex" or name == "mplsVpnInterfaceConfRowStatus" or name == "mplsVpnInterfaceConfStorageType" or name == "mplsVpnInterfaceLabelEdgeType" or name == "mplsVpnInterfaceVpnClassification" or name == "mplsVpnInterfaceVpnRouteDistProtocol"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "mplsVpnVrfName"):
                    self.mplsvpnvrfname = value
                    self.mplsvpnvrfname.value_namespace = name_space
                    self.mplsvpnvrfname.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnInterfaceConfIndex"):
                    self.mplsvpninterfaceconfindex = value
                    self.mplsvpninterfaceconfindex.value_namespace = name_space
                    self.mplsvpninterfaceconfindex.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnInterfaceConfRowStatus"):
                    self.mplsvpninterfaceconfrowstatus = value
                    self.mplsvpninterfaceconfrowstatus.value_namespace = name_space
                    self.mplsvpninterfaceconfrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnInterfaceConfStorageType"):
                    self.mplsvpninterfaceconfstoragetype = value
                    self.mplsvpninterfaceconfstoragetype.value_namespace = name_space
                    self.mplsvpninterfaceconfstoragetype.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnInterfaceLabelEdgeType"):
                    self.mplsvpninterfacelabeledgetype = value
                    self.mplsvpninterfacelabeledgetype.value_namespace = name_space
                    self.mplsvpninterfacelabeledgetype.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnInterfaceVpnClassification"):
                    self.mplsvpninterfacevpnclassification = value
                    self.mplsvpninterfacevpnclassification.value_namespace = name_space
                    self.mplsvpninterfacevpnclassification.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnInterfaceVpnRouteDistProtocol"):
                    self.mplsvpninterfacevpnroutedistprotocol[value] = True

        def has_data(self):
            for c in self.mplsvpninterfaceconfentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.mplsvpninterfaceconfentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mplsVpnInterfaceConfTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "MPLS-VPN-MIB:MPLS-VPN-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mplsVpnInterfaceConfEntry"):
                for c in self.mplsvpninterfaceconfentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = MplsVpnMib.Mplsvpninterfaceconftable.Mplsvpninterfaceconfentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mplsvpninterfaceconfentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mplsVpnInterfaceConfEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Mplsvpnvrftable(Entity):
        """
        This table specifies per\-interface MPLS/BGP VPN
        VRF Table capability and associated information.
        Entries in this table define VRF routing instances
        associated with MPLS/VPN interfaces. Note that
        multiple interfaces can belong to the same VRF
        instance. The collection of all VRF instances
        comprises an actual VPN.
        
        .. attribute:: mplsvpnvrfentry
        
        	An entry in this table is created by an LSR for every VRF capable of supporting MPLS/BGP VPN. The indexing provides an ordering of VRFs per\-VPN interface
        	**type**\: list of    :py:class:`Mplsvpnvrfentry <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrftable.Mplsvpnvrfentry>`
        
        

        """

        _prefix = 'MPLS-VPN-MIB'
        _revision = '2001-10-15'

        def __init__(self):
            super(MplsVpnMib.Mplsvpnvrftable, self).__init__()

            self.yang_name = "mplsVpnVrfTable"
            self.yang_parent_name = "MPLS-VPN-MIB"

            self.mplsvpnvrfentry = YList(self)

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
                        super(MplsVpnMib.Mplsvpnvrftable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsVpnMib.Mplsvpnvrftable, self).__setattr__(name, value)


        class Mplsvpnvrfentry(Entity):
            """
            An entry in this table is created by an LSR for
            every VRF capable of supporting MPLS/BGP VPN. The
            indexing provides an ordering of VRFs per\-VPN
            interface.
            
            .. attribute:: mplsvpnvrfname  <key>
            
            	The human\-readable name of this VPN. This MAY be equivalent to the RFC2685 VPN\-ID
            	**type**\:  str
            
            	**length:** 0..31
            
            .. attribute:: mplsvpnvrfactiveinterfaces
            
            	Total number of interfaces connected to this VRF with    ifOperStatus = up(1).   This counter should be incremented when\:  a. When the ifOperStatus of one of the connected interfaces     changes from down(2) to up(1).  b. When an interface with ifOperStatus = up(1) is connected    to this VRF.  This counter should be decremented when\:  a. When the ifOperStatus of one of the connected interfaces     changes from up(1) to down(2).  b. When one of the connected interfaces with     ifOperStatus = up(1) gets disconnected from this VRF
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfassociatedinterfaces
            
            	Total number of interfaces connected to this VRF  (independent of ifOperStatus type)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfconfhighroutethreshold
            
            	Denotes high\-level water marker for the number of routes which  this VRF may hold
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfconflastchanged
            
            	The value of sysUpTime at the time of the last change of this table entry, which includes changes of VRF parameters defined in this table or addition or deletion of interfaces associated with this VRF
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfconfmaxroutes
            
            	Denotes maximum number of routes which this VRF is configured to hold. This value MUST be less than or equal to mplsVrfMaxPossibleRoutes unless it is set to 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfconfmidroutethreshold
            
            	Denotes mid\-level water marker for the number of routes which  this VRF may hold
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfconfrowstatus
            
            	This variable is used to create, modify, and/or delete a row in this table
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: mplsvpnvrfconfstoragetype
            
            	The storage type for this entry
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            .. attribute:: mplsvpnvrfcreationtime
            
            	The time at which this VRF entry was created
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfdescription
            
            	The human\-readable description of this VRF
            	**type**\:  str
            
            .. attribute:: mplsvpnvrfoperstatus
            
            	Denotes whether a VRF is operational or not. A VRF is  up(1) when at least one interface associated with the VRF, which ifOperStatus is up(1). A VRF is down(2) when\:  a. There does not exist at least one interface whose    ifOperStatus is up(1).  b. There are no interfaces associated with the VRF
            	**type**\:   :py:class:`Mplsvpnvrfoperstatus <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrftable.Mplsvpnvrfentry.Mplsvpnvrfoperstatus>`
            
            .. attribute:: mplsvpnvrfperfcurrnumroutes
            
            	Indicates the number of routes currently used by this VRF
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfperfroutesadded
            
            	Indicates the number of routes added to this VPN/VRF over the coarse of its lifetime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfperfroutesdeleted
            
            	Indicates the number of routes removed from this VPN/VRF
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfroutedistinguisher
            
            	The route distinguisher for this VRF
            	**type**\:  str
            
            	**length:** 0..256
            
            .. attribute:: mplsvpnvrfsecillegallabelrcvthresh
            
            	The number of illegally received labels above which this  notification is issued
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfsecillegallabelviolations
            
            	Indicates the number of illegally received labels on this VPN/VRF
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'MPLS-VPN-MIB'
            _revision = '2001-10-15'

            def __init__(self):
                super(MplsVpnMib.Mplsvpnvrftable.Mplsvpnvrfentry, self).__init__()

                self.yang_name = "mplsVpnVrfEntry"
                self.yang_parent_name = "mplsVpnVrfTable"

                self.mplsvpnvrfname = YLeaf(YType.str, "mplsVpnVrfName")

                self.mplsvpnvrfactiveinterfaces = YLeaf(YType.uint32, "mplsVpnVrfActiveInterfaces")

                self.mplsvpnvrfassociatedinterfaces = YLeaf(YType.uint32, "mplsVpnVrfAssociatedInterfaces")

                self.mplsvpnvrfconfhighroutethreshold = YLeaf(YType.uint32, "mplsVpnVrfConfHighRouteThreshold")

                self.mplsvpnvrfconflastchanged = YLeaf(YType.uint32, "mplsVpnVrfConfLastChanged")

                self.mplsvpnvrfconfmaxroutes = YLeaf(YType.uint32, "mplsVpnVrfConfMaxRoutes")

                self.mplsvpnvrfconfmidroutethreshold = YLeaf(YType.uint32, "mplsVpnVrfConfMidRouteThreshold")

                self.mplsvpnvrfconfrowstatus = YLeaf(YType.enumeration, "mplsVpnVrfConfRowStatus")

                self.mplsvpnvrfconfstoragetype = YLeaf(YType.enumeration, "mplsVpnVrfConfStorageType")

                self.mplsvpnvrfcreationtime = YLeaf(YType.uint32, "mplsVpnVrfCreationTime")

                self.mplsvpnvrfdescription = YLeaf(YType.str, "mplsVpnVrfDescription")

                self.mplsvpnvrfoperstatus = YLeaf(YType.enumeration, "mplsVpnVrfOperStatus")

                self.mplsvpnvrfperfcurrnumroutes = YLeaf(YType.uint32, "mplsVpnVrfPerfCurrNumRoutes")

                self.mplsvpnvrfperfroutesadded = YLeaf(YType.uint32, "mplsVpnVrfPerfRoutesAdded")

                self.mplsvpnvrfperfroutesdeleted = YLeaf(YType.uint32, "mplsVpnVrfPerfRoutesDeleted")

                self.mplsvpnvrfroutedistinguisher = YLeaf(YType.str, "mplsVpnVrfRouteDistinguisher")

                self.mplsvpnvrfsecillegallabelrcvthresh = YLeaf(YType.uint32, "mplsVpnVrfSecIllegalLabelRcvThresh")

                self.mplsvpnvrfsecillegallabelviolations = YLeaf(YType.uint32, "mplsVpnVrfSecIllegalLabelViolations")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("mplsvpnvrfname",
                                "mplsvpnvrfactiveinterfaces",
                                "mplsvpnvrfassociatedinterfaces",
                                "mplsvpnvrfconfhighroutethreshold",
                                "mplsvpnvrfconflastchanged",
                                "mplsvpnvrfconfmaxroutes",
                                "mplsvpnvrfconfmidroutethreshold",
                                "mplsvpnvrfconfrowstatus",
                                "mplsvpnvrfconfstoragetype",
                                "mplsvpnvrfcreationtime",
                                "mplsvpnvrfdescription",
                                "mplsvpnvrfoperstatus",
                                "mplsvpnvrfperfcurrnumroutes",
                                "mplsvpnvrfperfroutesadded",
                                "mplsvpnvrfperfroutesdeleted",
                                "mplsvpnvrfroutedistinguisher",
                                "mplsvpnvrfsecillegallabelrcvthresh",
                                "mplsvpnvrfsecillegallabelviolations") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsVpnMib.Mplsvpnvrftable.Mplsvpnvrfentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsVpnMib.Mplsvpnvrftable.Mplsvpnvrfentry, self).__setattr__(name, value)

            class Mplsvpnvrfoperstatus(Enum):
                """
                Mplsvpnvrfoperstatus

                Denotes whether a VRF is operational or not. A VRF is 

                up(1) when at least one interface associated with the

                VRF, which ifOperStatus is up(1). A VRF is down(2) when\:

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
                    self.mplsvpnvrfname.is_set or
                    self.mplsvpnvrfactiveinterfaces.is_set or
                    self.mplsvpnvrfassociatedinterfaces.is_set or
                    self.mplsvpnvrfconfhighroutethreshold.is_set or
                    self.mplsvpnvrfconflastchanged.is_set or
                    self.mplsvpnvrfconfmaxroutes.is_set or
                    self.mplsvpnvrfconfmidroutethreshold.is_set or
                    self.mplsvpnvrfconfrowstatus.is_set or
                    self.mplsvpnvrfconfstoragetype.is_set or
                    self.mplsvpnvrfcreationtime.is_set or
                    self.mplsvpnvrfdescription.is_set or
                    self.mplsvpnvrfoperstatus.is_set or
                    self.mplsvpnvrfperfcurrnumroutes.is_set or
                    self.mplsvpnvrfperfroutesadded.is_set or
                    self.mplsvpnvrfperfroutesdeleted.is_set or
                    self.mplsvpnvrfroutedistinguisher.is_set or
                    self.mplsvpnvrfsecillegallabelrcvthresh.is_set or
                    self.mplsvpnvrfsecillegallabelviolations.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mplsvpnvrfname.yfilter != YFilter.not_set or
                    self.mplsvpnvrfactiveinterfaces.yfilter != YFilter.not_set or
                    self.mplsvpnvrfassociatedinterfaces.yfilter != YFilter.not_set or
                    self.mplsvpnvrfconfhighroutethreshold.yfilter != YFilter.not_set or
                    self.mplsvpnvrfconflastchanged.yfilter != YFilter.not_set or
                    self.mplsvpnvrfconfmaxroutes.yfilter != YFilter.not_set or
                    self.mplsvpnvrfconfmidroutethreshold.yfilter != YFilter.not_set or
                    self.mplsvpnvrfconfrowstatus.yfilter != YFilter.not_set or
                    self.mplsvpnvrfconfstoragetype.yfilter != YFilter.not_set or
                    self.mplsvpnvrfcreationtime.yfilter != YFilter.not_set or
                    self.mplsvpnvrfdescription.yfilter != YFilter.not_set or
                    self.mplsvpnvrfoperstatus.yfilter != YFilter.not_set or
                    self.mplsvpnvrfperfcurrnumroutes.yfilter != YFilter.not_set or
                    self.mplsvpnvrfperfroutesadded.yfilter != YFilter.not_set or
                    self.mplsvpnvrfperfroutesdeleted.yfilter != YFilter.not_set or
                    self.mplsvpnvrfroutedistinguisher.yfilter != YFilter.not_set or
                    self.mplsvpnvrfsecillegallabelrcvthresh.yfilter != YFilter.not_set or
                    self.mplsvpnvrfsecillegallabelviolations.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mplsVpnVrfEntry" + "[mplsVpnVrfName='" + self.mplsvpnvrfname.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "MPLS-VPN-MIB:MPLS-VPN-MIB/mplsVpnVrfTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.mplsvpnvrfname.is_set or self.mplsvpnvrfname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfname.get_name_leafdata())
                if (self.mplsvpnvrfactiveinterfaces.is_set or self.mplsvpnvrfactiveinterfaces.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfactiveinterfaces.get_name_leafdata())
                if (self.mplsvpnvrfassociatedinterfaces.is_set or self.mplsvpnvrfassociatedinterfaces.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfassociatedinterfaces.get_name_leafdata())
                if (self.mplsvpnvrfconfhighroutethreshold.is_set or self.mplsvpnvrfconfhighroutethreshold.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfconfhighroutethreshold.get_name_leafdata())
                if (self.mplsvpnvrfconflastchanged.is_set or self.mplsvpnvrfconflastchanged.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfconflastchanged.get_name_leafdata())
                if (self.mplsvpnvrfconfmaxroutes.is_set or self.mplsvpnvrfconfmaxroutes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfconfmaxroutes.get_name_leafdata())
                if (self.mplsvpnvrfconfmidroutethreshold.is_set or self.mplsvpnvrfconfmidroutethreshold.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfconfmidroutethreshold.get_name_leafdata())
                if (self.mplsvpnvrfconfrowstatus.is_set or self.mplsvpnvrfconfrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfconfrowstatus.get_name_leafdata())
                if (self.mplsvpnvrfconfstoragetype.is_set or self.mplsvpnvrfconfstoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfconfstoragetype.get_name_leafdata())
                if (self.mplsvpnvrfcreationtime.is_set or self.mplsvpnvrfcreationtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfcreationtime.get_name_leafdata())
                if (self.mplsvpnvrfdescription.is_set or self.mplsvpnvrfdescription.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfdescription.get_name_leafdata())
                if (self.mplsvpnvrfoperstatus.is_set or self.mplsvpnvrfoperstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfoperstatus.get_name_leafdata())
                if (self.mplsvpnvrfperfcurrnumroutes.is_set or self.mplsvpnvrfperfcurrnumroutes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfperfcurrnumroutes.get_name_leafdata())
                if (self.mplsvpnvrfperfroutesadded.is_set or self.mplsvpnvrfperfroutesadded.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfperfroutesadded.get_name_leafdata())
                if (self.mplsvpnvrfperfroutesdeleted.is_set or self.mplsvpnvrfperfroutesdeleted.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfperfroutesdeleted.get_name_leafdata())
                if (self.mplsvpnvrfroutedistinguisher.is_set or self.mplsvpnvrfroutedistinguisher.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfroutedistinguisher.get_name_leafdata())
                if (self.mplsvpnvrfsecillegallabelrcvthresh.is_set or self.mplsvpnvrfsecillegallabelrcvthresh.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfsecillegallabelrcvthresh.get_name_leafdata())
                if (self.mplsvpnvrfsecillegallabelviolations.is_set or self.mplsvpnvrfsecillegallabelviolations.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfsecillegallabelviolations.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mplsVpnVrfName" or name == "mplsVpnVrfActiveInterfaces" or name == "mplsVpnVrfAssociatedInterfaces" or name == "mplsVpnVrfConfHighRouteThreshold" or name == "mplsVpnVrfConfLastChanged" or name == "mplsVpnVrfConfMaxRoutes" or name == "mplsVpnVrfConfMidRouteThreshold" or name == "mplsVpnVrfConfRowStatus" or name == "mplsVpnVrfConfStorageType" or name == "mplsVpnVrfCreationTime" or name == "mplsVpnVrfDescription" or name == "mplsVpnVrfOperStatus" or name == "mplsVpnVrfPerfCurrNumRoutes" or name == "mplsVpnVrfPerfRoutesAdded" or name == "mplsVpnVrfPerfRoutesDeleted" or name == "mplsVpnVrfRouteDistinguisher" or name == "mplsVpnVrfSecIllegalLabelRcvThresh" or name == "mplsVpnVrfSecIllegalLabelViolations"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "mplsVpnVrfName"):
                    self.mplsvpnvrfname = value
                    self.mplsvpnvrfname.value_namespace = name_space
                    self.mplsvpnvrfname.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfActiveInterfaces"):
                    self.mplsvpnvrfactiveinterfaces = value
                    self.mplsvpnvrfactiveinterfaces.value_namespace = name_space
                    self.mplsvpnvrfactiveinterfaces.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfAssociatedInterfaces"):
                    self.mplsvpnvrfassociatedinterfaces = value
                    self.mplsvpnvrfassociatedinterfaces.value_namespace = name_space
                    self.mplsvpnvrfassociatedinterfaces.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfConfHighRouteThreshold"):
                    self.mplsvpnvrfconfhighroutethreshold = value
                    self.mplsvpnvrfconfhighroutethreshold.value_namespace = name_space
                    self.mplsvpnvrfconfhighroutethreshold.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfConfLastChanged"):
                    self.mplsvpnvrfconflastchanged = value
                    self.mplsvpnvrfconflastchanged.value_namespace = name_space
                    self.mplsvpnvrfconflastchanged.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfConfMaxRoutes"):
                    self.mplsvpnvrfconfmaxroutes = value
                    self.mplsvpnvrfconfmaxroutes.value_namespace = name_space
                    self.mplsvpnvrfconfmaxroutes.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfConfMidRouteThreshold"):
                    self.mplsvpnvrfconfmidroutethreshold = value
                    self.mplsvpnvrfconfmidroutethreshold.value_namespace = name_space
                    self.mplsvpnvrfconfmidroutethreshold.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfConfRowStatus"):
                    self.mplsvpnvrfconfrowstatus = value
                    self.mplsvpnvrfconfrowstatus.value_namespace = name_space
                    self.mplsvpnvrfconfrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfConfStorageType"):
                    self.mplsvpnvrfconfstoragetype = value
                    self.mplsvpnvrfconfstoragetype.value_namespace = name_space
                    self.mplsvpnvrfconfstoragetype.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfCreationTime"):
                    self.mplsvpnvrfcreationtime = value
                    self.mplsvpnvrfcreationtime.value_namespace = name_space
                    self.mplsvpnvrfcreationtime.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfDescription"):
                    self.mplsvpnvrfdescription = value
                    self.mplsvpnvrfdescription.value_namespace = name_space
                    self.mplsvpnvrfdescription.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfOperStatus"):
                    self.mplsvpnvrfoperstatus = value
                    self.mplsvpnvrfoperstatus.value_namespace = name_space
                    self.mplsvpnvrfoperstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfPerfCurrNumRoutes"):
                    self.mplsvpnvrfperfcurrnumroutes = value
                    self.mplsvpnvrfperfcurrnumroutes.value_namespace = name_space
                    self.mplsvpnvrfperfcurrnumroutes.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfPerfRoutesAdded"):
                    self.mplsvpnvrfperfroutesadded = value
                    self.mplsvpnvrfperfroutesadded.value_namespace = name_space
                    self.mplsvpnvrfperfroutesadded.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfPerfRoutesDeleted"):
                    self.mplsvpnvrfperfroutesdeleted = value
                    self.mplsvpnvrfperfroutesdeleted.value_namespace = name_space
                    self.mplsvpnvrfperfroutesdeleted.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfRouteDistinguisher"):
                    self.mplsvpnvrfroutedistinguisher = value
                    self.mplsvpnvrfroutedistinguisher.value_namespace = name_space
                    self.mplsvpnvrfroutedistinguisher.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfSecIllegalLabelRcvThresh"):
                    self.mplsvpnvrfsecillegallabelrcvthresh = value
                    self.mplsvpnvrfsecillegallabelrcvthresh.value_namespace = name_space
                    self.mplsvpnvrfsecillegallabelrcvthresh.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfSecIllegalLabelViolations"):
                    self.mplsvpnvrfsecillegallabelviolations = value
                    self.mplsvpnvrfsecillegallabelviolations.value_namespace = name_space
                    self.mplsvpnvrfsecillegallabelviolations.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.mplsvpnvrfentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.mplsvpnvrfentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mplsVpnVrfTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "MPLS-VPN-MIB:MPLS-VPN-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mplsVpnVrfEntry"):
                for c in self.mplsvpnvrfentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = MplsVpnMib.Mplsvpnvrftable.Mplsvpnvrfentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mplsvpnvrfentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mplsVpnVrfEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Mplsvpnvrfroutetargettable(Entity):
        """
        This table specifies per\-VRF route target association.
        Each entry identifies a connectivity policy supported
        as part of a VPN.
        
        .. attribute:: mplsvpnvrfroutetargetentry
        
        	 An entry in this table is created by an LSR for each route target configured for a VRF supporting a MPLS/BGP VPN instance. The indexing provides an ordering per\-VRF instance
        	**type**\: list of    :py:class:`Mplsvpnvrfroutetargetentry <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrfroutetargettable.Mplsvpnvrfroutetargetentry>`
        
        

        """

        _prefix = 'MPLS-VPN-MIB'
        _revision = '2001-10-15'

        def __init__(self):
            super(MplsVpnMib.Mplsvpnvrfroutetargettable, self).__init__()

            self.yang_name = "mplsVpnVrfRouteTargetTable"
            self.yang_parent_name = "MPLS-VPN-MIB"

            self.mplsvpnvrfroutetargetentry = YList(self)

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
                        super(MplsVpnMib.Mplsvpnvrfroutetargettable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsVpnMib.Mplsvpnvrfroutetargettable, self).__setattr__(name, value)


        class Mplsvpnvrfroutetargetentry(Entity):
            """
             An entry in this table is created by an LSR for
            each route target configured for a VRF supporting
            a MPLS/BGP VPN instance. The indexing provides an
            ordering per\-VRF instance.
            
            .. attribute:: mplsvpnvrfname  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..31
            
            	**refers to**\:  :py:class:`mplsvpnvrfname <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrftable.Mplsvpnvrfentry>`
            
            .. attribute:: mplsvpnvrfroutetargetindex  <key>
            
            	Auxiliary index for route\-targets configured for a  particular VRF
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfroutetargettype  <key>
            
            	The route target export distribution type
            	**type**\:   :py:class:`Mplsvpnvrfroutetargettype <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrfroutetargettable.Mplsvpnvrfroutetargetentry.Mplsvpnvrfroutetargettype>`
            
            .. attribute:: mplsvpnvrfroutetarget
            
            	The route target distribution policy
            	**type**\:  str
            
            	**length:** 0..256
            
            .. attribute:: mplsvpnvrfroutetargetdescr
            
            	Description of the route target
            	**type**\:  str
            
            .. attribute:: mplsvpnvrfroutetargetrowstatus
            
            	Row status for this entry
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            

            """

            _prefix = 'MPLS-VPN-MIB'
            _revision = '2001-10-15'

            def __init__(self):
                super(MplsVpnMib.Mplsvpnvrfroutetargettable.Mplsvpnvrfroutetargetentry, self).__init__()

                self.yang_name = "mplsVpnVrfRouteTargetEntry"
                self.yang_parent_name = "mplsVpnVrfRouteTargetTable"

                self.mplsvpnvrfname = YLeaf(YType.str, "mplsVpnVrfName")

                self.mplsvpnvrfroutetargetindex = YLeaf(YType.uint32, "mplsVpnVrfRouteTargetIndex")

                self.mplsvpnvrfroutetargettype = YLeaf(YType.enumeration, "mplsVpnVrfRouteTargetType")

                self.mplsvpnvrfroutetarget = YLeaf(YType.str, "mplsVpnVrfRouteTarget")

                self.mplsvpnvrfroutetargetdescr = YLeaf(YType.str, "mplsVpnVrfRouteTargetDescr")

                self.mplsvpnvrfroutetargetrowstatus = YLeaf(YType.enumeration, "mplsVpnVrfRouteTargetRowStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("mplsvpnvrfname",
                                "mplsvpnvrfroutetargetindex",
                                "mplsvpnvrfroutetargettype",
                                "mplsvpnvrfroutetarget",
                                "mplsvpnvrfroutetargetdescr",
                                "mplsvpnvrfroutetargetrowstatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsVpnMib.Mplsvpnvrfroutetargettable.Mplsvpnvrfroutetargetentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsVpnMib.Mplsvpnvrfroutetargettable.Mplsvpnvrfroutetargetentry, self).__setattr__(name, value)

            class Mplsvpnvrfroutetargettype(Enum):
                """
                Mplsvpnvrfroutetargettype

                The route target export distribution type.

                .. data:: import_ = 1

                .. data:: export = 2

                .. data:: both = 3

                """

                import_ = Enum.YLeaf(1, "import")

                export = Enum.YLeaf(2, "export")

                both = Enum.YLeaf(3, "both")


            def has_data(self):
                return (
                    self.mplsvpnvrfname.is_set or
                    self.mplsvpnvrfroutetargetindex.is_set or
                    self.mplsvpnvrfroutetargettype.is_set or
                    self.mplsvpnvrfroutetarget.is_set or
                    self.mplsvpnvrfroutetargetdescr.is_set or
                    self.mplsvpnvrfroutetargetrowstatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mplsvpnvrfname.yfilter != YFilter.not_set or
                    self.mplsvpnvrfroutetargetindex.yfilter != YFilter.not_set or
                    self.mplsvpnvrfroutetargettype.yfilter != YFilter.not_set or
                    self.mplsvpnvrfroutetarget.yfilter != YFilter.not_set or
                    self.mplsvpnvrfroutetargetdescr.yfilter != YFilter.not_set or
                    self.mplsvpnvrfroutetargetrowstatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mplsVpnVrfRouteTargetEntry" + "[mplsVpnVrfName='" + self.mplsvpnvrfname.get() + "']" + "[mplsVpnVrfRouteTargetIndex='" + self.mplsvpnvrfroutetargetindex.get() + "']" + "[mplsVpnVrfRouteTargetType='" + self.mplsvpnvrfroutetargettype.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "MPLS-VPN-MIB:MPLS-VPN-MIB/mplsVpnVrfRouteTargetTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.mplsvpnvrfname.is_set or self.mplsvpnvrfname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfname.get_name_leafdata())
                if (self.mplsvpnvrfroutetargetindex.is_set or self.mplsvpnvrfroutetargetindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfroutetargetindex.get_name_leafdata())
                if (self.mplsvpnvrfroutetargettype.is_set or self.mplsvpnvrfroutetargettype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfroutetargettype.get_name_leafdata())
                if (self.mplsvpnvrfroutetarget.is_set or self.mplsvpnvrfroutetarget.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfroutetarget.get_name_leafdata())
                if (self.mplsvpnvrfroutetargetdescr.is_set or self.mplsvpnvrfroutetargetdescr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfroutetargetdescr.get_name_leafdata())
                if (self.mplsvpnvrfroutetargetrowstatus.is_set or self.mplsvpnvrfroutetargetrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfroutetargetrowstatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mplsVpnVrfName" or name == "mplsVpnVrfRouteTargetIndex" or name == "mplsVpnVrfRouteTargetType" or name == "mplsVpnVrfRouteTarget" or name == "mplsVpnVrfRouteTargetDescr" or name == "mplsVpnVrfRouteTargetRowStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "mplsVpnVrfName"):
                    self.mplsvpnvrfname = value
                    self.mplsvpnvrfname.value_namespace = name_space
                    self.mplsvpnvrfname.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfRouteTargetIndex"):
                    self.mplsvpnvrfroutetargetindex = value
                    self.mplsvpnvrfroutetargetindex.value_namespace = name_space
                    self.mplsvpnvrfroutetargetindex.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfRouteTargetType"):
                    self.mplsvpnvrfroutetargettype = value
                    self.mplsvpnvrfroutetargettype.value_namespace = name_space
                    self.mplsvpnvrfroutetargettype.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfRouteTarget"):
                    self.mplsvpnvrfroutetarget = value
                    self.mplsvpnvrfroutetarget.value_namespace = name_space
                    self.mplsvpnvrfroutetarget.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfRouteTargetDescr"):
                    self.mplsvpnvrfroutetargetdescr = value
                    self.mplsvpnvrfroutetargetdescr.value_namespace = name_space
                    self.mplsvpnvrfroutetargetdescr.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfRouteTargetRowStatus"):
                    self.mplsvpnvrfroutetargetrowstatus = value
                    self.mplsvpnvrfroutetargetrowstatus.value_namespace = name_space
                    self.mplsvpnvrfroutetargetrowstatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.mplsvpnvrfroutetargetentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.mplsvpnvrfroutetargetentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mplsVpnVrfRouteTargetTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "MPLS-VPN-MIB:MPLS-VPN-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mplsVpnVrfRouteTargetEntry"):
                for c in self.mplsvpnvrfroutetargetentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = MplsVpnMib.Mplsvpnvrfroutetargettable.Mplsvpnvrfroutetargetentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mplsvpnvrfroutetargetentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mplsVpnVrfRouteTargetEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Mplsvpnvrfbgpnbraddrtable(Entity):
        """
        Each entry in this table specifies a per\-interface 
        MPLS/EBGP neighbor.
        
        .. attribute:: mplsvpnvrfbgpnbraddrentry
        
        	An entry in this table is created by an LSR for every VRF capable of supporting MPLS/BGP VPN. The indexing provides an ordering of VRFs per\-VPN interface
        	**type**\: list of    :py:class:`Mplsvpnvrfbgpnbraddrentry <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrfbgpnbraddrtable.Mplsvpnvrfbgpnbraddrentry>`
        
        

        """

        _prefix = 'MPLS-VPN-MIB'
        _revision = '2001-10-15'

        def __init__(self):
            super(MplsVpnMib.Mplsvpnvrfbgpnbraddrtable, self).__init__()

            self.yang_name = "mplsVpnVrfBgpNbrAddrTable"
            self.yang_parent_name = "MPLS-VPN-MIB"

            self.mplsvpnvrfbgpnbraddrentry = YList(self)

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
                        super(MplsVpnMib.Mplsvpnvrfbgpnbraddrtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsVpnMib.Mplsvpnvrfbgpnbraddrtable, self).__setattr__(name, value)


        class Mplsvpnvrfbgpnbraddrentry(Entity):
            """
            An entry in this table is created by an LSR for
            every VRF capable of supporting MPLS/BGP VPN. The
            indexing provides an ordering of VRFs per\-VPN
            interface.
            
            .. attribute:: mplsvpnvrfname  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..31
            
            	**refers to**\:  :py:class:`mplsvpnvrfname <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrftable.Mplsvpnvrfentry>`
            
            .. attribute:: mplsvpninterfaceconfindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`mplsvpninterfaceconfindex <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpninterfaceconftable.Mplsvpninterfaceconfentry>`
            
            .. attribute:: mplsvpnvrfbgpnbrindex  <key>
            
            	This is a unique tertiary index for an entry in the MplsVpnVrfBgpNbrAddrEntry Table
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfbgpnbraddr
            
            	Denotes the EBGP neighbor address
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: mplsvpnvrfbgpnbrrole
            
            	Denotes the role played by this EBGP neighbor with respect to this VRF
            	**type**\:   :py:class:`Mplsvpnvrfbgpnbrrole <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrfbgpnbraddrtable.Mplsvpnvrfbgpnbraddrentry.Mplsvpnvrfbgpnbrrole>`
            
            .. attribute:: mplsvpnvrfbgpnbrrowstatus
            
            	This variable is used to create, modify, and/or delete a row in this table
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: mplsvpnvrfbgpnbrstoragetype
            
            	The storage type for this entry
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            .. attribute:: mplsvpnvrfbgpnbrtype
            
            	Denotes the address family of the PE address
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            

            """

            _prefix = 'MPLS-VPN-MIB'
            _revision = '2001-10-15'

            def __init__(self):
                super(MplsVpnMib.Mplsvpnvrfbgpnbraddrtable.Mplsvpnvrfbgpnbraddrentry, self).__init__()

                self.yang_name = "mplsVpnVrfBgpNbrAddrEntry"
                self.yang_parent_name = "mplsVpnVrfBgpNbrAddrTable"

                self.mplsvpnvrfname = YLeaf(YType.str, "mplsVpnVrfName")

                self.mplsvpninterfaceconfindex = YLeaf(YType.str, "mplsVpnInterfaceConfIndex")

                self.mplsvpnvrfbgpnbrindex = YLeaf(YType.uint32, "mplsVpnVrfBgpNbrIndex")

                self.mplsvpnvrfbgpnbraddr = YLeaf(YType.str, "mplsVpnVrfBgpNbrAddr")

                self.mplsvpnvrfbgpnbrrole = YLeaf(YType.enumeration, "mplsVpnVrfBgpNbrRole")

                self.mplsvpnvrfbgpnbrrowstatus = YLeaf(YType.enumeration, "mplsVpnVrfBgpNbrRowStatus")

                self.mplsvpnvrfbgpnbrstoragetype = YLeaf(YType.enumeration, "mplsVpnVrfBgpNbrStorageType")

                self.mplsvpnvrfbgpnbrtype = YLeaf(YType.enumeration, "mplsVpnVrfBgpNbrType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("mplsvpnvrfname",
                                "mplsvpninterfaceconfindex",
                                "mplsvpnvrfbgpnbrindex",
                                "mplsvpnvrfbgpnbraddr",
                                "mplsvpnvrfbgpnbrrole",
                                "mplsvpnvrfbgpnbrrowstatus",
                                "mplsvpnvrfbgpnbrstoragetype",
                                "mplsvpnvrfbgpnbrtype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsVpnMib.Mplsvpnvrfbgpnbraddrtable.Mplsvpnvrfbgpnbraddrentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsVpnMib.Mplsvpnvrfbgpnbraddrtable.Mplsvpnvrfbgpnbraddrentry, self).__setattr__(name, value)

            class Mplsvpnvrfbgpnbrrole(Enum):
                """
                Mplsvpnvrfbgpnbrrole

                Denotes the role played by this EBGP neighbor

                with respect to this VRF.

                .. data:: ce = 1

                .. data:: pe = 2

                """

                ce = Enum.YLeaf(1, "ce")

                pe = Enum.YLeaf(2, "pe")


            def has_data(self):
                return (
                    self.mplsvpnvrfname.is_set or
                    self.mplsvpninterfaceconfindex.is_set or
                    self.mplsvpnvrfbgpnbrindex.is_set or
                    self.mplsvpnvrfbgpnbraddr.is_set or
                    self.mplsvpnvrfbgpnbrrole.is_set or
                    self.mplsvpnvrfbgpnbrrowstatus.is_set or
                    self.mplsvpnvrfbgpnbrstoragetype.is_set or
                    self.mplsvpnvrfbgpnbrtype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mplsvpnvrfname.yfilter != YFilter.not_set or
                    self.mplsvpninterfaceconfindex.yfilter != YFilter.not_set or
                    self.mplsvpnvrfbgpnbrindex.yfilter != YFilter.not_set or
                    self.mplsvpnvrfbgpnbraddr.yfilter != YFilter.not_set or
                    self.mplsvpnvrfbgpnbrrole.yfilter != YFilter.not_set or
                    self.mplsvpnvrfbgpnbrrowstatus.yfilter != YFilter.not_set or
                    self.mplsvpnvrfbgpnbrstoragetype.yfilter != YFilter.not_set or
                    self.mplsvpnvrfbgpnbrtype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mplsVpnVrfBgpNbrAddrEntry" + "[mplsVpnVrfName='" + self.mplsvpnvrfname.get() + "']" + "[mplsVpnInterfaceConfIndex='" + self.mplsvpninterfaceconfindex.get() + "']" + "[mplsVpnVrfBgpNbrIndex='" + self.mplsvpnvrfbgpnbrindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "MPLS-VPN-MIB:MPLS-VPN-MIB/mplsVpnVrfBgpNbrAddrTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.mplsvpnvrfname.is_set or self.mplsvpnvrfname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfname.get_name_leafdata())
                if (self.mplsvpninterfaceconfindex.is_set or self.mplsvpninterfaceconfindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpninterfaceconfindex.get_name_leafdata())
                if (self.mplsvpnvrfbgpnbrindex.is_set or self.mplsvpnvrfbgpnbrindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfbgpnbrindex.get_name_leafdata())
                if (self.mplsvpnvrfbgpnbraddr.is_set or self.mplsvpnvrfbgpnbraddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfbgpnbraddr.get_name_leafdata())
                if (self.mplsvpnvrfbgpnbrrole.is_set or self.mplsvpnvrfbgpnbrrole.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfbgpnbrrole.get_name_leafdata())
                if (self.mplsvpnvrfbgpnbrrowstatus.is_set or self.mplsvpnvrfbgpnbrrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfbgpnbrrowstatus.get_name_leafdata())
                if (self.mplsvpnvrfbgpnbrstoragetype.is_set or self.mplsvpnvrfbgpnbrstoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfbgpnbrstoragetype.get_name_leafdata())
                if (self.mplsvpnvrfbgpnbrtype.is_set or self.mplsvpnvrfbgpnbrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfbgpnbrtype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mplsVpnVrfName" or name == "mplsVpnInterfaceConfIndex" or name == "mplsVpnVrfBgpNbrIndex" or name == "mplsVpnVrfBgpNbrAddr" or name == "mplsVpnVrfBgpNbrRole" or name == "mplsVpnVrfBgpNbrRowStatus" or name == "mplsVpnVrfBgpNbrStorageType" or name == "mplsVpnVrfBgpNbrType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "mplsVpnVrfName"):
                    self.mplsvpnvrfname = value
                    self.mplsvpnvrfname.value_namespace = name_space
                    self.mplsvpnvrfname.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnInterfaceConfIndex"):
                    self.mplsvpninterfaceconfindex = value
                    self.mplsvpninterfaceconfindex.value_namespace = name_space
                    self.mplsvpninterfaceconfindex.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfBgpNbrIndex"):
                    self.mplsvpnvrfbgpnbrindex = value
                    self.mplsvpnvrfbgpnbrindex.value_namespace = name_space
                    self.mplsvpnvrfbgpnbrindex.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfBgpNbrAddr"):
                    self.mplsvpnvrfbgpnbraddr = value
                    self.mplsvpnvrfbgpnbraddr.value_namespace = name_space
                    self.mplsvpnvrfbgpnbraddr.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfBgpNbrRole"):
                    self.mplsvpnvrfbgpnbrrole = value
                    self.mplsvpnvrfbgpnbrrole.value_namespace = name_space
                    self.mplsvpnvrfbgpnbrrole.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfBgpNbrRowStatus"):
                    self.mplsvpnvrfbgpnbrrowstatus = value
                    self.mplsvpnvrfbgpnbrrowstatus.value_namespace = name_space
                    self.mplsvpnvrfbgpnbrrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfBgpNbrStorageType"):
                    self.mplsvpnvrfbgpnbrstoragetype = value
                    self.mplsvpnvrfbgpnbrstoragetype.value_namespace = name_space
                    self.mplsvpnvrfbgpnbrstoragetype.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfBgpNbrType"):
                    self.mplsvpnvrfbgpnbrtype = value
                    self.mplsvpnvrfbgpnbrtype.value_namespace = name_space
                    self.mplsvpnvrfbgpnbrtype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.mplsvpnvrfbgpnbraddrentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.mplsvpnvrfbgpnbraddrentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mplsVpnVrfBgpNbrAddrTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "MPLS-VPN-MIB:MPLS-VPN-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mplsVpnVrfBgpNbrAddrEntry"):
                for c in self.mplsvpnvrfbgpnbraddrentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = MplsVpnMib.Mplsvpnvrfbgpnbraddrtable.Mplsvpnvrfbgpnbraddrentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mplsvpnvrfbgpnbraddrentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mplsVpnVrfBgpNbrAddrEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Mplsvpnvrfbgpnbrprefixtable(Entity):
        """
        This table specifies per\-VRF vpnv4 multi\-protocol
        prefixes supported by BGP.
        
        .. attribute:: mplsvpnvrfbgpnbrprefixentry
        
        	An entry in this table is created by an LSR for every BGP prefix associated with a VRF supporting a  MPLS/BGP VPN. The indexing provides an ordering of  BGP prefixes per VRF
        	**type**\: list of    :py:class:`Mplsvpnvrfbgpnbrprefixentry <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrfbgpnbrprefixtable.Mplsvpnvrfbgpnbrprefixentry>`
        
        

        """

        _prefix = 'MPLS-VPN-MIB'
        _revision = '2001-10-15'

        def __init__(self):
            super(MplsVpnMib.Mplsvpnvrfbgpnbrprefixtable, self).__init__()

            self.yang_name = "mplsVpnVrfBgpNbrPrefixTable"
            self.yang_parent_name = "MPLS-VPN-MIB"

            self.mplsvpnvrfbgpnbrprefixentry = YList(self)

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
                        super(MplsVpnMib.Mplsvpnvrfbgpnbrprefixtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsVpnMib.Mplsvpnvrfbgpnbrprefixtable, self).__setattr__(name, value)


        class Mplsvpnvrfbgpnbrprefixentry(Entity):
            """
            An entry in this table is created by an LSR for
            every BGP prefix associated with a VRF supporting a 
            MPLS/BGP VPN. The indexing provides an ordering of 
            BGP prefixes per VRF.
            
            .. attribute:: mplsvpnvrfname  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..31
            
            	**refers to**\:  :py:class:`mplsvpnvrfname <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrftable.Mplsvpnvrfentry>`
            
            .. attribute:: mplsvpnvrfbgppathattripaddrprefix  <key>
            
            	An IP address prefix in the Network Layer Reachability Information field.  This object is an IP address containing the prefix with length specified by mplsVpnVrfBgpPathAttrIpAddrPrefixLen. Any bits beyond the length specified by mplsVpnVrfBgpPathAttrIpAddrPrefixLen are zeroed
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: mplsvpnvrfbgppathattripaddrprefixlen  <key>
            
            	Length in bits of the IP address prefix in the Network Layer Reachability Information field
            	**type**\:  int
            
            	**range:** 0..32
            
            .. attribute:: mplsvpnvrfbgppathattrpeer  <key>
            
            	The IP address of the peer where the path information was learned
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: mplsvpnvrfbgppathattraggregatoraddr
            
            	The IP address of the last BGP4 speaker that performed route aggregation.  A value of 0.0.0.0 indicates the absence of this attribute
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: mplsvpnvrfbgppathattraggregatoras
            
            	The AS number of the last BGP4 speaker that performed route aggregation.  A value of zero (0) indicates the absence of this attribute
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: mplsvpnvrfbgppathattraspathsegment
            
            	The sequence of AS path segments.  Each AS path segment is represented by a triple <type, length, value>.   The type is a 1\-octet field which has two  possible values\:      1      AS\_SET\: unordered set of ASs a             route in the UPDATE             message has traversed      2      AS\_SEQUENCE\: ordered set of ASs             a route in the UPDATE             message has traversed.             The length is a 1\-octet field containing the               number of ASs in the value field.              The value field contains one or more AS             numbers, each AS is represented in the octet             string as a pair of octets according to the             following algorithm\:              first\-byte\-of\-pair = ASNumber / 256;             second\-byte\-of\-pair = ASNumber & 255;
            	**type**\:  str
            
            	**length:** 2..255
            
            .. attribute:: mplsvpnvrfbgppathattratomicaggregate
            
            	Whether or not the local system has selected a less specific route without selecting a more specific route
            	**type**\:   :py:class:`Mplsvpnvrfbgppathattratomicaggregate <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrfbgpnbrprefixtable.Mplsvpnvrfbgpnbrprefixentry.Mplsvpnvrfbgppathattratomicaggregate>`
            
            .. attribute:: mplsvpnvrfbgppathattrbest
            
            	An indication of whether or not this route was chosen as the best BGP4 route
            	**type**\:   :py:class:`Mplsvpnvrfbgppathattrbest <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrfbgpnbrprefixtable.Mplsvpnvrfbgpnbrprefixentry.Mplsvpnvrfbgppathattrbest>`
            
            .. attribute:: mplsvpnvrfbgppathattrcalclocalpref
            
            	The degree of preference calculated by the receiving BGP4 speaker for an advertised route.  A value of \-1 indicates the absence of this attribute
            	**type**\:  int
            
            	**range:** \-1..2147483647
            
            .. attribute:: mplsvpnvrfbgppathattrlocalpref
            
            	The originating BGP4 speaker's degree of preference for an advertised route.  A value of \-1 indicates the absence of this attribute
            	**type**\:  int
            
            	**range:** \-1..2147483647
            
            .. attribute:: mplsvpnvrfbgppathattrmultiexitdisc
            
            	This metric is used to discriminate between multiple exit points to an adjacent autonomous system.  A value of \-1 indicates the absence of this attribute
            	**type**\:  int
            
            	**range:** \-1..2147483647
            
            .. attribute:: mplsvpnvrfbgppathattrnexthop
            
            	The address of the border router that should be used for the destination network
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: mplsvpnvrfbgppathattrorigin
            
            	The ultimate origin of the path information
            	**type**\:   :py:class:`Mplsvpnvrfbgppathattrorigin <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrfbgpnbrprefixtable.Mplsvpnvrfbgpnbrprefixentry.Mplsvpnvrfbgppathattrorigin>`
            
            .. attribute:: mplsvpnvrfbgppathattrunknown
            
            	One or more path attributes not understood by this BGP4 speaker.  Size zero (0) indicates the absence of such attribute(s).  Octets beyond the maximum size, if any, are not recorded by this object
            	**type**\:  str
            
            	**length:** 0..255
            
            

            """

            _prefix = 'MPLS-VPN-MIB'
            _revision = '2001-10-15'

            def __init__(self):
                super(MplsVpnMib.Mplsvpnvrfbgpnbrprefixtable.Mplsvpnvrfbgpnbrprefixentry, self).__init__()

                self.yang_name = "mplsVpnVrfBgpNbrPrefixEntry"
                self.yang_parent_name = "mplsVpnVrfBgpNbrPrefixTable"

                self.mplsvpnvrfname = YLeaf(YType.str, "mplsVpnVrfName")

                self.mplsvpnvrfbgppathattripaddrprefix = YLeaf(YType.str, "mplsVpnVrfBgpPathAttrIpAddrPrefix")

                self.mplsvpnvrfbgppathattripaddrprefixlen = YLeaf(YType.int32, "mplsVpnVrfBgpPathAttrIpAddrPrefixLen")

                self.mplsvpnvrfbgppathattrpeer = YLeaf(YType.str, "mplsVpnVrfBgpPathAttrPeer")

                self.mplsvpnvrfbgppathattraggregatoraddr = YLeaf(YType.str, "mplsVpnVrfBgpPathAttrAggregatorAddr")

                self.mplsvpnvrfbgppathattraggregatoras = YLeaf(YType.int32, "mplsVpnVrfBgpPathAttrAggregatorAS")

                self.mplsvpnvrfbgppathattraspathsegment = YLeaf(YType.str, "mplsVpnVrfBgpPathAttrASPathSegment")

                self.mplsvpnvrfbgppathattratomicaggregate = YLeaf(YType.enumeration, "mplsVpnVrfBgpPathAttrAtomicAggregate")

                self.mplsvpnvrfbgppathattrbest = YLeaf(YType.enumeration, "mplsVpnVrfBgpPathAttrBest")

                self.mplsvpnvrfbgppathattrcalclocalpref = YLeaf(YType.int32, "mplsVpnVrfBgpPathAttrCalcLocalPref")

                self.mplsvpnvrfbgppathattrlocalpref = YLeaf(YType.int32, "mplsVpnVrfBgpPathAttrLocalPref")

                self.mplsvpnvrfbgppathattrmultiexitdisc = YLeaf(YType.int32, "mplsVpnVrfBgpPathAttrMultiExitDisc")

                self.mplsvpnvrfbgppathattrnexthop = YLeaf(YType.str, "mplsVpnVrfBgpPathAttrNextHop")

                self.mplsvpnvrfbgppathattrorigin = YLeaf(YType.enumeration, "mplsVpnVrfBgpPathAttrOrigin")

                self.mplsvpnvrfbgppathattrunknown = YLeaf(YType.str, "mplsVpnVrfBgpPathAttrUnknown")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("mplsvpnvrfname",
                                "mplsvpnvrfbgppathattripaddrprefix",
                                "mplsvpnvrfbgppathattripaddrprefixlen",
                                "mplsvpnvrfbgppathattrpeer",
                                "mplsvpnvrfbgppathattraggregatoraddr",
                                "mplsvpnvrfbgppathattraggregatoras",
                                "mplsvpnvrfbgppathattraspathsegment",
                                "mplsvpnvrfbgppathattratomicaggregate",
                                "mplsvpnvrfbgppathattrbest",
                                "mplsvpnvrfbgppathattrcalclocalpref",
                                "mplsvpnvrfbgppathattrlocalpref",
                                "mplsvpnvrfbgppathattrmultiexitdisc",
                                "mplsvpnvrfbgppathattrnexthop",
                                "mplsvpnvrfbgppathattrorigin",
                                "mplsvpnvrfbgppathattrunknown") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsVpnMib.Mplsvpnvrfbgpnbrprefixtable.Mplsvpnvrfbgpnbrprefixentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsVpnMib.Mplsvpnvrfbgpnbrprefixtable.Mplsvpnvrfbgpnbrprefixentry, self).__setattr__(name, value)

            class Mplsvpnvrfbgppathattratomicaggregate(Enum):
                """
                Mplsvpnvrfbgppathattratomicaggregate

                Whether or not the local system has

                selected a less specific route without

                selecting a more specific route.

                .. data:: lessSpecificRrouteNotSelected = 1

                .. data:: lessSpecificRouteSelected = 2

                """

                lessSpecificRrouteNotSelected = Enum.YLeaf(1, "lessSpecificRrouteNotSelected")

                lessSpecificRouteSelected = Enum.YLeaf(2, "lessSpecificRouteSelected")


            class Mplsvpnvrfbgppathattrbest(Enum):
                """
                Mplsvpnvrfbgppathattrbest

                An indication of whether or not this route

                was chosen as the best BGP4 route.

                .. data:: false = 1

                .. data:: true = 2

                """

                false = Enum.YLeaf(1, "false")

                true = Enum.YLeaf(2, "true")


            class Mplsvpnvrfbgppathattrorigin(Enum):
                """
                Mplsvpnvrfbgppathattrorigin

                The ultimate origin of the path

                information.

                .. data:: igp = 1

                .. data:: egp = 2

                .. data:: incomplete = 3

                """

                igp = Enum.YLeaf(1, "igp")

                egp = Enum.YLeaf(2, "egp")

                incomplete = Enum.YLeaf(3, "incomplete")


            def has_data(self):
                return (
                    self.mplsvpnvrfname.is_set or
                    self.mplsvpnvrfbgppathattripaddrprefix.is_set or
                    self.mplsvpnvrfbgppathattripaddrprefixlen.is_set or
                    self.mplsvpnvrfbgppathattrpeer.is_set or
                    self.mplsvpnvrfbgppathattraggregatoraddr.is_set or
                    self.mplsvpnvrfbgppathattraggregatoras.is_set or
                    self.mplsvpnvrfbgppathattraspathsegment.is_set or
                    self.mplsvpnvrfbgppathattratomicaggregate.is_set or
                    self.mplsvpnvrfbgppathattrbest.is_set or
                    self.mplsvpnvrfbgppathattrcalclocalpref.is_set or
                    self.mplsvpnvrfbgppathattrlocalpref.is_set or
                    self.mplsvpnvrfbgppathattrmultiexitdisc.is_set or
                    self.mplsvpnvrfbgppathattrnexthop.is_set or
                    self.mplsvpnvrfbgppathattrorigin.is_set or
                    self.mplsvpnvrfbgppathattrunknown.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mplsvpnvrfname.yfilter != YFilter.not_set or
                    self.mplsvpnvrfbgppathattripaddrprefix.yfilter != YFilter.not_set or
                    self.mplsvpnvrfbgppathattripaddrprefixlen.yfilter != YFilter.not_set or
                    self.mplsvpnvrfbgppathattrpeer.yfilter != YFilter.not_set or
                    self.mplsvpnvrfbgppathattraggregatoraddr.yfilter != YFilter.not_set or
                    self.mplsvpnvrfbgppathattraggregatoras.yfilter != YFilter.not_set or
                    self.mplsvpnvrfbgppathattraspathsegment.yfilter != YFilter.not_set or
                    self.mplsvpnvrfbgppathattratomicaggregate.yfilter != YFilter.not_set or
                    self.mplsvpnvrfbgppathattrbest.yfilter != YFilter.not_set or
                    self.mplsvpnvrfbgppathattrcalclocalpref.yfilter != YFilter.not_set or
                    self.mplsvpnvrfbgppathattrlocalpref.yfilter != YFilter.not_set or
                    self.mplsvpnvrfbgppathattrmultiexitdisc.yfilter != YFilter.not_set or
                    self.mplsvpnvrfbgppathattrnexthop.yfilter != YFilter.not_set or
                    self.mplsvpnvrfbgppathattrorigin.yfilter != YFilter.not_set or
                    self.mplsvpnvrfbgppathattrunknown.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mplsVpnVrfBgpNbrPrefixEntry" + "[mplsVpnVrfName='" + self.mplsvpnvrfname.get() + "']" + "[mplsVpnVrfBgpPathAttrIpAddrPrefix='" + self.mplsvpnvrfbgppathattripaddrprefix.get() + "']" + "[mplsVpnVrfBgpPathAttrIpAddrPrefixLen='" + self.mplsvpnvrfbgppathattripaddrprefixlen.get() + "']" + "[mplsVpnVrfBgpPathAttrPeer='" + self.mplsvpnvrfbgppathattrpeer.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "MPLS-VPN-MIB:MPLS-VPN-MIB/mplsVpnVrfBgpNbrPrefixTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.mplsvpnvrfname.is_set or self.mplsvpnvrfname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfname.get_name_leafdata())
                if (self.mplsvpnvrfbgppathattripaddrprefix.is_set or self.mplsvpnvrfbgppathattripaddrprefix.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfbgppathattripaddrprefix.get_name_leafdata())
                if (self.mplsvpnvrfbgppathattripaddrprefixlen.is_set or self.mplsvpnvrfbgppathattripaddrprefixlen.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfbgppathattripaddrprefixlen.get_name_leafdata())
                if (self.mplsvpnvrfbgppathattrpeer.is_set or self.mplsvpnvrfbgppathattrpeer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfbgppathattrpeer.get_name_leafdata())
                if (self.mplsvpnvrfbgppathattraggregatoraddr.is_set or self.mplsvpnvrfbgppathattraggregatoraddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfbgppathattraggregatoraddr.get_name_leafdata())
                if (self.mplsvpnvrfbgppathattraggregatoras.is_set or self.mplsvpnvrfbgppathattraggregatoras.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfbgppathattraggregatoras.get_name_leafdata())
                if (self.mplsvpnvrfbgppathattraspathsegment.is_set or self.mplsvpnvrfbgppathattraspathsegment.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfbgppathattraspathsegment.get_name_leafdata())
                if (self.mplsvpnvrfbgppathattratomicaggregate.is_set or self.mplsvpnvrfbgppathattratomicaggregate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfbgppathattratomicaggregate.get_name_leafdata())
                if (self.mplsvpnvrfbgppathattrbest.is_set or self.mplsvpnvrfbgppathattrbest.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfbgppathattrbest.get_name_leafdata())
                if (self.mplsvpnvrfbgppathattrcalclocalpref.is_set or self.mplsvpnvrfbgppathattrcalclocalpref.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfbgppathattrcalclocalpref.get_name_leafdata())
                if (self.mplsvpnvrfbgppathattrlocalpref.is_set or self.mplsvpnvrfbgppathattrlocalpref.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfbgppathattrlocalpref.get_name_leafdata())
                if (self.mplsvpnvrfbgppathattrmultiexitdisc.is_set or self.mplsvpnvrfbgppathattrmultiexitdisc.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfbgppathattrmultiexitdisc.get_name_leafdata())
                if (self.mplsvpnvrfbgppathattrnexthop.is_set or self.mplsvpnvrfbgppathattrnexthop.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfbgppathattrnexthop.get_name_leafdata())
                if (self.mplsvpnvrfbgppathattrorigin.is_set or self.mplsvpnvrfbgppathattrorigin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfbgppathattrorigin.get_name_leafdata())
                if (self.mplsvpnvrfbgppathattrunknown.is_set or self.mplsvpnvrfbgppathattrunknown.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfbgppathattrunknown.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mplsVpnVrfName" or name == "mplsVpnVrfBgpPathAttrIpAddrPrefix" or name == "mplsVpnVrfBgpPathAttrIpAddrPrefixLen" or name == "mplsVpnVrfBgpPathAttrPeer" or name == "mplsVpnVrfBgpPathAttrAggregatorAddr" or name == "mplsVpnVrfBgpPathAttrAggregatorAS" or name == "mplsVpnVrfBgpPathAttrASPathSegment" or name == "mplsVpnVrfBgpPathAttrAtomicAggregate" or name == "mplsVpnVrfBgpPathAttrBest" or name == "mplsVpnVrfBgpPathAttrCalcLocalPref" or name == "mplsVpnVrfBgpPathAttrLocalPref" or name == "mplsVpnVrfBgpPathAttrMultiExitDisc" or name == "mplsVpnVrfBgpPathAttrNextHop" or name == "mplsVpnVrfBgpPathAttrOrigin" or name == "mplsVpnVrfBgpPathAttrUnknown"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "mplsVpnVrfName"):
                    self.mplsvpnvrfname = value
                    self.mplsvpnvrfname.value_namespace = name_space
                    self.mplsvpnvrfname.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfBgpPathAttrIpAddrPrefix"):
                    self.mplsvpnvrfbgppathattripaddrprefix = value
                    self.mplsvpnvrfbgppathattripaddrprefix.value_namespace = name_space
                    self.mplsvpnvrfbgppathattripaddrprefix.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfBgpPathAttrIpAddrPrefixLen"):
                    self.mplsvpnvrfbgppathattripaddrprefixlen = value
                    self.mplsvpnvrfbgppathattripaddrprefixlen.value_namespace = name_space
                    self.mplsvpnvrfbgppathattripaddrprefixlen.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfBgpPathAttrPeer"):
                    self.mplsvpnvrfbgppathattrpeer = value
                    self.mplsvpnvrfbgppathattrpeer.value_namespace = name_space
                    self.mplsvpnvrfbgppathattrpeer.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfBgpPathAttrAggregatorAddr"):
                    self.mplsvpnvrfbgppathattraggregatoraddr = value
                    self.mplsvpnvrfbgppathattraggregatoraddr.value_namespace = name_space
                    self.mplsvpnvrfbgppathattraggregatoraddr.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfBgpPathAttrAggregatorAS"):
                    self.mplsvpnvrfbgppathattraggregatoras = value
                    self.mplsvpnvrfbgppathattraggregatoras.value_namespace = name_space
                    self.mplsvpnvrfbgppathattraggregatoras.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfBgpPathAttrASPathSegment"):
                    self.mplsvpnvrfbgppathattraspathsegment = value
                    self.mplsvpnvrfbgppathattraspathsegment.value_namespace = name_space
                    self.mplsvpnvrfbgppathattraspathsegment.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfBgpPathAttrAtomicAggregate"):
                    self.mplsvpnvrfbgppathattratomicaggregate = value
                    self.mplsvpnvrfbgppathattratomicaggregate.value_namespace = name_space
                    self.mplsvpnvrfbgppathattratomicaggregate.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfBgpPathAttrBest"):
                    self.mplsvpnvrfbgppathattrbest = value
                    self.mplsvpnvrfbgppathattrbest.value_namespace = name_space
                    self.mplsvpnvrfbgppathattrbest.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfBgpPathAttrCalcLocalPref"):
                    self.mplsvpnvrfbgppathattrcalclocalpref = value
                    self.mplsvpnvrfbgppathattrcalclocalpref.value_namespace = name_space
                    self.mplsvpnvrfbgppathattrcalclocalpref.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfBgpPathAttrLocalPref"):
                    self.mplsvpnvrfbgppathattrlocalpref = value
                    self.mplsvpnvrfbgppathattrlocalpref.value_namespace = name_space
                    self.mplsvpnvrfbgppathattrlocalpref.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfBgpPathAttrMultiExitDisc"):
                    self.mplsvpnvrfbgppathattrmultiexitdisc = value
                    self.mplsvpnvrfbgppathattrmultiexitdisc.value_namespace = name_space
                    self.mplsvpnvrfbgppathattrmultiexitdisc.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfBgpPathAttrNextHop"):
                    self.mplsvpnvrfbgppathattrnexthop = value
                    self.mplsvpnvrfbgppathattrnexthop.value_namespace = name_space
                    self.mplsvpnvrfbgppathattrnexthop.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfBgpPathAttrOrigin"):
                    self.mplsvpnvrfbgppathattrorigin = value
                    self.mplsvpnvrfbgppathattrorigin.value_namespace = name_space
                    self.mplsvpnvrfbgppathattrorigin.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfBgpPathAttrUnknown"):
                    self.mplsvpnvrfbgppathattrunknown = value
                    self.mplsvpnvrfbgppathattrunknown.value_namespace = name_space
                    self.mplsvpnvrfbgppathattrunknown.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.mplsvpnvrfbgpnbrprefixentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.mplsvpnvrfbgpnbrprefixentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mplsVpnVrfBgpNbrPrefixTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "MPLS-VPN-MIB:MPLS-VPN-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mplsVpnVrfBgpNbrPrefixEntry"):
                for c in self.mplsvpnvrfbgpnbrprefixentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = MplsVpnMib.Mplsvpnvrfbgpnbrprefixtable.Mplsvpnvrfbgpnbrprefixentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mplsvpnvrfbgpnbrprefixentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mplsVpnVrfBgpNbrPrefixEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Mplsvpnvrfroutetable(Entity):
        """
        This table specifies per\-interface MPLS/BGP VPN VRF Table
        routing information. Entries in this table define VRF routing
        entries associated with the specified MPLS/VPN interfaces. Note
        that this table contains both BGP and IGP routes, as both may
        appear in the same VRF.
        
        .. attribute:: mplsvpnvrfrouteentry
        
        	An entry in this table is created by an LSR for every route present configured (either dynamically or statically) within the context of a specific VRF capable of supporting MPLS/BGP VPN. The indexing provides an ordering of VRFs per\-VPN interface
        	**type**\: list of    :py:class:`Mplsvpnvrfrouteentry <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrfroutetable.Mplsvpnvrfrouteentry>`
        
        

        """

        _prefix = 'MPLS-VPN-MIB'
        _revision = '2001-10-15'

        def __init__(self):
            super(MplsVpnMib.Mplsvpnvrfroutetable, self).__init__()

            self.yang_name = "mplsVpnVrfRouteTable"
            self.yang_parent_name = "MPLS-VPN-MIB"

            self.mplsvpnvrfrouteentry = YList(self)

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
                        super(MplsVpnMib.Mplsvpnvrfroutetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsVpnMib.Mplsvpnvrfroutetable, self).__setattr__(name, value)


        class Mplsvpnvrfrouteentry(Entity):
            """
            An entry in this table is created by an LSR for every route
            present configured (either dynamically or statically) within
            the context of a specific VRF capable of supporting MPLS/BGP
            VPN. The indexing provides an ordering of VRFs per\-VPN
            interface.
            
            .. attribute:: mplsvpnvrfname  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..31
            
            	**refers to**\:  :py:class:`mplsvpnvrfname <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrftable.Mplsvpnvrfentry>`
            
            .. attribute:: mplsvpnvrfroutedest  <key>
            
            	The destination IP address of this route. This object may not take a Multicast (Class D) address value.  Any assignment (implicit or otherwise) of an instance of this object to a value x must be rejected if the bit\-wise logical\-AND of x with the value of the corresponding instance of the mplsVpnVrfRouteMask object is not equal to x
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: mplsvpnvrfroutemask  <key>
            
            	Indicate the mask to be logical\-ANDed with the destination  address  before  being compared to the value  in  the  mplsVpnVrfRouteDest field. For those  systems  that  do  not support arbitrary subnet masks, an agent constructs the value of the mplsVpnVrfRouteMask by reference   to the IP Address Class.  Any assignment (implicit or otherwise) of an instance of this object to a value x must be rejected if the bit\-wise logical\-AND of x with the value of the corresponding instance of the mplsVpnVrfRouteDest object is not equal to mplsVpnVrfRouteDest
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: mplsvpnvrfroutetos  <key>
            
            	The IP TOS Field is used to specify the policy to be applied to this route.  The encoding of IP TOS is as specified  by  the  following convention. Zero indicates the default path if no more specific policy applies.  +\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+ \|                 \|                       \|     \| \|   PRECEDENCE    \|    TYPE OF SERVICE    \|  0  \| \|                 \|                       \|     \| +\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+             IP TOS                IP TOS       Field     Policy      Field     Policy       Contents    Code      Contents    Code       0 0 0 0  ==>   0      0 0 0 1  ==>   2       0 0 1 0  ==>   4      0 0 1 1  ==>   6       0 1 0 0  ==>   8      0 1 0 1  ==>  10       0 1 1 0  ==>  12      0 1 1 1  ==>  14       1 0 0 0  ==>  16      1 0 0 1  ==>  18       1 0 1 0  ==>  20      1 0 1 1  ==>  22       1 1 0 0  ==>  24      1 1 0 1  ==>  26       1 1 1 0  ==>  28      1 1 1 1  ==>  30
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfroutenexthop  <key>
            
            	On remote routes, the address of the next system en route; Otherwise, 0.0.0.0. 
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: mplsvpnvrfrouteage
            
            	The number of seconds since this route was last updated or otherwise determined to be correct. Note that no semantics of `too old' can be implied except through knowledge of the routing protocol by which the route was learned
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfroutedestaddrtype
            
            	The address type of the mplsVpnVrfRouteDest entry
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: mplsvpnvrfrouteifindex
            
            	The ifIndex value that identifies the local interface  through  which  the next hop of this route should be reached
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: mplsvpnvrfrouteinfo
            
            	A reference to MIB definitions specific to the particular routing protocol which is responsi\-   ble for this route, as determined by the  value specified  in the route's mplsVpnVrfRouteProto value. If this information is not present, its value SHOULD be set to the OBJECT IDENTIFIER { 0 0 }, which is a syntactically valid object identif\-ier, and any implementation conforming to ASN.1 and the Basic Encoding Rules must be able to generate and recognize this value
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: mplsvpnvrfroutemaskaddrtype
            
            	The address type of mplsVpnVrfRouteMask
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: mplsvpnvrfroutemetric1
            
            	The primary routing metric for this route. The semantics of this metric are determined by the routing\-protocol specified in  the  route's mplsVpnVrfRouteProto value. If this metric is not used, its value should be set to \-1
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: mplsvpnvrfroutemetric2
            
            	An alternate routing metric for this route. The semantics of this metric are determined by the routing\-protocol specified in  the  route's mplsVpnVrfRouteProto value. If this metric is not used, its value should be set to \-1
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: mplsvpnvrfroutemetric3
            
            	An alternate routing metric for this route. The semantics of this metric are determined by the routing\-protocol specified in  the  route's mplsVpnVrfRouteProto value. If this metric is not used, its value should be set to \-1
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: mplsvpnvrfroutemetric4
            
            	An alternate routing metric for this route. The semantics of this metric are determined by the routing\-protocol specified in  the  route's mplsVpnVrfRouteProto value. If this metric is not used, its value should be set to \-1
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: mplsvpnvrfroutemetric5
            
            	An alternate routing metric for this route. The semantics of this metric are determined by the routing\-protocol specified in  the  route's mplsVpnVrfRouteProto value. If this metric is not used, its value should be set to \-1
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: mplsvpnvrfroutenexthopaddrtype
            
            	The address type of the mplsVpnVrfRouteNextHopAddrType object
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: mplsvpnvrfroutenexthopas
            
            	The Autonomous System Number of the Next Hop. The semantics of this object are determined by the routing\-protocol specified in the route's mplsVpnVrfRouteProto value. When this object is unknown or not relevant its value should be set to zero
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfrouteproto
            
            	The routing mechanism via which this route was learned.  Inclusion of values for gateway rout\- ing protocols is not  intended  to  imply  that hosts should support those protocols
            	**type**\:   :py:class:`Mplsvpnvrfrouteproto <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrfroutetable.Mplsvpnvrfrouteentry.Mplsvpnvrfrouteproto>`
            
            .. attribute:: mplsvpnvrfrouterowstatus
            
            	Row status for this table. It is used according to row installation and removal conventions
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: mplsvpnvrfroutestoragetype
            
            	Storage type value
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            .. attribute:: mplsvpnvrfroutetype
            
            	The type of route.  Note that local(3)  refers to a route for which the next hop is the final destination; remote(4) refers to a route for that the next  hop is not the final destination. Routes which do not result in traffic forwarding or rejection should not be displayed even if the implementation keeps them stored internally.  reject (2) refers to a route which, if matched, discards the message as unreachable. This is used in some protocols as a means of correctly aggregating routes
            	**type**\:   :py:class:`Mplsvpnvrfroutetype <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrfroutetable.Mplsvpnvrfrouteentry.Mplsvpnvrfroutetype>`
            
            

            """

            _prefix = 'MPLS-VPN-MIB'
            _revision = '2001-10-15'

            def __init__(self):
                super(MplsVpnMib.Mplsvpnvrfroutetable.Mplsvpnvrfrouteentry, self).__init__()

                self.yang_name = "mplsVpnVrfRouteEntry"
                self.yang_parent_name = "mplsVpnVrfRouteTable"

                self.mplsvpnvrfname = YLeaf(YType.str, "mplsVpnVrfName")

                self.mplsvpnvrfroutedest = YLeaf(YType.str, "mplsVpnVrfRouteDest")

                self.mplsvpnvrfroutemask = YLeaf(YType.str, "mplsVpnVrfRouteMask")

                self.mplsvpnvrfroutetos = YLeaf(YType.uint32, "mplsVpnVrfRouteTos")

                self.mplsvpnvrfroutenexthop = YLeaf(YType.str, "mplsVpnVrfRouteNextHop")

                self.mplsvpnvrfrouteage = YLeaf(YType.uint32, "mplsVpnVrfRouteAge")

                self.mplsvpnvrfroutedestaddrtype = YLeaf(YType.enumeration, "mplsVpnVrfRouteDestAddrType")

                self.mplsvpnvrfrouteifindex = YLeaf(YType.int32, "mplsVpnVrfRouteIfIndex")

                self.mplsvpnvrfrouteinfo = YLeaf(YType.str, "mplsVpnVrfRouteInfo")

                self.mplsvpnvrfroutemaskaddrtype = YLeaf(YType.enumeration, "mplsVpnVrfRouteMaskAddrType")

                self.mplsvpnvrfroutemetric1 = YLeaf(YType.int32, "mplsVpnVrfRouteMetric1")

                self.mplsvpnvrfroutemetric2 = YLeaf(YType.int32, "mplsVpnVrfRouteMetric2")

                self.mplsvpnvrfroutemetric3 = YLeaf(YType.int32, "mplsVpnVrfRouteMetric3")

                self.mplsvpnvrfroutemetric4 = YLeaf(YType.int32, "mplsVpnVrfRouteMetric4")

                self.mplsvpnvrfroutemetric5 = YLeaf(YType.int32, "mplsVpnVrfRouteMetric5")

                self.mplsvpnvrfroutenexthopaddrtype = YLeaf(YType.enumeration, "mplsVpnVrfRouteNextHopAddrType")

                self.mplsvpnvrfroutenexthopas = YLeaf(YType.uint32, "mplsVpnVrfRouteNextHopAS")

                self.mplsvpnvrfrouteproto = YLeaf(YType.enumeration, "mplsVpnVrfRouteProto")

                self.mplsvpnvrfrouterowstatus = YLeaf(YType.enumeration, "mplsVpnVrfRouteRowStatus")

                self.mplsvpnvrfroutestoragetype = YLeaf(YType.enumeration, "mplsVpnVrfRouteStorageType")

                self.mplsvpnvrfroutetype = YLeaf(YType.enumeration, "mplsVpnVrfRouteType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("mplsvpnvrfname",
                                "mplsvpnvrfroutedest",
                                "mplsvpnvrfroutemask",
                                "mplsvpnvrfroutetos",
                                "mplsvpnvrfroutenexthop",
                                "mplsvpnvrfrouteage",
                                "mplsvpnvrfroutedestaddrtype",
                                "mplsvpnvrfrouteifindex",
                                "mplsvpnvrfrouteinfo",
                                "mplsvpnvrfroutemaskaddrtype",
                                "mplsvpnvrfroutemetric1",
                                "mplsvpnvrfroutemetric2",
                                "mplsvpnvrfroutemetric3",
                                "mplsvpnvrfroutemetric4",
                                "mplsvpnvrfroutemetric5",
                                "mplsvpnvrfroutenexthopaddrtype",
                                "mplsvpnvrfroutenexthopas",
                                "mplsvpnvrfrouteproto",
                                "mplsvpnvrfrouterowstatus",
                                "mplsvpnvrfroutestoragetype",
                                "mplsvpnvrfroutetype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsVpnMib.Mplsvpnvrfroutetable.Mplsvpnvrfrouteentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsVpnMib.Mplsvpnvrfroutetable.Mplsvpnvrfrouteentry, self).__setattr__(name, value)

            class Mplsvpnvrfrouteproto(Enum):
                """
                Mplsvpnvrfrouteproto

                The routing mechanism via which this route was

                learned.  Inclusion of values for gateway rout\-

                ing protocols is not  intended  to  imply  that

                hosts should support those protocols.

                .. data:: other = 1

                .. data:: local = 2

                .. data:: netmgmt = 3

                .. data:: icmp = 4

                .. data:: egp = 5

                .. data:: ggp = 6

                .. data:: hello = 7

                .. data:: rip = 8

                .. data:: isIs = 9

                .. data:: esIs = 10

                .. data:: ciscoIgrp = 11

                .. data:: bbnSpfIgp = 12

                .. data:: ospf = 13

                .. data:: bgp = 14

                .. data:: idpr = 15

                .. data:: ciscoEigrp = 16

                """

                other = Enum.YLeaf(1, "other")

                local = Enum.YLeaf(2, "local")

                netmgmt = Enum.YLeaf(3, "netmgmt")

                icmp = Enum.YLeaf(4, "icmp")

                egp = Enum.YLeaf(5, "egp")

                ggp = Enum.YLeaf(6, "ggp")

                hello = Enum.YLeaf(7, "hello")

                rip = Enum.YLeaf(8, "rip")

                isIs = Enum.YLeaf(9, "isIs")

                esIs = Enum.YLeaf(10, "esIs")

                ciscoIgrp = Enum.YLeaf(11, "ciscoIgrp")

                bbnSpfIgp = Enum.YLeaf(12, "bbnSpfIgp")

                ospf = Enum.YLeaf(13, "ospf")

                bgp = Enum.YLeaf(14, "bgp")

                idpr = Enum.YLeaf(15, "idpr")

                ciscoEigrp = Enum.YLeaf(16, "ciscoEigrp")


            class Mplsvpnvrfroutetype(Enum):
                """
                Mplsvpnvrfroutetype

                The type of route.  Note that local(3)  refers

                to a route for which the next hop is the final

                destination; remote(4) refers to a route for

                that the next  hop is not the final destination.

                Routes which do not result in traffic forwarding or

                rejection should not be displayed even if the

                implementation keeps them stored internally.

                reject (2) refers to a route which, if matched,

                discards the message as unreachable. This is used

                in some protocols as a means of correctly aggregating

                routes.

                .. data:: other = 1

                .. data:: reject = 2

                .. data:: local = 3

                .. data:: remote = 4

                """

                other = Enum.YLeaf(1, "other")

                reject = Enum.YLeaf(2, "reject")

                local = Enum.YLeaf(3, "local")

                remote = Enum.YLeaf(4, "remote")


            def has_data(self):
                return (
                    self.mplsvpnvrfname.is_set or
                    self.mplsvpnvrfroutedest.is_set or
                    self.mplsvpnvrfroutemask.is_set or
                    self.mplsvpnvrfroutetos.is_set or
                    self.mplsvpnvrfroutenexthop.is_set or
                    self.mplsvpnvrfrouteage.is_set or
                    self.mplsvpnvrfroutedestaddrtype.is_set or
                    self.mplsvpnvrfrouteifindex.is_set or
                    self.mplsvpnvrfrouteinfo.is_set or
                    self.mplsvpnvrfroutemaskaddrtype.is_set or
                    self.mplsvpnvrfroutemetric1.is_set or
                    self.mplsvpnvrfroutemetric2.is_set or
                    self.mplsvpnvrfroutemetric3.is_set or
                    self.mplsvpnvrfroutemetric4.is_set or
                    self.mplsvpnvrfroutemetric5.is_set or
                    self.mplsvpnvrfroutenexthopaddrtype.is_set or
                    self.mplsvpnvrfroutenexthopas.is_set or
                    self.mplsvpnvrfrouteproto.is_set or
                    self.mplsvpnvrfrouterowstatus.is_set or
                    self.mplsvpnvrfroutestoragetype.is_set or
                    self.mplsvpnvrfroutetype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mplsvpnvrfname.yfilter != YFilter.not_set or
                    self.mplsvpnvrfroutedest.yfilter != YFilter.not_set or
                    self.mplsvpnvrfroutemask.yfilter != YFilter.not_set or
                    self.mplsvpnvrfroutetos.yfilter != YFilter.not_set or
                    self.mplsvpnvrfroutenexthop.yfilter != YFilter.not_set or
                    self.mplsvpnvrfrouteage.yfilter != YFilter.not_set or
                    self.mplsvpnvrfroutedestaddrtype.yfilter != YFilter.not_set or
                    self.mplsvpnvrfrouteifindex.yfilter != YFilter.not_set or
                    self.mplsvpnvrfrouteinfo.yfilter != YFilter.not_set or
                    self.mplsvpnvrfroutemaskaddrtype.yfilter != YFilter.not_set or
                    self.mplsvpnvrfroutemetric1.yfilter != YFilter.not_set or
                    self.mplsvpnvrfroutemetric2.yfilter != YFilter.not_set or
                    self.mplsvpnvrfroutemetric3.yfilter != YFilter.not_set or
                    self.mplsvpnvrfroutemetric4.yfilter != YFilter.not_set or
                    self.mplsvpnvrfroutemetric5.yfilter != YFilter.not_set or
                    self.mplsvpnvrfroutenexthopaddrtype.yfilter != YFilter.not_set or
                    self.mplsvpnvrfroutenexthopas.yfilter != YFilter.not_set or
                    self.mplsvpnvrfrouteproto.yfilter != YFilter.not_set or
                    self.mplsvpnvrfrouterowstatus.yfilter != YFilter.not_set or
                    self.mplsvpnvrfroutestoragetype.yfilter != YFilter.not_set or
                    self.mplsvpnvrfroutetype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mplsVpnVrfRouteEntry" + "[mplsVpnVrfName='" + self.mplsvpnvrfname.get() + "']" + "[mplsVpnVrfRouteDest='" + self.mplsvpnvrfroutedest.get() + "']" + "[mplsVpnVrfRouteMask='" + self.mplsvpnvrfroutemask.get() + "']" + "[mplsVpnVrfRouteTos='" + self.mplsvpnvrfroutetos.get() + "']" + "[mplsVpnVrfRouteNextHop='" + self.mplsvpnvrfroutenexthop.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "MPLS-VPN-MIB:MPLS-VPN-MIB/mplsVpnVrfRouteTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.mplsvpnvrfname.is_set or self.mplsvpnvrfname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfname.get_name_leafdata())
                if (self.mplsvpnvrfroutedest.is_set or self.mplsvpnvrfroutedest.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfroutedest.get_name_leafdata())
                if (self.mplsvpnvrfroutemask.is_set or self.mplsvpnvrfroutemask.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfroutemask.get_name_leafdata())
                if (self.mplsvpnvrfroutetos.is_set or self.mplsvpnvrfroutetos.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfroutetos.get_name_leafdata())
                if (self.mplsvpnvrfroutenexthop.is_set or self.mplsvpnvrfroutenexthop.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfroutenexthop.get_name_leafdata())
                if (self.mplsvpnvrfrouteage.is_set or self.mplsvpnvrfrouteage.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfrouteage.get_name_leafdata())
                if (self.mplsvpnvrfroutedestaddrtype.is_set or self.mplsvpnvrfroutedestaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfroutedestaddrtype.get_name_leafdata())
                if (self.mplsvpnvrfrouteifindex.is_set or self.mplsvpnvrfrouteifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfrouteifindex.get_name_leafdata())
                if (self.mplsvpnvrfrouteinfo.is_set or self.mplsvpnvrfrouteinfo.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfrouteinfo.get_name_leafdata())
                if (self.mplsvpnvrfroutemaskaddrtype.is_set or self.mplsvpnvrfroutemaskaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfroutemaskaddrtype.get_name_leafdata())
                if (self.mplsvpnvrfroutemetric1.is_set or self.mplsvpnvrfroutemetric1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfroutemetric1.get_name_leafdata())
                if (self.mplsvpnvrfroutemetric2.is_set or self.mplsvpnvrfroutemetric2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfroutemetric2.get_name_leafdata())
                if (self.mplsvpnvrfroutemetric3.is_set or self.mplsvpnvrfroutemetric3.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfroutemetric3.get_name_leafdata())
                if (self.mplsvpnvrfroutemetric4.is_set or self.mplsvpnvrfroutemetric4.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfroutemetric4.get_name_leafdata())
                if (self.mplsvpnvrfroutemetric5.is_set or self.mplsvpnvrfroutemetric5.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfroutemetric5.get_name_leafdata())
                if (self.mplsvpnvrfroutenexthopaddrtype.is_set or self.mplsvpnvrfroutenexthopaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfroutenexthopaddrtype.get_name_leafdata())
                if (self.mplsvpnvrfroutenexthopas.is_set or self.mplsvpnvrfroutenexthopas.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfroutenexthopas.get_name_leafdata())
                if (self.mplsvpnvrfrouteproto.is_set or self.mplsvpnvrfrouteproto.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfrouteproto.get_name_leafdata())
                if (self.mplsvpnvrfrouterowstatus.is_set or self.mplsvpnvrfrouterowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfrouterowstatus.get_name_leafdata())
                if (self.mplsvpnvrfroutestoragetype.is_set or self.mplsvpnvrfroutestoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfroutestoragetype.get_name_leafdata())
                if (self.mplsvpnvrfroutetype.is_set or self.mplsvpnvrfroutetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsvpnvrfroutetype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mplsVpnVrfName" or name == "mplsVpnVrfRouteDest" or name == "mplsVpnVrfRouteMask" or name == "mplsVpnVrfRouteTos" or name == "mplsVpnVrfRouteNextHop" or name == "mplsVpnVrfRouteAge" or name == "mplsVpnVrfRouteDestAddrType" or name == "mplsVpnVrfRouteIfIndex" or name == "mplsVpnVrfRouteInfo" or name == "mplsVpnVrfRouteMaskAddrType" or name == "mplsVpnVrfRouteMetric1" or name == "mplsVpnVrfRouteMetric2" or name == "mplsVpnVrfRouteMetric3" or name == "mplsVpnVrfRouteMetric4" or name == "mplsVpnVrfRouteMetric5" or name == "mplsVpnVrfRouteNextHopAddrType" or name == "mplsVpnVrfRouteNextHopAS" or name == "mplsVpnVrfRouteProto" or name == "mplsVpnVrfRouteRowStatus" or name == "mplsVpnVrfRouteStorageType" or name == "mplsVpnVrfRouteType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "mplsVpnVrfName"):
                    self.mplsvpnvrfname = value
                    self.mplsvpnvrfname.value_namespace = name_space
                    self.mplsvpnvrfname.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfRouteDest"):
                    self.mplsvpnvrfroutedest = value
                    self.mplsvpnvrfroutedest.value_namespace = name_space
                    self.mplsvpnvrfroutedest.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfRouteMask"):
                    self.mplsvpnvrfroutemask = value
                    self.mplsvpnvrfroutemask.value_namespace = name_space
                    self.mplsvpnvrfroutemask.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfRouteTos"):
                    self.mplsvpnvrfroutetos = value
                    self.mplsvpnvrfroutetos.value_namespace = name_space
                    self.mplsvpnvrfroutetos.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfRouteNextHop"):
                    self.mplsvpnvrfroutenexthop = value
                    self.mplsvpnvrfroutenexthop.value_namespace = name_space
                    self.mplsvpnvrfroutenexthop.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfRouteAge"):
                    self.mplsvpnvrfrouteage = value
                    self.mplsvpnvrfrouteage.value_namespace = name_space
                    self.mplsvpnvrfrouteage.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfRouteDestAddrType"):
                    self.mplsvpnvrfroutedestaddrtype = value
                    self.mplsvpnvrfroutedestaddrtype.value_namespace = name_space
                    self.mplsvpnvrfroutedestaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfRouteIfIndex"):
                    self.mplsvpnvrfrouteifindex = value
                    self.mplsvpnvrfrouteifindex.value_namespace = name_space
                    self.mplsvpnvrfrouteifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfRouteInfo"):
                    self.mplsvpnvrfrouteinfo = value
                    self.mplsvpnvrfrouteinfo.value_namespace = name_space
                    self.mplsvpnvrfrouteinfo.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfRouteMaskAddrType"):
                    self.mplsvpnvrfroutemaskaddrtype = value
                    self.mplsvpnvrfroutemaskaddrtype.value_namespace = name_space
                    self.mplsvpnvrfroutemaskaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfRouteMetric1"):
                    self.mplsvpnvrfroutemetric1 = value
                    self.mplsvpnvrfroutemetric1.value_namespace = name_space
                    self.mplsvpnvrfroutemetric1.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfRouteMetric2"):
                    self.mplsvpnvrfroutemetric2 = value
                    self.mplsvpnvrfroutemetric2.value_namespace = name_space
                    self.mplsvpnvrfroutemetric2.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfRouteMetric3"):
                    self.mplsvpnvrfroutemetric3 = value
                    self.mplsvpnvrfroutemetric3.value_namespace = name_space
                    self.mplsvpnvrfroutemetric3.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfRouteMetric4"):
                    self.mplsvpnvrfroutemetric4 = value
                    self.mplsvpnvrfroutemetric4.value_namespace = name_space
                    self.mplsvpnvrfroutemetric4.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfRouteMetric5"):
                    self.mplsvpnvrfroutemetric5 = value
                    self.mplsvpnvrfroutemetric5.value_namespace = name_space
                    self.mplsvpnvrfroutemetric5.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfRouteNextHopAddrType"):
                    self.mplsvpnvrfroutenexthopaddrtype = value
                    self.mplsvpnvrfroutenexthopaddrtype.value_namespace = name_space
                    self.mplsvpnvrfroutenexthopaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfRouteNextHopAS"):
                    self.mplsvpnvrfroutenexthopas = value
                    self.mplsvpnvrfroutenexthopas.value_namespace = name_space
                    self.mplsvpnvrfroutenexthopas.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfRouteProto"):
                    self.mplsvpnvrfrouteproto = value
                    self.mplsvpnvrfrouteproto.value_namespace = name_space
                    self.mplsvpnvrfrouteproto.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfRouteRowStatus"):
                    self.mplsvpnvrfrouterowstatus = value
                    self.mplsvpnvrfrouterowstatus.value_namespace = name_space
                    self.mplsvpnvrfrouterowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfRouteStorageType"):
                    self.mplsvpnvrfroutestoragetype = value
                    self.mplsvpnvrfroutestoragetype.value_namespace = name_space
                    self.mplsvpnvrfroutestoragetype.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsVpnVrfRouteType"):
                    self.mplsvpnvrfroutetype = value
                    self.mplsvpnvrfroutetype.value_namespace = name_space
                    self.mplsvpnvrfroutetype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.mplsvpnvrfrouteentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.mplsvpnvrfrouteentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mplsVpnVrfRouteTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "MPLS-VPN-MIB:MPLS-VPN-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mplsVpnVrfRouteEntry"):
                for c in self.mplsvpnvrfrouteentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = MplsVpnMib.Mplsvpnvrfroutetable.Mplsvpnvrfrouteentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mplsvpnvrfrouteentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mplsVpnVrfRouteEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.mplsvpninterfaceconftable is not None and self.mplsvpninterfaceconftable.has_data()) or
            (self.mplsvpnscalars is not None and self.mplsvpnscalars.has_data()) or
            (self.mplsvpnvrfbgpnbraddrtable is not None and self.mplsvpnvrfbgpnbraddrtable.has_data()) or
            (self.mplsvpnvrfbgpnbrprefixtable is not None and self.mplsvpnvrfbgpnbrprefixtable.has_data()) or
            (self.mplsvpnvrfroutetable is not None and self.mplsvpnvrfroutetable.has_data()) or
            (self.mplsvpnvrfroutetargettable is not None and self.mplsvpnvrfroutetargettable.has_data()) or
            (self.mplsvpnvrftable is not None and self.mplsvpnvrftable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.mplsvpninterfaceconftable is not None and self.mplsvpninterfaceconftable.has_operation()) or
            (self.mplsvpnscalars is not None and self.mplsvpnscalars.has_operation()) or
            (self.mplsvpnvrfbgpnbraddrtable is not None and self.mplsvpnvrfbgpnbraddrtable.has_operation()) or
            (self.mplsvpnvrfbgpnbrprefixtable is not None and self.mplsvpnvrfbgpnbrprefixtable.has_operation()) or
            (self.mplsvpnvrfroutetable is not None and self.mplsvpnvrfroutetable.has_operation()) or
            (self.mplsvpnvrfroutetargettable is not None and self.mplsvpnvrfroutetargettable.has_operation()) or
            (self.mplsvpnvrftable is not None and self.mplsvpnvrftable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "MPLS-VPN-MIB:MPLS-VPN-MIB" + path_buffer

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

        if (child_yang_name == "mplsVpnInterfaceConfTable"):
            if (self.mplsvpninterfaceconftable is None):
                self.mplsvpninterfaceconftable = MplsVpnMib.Mplsvpninterfaceconftable()
                self.mplsvpninterfaceconftable.parent = self
                self._children_name_map["mplsvpninterfaceconftable"] = "mplsVpnInterfaceConfTable"
            return self.mplsvpninterfaceconftable

        if (child_yang_name == "mplsVpnScalars"):
            if (self.mplsvpnscalars is None):
                self.mplsvpnscalars = MplsVpnMib.Mplsvpnscalars()
                self.mplsvpnscalars.parent = self
                self._children_name_map["mplsvpnscalars"] = "mplsVpnScalars"
            return self.mplsvpnscalars

        if (child_yang_name == "mplsVpnVrfBgpNbrAddrTable"):
            if (self.mplsvpnvrfbgpnbraddrtable is None):
                self.mplsvpnvrfbgpnbraddrtable = MplsVpnMib.Mplsvpnvrfbgpnbraddrtable()
                self.mplsvpnvrfbgpnbraddrtable.parent = self
                self._children_name_map["mplsvpnvrfbgpnbraddrtable"] = "mplsVpnVrfBgpNbrAddrTable"
            return self.mplsvpnvrfbgpnbraddrtable

        if (child_yang_name == "mplsVpnVrfBgpNbrPrefixTable"):
            if (self.mplsvpnvrfbgpnbrprefixtable is None):
                self.mplsvpnvrfbgpnbrprefixtable = MplsVpnMib.Mplsvpnvrfbgpnbrprefixtable()
                self.mplsvpnvrfbgpnbrprefixtable.parent = self
                self._children_name_map["mplsvpnvrfbgpnbrprefixtable"] = "mplsVpnVrfBgpNbrPrefixTable"
            return self.mplsvpnvrfbgpnbrprefixtable

        if (child_yang_name == "mplsVpnVrfRouteTable"):
            if (self.mplsvpnvrfroutetable is None):
                self.mplsvpnvrfroutetable = MplsVpnMib.Mplsvpnvrfroutetable()
                self.mplsvpnvrfroutetable.parent = self
                self._children_name_map["mplsvpnvrfroutetable"] = "mplsVpnVrfRouteTable"
            return self.mplsvpnvrfroutetable

        if (child_yang_name == "mplsVpnVrfRouteTargetTable"):
            if (self.mplsvpnvrfroutetargettable is None):
                self.mplsvpnvrfroutetargettable = MplsVpnMib.Mplsvpnvrfroutetargettable()
                self.mplsvpnvrfroutetargettable.parent = self
                self._children_name_map["mplsvpnvrfroutetargettable"] = "mplsVpnVrfRouteTargetTable"
            return self.mplsvpnvrfroutetargettable

        if (child_yang_name == "mplsVpnVrfTable"):
            if (self.mplsvpnvrftable is None):
                self.mplsvpnvrftable = MplsVpnMib.Mplsvpnvrftable()
                self.mplsvpnvrftable.parent = self
                self._children_name_map["mplsvpnvrftable"] = "mplsVpnVrfTable"
            return self.mplsvpnvrftable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "mplsVpnInterfaceConfTable" or name == "mplsVpnScalars" or name == "mplsVpnVrfBgpNbrAddrTable" or name == "mplsVpnVrfBgpNbrPrefixTable" or name == "mplsVpnVrfRouteTable" or name == "mplsVpnVrfRouteTargetTable" or name == "mplsVpnVrfTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = MplsVpnMib()
        return self._top_entity


""" CISCO_IF_EXTENSION_MIB 

A MIB module for extending the IF\-MIB (RFC2863)
to add objects which provide additional information
about interfaces not available in other MIBS.
This MIB replaces the OLD\-CISCO\-INTERFACES\-MIB.

GLOSSARY \:

Virtual Switch \- A physical switch partitioned into 
        multiple logical switches.

Interface Sharing \- An interface can be shared among 
        multiple virtual switches.

Speed Group \- An interface is capable of operating in any one of
the speed range depending on the capability of the hardware.

Virtual Link (VL) \- Virtual Link is a logical connectivity 
    between two end points. A physical interface can 
    have multiple Virtual Links.

No Drop Virtual Link \- According to 802.3 standard, 
    No drop specifies lossless service on a virtual link.

Drop Virtual Link \- According to 802.3 standard,
    Traffic drop may occur on this virtual Link.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Ifindexpersistencestate(Enum):
    """
    Ifindexpersistencestate

    This textual convention is used to define the state of ifIndex

    Persistence for both global as well as interface level.

    The global object, cieIfIndexGlobalPersistence can have two

    state of ifIndex Persistence i.e. either enable or disable. At

    interface level, the object cieIfIndexPersistenceControl can

    take all the three values enable/disable/global.

    .. data:: disable = 1

    .. data:: enable = 2

    .. data:: global_ = 3

    """

    disable = Enum.YLeaf(1, "disable")

    enable = Enum.YLeaf(2, "enable")

    global_ = Enum.YLeaf(3, "global")



class CiscoIfExtensionMib(Entity):
    """
    
    
    .. attribute:: cieifdot1dbasemappingtable
    
    	This table contains the mappings of the ifIndex of an interface to its corresponding dot1dBasePort value
    	**type**\:   :py:class:`Cieifdot1Dbasemappingtable <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CiscoIfExtensionMib.Cieifdot1Dbasemappingtable>`
    
    .. attribute:: cieifdot1qcustomethertypetable
    
    	A list of the interfaces that support the 802.1q custom Ethertype feature
    	**type**\:   :py:class:`Cieifdot1Qcustomethertypetable <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CiscoIfExtensionMib.Cieifdot1Qcustomethertypetable>`
    
    .. attribute:: cieifindexpersistencetable
    
    	This table lists configuration data relating to ifIndex persistence.  This table has a sparse dependent relationship on the ifTable, containing a row for each ifEntry corresponding to an interface for which ifIndex persistence is supported
    	**type**\:   :py:class:`Cieifindexpersistencetable <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CiscoIfExtensionMib.Cieifindexpersistencetable>`
    
    .. attribute:: cieifinterfacetable
    
    	This  table contains objects which provide more information about interface   properties not available in IF\-MIB (RFC 2863).  Some objects defined in this table may be applicable to physical interfaces only. As a result, this table may be sparse for logical interfaces
    	**type**\:   :py:class:`Cieifinterfacetable <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CiscoIfExtensionMib.Cieifinterfacetable>`
    
    .. attribute:: cieifnamemappingtable
    
    	This table contains objects for providing the 'ifName' to 'ifIndex' mapping. This table contains one entry for each valid 'ifName' available in the system. Upon the first request, the implementation of this table will get all the available ifNames, and it will populate the entries in this table, it maintains this ifNames in a cache for ~30 seconds
    	**type**\:   :py:class:`Cieifnamemappingtable <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CiscoIfExtensionMib.Cieifnamemappingtable>`
    
    .. attribute:: cieifpacketstatstable
    
    	This  table contains interface packet statistics which are not available in  IF\-MIB(RFC2863).   As an example, some interfaces to which objects in this table are applicable are as follows \:          o Ethernet         o FastEthernet         o ATM         o BRI         o Sonet         o GigabitEthernet  Some objects defined in this table may be  applicable to physical interfaces only. As a result, this table may be sparse for some logical interfaces
    	**type**\:   :py:class:`Cieifpacketstatstable <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CiscoIfExtensionMib.Cieifpacketstatstable>`
    
    .. attribute:: cieifstatuslisttable
    
    	This table contains objects for providing the 'ifIndex', interface operational mode and  interface operational cause for all the  interfaces in the modules.  This table contains one entry for each  64 interfaces in an module.  This table provides efficient way of encoding  'ifIndex', interface operational mode and interface operational cause, from the point  of retrieval, by combining the values a set  of 64 interfaces in a single MIB object
    	**type**\:   :py:class:`Cieifstatuslisttable <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CiscoIfExtensionMib.Cieifstatuslisttable>`
    
    .. attribute:: cieifutiltable
    
    	This table contains the interface utilization rates for inbound and outbound traffic on an interface
    	**type**\:   :py:class:`Cieifutiltable <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CiscoIfExtensionMib.Cieifutiltable>`
    
    .. attribute:: cieifvlstatstable
    
    	This table contains VL (Virtual Link) statistics for a capable interface.  Objects defined in this table may be  applicable to physical interfaces only
    	**type**\:   :py:class:`Cieifvlstatstable <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CiscoIfExtensionMib.Cieifvlstatstable>`
    
    .. attribute:: ciscoifextsystemconfig
    
    	
    	**type**\:   :py:class:`Ciscoifextsystemconfig <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CiscoIfExtensionMib.Ciscoifextsystemconfig>`
    
    

    """

    _prefix = 'CISCO-IF-EXTENSION-MIB'
    _revision = '2013-03-13'

    def __init__(self):
        super(CiscoIfExtensionMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IF-EXTENSION-MIB"
        self.yang_parent_name = "CISCO-IF-EXTENSION-MIB"

        self.cieifdot1dbasemappingtable = CiscoIfExtensionMib.Cieifdot1Dbasemappingtable()
        self.cieifdot1dbasemappingtable.parent = self
        self._children_name_map["cieifdot1dbasemappingtable"] = "cieIfDot1dBaseMappingTable"
        self._children_yang_names.add("cieIfDot1dBaseMappingTable")

        self.cieifdot1qcustomethertypetable = CiscoIfExtensionMib.Cieifdot1Qcustomethertypetable()
        self.cieifdot1qcustomethertypetable.parent = self
        self._children_name_map["cieifdot1qcustomethertypetable"] = "cieIfDot1qCustomEtherTypeTable"
        self._children_yang_names.add("cieIfDot1qCustomEtherTypeTable")

        self.cieifindexpersistencetable = CiscoIfExtensionMib.Cieifindexpersistencetable()
        self.cieifindexpersistencetable.parent = self
        self._children_name_map["cieifindexpersistencetable"] = "cieIfIndexPersistenceTable"
        self._children_yang_names.add("cieIfIndexPersistenceTable")

        self.cieifinterfacetable = CiscoIfExtensionMib.Cieifinterfacetable()
        self.cieifinterfacetable.parent = self
        self._children_name_map["cieifinterfacetable"] = "cieIfInterfaceTable"
        self._children_yang_names.add("cieIfInterfaceTable")

        self.cieifnamemappingtable = CiscoIfExtensionMib.Cieifnamemappingtable()
        self.cieifnamemappingtable.parent = self
        self._children_name_map["cieifnamemappingtable"] = "cieIfNameMappingTable"
        self._children_yang_names.add("cieIfNameMappingTable")

        self.cieifpacketstatstable = CiscoIfExtensionMib.Cieifpacketstatstable()
        self.cieifpacketstatstable.parent = self
        self._children_name_map["cieifpacketstatstable"] = "cieIfPacketStatsTable"
        self._children_yang_names.add("cieIfPacketStatsTable")

        self.cieifstatuslisttable = CiscoIfExtensionMib.Cieifstatuslisttable()
        self.cieifstatuslisttable.parent = self
        self._children_name_map["cieifstatuslisttable"] = "cieIfStatusListTable"
        self._children_yang_names.add("cieIfStatusListTable")

        self.cieifutiltable = CiscoIfExtensionMib.Cieifutiltable()
        self.cieifutiltable.parent = self
        self._children_name_map["cieifutiltable"] = "cieIfUtilTable"
        self._children_yang_names.add("cieIfUtilTable")

        self.cieifvlstatstable = CiscoIfExtensionMib.Cieifvlstatstable()
        self.cieifvlstatstable.parent = self
        self._children_name_map["cieifvlstatstable"] = "cieIfVlStatsTable"
        self._children_yang_names.add("cieIfVlStatsTable")

        self.ciscoifextsystemconfig = CiscoIfExtensionMib.Ciscoifextsystemconfig()
        self.ciscoifextsystemconfig.parent = self
        self._children_name_map["ciscoifextsystemconfig"] = "ciscoIfExtSystemConfig"
        self._children_yang_names.add("ciscoIfExtSystemConfig")


    class Ciscoifextsystemconfig(Entity):
        """
        
        
        .. attribute:: ciedelayedlinkupdownnotifdelay
        
        	This object specifies the interval of time an interface's operational status must remain stable following a transition before the system will generate a cieDelayedLinkUpDownNotif
        	**type**\:  int
        
        	**range:** 1..60
        
        	**units**\: minutes
        
        .. attribute:: ciedelayedlinkupdownnotifenable
        
        	This object specifies whether the system generates a cieDelayedLinkUpDownNotif notification
        	**type**\:  bool
        
        .. attribute:: cieifindexglobalpersistence
        
        	This object specifies whether ifIndex values persist across reinitialization of the device.  ifIndex persistence means that the mapping between the ifDescr object values and the ifIndex object values will be retained across reboots.  Applications such as device inventory, billing, and fault detection depend on the maintenance of the correspondence between particular ifIndex values and their interfaces. During reboot or insertion of a new card, the data to correlate the interfaces to the ifIndex may become invalid in absence of ifIndex persistence feature.  ifIndex persistence for an interface ensures ifIndex value for the interface will remain the same after a system reboot. Hence, this feature allows users to avoid the workarounds required for consistent interface identification across reinitialization.  The allowed values for this object are either enable or disable. global value is not allowed
        	**type**\:   :py:class:`Ifindexpersistencestate <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.Ifindexpersistencestate>`
        
        .. attribute:: cieifindexpersistence
        
        	This object specifies whether ifIndex values persist across reinitialization of the device.  ifIndex persistence means that the mapping between the ifDescr object values and the ifIndex object values will be retained across reboots.  Applications such as device inventory, billing, and fault detection depend on the maintenance of the correspondence between particular ifIndex values and their interfaces. During reboot or insertion of a new card, the data to correlate the interfaces to the ifIndex may become invalid in absence of ifIndex persistence feature.  ifIndex persistence for an interface ensures ifIndex value for the interface will remain the same after a system reboot. Hence, this feature allows users to avoid the workarounds required for consistent interface identification across reinitialization.  Due to change in syntax, this object is deprecated by cieIfIndexGlobalPersistence
        	**type**\:  bool
        
        	**status**\: deprecated
        
        .. attribute:: cielinkupdownconfig
        
        	This object specifies whether standard mib\-II defined linkUp/ linkDown, extended linkUp/linkDown (with extra varbinds in addition to the varbinds defined in linkUp/linkDown) or cieLinkUp/cieLinkDown notifications should be generated for the interfaces in the system.  'standardLinkUp'     \- generate standard defined mib\-II                         linkUp notification if                         'ifLinkUpDownTrapEnable' for the                         interface is 'enabled'. 'standardLinkDown'   \- generate standard defined mib\-II                         linkDown notification if                         'ifLinkUpDownTrapEnable' for the                         interface is 'enabled'.   'additionalLinkUp'   \- generate linkUp notification with                        additional varbinds if                         'ifLinkUpDownTrapEnable' for the                         interface is 'enabled'.   'additionalLinkDown' \- generate linkDown notification with                        additional varbinds if                         'ifLinkUpDownTrapEnable' for the                         interface is 'enabled'. 'ciscoLinkUp'        \- generate cieLinkUp notification                        if the 'ifLinkUpDownTrapEnable' for the                        interface is 'enabled'. 'ciscoLinkDown'      \- generate cieLinkDown notification                        if the 'ifLinkUpDownTrapEnable' for the                        interface is 'enabled'.  If multiple bits are set then multiple notifications will be generated for an interface if the 'ifLinkUpDownTrapEnable'  for the interface is 'enabled'
        	**type**\:   :py:class:`Cielinkupdownconfig <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CiscoIfExtensionMib.Ciscoifextsystemconfig.Cielinkupdownconfig>`
        
        .. attribute:: cielinkupdownenable
        
        	Indicates whether cieLinkUp/cieLinkDown or standard mib\-II defined linkUp/Down or both, notifications should be generated for the interfaces in the system.  'standard'  \- only generate standard defined               mib\-II linkUp/linkDown notification               if 'ifLinkUpDownTrapEnable' for                the interface is 'enabled'. 'cisco'     \- only generate cieLinkUp/cieLinkDown               notifications for an interface if               the 'ifLinkUpDownTrapEnable' for the               interface is 'enabled'.  If both bits are selected then linkUp/linkDown and cieLinkUp/cieLinkDown are both generated for an  interface if the 'ifLinkUpDownTrapEnable' for the interface is 'enabled'
        	**type**\:   :py:class:`Cielinkupdownenable <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CiscoIfExtensionMib.Ciscoifextsystemconfig.Cielinkupdownenable>`
        
        	**status**\: deprecated
        
        .. attribute:: ciestandardlinkupdownvarbinds
        
        	Indicates whether to send the extra varbinds in addition to the varbinds defined  in linkUp/linkDown notifications.  'standard'   \- only send the varbinds defined in                the standard linkUp/linkDown                notification.   'additional' \- send the extra varbinds in addition                 to the defined ones. 'other'      \- any other config not covered by the above.                This value is read\-only
        	**type**\:   :py:class:`Ciestandardlinkupdownvarbinds <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CiscoIfExtensionMib.Ciscoifextsystemconfig.Ciestandardlinkupdownvarbinds>`
        
        	**status**\: deprecated
        
        .. attribute:: ciesystemmtu
        
        	Global system MTU in octets. This object specifies the MTU on all interfaces. However, the value specified by cieIfMtu takes precedence for an interface, which means that the interface's MTU uses the value specified by cieIfMtu, if it is configured
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        

        """

        _prefix = 'CISCO-IF-EXTENSION-MIB'
        _revision = '2013-03-13'

        def __init__(self):
            super(CiscoIfExtensionMib.Ciscoifextsystemconfig, self).__init__()

            self.yang_name = "ciscoIfExtSystemConfig"
            self.yang_parent_name = "CISCO-IF-EXTENSION-MIB"

            self.ciedelayedlinkupdownnotifdelay = YLeaf(YType.uint32, "cieDelayedLinkUpDownNotifDelay")

            self.ciedelayedlinkupdownnotifenable = YLeaf(YType.boolean, "cieDelayedLinkUpDownNotifEnable")

            self.cieifindexglobalpersistence = YLeaf(YType.enumeration, "cieIfIndexGlobalPersistence")

            self.cieifindexpersistence = YLeaf(YType.boolean, "cieIfIndexPersistence")

            self.cielinkupdownconfig = YLeaf(YType.bits, "cieLinkUpDownConfig")

            self.cielinkupdownenable = YLeaf(YType.bits, "cieLinkUpDownEnable")

            self.ciestandardlinkupdownvarbinds = YLeaf(YType.enumeration, "cieStandardLinkUpDownVarbinds")

            self.ciesystemmtu = YLeaf(YType.int32, "cieSystemMtu")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("ciedelayedlinkupdownnotifdelay",
                            "ciedelayedlinkupdownnotifenable",
                            "cieifindexglobalpersistence",
                            "cieifindexpersistence",
                            "cielinkupdownconfig",
                            "cielinkupdownenable",
                            "ciestandardlinkupdownvarbinds",
                            "ciesystemmtu") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoIfExtensionMib.Ciscoifextsystemconfig, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIfExtensionMib.Ciscoifextsystemconfig, self).__setattr__(name, value)

        class Ciestandardlinkupdownvarbinds(Enum):
            """
            Ciestandardlinkupdownvarbinds

            Indicates whether to send the extra

            varbinds in addition to the varbinds defined 

            in linkUp/linkDown notifications.

            'standard'   \- only send the varbinds defined in

                           the standard linkUp/linkDown

                           notification.  

            'additional' \- send the extra varbinds in addition 

                           to the defined ones.

            'other'      \- any other config not covered by the above.

                           This value is read\-only.

            .. data:: standard = 1

            .. data:: additional = 2

            .. data:: other = 3

            """

            standard = Enum.YLeaf(1, "standard")

            additional = Enum.YLeaf(2, "additional")

            other = Enum.YLeaf(3, "other")


        def has_data(self):
            return (
                self.ciedelayedlinkupdownnotifdelay.is_set or
                self.ciedelayedlinkupdownnotifenable.is_set or
                self.cieifindexglobalpersistence.is_set or
                self.cieifindexpersistence.is_set or
                self.cielinkupdownconfig.is_set or
                self.cielinkupdownenable.is_set or
                self.ciestandardlinkupdownvarbinds.is_set or
                self.ciesystemmtu.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.ciedelayedlinkupdownnotifdelay.yfilter != YFilter.not_set or
                self.ciedelayedlinkupdownnotifenable.yfilter != YFilter.not_set or
                self.cieifindexglobalpersistence.yfilter != YFilter.not_set or
                self.cieifindexpersistence.yfilter != YFilter.not_set or
                self.cielinkupdownconfig.yfilter != YFilter.not_set or
                self.cielinkupdownenable.yfilter != YFilter.not_set or
                self.ciestandardlinkupdownvarbinds.yfilter != YFilter.not_set or
                self.ciesystemmtu.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ciscoIfExtSystemConfig" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.ciedelayedlinkupdownnotifdelay.is_set or self.ciedelayedlinkupdownnotifdelay.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ciedelayedlinkupdownnotifdelay.get_name_leafdata())
            if (self.ciedelayedlinkupdownnotifenable.is_set or self.ciedelayedlinkupdownnotifenable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ciedelayedlinkupdownnotifenable.get_name_leafdata())
            if (self.cieifindexglobalpersistence.is_set or self.cieifindexglobalpersistence.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cieifindexglobalpersistence.get_name_leafdata())
            if (self.cieifindexpersistence.is_set or self.cieifindexpersistence.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cieifindexpersistence.get_name_leafdata())
            if (self.cielinkupdownconfig.is_set or self.cielinkupdownconfig.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cielinkupdownconfig.get_name_leafdata())
            if (self.cielinkupdownenable.is_set or self.cielinkupdownenable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cielinkupdownenable.get_name_leafdata())
            if (self.ciestandardlinkupdownvarbinds.is_set or self.ciestandardlinkupdownvarbinds.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ciestandardlinkupdownvarbinds.get_name_leafdata())
            if (self.ciesystemmtu.is_set or self.ciesystemmtu.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ciesystemmtu.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cieDelayedLinkUpDownNotifDelay" or name == "cieDelayedLinkUpDownNotifEnable" or name == "cieIfIndexGlobalPersistence" or name == "cieIfIndexPersistence" or name == "cieLinkUpDownConfig" or name == "cieLinkUpDownEnable" or name == "cieStandardLinkUpDownVarbinds" or name == "cieSystemMtu"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cieDelayedLinkUpDownNotifDelay"):
                self.ciedelayedlinkupdownnotifdelay = value
                self.ciedelayedlinkupdownnotifdelay.value_namespace = name_space
                self.ciedelayedlinkupdownnotifdelay.value_namespace_prefix = name_space_prefix
            if(value_path == "cieDelayedLinkUpDownNotifEnable"):
                self.ciedelayedlinkupdownnotifenable = value
                self.ciedelayedlinkupdownnotifenable.value_namespace = name_space
                self.ciedelayedlinkupdownnotifenable.value_namespace_prefix = name_space_prefix
            if(value_path == "cieIfIndexGlobalPersistence"):
                self.cieifindexglobalpersistence = value
                self.cieifindexglobalpersistence.value_namespace = name_space
                self.cieifindexglobalpersistence.value_namespace_prefix = name_space_prefix
            if(value_path == "cieIfIndexPersistence"):
                self.cieifindexpersistence = value
                self.cieifindexpersistence.value_namespace = name_space
                self.cieifindexpersistence.value_namespace_prefix = name_space_prefix
            if(value_path == "cieLinkUpDownConfig"):
                self.cielinkupdownconfig[value] = True
            if(value_path == "cieLinkUpDownEnable"):
                self.cielinkupdownenable[value] = True
            if(value_path == "cieStandardLinkUpDownVarbinds"):
                self.ciestandardlinkupdownvarbinds = value
                self.ciestandardlinkupdownvarbinds.value_namespace = name_space
                self.ciestandardlinkupdownvarbinds.value_namespace_prefix = name_space_prefix
            if(value_path == "cieSystemMtu"):
                self.ciesystemmtu = value
                self.ciesystemmtu.value_namespace = name_space
                self.ciesystemmtu.value_namespace_prefix = name_space_prefix


    class Cieifpacketstatstable(Entity):
        """
        This  table contains interface packet
        statistics which are not available in 
        IF\-MIB(RFC2863). 
        
        As an example, some interfaces to which
        objects in this table are applicable are
        as follows \:
        
                o Ethernet
                o FastEthernet
                o ATM
                o BRI
                o Sonet
                o GigabitEthernet
        
        Some objects defined in this table may be 
        applicable to physical interfaces only.
        As a result, this table may be sparse for
        some logical interfaces.
        
        .. attribute:: cieifpacketstatsentry
        
        	An entry into the cieIfPacketStatsTable
        	**type**\: list of    :py:class:`Cieifpacketstatsentry <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CiscoIfExtensionMib.Cieifpacketstatstable.Cieifpacketstatsentry>`
        
        

        """

        _prefix = 'CISCO-IF-EXTENSION-MIB'
        _revision = '2013-03-13'

        def __init__(self):
            super(CiscoIfExtensionMib.Cieifpacketstatstable, self).__init__()

            self.yang_name = "cieIfPacketStatsTable"
            self.yang_parent_name = "CISCO-IF-EXTENSION-MIB"

            self.cieifpacketstatsentry = YList(self)

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
                        super(CiscoIfExtensionMib.Cieifpacketstatstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIfExtensionMib.Cieifpacketstatstable, self).__setattr__(name, value)


        class Cieifpacketstatsentry(Entity):
            """
            An entry into the cieIfPacketStatsTable.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: cieifinaborterrs
            
            	Number of input packets which were dropped because the receiver aborted.  Examples of this could be when an abort sequence aborted the input frame or when there is a collision in an ethernet segment.  Discontinuities in the value of this variable can occur at re\-initialization of the management system, and at other times as  indicated by the values of  cieIfPacketDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cieifinframingerrs
            
            	The number of input packets on a physical interface which were misaligned or had framing errors. This happens when the  format of the incoming packet on a physical interface is incorrect.  Discontinuities in the value of this variable can occur at re\-initialization of the management system, and at other times as  indicated by the values of  cieIfPacketDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cieifingiantserrs
            
            	The number of input packets on a particular physical interface which were dropped as  they were larger than the ifMtu (largest  permitted  size of a packet which can be  sent/received on an interface).  Discontinuities in the value of this variable can occur at re\-initialization of the management system, and at other times as  indicated by the values of  cieIfPacketDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cieifinignored
            
            	The number of input packets which were simply ignored by this physical interface due to  insufficient resources to handle the incoming packets.  For example, this could indicate that the input receive buffers are not available or that the receiver lost a packet.  Discontinuities in the value of this variable can occur at re\-initialization of the management system, and at other times as  indicated by the values of  cieIfPacketDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cieifinoverrunerrs
            
            	The number of input packets which arrived on a particular physical interface which  were too quick for the hardware to receive and hence the receiver ran out of buffers.  Discontinuities in the value of this variable can occur at re\-initialization of the management system, and at other times as  indicated by the values of  cieIfPacketDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cieifinputqueuedrops
            
            	The number of input packets which were dropped.  Some reasons why this object could be  incremented are\:  o  Input queue is full. o  Errors at the receiver hardware     while receiving the packet.  Discontinuities in the value of this variable can occur at re\-initialization of the management system, and at other times as  indicated by the values of  cieIfPacketDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cieifinruntserrs
            
            	The number of packets input on a particular physical interface which were dropped as they were smaller than the minimum allowable  physical media limit.  Discontinuities in the value of this variable can occur at re\-initialization of the management system, and at other times as  indicated by the values of  cieIfPacketDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cieiflastintime
            
            	This object represents the elapsed time in milliseconds since last protocol input  packet was received.  Discontinuities in the value of this variable can occur at re\-initialization of the management system, and at other times as  indicated by the values of  cieIfPacketDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cieiflastouthangtime
            
            	This object represents the elapsed time in milliseconds since last protocol    output packet could not be successfully transmitted.  Discontinuities in the value of this variable can occur at re\-initialization of the management system, and at other times as  indicated by the values of  cieIfPacketDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cieiflastouttime
            
            	This object represents the elapsed time in milliseconds since last protocol  output  packet was transmitted.  Discontinuities in the value of this variable can occur at re\-initialization of the management system, and at other times as  indicated by the values of  cieIfPacketDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cieifoutputqueuedrops
            
            	This object indicates the  number of output packets dropped by the interface even though no error had been detected to prevent them being transmitted.   The packet could be dropped for many reasons, which could range from the interface being down to errors in the format of the packet.  Discontinuities in the value of this variable can occur at re\-initialization of the management system, and at other times as  indicated by the values of  cieIfPacketDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cieifpacketdiscontinuitytime
            
            	The value of sysUpTime on the most recent occasion at which this interface's  counters suffered a discontinuity.   If no such discontinuities have occurred  since the last re\-initialization of the  local management subsystem, then this  object contains a value of zero
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IF-EXTENSION-MIB'
            _revision = '2013-03-13'

            def __init__(self):
                super(CiscoIfExtensionMib.Cieifpacketstatstable.Cieifpacketstatsentry, self).__init__()

                self.yang_name = "cieIfPacketStatsEntry"
                self.yang_parent_name = "cieIfPacketStatsTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.cieifinaborterrs = YLeaf(YType.uint32, "cieIfInAbortErrs")

                self.cieifinframingerrs = YLeaf(YType.uint32, "cieIfInFramingErrs")

                self.cieifingiantserrs = YLeaf(YType.uint32, "cieIfInGiantsErrs")

                self.cieifinignored = YLeaf(YType.uint32, "cieIfInIgnored")

                self.cieifinoverrunerrs = YLeaf(YType.uint32, "cieIfInOverrunErrs")

                self.cieifinputqueuedrops = YLeaf(YType.uint32, "cieIfInputQueueDrops")

                self.cieifinruntserrs = YLeaf(YType.uint32, "cieIfInRuntsErrs")

                self.cieiflastintime = YLeaf(YType.uint32, "cieIfLastInTime")

                self.cieiflastouthangtime = YLeaf(YType.uint32, "cieIfLastOutHangTime")

                self.cieiflastouttime = YLeaf(YType.uint32, "cieIfLastOutTime")

                self.cieifoutputqueuedrops = YLeaf(YType.uint32, "cieIfOutputQueueDrops")

                self.cieifpacketdiscontinuitytime = YLeaf(YType.uint32, "cieIfPacketDiscontinuityTime")

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
                                "cieifinaborterrs",
                                "cieifinframingerrs",
                                "cieifingiantserrs",
                                "cieifinignored",
                                "cieifinoverrunerrs",
                                "cieifinputqueuedrops",
                                "cieifinruntserrs",
                                "cieiflastintime",
                                "cieiflastouthangtime",
                                "cieiflastouttime",
                                "cieifoutputqueuedrops",
                                "cieifpacketdiscontinuitytime") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIfExtensionMib.Cieifpacketstatstable.Cieifpacketstatsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIfExtensionMib.Cieifpacketstatstable.Cieifpacketstatsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.cieifinaborterrs.is_set or
                    self.cieifinframingerrs.is_set or
                    self.cieifingiantserrs.is_set or
                    self.cieifinignored.is_set or
                    self.cieifinoverrunerrs.is_set or
                    self.cieifinputqueuedrops.is_set or
                    self.cieifinruntserrs.is_set or
                    self.cieiflastintime.is_set or
                    self.cieiflastouthangtime.is_set or
                    self.cieiflastouttime.is_set or
                    self.cieifoutputqueuedrops.is_set or
                    self.cieifpacketdiscontinuitytime.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.cieifinaborterrs.yfilter != YFilter.not_set or
                    self.cieifinframingerrs.yfilter != YFilter.not_set or
                    self.cieifingiantserrs.yfilter != YFilter.not_set or
                    self.cieifinignored.yfilter != YFilter.not_set or
                    self.cieifinoverrunerrs.yfilter != YFilter.not_set or
                    self.cieifinputqueuedrops.yfilter != YFilter.not_set or
                    self.cieifinruntserrs.yfilter != YFilter.not_set or
                    self.cieiflastintime.yfilter != YFilter.not_set or
                    self.cieiflastouthangtime.yfilter != YFilter.not_set or
                    self.cieiflastouttime.yfilter != YFilter.not_set or
                    self.cieifoutputqueuedrops.yfilter != YFilter.not_set or
                    self.cieifpacketdiscontinuitytime.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cieIfPacketStatsEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/cieIfPacketStatsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.cieifinaborterrs.is_set or self.cieifinaborterrs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifinaborterrs.get_name_leafdata())
                if (self.cieifinframingerrs.is_set or self.cieifinframingerrs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifinframingerrs.get_name_leafdata())
                if (self.cieifingiantserrs.is_set or self.cieifingiantserrs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifingiantserrs.get_name_leafdata())
                if (self.cieifinignored.is_set or self.cieifinignored.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifinignored.get_name_leafdata())
                if (self.cieifinoverrunerrs.is_set or self.cieifinoverrunerrs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifinoverrunerrs.get_name_leafdata())
                if (self.cieifinputqueuedrops.is_set or self.cieifinputqueuedrops.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifinputqueuedrops.get_name_leafdata())
                if (self.cieifinruntserrs.is_set or self.cieifinruntserrs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifinruntserrs.get_name_leafdata())
                if (self.cieiflastintime.is_set or self.cieiflastintime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieiflastintime.get_name_leafdata())
                if (self.cieiflastouthangtime.is_set or self.cieiflastouthangtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieiflastouthangtime.get_name_leafdata())
                if (self.cieiflastouttime.is_set or self.cieiflastouttime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieiflastouttime.get_name_leafdata())
                if (self.cieifoutputqueuedrops.is_set or self.cieifoutputqueuedrops.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifoutputqueuedrops.get_name_leafdata())
                if (self.cieifpacketdiscontinuitytime.is_set or self.cieifpacketdiscontinuitytime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifpacketdiscontinuitytime.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "cieIfInAbortErrs" or name == "cieIfInFramingErrs" or name == "cieIfInGiantsErrs" or name == "cieIfInIgnored" or name == "cieIfInOverrunErrs" or name == "cieIfInputQueueDrops" or name == "cieIfInRuntsErrs" or name == "cieIfLastInTime" or name == "cieIfLastOutHangTime" or name == "cieIfLastOutTime" or name == "cieIfOutputQueueDrops" or name == "cieIfPacketDiscontinuityTime"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfInAbortErrs"):
                    self.cieifinaborterrs = value
                    self.cieifinaborterrs.value_namespace = name_space
                    self.cieifinaborterrs.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfInFramingErrs"):
                    self.cieifinframingerrs = value
                    self.cieifinframingerrs.value_namespace = name_space
                    self.cieifinframingerrs.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfInGiantsErrs"):
                    self.cieifingiantserrs = value
                    self.cieifingiantserrs.value_namespace = name_space
                    self.cieifingiantserrs.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfInIgnored"):
                    self.cieifinignored = value
                    self.cieifinignored.value_namespace = name_space
                    self.cieifinignored.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfInOverrunErrs"):
                    self.cieifinoverrunerrs = value
                    self.cieifinoverrunerrs.value_namespace = name_space
                    self.cieifinoverrunerrs.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfInputQueueDrops"):
                    self.cieifinputqueuedrops = value
                    self.cieifinputqueuedrops.value_namespace = name_space
                    self.cieifinputqueuedrops.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfInRuntsErrs"):
                    self.cieifinruntserrs = value
                    self.cieifinruntserrs.value_namespace = name_space
                    self.cieifinruntserrs.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfLastInTime"):
                    self.cieiflastintime = value
                    self.cieiflastintime.value_namespace = name_space
                    self.cieiflastintime.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfLastOutHangTime"):
                    self.cieiflastouthangtime = value
                    self.cieiflastouthangtime.value_namespace = name_space
                    self.cieiflastouthangtime.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfLastOutTime"):
                    self.cieiflastouttime = value
                    self.cieiflastouttime.value_namespace = name_space
                    self.cieiflastouttime.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfOutputQueueDrops"):
                    self.cieifoutputqueuedrops = value
                    self.cieifoutputqueuedrops.value_namespace = name_space
                    self.cieifoutputqueuedrops.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfPacketDiscontinuityTime"):
                    self.cieifpacketdiscontinuitytime = value
                    self.cieifpacketdiscontinuitytime.value_namespace = name_space
                    self.cieifpacketdiscontinuitytime.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cieifpacketstatsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cieifpacketstatsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cieIfPacketStatsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cieIfPacketStatsEntry"):
                for c in self.cieifpacketstatsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIfExtensionMib.Cieifpacketstatstable.Cieifpacketstatsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cieifpacketstatsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cieIfPacketStatsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cieifinterfacetable(Entity):
        """
        This  table contains objects which provide
        more information about interface  
        properties not available in IF\-MIB
        (RFC 2863).
        
        Some objects defined in this table may be
        applicable to physical interfaces only.
        As a result, this table may be sparse for
        logical interfaces.
        
        .. attribute:: cieifinterfaceentry
        
        	An entry into the cieIfInterfaceTable
        	**type**\: list of    :py:class:`Cieifinterfaceentry <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CiscoIfExtensionMib.Cieifinterfacetable.Cieifinterfaceentry>`
        
        

        """

        _prefix = 'CISCO-IF-EXTENSION-MIB'
        _revision = '2013-03-13'

        def __init__(self):
            super(CiscoIfExtensionMib.Cieifinterfacetable, self).__init__()

            self.yang_name = "cieIfInterfaceTable"
            self.yang_parent_name = "CISCO-IF-EXTENSION-MIB"

            self.cieifinterfaceentry = YList(self)

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
                        super(CiscoIfExtensionMib.Cieifinterfacetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIfExtensionMib.Cieifinterfacetable, self).__setattr__(name, value)


        class Cieifinterfaceentry(Entity):
            """
            An entry into the cieIfInterfaceTable.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: cieifcarriertransitioncount
            
            	Number of times interface saw the carrier signal transition.  For example, if a T1 line is unplugged,  then framer will detect the loss of signal  (LOS) on the line  and will count it as a transition.  Discontinuities in the value of this variable can occur at re\-initialization of the management system, and at other times as  indicated by the values of  cieIfInterfaceDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cieifcontextname
            
            	The ContextName denotes the interface 'context' and is used to logically separate the MIB management. RFC 2571 and RFC 2737 describe this approach. When the agent supports a different SNMP  context, as detailed in RFC 2571 and  RFC 2737, for different interfaces, then the value of this object specifies the context name used for this interface
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: cieifdhcpmode
            
            	The DHCP mode configured by the administrator. If 'true' the DHCP is enabled. In which case an IP address is requested in DHCP. This is in addition to any that are  configured by the administrator in 'ciiIPAddressTable' or 'ciiIPIfAddressTable' in CISCO\-IP\-IF\-MIB. If 'false' the DHCP is disabled. In which case all IP addresses are configured by the administrator in 'ciiIPAddressTable' or  'ciiIPIfAddressTable'. For interfaces, for which DHCP cannot be or is not supported, then this object has the value 'false'
            	**type**\:  bool
            
            .. attribute:: cieiffillpatternconfig
            
            	This object specifies the current switchport fill pattern configuration on the given interface.  'arbff8G' \- the inter frame gap fill pattern is 			ARBFF for 8G speed. 'idle8G' \- the inter frame gap fill pattern is 		   IDLE for 8G speed
            	**type**\:   :py:class:`Cieiffillpatternconfig <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CiscoIfExtensionMib.Cieifinterfacetable.Cieifinterfaceentry.Cieiffillpatternconfig>`
            
            .. attribute:: cieifhighspeedreceive
            
            	An estimate of the interface's current receive bandwidth in units of 1,000,000 bits per second.  If this object reports a value of `n' then the speed of the interface is somewhere in the range of `n\-500,000' to `n+499,999'.  For interfaces which do not vary in bandwidth or for those where no accurate estimation can be made, this object should contain the nominal bandwidth.  For a sub\-layer which has no concept of bandwidth, this object should be zero
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cieifignorebiterrorsconfig
            
            	This object specifies the current switchport biterrors configuration on the given interface.  If 'true(1)' the ignore bit errors is enabled.In which case the interface ignores bit errors. If 'false(2)' the ignore bit errors is disabled. In which  case the interface acts on the bit errors.  For interfaces, for which bit errors  is not supported, then this object has the value 'true(1)'
            	**type**\:  bool
            
            .. attribute:: cieifignoreinterruptthresholdconfig
            
            	This object specifies the current interrupt threshold configuration on the given interface.  'If 'true(1)' the ignore interrupt thresholds is enabled. In which case the interface ignores interrupt thresholds. If 'false(2)' the ignore interrupt thresholds is disabled. In which case the interface acts on the interrupt  thresholds.  For interfaces, for which interrupt thresholds  is not supported, then this object has the  value 'true(1)'
            	**type**\:  bool
            
            .. attribute:: cieifinterfacediscontinuitytime
            
            	The value of sysUpTime on the most recent occasion at which this interface's  counters  suffered  a discontinuity.   If no such discontinuities have occurred  since the last re\-initialization of the  local management subsystem, then this  object contains a value of zero
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cieifkeepaliveenabled
            
            	A keepalive is a small, layer\-2 message that is transmitted by a network device  to let directly\-connected network devices know of its presence.  This object returns 'true' if keepalives are enabled on this interface. If keepalives are not enabled, 'false' is returned.  Setting this object to TRUE or FALSE enables or disables (respectively) keepalive on this  interface
            	**type**\:  bool
            
            .. attribute:: cieifmtu
            
            	The MTU configured by the administrator. This object is exactly same as 'ifMtu' in  ifTable from IF\-MIB for the same ifIndex value , except that it is configurable by the administrator. For more description of this object refer to 'ifMtu' in IF\-MIB
            	**type**\:  int
            
            	**range:** 40..2147483647
            
            .. attribute:: cieifoperstatuscause
            
            	This object represents the detailed operational cause reason for the current  operational state of the interface.  The current operational state of the interface  is given by the 'ifOperStatus' defined  in IF\-MIB.   The corresponding instance of  'cieIfOperStatusCauseDescr' must be used to  get the information about the operational  cause value mentioned in this object.  For interfaces whose 'ifOperStatus' is 'down'  the objects 'cieIfOperStatusCause' and  'cieIfOperStatusCauseDescr' together provides  the information about the operational cause  reason and the description of the cause.   The value of this object will be 'none' for all the 'ifOperStatus' values except for  'down'. Its value will be one status cause  defined in the 'IfOperStatusReason' textual  convention if 'ifOperStatus' is 'down'.   The value of this object will be 'other'  if the operational status cause is not one  defined in 'IfOperStatusReason'
            	**type**\:   :py:class:`Ifoperstatusreason <ydk.models.cisco_ios_xe.CISCO_TC.Ifoperstatusreason>`
            
            .. attribute:: cieifoperstatuscausedescr
            
            	The description for the cause of current operational state of the interface, given  by the object 'cieIfOperStatusCause'.  For an interface whose 'ifOperStatus' is not 'down' the value of this object will be  'none'
            	**type**\:  str
            
            .. attribute:: cieifowner
            
            	This data type is used to model an administratively assigned name of the current owner of the interface resource. This  information is taken from the NVT ASCII character set.  It is  suggested that this name contain one or more of the following\:  SnmpEngineID, IP address, management station name, network  manager's name, location, or phone number. SNMP access control is articulated entirely in terms of the  contents of MIB views; access to a particular SNMP object  instance depends only upon its presence or absence in a  particular MIB view and never upon its value or the value of  related object instances. Thus, this object affords resolution of resource contention  only among cooperating managers; this object realizes no access control function with respect to uncooperative parties
            	**type**\:  str
            
            	**length:** 0..80
            
            .. attribute:: cieifresetcount
            
            	The number of times the interface was internally reset and brought up.  Some of the actions which can cause this counter to increment are \:  o  Bringing an interface up using the     interface CLI command.  o  Clearing the interface with the exec    CLI command.  o  Bringing the interface up via SNMP.  Discontinuities in the value of this variable can occur at re\-initialization of the management system, and at other times as  indicated by the values of  cieIfInterfaceDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cieifsharedconfig
            
            	This object indicates the current configuration of interface sharing on the given interface.  'notApplicable' \- the interface sharing configuration on              this interface is not applicable.  'ownerDedicated' \- the interface is in the dedicated mode             to the binding physical interface. 'ownerShared' \- the interface is shared amongst virtual switches          and this interface physically belongs to a its           virtual switch.   'sharedOnly' \- the interface is in purely shared mode
            	**type**\:   :py:class:`Cieifsharedconfig <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CiscoIfExtensionMib.Cieifinterfacetable.Cieifinterfaceentry.Cieifsharedconfig>`
            
            .. attribute:: cieifspeedgroupconfig
            
            	This object specifies the current speed group configuration on the given interface.  'notApplicable' \- the interface speed group configuration on             this interface is not applicable. It is a              read\-only value. '10G' \- the interface speed group configuration on             this interface as 10G. '1G\-2G\-4G\-8G' \- the interface speed group configuration              on this interface as 1G\-2G\-4G\-8G. '2G\-4G\-8G\-16G' \- the interface speed group configuration              on this interface as 2G\-4G\-8G\-16G
            	**type**\:   :py:class:`Cieifspeedgroupconfig <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CiscoIfExtensionMib.Cieifinterfacetable.Cieifinterfaceentry.Cieifspeedgroupconfig>`
            
            .. attribute:: cieifspeedreceive
            
            	An estimate of the interface's current receive bandwidth in bits per second.  This object is provided for interface with asymmetric interface speeds like ADSL and should be used in conjunction with ifSpeed object.  For interfaces which do not vary in bandwidth or for those where no accurate estimation can be made, this object should contain the nominal bandwidth. If the bandwidth of the interface is greater than the maximum value reportable by this object then this object should report its maximum value (4,294,967,295) and ifHighSpeed must be used to report the interace's speed.  For a sub\-layer which has no concept of bandwidth, this object should be zero
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cieifstatechangereason
            
            	This object displays a human\-readable textual string which describes the  cause of the last state change of the  interface.  Examples of the values this object can take are\:  o  'Lost Carrier' o  'administratively down' o  'up' o  'down'
            	**type**\:  str
            
            .. attribute:: cieiftransceiverfrequencyconfig
            
            	This object specifies the current transceiver frequency configuration on the given interface.  'notApplicable' \- the interface transceiver frequency  				  configuration on this interface  				  is not applicable. It is a read\-only value. 'FibreChannel' \- the interface transceiver frequency 				 configuration on this interface as                   Fibre Channel. 'Ethernet'	  \-  the interface transceiver frequency on 				 this interface as Ethernet
            	**type**\:   :py:class:`Cieiftransceiverfrequencyconfig <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CiscoIfExtensionMib.Cieifinterfacetable.Cieifinterfaceentry.Cieiftransceiverfrequencyconfig>`
            
            

            """

            _prefix = 'CISCO-IF-EXTENSION-MIB'
            _revision = '2013-03-13'

            def __init__(self):
                super(CiscoIfExtensionMib.Cieifinterfacetable.Cieifinterfaceentry, self).__init__()

                self.yang_name = "cieIfInterfaceEntry"
                self.yang_parent_name = "cieIfInterfaceTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.cieifcarriertransitioncount = YLeaf(YType.uint32, "cieIfCarrierTransitionCount")

                self.cieifcontextname = YLeaf(YType.str, "cieIfContextName")

                self.cieifdhcpmode = YLeaf(YType.boolean, "cieIfDhcpMode")

                self.cieiffillpatternconfig = YLeaf(YType.enumeration, "cieIfFillPatternConfig")

                self.cieifhighspeedreceive = YLeaf(YType.uint32, "cieIfHighSpeedReceive")

                self.cieifignorebiterrorsconfig = YLeaf(YType.boolean, "cieIfIgnoreBitErrorsConfig")

                self.cieifignoreinterruptthresholdconfig = YLeaf(YType.boolean, "cieIfIgnoreInterruptThresholdConfig")

                self.cieifinterfacediscontinuitytime = YLeaf(YType.uint32, "cieIfInterfaceDiscontinuityTime")

                self.cieifkeepaliveenabled = YLeaf(YType.boolean, "cieIfKeepAliveEnabled")

                self.cieifmtu = YLeaf(YType.int32, "cieIfMtu")

                self.cieifoperstatuscause = YLeaf(YType.enumeration, "cieIfOperStatusCause")

                self.cieifoperstatuscausedescr = YLeaf(YType.str, "cieIfOperStatusCauseDescr")

                self.cieifowner = YLeaf(YType.str, "cieIfOwner")

                self.cieifresetcount = YLeaf(YType.uint32, "cieIfResetCount")

                self.cieifsharedconfig = YLeaf(YType.enumeration, "cieIfSharedConfig")

                self.cieifspeedgroupconfig = YLeaf(YType.enumeration, "cieIfSpeedGroupConfig")

                self.cieifspeedreceive = YLeaf(YType.uint32, "cieIfSpeedReceive")

                self.cieifstatechangereason = YLeaf(YType.str, "cieIfStateChangeReason")

                self.cieiftransceiverfrequencyconfig = YLeaf(YType.enumeration, "cieIfTransceiverFrequencyConfig")

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
                                "cieifcarriertransitioncount",
                                "cieifcontextname",
                                "cieifdhcpmode",
                                "cieiffillpatternconfig",
                                "cieifhighspeedreceive",
                                "cieifignorebiterrorsconfig",
                                "cieifignoreinterruptthresholdconfig",
                                "cieifinterfacediscontinuitytime",
                                "cieifkeepaliveenabled",
                                "cieifmtu",
                                "cieifoperstatuscause",
                                "cieifoperstatuscausedescr",
                                "cieifowner",
                                "cieifresetcount",
                                "cieifsharedconfig",
                                "cieifspeedgroupconfig",
                                "cieifspeedreceive",
                                "cieifstatechangereason",
                                "cieiftransceiverfrequencyconfig") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIfExtensionMib.Cieifinterfacetable.Cieifinterfaceentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIfExtensionMib.Cieifinterfacetable.Cieifinterfaceentry, self).__setattr__(name, value)

            class Cieiffillpatternconfig(Enum):
                """
                Cieiffillpatternconfig

                This object specifies the current switchport fill pattern

                configuration on the given interface.

                'arbff8G' \- the inter frame gap fill pattern is

                			ARBFF for 8G speed.

                'idle8G' \- the inter frame gap fill pattern is

                		   IDLE for 8G speed.

                .. data:: arbff8G = 1

                .. data:: idle8G = 2

                """

                arbff8G = Enum.YLeaf(1, "arbff8G")

                idle8G = Enum.YLeaf(2, "idle8G")


            class Cieifsharedconfig(Enum):
                """
                Cieifsharedconfig

                This object indicates the current configuration of

                interface sharing on the given interface.

                'notApplicable' \- the interface sharing configuration on 

                            this interface is not applicable. 

                'ownerDedicated' \- the interface is in the dedicated mode

                            to the binding physical interface.

                'ownerShared' \- the interface is shared amongst virtual switches

                         and this interface physically belongs to a its 

                         virtual switch.  

                'sharedOnly' \- the interface is in purely shared mode.

                .. data:: notApplicable = 1

                .. data:: ownerDedicated = 2

                .. data:: ownerShared = 3

                .. data:: sharedOnly = 4

                """

                notApplicable = Enum.YLeaf(1, "notApplicable")

                ownerDedicated = Enum.YLeaf(2, "ownerDedicated")

                ownerShared = Enum.YLeaf(3, "ownerShared")

                sharedOnly = Enum.YLeaf(4, "sharedOnly")


            class Cieifspeedgroupconfig(Enum):
                """
                Cieifspeedgroupconfig

                This object specifies the current speed group

                configuration on the given interface.

                'notApplicable' \- the interface speed group configuration on

                            this interface is not applicable. It is a 

                            read\-only value.

                '10G' \- the interface speed group configuration on

                            this interface as 10G.

                '1G\-2G\-4G\-8G' \- the interface speed group configuration 

                            on this interface as 1G\-2G\-4G\-8G.

                '2G\-4G\-8G\-16G' \- the interface speed group configuration 

                            on this interface as 2G\-4G\-8G\-16G.

                .. data:: notApplicable = 1

                .. data:: tenG = 2

                .. data:: oneTwoFourEightG = 3

                .. data:: twoFourEightSixteenG = 4

                """

                notApplicable = Enum.YLeaf(1, "notApplicable")

                tenG = Enum.YLeaf(2, "tenG")

                oneTwoFourEightG = Enum.YLeaf(3, "oneTwoFourEightG")

                twoFourEightSixteenG = Enum.YLeaf(4, "twoFourEightSixteenG")


            class Cieiftransceiverfrequencyconfig(Enum):
                """
                Cieiftransceiverfrequencyconfig

                This object specifies the current transceiver frequency

                configuration on the given interface.

                'notApplicable' \- the interface transceiver frequency 

                				  configuration on this interface 

                				  is not applicable. It is a read\-only value.

                'FibreChannel' \- the interface transceiver frequency

                				 configuration on this interface as 

                                 Fibre Channel.

                'Ethernet'	  \-  the interface transceiver frequency on

                				 this interface as Ethernet.

                .. data:: notApplicable = 1

                .. data:: fibreChannel = 2

                .. data:: ethernet = 3

                """

                notApplicable = Enum.YLeaf(1, "notApplicable")

                fibreChannel = Enum.YLeaf(2, "fibreChannel")

                ethernet = Enum.YLeaf(3, "ethernet")


            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.cieifcarriertransitioncount.is_set or
                    self.cieifcontextname.is_set or
                    self.cieifdhcpmode.is_set or
                    self.cieiffillpatternconfig.is_set or
                    self.cieifhighspeedreceive.is_set or
                    self.cieifignorebiterrorsconfig.is_set or
                    self.cieifignoreinterruptthresholdconfig.is_set or
                    self.cieifinterfacediscontinuitytime.is_set or
                    self.cieifkeepaliveenabled.is_set or
                    self.cieifmtu.is_set or
                    self.cieifoperstatuscause.is_set or
                    self.cieifoperstatuscausedescr.is_set or
                    self.cieifowner.is_set or
                    self.cieifresetcount.is_set or
                    self.cieifsharedconfig.is_set or
                    self.cieifspeedgroupconfig.is_set or
                    self.cieifspeedreceive.is_set or
                    self.cieifstatechangereason.is_set or
                    self.cieiftransceiverfrequencyconfig.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.cieifcarriertransitioncount.yfilter != YFilter.not_set or
                    self.cieifcontextname.yfilter != YFilter.not_set or
                    self.cieifdhcpmode.yfilter != YFilter.not_set or
                    self.cieiffillpatternconfig.yfilter != YFilter.not_set or
                    self.cieifhighspeedreceive.yfilter != YFilter.not_set or
                    self.cieifignorebiterrorsconfig.yfilter != YFilter.not_set or
                    self.cieifignoreinterruptthresholdconfig.yfilter != YFilter.not_set or
                    self.cieifinterfacediscontinuitytime.yfilter != YFilter.not_set or
                    self.cieifkeepaliveenabled.yfilter != YFilter.not_set or
                    self.cieifmtu.yfilter != YFilter.not_set or
                    self.cieifoperstatuscause.yfilter != YFilter.not_set or
                    self.cieifoperstatuscausedescr.yfilter != YFilter.not_set or
                    self.cieifowner.yfilter != YFilter.not_set or
                    self.cieifresetcount.yfilter != YFilter.not_set or
                    self.cieifsharedconfig.yfilter != YFilter.not_set or
                    self.cieifspeedgroupconfig.yfilter != YFilter.not_set or
                    self.cieifspeedreceive.yfilter != YFilter.not_set or
                    self.cieifstatechangereason.yfilter != YFilter.not_set or
                    self.cieiftransceiverfrequencyconfig.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cieIfInterfaceEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/cieIfInterfaceTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.cieifcarriertransitioncount.is_set or self.cieifcarriertransitioncount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifcarriertransitioncount.get_name_leafdata())
                if (self.cieifcontextname.is_set or self.cieifcontextname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifcontextname.get_name_leafdata())
                if (self.cieifdhcpmode.is_set or self.cieifdhcpmode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifdhcpmode.get_name_leafdata())
                if (self.cieiffillpatternconfig.is_set or self.cieiffillpatternconfig.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieiffillpatternconfig.get_name_leafdata())
                if (self.cieifhighspeedreceive.is_set or self.cieifhighspeedreceive.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifhighspeedreceive.get_name_leafdata())
                if (self.cieifignorebiterrorsconfig.is_set or self.cieifignorebiterrorsconfig.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifignorebiterrorsconfig.get_name_leafdata())
                if (self.cieifignoreinterruptthresholdconfig.is_set or self.cieifignoreinterruptthresholdconfig.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifignoreinterruptthresholdconfig.get_name_leafdata())
                if (self.cieifinterfacediscontinuitytime.is_set or self.cieifinterfacediscontinuitytime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifinterfacediscontinuitytime.get_name_leafdata())
                if (self.cieifkeepaliveenabled.is_set or self.cieifkeepaliveenabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifkeepaliveenabled.get_name_leafdata())
                if (self.cieifmtu.is_set or self.cieifmtu.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifmtu.get_name_leafdata())
                if (self.cieifoperstatuscause.is_set or self.cieifoperstatuscause.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifoperstatuscause.get_name_leafdata())
                if (self.cieifoperstatuscausedescr.is_set or self.cieifoperstatuscausedescr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifoperstatuscausedescr.get_name_leafdata())
                if (self.cieifowner.is_set or self.cieifowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifowner.get_name_leafdata())
                if (self.cieifresetcount.is_set or self.cieifresetcount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifresetcount.get_name_leafdata())
                if (self.cieifsharedconfig.is_set or self.cieifsharedconfig.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifsharedconfig.get_name_leafdata())
                if (self.cieifspeedgroupconfig.is_set or self.cieifspeedgroupconfig.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifspeedgroupconfig.get_name_leafdata())
                if (self.cieifspeedreceive.is_set or self.cieifspeedreceive.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifspeedreceive.get_name_leafdata())
                if (self.cieifstatechangereason.is_set or self.cieifstatechangereason.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifstatechangereason.get_name_leafdata())
                if (self.cieiftransceiverfrequencyconfig.is_set or self.cieiftransceiverfrequencyconfig.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieiftransceiverfrequencyconfig.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "cieIfCarrierTransitionCount" or name == "cieIfContextName" or name == "cieIfDhcpMode" or name == "cieIfFillPatternConfig" or name == "cieIfHighSpeedReceive" or name == "cieIfIgnoreBitErrorsConfig" or name == "cieIfIgnoreInterruptThresholdConfig" or name == "cieIfInterfaceDiscontinuityTime" or name == "cieIfKeepAliveEnabled" or name == "cieIfMtu" or name == "cieIfOperStatusCause" or name == "cieIfOperStatusCauseDescr" or name == "cieIfOwner" or name == "cieIfResetCount" or name == "cieIfSharedConfig" or name == "cieIfSpeedGroupConfig" or name == "cieIfSpeedReceive" or name == "cieIfStateChangeReason" or name == "cieIfTransceiverFrequencyConfig"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfCarrierTransitionCount"):
                    self.cieifcarriertransitioncount = value
                    self.cieifcarriertransitioncount.value_namespace = name_space
                    self.cieifcarriertransitioncount.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfContextName"):
                    self.cieifcontextname = value
                    self.cieifcontextname.value_namespace = name_space
                    self.cieifcontextname.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfDhcpMode"):
                    self.cieifdhcpmode = value
                    self.cieifdhcpmode.value_namespace = name_space
                    self.cieifdhcpmode.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfFillPatternConfig"):
                    self.cieiffillpatternconfig = value
                    self.cieiffillpatternconfig.value_namespace = name_space
                    self.cieiffillpatternconfig.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfHighSpeedReceive"):
                    self.cieifhighspeedreceive = value
                    self.cieifhighspeedreceive.value_namespace = name_space
                    self.cieifhighspeedreceive.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfIgnoreBitErrorsConfig"):
                    self.cieifignorebiterrorsconfig = value
                    self.cieifignorebiterrorsconfig.value_namespace = name_space
                    self.cieifignorebiterrorsconfig.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfIgnoreInterruptThresholdConfig"):
                    self.cieifignoreinterruptthresholdconfig = value
                    self.cieifignoreinterruptthresholdconfig.value_namespace = name_space
                    self.cieifignoreinterruptthresholdconfig.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfInterfaceDiscontinuityTime"):
                    self.cieifinterfacediscontinuitytime = value
                    self.cieifinterfacediscontinuitytime.value_namespace = name_space
                    self.cieifinterfacediscontinuitytime.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfKeepAliveEnabled"):
                    self.cieifkeepaliveenabled = value
                    self.cieifkeepaliveenabled.value_namespace = name_space
                    self.cieifkeepaliveenabled.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfMtu"):
                    self.cieifmtu = value
                    self.cieifmtu.value_namespace = name_space
                    self.cieifmtu.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfOperStatusCause"):
                    self.cieifoperstatuscause = value
                    self.cieifoperstatuscause.value_namespace = name_space
                    self.cieifoperstatuscause.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfOperStatusCauseDescr"):
                    self.cieifoperstatuscausedescr = value
                    self.cieifoperstatuscausedescr.value_namespace = name_space
                    self.cieifoperstatuscausedescr.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfOwner"):
                    self.cieifowner = value
                    self.cieifowner.value_namespace = name_space
                    self.cieifowner.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfResetCount"):
                    self.cieifresetcount = value
                    self.cieifresetcount.value_namespace = name_space
                    self.cieifresetcount.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfSharedConfig"):
                    self.cieifsharedconfig = value
                    self.cieifsharedconfig.value_namespace = name_space
                    self.cieifsharedconfig.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfSpeedGroupConfig"):
                    self.cieifspeedgroupconfig = value
                    self.cieifspeedgroupconfig.value_namespace = name_space
                    self.cieifspeedgroupconfig.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfSpeedReceive"):
                    self.cieifspeedreceive = value
                    self.cieifspeedreceive.value_namespace = name_space
                    self.cieifspeedreceive.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfStateChangeReason"):
                    self.cieifstatechangereason = value
                    self.cieifstatechangereason.value_namespace = name_space
                    self.cieifstatechangereason.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfTransceiverFrequencyConfig"):
                    self.cieiftransceiverfrequencyconfig = value
                    self.cieiftransceiverfrequencyconfig.value_namespace = name_space
                    self.cieiftransceiverfrequencyconfig.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cieifinterfaceentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cieifinterfaceentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cieIfInterfaceTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cieIfInterfaceEntry"):
                for c in self.cieifinterfaceentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIfExtensionMib.Cieifinterfacetable.Cieifinterfaceentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cieifinterfaceentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cieIfInterfaceEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cieifstatuslisttable(Entity):
        """
        This table contains objects for providing
        the 'ifIndex', interface operational mode and 
        interface operational cause for all the 
        interfaces in the modules.
        
        This table contains one entry for each 
        64 interfaces in an module.
        
        This table provides efficient way of encoding 
        'ifIndex', interface operational mode and
        interface operational cause, from the point 
        of retrieval, by combining the values a set 
        of 64 interfaces in a single MIB object.
        
        .. attribute:: cieifstatuslistentry
        
        	Each entry represents the 'ifIndex', interface operational mode and interface  operational cause for a set of 64 interfaces  in a module
        	**type**\: list of    :py:class:`Cieifstatuslistentry <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CiscoIfExtensionMib.Cieifstatuslisttable.Cieifstatuslistentry>`
        
        

        """

        _prefix = 'CISCO-IF-EXTENSION-MIB'
        _revision = '2013-03-13'

        def __init__(self):
            super(CiscoIfExtensionMib.Cieifstatuslisttable, self).__init__()

            self.yang_name = "cieIfStatusListTable"
            self.yang_parent_name = "CISCO-IF-EXTENSION-MIB"

            self.cieifstatuslistentry = YList(self)

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
                        super(CiscoIfExtensionMib.Cieifstatuslisttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIfExtensionMib.Cieifstatuslisttable, self).__setattr__(name, value)


        class Cieifstatuslistentry(Entity):
            """
            Each entry represents the 'ifIndex',
            interface operational mode and interface 
            operational cause for a set of 64 interfaces 
            in a module.
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cieifstatuslistindex  <key>
            
            	An arbitrary integer value, greater than zero, which identifies a list of 64 interfaces within a module
            	**type**\:  int
            
            	**range:** 1..33554432
            
            .. attribute:: cieinterfaceownershipbitmap
            
            	This object indicates the status for a set of 64 interfaces in a module regarding whether or not each interface is  administratively assigned a name of the current owner of the  interface resource as per cieIfOwner
            	**type**\:  str
            
            	**length:** 0..8
            
            .. attribute:: cieinterfacesindex
            
            	This object represents the 'ifIndex' for a set of 64 interfaces in the module
            	**type**\:  str
            
            	**length:** 0..256
            
            .. attribute:: cieinterfacesopercause
            
            	This object represents the operational status cause for a set of 64 interfaces in the  module
            	**type**\:  str
            
            	**length:** 0..128
            
            .. attribute:: cieinterfacesopermode
            
            	This object represents the operational mode for a set of 64 interfaces in the module
            	**type**\:  str
            
            	**length:** 0..64
            
            

            """

            _prefix = 'CISCO-IF-EXTENSION-MIB'
            _revision = '2013-03-13'

            def __init__(self):
                super(CiscoIfExtensionMib.Cieifstatuslisttable.Cieifstatuslistentry, self).__init__()

                self.yang_name = "cieIfStatusListEntry"
                self.yang_parent_name = "cieIfStatusListTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.cieifstatuslistindex = YLeaf(YType.uint32, "cieIfStatusListIndex")

                self.cieinterfaceownershipbitmap = YLeaf(YType.str, "cieInterfaceOwnershipBitmap")

                self.cieinterfacesindex = YLeaf(YType.str, "cieInterfacesIndex")

                self.cieinterfacesopercause = YLeaf(YType.str, "cieInterfacesOperCause")

                self.cieinterfacesopermode = YLeaf(YType.str, "cieInterfacesOperMode")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "cieifstatuslistindex",
                                "cieinterfaceownershipbitmap",
                                "cieinterfacesindex",
                                "cieinterfacesopercause",
                                "cieinterfacesopermode") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIfExtensionMib.Cieifstatuslisttable.Cieifstatuslistentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIfExtensionMib.Cieifstatuslisttable.Cieifstatuslistentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.cieifstatuslistindex.is_set or
                    self.cieinterfaceownershipbitmap.is_set or
                    self.cieinterfacesindex.is_set or
                    self.cieinterfacesopercause.is_set or
                    self.cieinterfacesopermode.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.cieifstatuslistindex.yfilter != YFilter.not_set or
                    self.cieinterfaceownershipbitmap.yfilter != YFilter.not_set or
                    self.cieinterfacesindex.yfilter != YFilter.not_set or
                    self.cieinterfacesopercause.yfilter != YFilter.not_set or
                    self.cieinterfacesopermode.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cieIfStatusListEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + "[cieIfStatusListIndex='" + self.cieifstatuslistindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/cieIfStatusListTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.cieifstatuslistindex.is_set or self.cieifstatuslistindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifstatuslistindex.get_name_leafdata())
                if (self.cieinterfaceownershipbitmap.is_set or self.cieinterfaceownershipbitmap.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieinterfaceownershipbitmap.get_name_leafdata())
                if (self.cieinterfacesindex.is_set or self.cieinterfacesindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieinterfacesindex.get_name_leafdata())
                if (self.cieinterfacesopercause.is_set or self.cieinterfacesopercause.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieinterfacesopercause.get_name_leafdata())
                if (self.cieinterfacesopermode.is_set or self.cieinterfacesopermode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieinterfacesopermode.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "cieIfStatusListIndex" or name == "cieInterfaceOwnershipBitmap" or name == "cieInterfacesIndex" or name == "cieInterfacesOperCause" or name == "cieInterfacesOperMode"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfStatusListIndex"):
                    self.cieifstatuslistindex = value
                    self.cieifstatuslistindex.value_namespace = name_space
                    self.cieifstatuslistindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cieInterfaceOwnershipBitmap"):
                    self.cieinterfaceownershipbitmap = value
                    self.cieinterfaceownershipbitmap.value_namespace = name_space
                    self.cieinterfaceownershipbitmap.value_namespace_prefix = name_space_prefix
                if(value_path == "cieInterfacesIndex"):
                    self.cieinterfacesindex = value
                    self.cieinterfacesindex.value_namespace = name_space
                    self.cieinterfacesindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cieInterfacesOperCause"):
                    self.cieinterfacesopercause = value
                    self.cieinterfacesopercause.value_namespace = name_space
                    self.cieinterfacesopercause.value_namespace_prefix = name_space_prefix
                if(value_path == "cieInterfacesOperMode"):
                    self.cieinterfacesopermode = value
                    self.cieinterfacesopermode.value_namespace = name_space
                    self.cieinterfacesopermode.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cieifstatuslistentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cieifstatuslistentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cieIfStatusListTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cieIfStatusListEntry"):
                for c in self.cieifstatuslistentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIfExtensionMib.Cieifstatuslisttable.Cieifstatuslistentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cieifstatuslistentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cieIfStatusListEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cieifvlstatstable(Entity):
        """
        This table contains VL (Virtual Link) statistics
        for a capable interface.
        
        Objects defined in this table may be 
        applicable to physical interfaces only.
        
        .. attribute:: cieifvlstatsentry
        
        	Each row contains managed objects for Virtual Link statistics on interface capable of  providing this information
        	**type**\: list of    :py:class:`Cieifvlstatsentry <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CiscoIfExtensionMib.Cieifvlstatstable.Cieifvlstatsentry>`
        
        

        """

        _prefix = 'CISCO-IF-EXTENSION-MIB'
        _revision = '2013-03-13'

        def __init__(self):
            super(CiscoIfExtensionMib.Cieifvlstatstable, self).__init__()

            self.yang_name = "cieIfVlStatsTable"
            self.yang_parent_name = "CISCO-IF-EXTENSION-MIB"

            self.cieifvlstatsentry = YList(self)

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
                        super(CiscoIfExtensionMib.Cieifvlstatstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIfExtensionMib.Cieifvlstatstable, self).__setattr__(name, value)


        class Cieifvlstatsentry(Entity):
            """
            Each row contains managed objects for
            Virtual Link statistics on interface capable of 
            providing this information.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: cieifdropvlinoctets
            
            	This object indicates the number of input octets on all Drop Virtual Links belonged  to this interface
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cieifdropvlinpkts
            
            	This object indicates the number of input packets on all Drop Virtual Links belonged  to this interface
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cieifdropvloutoctets
            
            	This object indicates the number of output octets on all Drop Virtual Links belonged  to this interface
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cieifdropvloutpkts
            
            	This object indicates the number of output packets on all Drop Virtual Links belonged  to this interface
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cieifnodropvlinoctets
            
            	This object indicates the number of input octets on all No\-Drop Virtual Links belonged  to this interface
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cieifnodropvlinpkts
            
            	This object indicates the number of input packets on all No\-Drop Virtual Links belonged  to this interface
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cieifnodropvloutoctets
            
            	This object indicates the number of output octets on all No\-Drop Virtual Links belonged  to this interface
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cieifnodropvloutpkts
            
            	This object indicates the number of output packets on all No\-Drop Virtual Links belonged  to this interface
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'CISCO-IF-EXTENSION-MIB'
            _revision = '2013-03-13'

            def __init__(self):
                super(CiscoIfExtensionMib.Cieifvlstatstable.Cieifvlstatsentry, self).__init__()

                self.yang_name = "cieIfVlStatsEntry"
                self.yang_parent_name = "cieIfVlStatsTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.cieifdropvlinoctets = YLeaf(YType.uint64, "cieIfDropVlInOctets")

                self.cieifdropvlinpkts = YLeaf(YType.uint64, "cieIfDropVlInPkts")

                self.cieifdropvloutoctets = YLeaf(YType.uint64, "cieIfDropVlOutOctets")

                self.cieifdropvloutpkts = YLeaf(YType.uint64, "cieIfDropVlOutPkts")

                self.cieifnodropvlinoctets = YLeaf(YType.uint64, "cieIfNoDropVlInOctets")

                self.cieifnodropvlinpkts = YLeaf(YType.uint64, "cieIfNoDropVlInPkts")

                self.cieifnodropvloutoctets = YLeaf(YType.uint64, "cieIfNoDropVlOutOctets")

                self.cieifnodropvloutpkts = YLeaf(YType.uint64, "cieIfNoDropVlOutPkts")

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
                                "cieifdropvlinoctets",
                                "cieifdropvlinpkts",
                                "cieifdropvloutoctets",
                                "cieifdropvloutpkts",
                                "cieifnodropvlinoctets",
                                "cieifnodropvlinpkts",
                                "cieifnodropvloutoctets",
                                "cieifnodropvloutpkts") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIfExtensionMib.Cieifvlstatstable.Cieifvlstatsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIfExtensionMib.Cieifvlstatstable.Cieifvlstatsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.cieifdropvlinoctets.is_set or
                    self.cieifdropvlinpkts.is_set or
                    self.cieifdropvloutoctets.is_set or
                    self.cieifdropvloutpkts.is_set or
                    self.cieifnodropvlinoctets.is_set or
                    self.cieifnodropvlinpkts.is_set or
                    self.cieifnodropvloutoctets.is_set or
                    self.cieifnodropvloutpkts.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.cieifdropvlinoctets.yfilter != YFilter.not_set or
                    self.cieifdropvlinpkts.yfilter != YFilter.not_set or
                    self.cieifdropvloutoctets.yfilter != YFilter.not_set or
                    self.cieifdropvloutpkts.yfilter != YFilter.not_set or
                    self.cieifnodropvlinoctets.yfilter != YFilter.not_set or
                    self.cieifnodropvlinpkts.yfilter != YFilter.not_set or
                    self.cieifnodropvloutoctets.yfilter != YFilter.not_set or
                    self.cieifnodropvloutpkts.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cieIfVlStatsEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/cieIfVlStatsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.cieifdropvlinoctets.is_set or self.cieifdropvlinoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifdropvlinoctets.get_name_leafdata())
                if (self.cieifdropvlinpkts.is_set or self.cieifdropvlinpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifdropvlinpkts.get_name_leafdata())
                if (self.cieifdropvloutoctets.is_set or self.cieifdropvloutoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifdropvloutoctets.get_name_leafdata())
                if (self.cieifdropvloutpkts.is_set or self.cieifdropvloutpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifdropvloutpkts.get_name_leafdata())
                if (self.cieifnodropvlinoctets.is_set or self.cieifnodropvlinoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifnodropvlinoctets.get_name_leafdata())
                if (self.cieifnodropvlinpkts.is_set or self.cieifnodropvlinpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifnodropvlinpkts.get_name_leafdata())
                if (self.cieifnodropvloutoctets.is_set or self.cieifnodropvloutoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifnodropvloutoctets.get_name_leafdata())
                if (self.cieifnodropvloutpkts.is_set or self.cieifnodropvloutpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifnodropvloutpkts.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "cieIfDropVlInOctets" or name == "cieIfDropVlInPkts" or name == "cieIfDropVlOutOctets" or name == "cieIfDropVlOutPkts" or name == "cieIfNoDropVlInOctets" or name == "cieIfNoDropVlInPkts" or name == "cieIfNoDropVlOutOctets" or name == "cieIfNoDropVlOutPkts"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfDropVlInOctets"):
                    self.cieifdropvlinoctets = value
                    self.cieifdropvlinoctets.value_namespace = name_space
                    self.cieifdropvlinoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfDropVlInPkts"):
                    self.cieifdropvlinpkts = value
                    self.cieifdropvlinpkts.value_namespace = name_space
                    self.cieifdropvlinpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfDropVlOutOctets"):
                    self.cieifdropvloutoctets = value
                    self.cieifdropvloutoctets.value_namespace = name_space
                    self.cieifdropvloutoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfDropVlOutPkts"):
                    self.cieifdropvloutpkts = value
                    self.cieifdropvloutpkts.value_namespace = name_space
                    self.cieifdropvloutpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfNoDropVlInOctets"):
                    self.cieifnodropvlinoctets = value
                    self.cieifnodropvlinoctets.value_namespace = name_space
                    self.cieifnodropvlinoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfNoDropVlInPkts"):
                    self.cieifnodropvlinpkts = value
                    self.cieifnodropvlinpkts.value_namespace = name_space
                    self.cieifnodropvlinpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfNoDropVlOutOctets"):
                    self.cieifnodropvloutoctets = value
                    self.cieifnodropvloutoctets.value_namespace = name_space
                    self.cieifnodropvloutoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfNoDropVlOutPkts"):
                    self.cieifnodropvloutpkts = value
                    self.cieifnodropvloutpkts.value_namespace = name_space
                    self.cieifnodropvloutpkts.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cieifvlstatsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cieifvlstatsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cieIfVlStatsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cieIfVlStatsEntry"):
                for c in self.cieifvlstatsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIfExtensionMib.Cieifvlstatstable.Cieifvlstatsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cieifvlstatsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cieIfVlStatsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cieifindexpersistencetable(Entity):
        """
        This table lists configuration data relating to ifIndex
        persistence.
        
        This table has a sparse dependent relationship on the ifTable,
        containing a row for each ifEntry corresponding to an interface
        for which ifIndex persistence is supported.
        
        .. attribute:: cieifindexpersistenceentry
        
        	Each entry represents ifindex persistence configuration for an interface specified by ifIndex. Whenever an interface which supports ifindex persistence is created/destroyed in the ifTable, the corresponding ifindex persistence entry is created/destroyed respectively. Some of the interfaces may not support ifindex persistence, for example, a dynamic interface, such as a PPP connection or a IP subscriber interface
        	**type**\: list of    :py:class:`Cieifindexpersistenceentry <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CiscoIfExtensionMib.Cieifindexpersistencetable.Cieifindexpersistenceentry>`
        
        

        """

        _prefix = 'CISCO-IF-EXTENSION-MIB'
        _revision = '2013-03-13'

        def __init__(self):
            super(CiscoIfExtensionMib.Cieifindexpersistencetable, self).__init__()

            self.yang_name = "cieIfIndexPersistenceTable"
            self.yang_parent_name = "CISCO-IF-EXTENSION-MIB"

            self.cieifindexpersistenceentry = YList(self)

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
                        super(CiscoIfExtensionMib.Cieifindexpersistencetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIfExtensionMib.Cieifindexpersistencetable, self).__setattr__(name, value)


        class Cieifindexpersistenceentry(Entity):
            """
            Each entry represents ifindex persistence configuration for an
            interface specified by ifIndex. Whenever an interface which
            supports ifindex persistence is created/destroyed in the
            ifTable, the corresponding ifindex persistence entry is
            created/destroyed respectively. Some of the interfaces may not
            support ifindex persistence, for example, a dynamic interface,
            such as a PPP connection or a IP subscriber interface.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: cieifindexpersistencecontrol
            
            	This object specifies whether the interface's ifIndex value persist across reinitialization. In global state, the interface uses the global setting data for persistence i.e. cieIfIndexGlobalPersistence
            	**type**\:   :py:class:`Ifindexpersistencestate <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.Ifindexpersistencestate>`
            
            .. attribute:: cieifindexpersistenceenabled
            
            	This object specifies whether the interface's ifIndex value persist across reinitialization.  Due to change in syntax, this object is deprecated by cieIfIndexPersistenceControl
            	**type**\:  bool
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'CISCO-IF-EXTENSION-MIB'
            _revision = '2013-03-13'

            def __init__(self):
                super(CiscoIfExtensionMib.Cieifindexpersistencetable.Cieifindexpersistenceentry, self).__init__()

                self.yang_name = "cieIfIndexPersistenceEntry"
                self.yang_parent_name = "cieIfIndexPersistenceTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.cieifindexpersistencecontrol = YLeaf(YType.enumeration, "cieIfIndexPersistenceControl")

                self.cieifindexpersistenceenabled = YLeaf(YType.boolean, "cieIfIndexPersistenceEnabled")

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
                                "cieifindexpersistencecontrol",
                                "cieifindexpersistenceenabled") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIfExtensionMib.Cieifindexpersistencetable.Cieifindexpersistenceentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIfExtensionMib.Cieifindexpersistencetable.Cieifindexpersistenceentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.cieifindexpersistencecontrol.is_set or
                    self.cieifindexpersistenceenabled.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.cieifindexpersistencecontrol.yfilter != YFilter.not_set or
                    self.cieifindexpersistenceenabled.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cieIfIndexPersistenceEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/cieIfIndexPersistenceTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.cieifindexpersistencecontrol.is_set or self.cieifindexpersistencecontrol.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifindexpersistencecontrol.get_name_leafdata())
                if (self.cieifindexpersistenceenabled.is_set or self.cieifindexpersistenceenabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifindexpersistenceenabled.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "cieIfIndexPersistenceControl" or name == "cieIfIndexPersistenceEnabled"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfIndexPersistenceControl"):
                    self.cieifindexpersistencecontrol = value
                    self.cieifindexpersistencecontrol.value_namespace = name_space
                    self.cieifindexpersistencecontrol.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfIndexPersistenceEnabled"):
                    self.cieifindexpersistenceenabled = value
                    self.cieifindexpersistenceenabled.value_namespace = name_space
                    self.cieifindexpersistenceenabled.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cieifindexpersistenceentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cieifindexpersistenceentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cieIfIndexPersistenceTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cieIfIndexPersistenceEntry"):
                for c in self.cieifindexpersistenceentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIfExtensionMib.Cieifindexpersistencetable.Cieifindexpersistenceentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cieifindexpersistenceentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cieIfIndexPersistenceEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cieifdot1Qcustomethertypetable(Entity):
        """
        A list of the interfaces that support
        the 802.1q custom Ethertype feature.
        
        .. attribute:: cieifdot1qcustomethertypeentry
        
        	An entry containing the custom EtherType information for the interface.  Only interfaces with custom 802.1q ethertype control are listed in the  table
        	**type**\: list of    :py:class:`Cieifdot1Qcustomethertypeentry <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CiscoIfExtensionMib.Cieifdot1Qcustomethertypetable.Cieifdot1Qcustomethertypeentry>`
        
        

        """

        _prefix = 'CISCO-IF-EXTENSION-MIB'
        _revision = '2013-03-13'

        def __init__(self):
            super(CiscoIfExtensionMib.Cieifdot1Qcustomethertypetable, self).__init__()

            self.yang_name = "cieIfDot1qCustomEtherTypeTable"
            self.yang_parent_name = "CISCO-IF-EXTENSION-MIB"

            self.cieifdot1qcustomethertypeentry = YList(self)

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
                        super(CiscoIfExtensionMib.Cieifdot1Qcustomethertypetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIfExtensionMib.Cieifdot1Qcustomethertypetable, self).__setattr__(name, value)


        class Cieifdot1Qcustomethertypeentry(Entity):
            """
            An entry containing the custom EtherType
            information for the interface.
            
            Only interfaces with custom 802.1q
            ethertype control are listed in the 
            table.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: cieifdot1qcustomadminethertype
            
            	The Dot1qEtherType allow administrator to select a non\-standard (other than 0x8100) 2\-byte ethertype for the interface to  interoperate with third party vendor's system that do not use the standard 0x8100 ethertype to identify 802.1q\-tagged frames.  The current administrative value of the  802.1q ethertype for the interface.  The administrative 802.1q ethertype value may  differ from the operational 802.1q ethertype value.  On some platforms, 802.1q ethertype may be assigned per group rather than per port. If multiple ports belong to a port group, the 802.1q ethertype assigned to any of the ports in such group will apply to all ports in the same group.  To configure non\-standard dot1q ethertype is only recommended when the Cisco device is connected to any third party vendor device. Also be advised that the custom ethertype value needs to be changed in the whole cloud of  Cisco device with the same custom ethertype  value if the third party device are separated  by number of Cisco device in the middle
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cieifdot1qcustomoperethertype
            
            	The current operational value of the 802.1q ethertype for the interface
            	**type**\:  int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'CISCO-IF-EXTENSION-MIB'
            _revision = '2013-03-13'

            def __init__(self):
                super(CiscoIfExtensionMib.Cieifdot1Qcustomethertypetable.Cieifdot1Qcustomethertypeentry, self).__init__()

                self.yang_name = "cieIfDot1qCustomEtherTypeEntry"
                self.yang_parent_name = "cieIfDot1qCustomEtherTypeTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.cieifdot1qcustomadminethertype = YLeaf(YType.int32, "cieIfDot1qCustomAdminEtherType")

                self.cieifdot1qcustomoperethertype = YLeaf(YType.int32, "cieIfDot1qCustomOperEtherType")

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
                                "cieifdot1qcustomadminethertype",
                                "cieifdot1qcustomoperethertype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIfExtensionMib.Cieifdot1Qcustomethertypetable.Cieifdot1Qcustomethertypeentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIfExtensionMib.Cieifdot1Qcustomethertypetable.Cieifdot1Qcustomethertypeentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.cieifdot1qcustomadminethertype.is_set or
                    self.cieifdot1qcustomoperethertype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.cieifdot1qcustomadminethertype.yfilter != YFilter.not_set or
                    self.cieifdot1qcustomoperethertype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cieIfDot1qCustomEtherTypeEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/cieIfDot1qCustomEtherTypeTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.cieifdot1qcustomadminethertype.is_set or self.cieifdot1qcustomadminethertype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifdot1qcustomadminethertype.get_name_leafdata())
                if (self.cieifdot1qcustomoperethertype.is_set or self.cieifdot1qcustomoperethertype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifdot1qcustomoperethertype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "cieIfDot1qCustomAdminEtherType" or name == "cieIfDot1qCustomOperEtherType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfDot1qCustomAdminEtherType"):
                    self.cieifdot1qcustomadminethertype = value
                    self.cieifdot1qcustomadminethertype.value_namespace = name_space
                    self.cieifdot1qcustomadminethertype.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfDot1qCustomOperEtherType"):
                    self.cieifdot1qcustomoperethertype = value
                    self.cieifdot1qcustomoperethertype.value_namespace = name_space
                    self.cieifdot1qcustomoperethertype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cieifdot1qcustomethertypeentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cieifdot1qcustomethertypeentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cieIfDot1qCustomEtherTypeTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cieIfDot1qCustomEtherTypeEntry"):
                for c in self.cieifdot1qcustomethertypeentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIfExtensionMib.Cieifdot1Qcustomethertypetable.Cieifdot1Qcustomethertypeentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cieifdot1qcustomethertypeentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cieIfDot1qCustomEtherTypeEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cieifutiltable(Entity):
        """
        This table contains the interface utilization
        rates for inbound and outbound traffic on an
        interface.
        
        .. attribute:: cieifutilentry
        
        	An entry containing utilization rates for the interface.  Every interface for which the  inbound and  outbound traffic information is available has a corresponding entry in this table
        	**type**\: list of    :py:class:`Cieifutilentry <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CiscoIfExtensionMib.Cieifutiltable.Cieifutilentry>`
        
        

        """

        _prefix = 'CISCO-IF-EXTENSION-MIB'
        _revision = '2013-03-13'

        def __init__(self):
            super(CiscoIfExtensionMib.Cieifutiltable, self).__init__()

            self.yang_name = "cieIfUtilTable"
            self.yang_parent_name = "CISCO-IF-EXTENSION-MIB"

            self.cieifutilentry = YList(self)

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
                        super(CiscoIfExtensionMib.Cieifutiltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIfExtensionMib.Cieifutiltable, self).__setattr__(name, value)


        class Cieifutilentry(Entity):
            """
            An entry containing utilization rates for the
            interface.
            
            Every interface for which the  inbound and 
            outbound traffic information is available
            has a corresponding entry in this table.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: cieifinoctetrate
            
            	By default, this is the five minute exponentially\-decayed moving average of the inbound octet rate for this interface. However, if the corresponding instance of cieIfInterval is instantiated with a value which specifies an interval different from 5\-minutes, then cieIfInOctetRate is the exponentially\-decayed moving average of inbound octet rate over this different time interval
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: octets per second
            
            .. attribute:: cieifinpktrate
            
            	By default, this is the five minute exponentially\-decayed moving average of the inbound packet rate for this interface. However, if the corresponding instance of cieIfInterval is instantiated with a value which specifies an interval different from 5\-minutes, then cieIfInPktRate is the exponentially\-decayed moving average of inbound packet rate over this different time interval
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets per second
            
            .. attribute:: cieifinterval
            
            	This object specifies the time interval over which the inbound and outbound traffic rates are calculated for this interface
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cieifoutoctetrate
            
            	By default, this is the five minute exponentially\-decayed moving average of the outbound octet rate for this interface. However, if the corresponding instance of cieIfInterval is instantiated with a value which specifies an interval different from 5\-minutes, then cieIfOutOctetRate is the exponentially\-decayed moving average of outbound octet rate over this different time interval
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: octets per second
            
            .. attribute:: cieifoutpktrate
            
            	By default, this is the five minute exponentially\-decayed moving average of the outbound packet rate for this interface. However, if the corresponding instance of cieIfInterval is instantiated with a value which specifies an interval different from 5\-minutes, then cieIfOutPktRate is the exponentially\-decayed moving average of outbound packet rate over this different time interval
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets per second
            
            

            """

            _prefix = 'CISCO-IF-EXTENSION-MIB'
            _revision = '2013-03-13'

            def __init__(self):
                super(CiscoIfExtensionMib.Cieifutiltable.Cieifutilentry, self).__init__()

                self.yang_name = "cieIfUtilEntry"
                self.yang_parent_name = "cieIfUtilTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.cieifinoctetrate = YLeaf(YType.uint64, "cieIfInOctetRate")

                self.cieifinpktrate = YLeaf(YType.uint64, "cieIfInPktRate")

                self.cieifinterval = YLeaf(YType.uint32, "cieIfInterval")

                self.cieifoutoctetrate = YLeaf(YType.uint64, "cieIfOutOctetRate")

                self.cieifoutpktrate = YLeaf(YType.uint64, "cieIfOutPktRate")

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
                                "cieifinoctetrate",
                                "cieifinpktrate",
                                "cieifinterval",
                                "cieifoutoctetrate",
                                "cieifoutpktrate") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIfExtensionMib.Cieifutiltable.Cieifutilentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIfExtensionMib.Cieifutiltable.Cieifutilentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.cieifinoctetrate.is_set or
                    self.cieifinpktrate.is_set or
                    self.cieifinterval.is_set or
                    self.cieifoutoctetrate.is_set or
                    self.cieifoutpktrate.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.cieifinoctetrate.yfilter != YFilter.not_set or
                    self.cieifinpktrate.yfilter != YFilter.not_set or
                    self.cieifinterval.yfilter != YFilter.not_set or
                    self.cieifoutoctetrate.yfilter != YFilter.not_set or
                    self.cieifoutpktrate.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cieIfUtilEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/cieIfUtilTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.cieifinoctetrate.is_set or self.cieifinoctetrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifinoctetrate.get_name_leafdata())
                if (self.cieifinpktrate.is_set or self.cieifinpktrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifinpktrate.get_name_leafdata())
                if (self.cieifinterval.is_set or self.cieifinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifinterval.get_name_leafdata())
                if (self.cieifoutoctetrate.is_set or self.cieifoutoctetrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifoutoctetrate.get_name_leafdata())
                if (self.cieifoutpktrate.is_set or self.cieifoutpktrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifoutpktrate.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "cieIfInOctetRate" or name == "cieIfInPktRate" or name == "cieIfInterval" or name == "cieIfOutOctetRate" or name == "cieIfOutPktRate"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfInOctetRate"):
                    self.cieifinoctetrate = value
                    self.cieifinoctetrate.value_namespace = name_space
                    self.cieifinoctetrate.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfInPktRate"):
                    self.cieifinpktrate = value
                    self.cieifinpktrate.value_namespace = name_space
                    self.cieifinpktrate.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfInterval"):
                    self.cieifinterval = value
                    self.cieifinterval.value_namespace = name_space
                    self.cieifinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfOutOctetRate"):
                    self.cieifoutoctetrate = value
                    self.cieifoutoctetrate.value_namespace = name_space
                    self.cieifoutoctetrate.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfOutPktRate"):
                    self.cieifoutpktrate = value
                    self.cieifoutpktrate.value_namespace = name_space
                    self.cieifoutpktrate.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cieifutilentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cieifutilentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cieIfUtilTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cieIfUtilEntry"):
                for c in self.cieifutilentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIfExtensionMib.Cieifutiltable.Cieifutilentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cieifutilentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cieIfUtilEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cieifdot1Dbasemappingtable(Entity):
        """
        This table contains the mappings of the
        ifIndex of an interface to its
        corresponding dot1dBasePort value.
        
        .. attribute:: cieifdot1dbasemappingentry
        
        	An entry containing the mapping between the ifIndex value of an interface and its corresponding dot1dBasePort value.  Every interface which has been assigned a dot1dBasePort value by the system has a corresponding entry in this table
        	**type**\: list of    :py:class:`Cieifdot1Dbasemappingentry <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CiscoIfExtensionMib.Cieifdot1Dbasemappingtable.Cieifdot1Dbasemappingentry>`
        
        

        """

        _prefix = 'CISCO-IF-EXTENSION-MIB'
        _revision = '2013-03-13'

        def __init__(self):
            super(CiscoIfExtensionMib.Cieifdot1Dbasemappingtable, self).__init__()

            self.yang_name = "cieIfDot1dBaseMappingTable"
            self.yang_parent_name = "CISCO-IF-EXTENSION-MIB"

            self.cieifdot1dbasemappingentry = YList(self)

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
                        super(CiscoIfExtensionMib.Cieifdot1Dbasemappingtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIfExtensionMib.Cieifdot1Dbasemappingtable, self).__setattr__(name, value)


        class Cieifdot1Dbasemappingentry(Entity):
            """
            An entry containing the mapping between
            the ifIndex value of an interface and its
            corresponding dot1dBasePort value.
            
            Every interface which has been assigned
            a dot1dBasePort value by the system
            has a corresponding entry in this table.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: cieifdot1dbasemappingport
            
            	The dot1dBasePort value for this interface
            	**type**\:  int
            
            	**range:** 1..65535
            
            

            """

            _prefix = 'CISCO-IF-EXTENSION-MIB'
            _revision = '2013-03-13'

            def __init__(self):
                super(CiscoIfExtensionMib.Cieifdot1Dbasemappingtable.Cieifdot1Dbasemappingentry, self).__init__()

                self.yang_name = "cieIfDot1dBaseMappingEntry"
                self.yang_parent_name = "cieIfDot1dBaseMappingTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.cieifdot1dbasemappingport = YLeaf(YType.int32, "cieIfDot1dBaseMappingPort")

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
                                "cieifdot1dbasemappingport") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIfExtensionMib.Cieifdot1Dbasemappingtable.Cieifdot1Dbasemappingentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIfExtensionMib.Cieifdot1Dbasemappingtable.Cieifdot1Dbasemappingentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.cieifdot1dbasemappingport.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.cieifdot1dbasemappingport.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cieIfDot1dBaseMappingEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/cieIfDot1dBaseMappingTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.cieifdot1dbasemappingport.is_set or self.cieifdot1dbasemappingport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifdot1dbasemappingport.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "cieIfDot1dBaseMappingPort"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfDot1dBaseMappingPort"):
                    self.cieifdot1dbasemappingport = value
                    self.cieifdot1dbasemappingport.value_namespace = name_space
                    self.cieifdot1dbasemappingport.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cieifdot1dbasemappingentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cieifdot1dbasemappingentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cieIfDot1dBaseMappingTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cieIfDot1dBaseMappingEntry"):
                for c in self.cieifdot1dbasemappingentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIfExtensionMib.Cieifdot1Dbasemappingtable.Cieifdot1Dbasemappingentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cieifdot1dbasemappingentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cieIfDot1dBaseMappingEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cieifnamemappingtable(Entity):
        """
        This table contains objects for providing
        the 'ifName' to 'ifIndex' mapping.
        This table contains one entry for each
        valid 'ifName' available in the system.
        Upon the first request, the implementation
        of this table will get all the available
        ifNames, and it will populate the entries
        in this table, it maintains this ifNames
        in a cache for ~30 seconds.
        
        .. attribute:: cieifnamemappingentry
        
        	An entry into the cieIfNameMappingTable
        	**type**\: list of    :py:class:`Cieifnamemappingentry <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CiscoIfExtensionMib.Cieifnamemappingtable.Cieifnamemappingentry>`
        
        

        """

        _prefix = 'CISCO-IF-EXTENSION-MIB'
        _revision = '2013-03-13'

        def __init__(self):
            super(CiscoIfExtensionMib.Cieifnamemappingtable, self).__init__()

            self.yang_name = "cieIfNameMappingTable"
            self.yang_parent_name = "CISCO-IF-EXTENSION-MIB"

            self.cieifnamemappingentry = YList(self)

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
                        super(CiscoIfExtensionMib.Cieifnamemappingtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIfExtensionMib.Cieifnamemappingtable, self).__setattr__(name, value)


        class Cieifnamemappingentry(Entity):
            """
            An entry into the cieIfNameMappingTable.
            
            .. attribute:: cieifname  <key>
            
            	Represents an interface name mentioned in the 'ifName' object of this system
            	**type**\:  str
            
            	**length:** 1..112
            
            .. attribute:: cieifindex
            
            	This object represents the 'ifIndex' corresponding to the interface name mentioned in the 'cieIfName' object of this instance. If the 'ifName' mentioned in the 'cieIfName'  object of this instance corresponds to multiple 'ifIndex' values, then the value of this object is the numerically smallest of those multiple  'ifIndex' values
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            

            """

            _prefix = 'CISCO-IF-EXTENSION-MIB'
            _revision = '2013-03-13'

            def __init__(self):
                super(CiscoIfExtensionMib.Cieifnamemappingtable.Cieifnamemappingentry, self).__init__()

                self.yang_name = "cieIfNameMappingEntry"
                self.yang_parent_name = "cieIfNameMappingTable"

                self.cieifname = YLeaf(YType.str, "cieIfName")

                self.cieifindex = YLeaf(YType.int32, "cieIfIndex")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cieifname",
                                "cieifindex") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIfExtensionMib.Cieifnamemappingtable.Cieifnamemappingentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIfExtensionMib.Cieifnamemappingtable.Cieifnamemappingentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cieifname.is_set or
                    self.cieifindex.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cieifname.yfilter != YFilter.not_set or
                    self.cieifindex.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cieIfNameMappingEntry" + "[cieIfName='" + self.cieifname.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/cieIfNameMappingTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cieifname.is_set or self.cieifname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifname.get_name_leafdata())
                if (self.cieifindex.is_set or self.cieifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cieifindex.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cieIfName" or name == "cieIfIndex"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cieIfName"):
                    self.cieifname = value
                    self.cieifname.value_namespace = name_space
                    self.cieifname.value_namespace_prefix = name_space_prefix
                if(value_path == "cieIfIndex"):
                    self.cieifindex = value
                    self.cieifindex.value_namespace = name_space
                    self.cieifindex.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cieifnamemappingentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cieifnamemappingentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cieIfNameMappingTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cieIfNameMappingEntry"):
                for c in self.cieifnamemappingentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIfExtensionMib.Cieifnamemappingtable.Cieifnamemappingentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cieifnamemappingentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cieIfNameMappingEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.cieifdot1dbasemappingtable is not None and self.cieifdot1dbasemappingtable.has_data()) or
            (self.cieifdot1qcustomethertypetable is not None and self.cieifdot1qcustomethertypetable.has_data()) or
            (self.cieifindexpersistencetable is not None and self.cieifindexpersistencetable.has_data()) or
            (self.cieifinterfacetable is not None and self.cieifinterfacetable.has_data()) or
            (self.cieifnamemappingtable is not None and self.cieifnamemappingtable.has_data()) or
            (self.cieifpacketstatstable is not None and self.cieifpacketstatstable.has_data()) or
            (self.cieifstatuslisttable is not None and self.cieifstatuslisttable.has_data()) or
            (self.cieifutiltable is not None and self.cieifutiltable.has_data()) or
            (self.cieifvlstatstable is not None and self.cieifvlstatstable.has_data()) or
            (self.ciscoifextsystemconfig is not None and self.ciscoifextsystemconfig.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cieifdot1dbasemappingtable is not None and self.cieifdot1dbasemappingtable.has_operation()) or
            (self.cieifdot1qcustomethertypetable is not None and self.cieifdot1qcustomethertypetable.has_operation()) or
            (self.cieifindexpersistencetable is not None and self.cieifindexpersistencetable.has_operation()) or
            (self.cieifinterfacetable is not None and self.cieifinterfacetable.has_operation()) or
            (self.cieifnamemappingtable is not None and self.cieifnamemappingtable.has_operation()) or
            (self.cieifpacketstatstable is not None and self.cieifpacketstatstable.has_operation()) or
            (self.cieifstatuslisttable is not None and self.cieifstatuslisttable.has_operation()) or
            (self.cieifutiltable is not None and self.cieifutiltable.has_operation()) or
            (self.cieifvlstatstable is not None and self.cieifvlstatstable.has_operation()) or
            (self.ciscoifextsystemconfig is not None and self.ciscoifextsystemconfig.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB" + path_buffer

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

        if (child_yang_name == "cieIfDot1dBaseMappingTable"):
            if (self.cieifdot1dbasemappingtable is None):
                self.cieifdot1dbasemappingtable = CiscoIfExtensionMib.Cieifdot1Dbasemappingtable()
                self.cieifdot1dbasemappingtable.parent = self
                self._children_name_map["cieifdot1dbasemappingtable"] = "cieIfDot1dBaseMappingTable"
            return self.cieifdot1dbasemappingtable

        if (child_yang_name == "cieIfDot1qCustomEtherTypeTable"):
            if (self.cieifdot1qcustomethertypetable is None):
                self.cieifdot1qcustomethertypetable = CiscoIfExtensionMib.Cieifdot1Qcustomethertypetable()
                self.cieifdot1qcustomethertypetable.parent = self
                self._children_name_map["cieifdot1qcustomethertypetable"] = "cieIfDot1qCustomEtherTypeTable"
            return self.cieifdot1qcustomethertypetable

        if (child_yang_name == "cieIfIndexPersistenceTable"):
            if (self.cieifindexpersistencetable is None):
                self.cieifindexpersistencetable = CiscoIfExtensionMib.Cieifindexpersistencetable()
                self.cieifindexpersistencetable.parent = self
                self._children_name_map["cieifindexpersistencetable"] = "cieIfIndexPersistenceTable"
            return self.cieifindexpersistencetable

        if (child_yang_name == "cieIfInterfaceTable"):
            if (self.cieifinterfacetable is None):
                self.cieifinterfacetable = CiscoIfExtensionMib.Cieifinterfacetable()
                self.cieifinterfacetable.parent = self
                self._children_name_map["cieifinterfacetable"] = "cieIfInterfaceTable"
            return self.cieifinterfacetable

        if (child_yang_name == "cieIfNameMappingTable"):
            if (self.cieifnamemappingtable is None):
                self.cieifnamemappingtable = CiscoIfExtensionMib.Cieifnamemappingtable()
                self.cieifnamemappingtable.parent = self
                self._children_name_map["cieifnamemappingtable"] = "cieIfNameMappingTable"
            return self.cieifnamemappingtable

        if (child_yang_name == "cieIfPacketStatsTable"):
            if (self.cieifpacketstatstable is None):
                self.cieifpacketstatstable = CiscoIfExtensionMib.Cieifpacketstatstable()
                self.cieifpacketstatstable.parent = self
                self._children_name_map["cieifpacketstatstable"] = "cieIfPacketStatsTable"
            return self.cieifpacketstatstable

        if (child_yang_name == "cieIfStatusListTable"):
            if (self.cieifstatuslisttable is None):
                self.cieifstatuslisttable = CiscoIfExtensionMib.Cieifstatuslisttable()
                self.cieifstatuslisttable.parent = self
                self._children_name_map["cieifstatuslisttable"] = "cieIfStatusListTable"
            return self.cieifstatuslisttable

        if (child_yang_name == "cieIfUtilTable"):
            if (self.cieifutiltable is None):
                self.cieifutiltable = CiscoIfExtensionMib.Cieifutiltable()
                self.cieifutiltable.parent = self
                self._children_name_map["cieifutiltable"] = "cieIfUtilTable"
            return self.cieifutiltable

        if (child_yang_name == "cieIfVlStatsTable"):
            if (self.cieifvlstatstable is None):
                self.cieifvlstatstable = CiscoIfExtensionMib.Cieifvlstatstable()
                self.cieifvlstatstable.parent = self
                self._children_name_map["cieifvlstatstable"] = "cieIfVlStatsTable"
            return self.cieifvlstatstable

        if (child_yang_name == "ciscoIfExtSystemConfig"):
            if (self.ciscoifextsystemconfig is None):
                self.ciscoifextsystemconfig = CiscoIfExtensionMib.Ciscoifextsystemconfig()
                self.ciscoifextsystemconfig.parent = self
                self._children_name_map["ciscoifextsystemconfig"] = "ciscoIfExtSystemConfig"
            return self.ciscoifextsystemconfig

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cieIfDot1dBaseMappingTable" or name == "cieIfDot1qCustomEtherTypeTable" or name == "cieIfIndexPersistenceTable" or name == "cieIfInterfaceTable" or name == "cieIfNameMappingTable" or name == "cieIfPacketStatsTable" or name == "cieIfStatusListTable" or name == "cieIfUtilTable" or name == "cieIfVlStatsTable" or name == "ciscoIfExtSystemConfig"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoIfExtensionMib()
        return self._top_entity


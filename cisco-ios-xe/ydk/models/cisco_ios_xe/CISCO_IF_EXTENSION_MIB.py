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
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class IfIndexPersistenceState(Enum):
    """
    IfIndexPersistenceState (Enum Class)

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



class CISCOIFEXTENSIONMIB(Entity):
    """
    
    
    .. attribute:: ciscoifextsystemconfig
    
    	
    	**type**\:  :py:class:`Ciscoifextsystemconfig <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.Ciscoifextsystemconfig>`
    
    .. attribute:: cieifpacketstatstable
    
    	This  table contains interface packet statistics which are not available in  IF\-MIB(RFC2863).   As an example, some interfaces to which objects in this table are applicable are as follows \:          o Ethernet         o FastEthernet         o ATM         o BRI         o Sonet         o GigabitEthernet  Some objects defined in this table may be  applicable to physical interfaces only. As a result, this table may be sparse for some logical interfaces
    	**type**\:  :py:class:`Cieifpacketstatstable <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.Cieifpacketstatstable>`
    
    .. attribute:: cieifinterfacetable
    
    	This  table contains objects which provide more information about interface   properties not available in IF\-MIB (RFC 2863).  Some objects defined in this table may be applicable to physical interfaces only. As a result, this table may be sparse for logical interfaces
    	**type**\:  :py:class:`Cieifinterfacetable <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.Cieifinterfacetable>`
    
    .. attribute:: cieifstatuslisttable
    
    	This table contains objects for providing the 'ifIndex', interface operational mode and  interface operational cause for all the  interfaces in the modules.  This table contains one entry for each  64 interfaces in an module.  This table provides efficient way of encoding  'ifIndex', interface operational mode and interface operational cause, from the point  of retrieval, by combining the values a set  of 64 interfaces in a single MIB object
    	**type**\:  :py:class:`Cieifstatuslisttable <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.Cieifstatuslisttable>`
    
    .. attribute:: cieifvlstatstable
    
    	This table contains VL (Virtual Link) statistics for a capable interface.  Objects defined in this table may be  applicable to physical interfaces only
    	**type**\:  :py:class:`Cieifvlstatstable <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.Cieifvlstatstable>`
    
    .. attribute:: cieifindexpersistencetable
    
    	This table lists configuration data relating to ifIndex persistence.  This table has a sparse dependent relationship on the ifTable, containing a row for each ifEntry corresponding to an interface for which ifIndex persistence is supported
    	**type**\:  :py:class:`Cieifindexpersistencetable <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.Cieifindexpersistencetable>`
    
    .. attribute:: cieifdot1qcustomethertypetable
    
    	A list of the interfaces that support the 802.1q custom Ethertype feature
    	**type**\:  :py:class:`Cieifdot1Qcustomethertypetable <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.Cieifdot1Qcustomethertypetable>`
    
    .. attribute:: cieifutiltable
    
    	This table contains the interface utilization rates for inbound and outbound traffic on an interface
    	**type**\:  :py:class:`Cieifutiltable <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.Cieifutiltable>`
    
    .. attribute:: cieifdot1dbasemappingtable
    
    	This table contains the mappings of the ifIndex of an interface to its corresponding dot1dBasePort value
    	**type**\:  :py:class:`Cieifdot1Dbasemappingtable <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.Cieifdot1Dbasemappingtable>`
    
    .. attribute:: cieifnamemappingtable
    
    	This table contains objects for providing the 'ifName' to 'ifIndex' mapping. This table contains one entry for each valid 'ifName' available in the system. Upon the first request, the implementation of this table will get all the available ifNames, and it will populate the entries in this table, it maintains this ifNames in a cache for ~30 seconds
    	**type**\:  :py:class:`Cieifnamemappingtable <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.Cieifnamemappingtable>`
    
    

    """

    _prefix = 'CISCO-IF-EXTENSION-MIB'
    _revision = '2013-03-13'

    def __init__(self):
        super(CISCOIFEXTENSIONMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IF-EXTENSION-MIB"
        self.yang_parent_name = "CISCO-IF-EXTENSION-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("ciscoIfExtSystemConfig", ("ciscoifextsystemconfig", CISCOIFEXTENSIONMIB.Ciscoifextsystemconfig)), ("cieIfPacketStatsTable", ("cieifpacketstatstable", CISCOIFEXTENSIONMIB.Cieifpacketstatstable)), ("cieIfInterfaceTable", ("cieifinterfacetable", CISCOIFEXTENSIONMIB.Cieifinterfacetable)), ("cieIfStatusListTable", ("cieifstatuslisttable", CISCOIFEXTENSIONMIB.Cieifstatuslisttable)), ("cieIfVlStatsTable", ("cieifvlstatstable", CISCOIFEXTENSIONMIB.Cieifvlstatstable)), ("cieIfIndexPersistenceTable", ("cieifindexpersistencetable", CISCOIFEXTENSIONMIB.Cieifindexpersistencetable)), ("cieIfDot1qCustomEtherTypeTable", ("cieifdot1qcustomethertypetable", CISCOIFEXTENSIONMIB.Cieifdot1Qcustomethertypetable)), ("cieIfUtilTable", ("cieifutiltable", CISCOIFEXTENSIONMIB.Cieifutiltable)), ("cieIfDot1dBaseMappingTable", ("cieifdot1dbasemappingtable", CISCOIFEXTENSIONMIB.Cieifdot1Dbasemappingtable)), ("cieIfNameMappingTable", ("cieifnamemappingtable", CISCOIFEXTENSIONMIB.Cieifnamemappingtable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.ciscoifextsystemconfig = CISCOIFEXTENSIONMIB.Ciscoifextsystemconfig()
        self.ciscoifextsystemconfig.parent = self
        self._children_name_map["ciscoifextsystemconfig"] = "ciscoIfExtSystemConfig"
        self._children_yang_names.add("ciscoIfExtSystemConfig")

        self.cieifpacketstatstable = CISCOIFEXTENSIONMIB.Cieifpacketstatstable()
        self.cieifpacketstatstable.parent = self
        self._children_name_map["cieifpacketstatstable"] = "cieIfPacketStatsTable"
        self._children_yang_names.add("cieIfPacketStatsTable")

        self.cieifinterfacetable = CISCOIFEXTENSIONMIB.Cieifinterfacetable()
        self.cieifinterfacetable.parent = self
        self._children_name_map["cieifinterfacetable"] = "cieIfInterfaceTable"
        self._children_yang_names.add("cieIfInterfaceTable")

        self.cieifstatuslisttable = CISCOIFEXTENSIONMIB.Cieifstatuslisttable()
        self.cieifstatuslisttable.parent = self
        self._children_name_map["cieifstatuslisttable"] = "cieIfStatusListTable"
        self._children_yang_names.add("cieIfStatusListTable")

        self.cieifvlstatstable = CISCOIFEXTENSIONMIB.Cieifvlstatstable()
        self.cieifvlstatstable.parent = self
        self._children_name_map["cieifvlstatstable"] = "cieIfVlStatsTable"
        self._children_yang_names.add("cieIfVlStatsTable")

        self.cieifindexpersistencetable = CISCOIFEXTENSIONMIB.Cieifindexpersistencetable()
        self.cieifindexpersistencetable.parent = self
        self._children_name_map["cieifindexpersistencetable"] = "cieIfIndexPersistenceTable"
        self._children_yang_names.add("cieIfIndexPersistenceTable")

        self.cieifdot1qcustomethertypetable = CISCOIFEXTENSIONMIB.Cieifdot1Qcustomethertypetable()
        self.cieifdot1qcustomethertypetable.parent = self
        self._children_name_map["cieifdot1qcustomethertypetable"] = "cieIfDot1qCustomEtherTypeTable"
        self._children_yang_names.add("cieIfDot1qCustomEtherTypeTable")

        self.cieifutiltable = CISCOIFEXTENSIONMIB.Cieifutiltable()
        self.cieifutiltable.parent = self
        self._children_name_map["cieifutiltable"] = "cieIfUtilTable"
        self._children_yang_names.add("cieIfUtilTable")

        self.cieifdot1dbasemappingtable = CISCOIFEXTENSIONMIB.Cieifdot1Dbasemappingtable()
        self.cieifdot1dbasemappingtable.parent = self
        self._children_name_map["cieifdot1dbasemappingtable"] = "cieIfDot1dBaseMappingTable"
        self._children_yang_names.add("cieIfDot1dBaseMappingTable")

        self.cieifnamemappingtable = CISCOIFEXTENSIONMIB.Cieifnamemappingtable()
        self.cieifnamemappingtable.parent = self
        self._children_name_map["cieifnamemappingtable"] = "cieIfNameMappingTable"
        self._children_yang_names.add("cieIfNameMappingTable")
        self._segment_path = lambda: "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB"


    class Ciscoifextsystemconfig(Entity):
        """
        
        
        .. attribute:: ciesystemmtu
        
        	Global system MTU in octets. This object specifies the MTU on all interfaces. However, the value specified by cieIfMtu takes precedence for an interface, which means that the interface's MTU uses the value specified by cieIfMtu, if it is configured
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: cielinkupdownenable
        
        	Indicates whether cieLinkUp/cieLinkDown or standard mib\-II defined linkUp/Down or both, notifications should be generated for the interfaces in the system.  'standard'  \- only generate standard defined               mib\-II linkUp/linkDown notification               if 'ifLinkUpDownTrapEnable' for                the interface is 'enabled'. 'cisco'     \- only generate cieLinkUp/cieLinkDown               notifications for an interface if               the 'ifLinkUpDownTrapEnable' for the               interface is 'enabled'.  If both bits are selected then linkUp/linkDown and cieLinkUp/cieLinkDown are both generated for an  interface if the 'ifLinkUpDownTrapEnable' for the interface is 'enabled'
        	**type**\:  :py:class:`Cielinkupdownenable <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.Ciscoifextsystemconfig.Cielinkupdownenable>`
        
        	**status**\: deprecated
        
        .. attribute:: ciestandardlinkupdownvarbinds
        
        	Indicates whether to send the extra varbinds in addition to the varbinds defined  in linkUp/linkDown notifications.  'standard'   \- only send the varbinds defined in                the standard linkUp/linkDown                notification.   'additional' \- send the extra varbinds in addition                 to the defined ones. 'other'      \- any other config not covered by the above.                This value is read\-only
        	**type**\:  :py:class:`Ciestandardlinkupdownvarbinds <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.Ciscoifextsystemconfig.Ciestandardlinkupdownvarbinds>`
        
        	**status**\: deprecated
        
        .. attribute:: cieifindexpersistence
        
        	This object specifies whether ifIndex values persist across reinitialization of the device.  ifIndex persistence means that the mapping between the ifDescr object values and the ifIndex object values will be retained across reboots.  Applications such as device inventory, billing, and fault detection depend on the maintenance of the correspondence between particular ifIndex values and their interfaces. During reboot or insertion of a new card, the data to correlate the interfaces to the ifIndex may become invalid in absence of ifIndex persistence feature.  ifIndex persistence for an interface ensures ifIndex value for the interface will remain the same after a system reboot. Hence, this feature allows users to avoid the workarounds required for consistent interface identification across reinitialization.  Due to change in syntax, this object is deprecated by cieIfIndexGlobalPersistence
        	**type**\: bool
        
        	**status**\: deprecated
        
        .. attribute:: ciedelayedlinkupdownnotifenable
        
        	This object specifies whether the system generates a cieDelayedLinkUpDownNotif notification
        	**type**\: bool
        
        .. attribute:: ciedelayedlinkupdownnotifdelay
        
        	This object specifies the interval of time an interface's operational status must remain stable following a transition before the system will generate a cieDelayedLinkUpDownNotif
        	**type**\: int
        
        	**range:** 1..60
        
        	**units**\: minutes
        
        .. attribute:: cieifindexglobalpersistence
        
        	This object specifies whether ifIndex values persist across reinitialization of the device.  ifIndex persistence means that the mapping between the ifDescr object values and the ifIndex object values will be retained across reboots.  Applications such as device inventory, billing, and fault detection depend on the maintenance of the correspondence between particular ifIndex values and their interfaces. During reboot or insertion of a new card, the data to correlate the interfaces to the ifIndex may become invalid in absence of ifIndex persistence feature.  ifIndex persistence for an interface ensures ifIndex value for the interface will remain the same after a system reboot. Hence, this feature allows users to avoid the workarounds required for consistent interface identification across reinitialization.  The allowed values for this object are either enable or disable. global value is not allowed
        	**type**\:  :py:class:`IfIndexPersistenceState <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.IfIndexPersistenceState>`
        
        .. attribute:: cielinkupdownconfig
        
        	This object specifies whether standard mib\-II defined linkUp/ linkDown, extended linkUp/linkDown (with extra varbinds in addition to the varbinds defined in linkUp/linkDown) or cieLinkUp/cieLinkDown notifications should be generated for the interfaces in the system.  'standardLinkUp'     \- generate standard defined mib\-II                         linkUp notification if                         'ifLinkUpDownTrapEnable' for the                         interface is 'enabled'. 'standardLinkDown'   \- generate standard defined mib\-II                         linkDown notification if                         'ifLinkUpDownTrapEnable' for the                         interface is 'enabled'.   'additionalLinkUp'   \- generate linkUp notification with                        additional varbinds if                         'ifLinkUpDownTrapEnable' for the                         interface is 'enabled'.   'additionalLinkDown' \- generate linkDown notification with                        additional varbinds if                         'ifLinkUpDownTrapEnable' for the                         interface is 'enabled'. 'ciscoLinkUp'        \- generate cieLinkUp notification                        if the 'ifLinkUpDownTrapEnable' for the                        interface is 'enabled'. 'ciscoLinkDown'      \- generate cieLinkDown notification                        if the 'ifLinkUpDownTrapEnable' for the                        interface is 'enabled'.  If multiple bits are set then multiple notifications will be generated for an interface if the 'ifLinkUpDownTrapEnable'  for the interface is 'enabled'
        	**type**\:  :py:class:`Cielinkupdownconfig <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.Ciscoifextsystemconfig.Cielinkupdownconfig>`
        
        

        """

        _prefix = 'CISCO-IF-EXTENSION-MIB'
        _revision = '2013-03-13'

        def __init__(self):
            super(CISCOIFEXTENSIONMIB.Ciscoifextsystemconfig, self).__init__()

            self.yang_name = "ciscoIfExtSystemConfig"
            self.yang_parent_name = "CISCO-IF-EXTENSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ciesystemmtu', YLeaf(YType.int32, 'cieSystemMtu')),
                ('cielinkupdownenable', YLeaf(YType.bits, 'cieLinkUpDownEnable')),
                ('ciestandardlinkupdownvarbinds', YLeaf(YType.enumeration, 'cieStandardLinkUpDownVarbinds')),
                ('cieifindexpersistence', YLeaf(YType.boolean, 'cieIfIndexPersistence')),
                ('ciedelayedlinkupdownnotifenable', YLeaf(YType.boolean, 'cieDelayedLinkUpDownNotifEnable')),
                ('ciedelayedlinkupdownnotifdelay', YLeaf(YType.uint32, 'cieDelayedLinkUpDownNotifDelay')),
                ('cieifindexglobalpersistence', YLeaf(YType.enumeration, 'cieIfIndexGlobalPersistence')),
                ('cielinkupdownconfig', YLeaf(YType.bits, 'cieLinkUpDownConfig')),
            ])
            self.ciesystemmtu = None
            self.cielinkupdownenable = Bits()
            self.ciestandardlinkupdownvarbinds = None
            self.cieifindexpersistence = None
            self.ciedelayedlinkupdownnotifenable = None
            self.ciedelayedlinkupdownnotifdelay = None
            self.cieifindexglobalpersistence = None
            self.cielinkupdownconfig = Bits()
            self._segment_path = lambda: "ciscoIfExtSystemConfig"
            self._absolute_path = lambda: "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIFEXTENSIONMIB.Ciscoifextsystemconfig, ['ciesystemmtu', 'cielinkupdownenable', 'ciestandardlinkupdownvarbinds', 'cieifindexpersistence', 'ciedelayedlinkupdownnotifenable', 'ciedelayedlinkupdownnotifdelay', 'cieifindexglobalpersistence', 'cielinkupdownconfig'], name, value)

        class Ciestandardlinkupdownvarbinds(Enum):
            """
            Ciestandardlinkupdownvarbinds (Enum Class)

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
        	**type**\: list of  		 :py:class:`Cieifpacketstatsentry <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.Cieifpacketstatstable.Cieifpacketstatsentry>`
        
        

        """

        _prefix = 'CISCO-IF-EXTENSION-MIB'
        _revision = '2013-03-13'

        def __init__(self):
            super(CISCOIFEXTENSIONMIB.Cieifpacketstatstable, self).__init__()

            self.yang_name = "cieIfPacketStatsTable"
            self.yang_parent_name = "CISCO-IF-EXTENSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cieIfPacketStatsEntry", ("cieifpacketstatsentry", CISCOIFEXTENSIONMIB.Cieifpacketstatstable.Cieifpacketstatsentry))])
            self._leafs = OrderedDict()

            self.cieifpacketstatsentry = YList(self)
            self._segment_path = lambda: "cieIfPacketStatsTable"
            self._absolute_path = lambda: "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIFEXTENSIONMIB.Cieifpacketstatstable, [], name, value)


        class Cieifpacketstatsentry(Entity):
            """
            An entry into the cieIfPacketStatsTable.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: cieiflastintime
            
            	This object represents the elapsed time in milliseconds since last protocol input  packet was received.  Discontinuities in the value of this variable can occur at re\-initialization of the management system, and at other times as  indicated by the values of  cieIfPacketDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cieiflastouttime
            
            	This object represents the elapsed time in milliseconds since last protocol  output  packet was transmitted.  Discontinuities in the value of this variable can occur at re\-initialization of the management system, and at other times as  indicated by the values of  cieIfPacketDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cieiflastouthangtime
            
            	This object represents the elapsed time in milliseconds since last protocol    output packet could not be successfully transmitted.  Discontinuities in the value of this variable can occur at re\-initialization of the management system, and at other times as  indicated by the values of  cieIfPacketDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cieifinruntserrs
            
            	The number of packets input on a particular physical interface which were dropped as they were smaller than the minimum allowable  physical media limit.  Discontinuities in the value of this variable can occur at re\-initialization of the management system, and at other times as  indicated by the values of  cieIfPacketDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cieifingiantserrs
            
            	The number of input packets on a particular physical interface which were dropped as  they were larger than the ifMtu (largest  permitted  size of a packet which can be  sent/received on an interface).  Discontinuities in the value of this variable can occur at re\-initialization of the management system, and at other times as  indicated by the values of  cieIfPacketDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cieifinframingerrs
            
            	The number of input packets on a physical interface which were misaligned or had framing errors. This happens when the  format of the incoming packet on a physical interface is incorrect.  Discontinuities in the value of this variable can occur at re\-initialization of the management system, and at other times as  indicated by the values of  cieIfPacketDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cieifinoverrunerrs
            
            	The number of input packets which arrived on a particular physical interface which  were too quick for the hardware to receive and hence the receiver ran out of buffers.  Discontinuities in the value of this variable can occur at re\-initialization of the management system, and at other times as  indicated by the values of  cieIfPacketDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cieifinignored
            
            	The number of input packets which were simply ignored by this physical interface due to  insufficient resources to handle the incoming packets.  For example, this could indicate that the input receive buffers are not available or that the receiver lost a packet.  Discontinuities in the value of this variable can occur at re\-initialization of the management system, and at other times as  indicated by the values of  cieIfPacketDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cieifinaborterrs
            
            	Number of input packets which were dropped because the receiver aborted.  Examples of this could be when an abort sequence aborted the input frame or when there is a collision in an ethernet segment.  Discontinuities in the value of this variable can occur at re\-initialization of the management system, and at other times as  indicated by the values of  cieIfPacketDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cieifinputqueuedrops
            
            	The number of input packets which were dropped.  Some reasons why this object could be  incremented are\:  o  Input queue is full. o  Errors at the receiver hardware     while receiving the packet.  Discontinuities in the value of this variable can occur at re\-initialization of the management system, and at other times as  indicated by the values of  cieIfPacketDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cieifoutputqueuedrops
            
            	This object indicates the  number of output packets dropped by the interface even though no error had been detected to prevent them being transmitted.   The packet could be dropped for many reasons, which could range from the interface being down to errors in the format of the packet.  Discontinuities in the value of this variable can occur at re\-initialization of the management system, and at other times as  indicated by the values of  cieIfPacketDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cieifpacketdiscontinuitytime
            
            	The value of sysUpTime on the most recent occasion at which this interface's  counters suffered a discontinuity.   If no such discontinuities have occurred  since the last re\-initialization of the  local management subsystem, then this  object contains a value of zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IF-EXTENSION-MIB'
            _revision = '2013-03-13'

            def __init__(self):
                super(CISCOIFEXTENSIONMIB.Cieifpacketstatstable.Cieifpacketstatsentry, self).__init__()

                self.yang_name = "cieIfPacketStatsEntry"
                self.yang_parent_name = "cieIfPacketStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('cieiflastintime', YLeaf(YType.uint32, 'cieIfLastInTime')),
                    ('cieiflastouttime', YLeaf(YType.uint32, 'cieIfLastOutTime')),
                    ('cieiflastouthangtime', YLeaf(YType.uint32, 'cieIfLastOutHangTime')),
                    ('cieifinruntserrs', YLeaf(YType.uint32, 'cieIfInRuntsErrs')),
                    ('cieifingiantserrs', YLeaf(YType.uint32, 'cieIfInGiantsErrs')),
                    ('cieifinframingerrs', YLeaf(YType.uint32, 'cieIfInFramingErrs')),
                    ('cieifinoverrunerrs', YLeaf(YType.uint32, 'cieIfInOverrunErrs')),
                    ('cieifinignored', YLeaf(YType.uint32, 'cieIfInIgnored')),
                    ('cieifinaborterrs', YLeaf(YType.uint32, 'cieIfInAbortErrs')),
                    ('cieifinputqueuedrops', YLeaf(YType.uint32, 'cieIfInputQueueDrops')),
                    ('cieifoutputqueuedrops', YLeaf(YType.uint32, 'cieIfOutputQueueDrops')),
                    ('cieifpacketdiscontinuitytime', YLeaf(YType.uint32, 'cieIfPacketDiscontinuityTime')),
                ])
                self.ifindex = None
                self.cieiflastintime = None
                self.cieiflastouttime = None
                self.cieiflastouthangtime = None
                self.cieifinruntserrs = None
                self.cieifingiantserrs = None
                self.cieifinframingerrs = None
                self.cieifinoverrunerrs = None
                self.cieifinignored = None
                self.cieifinaborterrs = None
                self.cieifinputqueuedrops = None
                self.cieifoutputqueuedrops = None
                self.cieifpacketdiscontinuitytime = None
                self._segment_path = lambda: "cieIfPacketStatsEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/cieIfPacketStatsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIFEXTENSIONMIB.Cieifpacketstatstable.Cieifpacketstatsentry, ['ifindex', 'cieiflastintime', 'cieiflastouttime', 'cieiflastouthangtime', 'cieifinruntserrs', 'cieifingiantserrs', 'cieifinframingerrs', 'cieifinoverrunerrs', 'cieifinignored', 'cieifinaborterrs', 'cieifinputqueuedrops', 'cieifoutputqueuedrops', 'cieifpacketdiscontinuitytime'], name, value)


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
        	**type**\: list of  		 :py:class:`Cieifinterfaceentry <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.Cieifinterfacetable.Cieifinterfaceentry>`
        
        

        """

        _prefix = 'CISCO-IF-EXTENSION-MIB'
        _revision = '2013-03-13'

        def __init__(self):
            super(CISCOIFEXTENSIONMIB.Cieifinterfacetable, self).__init__()

            self.yang_name = "cieIfInterfaceTable"
            self.yang_parent_name = "CISCO-IF-EXTENSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cieIfInterfaceEntry", ("cieifinterfaceentry", CISCOIFEXTENSIONMIB.Cieifinterfacetable.Cieifinterfaceentry))])
            self._leafs = OrderedDict()

            self.cieifinterfaceentry = YList(self)
            self._segment_path = lambda: "cieIfInterfaceTable"
            self._absolute_path = lambda: "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIFEXTENSIONMIB.Cieifinterfacetable, [], name, value)


        class Cieifinterfaceentry(Entity):
            """
            An entry into the cieIfInterfaceTable.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: cieifresetcount
            
            	The number of times the interface was internally reset and brought up.  Some of the actions which can cause this counter to increment are \:  o  Bringing an interface up using the     interface CLI command.  o  Clearing the interface with the exec    CLI command.  o  Bringing the interface up via SNMP.  Discontinuities in the value of this variable can occur at re\-initialization of the management system, and at other times as  indicated by the values of  cieIfInterfaceDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cieifkeepaliveenabled
            
            	A keepalive is a small, layer\-2 message that is transmitted by a network device  to let directly\-connected network devices know of its presence.  This object returns 'true' if keepalives are enabled on this interface. If keepalives are not enabled, 'false' is returned.  Setting this object to TRUE or FALSE enables or disables (respectively) keepalive on this  interface
            	**type**\: bool
            
            .. attribute:: cieifstatechangereason
            
            	This object displays a human\-readable textual string which describes the  cause of the last state change of the  interface.  Examples of the values this object can take are\:  o  'Lost Carrier' o  'administratively down' o  'up' o  'down'
            	**type**\: str
            
            .. attribute:: cieifcarriertransitioncount
            
            	Number of times interface saw the carrier signal transition.  For example, if a T1 line is unplugged,  then framer will detect the loss of signal  (LOS) on the line  and will count it as a transition.  Discontinuities in the value of this variable can occur at re\-initialization of the management system, and at other times as  indicated by the values of  cieIfInterfaceDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cieifinterfacediscontinuitytime
            
            	The value of sysUpTime on the most recent occasion at which this interface's  counters  suffered  a discontinuity.   If no such discontinuities have occurred  since the last re\-initialization of the  local management subsystem, then this  object contains a value of zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cieifdhcpmode
            
            	The DHCP mode configured by the administrator. If 'true' the DHCP is enabled. In which case an IP address is requested in DHCP. This is in addition to any that are  configured by the administrator in 'ciiIPAddressTable' or 'ciiIPIfAddressTable' in CISCO\-IP\-IF\-MIB. If 'false' the DHCP is disabled. In which case all IP addresses are configured by the administrator in 'ciiIPAddressTable' or  'ciiIPIfAddressTable'. For interfaces, for which DHCP cannot be or is not supported, then this object has the value 'false'
            	**type**\: bool
            
            .. attribute:: cieifmtu
            
            	The MTU configured by the administrator. This object is exactly same as 'ifMtu' in  ifTable from IF\-MIB for the same ifIndex value , except that it is configurable by the administrator. For more description of this object refer to 'ifMtu' in IF\-MIB
            	**type**\: int
            
            	**range:** 40..2147483647
            
            .. attribute:: cieifcontextname
            
            	The ContextName denotes the interface 'context' and is used to logically separate the MIB management. RFC 2571 and RFC 2737 describe this approach. When the agent supports a different SNMP  context, as detailed in RFC 2571 and  RFC 2737, for different interfaces, then the value of this object specifies the context name used for this interface
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: cieifoperstatuscause
            
            	This object represents the detailed operational cause reason for the current  operational state of the interface.  The current operational state of the interface  is given by the 'ifOperStatus' defined  in IF\-MIB.   The corresponding instance of  'cieIfOperStatusCauseDescr' must be used to  get the information about the operational  cause value mentioned in this object.  For interfaces whose 'ifOperStatus' is 'down'  the objects 'cieIfOperStatusCause' and  'cieIfOperStatusCauseDescr' together provides  the information about the operational cause  reason and the description of the cause.   The value of this object will be 'none' for all the 'ifOperStatus' values except for  'down'. Its value will be one status cause  defined in the 'IfOperStatusReason' textual  convention if 'ifOperStatus' is 'down'.   The value of this object will be 'other'  if the operational status cause is not one  defined in 'IfOperStatusReason'
            	**type**\:  :py:class:`IfOperStatusReason <ydk.models.cisco_ios_xe.CISCO_TC.IfOperStatusReason>`
            
            .. attribute:: cieifoperstatuscausedescr
            
            	The description for the cause of current operational state of the interface, given  by the object 'cieIfOperStatusCause'.  For an interface whose 'ifOperStatus' is not 'down' the value of this object will be  'none'
            	**type**\: str
            
            .. attribute:: cieifspeedreceive
            
            	An estimate of the interface's current receive bandwidth in bits per second.  This object is provided for interface with asymmetric interface speeds like ADSL and should be used in conjunction with ifSpeed object.  For interfaces which do not vary in bandwidth or for those where no accurate estimation can be made, this object should contain the nominal bandwidth. If the bandwidth of the interface is greater than the maximum value reportable by this object then this object should report its maximum value (4,294,967,295) and ifHighSpeed must be used to report the interace's speed.  For a sub\-layer which has no concept of bandwidth, this object should be zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cieifhighspeedreceive
            
            	An estimate of the interface's current receive bandwidth in units of 1,000,000 bits per second.  If this object reports a value of `n' then the speed of the interface is somewhere in the range of `n\-500,000' to `n+499,999'.  For interfaces which do not vary in bandwidth or for those where no accurate estimation can be made, this object should contain the nominal bandwidth.  For a sub\-layer which has no concept of bandwidth, this object should be zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cieifowner
            
            	This data type is used to model an administratively assigned name of the current owner of the interface resource. This  information is taken from the NVT ASCII character set.  It is  suggested that this name contain one or more of the following\:  SnmpEngineID, IP address, management station name, network  manager's name, location, or phone number. SNMP access control is articulated entirely in terms of the  contents of MIB views; access to a particular SNMP object  instance depends only upon its presence or absence in a  particular MIB view and never upon its value or the value of  related object instances. Thus, this object affords resolution of resource contention  only among cooperating managers; this object realizes no access control function with respect to uncooperative parties
            	**type**\: str
            
            	**length:** 0..80
            
            .. attribute:: cieifsharedconfig
            
            	This object indicates the current configuration of interface sharing on the given interface.  'notApplicable' \- the interface sharing configuration on              this interface is not applicable.  'ownerDedicated' \- the interface is in the dedicated mode             to the binding physical interface. 'ownerShared' \- the interface is shared amongst virtual switches          and this interface physically belongs to a its           virtual switch.   'sharedOnly' \- the interface is in purely shared mode
            	**type**\:  :py:class:`Cieifsharedconfig <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.Cieifinterfacetable.Cieifinterfaceentry.Cieifsharedconfig>`
            
            .. attribute:: cieifspeedgroupconfig
            
            	This object specifies the current speed group configuration on the given interface.  'notApplicable' \- the interface speed group configuration on             this interface is not applicable. It is a              read\-only value. '10G' \- the interface speed group configuration on             this interface as 10G. '1G\-2G\-4G\-8G' \- the interface speed group configuration              on this interface as 1G\-2G\-4G\-8G. '2G\-4G\-8G\-16G' \- the interface speed group configuration              on this interface as 2G\-4G\-8G\-16G
            	**type**\:  :py:class:`Cieifspeedgroupconfig <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.Cieifinterfacetable.Cieifinterfaceentry.Cieifspeedgroupconfig>`
            
            .. attribute:: cieiftransceiverfrequencyconfig
            
            	This object specifies the current transceiver frequency configuration on the given interface.  'notApplicable' \- the interface transceiver frequency  				  configuration on this interface  				  is not applicable. It is a read\-only value. 'FibreChannel' \- the interface transceiver frequency 				 configuration on this interface as                   Fibre Channel. 'Ethernet'	  \-  the interface transceiver frequency on 				 this interface as Ethernet
            	**type**\:  :py:class:`Cieiftransceiverfrequencyconfig <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.Cieifinterfacetable.Cieifinterfaceentry.Cieiftransceiverfrequencyconfig>`
            
            .. attribute:: cieiffillpatternconfig
            
            	This object specifies the current switchport fill pattern configuration on the given interface.  'arbff8G' \- the inter frame gap fill pattern is 			ARBFF for 8G speed. 'idle8G' \- the inter frame gap fill pattern is 		   IDLE for 8G speed
            	**type**\:  :py:class:`Cieiffillpatternconfig <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.Cieifinterfacetable.Cieifinterfaceentry.Cieiffillpatternconfig>`
            
            .. attribute:: cieifignorebiterrorsconfig
            
            	This object specifies the current switchport biterrors configuration on the given interface.  If 'true(1)' the ignore bit errors is enabled.In which case the interface ignores bit errors. If 'false(2)' the ignore bit errors is disabled. In which  case the interface acts on the bit errors.  For interfaces, for which bit errors  is not supported, then this object has the value 'true(1)'
            	**type**\: bool
            
            .. attribute:: cieifignoreinterruptthresholdconfig
            
            	This object specifies the current interrupt threshold configuration on the given interface.  'If 'true(1)' the ignore interrupt thresholds is enabled. In which case the interface ignores interrupt thresholds. If 'false(2)' the ignore interrupt thresholds is disabled. In which case the interface acts on the interrupt  thresholds.  For interfaces, for which interrupt thresholds  is not supported, then this object has the  value 'true(1)'
            	**type**\: bool
            
            

            """

            _prefix = 'CISCO-IF-EXTENSION-MIB'
            _revision = '2013-03-13'

            def __init__(self):
                super(CISCOIFEXTENSIONMIB.Cieifinterfacetable.Cieifinterfaceentry, self).__init__()

                self.yang_name = "cieIfInterfaceEntry"
                self.yang_parent_name = "cieIfInterfaceTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('cieifresetcount', YLeaf(YType.uint32, 'cieIfResetCount')),
                    ('cieifkeepaliveenabled', YLeaf(YType.boolean, 'cieIfKeepAliveEnabled')),
                    ('cieifstatechangereason', YLeaf(YType.str, 'cieIfStateChangeReason')),
                    ('cieifcarriertransitioncount', YLeaf(YType.uint32, 'cieIfCarrierTransitionCount')),
                    ('cieifinterfacediscontinuitytime', YLeaf(YType.uint32, 'cieIfInterfaceDiscontinuityTime')),
                    ('cieifdhcpmode', YLeaf(YType.boolean, 'cieIfDhcpMode')),
                    ('cieifmtu', YLeaf(YType.int32, 'cieIfMtu')),
                    ('cieifcontextname', YLeaf(YType.str, 'cieIfContextName')),
                    ('cieifoperstatuscause', YLeaf(YType.enumeration, 'cieIfOperStatusCause')),
                    ('cieifoperstatuscausedescr', YLeaf(YType.str, 'cieIfOperStatusCauseDescr')),
                    ('cieifspeedreceive', YLeaf(YType.uint32, 'cieIfSpeedReceive')),
                    ('cieifhighspeedreceive', YLeaf(YType.uint32, 'cieIfHighSpeedReceive')),
                    ('cieifowner', YLeaf(YType.str, 'cieIfOwner')),
                    ('cieifsharedconfig', YLeaf(YType.enumeration, 'cieIfSharedConfig')),
                    ('cieifspeedgroupconfig', YLeaf(YType.enumeration, 'cieIfSpeedGroupConfig')),
                    ('cieiftransceiverfrequencyconfig', YLeaf(YType.enumeration, 'cieIfTransceiverFrequencyConfig')),
                    ('cieiffillpatternconfig', YLeaf(YType.enumeration, 'cieIfFillPatternConfig')),
                    ('cieifignorebiterrorsconfig', YLeaf(YType.boolean, 'cieIfIgnoreBitErrorsConfig')),
                    ('cieifignoreinterruptthresholdconfig', YLeaf(YType.boolean, 'cieIfIgnoreInterruptThresholdConfig')),
                ])
                self.ifindex = None
                self.cieifresetcount = None
                self.cieifkeepaliveenabled = None
                self.cieifstatechangereason = None
                self.cieifcarriertransitioncount = None
                self.cieifinterfacediscontinuitytime = None
                self.cieifdhcpmode = None
                self.cieifmtu = None
                self.cieifcontextname = None
                self.cieifoperstatuscause = None
                self.cieifoperstatuscausedescr = None
                self.cieifspeedreceive = None
                self.cieifhighspeedreceive = None
                self.cieifowner = None
                self.cieifsharedconfig = None
                self.cieifspeedgroupconfig = None
                self.cieiftransceiverfrequencyconfig = None
                self.cieiffillpatternconfig = None
                self.cieifignorebiterrorsconfig = None
                self.cieifignoreinterruptthresholdconfig = None
                self._segment_path = lambda: "cieIfInterfaceEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/cieIfInterfaceTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIFEXTENSIONMIB.Cieifinterfacetable.Cieifinterfaceentry, ['ifindex', 'cieifresetcount', 'cieifkeepaliveenabled', 'cieifstatechangereason', 'cieifcarriertransitioncount', 'cieifinterfacediscontinuitytime', 'cieifdhcpmode', 'cieifmtu', 'cieifcontextname', 'cieifoperstatuscause', 'cieifoperstatuscausedescr', 'cieifspeedreceive', 'cieifhighspeedreceive', 'cieifowner', 'cieifsharedconfig', 'cieifspeedgroupconfig', 'cieiftransceiverfrequencyconfig', 'cieiffillpatternconfig', 'cieifignorebiterrorsconfig', 'cieifignoreinterruptthresholdconfig'], name, value)

            class Cieiffillpatternconfig(Enum):
                """
                Cieiffillpatternconfig (Enum Class)

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
                Cieifsharedconfig (Enum Class)

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
                Cieifspeedgroupconfig (Enum Class)

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
                Cieiftransceiverfrequencyconfig (Enum Class)

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
        	**type**\: list of  		 :py:class:`Cieifstatuslistentry <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.Cieifstatuslisttable.Cieifstatuslistentry>`
        
        

        """

        _prefix = 'CISCO-IF-EXTENSION-MIB'
        _revision = '2013-03-13'

        def __init__(self):
            super(CISCOIFEXTENSIONMIB.Cieifstatuslisttable, self).__init__()

            self.yang_name = "cieIfStatusListTable"
            self.yang_parent_name = "CISCO-IF-EXTENSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cieIfStatusListEntry", ("cieifstatuslistentry", CISCOIFEXTENSIONMIB.Cieifstatuslisttable.Cieifstatuslistentry))])
            self._leafs = OrderedDict()

            self.cieifstatuslistentry = YList(self)
            self._segment_path = lambda: "cieIfStatusListTable"
            self._absolute_path = lambda: "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIFEXTENSIONMIB.Cieifstatuslisttable, [], name, value)


        class Cieifstatuslistentry(Entity):
            """
            Each entry represents the 'ifIndex',
            interface operational mode and interface 
            operational cause for a set of 64 interfaces 
            in a module.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cieifstatuslistindex  (key)
            
            	An arbitrary integer value, greater than zero, which identifies a list of 64 interfaces within a module
            	**type**\: int
            
            	**range:** 1..33554432
            
            .. attribute:: cieinterfacesindex
            
            	This object represents the 'ifIndex' for a set of 64 interfaces in the module
            	**type**\: str
            
            	**length:** 0..256
            
            .. attribute:: cieinterfacesopermode
            
            	This object represents the operational mode for a set of 64 interfaces in the module
            	**type**\: str
            
            	**length:** 0..64
            
            .. attribute:: cieinterfacesopercause
            
            	This object represents the operational status cause for a set of 64 interfaces in the  module
            	**type**\: str
            
            	**length:** 0..128
            
            .. attribute:: cieinterfaceownershipbitmap
            
            	This object indicates the status for a set of 64 interfaces in a module regarding whether or not each interface is  administratively assigned a name of the current owner of the  interface resource as per cieIfOwner
            	**type**\: str
            
            	**length:** 0..8
            
            

            """

            _prefix = 'CISCO-IF-EXTENSION-MIB'
            _revision = '2013-03-13'

            def __init__(self):
                super(CISCOIFEXTENSIONMIB.Cieifstatuslisttable.Cieifstatuslistentry, self).__init__()

                self.yang_name = "cieIfStatusListEntry"
                self.yang_parent_name = "cieIfStatusListTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','cieifstatuslistindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', YLeaf(YType.str, 'entPhysicalIndex')),
                    ('cieifstatuslistindex', YLeaf(YType.uint32, 'cieIfStatusListIndex')),
                    ('cieinterfacesindex', YLeaf(YType.str, 'cieInterfacesIndex')),
                    ('cieinterfacesopermode', YLeaf(YType.str, 'cieInterfacesOperMode')),
                    ('cieinterfacesopercause', YLeaf(YType.str, 'cieInterfacesOperCause')),
                    ('cieinterfaceownershipbitmap', YLeaf(YType.str, 'cieInterfaceOwnershipBitmap')),
                ])
                self.entphysicalindex = None
                self.cieifstatuslistindex = None
                self.cieinterfacesindex = None
                self.cieinterfacesopermode = None
                self.cieinterfacesopercause = None
                self.cieinterfaceownershipbitmap = None
                self._segment_path = lambda: "cieIfStatusListEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']" + "[cieIfStatusListIndex='" + str(self.cieifstatuslistindex) + "']"
                self._absolute_path = lambda: "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/cieIfStatusListTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIFEXTENSIONMIB.Cieifstatuslisttable.Cieifstatuslistentry, ['entphysicalindex', 'cieifstatuslistindex', 'cieinterfacesindex', 'cieinterfacesopermode', 'cieinterfacesopercause', 'cieinterfaceownershipbitmap'], name, value)


    class Cieifvlstatstable(Entity):
        """
        This table contains VL (Virtual Link) statistics
        for a capable interface.
        
        Objects defined in this table may be 
        applicable to physical interfaces only.
        
        .. attribute:: cieifvlstatsentry
        
        	Each row contains managed objects for Virtual Link statistics on interface capable of  providing this information
        	**type**\: list of  		 :py:class:`Cieifvlstatsentry <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.Cieifvlstatstable.Cieifvlstatsentry>`
        
        

        """

        _prefix = 'CISCO-IF-EXTENSION-MIB'
        _revision = '2013-03-13'

        def __init__(self):
            super(CISCOIFEXTENSIONMIB.Cieifvlstatstable, self).__init__()

            self.yang_name = "cieIfVlStatsTable"
            self.yang_parent_name = "CISCO-IF-EXTENSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cieIfVlStatsEntry", ("cieifvlstatsentry", CISCOIFEXTENSIONMIB.Cieifvlstatstable.Cieifvlstatsentry))])
            self._leafs = OrderedDict()

            self.cieifvlstatsentry = YList(self)
            self._segment_path = lambda: "cieIfVlStatsTable"
            self._absolute_path = lambda: "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIFEXTENSIONMIB.Cieifvlstatstable, [], name, value)


        class Cieifvlstatsentry(Entity):
            """
            Each row contains managed objects for
            Virtual Link statistics on interface capable of 
            providing this information.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: cieifnodropvlinpkts
            
            	This object indicates the number of input packets on all No\-Drop Virtual Links belonged  to this interface
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cieifnodropvlinoctets
            
            	This object indicates the number of input octets on all No\-Drop Virtual Links belonged  to this interface
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cieifnodropvloutpkts
            
            	This object indicates the number of output packets on all No\-Drop Virtual Links belonged  to this interface
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cieifnodropvloutoctets
            
            	This object indicates the number of output octets on all No\-Drop Virtual Links belonged  to this interface
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cieifdropvlinpkts
            
            	This object indicates the number of input packets on all Drop Virtual Links belonged  to this interface
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cieifdropvlinoctets
            
            	This object indicates the number of input octets on all Drop Virtual Links belonged  to this interface
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cieifdropvloutpkts
            
            	This object indicates the number of output packets on all Drop Virtual Links belonged  to this interface
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cieifdropvloutoctets
            
            	This object indicates the number of output octets on all Drop Virtual Links belonged  to this interface
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'CISCO-IF-EXTENSION-MIB'
            _revision = '2013-03-13'

            def __init__(self):
                super(CISCOIFEXTENSIONMIB.Cieifvlstatstable.Cieifvlstatsentry, self).__init__()

                self.yang_name = "cieIfVlStatsEntry"
                self.yang_parent_name = "cieIfVlStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('cieifnodropvlinpkts', YLeaf(YType.uint64, 'cieIfNoDropVlInPkts')),
                    ('cieifnodropvlinoctets', YLeaf(YType.uint64, 'cieIfNoDropVlInOctets')),
                    ('cieifnodropvloutpkts', YLeaf(YType.uint64, 'cieIfNoDropVlOutPkts')),
                    ('cieifnodropvloutoctets', YLeaf(YType.uint64, 'cieIfNoDropVlOutOctets')),
                    ('cieifdropvlinpkts', YLeaf(YType.uint64, 'cieIfDropVlInPkts')),
                    ('cieifdropvlinoctets', YLeaf(YType.uint64, 'cieIfDropVlInOctets')),
                    ('cieifdropvloutpkts', YLeaf(YType.uint64, 'cieIfDropVlOutPkts')),
                    ('cieifdropvloutoctets', YLeaf(YType.uint64, 'cieIfDropVlOutOctets')),
                ])
                self.ifindex = None
                self.cieifnodropvlinpkts = None
                self.cieifnodropvlinoctets = None
                self.cieifnodropvloutpkts = None
                self.cieifnodropvloutoctets = None
                self.cieifdropvlinpkts = None
                self.cieifdropvlinoctets = None
                self.cieifdropvloutpkts = None
                self.cieifdropvloutoctets = None
                self._segment_path = lambda: "cieIfVlStatsEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/cieIfVlStatsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIFEXTENSIONMIB.Cieifvlstatstable.Cieifvlstatsentry, ['ifindex', 'cieifnodropvlinpkts', 'cieifnodropvlinoctets', 'cieifnodropvloutpkts', 'cieifnodropvloutoctets', 'cieifdropvlinpkts', 'cieifdropvlinoctets', 'cieifdropvloutpkts', 'cieifdropvloutoctets'], name, value)


    class Cieifindexpersistencetable(Entity):
        """
        This table lists configuration data relating to ifIndex
        persistence.
        
        This table has a sparse dependent relationship on the ifTable,
        containing a row for each ifEntry corresponding to an interface
        for which ifIndex persistence is supported.
        
        .. attribute:: cieifindexpersistenceentry
        
        	Each entry represents ifindex persistence configuration for an interface specified by ifIndex. Whenever an interface which supports ifindex persistence is created/destroyed in the ifTable, the corresponding ifindex persistence entry is created/destroyed respectively. Some of the interfaces may not support ifindex persistence, for example, a dynamic interface, such as a PPP connection or a IP subscriber interface
        	**type**\: list of  		 :py:class:`Cieifindexpersistenceentry <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.Cieifindexpersistencetable.Cieifindexpersistenceentry>`
        
        

        """

        _prefix = 'CISCO-IF-EXTENSION-MIB'
        _revision = '2013-03-13'

        def __init__(self):
            super(CISCOIFEXTENSIONMIB.Cieifindexpersistencetable, self).__init__()

            self.yang_name = "cieIfIndexPersistenceTable"
            self.yang_parent_name = "CISCO-IF-EXTENSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cieIfIndexPersistenceEntry", ("cieifindexpersistenceentry", CISCOIFEXTENSIONMIB.Cieifindexpersistencetable.Cieifindexpersistenceentry))])
            self._leafs = OrderedDict()

            self.cieifindexpersistenceentry = YList(self)
            self._segment_path = lambda: "cieIfIndexPersistenceTable"
            self._absolute_path = lambda: "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIFEXTENSIONMIB.Cieifindexpersistencetable, [], name, value)


        class Cieifindexpersistenceentry(Entity):
            """
            Each entry represents ifindex persistence configuration for an
            interface specified by ifIndex. Whenever an interface which
            supports ifindex persistence is created/destroyed in the
            ifTable, the corresponding ifindex persistence entry is
            created/destroyed respectively. Some of the interfaces may not
            support ifindex persistence, for example, a dynamic interface,
            such as a PPP connection or a IP subscriber interface.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: cieifindexpersistenceenabled
            
            	This object specifies whether the interface's ifIndex value persist across reinitialization.  Due to change in syntax, this object is deprecated by cieIfIndexPersistenceControl
            	**type**\: bool
            
            	**status**\: deprecated
            
            .. attribute:: cieifindexpersistencecontrol
            
            	This object specifies whether the interface's ifIndex value persist across reinitialization. In global state, the interface uses the global setting data for persistence i.e. cieIfIndexGlobalPersistence
            	**type**\:  :py:class:`IfIndexPersistenceState <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.IfIndexPersistenceState>`
            
            

            """

            _prefix = 'CISCO-IF-EXTENSION-MIB'
            _revision = '2013-03-13'

            def __init__(self):
                super(CISCOIFEXTENSIONMIB.Cieifindexpersistencetable.Cieifindexpersistenceentry, self).__init__()

                self.yang_name = "cieIfIndexPersistenceEntry"
                self.yang_parent_name = "cieIfIndexPersistenceTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('cieifindexpersistenceenabled', YLeaf(YType.boolean, 'cieIfIndexPersistenceEnabled')),
                    ('cieifindexpersistencecontrol', YLeaf(YType.enumeration, 'cieIfIndexPersistenceControl')),
                ])
                self.ifindex = None
                self.cieifindexpersistenceenabled = None
                self.cieifindexpersistencecontrol = None
                self._segment_path = lambda: "cieIfIndexPersistenceEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/cieIfIndexPersistenceTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIFEXTENSIONMIB.Cieifindexpersistencetable.Cieifindexpersistenceentry, ['ifindex', 'cieifindexpersistenceenabled', 'cieifindexpersistencecontrol'], name, value)


    class Cieifdot1Qcustomethertypetable(Entity):
        """
        A list of the interfaces that support
        the 802.1q custom Ethertype feature.
        
        .. attribute:: cieifdot1qcustomethertypeentry
        
        	An entry containing the custom EtherType information for the interface.  Only interfaces with custom 802.1q ethertype control are listed in the  table
        	**type**\: list of  		 :py:class:`Cieifdot1Qcustomethertypeentry <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.Cieifdot1Qcustomethertypetable.Cieifdot1Qcustomethertypeentry>`
        
        

        """

        _prefix = 'CISCO-IF-EXTENSION-MIB'
        _revision = '2013-03-13'

        def __init__(self):
            super(CISCOIFEXTENSIONMIB.Cieifdot1Qcustomethertypetable, self).__init__()

            self.yang_name = "cieIfDot1qCustomEtherTypeTable"
            self.yang_parent_name = "CISCO-IF-EXTENSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cieIfDot1qCustomEtherTypeEntry", ("cieifdot1qcustomethertypeentry", CISCOIFEXTENSIONMIB.Cieifdot1Qcustomethertypetable.Cieifdot1Qcustomethertypeentry))])
            self._leafs = OrderedDict()

            self.cieifdot1qcustomethertypeentry = YList(self)
            self._segment_path = lambda: "cieIfDot1qCustomEtherTypeTable"
            self._absolute_path = lambda: "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIFEXTENSIONMIB.Cieifdot1Qcustomethertypetable, [], name, value)


        class Cieifdot1Qcustomethertypeentry(Entity):
            """
            An entry containing the custom EtherType
            information for the interface.
            
            Only interfaces with custom 802.1q
            ethertype control are listed in the 
            table.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: cieifdot1qcustomadminethertype
            
            	The Dot1qEtherType allow administrator to select a non\-standard (other than 0x8100) 2\-byte ethertype for the interface to  interoperate with third party vendor's system that do not use the standard 0x8100 ethertype to identify 802.1q\-tagged frames.  The current administrative value of the  802.1q ethertype for the interface.  The administrative 802.1q ethertype value may  differ from the operational 802.1q ethertype value.  On some platforms, 802.1q ethertype may be assigned per group rather than per port. If multiple ports belong to a port group, the 802.1q ethertype assigned to any of the ports in such group will apply to all ports in the same group.  To configure non\-standard dot1q ethertype is only recommended when the Cisco device is connected to any third party vendor device. Also be advised that the custom ethertype value needs to be changed in the whole cloud of  Cisco device with the same custom ethertype  value if the third party device are separated  by number of Cisco device in the middle
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cieifdot1qcustomoperethertype
            
            	The current operational value of the 802.1q ethertype for the interface
            	**type**\: int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'CISCO-IF-EXTENSION-MIB'
            _revision = '2013-03-13'

            def __init__(self):
                super(CISCOIFEXTENSIONMIB.Cieifdot1Qcustomethertypetable.Cieifdot1Qcustomethertypeentry, self).__init__()

                self.yang_name = "cieIfDot1qCustomEtherTypeEntry"
                self.yang_parent_name = "cieIfDot1qCustomEtherTypeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('cieifdot1qcustomadminethertype', YLeaf(YType.int32, 'cieIfDot1qCustomAdminEtherType')),
                    ('cieifdot1qcustomoperethertype', YLeaf(YType.int32, 'cieIfDot1qCustomOperEtherType')),
                ])
                self.ifindex = None
                self.cieifdot1qcustomadminethertype = None
                self.cieifdot1qcustomoperethertype = None
                self._segment_path = lambda: "cieIfDot1qCustomEtherTypeEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/cieIfDot1qCustomEtherTypeTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIFEXTENSIONMIB.Cieifdot1Qcustomethertypetable.Cieifdot1Qcustomethertypeentry, ['ifindex', 'cieifdot1qcustomadminethertype', 'cieifdot1qcustomoperethertype'], name, value)


    class Cieifutiltable(Entity):
        """
        This table contains the interface utilization
        rates for inbound and outbound traffic on an
        interface.
        
        .. attribute:: cieifutilentry
        
        	An entry containing utilization rates for the interface.  Every interface for which the  inbound and  outbound traffic information is available has a corresponding entry in this table
        	**type**\: list of  		 :py:class:`Cieifutilentry <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.Cieifutiltable.Cieifutilentry>`
        
        

        """

        _prefix = 'CISCO-IF-EXTENSION-MIB'
        _revision = '2013-03-13'

        def __init__(self):
            super(CISCOIFEXTENSIONMIB.Cieifutiltable, self).__init__()

            self.yang_name = "cieIfUtilTable"
            self.yang_parent_name = "CISCO-IF-EXTENSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cieIfUtilEntry", ("cieifutilentry", CISCOIFEXTENSIONMIB.Cieifutiltable.Cieifutilentry))])
            self._leafs = OrderedDict()

            self.cieifutilentry = YList(self)
            self._segment_path = lambda: "cieIfUtilTable"
            self._absolute_path = lambda: "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIFEXTENSIONMIB.Cieifutiltable, [], name, value)


        class Cieifutilentry(Entity):
            """
            An entry containing utilization rates for the
            interface.
            
            Every interface for which the  inbound and 
            outbound traffic information is available
            has a corresponding entry in this table.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: cieifinpktrate
            
            	By default, this is the five minute exponentially\-decayed moving average of the inbound packet rate for this interface. However, if the corresponding instance of cieIfInterval is instantiated with a value which specifies an interval different from 5\-minutes, then cieIfInPktRate is the exponentially\-decayed moving average of inbound packet rate over this different time interval
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets per second
            
            .. attribute:: cieifinoctetrate
            
            	By default, this is the five minute exponentially\-decayed moving average of the inbound octet rate for this interface. However, if the corresponding instance of cieIfInterval is instantiated with a value which specifies an interval different from 5\-minutes, then cieIfInOctetRate is the exponentially\-decayed moving average of inbound octet rate over this different time interval
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: octets per second
            
            .. attribute:: cieifoutpktrate
            
            	By default, this is the five minute exponentially\-decayed moving average of the outbound packet rate for this interface. However, if the corresponding instance of cieIfInterval is instantiated with a value which specifies an interval different from 5\-minutes, then cieIfOutPktRate is the exponentially\-decayed moving average of outbound packet rate over this different time interval
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets per second
            
            .. attribute:: cieifoutoctetrate
            
            	By default, this is the five minute exponentially\-decayed moving average of the outbound octet rate for this interface. However, if the corresponding instance of cieIfInterval is instantiated with a value which specifies an interval different from 5\-minutes, then cieIfOutOctetRate is the exponentially\-decayed moving average of outbound octet rate over this different time interval
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: octets per second
            
            .. attribute:: cieifinterval
            
            	This object specifies the time interval over which the inbound and outbound traffic rates are calculated for this interface
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**units**\: seconds
            
            

            """

            _prefix = 'CISCO-IF-EXTENSION-MIB'
            _revision = '2013-03-13'

            def __init__(self):
                super(CISCOIFEXTENSIONMIB.Cieifutiltable.Cieifutilentry, self).__init__()

                self.yang_name = "cieIfUtilEntry"
                self.yang_parent_name = "cieIfUtilTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('cieifinpktrate', YLeaf(YType.uint64, 'cieIfInPktRate')),
                    ('cieifinoctetrate', YLeaf(YType.uint64, 'cieIfInOctetRate')),
                    ('cieifoutpktrate', YLeaf(YType.uint64, 'cieIfOutPktRate')),
                    ('cieifoutoctetrate', YLeaf(YType.uint64, 'cieIfOutOctetRate')),
                    ('cieifinterval', YLeaf(YType.uint32, 'cieIfInterval')),
                ])
                self.ifindex = None
                self.cieifinpktrate = None
                self.cieifinoctetrate = None
                self.cieifoutpktrate = None
                self.cieifoutoctetrate = None
                self.cieifinterval = None
                self._segment_path = lambda: "cieIfUtilEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/cieIfUtilTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIFEXTENSIONMIB.Cieifutiltable.Cieifutilentry, ['ifindex', 'cieifinpktrate', 'cieifinoctetrate', 'cieifoutpktrate', 'cieifoutoctetrate', 'cieifinterval'], name, value)


    class Cieifdot1Dbasemappingtable(Entity):
        """
        This table contains the mappings of the
        ifIndex of an interface to its
        corresponding dot1dBasePort value.
        
        .. attribute:: cieifdot1dbasemappingentry
        
        	An entry containing the mapping between the ifIndex value of an interface and its corresponding dot1dBasePort value.  Every interface which has been assigned a dot1dBasePort value by the system has a corresponding entry in this table
        	**type**\: list of  		 :py:class:`Cieifdot1Dbasemappingentry <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.Cieifdot1Dbasemappingtable.Cieifdot1Dbasemappingentry>`
        
        

        """

        _prefix = 'CISCO-IF-EXTENSION-MIB'
        _revision = '2013-03-13'

        def __init__(self):
            super(CISCOIFEXTENSIONMIB.Cieifdot1Dbasemappingtable, self).__init__()

            self.yang_name = "cieIfDot1dBaseMappingTable"
            self.yang_parent_name = "CISCO-IF-EXTENSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cieIfDot1dBaseMappingEntry", ("cieifdot1dbasemappingentry", CISCOIFEXTENSIONMIB.Cieifdot1Dbasemappingtable.Cieifdot1Dbasemappingentry))])
            self._leafs = OrderedDict()

            self.cieifdot1dbasemappingentry = YList(self)
            self._segment_path = lambda: "cieIfDot1dBaseMappingTable"
            self._absolute_path = lambda: "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIFEXTENSIONMIB.Cieifdot1Dbasemappingtable, [], name, value)


        class Cieifdot1Dbasemappingentry(Entity):
            """
            An entry containing the mapping between
            the ifIndex value of an interface and its
            corresponding dot1dBasePort value.
            
            Every interface which has been assigned
            a dot1dBasePort value by the system
            has a corresponding entry in this table.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: cieifdot1dbasemappingport
            
            	The dot1dBasePort value for this interface
            	**type**\: int
            
            	**range:** 1..65535
            
            

            """

            _prefix = 'CISCO-IF-EXTENSION-MIB'
            _revision = '2013-03-13'

            def __init__(self):
                super(CISCOIFEXTENSIONMIB.Cieifdot1Dbasemappingtable.Cieifdot1Dbasemappingentry, self).__init__()

                self.yang_name = "cieIfDot1dBaseMappingEntry"
                self.yang_parent_name = "cieIfDot1dBaseMappingTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('cieifdot1dbasemappingport', YLeaf(YType.int32, 'cieIfDot1dBaseMappingPort')),
                ])
                self.ifindex = None
                self.cieifdot1dbasemappingport = None
                self._segment_path = lambda: "cieIfDot1dBaseMappingEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/cieIfDot1dBaseMappingTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIFEXTENSIONMIB.Cieifdot1Dbasemappingtable.Cieifdot1Dbasemappingentry, ['ifindex', 'cieifdot1dbasemappingport'], name, value)


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
        	**type**\: list of  		 :py:class:`Cieifnamemappingentry <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.Cieifnamemappingtable.Cieifnamemappingentry>`
        
        

        """

        _prefix = 'CISCO-IF-EXTENSION-MIB'
        _revision = '2013-03-13'

        def __init__(self):
            super(CISCOIFEXTENSIONMIB.Cieifnamemappingtable, self).__init__()

            self.yang_name = "cieIfNameMappingTable"
            self.yang_parent_name = "CISCO-IF-EXTENSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cieIfNameMappingEntry", ("cieifnamemappingentry", CISCOIFEXTENSIONMIB.Cieifnamemappingtable.Cieifnamemappingentry))])
            self._leafs = OrderedDict()

            self.cieifnamemappingentry = YList(self)
            self._segment_path = lambda: "cieIfNameMappingTable"
            self._absolute_path = lambda: "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIFEXTENSIONMIB.Cieifnamemappingtable, [], name, value)


        class Cieifnamemappingentry(Entity):
            """
            An entry into the cieIfNameMappingTable.
            
            .. attribute:: cieifname  (key)
            
            	Represents an interface name mentioned in the 'ifName' object of this system
            	**type**\: str
            
            	**length:** 1..112
            
            .. attribute:: cieifindex
            
            	This object represents the 'ifIndex' corresponding to the interface name mentioned in the 'cieIfName' object of this instance. If the 'ifName' mentioned in the 'cieIfName'  object of this instance corresponds to multiple 'ifIndex' values, then the value of this object is the numerically smallest of those multiple  'ifIndex' values
            	**type**\: int
            
            	**range:** 0..2147483647
            
            

            """

            _prefix = 'CISCO-IF-EXTENSION-MIB'
            _revision = '2013-03-13'

            def __init__(self):
                super(CISCOIFEXTENSIONMIB.Cieifnamemappingtable.Cieifnamemappingentry, self).__init__()

                self.yang_name = "cieIfNameMappingEntry"
                self.yang_parent_name = "cieIfNameMappingTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cieifname']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cieifname', YLeaf(YType.str, 'cieIfName')),
                    ('cieifindex', YLeaf(YType.int32, 'cieIfIndex')),
                ])
                self.cieifname = None
                self.cieifindex = None
                self._segment_path = lambda: "cieIfNameMappingEntry" + "[cieIfName='" + str(self.cieifname) + "']"
                self._absolute_path = lambda: "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/cieIfNameMappingTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIFEXTENSIONMIB.Cieifnamemappingtable.Cieifnamemappingentry, ['cieifname', 'cieifindex'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOIFEXTENSIONMIB()
        return self._top_entity


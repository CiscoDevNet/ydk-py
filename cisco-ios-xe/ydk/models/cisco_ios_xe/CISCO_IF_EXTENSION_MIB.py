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
    
    	
    	**type**\:  :py:class:`CiscoIfExtSystemConfig <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.CiscoIfExtSystemConfig>`
    
    	**config**\: False
    
    .. attribute:: cieifpacketstatstable
    
    	This  table contains interface packet statistics which are not available in  IF\-MIB(RFC2863).   As an example, some interfaces to which objects in this table are applicable are as follows \:          o Ethernet         o FastEthernet         o ATM         o BRI         o Sonet         o GigabitEthernet  Some objects defined in this table may be  applicable to physical interfaces only. As a result, this table may be sparse for some logical interfaces
    	**type**\:  :py:class:`CieIfPacketStatsTable <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.CieIfPacketStatsTable>`
    
    	**config**\: False
    
    .. attribute:: cieifinterfacetable
    
    	This  table contains objects which provide more information about interface   properties not available in IF\-MIB (RFC 2863).  Some objects defined in this table may be applicable to physical interfaces only. As a result, this table may be sparse for logical interfaces
    	**type**\:  :py:class:`CieIfInterfaceTable <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.CieIfInterfaceTable>`
    
    	**config**\: False
    
    .. attribute:: cieifstatuslisttable
    
    	This table contains objects for providing the 'ifIndex', interface operational mode and  interface operational cause for all the  interfaces in the modules.  This table contains one entry for each  64 interfaces in an module.  This table provides efficient way of encoding  'ifIndex', interface operational mode and interface operational cause, from the point  of retrieval, by combining the values a set  of 64 interfaces in a single MIB object
    	**type**\:  :py:class:`CieIfStatusListTable <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.CieIfStatusListTable>`
    
    	**config**\: False
    
    .. attribute:: cieifvlstatstable
    
    	This table contains VL (Virtual Link) statistics for a capable interface.  Objects defined in this table may be  applicable to physical interfaces only
    	**type**\:  :py:class:`CieIfVlStatsTable <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.CieIfVlStatsTable>`
    
    	**config**\: False
    
    .. attribute:: cieifindexpersistencetable
    
    	This table lists configuration data relating to ifIndex persistence.  This table has a sparse dependent relationship on the ifTable, containing a row for each ifEntry corresponding to an interface for which ifIndex persistence is supported
    	**type**\:  :py:class:`CieIfIndexPersistenceTable <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.CieIfIndexPersistenceTable>`
    
    	**config**\: False
    
    .. attribute:: cieifdot1qcustomethertypetable
    
    	A list of the interfaces that support the 802.1q custom Ethertype feature
    	**type**\:  :py:class:`CieIfDot1qCustomEtherTypeTable <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.CieIfDot1qCustomEtherTypeTable>`
    
    	**config**\: False
    
    .. attribute:: cieifutiltable
    
    	This table contains the interface utilization rates for inbound and outbound traffic on an interface
    	**type**\:  :py:class:`CieIfUtilTable <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.CieIfUtilTable>`
    
    	**config**\: False
    
    .. attribute:: cieifdot1dbasemappingtable
    
    	This table contains the mappings of the ifIndex of an interface to its corresponding dot1dBasePort value
    	**type**\:  :py:class:`CieIfDot1dBaseMappingTable <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.CieIfDot1dBaseMappingTable>`
    
    	**config**\: False
    
    .. attribute:: cieifnamemappingtable
    
    	This table contains objects for providing the 'ifName' to 'ifIndex' mapping. This table contains one entry for each valid 'ifName' available in the system. Upon the first request, the implementation of this table will get all the available ifNames, and it will populate the entries in this table, it maintains this ifNames in a cache for ~30 seconds
    	**type**\:  :py:class:`CieIfNameMappingTable <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.CieIfNameMappingTable>`
    
    	**config**\: False
    
    

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
        self._child_classes = OrderedDict([("ciscoIfExtSystemConfig", ("ciscoifextsystemconfig", CISCOIFEXTENSIONMIB.CiscoIfExtSystemConfig)), ("cieIfPacketStatsTable", ("cieifpacketstatstable", CISCOIFEXTENSIONMIB.CieIfPacketStatsTable)), ("cieIfInterfaceTable", ("cieifinterfacetable", CISCOIFEXTENSIONMIB.CieIfInterfaceTable)), ("cieIfStatusListTable", ("cieifstatuslisttable", CISCOIFEXTENSIONMIB.CieIfStatusListTable)), ("cieIfVlStatsTable", ("cieifvlstatstable", CISCOIFEXTENSIONMIB.CieIfVlStatsTable)), ("cieIfIndexPersistenceTable", ("cieifindexpersistencetable", CISCOIFEXTENSIONMIB.CieIfIndexPersistenceTable)), ("cieIfDot1qCustomEtherTypeTable", ("cieifdot1qcustomethertypetable", CISCOIFEXTENSIONMIB.CieIfDot1qCustomEtherTypeTable)), ("cieIfUtilTable", ("cieifutiltable", CISCOIFEXTENSIONMIB.CieIfUtilTable)), ("cieIfDot1dBaseMappingTable", ("cieifdot1dbasemappingtable", CISCOIFEXTENSIONMIB.CieIfDot1dBaseMappingTable)), ("cieIfNameMappingTable", ("cieifnamemappingtable", CISCOIFEXTENSIONMIB.CieIfNameMappingTable))])
        self._leafs = OrderedDict()

        self.ciscoifextsystemconfig = CISCOIFEXTENSIONMIB.CiscoIfExtSystemConfig()
        self.ciscoifextsystemconfig.parent = self
        self._children_name_map["ciscoifextsystemconfig"] = "ciscoIfExtSystemConfig"

        self.cieifpacketstatstable = CISCOIFEXTENSIONMIB.CieIfPacketStatsTable()
        self.cieifpacketstatstable.parent = self
        self._children_name_map["cieifpacketstatstable"] = "cieIfPacketStatsTable"

        self.cieifinterfacetable = CISCOIFEXTENSIONMIB.CieIfInterfaceTable()
        self.cieifinterfacetable.parent = self
        self._children_name_map["cieifinterfacetable"] = "cieIfInterfaceTable"

        self.cieifstatuslisttable = CISCOIFEXTENSIONMIB.CieIfStatusListTable()
        self.cieifstatuslisttable.parent = self
        self._children_name_map["cieifstatuslisttable"] = "cieIfStatusListTable"

        self.cieifvlstatstable = CISCOIFEXTENSIONMIB.CieIfVlStatsTable()
        self.cieifvlstatstable.parent = self
        self._children_name_map["cieifvlstatstable"] = "cieIfVlStatsTable"

        self.cieifindexpersistencetable = CISCOIFEXTENSIONMIB.CieIfIndexPersistenceTable()
        self.cieifindexpersistencetable.parent = self
        self._children_name_map["cieifindexpersistencetable"] = "cieIfIndexPersistenceTable"

        self.cieifdot1qcustomethertypetable = CISCOIFEXTENSIONMIB.CieIfDot1qCustomEtherTypeTable()
        self.cieifdot1qcustomethertypetable.parent = self
        self._children_name_map["cieifdot1qcustomethertypetable"] = "cieIfDot1qCustomEtherTypeTable"

        self.cieifutiltable = CISCOIFEXTENSIONMIB.CieIfUtilTable()
        self.cieifutiltable.parent = self
        self._children_name_map["cieifutiltable"] = "cieIfUtilTable"

        self.cieifdot1dbasemappingtable = CISCOIFEXTENSIONMIB.CieIfDot1dBaseMappingTable()
        self.cieifdot1dbasemappingtable.parent = self
        self._children_name_map["cieifdot1dbasemappingtable"] = "cieIfDot1dBaseMappingTable"

        self.cieifnamemappingtable = CISCOIFEXTENSIONMIB.CieIfNameMappingTable()
        self.cieifnamemappingtable.parent = self
        self._children_name_map["cieifnamemappingtable"] = "cieIfNameMappingTable"
        self._segment_path = lambda: "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCOIFEXTENSIONMIB, [], name, value)


    class CiscoIfExtSystemConfig(Entity):
        """
        
        
        .. attribute:: ciesystemmtu
        
        	Global system MTU in octets. This object specifies the MTU on all interfaces. However, the value specified by cieIfMtu takes precedence for an interface, which means that the interface's MTU uses the value specified by cieIfMtu, if it is configured
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        	**config**\: False
        
        .. attribute:: cielinkupdownenable
        
        	Indicates whether cieLinkUp/cieLinkDown or standard mib\-II defined linkUp/Down or both, notifications should be generated for the interfaces in the system.  'standard'  \- only generate standard defined               mib\-II linkUp/linkDown notification               if 'ifLinkUpDownTrapEnable' for                the interface is 'enabled'. 'cisco'     \- only generate cieLinkUp/cieLinkDown               notifications for an interface if               the 'ifLinkUpDownTrapEnable' for the               interface is 'enabled'.  If both bits are selected then linkUp/linkDown and cieLinkUp/cieLinkDown are both generated for an  interface if the 'ifLinkUpDownTrapEnable' for the interface is 'enabled'
        	**type**\:  :py:class:`CieLinkUpDownEnable <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.CiscoIfExtSystemConfig.CieLinkUpDownEnable>`
        
        	**config**\: False
        
        	**status**\: deprecated
        
        .. attribute:: ciestandardlinkupdownvarbinds
        
        	Indicates whether to send the extra varbinds in addition to the varbinds defined  in linkUp/linkDown notifications.  'standard'   \- only send the varbinds defined in                the standard linkUp/linkDown                notification.   'additional' \- send the extra varbinds in addition                 to the defined ones. 'other'      \- any other config not covered by the above.                This value is read\-only
        	**type**\:  :py:class:`CieStandardLinkUpDownVarbinds <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.CiscoIfExtSystemConfig.CieStandardLinkUpDownVarbinds>`
        
        	**config**\: False
        
        	**status**\: deprecated
        
        .. attribute:: cieifindexpersistence
        
        	This object specifies whether ifIndex values persist across reinitialization of the device.  ifIndex persistence means that the mapping between the ifDescr object values and the ifIndex object values will be retained across reboots.  Applications such as device inventory, billing, and fault detection depend on the maintenance of the correspondence between particular ifIndex values and their interfaces. During reboot or insertion of a new card, the data to correlate the interfaces to the ifIndex may become invalid in absence of ifIndex persistence feature.  ifIndex persistence for an interface ensures ifIndex value for the interface will remain the same after a system reboot. Hence, this feature allows users to avoid the workarounds required for consistent interface identification across reinitialization.  Due to change in syntax, this object is deprecated by cieIfIndexGlobalPersistence
        	**type**\: bool
        
        	**config**\: False
        
        	**status**\: deprecated
        
        .. attribute:: ciedelayedlinkupdownnotifenable
        
        	This object specifies whether the system generates a cieDelayedLinkUpDownNotif notification
        	**type**\: bool
        
        	**config**\: False
        
        .. attribute:: ciedelayedlinkupdownnotifdelay
        
        	This object specifies the interval of time an interface's operational status must remain stable following a transition before the system will generate a cieDelayedLinkUpDownNotif
        	**type**\: int
        
        	**range:** 1..60
        
        	**config**\: False
        
        	**units**\: minutes
        
        .. attribute:: cieifindexglobalpersistence
        
        	This object specifies whether ifIndex values persist across reinitialization of the device.  ifIndex persistence means that the mapping between the ifDescr object values and the ifIndex object values will be retained across reboots.  Applications such as device inventory, billing, and fault detection depend on the maintenance of the correspondence between particular ifIndex values and their interfaces. During reboot or insertion of a new card, the data to correlate the interfaces to the ifIndex may become invalid in absence of ifIndex persistence feature.  ifIndex persistence for an interface ensures ifIndex value for the interface will remain the same after a system reboot. Hence, this feature allows users to avoid the workarounds required for consistent interface identification across reinitialization.  The allowed values for this object are either enable or disable. global value is not allowed
        	**type**\:  :py:class:`IfIndexPersistenceState <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.IfIndexPersistenceState>`
        
        	**config**\: False
        
        .. attribute:: cielinkupdownconfig
        
        	This object specifies whether standard mib\-II defined linkUp/ linkDown, extended linkUp/linkDown (with extra varbinds in addition to the varbinds defined in linkUp/linkDown) or cieLinkUp/cieLinkDown notifications should be generated for the interfaces in the system.  'standardLinkUp'     \- generate standard defined mib\-II                         linkUp notification if                         'ifLinkUpDownTrapEnable' for the                         interface is 'enabled'. 'standardLinkDown'   \- generate standard defined mib\-II                         linkDown notification if                         'ifLinkUpDownTrapEnable' for the                         interface is 'enabled'.   'additionalLinkUp'   \- generate linkUp notification with                        additional varbinds if                         'ifLinkUpDownTrapEnable' for the                         interface is 'enabled'.   'additionalLinkDown' \- generate linkDown notification with                        additional varbinds if                         'ifLinkUpDownTrapEnable' for the                         interface is 'enabled'. 'ciscoLinkUp'        \- generate cieLinkUp notification                        if the 'ifLinkUpDownTrapEnable' for the                        interface is 'enabled'. 'ciscoLinkDown'      \- generate cieLinkDown notification                        if the 'ifLinkUpDownTrapEnable' for the                        interface is 'enabled'.  If multiple bits are set then multiple notifications will be generated for an interface if the 'ifLinkUpDownTrapEnable'  for the interface is 'enabled'
        	**type**\:  :py:class:`CieLinkUpDownConfig <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.CiscoIfExtSystemConfig.CieLinkUpDownConfig>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-IF-EXTENSION-MIB'
        _revision = '2013-03-13'

        def __init__(self):
            super(CISCOIFEXTENSIONMIB.CiscoIfExtSystemConfig, self).__init__()

            self.yang_name = "ciscoIfExtSystemConfig"
            self.yang_parent_name = "CISCO-IF-EXTENSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ciesystemmtu', (YLeaf(YType.int32, 'cieSystemMtu'), ['int'])),
                ('cielinkupdownenable', (YLeaf(YType.bits, 'cieLinkUpDownEnable'), ['Bits'])),
                ('ciestandardlinkupdownvarbinds', (YLeaf(YType.enumeration, 'cieStandardLinkUpDownVarbinds'), [('ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB', 'CISCOIFEXTENSIONMIB', 'CiscoIfExtSystemConfig.CieStandardLinkUpDownVarbinds')])),
                ('cieifindexpersistence', (YLeaf(YType.boolean, 'cieIfIndexPersistence'), ['bool'])),
                ('ciedelayedlinkupdownnotifenable', (YLeaf(YType.boolean, 'cieDelayedLinkUpDownNotifEnable'), ['bool'])),
                ('ciedelayedlinkupdownnotifdelay', (YLeaf(YType.uint32, 'cieDelayedLinkUpDownNotifDelay'), ['int'])),
                ('cieifindexglobalpersistence', (YLeaf(YType.enumeration, 'cieIfIndexGlobalPersistence'), [('ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB', 'IfIndexPersistenceState', '')])),
                ('cielinkupdownconfig', (YLeaf(YType.bits, 'cieLinkUpDownConfig'), ['Bits'])),
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
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIFEXTENSIONMIB.CiscoIfExtSystemConfig, ['ciesystemmtu', 'cielinkupdownenable', 'ciestandardlinkupdownvarbinds', 'cieifindexpersistence', 'ciedelayedlinkupdownnotifenable', 'ciedelayedlinkupdownnotifdelay', 'cieifindexglobalpersistence', 'cielinkupdownconfig'], name, value)

        class CieStandardLinkUpDownVarbinds(Enum):
            """
            CieStandardLinkUpDownVarbinds (Enum Class)

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




    class CieIfPacketStatsTable(Entity):
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
        	**type**\: list of  		 :py:class:`CieIfPacketStatsEntry <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.CieIfPacketStatsTable.CieIfPacketStatsEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-IF-EXTENSION-MIB'
        _revision = '2013-03-13'

        def __init__(self):
            super(CISCOIFEXTENSIONMIB.CieIfPacketStatsTable, self).__init__()

            self.yang_name = "cieIfPacketStatsTable"
            self.yang_parent_name = "CISCO-IF-EXTENSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cieIfPacketStatsEntry", ("cieifpacketstatsentry", CISCOIFEXTENSIONMIB.CieIfPacketStatsTable.CieIfPacketStatsEntry))])
            self._leafs = OrderedDict()

            self.cieifpacketstatsentry = YList(self)
            self._segment_path = lambda: "cieIfPacketStatsTable"
            self._absolute_path = lambda: "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIFEXTENSIONMIB.CieIfPacketStatsTable, [], name, value)


        class CieIfPacketStatsEntry(Entity):
            """
            An entry into the cieIfPacketStatsTable.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: cieiflastintime
            
            	This object represents the elapsed time in milliseconds since last protocol input  packet was received.  Discontinuities in the value of this variable can occur at re\-initialization of the management system, and at other times as  indicated by the values of  cieIfPacketDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: milliseconds
            
            .. attribute:: cieiflastouttime
            
            	This object represents the elapsed time in milliseconds since last protocol  output  packet was transmitted.  Discontinuities in the value of this variable can occur at re\-initialization of the management system, and at other times as  indicated by the values of  cieIfPacketDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: milliseconds
            
            .. attribute:: cieiflastouthangtime
            
            	This object represents the elapsed time in milliseconds since last protocol    output packet could not be successfully transmitted.  Discontinuities in the value of this variable can occur at re\-initialization of the management system, and at other times as  indicated by the values of  cieIfPacketDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: milliseconds
            
            .. attribute:: cieifinruntserrs
            
            	The number of packets input on a particular physical interface which were dropped as they were smaller than the minimum allowable  physical media limit.  Discontinuities in the value of this variable can occur at re\-initialization of the management system, and at other times as  indicated by the values of  cieIfPacketDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cieifingiantserrs
            
            	The number of input packets on a particular physical interface which were dropped as  they were larger than the ifMtu (largest  permitted  size of a packet which can be  sent/received on an interface).  Discontinuities in the value of this variable can occur at re\-initialization of the management system, and at other times as  indicated by the values of  cieIfPacketDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cieifinframingerrs
            
            	The number of input packets on a physical interface which were misaligned or had framing errors. This happens when the  format of the incoming packet on a physical interface is incorrect.  Discontinuities in the value of this variable can occur at re\-initialization of the management system, and at other times as  indicated by the values of  cieIfPacketDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cieifinoverrunerrs
            
            	The number of input packets which arrived on a particular physical interface which  were too quick for the hardware to receive and hence the receiver ran out of buffers.  Discontinuities in the value of this variable can occur at re\-initialization of the management system, and at other times as  indicated by the values of  cieIfPacketDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cieifinignored
            
            	The number of input packets which were simply ignored by this physical interface due to  insufficient resources to handle the incoming packets.  For example, this could indicate that the input receive buffers are not available or that the receiver lost a packet.  Discontinuities in the value of this variable can occur at re\-initialization of the management system, and at other times as  indicated by the values of  cieIfPacketDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cieifinaborterrs
            
            	Number of input packets which were dropped because the receiver aborted.  Examples of this could be when an abort sequence aborted the input frame or when there is a collision in an ethernet segment.  Discontinuities in the value of this variable can occur at re\-initialization of the management system, and at other times as  indicated by the values of  cieIfPacketDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cieifinputqueuedrops
            
            	The number of input packets which were dropped.  Some reasons why this object could be  incremented are\:  o  Input queue is full. o  Errors at the receiver hardware     while receiving the packet.  Discontinuities in the value of this variable can occur at re\-initialization of the management system, and at other times as  indicated by the values of  cieIfPacketDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cieifoutputqueuedrops
            
            	This object indicates the  number of output packets dropped by the interface even though no error had been detected to prevent them being transmitted.   The packet could be dropped for many reasons, which could range from the interface being down to errors in the format of the packet.  Discontinuities in the value of this variable can occur at re\-initialization of the management system, and at other times as  indicated by the values of  cieIfPacketDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cieifpacketdiscontinuitytime
            
            	The value of sysUpTime on the most recent occasion at which this interface's  counters suffered a discontinuity.   If no such discontinuities have occurred  since the last re\-initialization of the  local management subsystem, then this  object contains a value of zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-IF-EXTENSION-MIB'
            _revision = '2013-03-13'

            def __init__(self):
                super(CISCOIFEXTENSIONMIB.CieIfPacketStatsTable.CieIfPacketStatsEntry, self).__init__()

                self.yang_name = "cieIfPacketStatsEntry"
                self.yang_parent_name = "cieIfPacketStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('cieiflastintime', (YLeaf(YType.uint32, 'cieIfLastInTime'), ['int'])),
                    ('cieiflastouttime', (YLeaf(YType.uint32, 'cieIfLastOutTime'), ['int'])),
                    ('cieiflastouthangtime', (YLeaf(YType.uint32, 'cieIfLastOutHangTime'), ['int'])),
                    ('cieifinruntserrs', (YLeaf(YType.uint32, 'cieIfInRuntsErrs'), ['int'])),
                    ('cieifingiantserrs', (YLeaf(YType.uint32, 'cieIfInGiantsErrs'), ['int'])),
                    ('cieifinframingerrs', (YLeaf(YType.uint32, 'cieIfInFramingErrs'), ['int'])),
                    ('cieifinoverrunerrs', (YLeaf(YType.uint32, 'cieIfInOverrunErrs'), ['int'])),
                    ('cieifinignored', (YLeaf(YType.uint32, 'cieIfInIgnored'), ['int'])),
                    ('cieifinaborterrs', (YLeaf(YType.uint32, 'cieIfInAbortErrs'), ['int'])),
                    ('cieifinputqueuedrops', (YLeaf(YType.uint32, 'cieIfInputQueueDrops'), ['int'])),
                    ('cieifoutputqueuedrops', (YLeaf(YType.uint32, 'cieIfOutputQueueDrops'), ['int'])),
                    ('cieifpacketdiscontinuitytime', (YLeaf(YType.uint32, 'cieIfPacketDiscontinuityTime'), ['int'])),
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
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIFEXTENSIONMIB.CieIfPacketStatsTable.CieIfPacketStatsEntry, ['ifindex', 'cieiflastintime', 'cieiflastouttime', 'cieiflastouthangtime', 'cieifinruntserrs', 'cieifingiantserrs', 'cieifinframingerrs', 'cieifinoverrunerrs', 'cieifinignored', 'cieifinaborterrs', 'cieifinputqueuedrops', 'cieifoutputqueuedrops', 'cieifpacketdiscontinuitytime'], name, value)




    class CieIfInterfaceTable(Entity):
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
        	**type**\: list of  		 :py:class:`CieIfInterfaceEntry <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.CieIfInterfaceTable.CieIfInterfaceEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-IF-EXTENSION-MIB'
        _revision = '2013-03-13'

        def __init__(self):
            super(CISCOIFEXTENSIONMIB.CieIfInterfaceTable, self).__init__()

            self.yang_name = "cieIfInterfaceTable"
            self.yang_parent_name = "CISCO-IF-EXTENSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cieIfInterfaceEntry", ("cieifinterfaceentry", CISCOIFEXTENSIONMIB.CieIfInterfaceTable.CieIfInterfaceEntry))])
            self._leafs = OrderedDict()

            self.cieifinterfaceentry = YList(self)
            self._segment_path = lambda: "cieIfInterfaceTable"
            self._absolute_path = lambda: "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIFEXTENSIONMIB.CieIfInterfaceTable, [], name, value)


        class CieIfInterfaceEntry(Entity):
            """
            An entry into the cieIfInterfaceTable.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: cieifresetcount
            
            	The number of times the interface was internally reset and brought up.  Some of the actions which can cause this counter to increment are \:  o  Bringing an interface up using the     interface CLI command.  o  Clearing the interface with the exec    CLI command.  o  Bringing the interface up via SNMP.  Discontinuities in the value of this variable can occur at re\-initialization of the management system, and at other times as  indicated by the values of  cieIfInterfaceDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cieifkeepaliveenabled
            
            	A keepalive is a small, layer\-2 message that is transmitted by a network device  to let directly\-connected network devices know of its presence.  This object returns 'true' if keepalives are enabled on this interface. If keepalives are not enabled, 'false' is returned.  Setting this object to TRUE or FALSE enables or disables (respectively) keepalive on this  interface
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cieifstatechangereason
            
            	This object displays a human\-readable textual string which describes the  cause of the last state change of the  interface.  Examples of the values this object can take are\:  o  'Lost Carrier' o  'administratively down' o  'up' o  'down'
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: cieifcarriertransitioncount
            
            	Number of times interface saw the carrier signal transition.  For example, if a T1 line is unplugged,  then framer will detect the loss of signal  (LOS) on the line  and will count it as a transition.  Discontinuities in the value of this variable can occur at re\-initialization of the management system, and at other times as  indicated by the values of  cieIfInterfaceDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cieifinterfacediscontinuitytime
            
            	The value of sysUpTime on the most recent occasion at which this interface's  counters  suffered  a discontinuity.   If no such discontinuities have occurred  since the last re\-initialization of the  local management subsystem, then this  object contains a value of zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cieifdhcpmode
            
            	The DHCP mode configured by the administrator. If 'true' the DHCP is enabled. In which case an IP address is requested in DHCP. This is in addition to any that are  configured by the administrator in 'ciiIPAddressTable' or 'ciiIPIfAddressTable' in CISCO\-IP\-IF\-MIB. If 'false' the DHCP is disabled. In which case all IP addresses are configured by the administrator in 'ciiIPAddressTable' or  'ciiIPIfAddressTable'. For interfaces, for which DHCP cannot be or is not supported, then this object has the value 'false'
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cieifmtu
            
            	The MTU configured by the administrator. This object is exactly same as 'ifMtu' in  ifTable from IF\-MIB for the same ifIndex value , except that it is configurable by the administrator. For more description of this object refer to 'ifMtu' in IF\-MIB
            	**type**\: int
            
            	**range:** 40..2147483647
            
            	**config**\: False
            
            .. attribute:: cieifcontextname
            
            	The ContextName denotes the interface 'context' and is used to logically separate the MIB management. RFC 2571 and RFC 2737 describe this approach. When the agent supports a different SNMP  context, as detailed in RFC 2571 and  RFC 2737, for different interfaces, then the value of this object specifies the context name used for this interface
            	**type**\: str
            
            	**length:** 0..32
            
            	**config**\: False
            
            .. attribute:: cieifoperstatuscause
            
            	This object represents the detailed operational cause reason for the current  operational state of the interface.  The current operational state of the interface  is given by the 'ifOperStatus' defined  in IF\-MIB.   The corresponding instance of  'cieIfOperStatusCauseDescr' must be used to  get the information about the operational  cause value mentioned in this object.  For interfaces whose 'ifOperStatus' is 'down'  the objects 'cieIfOperStatusCause' and  'cieIfOperStatusCauseDescr' together provides  the information about the operational cause  reason and the description of the cause.   The value of this object will be 'none' for all the 'ifOperStatus' values except for  'down'. Its value will be one status cause  defined in the 'IfOperStatusReason' textual  convention if 'ifOperStatus' is 'down'.   The value of this object will be 'other'  if the operational status cause is not one  defined in 'IfOperStatusReason'
            	**type**\:  :py:class:`IfOperStatusReason <ydk.models.cisco_ios_xe.CISCO_TC.IfOperStatusReason>`
            
            	**config**\: False
            
            .. attribute:: cieifoperstatuscausedescr
            
            	The description for the cause of current operational state of the interface, given  by the object 'cieIfOperStatusCause'.  For an interface whose 'ifOperStatus' is not 'down' the value of this object will be  'none'
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: cieifspeedreceive
            
            	An estimate of the interface's current receive bandwidth in bits per second.  This object is provided for interface with asymmetric interface speeds like ADSL and should be used in conjunction with ifSpeed object.  For interfaces which do not vary in bandwidth or for those where no accurate estimation can be made, this object should contain the nominal bandwidth. If the bandwidth of the interface is greater than the maximum value reportable by this object then this object should report its maximum value (4,294,967,295) and ifHighSpeed must be used to report the interace's speed.  For a sub\-layer which has no concept of bandwidth, this object should be zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cieifhighspeedreceive
            
            	An estimate of the interface's current receive bandwidth in units of 1,000,000 bits per second.  If this object reports a value of `n' then the speed of the interface is somewhere in the range of `n\-500,000' to `n+499,999'.  For interfaces which do not vary in bandwidth or for those where no accurate estimation can be made, this object should contain the nominal bandwidth.  For a sub\-layer which has no concept of bandwidth, this object should be zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cieifowner
            
            	This data type is used to model an administratively assigned name of the current owner of the interface resource. This  information is taken from the NVT ASCII character set.  It is  suggested that this name contain one or more of the following\:  SnmpEngineID, IP address, management station name, network  manager's name, location, or phone number. SNMP access control is articulated entirely in terms of the  contents of MIB views; access to a particular SNMP object  instance depends only upon its presence or absence in a  particular MIB view and never upon its value or the value of  related object instances. Thus, this object affords resolution of resource contention  only among cooperating managers; this object realizes no access control function with respect to uncooperative parties
            	**type**\: str
            
            	**length:** 0..80
            
            	**config**\: False
            
            .. attribute:: cieifsharedconfig
            
            	This object indicates the current configuration of interface sharing on the given interface.  'notApplicable' \- the interface sharing configuration on              this interface is not applicable.  'ownerDedicated' \- the interface is in the dedicated mode             to the binding physical interface. 'ownerShared' \- the interface is shared amongst virtual switches          and this interface physically belongs to a its           virtual switch.   'sharedOnly' \- the interface is in purely shared mode
            	**type**\:  :py:class:`CieIfSharedConfig <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.CieIfInterfaceTable.CieIfInterfaceEntry.CieIfSharedConfig>`
            
            	**config**\: False
            
            .. attribute:: cieifspeedgroupconfig
            
            	This object specifies the current speed group configuration on the given interface.  'notApplicable' \- the interface speed group configuration on             this interface is not applicable. It is a              read\-only value. '10G' \- the interface speed group configuration on             this interface as 10G. '1G\-2G\-4G\-8G' \- the interface speed group configuration              on this interface as 1G\-2G\-4G\-8G. '2G\-4G\-8G\-16G' \- the interface speed group configuration              on this interface as 2G\-4G\-8G\-16G
            	**type**\:  :py:class:`CieIfSpeedGroupConfig <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.CieIfInterfaceTable.CieIfInterfaceEntry.CieIfSpeedGroupConfig>`
            
            	**config**\: False
            
            .. attribute:: cieiftransceiverfrequencyconfig
            
            	This object specifies the current transceiver frequency configuration on the given interface.  'notApplicable' \- the interface transceiver frequency  				  configuration on this interface  				  is not applicable. It is a read\-only value. 'FibreChannel' \- the interface transceiver frequency 				 configuration on this interface as                   Fibre Channel. 'Ethernet'	  \-  the interface transceiver frequency on 				 this interface as Ethernet
            	**type**\:  :py:class:`CieIfTransceiverFrequencyConfig <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.CieIfInterfaceTable.CieIfInterfaceEntry.CieIfTransceiverFrequencyConfig>`
            
            	**config**\: False
            
            .. attribute:: cieiffillpatternconfig
            
            	This object specifies the current switchport fill pattern configuration on the given interface.  'arbff8G' \- the inter frame gap fill pattern is 			ARBFF for 8G speed. 'idle8G' \- the inter frame gap fill pattern is 		   IDLE for 8G speed
            	**type**\:  :py:class:`CieIfFillPatternConfig <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.CieIfInterfaceTable.CieIfInterfaceEntry.CieIfFillPatternConfig>`
            
            	**config**\: False
            
            .. attribute:: cieifignorebiterrorsconfig
            
            	This object specifies the current switchport biterrors configuration on the given interface.  If 'true(1)' the ignore bit errors is enabled.In which case the interface ignores bit errors. If 'false(2)' the ignore bit errors is disabled. In which  case the interface acts on the bit errors.  For interfaces, for which bit errors  is not supported, then this object has the value 'true(1)'
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cieifignoreinterruptthresholdconfig
            
            	This object specifies the current interrupt threshold configuration on the given interface.  'If 'true(1)' the ignore interrupt thresholds is enabled. In which case the interface ignores interrupt thresholds. If 'false(2)' the ignore interrupt thresholds is disabled. In which case the interface acts on the interrupt  thresholds.  For interfaces, for which interrupt thresholds  is not supported, then this object has the  value 'true(1)'
            	**type**\: bool
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-IF-EXTENSION-MIB'
            _revision = '2013-03-13'

            def __init__(self):
                super(CISCOIFEXTENSIONMIB.CieIfInterfaceTable.CieIfInterfaceEntry, self).__init__()

                self.yang_name = "cieIfInterfaceEntry"
                self.yang_parent_name = "cieIfInterfaceTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('cieifresetcount', (YLeaf(YType.uint32, 'cieIfResetCount'), ['int'])),
                    ('cieifkeepaliveenabled', (YLeaf(YType.boolean, 'cieIfKeepAliveEnabled'), ['bool'])),
                    ('cieifstatechangereason', (YLeaf(YType.str, 'cieIfStateChangeReason'), ['str'])),
                    ('cieifcarriertransitioncount', (YLeaf(YType.uint32, 'cieIfCarrierTransitionCount'), ['int'])),
                    ('cieifinterfacediscontinuitytime', (YLeaf(YType.uint32, 'cieIfInterfaceDiscontinuityTime'), ['int'])),
                    ('cieifdhcpmode', (YLeaf(YType.boolean, 'cieIfDhcpMode'), ['bool'])),
                    ('cieifmtu', (YLeaf(YType.int32, 'cieIfMtu'), ['int'])),
                    ('cieifcontextname', (YLeaf(YType.str, 'cieIfContextName'), ['str'])),
                    ('cieifoperstatuscause', (YLeaf(YType.enumeration, 'cieIfOperStatusCause'), [('ydk.models.cisco_ios_xe.CISCO_TC', 'IfOperStatusReason', '')])),
                    ('cieifoperstatuscausedescr', (YLeaf(YType.str, 'cieIfOperStatusCauseDescr'), ['str'])),
                    ('cieifspeedreceive', (YLeaf(YType.uint32, 'cieIfSpeedReceive'), ['int'])),
                    ('cieifhighspeedreceive', (YLeaf(YType.uint32, 'cieIfHighSpeedReceive'), ['int'])),
                    ('cieifowner', (YLeaf(YType.str, 'cieIfOwner'), ['str'])),
                    ('cieifsharedconfig', (YLeaf(YType.enumeration, 'cieIfSharedConfig'), [('ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB', 'CISCOIFEXTENSIONMIB', 'CieIfInterfaceTable.CieIfInterfaceEntry.CieIfSharedConfig')])),
                    ('cieifspeedgroupconfig', (YLeaf(YType.enumeration, 'cieIfSpeedGroupConfig'), [('ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB', 'CISCOIFEXTENSIONMIB', 'CieIfInterfaceTable.CieIfInterfaceEntry.CieIfSpeedGroupConfig')])),
                    ('cieiftransceiverfrequencyconfig', (YLeaf(YType.enumeration, 'cieIfTransceiverFrequencyConfig'), [('ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB', 'CISCOIFEXTENSIONMIB', 'CieIfInterfaceTable.CieIfInterfaceEntry.CieIfTransceiverFrequencyConfig')])),
                    ('cieiffillpatternconfig', (YLeaf(YType.enumeration, 'cieIfFillPatternConfig'), [('ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB', 'CISCOIFEXTENSIONMIB', 'CieIfInterfaceTable.CieIfInterfaceEntry.CieIfFillPatternConfig')])),
                    ('cieifignorebiterrorsconfig', (YLeaf(YType.boolean, 'cieIfIgnoreBitErrorsConfig'), ['bool'])),
                    ('cieifignoreinterruptthresholdconfig', (YLeaf(YType.boolean, 'cieIfIgnoreInterruptThresholdConfig'), ['bool'])),
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
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIFEXTENSIONMIB.CieIfInterfaceTable.CieIfInterfaceEntry, ['ifindex', 'cieifresetcount', 'cieifkeepaliveenabled', 'cieifstatechangereason', 'cieifcarriertransitioncount', 'cieifinterfacediscontinuitytime', 'cieifdhcpmode', 'cieifmtu', 'cieifcontextname', 'cieifoperstatuscause', 'cieifoperstatuscausedescr', 'cieifspeedreceive', 'cieifhighspeedreceive', 'cieifowner', 'cieifsharedconfig', 'cieifspeedgroupconfig', 'cieiftransceiverfrequencyconfig', 'cieiffillpatternconfig', 'cieifignorebiterrorsconfig', 'cieifignoreinterruptthresholdconfig'], name, value)

            class CieIfFillPatternConfig(Enum):
                """
                CieIfFillPatternConfig (Enum Class)

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


            class CieIfSharedConfig(Enum):
                """
                CieIfSharedConfig (Enum Class)

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


            class CieIfSpeedGroupConfig(Enum):
                """
                CieIfSpeedGroupConfig (Enum Class)

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


            class CieIfTransceiverFrequencyConfig(Enum):
                """
                CieIfTransceiverFrequencyConfig (Enum Class)

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





    class CieIfStatusListTable(Entity):
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
        	**type**\: list of  		 :py:class:`CieIfStatusListEntry <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.CieIfStatusListTable.CieIfStatusListEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-IF-EXTENSION-MIB'
        _revision = '2013-03-13'

        def __init__(self):
            super(CISCOIFEXTENSIONMIB.CieIfStatusListTable, self).__init__()

            self.yang_name = "cieIfStatusListTable"
            self.yang_parent_name = "CISCO-IF-EXTENSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cieIfStatusListEntry", ("cieifstatuslistentry", CISCOIFEXTENSIONMIB.CieIfStatusListTable.CieIfStatusListEntry))])
            self._leafs = OrderedDict()

            self.cieifstatuslistentry = YList(self)
            self._segment_path = lambda: "cieIfStatusListTable"
            self._absolute_path = lambda: "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIFEXTENSIONMIB.CieIfStatusListTable, [], name, value)


        class CieIfStatusListEntry(Entity):
            """
            Each entry represents the 'ifIndex',
            interface operational mode and interface 
            operational cause for a set of 64 interfaces 
            in a module.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.EntPhysicalTable.EntPhysicalEntry>`
            
            	**config**\: False
            
            .. attribute:: cieifstatuslistindex  (key)
            
            	An arbitrary integer value, greater than zero, which identifies a list of 64 interfaces within a module
            	**type**\: int
            
            	**range:** 1..33554432
            
            	**config**\: False
            
            .. attribute:: cieinterfacesindex
            
            	This object represents the 'ifIndex' for a set of 64 interfaces in the module
            	**type**\: str
            
            	**length:** 0..256
            
            	**config**\: False
            
            .. attribute:: cieinterfacesopermode
            
            	This object represents the operational mode for a set of 64 interfaces in the module
            	**type**\: str
            
            	**length:** 0..64
            
            	**config**\: False
            
            .. attribute:: cieinterfacesopercause
            
            	This object represents the operational status cause for a set of 64 interfaces in the  module
            	**type**\: str
            
            	**length:** 0..128
            
            	**config**\: False
            
            .. attribute:: cieinterfaceownershipbitmap
            
            	This object indicates the status for a set of 64 interfaces in a module regarding whether or not each interface is  administratively assigned a name of the current owner of the  interface resource as per cieIfOwner
            	**type**\: str
            
            	**length:** 0..8
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-IF-EXTENSION-MIB'
            _revision = '2013-03-13'

            def __init__(self):
                super(CISCOIFEXTENSIONMIB.CieIfStatusListTable.CieIfStatusListEntry, self).__init__()

                self.yang_name = "cieIfStatusListEntry"
                self.yang_parent_name = "cieIfStatusListTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','cieifstatuslistindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.str, 'entPhysicalIndex'), ['int'])),
                    ('cieifstatuslistindex', (YLeaf(YType.uint32, 'cieIfStatusListIndex'), ['int'])),
                    ('cieinterfacesindex', (YLeaf(YType.str, 'cieInterfacesIndex'), ['str'])),
                    ('cieinterfacesopermode', (YLeaf(YType.str, 'cieInterfacesOperMode'), ['str'])),
                    ('cieinterfacesopercause', (YLeaf(YType.str, 'cieInterfacesOperCause'), ['str'])),
                    ('cieinterfaceownershipbitmap', (YLeaf(YType.str, 'cieInterfaceOwnershipBitmap'), ['str'])),
                ])
                self.entphysicalindex = None
                self.cieifstatuslistindex = None
                self.cieinterfacesindex = None
                self.cieinterfacesopermode = None
                self.cieinterfacesopercause = None
                self.cieinterfaceownershipbitmap = None
                self._segment_path = lambda: "cieIfStatusListEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']" + "[cieIfStatusListIndex='" + str(self.cieifstatuslistindex) + "']"
                self._absolute_path = lambda: "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/cieIfStatusListTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIFEXTENSIONMIB.CieIfStatusListTable.CieIfStatusListEntry, ['entphysicalindex', 'cieifstatuslistindex', 'cieinterfacesindex', 'cieinterfacesopermode', 'cieinterfacesopercause', 'cieinterfaceownershipbitmap'], name, value)




    class CieIfVlStatsTable(Entity):
        """
        This table contains VL (Virtual Link) statistics
        for a capable interface.
        
        Objects defined in this table may be 
        applicable to physical interfaces only.
        
        .. attribute:: cieifvlstatsentry
        
        	Each row contains managed objects for Virtual Link statistics on interface capable of  providing this information
        	**type**\: list of  		 :py:class:`CieIfVlStatsEntry <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.CieIfVlStatsTable.CieIfVlStatsEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-IF-EXTENSION-MIB'
        _revision = '2013-03-13'

        def __init__(self):
            super(CISCOIFEXTENSIONMIB.CieIfVlStatsTable, self).__init__()

            self.yang_name = "cieIfVlStatsTable"
            self.yang_parent_name = "CISCO-IF-EXTENSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cieIfVlStatsEntry", ("cieifvlstatsentry", CISCOIFEXTENSIONMIB.CieIfVlStatsTable.CieIfVlStatsEntry))])
            self._leafs = OrderedDict()

            self.cieifvlstatsentry = YList(self)
            self._segment_path = lambda: "cieIfVlStatsTable"
            self._absolute_path = lambda: "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIFEXTENSIONMIB.CieIfVlStatsTable, [], name, value)


        class CieIfVlStatsEntry(Entity):
            """
            Each row contains managed objects for
            Virtual Link statistics on interface capable of 
            providing this information.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: cieifnodropvlinpkts
            
            	This object indicates the number of input packets on all No\-Drop Virtual Links belonged  to this interface
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: cieifnodropvlinoctets
            
            	This object indicates the number of input octets on all No\-Drop Virtual Links belonged  to this interface
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: cieifnodropvloutpkts
            
            	This object indicates the number of output packets on all No\-Drop Virtual Links belonged  to this interface
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: cieifnodropvloutoctets
            
            	This object indicates the number of output octets on all No\-Drop Virtual Links belonged  to this interface
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: cieifdropvlinpkts
            
            	This object indicates the number of input packets on all Drop Virtual Links belonged  to this interface
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: cieifdropvlinoctets
            
            	This object indicates the number of input octets on all Drop Virtual Links belonged  to this interface
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: cieifdropvloutpkts
            
            	This object indicates the number of output packets on all Drop Virtual Links belonged  to this interface
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: cieifdropvloutoctets
            
            	This object indicates the number of output octets on all Drop Virtual Links belonged  to this interface
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-IF-EXTENSION-MIB'
            _revision = '2013-03-13'

            def __init__(self):
                super(CISCOIFEXTENSIONMIB.CieIfVlStatsTable.CieIfVlStatsEntry, self).__init__()

                self.yang_name = "cieIfVlStatsEntry"
                self.yang_parent_name = "cieIfVlStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('cieifnodropvlinpkts', (YLeaf(YType.uint64, 'cieIfNoDropVlInPkts'), ['int'])),
                    ('cieifnodropvlinoctets', (YLeaf(YType.uint64, 'cieIfNoDropVlInOctets'), ['int'])),
                    ('cieifnodropvloutpkts', (YLeaf(YType.uint64, 'cieIfNoDropVlOutPkts'), ['int'])),
                    ('cieifnodropvloutoctets', (YLeaf(YType.uint64, 'cieIfNoDropVlOutOctets'), ['int'])),
                    ('cieifdropvlinpkts', (YLeaf(YType.uint64, 'cieIfDropVlInPkts'), ['int'])),
                    ('cieifdropvlinoctets', (YLeaf(YType.uint64, 'cieIfDropVlInOctets'), ['int'])),
                    ('cieifdropvloutpkts', (YLeaf(YType.uint64, 'cieIfDropVlOutPkts'), ['int'])),
                    ('cieifdropvloutoctets', (YLeaf(YType.uint64, 'cieIfDropVlOutOctets'), ['int'])),
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
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIFEXTENSIONMIB.CieIfVlStatsTable.CieIfVlStatsEntry, ['ifindex', 'cieifnodropvlinpkts', 'cieifnodropvlinoctets', 'cieifnodropvloutpkts', 'cieifnodropvloutoctets', 'cieifdropvlinpkts', 'cieifdropvlinoctets', 'cieifdropvloutpkts', 'cieifdropvloutoctets'], name, value)




    class CieIfIndexPersistenceTable(Entity):
        """
        This table lists configuration data relating to ifIndex
        persistence.
        
        This table has a sparse dependent relationship on the ifTable,
        containing a row for each ifEntry corresponding to an interface
        for which ifIndex persistence is supported.
        
        .. attribute:: cieifindexpersistenceentry
        
        	Each entry represents ifindex persistence configuration for an interface specified by ifIndex. Whenever an interface which supports ifindex persistence is created/destroyed in the ifTable, the corresponding ifindex persistence entry is created/destroyed respectively. Some of the interfaces may not support ifindex persistence, for example, a dynamic interface, such as a PPP connection or a IP subscriber interface
        	**type**\: list of  		 :py:class:`CieIfIndexPersistenceEntry <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.CieIfIndexPersistenceTable.CieIfIndexPersistenceEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-IF-EXTENSION-MIB'
        _revision = '2013-03-13'

        def __init__(self):
            super(CISCOIFEXTENSIONMIB.CieIfIndexPersistenceTable, self).__init__()

            self.yang_name = "cieIfIndexPersistenceTable"
            self.yang_parent_name = "CISCO-IF-EXTENSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cieIfIndexPersistenceEntry", ("cieifindexpersistenceentry", CISCOIFEXTENSIONMIB.CieIfIndexPersistenceTable.CieIfIndexPersistenceEntry))])
            self._leafs = OrderedDict()

            self.cieifindexpersistenceentry = YList(self)
            self._segment_path = lambda: "cieIfIndexPersistenceTable"
            self._absolute_path = lambda: "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIFEXTENSIONMIB.CieIfIndexPersistenceTable, [], name, value)


        class CieIfIndexPersistenceEntry(Entity):
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
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: cieifindexpersistenceenabled
            
            	This object specifies whether the interface's ifIndex value persist across reinitialization.  Due to change in syntax, this object is deprecated by cieIfIndexPersistenceControl
            	**type**\: bool
            
            	**config**\: False
            
            	**status**\: deprecated
            
            .. attribute:: cieifindexpersistencecontrol
            
            	This object specifies whether the interface's ifIndex value persist across reinitialization. In global state, the interface uses the global setting data for persistence i.e. cieIfIndexGlobalPersistence
            	**type**\:  :py:class:`IfIndexPersistenceState <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.IfIndexPersistenceState>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-IF-EXTENSION-MIB'
            _revision = '2013-03-13'

            def __init__(self):
                super(CISCOIFEXTENSIONMIB.CieIfIndexPersistenceTable.CieIfIndexPersistenceEntry, self).__init__()

                self.yang_name = "cieIfIndexPersistenceEntry"
                self.yang_parent_name = "cieIfIndexPersistenceTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('cieifindexpersistenceenabled', (YLeaf(YType.boolean, 'cieIfIndexPersistenceEnabled'), ['bool'])),
                    ('cieifindexpersistencecontrol', (YLeaf(YType.enumeration, 'cieIfIndexPersistenceControl'), [('ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB', 'IfIndexPersistenceState', '')])),
                ])
                self.ifindex = None
                self.cieifindexpersistenceenabled = None
                self.cieifindexpersistencecontrol = None
                self._segment_path = lambda: "cieIfIndexPersistenceEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/cieIfIndexPersistenceTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIFEXTENSIONMIB.CieIfIndexPersistenceTable.CieIfIndexPersistenceEntry, ['ifindex', 'cieifindexpersistenceenabled', 'cieifindexpersistencecontrol'], name, value)




    class CieIfDot1qCustomEtherTypeTable(Entity):
        """
        A list of the interfaces that support
        the 802.1q custom Ethertype feature.
        
        .. attribute:: cieifdot1qcustomethertypeentry
        
        	An entry containing the custom EtherType information for the interface.  Only interfaces with custom 802.1q ethertype control are listed in the  table
        	**type**\: list of  		 :py:class:`CieIfDot1qCustomEtherTypeEntry <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.CieIfDot1qCustomEtherTypeTable.CieIfDot1qCustomEtherTypeEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-IF-EXTENSION-MIB'
        _revision = '2013-03-13'

        def __init__(self):
            super(CISCOIFEXTENSIONMIB.CieIfDot1qCustomEtherTypeTable, self).__init__()

            self.yang_name = "cieIfDot1qCustomEtherTypeTable"
            self.yang_parent_name = "CISCO-IF-EXTENSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cieIfDot1qCustomEtherTypeEntry", ("cieifdot1qcustomethertypeentry", CISCOIFEXTENSIONMIB.CieIfDot1qCustomEtherTypeTable.CieIfDot1qCustomEtherTypeEntry))])
            self._leafs = OrderedDict()

            self.cieifdot1qcustomethertypeentry = YList(self)
            self._segment_path = lambda: "cieIfDot1qCustomEtherTypeTable"
            self._absolute_path = lambda: "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIFEXTENSIONMIB.CieIfDot1qCustomEtherTypeTable, [], name, value)


        class CieIfDot1qCustomEtherTypeEntry(Entity):
            """
            An entry containing the custom EtherType
            information for the interface.
            
            Only interfaces with custom 802.1q
            ethertype control are listed in the 
            table.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: cieifdot1qcustomadminethertype
            
            	The Dot1qEtherType allow administrator to select a non\-standard (other than 0x8100) 2\-byte ethertype for the interface to  interoperate with third party vendor's system that do not use the standard 0x8100 ethertype to identify 802.1q\-tagged frames.  The current administrative value of the  802.1q ethertype for the interface.  The administrative 802.1q ethertype value may  differ from the operational 802.1q ethertype value.  On some platforms, 802.1q ethertype may be assigned per group rather than per port. If multiple ports belong to a port group, the 802.1q ethertype assigned to any of the ports in such group will apply to all ports in the same group.  To configure non\-standard dot1q ethertype is only recommended when the Cisco device is connected to any third party vendor device. Also be advised that the custom ethertype value needs to be changed in the whole cloud of  Cisco device with the same custom ethertype  value if the third party device are separated  by number of Cisco device in the middle
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: cieifdot1qcustomoperethertype
            
            	The current operational value of the 802.1q ethertype for the interface
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-IF-EXTENSION-MIB'
            _revision = '2013-03-13'

            def __init__(self):
                super(CISCOIFEXTENSIONMIB.CieIfDot1qCustomEtherTypeTable.CieIfDot1qCustomEtherTypeEntry, self).__init__()

                self.yang_name = "cieIfDot1qCustomEtherTypeEntry"
                self.yang_parent_name = "cieIfDot1qCustomEtherTypeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('cieifdot1qcustomadminethertype', (YLeaf(YType.int32, 'cieIfDot1qCustomAdminEtherType'), ['int'])),
                    ('cieifdot1qcustomoperethertype', (YLeaf(YType.int32, 'cieIfDot1qCustomOperEtherType'), ['int'])),
                ])
                self.ifindex = None
                self.cieifdot1qcustomadminethertype = None
                self.cieifdot1qcustomoperethertype = None
                self._segment_path = lambda: "cieIfDot1qCustomEtherTypeEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/cieIfDot1qCustomEtherTypeTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIFEXTENSIONMIB.CieIfDot1qCustomEtherTypeTable.CieIfDot1qCustomEtherTypeEntry, ['ifindex', 'cieifdot1qcustomadminethertype', 'cieifdot1qcustomoperethertype'], name, value)




    class CieIfUtilTable(Entity):
        """
        This table contains the interface utilization
        rates for inbound and outbound traffic on an
        interface.
        
        .. attribute:: cieifutilentry
        
        	An entry containing utilization rates for the interface.  Every interface for which the  inbound and  outbound traffic information is available has a corresponding entry in this table
        	**type**\: list of  		 :py:class:`CieIfUtilEntry <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.CieIfUtilTable.CieIfUtilEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-IF-EXTENSION-MIB'
        _revision = '2013-03-13'

        def __init__(self):
            super(CISCOIFEXTENSIONMIB.CieIfUtilTable, self).__init__()

            self.yang_name = "cieIfUtilTable"
            self.yang_parent_name = "CISCO-IF-EXTENSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cieIfUtilEntry", ("cieifutilentry", CISCOIFEXTENSIONMIB.CieIfUtilTable.CieIfUtilEntry))])
            self._leafs = OrderedDict()

            self.cieifutilentry = YList(self)
            self._segment_path = lambda: "cieIfUtilTable"
            self._absolute_path = lambda: "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIFEXTENSIONMIB.CieIfUtilTable, [], name, value)


        class CieIfUtilEntry(Entity):
            """
            An entry containing utilization rates for the
            interface.
            
            Every interface for which the  inbound and 
            outbound traffic information is available
            has a corresponding entry in this table.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: cieifinpktrate
            
            	By default, this is the five minute exponentially\-decayed moving average of the inbound packet rate for this interface. However, if the corresponding instance of cieIfInterval is instantiated with a value which specifies an interval different from 5\-minutes, then cieIfInPktRate is the exponentially\-decayed moving average of inbound packet rate over this different time interval
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: packets per second
            
            .. attribute:: cieifinoctetrate
            
            	By default, this is the five minute exponentially\-decayed moving average of the inbound octet rate for this interface. However, if the corresponding instance of cieIfInterval is instantiated with a value which specifies an interval different from 5\-minutes, then cieIfInOctetRate is the exponentially\-decayed moving average of inbound octet rate over this different time interval
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: octets per second
            
            .. attribute:: cieifoutpktrate
            
            	By default, this is the five minute exponentially\-decayed moving average of the outbound packet rate for this interface. However, if the corresponding instance of cieIfInterval is instantiated with a value which specifies an interval different from 5\-minutes, then cieIfOutPktRate is the exponentially\-decayed moving average of outbound packet rate over this different time interval
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: packets per second
            
            .. attribute:: cieifoutoctetrate
            
            	By default, this is the five minute exponentially\-decayed moving average of the outbound octet rate for this interface. However, if the corresponding instance of cieIfInterval is instantiated with a value which specifies an interval different from 5\-minutes, then cieIfOutOctetRate is the exponentially\-decayed moving average of outbound octet rate over this different time interval
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: octets per second
            
            .. attribute:: cieifinterval
            
            	This object specifies the time interval over which the inbound and outbound traffic rates are calculated for this interface
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            	**units**\: seconds
            
            

            """

            _prefix = 'CISCO-IF-EXTENSION-MIB'
            _revision = '2013-03-13'

            def __init__(self):
                super(CISCOIFEXTENSIONMIB.CieIfUtilTable.CieIfUtilEntry, self).__init__()

                self.yang_name = "cieIfUtilEntry"
                self.yang_parent_name = "cieIfUtilTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('cieifinpktrate', (YLeaf(YType.uint64, 'cieIfInPktRate'), ['int'])),
                    ('cieifinoctetrate', (YLeaf(YType.uint64, 'cieIfInOctetRate'), ['int'])),
                    ('cieifoutpktrate', (YLeaf(YType.uint64, 'cieIfOutPktRate'), ['int'])),
                    ('cieifoutoctetrate', (YLeaf(YType.uint64, 'cieIfOutOctetRate'), ['int'])),
                    ('cieifinterval', (YLeaf(YType.uint32, 'cieIfInterval'), ['int'])),
                ])
                self.ifindex = None
                self.cieifinpktrate = None
                self.cieifinoctetrate = None
                self.cieifoutpktrate = None
                self.cieifoutoctetrate = None
                self.cieifinterval = None
                self._segment_path = lambda: "cieIfUtilEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/cieIfUtilTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIFEXTENSIONMIB.CieIfUtilTable.CieIfUtilEntry, ['ifindex', 'cieifinpktrate', 'cieifinoctetrate', 'cieifoutpktrate', 'cieifoutoctetrate', 'cieifinterval'], name, value)




    class CieIfDot1dBaseMappingTable(Entity):
        """
        This table contains the mappings of the
        ifIndex of an interface to its
        corresponding dot1dBasePort value.
        
        .. attribute:: cieifdot1dbasemappingentry
        
        	An entry containing the mapping between the ifIndex value of an interface and its corresponding dot1dBasePort value.  Every interface which has been assigned a dot1dBasePort value by the system has a corresponding entry in this table
        	**type**\: list of  		 :py:class:`CieIfDot1dBaseMappingEntry <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.CieIfDot1dBaseMappingTable.CieIfDot1dBaseMappingEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-IF-EXTENSION-MIB'
        _revision = '2013-03-13'

        def __init__(self):
            super(CISCOIFEXTENSIONMIB.CieIfDot1dBaseMappingTable, self).__init__()

            self.yang_name = "cieIfDot1dBaseMappingTable"
            self.yang_parent_name = "CISCO-IF-EXTENSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cieIfDot1dBaseMappingEntry", ("cieifdot1dbasemappingentry", CISCOIFEXTENSIONMIB.CieIfDot1dBaseMappingTable.CieIfDot1dBaseMappingEntry))])
            self._leafs = OrderedDict()

            self.cieifdot1dbasemappingentry = YList(self)
            self._segment_path = lambda: "cieIfDot1dBaseMappingTable"
            self._absolute_path = lambda: "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIFEXTENSIONMIB.CieIfDot1dBaseMappingTable, [], name, value)


        class CieIfDot1dBaseMappingEntry(Entity):
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
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: cieifdot1dbasemappingport
            
            	The dot1dBasePort value for this interface
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-IF-EXTENSION-MIB'
            _revision = '2013-03-13'

            def __init__(self):
                super(CISCOIFEXTENSIONMIB.CieIfDot1dBaseMappingTable.CieIfDot1dBaseMappingEntry, self).__init__()

                self.yang_name = "cieIfDot1dBaseMappingEntry"
                self.yang_parent_name = "cieIfDot1dBaseMappingTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('cieifdot1dbasemappingport', (YLeaf(YType.int32, 'cieIfDot1dBaseMappingPort'), ['int'])),
                ])
                self.ifindex = None
                self.cieifdot1dbasemappingport = None
                self._segment_path = lambda: "cieIfDot1dBaseMappingEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/cieIfDot1dBaseMappingTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIFEXTENSIONMIB.CieIfDot1dBaseMappingTable.CieIfDot1dBaseMappingEntry, ['ifindex', 'cieifdot1dbasemappingport'], name, value)




    class CieIfNameMappingTable(Entity):
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
        	**type**\: list of  		 :py:class:`CieIfNameMappingEntry <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CISCOIFEXTENSIONMIB.CieIfNameMappingTable.CieIfNameMappingEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-IF-EXTENSION-MIB'
        _revision = '2013-03-13'

        def __init__(self):
            super(CISCOIFEXTENSIONMIB.CieIfNameMappingTable, self).__init__()

            self.yang_name = "cieIfNameMappingTable"
            self.yang_parent_name = "CISCO-IF-EXTENSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cieIfNameMappingEntry", ("cieifnamemappingentry", CISCOIFEXTENSIONMIB.CieIfNameMappingTable.CieIfNameMappingEntry))])
            self._leafs = OrderedDict()

            self.cieifnamemappingentry = YList(self)
            self._segment_path = lambda: "cieIfNameMappingTable"
            self._absolute_path = lambda: "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIFEXTENSIONMIB.CieIfNameMappingTable, [], name, value)


        class CieIfNameMappingEntry(Entity):
            """
            An entry into the cieIfNameMappingTable.
            
            .. attribute:: cieifname  (key)
            
            	Represents an interface name mentioned in the 'ifName' object of this system
            	**type**\: str
            
            	**length:** 1..112
            
            	**config**\: False
            
            .. attribute:: cieifindex
            
            	This object represents the 'ifIndex' corresponding to the interface name mentioned in the 'cieIfName' object of this instance. If the 'ifName' mentioned in the 'cieIfName'  object of this instance corresponds to multiple 'ifIndex' values, then the value of this object is the numerically smallest of those multiple  'ifIndex' values
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-IF-EXTENSION-MIB'
            _revision = '2013-03-13'

            def __init__(self):
                super(CISCOIFEXTENSIONMIB.CieIfNameMappingTable.CieIfNameMappingEntry, self).__init__()

                self.yang_name = "cieIfNameMappingEntry"
                self.yang_parent_name = "cieIfNameMappingTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cieifname']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cieifname', (YLeaf(YType.str, 'cieIfName'), ['str'])),
                    ('cieifindex', (YLeaf(YType.int32, 'cieIfIndex'), ['int'])),
                ])
                self.cieifname = None
                self.cieifindex = None
                self._segment_path = lambda: "cieIfNameMappingEntry" + "[cieIfName='" + str(self.cieifname) + "']"
                self._absolute_path = lambda: "CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/cieIfNameMappingTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIFEXTENSIONMIB.CieIfNameMappingTable.CieIfNameMappingEntry, ['cieifname', 'cieifindex'], name, value)



    def clone_ptr(self):
        self._top_entity = CISCOIFEXTENSIONMIB()
        return self._top_entity




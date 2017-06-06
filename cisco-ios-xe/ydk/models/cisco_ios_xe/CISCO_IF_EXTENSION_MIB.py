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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class IfindexpersistencestateEnum(Enum):
    """
    IfindexpersistencestateEnum

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

    disable = 1

    enable = 2

    global_ = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_IF_EXTENSION_MIB as meta
        return meta._meta_table['IfindexpersistencestateEnum']



class CiscoIfExtensionMib(object):
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
        self.cieifdot1dbasemappingtable = CiscoIfExtensionMib.Cieifdot1Dbasemappingtable()
        self.cieifdot1dbasemappingtable.parent = self
        self.cieifdot1qcustomethertypetable = CiscoIfExtensionMib.Cieifdot1Qcustomethertypetable()
        self.cieifdot1qcustomethertypetable.parent = self
        self.cieifindexpersistencetable = CiscoIfExtensionMib.Cieifindexpersistencetable()
        self.cieifindexpersistencetable.parent = self
        self.cieifinterfacetable = CiscoIfExtensionMib.Cieifinterfacetable()
        self.cieifinterfacetable.parent = self
        self.cieifnamemappingtable = CiscoIfExtensionMib.Cieifnamemappingtable()
        self.cieifnamemappingtable.parent = self
        self.cieifpacketstatstable = CiscoIfExtensionMib.Cieifpacketstatstable()
        self.cieifpacketstatstable.parent = self
        self.cieifstatuslisttable = CiscoIfExtensionMib.Cieifstatuslisttable()
        self.cieifstatuslisttable.parent = self
        self.cieifutiltable = CiscoIfExtensionMib.Cieifutiltable()
        self.cieifutiltable.parent = self
        self.cieifvlstatstable = CiscoIfExtensionMib.Cieifvlstatstable()
        self.cieifvlstatstable.parent = self
        self.ciscoifextsystemconfig = CiscoIfExtensionMib.Ciscoifextsystemconfig()
        self.ciscoifextsystemconfig.parent = self


    class Ciscoifextsystemconfig(object):
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
        	**type**\:   :py:class:`IfindexpersistencestateEnum <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.IfindexpersistencestateEnum>`
        
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
        	**type**\:   :py:class:`CiestandardlinkupdownvarbindsEnum <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CiscoIfExtensionMib.Ciscoifextsystemconfig.CiestandardlinkupdownvarbindsEnum>`
        
        	**status**\: deprecated
        
        .. attribute:: ciesystemmtu
        
        	Global system MTU in octets. This object specifies the MTU on all interfaces. However, the value specified by cieIfMtu takes precedence for an interface, which means that the interface's MTU uses the value specified by cieIfMtu, if it is configured
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        

        """

        _prefix = 'CISCO-IF-EXTENSION-MIB'
        _revision = '2013-03-13'

        def __init__(self):
            self.parent = None
            self.ciedelayedlinkupdownnotifdelay = None
            self.ciedelayedlinkupdownnotifenable = None
            self.cieifindexglobalpersistence = None
            self.cieifindexpersistence = None
            self.cielinkupdownconfig = CiscoIfExtensionMib.Ciscoifextsystemconfig.Cielinkupdownconfig()
            self.cielinkupdownenable = CiscoIfExtensionMib.Ciscoifextsystemconfig.Cielinkupdownenable()
            self.ciestandardlinkupdownvarbinds = None
            self.ciesystemmtu = None

        class CiestandardlinkupdownvarbindsEnum(Enum):
            """
            CiestandardlinkupdownvarbindsEnum

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

            standard = 1

            additional = 2

            other = 3


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IF_EXTENSION_MIB as meta
                return meta._meta_table['CiscoIfExtensionMib.Ciscoifextsystemconfig.CiestandardlinkupdownvarbindsEnum']


        class Cielinkupdownconfig(FixedBitsDict):
            """
            Cielinkupdownconfig

            This object specifies whether standard mib\-II defined linkUp/
            linkDown, extended linkUp/linkDown (with extra varbinds in
            addition to the varbinds defined in linkUp/linkDown) or
            cieLinkUp/cieLinkDown notifications should be generated for
            the interfaces in the system.
            
            'standardLinkUp'     \- generate standard defined mib\-II 
                                   linkUp notification if 
                                   'ifLinkUpDownTrapEnable' for the 
                                   interface is 'enabled'.
            'standardLinkDown'   \- generate standard defined mib\-II 
                                   linkDown notification if 
                                   'ifLinkUpDownTrapEnable' for the 
                                   interface is 'enabled'.  
            'additionalLinkUp'   \- generate linkUp notification with
                                   additional varbinds if 
                                   'ifLinkUpDownTrapEnable' for the 
                                   interface is 'enabled'.  
            'additionalLinkDown' \- generate linkDown notification with
                                   additional varbinds if 
                                   'ifLinkUpDownTrapEnable' for the 
                                   interface is 'enabled'.
            'ciscoLinkUp'        \- generate cieLinkUp notification
                                   if the 'ifLinkUpDownTrapEnable' for the
                                   interface is 'enabled'.
            'ciscoLinkDown'      \- generate cieLinkDown notification
                                   if the 'ifLinkUpDownTrapEnable' for the
                                   interface is 'enabled'.
            
            If multiple bits are set then multiple notifications will
            be generated for an interface if the 'ifLinkUpDownTrapEnable' 
            for the interface is 'enabled'.
            Keys are:- additionalLinkUp , additionalLinkDown , ciscoLinkDown , standardLinkDown , standardLinkUp , ciscoLinkUp

            """

            def __init__(self):
                self._dictionary = { 
                    'additionalLinkUp':False,
                    'additionalLinkDown':False,
                    'ciscoLinkDown':False,
                    'standardLinkDown':False,
                    'standardLinkUp':False,
                    'ciscoLinkUp':False,
                }
                self._pos_map = { 
                    'additionalLinkUp':2,
                    'additionalLinkDown':3,
                    'ciscoLinkDown':5,
                    'standardLinkDown':1,
                    'standardLinkUp':0,
                    'ciscoLinkUp':4,
                }

        class Cielinkupdownenable(FixedBitsDict):
            """
            Cielinkupdownenable

            Indicates whether cieLinkUp/cieLinkDown
            or standard mib\-II defined linkUp/Down or
            both, notifications should be generated
            for the interfaces in the system.
            
            'standard'  \- only generate standard defined
                          mib\-II linkUp/linkDown notification
                          if 'ifLinkUpDownTrapEnable' for 
                          the interface is 'enabled'.
            'cisco'     \- only generate cieLinkUp/cieLinkDown
                          notifications for an interface if
                          the 'ifLinkUpDownTrapEnable' for the
                          interface is 'enabled'.
            
            If both bits are selected then linkUp/linkDown and
            cieLinkUp/cieLinkDown are both generated for an 
            interface if the 'ifLinkUpDownTrapEnable' for the
            interface is 'enabled'.
            Keys are:- cisco , standard

            """

            def __init__(self):
                self._dictionary = { 
                    'cisco':False,
                    'standard':False,
                }
                self._pos_map = { 
                    'cisco':1,
                    'standard':0,
                }

        @property
        def _common_path(self):

            return '/CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/CISCO-IF-EXTENSION-MIB:ciscoIfExtSystemConfig'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ciedelayedlinkupdownnotifdelay is not None:
                return True

            if self.ciedelayedlinkupdownnotifenable is not None:
                return True

            if self.cieifindexglobalpersistence is not None:
                return True

            if self.cieifindexpersistence is not None:
                return True

            if self.cielinkupdownconfig is not None:
                if self.cielinkupdownconfig._has_data():
                    return True

            if self.cielinkupdownenable is not None:
                if self.cielinkupdownenable._has_data():
                    return True

            if self.ciestandardlinkupdownvarbinds is not None:
                return True

            if self.ciesystemmtu is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IF_EXTENSION_MIB as meta
            return meta._meta_table['CiscoIfExtensionMib.Ciscoifextsystemconfig']['meta_info']


    class Cieifpacketstatstable(object):
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
            self.parent = None
            self.cieifpacketstatsentry = YList()
            self.cieifpacketstatsentry.parent = self
            self.cieifpacketstatsentry.name = 'cieifpacketstatsentry'


        class Cieifpacketstatsentry(object):
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
                self.parent = None
                self.ifindex = None
                self.cieifinaborterrs = None
                self.cieifinframingerrs = None
                self.cieifingiantserrs = None
                self.cieifinignored = None
                self.cieifinoverrunerrs = None
                self.cieifinputqueuedrops = None
                self.cieifinruntserrs = None
                self.cieiflastintime = None
                self.cieiflastouthangtime = None
                self.cieiflastouttime = None
                self.cieifoutputqueuedrops = None
                self.cieifpacketdiscontinuitytime = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')

                return '/CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/CISCO-IF-EXTENSION-MIB:cieIfPacketStatsTable/CISCO-IF-EXTENSION-MIB:cieIfPacketStatsEntry[CISCO-IF-EXTENSION-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ifindex is not None:
                    return True

                if self.cieifinaborterrs is not None:
                    return True

                if self.cieifinframingerrs is not None:
                    return True

                if self.cieifingiantserrs is not None:
                    return True

                if self.cieifinignored is not None:
                    return True

                if self.cieifinoverrunerrs is not None:
                    return True

                if self.cieifinputqueuedrops is not None:
                    return True

                if self.cieifinruntserrs is not None:
                    return True

                if self.cieiflastintime is not None:
                    return True

                if self.cieiflastouthangtime is not None:
                    return True

                if self.cieiflastouttime is not None:
                    return True

                if self.cieifoutputqueuedrops is not None:
                    return True

                if self.cieifpacketdiscontinuitytime is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IF_EXTENSION_MIB as meta
                return meta._meta_table['CiscoIfExtensionMib.Cieifpacketstatstable.Cieifpacketstatsentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/CISCO-IF-EXTENSION-MIB:cieIfPacketStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cieifpacketstatsentry is not None:
                for child_ref in self.cieifpacketstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IF_EXTENSION_MIB as meta
            return meta._meta_table['CiscoIfExtensionMib.Cieifpacketstatstable']['meta_info']


    class Cieifinterfacetable(object):
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
            self.parent = None
            self.cieifinterfaceentry = YList()
            self.cieifinterfaceentry.parent = self
            self.cieifinterfaceentry.name = 'cieifinterfaceentry'


        class Cieifinterfaceentry(object):
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
            	**type**\:   :py:class:`CieiffillpatternconfigEnum <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CiscoIfExtensionMib.Cieifinterfacetable.Cieifinterfaceentry.CieiffillpatternconfigEnum>`
            
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
            	**type**\:   :py:class:`IfoperstatusreasonEnum <ydk.models.cisco_ios_xe.CISCO_TC.IfoperstatusreasonEnum>`
            
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
            	**type**\:   :py:class:`CieifsharedconfigEnum <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CiscoIfExtensionMib.Cieifinterfacetable.Cieifinterfaceentry.CieifsharedconfigEnum>`
            
            .. attribute:: cieifspeedgroupconfig
            
            	This object specifies the current speed group configuration on the given interface.  'notApplicable' \- the interface speed group configuration on             this interface is not applicable. It is a              read\-only value. '10G' \- the interface speed group configuration on             this interface as 10G. '1G\-2G\-4G\-8G' \- the interface speed group configuration              on this interface as 1G\-2G\-4G\-8G. '2G\-4G\-8G\-16G' \- the interface speed group configuration              on this interface as 2G\-4G\-8G\-16G
            	**type**\:   :py:class:`CieifspeedgroupconfigEnum <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CiscoIfExtensionMib.Cieifinterfacetable.Cieifinterfaceentry.CieifspeedgroupconfigEnum>`
            
            .. attribute:: cieifspeedreceive
            
            	An estimate of the interface's current receive bandwidth in bits per second.  This object is provided for interface with asymmetric interface speeds like ADSL and should be used in conjunction with ifSpeed object.  For interfaces which do not vary in bandwidth or for those where no accurate estimation can be made, this object should contain the nominal bandwidth. If the bandwidth of the interface is greater than the maximum value reportable by this object then this object should report its maximum value (4,294,967,295) and ifHighSpeed must be used to report the interace's speed.  For a sub\-layer which has no concept of bandwidth, this object should be zero
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cieifstatechangereason
            
            	This object displays a human\-readable textual string which describes the  cause of the last state change of the  interface.  Examples of the values this object can take are\:  o  'Lost Carrier' o  'administratively down' o  'up' o  'down'
            	**type**\:  str
            
            .. attribute:: cieiftransceiverfrequencyconfig
            
            	This object specifies the current transceiver frequency configuration on the given interface.  'notApplicable' \- the interface transceiver frequency  				  configuration on this interface  				  is not applicable. It is a read\-only value. 'FibreChannel' \- the interface transceiver frequency 				 configuration on this interface as                   Fibre Channel. 'Ethernet'	  \-  the interface transceiver frequency on 				 this interface as Ethernet
            	**type**\:   :py:class:`CieiftransceiverfrequencyconfigEnum <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.CiscoIfExtensionMib.Cieifinterfacetable.Cieifinterfaceentry.CieiftransceiverfrequencyconfigEnum>`
            
            

            """

            _prefix = 'CISCO-IF-EXTENSION-MIB'
            _revision = '2013-03-13'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.cieifcarriertransitioncount = None
                self.cieifcontextname = None
                self.cieifdhcpmode = None
                self.cieiffillpatternconfig = None
                self.cieifhighspeedreceive = None
                self.cieifignorebiterrorsconfig = None
                self.cieifignoreinterruptthresholdconfig = None
                self.cieifinterfacediscontinuitytime = None
                self.cieifkeepaliveenabled = None
                self.cieifmtu = None
                self.cieifoperstatuscause = None
                self.cieifoperstatuscausedescr = None
                self.cieifowner = None
                self.cieifresetcount = None
                self.cieifsharedconfig = None
                self.cieifspeedgroupconfig = None
                self.cieifspeedreceive = None
                self.cieifstatechangereason = None
                self.cieiftransceiverfrequencyconfig = None

            class CieiffillpatternconfigEnum(Enum):
                """
                CieiffillpatternconfigEnum

                This object specifies the current switchport fill pattern

                configuration on the given interface.

                'arbff8G' \- the inter frame gap fill pattern is

                			ARBFF for 8G speed.

                'idle8G' \- the inter frame gap fill pattern is

                		   IDLE for 8G speed.

                .. data:: arbff8G = 1

                .. data:: idle8G = 2

                """

                arbff8G = 1

                idle8G = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_IF_EXTENSION_MIB as meta
                    return meta._meta_table['CiscoIfExtensionMib.Cieifinterfacetable.Cieifinterfaceentry.CieiffillpatternconfigEnum']


            class CieifsharedconfigEnum(Enum):
                """
                CieifsharedconfigEnum

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

                notApplicable = 1

                ownerDedicated = 2

                ownerShared = 3

                sharedOnly = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_IF_EXTENSION_MIB as meta
                    return meta._meta_table['CiscoIfExtensionMib.Cieifinterfacetable.Cieifinterfaceentry.CieifsharedconfigEnum']


            class CieifspeedgroupconfigEnum(Enum):
                """
                CieifspeedgroupconfigEnum

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

                notApplicable = 1

                tenG = 2

                oneTwoFourEightG = 3

                twoFourEightSixteenG = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_IF_EXTENSION_MIB as meta
                    return meta._meta_table['CiscoIfExtensionMib.Cieifinterfacetable.Cieifinterfaceentry.CieifspeedgroupconfigEnum']


            class CieiftransceiverfrequencyconfigEnum(Enum):
                """
                CieiftransceiverfrequencyconfigEnum

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

                notApplicable = 1

                fibreChannel = 2

                ethernet = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_IF_EXTENSION_MIB as meta
                    return meta._meta_table['CiscoIfExtensionMib.Cieifinterfacetable.Cieifinterfaceentry.CieiftransceiverfrequencyconfigEnum']


            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')

                return '/CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/CISCO-IF-EXTENSION-MIB:cieIfInterfaceTable/CISCO-IF-EXTENSION-MIB:cieIfInterfaceEntry[CISCO-IF-EXTENSION-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ifindex is not None:
                    return True

                if self.cieifcarriertransitioncount is not None:
                    return True

                if self.cieifcontextname is not None:
                    return True

                if self.cieifdhcpmode is not None:
                    return True

                if self.cieiffillpatternconfig is not None:
                    return True

                if self.cieifhighspeedreceive is not None:
                    return True

                if self.cieifignorebiterrorsconfig is not None:
                    return True

                if self.cieifignoreinterruptthresholdconfig is not None:
                    return True

                if self.cieifinterfacediscontinuitytime is not None:
                    return True

                if self.cieifkeepaliveenabled is not None:
                    return True

                if self.cieifmtu is not None:
                    return True

                if self.cieifoperstatuscause is not None:
                    return True

                if self.cieifoperstatuscausedescr is not None:
                    return True

                if self.cieifowner is not None:
                    return True

                if self.cieifresetcount is not None:
                    return True

                if self.cieifsharedconfig is not None:
                    return True

                if self.cieifspeedgroupconfig is not None:
                    return True

                if self.cieifspeedreceive is not None:
                    return True

                if self.cieifstatechangereason is not None:
                    return True

                if self.cieiftransceiverfrequencyconfig is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IF_EXTENSION_MIB as meta
                return meta._meta_table['CiscoIfExtensionMib.Cieifinterfacetable.Cieifinterfaceentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/CISCO-IF-EXTENSION-MIB:cieIfInterfaceTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cieifinterfaceentry is not None:
                for child_ref in self.cieifinterfaceentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IF_EXTENSION_MIB as meta
            return meta._meta_table['CiscoIfExtensionMib.Cieifinterfacetable']['meta_info']


    class Cieifstatuslisttable(object):
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
            self.parent = None
            self.cieifstatuslistentry = YList()
            self.cieifstatuslistentry.parent = self
            self.cieifstatuslistentry.name = 'cieifstatuslistentry'


        class Cieifstatuslistentry(object):
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
                self.parent = None
                self.entphysicalindex = None
                self.cieifstatuslistindex = None
                self.cieinterfaceownershipbitmap = None
                self.cieinterfacesindex = None
                self.cieinterfacesopercause = None
                self.cieinterfacesopermode = None

            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYModelError('Key property entphysicalindex is None')
                if self.cieifstatuslistindex is None:
                    raise YPYModelError('Key property cieifstatuslistindex is None')

                return '/CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/CISCO-IF-EXTENSION-MIB:cieIfStatusListTable/CISCO-IF-EXTENSION-MIB:cieIfStatusListEntry[CISCO-IF-EXTENSION-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + '][CISCO-IF-EXTENSION-MIB:cieIfStatusListIndex = ' + str(self.cieifstatuslistindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.entphysicalindex is not None:
                    return True

                if self.cieifstatuslistindex is not None:
                    return True

                if self.cieinterfaceownershipbitmap is not None:
                    return True

                if self.cieinterfacesindex is not None:
                    return True

                if self.cieinterfacesopercause is not None:
                    return True

                if self.cieinterfacesopermode is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IF_EXTENSION_MIB as meta
                return meta._meta_table['CiscoIfExtensionMib.Cieifstatuslisttable.Cieifstatuslistentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/CISCO-IF-EXTENSION-MIB:cieIfStatusListTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cieifstatuslistentry is not None:
                for child_ref in self.cieifstatuslistentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IF_EXTENSION_MIB as meta
            return meta._meta_table['CiscoIfExtensionMib.Cieifstatuslisttable']['meta_info']


    class Cieifvlstatstable(object):
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
            self.parent = None
            self.cieifvlstatsentry = YList()
            self.cieifvlstatsentry.parent = self
            self.cieifvlstatsentry.name = 'cieifvlstatsentry'


        class Cieifvlstatsentry(object):
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
                self.parent = None
                self.ifindex = None
                self.cieifdropvlinoctets = None
                self.cieifdropvlinpkts = None
                self.cieifdropvloutoctets = None
                self.cieifdropvloutpkts = None
                self.cieifnodropvlinoctets = None
                self.cieifnodropvlinpkts = None
                self.cieifnodropvloutoctets = None
                self.cieifnodropvloutpkts = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')

                return '/CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/CISCO-IF-EXTENSION-MIB:cieIfVlStatsTable/CISCO-IF-EXTENSION-MIB:cieIfVlStatsEntry[CISCO-IF-EXTENSION-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ifindex is not None:
                    return True

                if self.cieifdropvlinoctets is not None:
                    return True

                if self.cieifdropvlinpkts is not None:
                    return True

                if self.cieifdropvloutoctets is not None:
                    return True

                if self.cieifdropvloutpkts is not None:
                    return True

                if self.cieifnodropvlinoctets is not None:
                    return True

                if self.cieifnodropvlinpkts is not None:
                    return True

                if self.cieifnodropvloutoctets is not None:
                    return True

                if self.cieifnodropvloutpkts is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IF_EXTENSION_MIB as meta
                return meta._meta_table['CiscoIfExtensionMib.Cieifvlstatstable.Cieifvlstatsentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/CISCO-IF-EXTENSION-MIB:cieIfVlStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cieifvlstatsentry is not None:
                for child_ref in self.cieifvlstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IF_EXTENSION_MIB as meta
            return meta._meta_table['CiscoIfExtensionMib.Cieifvlstatstable']['meta_info']


    class Cieifindexpersistencetable(object):
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
            self.parent = None
            self.cieifindexpersistenceentry = YList()
            self.cieifindexpersistenceentry.parent = self
            self.cieifindexpersistenceentry.name = 'cieifindexpersistenceentry'


        class Cieifindexpersistenceentry(object):
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
            	**type**\:   :py:class:`IfindexpersistencestateEnum <ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB.IfindexpersistencestateEnum>`
            
            .. attribute:: cieifindexpersistenceenabled
            
            	This object specifies whether the interface's ifIndex value persist across reinitialization.  Due to change in syntax, this object is deprecated by cieIfIndexPersistenceControl
            	**type**\:  bool
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'CISCO-IF-EXTENSION-MIB'
            _revision = '2013-03-13'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.cieifindexpersistencecontrol = None
                self.cieifindexpersistenceenabled = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')

                return '/CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/CISCO-IF-EXTENSION-MIB:cieIfIndexPersistenceTable/CISCO-IF-EXTENSION-MIB:cieIfIndexPersistenceEntry[CISCO-IF-EXTENSION-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ifindex is not None:
                    return True

                if self.cieifindexpersistencecontrol is not None:
                    return True

                if self.cieifindexpersistenceenabled is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IF_EXTENSION_MIB as meta
                return meta._meta_table['CiscoIfExtensionMib.Cieifindexpersistencetable.Cieifindexpersistenceentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/CISCO-IF-EXTENSION-MIB:cieIfIndexPersistenceTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cieifindexpersistenceentry is not None:
                for child_ref in self.cieifindexpersistenceentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IF_EXTENSION_MIB as meta
            return meta._meta_table['CiscoIfExtensionMib.Cieifindexpersistencetable']['meta_info']


    class Cieifdot1Qcustomethertypetable(object):
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
            self.parent = None
            self.cieifdot1qcustomethertypeentry = YList()
            self.cieifdot1qcustomethertypeentry.parent = self
            self.cieifdot1qcustomethertypeentry.name = 'cieifdot1qcustomethertypeentry'


        class Cieifdot1Qcustomethertypeentry(object):
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
                self.parent = None
                self.ifindex = None
                self.cieifdot1qcustomadminethertype = None
                self.cieifdot1qcustomoperethertype = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')

                return '/CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/CISCO-IF-EXTENSION-MIB:cieIfDot1qCustomEtherTypeTable/CISCO-IF-EXTENSION-MIB:cieIfDot1qCustomEtherTypeEntry[CISCO-IF-EXTENSION-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ifindex is not None:
                    return True

                if self.cieifdot1qcustomadminethertype is not None:
                    return True

                if self.cieifdot1qcustomoperethertype is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IF_EXTENSION_MIB as meta
                return meta._meta_table['CiscoIfExtensionMib.Cieifdot1Qcustomethertypetable.Cieifdot1Qcustomethertypeentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/CISCO-IF-EXTENSION-MIB:cieIfDot1qCustomEtherTypeTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cieifdot1qcustomethertypeentry is not None:
                for child_ref in self.cieifdot1qcustomethertypeentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IF_EXTENSION_MIB as meta
            return meta._meta_table['CiscoIfExtensionMib.Cieifdot1Qcustomethertypetable']['meta_info']


    class Cieifutiltable(object):
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
            self.parent = None
            self.cieifutilentry = YList()
            self.cieifutilentry.parent = self
            self.cieifutilentry.name = 'cieifutilentry'


        class Cieifutilentry(object):
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
                self.parent = None
                self.ifindex = None
                self.cieifinoctetrate = None
                self.cieifinpktrate = None
                self.cieifinterval = None
                self.cieifoutoctetrate = None
                self.cieifoutpktrate = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')

                return '/CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/CISCO-IF-EXTENSION-MIB:cieIfUtilTable/CISCO-IF-EXTENSION-MIB:cieIfUtilEntry[CISCO-IF-EXTENSION-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ifindex is not None:
                    return True

                if self.cieifinoctetrate is not None:
                    return True

                if self.cieifinpktrate is not None:
                    return True

                if self.cieifinterval is not None:
                    return True

                if self.cieifoutoctetrate is not None:
                    return True

                if self.cieifoutpktrate is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IF_EXTENSION_MIB as meta
                return meta._meta_table['CiscoIfExtensionMib.Cieifutiltable.Cieifutilentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/CISCO-IF-EXTENSION-MIB:cieIfUtilTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cieifutilentry is not None:
                for child_ref in self.cieifutilentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IF_EXTENSION_MIB as meta
            return meta._meta_table['CiscoIfExtensionMib.Cieifutiltable']['meta_info']


    class Cieifdot1Dbasemappingtable(object):
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
            self.parent = None
            self.cieifdot1dbasemappingentry = YList()
            self.cieifdot1dbasemappingentry.parent = self
            self.cieifdot1dbasemappingentry.name = 'cieifdot1dbasemappingentry'


        class Cieifdot1Dbasemappingentry(object):
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
                self.parent = None
                self.ifindex = None
                self.cieifdot1dbasemappingport = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')

                return '/CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/CISCO-IF-EXTENSION-MIB:cieIfDot1dBaseMappingTable/CISCO-IF-EXTENSION-MIB:cieIfDot1dBaseMappingEntry[CISCO-IF-EXTENSION-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ifindex is not None:
                    return True

                if self.cieifdot1dbasemappingport is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IF_EXTENSION_MIB as meta
                return meta._meta_table['CiscoIfExtensionMib.Cieifdot1Dbasemappingtable.Cieifdot1Dbasemappingentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/CISCO-IF-EXTENSION-MIB:cieIfDot1dBaseMappingTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cieifdot1dbasemappingentry is not None:
                for child_ref in self.cieifdot1dbasemappingentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IF_EXTENSION_MIB as meta
            return meta._meta_table['CiscoIfExtensionMib.Cieifdot1Dbasemappingtable']['meta_info']


    class Cieifnamemappingtable(object):
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
            self.parent = None
            self.cieifnamemappingentry = YList()
            self.cieifnamemappingentry.parent = self
            self.cieifnamemappingentry.name = 'cieifnamemappingentry'


        class Cieifnamemappingentry(object):
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
                self.parent = None
                self.cieifname = None
                self.cieifindex = None

            @property
            def _common_path(self):
                if self.cieifname is None:
                    raise YPYModelError('Key property cieifname is None')

                return '/CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/CISCO-IF-EXTENSION-MIB:cieIfNameMappingTable/CISCO-IF-EXTENSION-MIB:cieIfNameMappingEntry[CISCO-IF-EXTENSION-MIB:cieIfName = ' + str(self.cieifname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cieifname is not None:
                    return True

                if self.cieifindex is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IF_EXTENSION_MIB as meta
                return meta._meta_table['CiscoIfExtensionMib.Cieifnamemappingtable.Cieifnamemappingentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB/CISCO-IF-EXTENSION-MIB:cieIfNameMappingTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cieifnamemappingentry is not None:
                for child_ref in self.cieifnamemappingentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IF_EXTENSION_MIB as meta
            return meta._meta_table['CiscoIfExtensionMib.Cieifnamemappingtable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-IF-EXTENSION-MIB:CISCO-IF-EXTENSION-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.cieifdot1dbasemappingtable is not None and self.cieifdot1dbasemappingtable._has_data():
            return True

        if self.cieifdot1qcustomethertypetable is not None and self.cieifdot1qcustomethertypetable._has_data():
            return True

        if self.cieifindexpersistencetable is not None and self.cieifindexpersistencetable._has_data():
            return True

        if self.cieifinterfacetable is not None and self.cieifinterfacetable._has_data():
            return True

        if self.cieifnamemappingtable is not None and self.cieifnamemappingtable._has_data():
            return True

        if self.cieifpacketstatstable is not None and self.cieifpacketstatstable._has_data():
            return True

        if self.cieifstatuslisttable is not None and self.cieifstatuslisttable._has_data():
            return True

        if self.cieifutiltable is not None and self.cieifutiltable._has_data():
            return True

        if self.cieifvlstatstable is not None and self.cieifvlstatstable._has_data():
            return True

        if self.ciscoifextsystemconfig is not None and self.ciscoifextsystemconfig._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_IF_EXTENSION_MIB as meta
        return meta._meta_table['CiscoIfExtensionMib']['meta_info']



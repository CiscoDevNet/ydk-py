""" CISCO_CABLE_WIDEBAND_MIB 

This is the MIB module for the support of Channel Bonding
Protocol for the Cable Modem Termination System (CMTS).

Wideband DOCSIS is a method of increasing downstream
bandwidth by simultaneously transmitting DOCSIS data
over multiple RF channels. This DOCSIS data is
organized as a sequence of 188\-byte MPEG\-TS data packets.

A Wideband CMTS (WCMTS) is a CMTS that also transmits
Wideband MPEG\-TS packets.

An Edge QAM (Quadrature Amplitude Modulation) device is one
which provides the QAM and used to couple the Wideband MPEG\-TS
packet onto the HFC plant.

A Wideband Cable Modem (WCM) is a CableModem (CM) that
is able to receive Wideband MPEG\-TS packets.

A wideband channel or Bonded Group (BG) is a logical
grouping of one or more physical RF channels over which
MPEG\-TS packets are carried. Wideband channel carries DOCSIS
bonded packets encapsulated in MPEG\-TS packets from a
WCMTS to one or more WCMs.

Packets outgoing from WCMTS to the WCM are formatted with
the DOCSIS Header. The DOCSIS packets are then formatted into
MPEG\-TS data packets. These are 188 byte MPEG packets
containing the DOCSIS information.
Within DOCSIS Header of the WB Channel there is an extended
header called, DOCSIS Bonding Extended Header, the format of
which is shown below\:

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-
\|  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-  \|
\| \|  TYPE \| LEN \|       BSID           \|      SEQ        \|
\|  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-  \|
\| \|    byte 0   \|     byte 1\-2         \|    byte 3\-4     \|
\|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\|
              DOCSIS Bonding Extended Header

BSID is the Bonding Service IDentifier, it defines a sequence
number for a Wideband channel. It is used by the WCM to
re\-sequence packets received over downstream channels to
maintain packet order. SEQ is per service flow sequence number.
Whereas TYPE is the type of the Bonding Extended Header and LEN
specifies its length.

A Narrowband Channel is a standard DOCSIS downstream channel
which contains exactly one RF channel.
The wideband protocol utilizes the existing narrowband
downstream channel for carrying the MAC management and
signaling messages and the associated narrowband upstream
for return data traffic and signaling.

The channel bonding protocol supports multiple wideband
bonded groups. This will allow the WCM to listen to multiple
bonded groups at the same time. This would support (for example)
multicast video being sent to a CPE device on the LAN side of
the WCM in addition to standard DOCSIS data.

Channel Bonding allows two types of Bonding Group (BG) interfaces.
These are Secondary BG interface and non\-Secondary BG
interface. The Secondary BG interfaces will carry the multicast
traffic, whereas, the non\-Secondary BG interface will carry the
non\-multicast traffic.
This MIB also allows for configuration of the RF channels
on the WCMTS, as well as the association between the RF and
narrowband downstream channels with the BG channel.

Fiber Node is an optical node which terminates the fiber based
downstream signal as an electrical signal onto a coaxial RF cable.

DEPI\:  Downstream external physical interface. 
TSID\:  MPEG2 Transport Stream ID.
SFP\:   Small Form\-Factor Pluggable.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class CISCOCABLEWIDEBANDMIB(Entity):
    """
    
    
    .. attribute:: ciscocablewidebandmibobjects
    
    	
    	**type**\:  :py:class:`CiscoCableWidebandMIBObjects <ydk.models.cisco_ios_xe.CISCO_CABLE_WIDEBAND_MIB.CISCOCABLEWIDEBANDMIB.CiscoCableWidebandMIBObjects>`
    
    	**config**\: False
    
    .. attribute:: ccwbrfchanneltable
    
    	This table contains attributes of the physical RF channels. MPEG\-TS packets are sent across RF channels within a wideband channel.  These physical RF channels might be present on a different system but the WCMTS entity requires the knowledge of that system for its operation
    	**type**\:  :py:class:`CcwbRFChannelTable <ydk.models.cisco_ios_xe.CISCO_CABLE_WIDEBAND_MIB.CISCOCABLEWIDEBANDMIB.CcwbRFChannelTable>`
    
    	**config**\: False
    
    .. attribute:: ccwbwbtorfmappingtable
    
    	A wideband channel is a logical grouping of one or more physical RF channels over which Wideband MPEG\-TS packets are carried.  This table contains association information of the wideband channels to the RF channels that are available for the WCMTS
    	**type**\:  :py:class:`CcwbWBtoRFMappingTable <ydk.models.cisco_ios_xe.CISCO_CABLE_WIDEBAND_MIB.CISCOCABLEWIDEBANDMIB.CcwbWBtoRFMappingTable>`
    
    	**config**\: False
    
    .. attribute:: ccwbwbtonbmappingtable
    
    	This table contains information of the mapping of the wideband channels to the Narrowband channels that are available on the WCMTS.  The wideband protocol utilizes the existing narrowband downstream channel for carrying the MAC management and signaling messages and the associated narrowband upstream for return data traffic and signaling
    	**type**\:  :py:class:`CcwbWBtoNBMappingTable <ydk.models.cisco_ios_xe.CISCO_CABLE_WIDEBAND_MIB.CISCOCABLEWIDEBANDMIB.CcwbWBtoNBMappingTable>`
    
    	**config**\: False
    
    .. attribute:: ccwbwbbondgrptable
    
    	This table provides information about a Wideband BG interface, whether its configured to carry multicast or non\-multicast traffic. For multicast the BG interface type is Secondary and for non\-multicast its non\-Secondary. Other objects could be added to this later in the future
    	**type**\:  :py:class:`CcwbWBBondGrpTable <ydk.models.cisco_ios_xe.CISCO_CABLE_WIDEBAND_MIB.CISCOCABLEWIDEBANDMIB.CcwbWBBondGrpTable>`
    
    	**config**\: False
    
    .. attribute:: ccwbwbcmstatustable
    
    	This table contains Wideband Cable Modem(WCM) connectivity state. A WCM connectivity state can be associated with multiple Wideband interfaces
    	**type**\:  :py:class:`CcwbWBCmStatusTable <ydk.models.cisco_ios_xe.CISCO_CABLE_WIDEBAND_MIB.CISCOCABLEWIDEBANDMIB.CcwbWBCmStatusTable>`
    
    	**config**\: False
    
    .. attribute:: ccwbwbcmstatusexttable
    
    	An entry in this table exists for each Wideband Cable Modem which links to one or more WB interface
    	**type**\:  :py:class:`CcwbWBCmStatusExtTable <ydk.models.cisco_ios_xe.CISCO_CABLE_WIDEBAND_MIB.CISCOCABLEWIDEBANDMIB.CcwbWBCmStatusExtTable>`
    
    	**config**\: False
    
    .. attribute:: ccwbfibernodedescrtable
    
    	This table contains the description of a Fiber Node on a CMTS. An entry in this table exists for each FiberNode ID
    	**type**\:  :py:class:`CcwbFiberNodeDescrTable <ydk.models.cisco_ios_xe.CISCO_CABLE_WIDEBAND_MIB.CISCOCABLEWIDEBANDMIB.CcwbFiberNodeDescrTable>`
    
    	**config**\: False
    
    .. attribute:: ccwbfibernodetable
    
    	This table provides configuration information of each Fiber node. It will provide topology information of each Fiber node, which includes information such as, Narrowband and Wideband QAMs
    	**type**\:  :py:class:`CcwbFiberNodeTable <ydk.models.cisco_ios_xe.CISCO_CABLE_WIDEBAND_MIB.CISCOCABLEWIDEBANDMIB.CcwbFiberNodeTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'CISCO-CABLE-WIDEBAND-MIB'
    _revision = '2011-01-05'

    def __init__(self):
        super(CISCOCABLEWIDEBANDMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-CABLE-WIDEBAND-MIB"
        self.yang_parent_name = "CISCO-CABLE-WIDEBAND-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("ciscoCableWidebandMIBObjects", ("ciscocablewidebandmibobjects", CISCOCABLEWIDEBANDMIB.CiscoCableWidebandMIBObjects)), ("ccwbRFChannelTable", ("ccwbrfchanneltable", CISCOCABLEWIDEBANDMIB.CcwbRFChannelTable)), ("ccwbWBtoRFMappingTable", ("ccwbwbtorfmappingtable", CISCOCABLEWIDEBANDMIB.CcwbWBtoRFMappingTable)), ("ccwbWBtoNBMappingTable", ("ccwbwbtonbmappingtable", CISCOCABLEWIDEBANDMIB.CcwbWBtoNBMappingTable)), ("ccwbWBBondGrpTable", ("ccwbwbbondgrptable", CISCOCABLEWIDEBANDMIB.CcwbWBBondGrpTable)), ("ccwbWBCmStatusTable", ("ccwbwbcmstatustable", CISCOCABLEWIDEBANDMIB.CcwbWBCmStatusTable)), ("ccwbWBCmStatusExtTable", ("ccwbwbcmstatusexttable", CISCOCABLEWIDEBANDMIB.CcwbWBCmStatusExtTable)), ("ccwbFiberNodeDescrTable", ("ccwbfibernodedescrtable", CISCOCABLEWIDEBANDMIB.CcwbFiberNodeDescrTable)), ("ccwbFiberNodeTable", ("ccwbfibernodetable", CISCOCABLEWIDEBANDMIB.CcwbFiberNodeTable))])
        self._leafs = OrderedDict()

        self.ciscocablewidebandmibobjects = CISCOCABLEWIDEBANDMIB.CiscoCableWidebandMIBObjects()
        self.ciscocablewidebandmibobjects.parent = self
        self._children_name_map["ciscocablewidebandmibobjects"] = "ciscoCableWidebandMIBObjects"

        self.ccwbrfchanneltable = CISCOCABLEWIDEBANDMIB.CcwbRFChannelTable()
        self.ccwbrfchanneltable.parent = self
        self._children_name_map["ccwbrfchanneltable"] = "ccwbRFChannelTable"

        self.ccwbwbtorfmappingtable = CISCOCABLEWIDEBANDMIB.CcwbWBtoRFMappingTable()
        self.ccwbwbtorfmappingtable.parent = self
        self._children_name_map["ccwbwbtorfmappingtable"] = "ccwbWBtoRFMappingTable"

        self.ccwbwbtonbmappingtable = CISCOCABLEWIDEBANDMIB.CcwbWBtoNBMappingTable()
        self.ccwbwbtonbmappingtable.parent = self
        self._children_name_map["ccwbwbtonbmappingtable"] = "ccwbWBtoNBMappingTable"

        self.ccwbwbbondgrptable = CISCOCABLEWIDEBANDMIB.CcwbWBBondGrpTable()
        self.ccwbwbbondgrptable.parent = self
        self._children_name_map["ccwbwbbondgrptable"] = "ccwbWBBondGrpTable"

        self.ccwbwbcmstatustable = CISCOCABLEWIDEBANDMIB.CcwbWBCmStatusTable()
        self.ccwbwbcmstatustable.parent = self
        self._children_name_map["ccwbwbcmstatustable"] = "ccwbWBCmStatusTable"

        self.ccwbwbcmstatusexttable = CISCOCABLEWIDEBANDMIB.CcwbWBCmStatusExtTable()
        self.ccwbwbcmstatusexttable.parent = self
        self._children_name_map["ccwbwbcmstatusexttable"] = "ccwbWBCmStatusExtTable"

        self.ccwbfibernodedescrtable = CISCOCABLEWIDEBANDMIB.CcwbFiberNodeDescrTable()
        self.ccwbfibernodedescrtable.parent = self
        self._children_name_map["ccwbfibernodedescrtable"] = "ccwbFiberNodeDescrTable"

        self.ccwbfibernodetable = CISCOCABLEWIDEBANDMIB.CcwbFiberNodeTable()
        self.ccwbfibernodetable.parent = self
        self._children_name_map["ccwbfibernodetable"] = "ccwbFiberNodeTable"
        self._segment_path = lambda: "CISCO-CABLE-WIDEBAND-MIB:CISCO-CABLE-WIDEBAND-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCOCABLEWIDEBANDMIB, [], name, value)


    class CiscoCableWidebandMIBObjects(Entity):
        """
        
        
        .. attribute:: ccwbrfchanutilinterval
        
        	The time interval in seconds over which the RF channels utilization index is calculated. All RF channels use the same interval.  Setting a value of zero disables utilization reporting.  This value should be persisted accross CMTS reinitializations
        	**type**\: int
        
        	**range:** 0..86400
        
        	**config**\: False
        
        	**units**\: seconds
        
        .. attribute:: ccwbsfplinktrapenable
        
        	This object specifies whether ccwbSFPLinkDownNotification and ccwbSFPLinkUpNotification are generated
        	**type**\: int
        
        	**range:** 0..1
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-CABLE-WIDEBAND-MIB'
        _revision = '2011-01-05'

        def __init__(self):
            super(CISCOCABLEWIDEBANDMIB.CiscoCableWidebandMIBObjects, self).__init__()

            self.yang_name = "ciscoCableWidebandMIBObjects"
            self.yang_parent_name = "CISCO-CABLE-WIDEBAND-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ccwbrfchanutilinterval', (YLeaf(YType.uint32, 'ccwbRFChanUtilInterval'), ['int'])),
                ('ccwbsfplinktrapenable', (YLeaf(YType.int32, 'ccwbSFPLinkTrapEnable'), ['int'])),
            ])
            self.ccwbrfchanutilinterval = None
            self.ccwbsfplinktrapenable = None
            self._segment_path = lambda: "ciscoCableWidebandMIBObjects"
            self._absolute_path = lambda: "CISCO-CABLE-WIDEBAND-MIB:CISCO-CABLE-WIDEBAND-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCABLEWIDEBANDMIB.CiscoCableWidebandMIBObjects, ['ccwbrfchanutilinterval', 'ccwbsfplinktrapenable'], name, value)



    class CcwbRFChannelTable(Entity):
        """
        This table contains attributes of the physical
        RF channels. MPEG\-TS packets are sent across RF
        channels within a wideband channel.
        
        These physical RF channels might be present on a
        different system but the WCMTS entity requires
        the knowledge of that system for its operation.
        
        .. attribute:: ccwbrfchannelentry
        
        	An entry provides a list of attributes for a single downstream RF channel per WCMTS entity.  An entry in this table exists for each configured RF channel on the WCMTS entity that provides the wideband DOCSIS functionality. The index, entPhysicalIndex, used here is the physical index of the wideband controller card. Since RF channels are considered part of the Wideband controller card, hence entPhysicalIndex is used for associating RF channels
        	**type**\: list of  		 :py:class:`CcwbRFChannelEntry <ydk.models.cisco_ios_xe.CISCO_CABLE_WIDEBAND_MIB.CISCOCABLEWIDEBANDMIB.CcwbRFChannelTable.CcwbRFChannelEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-CABLE-WIDEBAND-MIB'
        _revision = '2011-01-05'

        def __init__(self):
            super(CISCOCABLEWIDEBANDMIB.CcwbRFChannelTable, self).__init__()

            self.yang_name = "ccwbRFChannelTable"
            self.yang_parent_name = "CISCO-CABLE-WIDEBAND-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ccwbRFChannelEntry", ("ccwbrfchannelentry", CISCOCABLEWIDEBANDMIB.CcwbRFChannelTable.CcwbRFChannelEntry))])
            self._leafs = OrderedDict()

            self.ccwbrfchannelentry = YList(self)
            self._segment_path = lambda: "ccwbRFChannelTable"
            self._absolute_path = lambda: "CISCO-CABLE-WIDEBAND-MIB:CISCO-CABLE-WIDEBAND-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCABLEWIDEBANDMIB.CcwbRFChannelTable, [], name, value)


        class CcwbRFChannelEntry(Entity):
            """
            An entry provides a list of attributes for a single
            downstream RF channel per WCMTS entity.
            
            An entry in this table exists for each configured
            RF channel on the WCMTS entity that provides the
            wideband DOCSIS functionality. The index, entPhysicalIndex,
            used here is the physical index of the wideband controller
            card. Since RF channels are considered part of the Wideband
            controller card, hence entPhysicalIndex is used for
            associating RF channels.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.EntPhysicalTable.EntPhysicalEntry>`
            
            	**config**\: False
            
            .. attribute:: ccwbrfchannelnum  (key)
            
            	The WCMTS identification of the RF channel. The range of this object is limited to 0\-18 in the case of annex A/256qam, and 0\-23 for Annex B and C
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: ccwbrfchannelfrequency
            
            	The center of the downstream frequency associated with this RF channel. The final downstream RF frequency may be provided by an edge QAM device or the CMTS itself. See the associated compliance object for a description of valid frequencies that may be written to this object.  If the downstream frequency associated with this RF channel is greater than the maximum value reportable by this object then this object should report its maximum value (1,000,000,000) and ccwbRFChannelFrequencyRev1 must be used to report the downstream frequency.  This object is deprecated and replaced by ccwbRFChannelFrequencyRev1
            	**type**\: int
            
            	**range:** 0..1000000000
            
            	**config**\: False
            
            	**units**\: hertz
            
            	**status**\: deprecated
            
            .. attribute:: ccwbrfchannelwidth
            
            	The bandwidth of this downstream RF channel. Most implementations are expected to support a channel width of 6 MHz (North America) and/or 8 MHz (Europe). See the associated compliance object for a description of the valid channel widths for this object
            	**type**\: int
            
            	**range:** 0..16000000
            
            	**config**\: False
            
            	**units**\: hertz
            
            .. attribute:: ccwbrfchannelmodulation
            
            	The modulation type associated with this downstream RF channel. See the associated conformance object for write conditions an limitations. See the DOCSIS specification for specifics on the modulation profiles implied by qam64 qam256 and qam1024. qam64, qam256 and qam1024 are various modulation schemes often used in digital cable and cable modem applications. The numbers 64/256/1024 in qam represent constellation points, which is the measurement of qam transmission capability, the higher the number, higher the bits that can be transmitted
            	**type**\:  :py:class:`CcwbRFChannelModulation <ydk.models.cisco_ios_xe.CISCO_CABLE_WIDEBAND_MIB.CISCOCABLEWIDEBANDMIB.CcwbRFChannelTable.CcwbRFChannelEntry.CcwbRFChannelModulation>`
            
            	**config**\: False
            
            .. attribute:: ccwbrfchannelannex
            
            	The value of this object indicates the conformance of the implementation to important regional cable standards. annexA \: Annex A from ITU\-J83 is used. annexB \: Annex B from ITU\-J83 is used. annexC \: Annex C from ITU\-J83 is used
            	**type**\:  :py:class:`CcwbRFChannelAnnex <ydk.models.cisco_ios_xe.CISCO_CABLE_WIDEBAND_MIB.CISCOCABLEWIDEBANDMIB.CcwbRFChannelTable.CcwbRFChannelEntry.CcwbRFChannelAnnex>`
            
            	**config**\: False
            
            .. attribute:: ccwbrfchannelmpegpkts
            
            	The number of MPEG packets transmitted on this RF channel
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: Packets
            
            .. attribute:: ccwbrfchannelstoragetype
            
            	The storage type for this conceptual row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            	**config**\: False
            
            .. attribute:: ccwbrfchannelrowstatus
            
            	Controls and reflects the status of rows in this table. It can be used for creating and deleting entries in this table.  The ccwbRFChannelAnnex and ccwbRFChannelModulation must be valid for a row to be created
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            .. attribute:: ccwbrfchannelutilization
            
            	The calculated and truncated utilization for this RF channel over the previous complete measuring interval. The configured duration of the measurement intervals is defined in the ccwbRFChanUtilInterval object.  The utilization index is a percentage expressing the ratio between bytes used to transmit data versus the total number of bytes transmitted in the raw bandwidth of the RF channel
            	**type**\: int
            
            	**range:** 0..100
            
            	**config**\: False
            
            	**units**\: percent
            
            .. attribute:: ccwbrfchannelfrequencyrev1
            
            	The center of the downstream frequency associated with this RF channel. The final downstream RF frequency may be provided by an edge QAM device or the CMTS itself. See the associated compliance object for a description of valid frequencies that may be written to this object
            	**type**\: int
            
            	**range:** 55000000..1050000000
            
            	**config**\: False
            
            	**units**\: hertz
            
            .. attribute:: ccwbrfchanqamipaddresstype
            
            	The type of internet address. This object identifies the internet address type specified by ccwbRFChanQamIPAddress object
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: ccwbrfchanqamipaddress
            
            	The IP address of the edge QAM device or the CMTS cable interface which provides the physical RF channel. The IP address will be of the type represented by object ccwbRFChanQamIPAddressType
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: ccwbrfchanqammacaddress
            
            	The MAC address of the edge QAM device or next hop router which might be present between the WCMTS and the edge QAM
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            	**config**\: False
            
            .. attribute:: ccwbrfchanqamudpport
            
            	The port number on the edge QAM associated with this RF channel
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: ccwbrfchanqamtos
            
            	The value of the TOS field in the IP header for all Ethernet frames destined for the given RF channel
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: ccwbrfchanqamvlanid
            
            	The VLAN ID to be inserted in the Ethernet frames when using 802.1q frames instead of normal 802.1 frames for the given RF channel. The value of 0 indicates that 802.1 frames are being used and is not supported in setting this object
            	**type**\: int
            
            	**range:** 0..4095
            
            	**config**\: False
            
            .. attribute:: ccwbrfchanqamprioritybits
            
            	The priority bits used when inserting Ethernet 802.1q VLAN tags into the Ethernet frames destined for a given RF channel. Priority Bits (0=Best effort, 1=background, 2=spare, 3=excellent effort, 4=controlled load, 5=video, 6=voice, 7=network control)
            	**type**\: int
            
            	**range:** 0..7
            
            	**config**\: False
            
            .. attribute:: ccwbrfchanqamdepiremoteid
            
            	The DEPI remote ID on edge QAM associated with this RF channel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ccwbrfchanqamdepitunnel
            
            	This object specifies the name of the DEPI tunnel which determines the DEPI data session configuration associated with this RF channel
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: ccwbrfchanqamtsid
            
            	This object specifies the MPEG2 transport stream ID which is associated with this RF channel
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-CABLE-WIDEBAND-MIB'
            _revision = '2011-01-05'

            def __init__(self):
                super(CISCOCABLEWIDEBANDMIB.CcwbRFChannelTable.CcwbRFChannelEntry, self).__init__()

                self.yang_name = "ccwbRFChannelEntry"
                self.yang_parent_name = "ccwbRFChannelTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','ccwbrfchannelnum']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.str, 'entPhysicalIndex'), ['int'])),
                    ('ccwbrfchannelnum', (YLeaf(YType.uint32, 'ccwbRFChannelNum'), ['int'])),
                    ('ccwbrfchannelfrequency', (YLeaf(YType.uint32, 'ccwbRFChannelFrequency'), ['int'])),
                    ('ccwbrfchannelwidth', (YLeaf(YType.uint32, 'ccwbRFChannelWidth'), ['int'])),
                    ('ccwbrfchannelmodulation', (YLeaf(YType.enumeration, 'ccwbRFChannelModulation'), [('ydk.models.cisco_ios_xe.CISCO_CABLE_WIDEBAND_MIB', 'CISCOCABLEWIDEBANDMIB', 'CcwbRFChannelTable.CcwbRFChannelEntry.CcwbRFChannelModulation')])),
                    ('ccwbrfchannelannex', (YLeaf(YType.enumeration, 'ccwbRFChannelAnnex'), [('ydk.models.cisco_ios_xe.CISCO_CABLE_WIDEBAND_MIB', 'CISCOCABLEWIDEBANDMIB', 'CcwbRFChannelTable.CcwbRFChannelEntry.CcwbRFChannelAnnex')])),
                    ('ccwbrfchannelmpegpkts', (YLeaf(YType.uint64, 'ccwbRFChannelMpegPkts'), ['int'])),
                    ('ccwbrfchannelstoragetype', (YLeaf(YType.enumeration, 'ccwbRFChannelStorageType'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                    ('ccwbrfchannelrowstatus', (YLeaf(YType.enumeration, 'ccwbRFChannelRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('ccwbrfchannelutilization', (YLeaf(YType.uint32, 'ccwbRFChannelUtilization'), ['int'])),
                    ('ccwbrfchannelfrequencyrev1', (YLeaf(YType.uint32, 'ccwbRFChannelFrequencyRev1'), ['int'])),
                    ('ccwbrfchanqamipaddresstype', (YLeaf(YType.enumeration, 'ccwbRFChanQamIPAddressType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('ccwbrfchanqamipaddress', (YLeaf(YType.str, 'ccwbRFChanQamIPAddress'), ['str'])),
                    ('ccwbrfchanqammacaddress', (YLeaf(YType.str, 'ccwbRFChanQamMacAddress'), ['str'])),
                    ('ccwbrfchanqamudpport', (YLeaf(YType.uint16, 'ccwbRFChanQamUdpPort'), ['int'])),
                    ('ccwbrfchanqamtos', (YLeaf(YType.uint32, 'ccwbRFChanQamTos'), ['int'])),
                    ('ccwbrfchanqamvlanid', (YLeaf(YType.uint32, 'ccwbRFChanQamVlanId'), ['int'])),
                    ('ccwbrfchanqamprioritybits', (YLeaf(YType.uint32, 'ccwbRFChanQamPriorityBits'), ['int'])),
                    ('ccwbrfchanqamdepiremoteid', (YLeaf(YType.uint32, 'ccwbRFChanQamDepiRemoteId'), ['int'])),
                    ('ccwbrfchanqamdepitunnel', (YLeaf(YType.str, 'ccwbRFChanQamDepiTunnel'), ['str'])),
                    ('ccwbrfchanqamtsid', (YLeaf(YType.uint32, 'ccwbRFChanQamTsid'), ['int'])),
                ])
                self.entphysicalindex = None
                self.ccwbrfchannelnum = None
                self.ccwbrfchannelfrequency = None
                self.ccwbrfchannelwidth = None
                self.ccwbrfchannelmodulation = None
                self.ccwbrfchannelannex = None
                self.ccwbrfchannelmpegpkts = None
                self.ccwbrfchannelstoragetype = None
                self.ccwbrfchannelrowstatus = None
                self.ccwbrfchannelutilization = None
                self.ccwbrfchannelfrequencyrev1 = None
                self.ccwbrfchanqamipaddresstype = None
                self.ccwbrfchanqamipaddress = None
                self.ccwbrfchanqammacaddress = None
                self.ccwbrfchanqamudpport = None
                self.ccwbrfchanqamtos = None
                self.ccwbrfchanqamvlanid = None
                self.ccwbrfchanqamprioritybits = None
                self.ccwbrfchanqamdepiremoteid = None
                self.ccwbrfchanqamdepitunnel = None
                self.ccwbrfchanqamtsid = None
                self._segment_path = lambda: "ccwbRFChannelEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']" + "[ccwbRFChannelNum='" + str(self.ccwbrfchannelnum) + "']"
                self._absolute_path = lambda: "CISCO-CABLE-WIDEBAND-MIB:CISCO-CABLE-WIDEBAND-MIB/ccwbRFChannelTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCABLEWIDEBANDMIB.CcwbRFChannelTable.CcwbRFChannelEntry, ['entphysicalindex', 'ccwbrfchannelnum', 'ccwbrfchannelfrequency', 'ccwbrfchannelwidth', 'ccwbrfchannelmodulation', 'ccwbrfchannelannex', 'ccwbrfchannelmpegpkts', 'ccwbrfchannelstoragetype', 'ccwbrfchannelrowstatus', 'ccwbrfchannelutilization', 'ccwbrfchannelfrequencyrev1', 'ccwbrfchanqamipaddresstype', 'ccwbrfchanqamipaddress', 'ccwbrfchanqammacaddress', 'ccwbrfchanqamudpport', 'ccwbrfchanqamtos', 'ccwbrfchanqamvlanid', 'ccwbrfchanqamprioritybits', 'ccwbrfchanqamdepiremoteid', 'ccwbrfchanqamdepitunnel', 'ccwbrfchanqamtsid'], name, value)

            class CcwbRFChannelAnnex(Enum):
                """
                CcwbRFChannelAnnex (Enum Class)

                The value of this object indicates the conformance of

                the implementation to important regional cable standards.

                annexA \: Annex A from ITU\-J83 is used.

                annexB \: Annex B from ITU\-J83 is used.

                annexC \: Annex C from ITU\-J83 is used.

                .. data:: annexA = 1

                .. data:: annexB = 2

                .. data:: annexC = 3

                """

                annexA = Enum.YLeaf(1, "annexA")

                annexB = Enum.YLeaf(2, "annexB")

                annexC = Enum.YLeaf(3, "annexC")


            class CcwbRFChannelModulation(Enum):
                """
                CcwbRFChannelModulation (Enum Class)

                The modulation type associated with this downstream RF

                channel. See the associated conformance object for write

                conditions an limitations. See the DOCSIS specification

                for specifics on the modulation profiles implied by qam64

                qam256 and qam1024.

                qam64, qam256 and qam1024 are various modulation schemes

                often used in digital cable and cable modem applications.

                The numbers 64/256/1024 in qam represent constellation

                points, which is the measurement of qam transmission

                capability, the higher the number, higher the bits that

                can be transmitted.

                .. data:: qam64 = 1

                .. data:: qam256 = 2

                .. data:: qam1024 = 3

                """

                qam64 = Enum.YLeaf(1, "qam64")

                qam256 = Enum.YLeaf(2, "qam256")

                qam1024 = Enum.YLeaf(3, "qam1024")





    class CcwbWBtoRFMappingTable(Entity):
        """
        A wideband channel is a logical grouping of one or more
        physical RF channels over which Wideband MPEG\-TS packets
        are carried.
        
        This table contains association information of the wideband
        channels to the RF channels that are available for the WCMTS.
        
        .. attribute:: ccwbwbtorfmappingentry
        
        	An entry provides a list of attributes for a single association between a wideband channel and a RF channel.  An entry in this table exists for each association between a wideband channel and RF channel on the WCMTS. It is indexed by the ifIndex of the wideband channel and entPhysicalIndex and ccwbRFChannelNum which represents the RF channel.  This object may be modified or deleted once they are already created
        	**type**\: list of  		 :py:class:`CcwbWBtoRFMappingEntry <ydk.models.cisco_ios_xe.CISCO_CABLE_WIDEBAND_MIB.CISCOCABLEWIDEBANDMIB.CcwbWBtoRFMappingTable.CcwbWBtoRFMappingEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-CABLE-WIDEBAND-MIB'
        _revision = '2011-01-05'

        def __init__(self):
            super(CISCOCABLEWIDEBANDMIB.CcwbWBtoRFMappingTable, self).__init__()

            self.yang_name = "ccwbWBtoRFMappingTable"
            self.yang_parent_name = "CISCO-CABLE-WIDEBAND-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ccwbWBtoRFMappingEntry", ("ccwbwbtorfmappingentry", CISCOCABLEWIDEBANDMIB.CcwbWBtoRFMappingTable.CcwbWBtoRFMappingEntry))])
            self._leafs = OrderedDict()

            self.ccwbwbtorfmappingentry = YList(self)
            self._segment_path = lambda: "ccwbWBtoRFMappingTable"
            self._absolute_path = lambda: "CISCO-CABLE-WIDEBAND-MIB:CISCO-CABLE-WIDEBAND-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCABLEWIDEBANDMIB.CcwbWBtoRFMappingTable, [], name, value)


        class CcwbWBtoRFMappingEntry(Entity):
            """
            An entry provides a list of attributes for a single
            association between a wideband channel and a RF channel.
            
            An entry in this table exists for each association
            between a wideband channel and RF channel on the WCMTS.
            It is indexed by the ifIndex of the wideband channel
            and entPhysicalIndex and ccwbRFChannelNum which
            represents the RF channel.
            
            This object may be modified or deleted once they are
            already created.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.EntPhysicalTable.EntPhysicalEntry>`
            
            	**config**\: False
            
            .. attribute:: ccwbrfchannelnum  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..255
            
            	**refers to**\:  :py:class:`ccwbrfchannelnum <ydk.models.cisco_ios_xe.CISCO_CABLE_WIDEBAND_MIB.CISCOCABLEWIDEBANDMIB.CcwbRFChannelTable.CcwbRFChannelEntry>`
            
            	**config**\: False
            
            .. attribute:: ccwbwbtorfbandwidth
            
            	The percentage of the RF channel bandwidth allocated for this wideband channel
            	**type**\: int
            
            	**range:** 1..100
            
            	**config**\: False
            
            	**units**\: percent
            
            .. attribute:: ccwbwbtorfstoragetype
            
            	The storage type for this conceptual row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            	**config**\: False
            
            .. attribute:: ccwbwbtorfrowstatus
            
            	Controls and reflects the status of rows in this table. It can be used for creating and deleting entries in this table.  The ccwbWBtoRFBandwidth must be valid for a row to be created. When ccwbWBtoRFRowStatus is 'active', the object ccwbWBtoRFBandwidth can be modified
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-CABLE-WIDEBAND-MIB'
            _revision = '2011-01-05'

            def __init__(self):
                super(CISCOCABLEWIDEBANDMIB.CcwbWBtoRFMappingTable.CcwbWBtoRFMappingEntry, self).__init__()

                self.yang_name = "ccwbWBtoRFMappingEntry"
                self.yang_parent_name = "ccwbWBtoRFMappingTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','entphysicalindex','ccwbrfchannelnum']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('entphysicalindex', (YLeaf(YType.str, 'entPhysicalIndex'), ['int'])),
                    ('ccwbrfchannelnum', (YLeaf(YType.str, 'ccwbRFChannelNum'), ['int'])),
                    ('ccwbwbtorfbandwidth', (YLeaf(YType.uint32, 'ccwbWBtoRFBandwidth'), ['int'])),
                    ('ccwbwbtorfstoragetype', (YLeaf(YType.enumeration, 'ccwbWBtoRFStorageType'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                    ('ccwbwbtorfrowstatus', (YLeaf(YType.enumeration, 'ccwbWBtoRFRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.ifindex = None
                self.entphysicalindex = None
                self.ccwbrfchannelnum = None
                self.ccwbwbtorfbandwidth = None
                self.ccwbwbtorfstoragetype = None
                self.ccwbwbtorfrowstatus = None
                self._segment_path = lambda: "ccwbWBtoRFMappingEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']" + "[ccwbRFChannelNum='" + str(self.ccwbrfchannelnum) + "']"
                self._absolute_path = lambda: "CISCO-CABLE-WIDEBAND-MIB:CISCO-CABLE-WIDEBAND-MIB/ccwbWBtoRFMappingTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCABLEWIDEBANDMIB.CcwbWBtoRFMappingTable.CcwbWBtoRFMappingEntry, ['ifindex', 'entphysicalindex', 'ccwbrfchannelnum', 'ccwbwbtorfbandwidth', 'ccwbwbtorfstoragetype', 'ccwbwbtorfrowstatus'], name, value)




    class CcwbWBtoNBMappingTable(Entity):
        """
        This table contains information of the mapping
        of the wideband channels to the Narrowband channels
        that are available on the WCMTS.
        
        The wideband protocol utilizes the existing narrowband
        downstream channel for carrying the MAC management and
        signaling messages and the associated narrowband upstream
        for return data traffic and signaling.
        
        .. attribute:: ccwbwbtonbmappingentry
        
        	An entry provides a list of attributes for a association between a wideband channel and a narrowband channel.  An entry in this table exists for each association between a wideband channel and narrowband channel on the WCMTS. The valid ifType for the ifIndex used here is, ciscoDocsCableWBDownstream(224)
        	**type**\: list of  		 :py:class:`CcwbWBtoNBMappingEntry <ydk.models.cisco_ios_xe.CISCO_CABLE_WIDEBAND_MIB.CISCOCABLEWIDEBANDMIB.CcwbWBtoNBMappingTable.CcwbWBtoNBMappingEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-CABLE-WIDEBAND-MIB'
        _revision = '2011-01-05'

        def __init__(self):
            super(CISCOCABLEWIDEBANDMIB.CcwbWBtoNBMappingTable, self).__init__()

            self.yang_name = "ccwbWBtoNBMappingTable"
            self.yang_parent_name = "CISCO-CABLE-WIDEBAND-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ccwbWBtoNBMappingEntry", ("ccwbwbtonbmappingentry", CISCOCABLEWIDEBANDMIB.CcwbWBtoNBMappingTable.CcwbWBtoNBMappingEntry))])
            self._leafs = OrderedDict()

            self.ccwbwbtonbmappingentry = YList(self)
            self._segment_path = lambda: "ccwbWBtoNBMappingTable"
            self._absolute_path = lambda: "CISCO-CABLE-WIDEBAND-MIB:CISCO-CABLE-WIDEBAND-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCABLEWIDEBANDMIB.CcwbWBtoNBMappingTable, [], name, value)


        class CcwbWBtoNBMappingEntry(Entity):
            """
            An entry provides a list of attributes for a
            association between a wideband channel and a narrowband
            channel.
            
            An entry in this table exists for each association
            between a wideband channel and narrowband channel on the
            WCMTS. The valid ifType for the ifIndex used here is,
            ciscoDocsCableWBDownstream(224).
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: ccwbwbtonbifindexfornb  (key)
            
            	The ifIndex of the narrowband cable interface associated with this wideband channel
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: ccwbwbtonbstoragetype
            
            	The storage type for this conceptual row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            	**config**\: False
            
            .. attribute:: ccwbwbtonbrowstatus
            
            	Controls and reflects the status of rows in this table. It can be used for creating and deleting entries in this table. The object ccwbWBtoNBifIndexForNB must be valid in order for row to be created
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-CABLE-WIDEBAND-MIB'
            _revision = '2011-01-05'

            def __init__(self):
                super(CISCOCABLEWIDEBANDMIB.CcwbWBtoNBMappingTable.CcwbWBtoNBMappingEntry, self).__init__()

                self.yang_name = "ccwbWBtoNBMappingEntry"
                self.yang_parent_name = "ccwbWBtoNBMappingTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','ccwbwbtonbifindexfornb']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('ccwbwbtonbifindexfornb', (YLeaf(YType.int32, 'ccwbWBtoNBifIndexForNB'), ['int'])),
                    ('ccwbwbtonbstoragetype', (YLeaf(YType.enumeration, 'ccwbWBtoNBStorageType'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                    ('ccwbwbtonbrowstatus', (YLeaf(YType.enumeration, 'ccwbWBtoNBRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.ifindex = None
                self.ccwbwbtonbifindexfornb = None
                self.ccwbwbtonbstoragetype = None
                self.ccwbwbtonbrowstatus = None
                self._segment_path = lambda: "ccwbWBtoNBMappingEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[ccwbWBtoNBifIndexForNB='" + str(self.ccwbwbtonbifindexfornb) + "']"
                self._absolute_path = lambda: "CISCO-CABLE-WIDEBAND-MIB:CISCO-CABLE-WIDEBAND-MIB/ccwbWBtoNBMappingTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCABLEWIDEBANDMIB.CcwbWBtoNBMappingTable.CcwbWBtoNBMappingEntry, ['ifindex', 'ccwbwbtonbifindexfornb', 'ccwbwbtonbstoragetype', 'ccwbwbtonbrowstatus'], name, value)




    class CcwbWBBondGrpTable(Entity):
        """
        This table provides information about a
        Wideband BG interface, whether its configured
        to carry multicast or non\-multicast traffic.
        For multicast the BG interface type is
        Secondary and for non\-multicast its non\-Secondary.
        Other objects could be added to this later in
        the future.
        
        .. attribute:: ccwbwbbondgrpentry
        
        	An entry in this table provides information about each Wideband BG interface whose ifType is ciscoDocsCableWBDownstream(224)
        	**type**\: list of  		 :py:class:`CcwbWBBondGrpEntry <ydk.models.cisco_ios_xe.CISCO_CABLE_WIDEBAND_MIB.CISCOCABLEWIDEBANDMIB.CcwbWBBondGrpTable.CcwbWBBondGrpEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-CABLE-WIDEBAND-MIB'
        _revision = '2011-01-05'

        def __init__(self):
            super(CISCOCABLEWIDEBANDMIB.CcwbWBBondGrpTable, self).__init__()

            self.yang_name = "ccwbWBBondGrpTable"
            self.yang_parent_name = "CISCO-CABLE-WIDEBAND-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ccwbWBBondGrpEntry", ("ccwbwbbondgrpentry", CISCOCABLEWIDEBANDMIB.CcwbWBBondGrpTable.CcwbWBBondGrpEntry))])
            self._leafs = OrderedDict()

            self.ccwbwbbondgrpentry = YList(self)
            self._segment_path = lambda: "ccwbWBBondGrpTable"
            self._absolute_path = lambda: "CISCO-CABLE-WIDEBAND-MIB:CISCO-CABLE-WIDEBAND-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCABLEWIDEBANDMIB.CcwbWBBondGrpTable, [], name, value)


        class CcwbWBBondGrpEntry(Entity):
            """
            An entry in this table provides information
            about each Wideband BG interface whose ifType is
            ciscoDocsCableWBDownstream(224).
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: ccwbwbbondgrpsecondary
            
            	This object has the value 'true(1)' if the WB interface(BG) is Seconday and the value 'false(2)' for non\-Secondary
            	**type**\: bool
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-CABLE-WIDEBAND-MIB'
            _revision = '2011-01-05'

            def __init__(self):
                super(CISCOCABLEWIDEBANDMIB.CcwbWBBondGrpTable.CcwbWBBondGrpEntry, self).__init__()

                self.yang_name = "ccwbWBBondGrpEntry"
                self.yang_parent_name = "ccwbWBBondGrpTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('ccwbwbbondgrpsecondary', (YLeaf(YType.boolean, 'ccwbWBBondGrpSecondary'), ['bool'])),
                ])
                self.ifindex = None
                self.ccwbwbbondgrpsecondary = None
                self._segment_path = lambda: "ccwbWBBondGrpEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-CABLE-WIDEBAND-MIB:CISCO-CABLE-WIDEBAND-MIB/ccwbWBBondGrpTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCABLEWIDEBANDMIB.CcwbWBBondGrpTable.CcwbWBBondGrpEntry, ['ifindex', 'ccwbwbbondgrpsecondary'], name, value)




    class CcwbWBCmStatusTable(Entity):
        """
        This table contains Wideband Cable Modem(WCM) connectivity state.
        A WCM connectivity state can be associated with multiple
        Wideband interfaces.
        
        .. attribute:: ccwbwbcmstatusentry
        
        	Status information for a single Wideband Cable Modem. An entry in this table exists for each Wideband Cable Modem that is connected to the WCMTS
        	**type**\: list of  		 :py:class:`CcwbWBCmStatusEntry <ydk.models.cisco_ios_xe.CISCO_CABLE_WIDEBAND_MIB.CISCOCABLEWIDEBANDMIB.CcwbWBCmStatusTable.CcwbWBCmStatusEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-CABLE-WIDEBAND-MIB'
        _revision = '2011-01-05'

        def __init__(self):
            super(CISCOCABLEWIDEBANDMIB.CcwbWBCmStatusTable, self).__init__()

            self.yang_name = "ccwbWBCmStatusTable"
            self.yang_parent_name = "CISCO-CABLE-WIDEBAND-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ccwbWBCmStatusEntry", ("ccwbwbcmstatusentry", CISCOCABLEWIDEBANDMIB.CcwbWBCmStatusTable.CcwbWBCmStatusEntry))])
            self._leafs = OrderedDict()

            self.ccwbwbcmstatusentry = YList(self)
            self._segment_path = lambda: "ccwbWBCmStatusTable"
            self._absolute_path = lambda: "CISCO-CABLE-WIDEBAND-MIB:CISCO-CABLE-WIDEBAND-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCABLEWIDEBANDMIB.CcwbWBCmStatusTable, [], name, value)


        class CcwbWBCmStatusEntry(Entity):
            """
            Status information for a single Wideband Cable Modem.
            An entry in this table exists for each Wideband Cable Modem
            that is connected to the WCMTS.
            
            .. attribute:: docsifcmtscmstatusindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`docsifcmtscmstatusindex <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmtsCmStatusTable.DocsIfCmtsCmStatusEntry>`
            
            	**config**\: False
            
            .. attribute:: ccwbwbcmstatusvalue
            
            	Current WB Cable Modem connectivity state, as specified in the RF Interface Specification. Returned status information is the WCM status as assumed by the WCMTS, and indicates the following events\:  The enumerations are\: offline(1)                \: modem considered offline. others(2)                 \: states is in                             ccwbWBCmStatusValue. initRangingRcvd(3)        \: modem sent initial ranging. initDhcpReqRcvd(4)        \: dhcp request received. onlineNetAccessDisabled(5)\: modem registered, but network                             access for the WCM is disabled. onlineKekAssigned(6)      \: modem registered, BPI enabled                             and KEK assigned. onlineTekAssigned(7)      \: modem registered, BPI enabled                             and TEK assigned. rejectBadMic(8)           \: modem did attempt to register                             but registration was refused                             due to bad mic. rejectBadCos(9)           \: modem did attempt to register                             but registration was refused                             due to bad COS. kekRejected(10)           \: KEK modem key assignment                             rejected. tekRejected(11)           \: TEK modem key assignment                             rejected. online(12)                \: modem registered, enabled for                             data. initTftpPacketRcvd(13)    \: tftp packet received and option                             file transfer started. initTodRquestRcvd(14)     \: Time of the Day (TOD) request                             received. reset(15)                 \: modem is resetting. rangingInProgress(16)     \: initial ranging is in progress. dhcpGotIpAddr(17)         \: modem has got an IP address rejStaleConfig(18)        \: modem did attempt to register                             but registration was refused                             due to stale Config. rejIpSpoof(19)            \: modem did attempt to register                             but registration was refused                             due to IP Spoof. rejClassFail(20)          \: modem did attempt to register                             but registration was refused                             due to Class failure. rejRegNack(21)            \: modem did attempt to register                             but no acknowledgement was                             received. bpiKekExpired(22)         \: KEK modem key assignment                             expired. bpiTekExpired(23)         \: TEK modem key assignment                             expired. shutdown(24)              \: modem is in shutdown state. channelChgInitRangingRcvd(25)  \: modem sent initial ranging                                   during channel change. channelChgRangingInProgress(26) \: initial ranging is in                                   progress during channel                                   change. wbOnline(27)               \: Wideband modem is online. wbOnlinePrivacy(28)        \: Wideband modem is online Privacy                              enabled. wbOnlineKekAssigned(29)    \: Wideband modem is online                              and KEK assigned. wbOnlineTekAssigned(30)    \: Wideband modem is online                              and TEK assigned. wbOnlineNetAccessDis(31)   \: Wideband modem registered but                              Network access disabled. wbKekReject(32)            \: KEK wideband modem key assignment                              rejected. wbTekReject(33)            \: TEK wideband modem key assignment                              rejected. wbNetAccessDisReject(34)   \: wideband modem rejected \-                              Net access disabled. wbPrivacyEnabReject(35)    \: wideband modem rejected                              Privacy enabled. wbKekExpire(36)            \: KEK Wideband modem key assignment                              expired. wbTekExpire(37)            \: TEK wideband modem key assignment                              rejected. wbNetAccessDisExpire(38)   \: wideband modem expire \- Network                              access disabled. wbPrivacyEnabExpire(39)    \: wideband modem expire \- Privacy                              enabled.   This ccwbWBCmStatusValue could return initRangingRcvd(3) or rangingInProgress(16) when the ccwbWBCmStatusValue is ranging(2).  This ccwbWBCmStatusValue will return others(2) when the ccwbWBCmStatusValue states is either rangingAborted(3), rangingComplete(4), and ipComplete(5).  This ccwbWBCmStatusValue could return wbonline(27), or onlineNetAccessDisabled(5) for WCM with BPI disabled, or onlineNetAccessDisabled(5) or onlineTekAssigned(7) for WCM with BPI enabled, when the ccwbWBCmStatusValue is registrationComplete(6).  This ccwbWBCmStatusValue could return either rejectBadMic(8), rejectBadCos(9) rejStaleConfig(19) or rejRegNack(22) when the ccwbWBCmStatusValue is accessDenied(7) for possible reasons of cable modem registration abort.  This ccwbWBCmStatusValue could return either onlineKekAssigned(6), kekRejected(10), tekRejected(11), or online(12) for the WCM with BPI enabled when the ccwbWBCmStatusValue is registeredBPIInitializing(9).  The state rejectBadCos(9) is not applicable for DOCSIS1.1 modems. The WCMTS only needs to report states it is able to detect
            	**type**\:  :py:class:`CcwbWBCmStatusValue <ydk.models.cisco_ios_xe.CISCO_CABLE_WIDEBAND_MIB.CISCOCABLEWIDEBANDMIB.CcwbWBCmStatusTable.CcwbWBCmStatusEntry.CcwbWBCmStatusValue>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-CABLE-WIDEBAND-MIB'
            _revision = '2011-01-05'

            def __init__(self):
                super(CISCOCABLEWIDEBANDMIB.CcwbWBCmStatusTable.CcwbWBCmStatusEntry, self).__init__()

                self.yang_name = "ccwbWBCmStatusEntry"
                self.yang_parent_name = "ccwbWBCmStatusTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['docsifcmtscmstatusindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('docsifcmtscmstatusindex', (YLeaf(YType.str, 'docsIfCmtsCmStatusIndex'), ['int'])),
                    ('ccwbwbcmstatusvalue', (YLeaf(YType.enumeration, 'ccwbWBCmStatusValue'), [('ydk.models.cisco_ios_xe.CISCO_CABLE_WIDEBAND_MIB', 'CISCOCABLEWIDEBANDMIB', 'CcwbWBCmStatusTable.CcwbWBCmStatusEntry.CcwbWBCmStatusValue')])),
                ])
                self.docsifcmtscmstatusindex = None
                self.ccwbwbcmstatusvalue = None
                self._segment_path = lambda: "ccwbWBCmStatusEntry" + "[docsIfCmtsCmStatusIndex='" + str(self.docsifcmtscmstatusindex) + "']"
                self._absolute_path = lambda: "CISCO-CABLE-WIDEBAND-MIB:CISCO-CABLE-WIDEBAND-MIB/ccwbWBCmStatusTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCABLEWIDEBANDMIB.CcwbWBCmStatusTable.CcwbWBCmStatusEntry, ['docsifcmtscmstatusindex', 'ccwbwbcmstatusvalue'], name, value)

            class CcwbWBCmStatusValue(Enum):
                """
                CcwbWBCmStatusValue (Enum Class)

                Current WB Cable Modem connectivity state, as specified

                in the RF Interface Specification. Returned status

                information is the WCM status as assumed by the WCMTS,

                and indicates the following events\:

                The enumerations are\:

                offline(1)                \: modem considered offline.

                others(2)                 \: states is in

                                            ccwbWBCmStatusValue.

                initRangingRcvd(3)        \: modem sent initial ranging.

                initDhcpReqRcvd(4)        \: dhcp request received.

                onlineNetAccessDisabled(5)\: modem registered, but network

                                            access for the WCM is disabled.

                onlineKekAssigned(6)      \: modem registered, BPI enabled

                                            and KEK assigned.

                onlineTekAssigned(7)      \: modem registered, BPI enabled

                                            and TEK assigned.

                rejectBadMic(8)           \: modem did attempt to register

                                            but registration was refused

                                            due to bad mic.

                rejectBadCos(9)           \: modem did attempt to register

                                            but registration was refused

                                            due to bad COS.

                kekRejected(10)           \: KEK modem key assignment

                                            rejected.

                tekRejected(11)           \: TEK modem key assignment

                                            rejected.

                online(12)                \: modem registered, enabled for

                                            data.

                initTftpPacketRcvd(13)    \: tftp packet received and option

                                            file transfer started.

                initTodRquestRcvd(14)     \: Time of the Day (TOD) request

                                            received.

                reset(15)                 \: modem is resetting.

                rangingInProgress(16)     \: initial ranging is in progress.

                dhcpGotIpAddr(17)         \: modem has got an IP address

                rejStaleConfig(18)        \: modem did attempt to register

                                            but registration was refused

                                            due to stale Config.

                rejIpSpoof(19)            \: modem did attempt to register

                                            but registration was refused

                                            due to IP Spoof.

                rejClassFail(20)          \: modem did attempt to register

                                            but registration was refused

                                            due to Class failure.

                rejRegNack(21)            \: modem did attempt to register

                                            but no acknowledgement was

                                            received.

                bpiKekExpired(22)         \: KEK modem key assignment

                                            expired.

                bpiTekExpired(23)         \: TEK modem key assignment

                                            expired.

                shutdown(24)              \: modem is in shutdown state.

                channelChgInitRangingRcvd(25)  \: modem sent initial ranging

                                                  during channel change.

                channelChgRangingInProgress(26) \: initial ranging is in

                                                  progress during channel

                                                  change.

                wbOnline(27)               \: Wideband modem is online.

                wbOnlinePrivacy(28)        \: Wideband modem is online Privacy

                                             enabled.

                wbOnlineKekAssigned(29)    \: Wideband modem is online

                                             and KEK assigned.

                wbOnlineTekAssigned(30)    \: Wideband modem is online

                                             and TEK assigned.

                wbOnlineNetAccessDis(31)   \: Wideband modem registered but

                                             Network access disabled.

                wbKekReject(32)            \: KEK wideband modem key assignment

                                             rejected.

                wbTekReject(33)            \: TEK wideband modem key assignment

                                             rejected.

                wbNetAccessDisReject(34)   \: wideband modem rejected \-

                                             Net access disabled.

                wbPrivacyEnabReject(35)    \: wideband modem rejected

                                             Privacy enabled.

                wbKekExpire(36)            \: KEK Wideband modem key assignment

                                             expired.

                wbTekExpire(37)            \: TEK wideband modem key assignment

                                             rejected.

                wbNetAccessDisExpire(38)   \: wideband modem expire \- Network

                                             access disabled.

                wbPrivacyEnabExpire(39)    \: wideband modem expire \- Privacy

                                             enabled.

                This ccwbWBCmStatusValue could return initRangingRcvd(3)

                or rangingInProgress(16) when the ccwbWBCmStatusValue

                is ranging(2).

                This ccwbWBCmStatusValue will return others(2) when the

                ccwbWBCmStatusValue states is either rangingAborted(3),

                rangingComplete(4), and ipComplete(5).

                This ccwbWBCmStatusValue could return wbonline(27), or

                onlineNetAccessDisabled(5) for WCM with BPI disabled, or

                onlineNetAccessDisabled(5) or onlineTekAssigned(7) for

                WCM with BPI enabled, when the ccwbWBCmStatusValue

                is registrationComplete(6).

                This ccwbWBCmStatusValue could return either rejectBadMic(8),

                rejectBadCos(9) rejStaleConfig(19) or rejRegNack(22) when

                the ccwbWBCmStatusValue is accessDenied(7) for possible

                reasons of cable modem registration abort.

                This ccwbWBCmStatusValue could return either onlineKekAssigned(6),

                kekRejected(10), tekRejected(11), or online(12) for the WCM with

                BPI enabled when the ccwbWBCmStatusValue is

                registeredBPIInitializing(9).

                The state rejectBadCos(9) is not applicable for DOCSIS1.1 modems.

                The WCMTS only needs to report states it is able to detect.

                .. data:: offline = 1

                .. data:: others = 2

                .. data:: initRangingRcvd = 3

                .. data:: initDhcpReqRcvd = 4

                .. data:: onlineNetAccessDisabled = 5

                .. data:: onlineKekAssigned = 6

                .. data:: onlineTekAssigned = 7

                .. data:: rejectBadMic = 8

                .. data:: rejectBadCos = 9

                .. data:: kekRejected = 10

                .. data:: tekRejected = 11

                .. data:: online = 12

                .. data:: initTftpPacketRcvd = 13

                .. data:: initTodRequestRcvd = 14

                .. data:: reset = 15

                .. data:: rangingInProgress = 16

                .. data:: dhcpGotIpAddr = 17

                .. data:: rejStaleConfig = 18

                .. data:: rejIpSpoof = 19

                .. data:: rejClassFail = 20

                .. data:: rejRegNack = 21

                .. data:: bpiKekExpired = 22

                .. data:: bpiTekExpired = 23

                .. data:: shutdown = 24

                .. data:: channelChgInitRangingRcvd = 25

                .. data:: channelChgRangingInProgress = 26

                .. data:: wbOnline = 27

                .. data:: wbOnlinePrivacy = 28

                .. data:: wbOnlineKekAssigned = 29

                .. data:: wbOnlineTekAssigned = 30

                .. data:: wbOnlineNetAccessDis = 31

                .. data:: wbKekReject = 32

                .. data:: wbTekReject = 33

                .. data:: wbNetAccessDisReject = 34

                .. data:: wbPrivacyEnabReject = 35

                .. data:: wbKekExpire = 36

                .. data:: wbTekExpire = 37

                .. data:: wbNetAccessDisExpire = 38

                .. data:: wbPrivacyEnabExpire = 39

                """

                offline = Enum.YLeaf(1, "offline")

                others = Enum.YLeaf(2, "others")

                initRangingRcvd = Enum.YLeaf(3, "initRangingRcvd")

                initDhcpReqRcvd = Enum.YLeaf(4, "initDhcpReqRcvd")

                onlineNetAccessDisabled = Enum.YLeaf(5, "onlineNetAccessDisabled")

                onlineKekAssigned = Enum.YLeaf(6, "onlineKekAssigned")

                onlineTekAssigned = Enum.YLeaf(7, "onlineTekAssigned")

                rejectBadMic = Enum.YLeaf(8, "rejectBadMic")

                rejectBadCos = Enum.YLeaf(9, "rejectBadCos")

                kekRejected = Enum.YLeaf(10, "kekRejected")

                tekRejected = Enum.YLeaf(11, "tekRejected")

                online = Enum.YLeaf(12, "online")

                initTftpPacketRcvd = Enum.YLeaf(13, "initTftpPacketRcvd")

                initTodRequestRcvd = Enum.YLeaf(14, "initTodRequestRcvd")

                reset = Enum.YLeaf(15, "reset")

                rangingInProgress = Enum.YLeaf(16, "rangingInProgress")

                dhcpGotIpAddr = Enum.YLeaf(17, "dhcpGotIpAddr")

                rejStaleConfig = Enum.YLeaf(18, "rejStaleConfig")

                rejIpSpoof = Enum.YLeaf(19, "rejIpSpoof")

                rejClassFail = Enum.YLeaf(20, "rejClassFail")

                rejRegNack = Enum.YLeaf(21, "rejRegNack")

                bpiKekExpired = Enum.YLeaf(22, "bpiKekExpired")

                bpiTekExpired = Enum.YLeaf(23, "bpiTekExpired")

                shutdown = Enum.YLeaf(24, "shutdown")

                channelChgInitRangingRcvd = Enum.YLeaf(25, "channelChgInitRangingRcvd")

                channelChgRangingInProgress = Enum.YLeaf(26, "channelChgRangingInProgress")

                wbOnline = Enum.YLeaf(27, "wbOnline")

                wbOnlinePrivacy = Enum.YLeaf(28, "wbOnlinePrivacy")

                wbOnlineKekAssigned = Enum.YLeaf(29, "wbOnlineKekAssigned")

                wbOnlineTekAssigned = Enum.YLeaf(30, "wbOnlineTekAssigned")

                wbOnlineNetAccessDis = Enum.YLeaf(31, "wbOnlineNetAccessDis")

                wbKekReject = Enum.YLeaf(32, "wbKekReject")

                wbTekReject = Enum.YLeaf(33, "wbTekReject")

                wbNetAccessDisReject = Enum.YLeaf(34, "wbNetAccessDisReject")

                wbPrivacyEnabReject = Enum.YLeaf(35, "wbPrivacyEnabReject")

                wbKekExpire = Enum.YLeaf(36, "wbKekExpire")

                wbTekExpire = Enum.YLeaf(37, "wbTekExpire")

                wbNetAccessDisExpire = Enum.YLeaf(38, "wbNetAccessDisExpire")

                wbPrivacyEnabExpire = Enum.YLeaf(39, "wbPrivacyEnabExpire")





    class CcwbWBCmStatusExtTable(Entity):
        """
        An entry in this table exists for each Wideband
        Cable Modem which links to one or more WB interface.
        
        .. attribute:: ccwbwbcmstatusextentry
        
        	This entry exists for each Wideband Cable Modem(WCM) which links to one or more WB interface
        	**type**\: list of  		 :py:class:`CcwbWBCmStatusExtEntry <ydk.models.cisco_ios_xe.CISCO_CABLE_WIDEBAND_MIB.CISCOCABLEWIDEBANDMIB.CcwbWBCmStatusExtTable.CcwbWBCmStatusExtEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-CABLE-WIDEBAND-MIB'
        _revision = '2011-01-05'

        def __init__(self):
            super(CISCOCABLEWIDEBANDMIB.CcwbWBCmStatusExtTable, self).__init__()

            self.yang_name = "ccwbWBCmStatusExtTable"
            self.yang_parent_name = "CISCO-CABLE-WIDEBAND-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ccwbWBCmStatusExtEntry", ("ccwbwbcmstatusextentry", CISCOCABLEWIDEBANDMIB.CcwbWBCmStatusExtTable.CcwbWBCmStatusExtEntry))])
            self._leafs = OrderedDict()

            self.ccwbwbcmstatusextentry = YList(self)
            self._segment_path = lambda: "ccwbWBCmStatusExtTable"
            self._absolute_path = lambda: "CISCO-CABLE-WIDEBAND-MIB:CISCO-CABLE-WIDEBAND-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCABLEWIDEBANDMIB.CcwbWBCmStatusExtTable, [], name, value)


        class CcwbWBCmStatusExtEntry(Entity):
            """
            This entry exists for each Wideband Cable Modem(WCM)
            which links to one or more WB interface.
            
            .. attribute:: docsifcmtscmstatusindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`docsifcmtscmstatusindex <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmtsCmStatusTable.DocsIfCmtsCmStatusEntry>`
            
            	**config**\: False
            
            .. attribute:: ccwbwbcmstatusextindex  (key)
            
            	The value of this object uniquely identifies an association between a WCM and a BG
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: ccwbwbcmwbifindex
            
            	ifIndex of the wideband channel associated with the WCM
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-CABLE-WIDEBAND-MIB'
            _revision = '2011-01-05'

            def __init__(self):
                super(CISCOCABLEWIDEBANDMIB.CcwbWBCmStatusExtTable.CcwbWBCmStatusExtEntry, self).__init__()

                self.yang_name = "ccwbWBCmStatusExtEntry"
                self.yang_parent_name = "ccwbWBCmStatusExtTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['docsifcmtscmstatusindex','ccwbwbcmstatusextindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('docsifcmtscmstatusindex', (YLeaf(YType.str, 'docsIfCmtsCmStatusIndex'), ['int'])),
                    ('ccwbwbcmstatusextindex', (YLeaf(YType.int32, 'ccwbWBCmStatusExtIndex'), ['int'])),
                    ('ccwbwbcmwbifindex', (YLeaf(YType.int32, 'ccwbWBCmWBIfindex'), ['int'])),
                ])
                self.docsifcmtscmstatusindex = None
                self.ccwbwbcmstatusextindex = None
                self.ccwbwbcmwbifindex = None
                self._segment_path = lambda: "ccwbWBCmStatusExtEntry" + "[docsIfCmtsCmStatusIndex='" + str(self.docsifcmtscmstatusindex) + "']" + "[ccwbWBCmStatusExtIndex='" + str(self.ccwbwbcmstatusextindex) + "']"
                self._absolute_path = lambda: "CISCO-CABLE-WIDEBAND-MIB:CISCO-CABLE-WIDEBAND-MIB/ccwbWBCmStatusExtTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCABLEWIDEBANDMIB.CcwbWBCmStatusExtTable.CcwbWBCmStatusExtEntry, ['docsifcmtscmstatusindex', 'ccwbwbcmstatusextindex', 'ccwbwbcmwbifindex'], name, value)




    class CcwbFiberNodeDescrTable(Entity):
        """
        This table contains the description of a Fiber Node
        on a CMTS. An entry in this table exists for each
        FiberNode ID.
        
        .. attribute:: ccwbfibernodedescrentry
        
        	This entry provides the description of each fiber node on the CMTS and it is part of the Fiber node configuration
        	**type**\: list of  		 :py:class:`CcwbFiberNodeDescrEntry <ydk.models.cisco_ios_xe.CISCO_CABLE_WIDEBAND_MIB.CISCOCABLEWIDEBANDMIB.CcwbFiberNodeDescrTable.CcwbFiberNodeDescrEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-CABLE-WIDEBAND-MIB'
        _revision = '2011-01-05'

        def __init__(self):
            super(CISCOCABLEWIDEBANDMIB.CcwbFiberNodeDescrTable, self).__init__()

            self.yang_name = "ccwbFiberNodeDescrTable"
            self.yang_parent_name = "CISCO-CABLE-WIDEBAND-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ccwbFiberNodeDescrEntry", ("ccwbfibernodedescrentry", CISCOCABLEWIDEBANDMIB.CcwbFiberNodeDescrTable.CcwbFiberNodeDescrEntry))])
            self._leafs = OrderedDict()

            self.ccwbfibernodedescrentry = YList(self)
            self._segment_path = lambda: "ccwbFiberNodeDescrTable"
            self._absolute_path = lambda: "CISCO-CABLE-WIDEBAND-MIB:CISCO-CABLE-WIDEBAND-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCABLEWIDEBANDMIB.CcwbFiberNodeDescrTable, [], name, value)


        class CcwbFiberNodeDescrEntry(Entity):
            """
            This entry provides the description of each fiber node
            on the CMTS and it is part of the Fiber node configuration.
            
            .. attribute:: ccwbfibernodeid  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..1000
            
            	**refers to**\:  :py:class:`ccwbfibernodeid <ydk.models.cisco_ios_xe.CISCO_CABLE_WIDEBAND_MIB.CISCOCABLEWIDEBANDMIB.CcwbFiberNodeTable.CcwbFiberNodeEntry>`
            
            	**config**\: False
            
            .. attribute:: ccwbfibernodedescription
            
            	This object contains the user configured description string of the fiber node
            	**type**\: str
            
            	**length:** 0..80
            
            	**config**\: False
            
            .. attribute:: ccwbfibernodedescrstoragetype
            
            	The storage type for this conceptual row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            	**config**\: False
            
            .. attribute:: ccwbfibernodedescrrowstatus
            
            	Controls and reflects the status of rows in this table. It can be used for creating and deleting entries in this table. ccwbFiberNodeDescription must not be null in order for row to be created
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-CABLE-WIDEBAND-MIB'
            _revision = '2011-01-05'

            def __init__(self):
                super(CISCOCABLEWIDEBANDMIB.CcwbFiberNodeDescrTable.CcwbFiberNodeDescrEntry, self).__init__()

                self.yang_name = "ccwbFiberNodeDescrEntry"
                self.yang_parent_name = "ccwbFiberNodeDescrTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ccwbfibernodeid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ccwbfibernodeid', (YLeaf(YType.str, 'ccwbFiberNodeID'), ['int'])),
                    ('ccwbfibernodedescription', (YLeaf(YType.str, 'ccwbFiberNodeDescription'), ['str'])),
                    ('ccwbfibernodedescrstoragetype', (YLeaf(YType.enumeration, 'ccwbFiberNodeDescrStorageType'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                    ('ccwbfibernodedescrrowstatus', (YLeaf(YType.enumeration, 'ccwbFiberNodeDescrRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.ccwbfibernodeid = None
                self.ccwbfibernodedescription = None
                self.ccwbfibernodedescrstoragetype = None
                self.ccwbfibernodedescrrowstatus = None
                self._segment_path = lambda: "ccwbFiberNodeDescrEntry" + "[ccwbFiberNodeID='" + str(self.ccwbfibernodeid) + "']"
                self._absolute_path = lambda: "CISCO-CABLE-WIDEBAND-MIB:CISCO-CABLE-WIDEBAND-MIB/ccwbFiberNodeDescrTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCABLEWIDEBANDMIB.CcwbFiberNodeDescrTable.CcwbFiberNodeDescrEntry, ['ccwbfibernodeid', 'ccwbfibernodedescription', 'ccwbfibernodedescrstoragetype', 'ccwbfibernodedescrrowstatus'], name, value)




    class CcwbFiberNodeTable(Entity):
        """
        This table provides configuration information of each Fiber node.
        It will provide topology information of each Fiber node, which
        includes information such as, Narrowband and Wideband QAMs.
        
        .. attribute:: ccwbfibernodeentry
        
        	An entry in this table exists for each FiberNode ID that is in use. It uses two indices, i.e. ccwbFiberNodeID which is the Fiber node ID, and ccwbFiberNodeGlobRFID, which is the combined bit mask of Narrowband RF channels and Wideband rf\-ports(rf\-channels)
        	**type**\: list of  		 :py:class:`CcwbFiberNodeEntry <ydk.models.cisco_ios_xe.CISCO_CABLE_WIDEBAND_MIB.CISCOCABLEWIDEBANDMIB.CcwbFiberNodeTable.CcwbFiberNodeEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-CABLE-WIDEBAND-MIB'
        _revision = '2011-01-05'

        def __init__(self):
            super(CISCOCABLEWIDEBANDMIB.CcwbFiberNodeTable, self).__init__()

            self.yang_name = "ccwbFiberNodeTable"
            self.yang_parent_name = "CISCO-CABLE-WIDEBAND-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ccwbFiberNodeEntry", ("ccwbfibernodeentry", CISCOCABLEWIDEBANDMIB.CcwbFiberNodeTable.CcwbFiberNodeEntry))])
            self._leafs = OrderedDict()

            self.ccwbfibernodeentry = YList(self)
            self._segment_path = lambda: "ccwbFiberNodeTable"
            self._absolute_path = lambda: "CISCO-CABLE-WIDEBAND-MIB:CISCO-CABLE-WIDEBAND-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCABLEWIDEBANDMIB.CcwbFiberNodeTable, [], name, value)


        class CcwbFiberNodeEntry(Entity):
            """
            An entry in this table exists for each FiberNode ID that is in use.
            It uses two indices, i.e. ccwbFiberNodeID which is the
            Fiber node ID, and ccwbFiberNodeGlobRFID, which is the combined
            bit mask of Narrowband RF channels and Wideband
            rf\-ports(rf\-channels).
            
            .. attribute:: ccwbfibernodeid  (key)
            
            	This object represents the Fiber node ID. Each Fiber node configuration on the CMTS is assigned a unique Fiber node ID
            	**type**\: int
            
            	**range:** 1..1000
            
            	**config**\: False
            
            .. attribute:: ccwbfibernodeglobrfid  (key)
            
            	This is the RF ID of both Narrowband and Wideband QAMs(rf\-channels) combined
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ccwbfibernodenbifindx
            
            	This object represents the Narrowband Ifindex of the  RF downstream channel which is part of the Fiber node configuation
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: ccwbfibernodewbcontlrphyindx
            
            	This object represents the entity physical index of Wideband controller card. This card contains the RF port which is part of the ccwbFiberNodeGlobRFID bit mask. A value of zero means the index is invalid. ccwbFiberNodeWBRFPort and ccwbFiberNodeWBContlrPhyIndx are mutually inclusive
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: ccwbfibernodewbrfport
            
            	This object represents the RF downstream channel IDs (rf\-ports) of the wideband controller card. Each Wideband controller can have 24 RF channels. ccwbFiberNodeWBRFPort and ccwbFiberNodeWBContlrPhyIndx are mutually inclusive
            	**type**\: int
            
            	**range:** 0..1024
            
            	**config**\: False
            
            .. attribute:: ccwbfibernodestoragetype
            
            	The storage type for this conceptual row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            	**config**\: False
            
            .. attribute:: ccwbfibernoderowstatus
            
            	Controls and reflects the status of rows in this table. It can be used for creating and deleting entries in this table
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-CABLE-WIDEBAND-MIB'
            _revision = '2011-01-05'

            def __init__(self):
                super(CISCOCABLEWIDEBANDMIB.CcwbFiberNodeTable.CcwbFiberNodeEntry, self).__init__()

                self.yang_name = "ccwbFiberNodeEntry"
                self.yang_parent_name = "ccwbFiberNodeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ccwbfibernodeid','ccwbfibernodeglobrfid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ccwbfibernodeid', (YLeaf(YType.uint32, 'ccwbFiberNodeID'), ['int'])),
                    ('ccwbfibernodeglobrfid', (YLeaf(YType.uint32, 'ccwbFiberNodeGlobRFID'), ['int'])),
                    ('ccwbfibernodenbifindx', (YLeaf(YType.int32, 'ccwbFiberNodeNBIfIndx'), ['int'])),
                    ('ccwbfibernodewbcontlrphyindx', (YLeaf(YType.int32, 'ccwbFiberNodeWBContlrPhyIndx'), ['int'])),
                    ('ccwbfibernodewbrfport', (YLeaf(YType.int32, 'ccwbFiberNodeWBRFPort'), ['int'])),
                    ('ccwbfibernodestoragetype', (YLeaf(YType.enumeration, 'ccwbFiberNodeStorageType'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                    ('ccwbfibernoderowstatus', (YLeaf(YType.enumeration, 'ccwbFiberNodeRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.ccwbfibernodeid = None
                self.ccwbfibernodeglobrfid = None
                self.ccwbfibernodenbifindx = None
                self.ccwbfibernodewbcontlrphyindx = None
                self.ccwbfibernodewbrfport = None
                self.ccwbfibernodestoragetype = None
                self.ccwbfibernoderowstatus = None
                self._segment_path = lambda: "ccwbFiberNodeEntry" + "[ccwbFiberNodeID='" + str(self.ccwbfibernodeid) + "']" + "[ccwbFiberNodeGlobRFID='" + str(self.ccwbfibernodeglobrfid) + "']"
                self._absolute_path = lambda: "CISCO-CABLE-WIDEBAND-MIB:CISCO-CABLE-WIDEBAND-MIB/ccwbFiberNodeTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCABLEWIDEBANDMIB.CcwbFiberNodeTable.CcwbFiberNodeEntry, ['ccwbfibernodeid', 'ccwbfibernodeglobrfid', 'ccwbfibernodenbifindx', 'ccwbfibernodewbcontlrphyindx', 'ccwbfibernodewbrfport', 'ccwbfibernodestoragetype', 'ccwbfibernoderowstatus'], name, value)



    def clone_ptr(self):
        self._top_entity = CISCOCABLEWIDEBANDMIB()
        return self._top_entity




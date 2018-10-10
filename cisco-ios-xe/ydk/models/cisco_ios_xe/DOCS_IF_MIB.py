""" DOCS_IF_MIB 

This is the MIB Module for DOCSIS 2.0 compliant Radio
Frequency (RF) interfaces in Cable Modems (CM) and
Cable Modem Termination Systems (CMTS).

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class DocsisQosVersion(Enum):
    """
    DocsisQosVersion (Enum Class)

    Indicates the quality of service level.

    .. data:: docsis10 = 1

    .. data:: docsis11 = 2

    """

    docsis10 = Enum.YLeaf(1, "docsis10")

    docsis11 = Enum.YLeaf(2, "docsis11")


class DocsisUpstreamType(Enum):
    """
    DocsisUpstreamType (Enum Class)

    Indicates the DOCSIS Upstream Channel Type.

    .. data:: unknown = 0

    .. data:: tdma = 1

    .. data:: atdma = 2

    .. data:: scdma = 3

    .. data:: tdmaAndAtdma = 4

    """

    unknown = Enum.YLeaf(0, "unknown")

    tdma = Enum.YLeaf(1, "tdma")

    atdma = Enum.YLeaf(2, "atdma")

    scdma = Enum.YLeaf(3, "scdma")

    tdmaAndAtdma = Enum.YLeaf(4, "tdmaAndAtdma")


class DocsisUpstreamTypeStatus(Enum):
    """
    DocsisUpstreamTypeStatus (Enum Class)

    Indicates the DOCSIS Upstream Channel Type Status. 

    The shared channel indicator type is not valid, since

    this type is used to specifically identify PHY mode.

    .. data:: unknown = 0

    .. data:: tdma = 1

    .. data:: atdma = 2

    .. data:: scdma = 3

    """

    unknown = Enum.YLeaf(0, "unknown")

    tdma = Enum.YLeaf(1, "tdma")

    atdma = Enum.YLeaf(2, "atdma")

    scdma = Enum.YLeaf(3, "scdma")


class DocsisVersion(Enum):
    """
    DocsisVersion (Enum Class)

    'docsis10' indicates DOCSIS 1.0.

    'docsis11' indicates DOCSIS 1.1.

    'docsis20' indicates DOCSIS 2.0.

    'docsis30' indicates DOCSIS 3.0.

    .. data:: docsis10 = 1

    .. data:: docsis11 = 2

    .. data:: docsis20 = 3

    .. data:: docsis30 = 4

    """

    docsis10 = Enum.YLeaf(1, "docsis10")

    docsis11 = Enum.YLeaf(2, "docsis11")

    docsis20 = Enum.YLeaf(3, "docsis20")

    docsis30 = Enum.YLeaf(4, "docsis30")



class DOCSIFMIB(Entity):
    """
    
    
    .. attribute:: docsifbaseobjects
    
    	
    	**type**\:  :py:class:`DocsIfBaseObjects <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfBaseObjects>`
    
    .. attribute:: docsifcmtsobjects
    
    	
    	**type**\:  :py:class:`DocsIfCmtsObjects <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmtsObjects>`
    
    .. attribute:: docsifdownstreamchanneltable
    
    	This table describes the attributes of downstream channels (frequency bands)
    	**type**\:  :py:class:`DocsIfDownstreamChannelTable <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfDownstreamChannelTable>`
    
    .. attribute:: docsifupstreamchanneltable
    
    	This table describes the attributes of attached upstream channels
    	**type**\:  :py:class:`DocsIfUpstreamChannelTable <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfUpstreamChannelTable>`
    
    .. attribute:: docsifqosprofiletable
    
    	Describes the attributes for each class of service
    	**type**\:  :py:class:`DocsIfQosProfileTable <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfQosProfileTable>`
    
    .. attribute:: docsifsignalqualitytable
    
    	At the CM, describes the PHY signal quality of downstream channels. At the CMTS, describes the PHY signal quality of upstream channels. At the CMTS, this table may exclude contention intervals
    	**type**\:  :py:class:`DocsIfSignalQualityTable <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfSignalQualityTable>`
    
    .. attribute:: docsifcmmactable
    
    	Describes the attributes of each CM MAC interface, extending the information available from ifEntry
    	**type**\:  :py:class:`DocsIfCmMacTable <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmMacTable>`
    
    .. attribute:: docsifcmstatustable
    
    	This table maintains a number of status objects and counters for Cable Modems
    	**type**\:  :py:class:`DocsIfCmStatusTable <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmStatusTable>`
    
    .. attribute:: docsifcmservicetable
    
    	Describes the attributes of each upstream service queue on a CM
    	**type**\:  :py:class:`DocsIfCmServiceTable <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmServiceTable>`
    
    .. attribute:: docsifcmtsmactable
    
    	Describes the attributes of each CMTS MAC interface, extending the information available from ifEntry. Mandatory for all CMTS devices
    	**type**\:  :py:class:`DocsIfCmtsMacTable <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmtsMacTable>`
    
    .. attribute:: docsifcmtsstatustable
    
    	For the MAC layer, this group maintains a number of status objects and counters
    	**type**\:  :py:class:`DocsIfCmtsStatusTable <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmtsStatusTable>`
    
    .. attribute:: docsifcmtscmstatustable
    
    	A set of objects in the CMTS, maintained for each Cable Modem connected to this CMTS
    	**type**\:  :py:class:`DocsIfCmtsCmStatusTable <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmtsCmStatusTable>`
    
    .. attribute:: docsifcmtsservicetable
    
    	Describes the attributes of upstream service queues in a Cable Modem Termination System
    	**type**\:  :py:class:`DocsIfCmtsServiceTable <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmtsServiceTable>`
    
    .. attribute:: docsifcmtsmodulationtable
    
    	Describes a modulation profile associated with one or more upstream channels
    	**type**\:  :py:class:`DocsIfCmtsModulationTable <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmtsModulationTable>`
    
    .. attribute:: docsifcmtsmactocmtable
    
    	This is a table to provide a quick access index into the docsIfCmtsCmStatusTable. There is exactly one row in this table for each row in the docsIfCmtsCmStatusTable. In general, the management station should use this table only to get a pointer into the docsIfCmtsCmStatusTable (which corresponds to the CM's RF interface MAC address), and should not iterate (e.g. GetNext through) this table
    	**type**\:  :py:class:`DocsIfCmtsMacToCmTable <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmtsMacToCmTable>`
    
    .. attribute:: docsifcmtschannelutilizationtable
    
    	Reports utilization statistics for attached upstream and downstream physical channels
    	**type**\:  :py:class:`DocsIfCmtsChannelUtilizationTable <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmtsChannelUtilizationTable>`
    
    .. attribute:: docsifcmtsdownchannelcountertable
    
    	This table is implemented at the CMTS to collect downstream channel statistics for utilization calculations
    	**type**\:  :py:class:`DocsIfCmtsDownChannelCounterTable <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmtsDownChannelCounterTable>`
    
    .. attribute:: docsifcmtsupchannelcountertable
    
    	This table is implemented at the CMTS to provide upstream channel statistics appropriate for channel utilization calculations
    	**type**\:  :py:class:`DocsIfCmtsUpChannelCounterTable <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmtsUpChannelCounterTable>`
    
    

    """

    _prefix = 'DOCS-IF-MIB'
    _revision = '2007-09-12'

    def __init__(self):
        super(DOCSIFMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "DOCS-IF-MIB"
        self.yang_parent_name = "DOCS-IF-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("docsIfBaseObjects", ("docsifbaseobjects", DOCSIFMIB.DocsIfBaseObjects)), ("docsIfCmtsObjects", ("docsifcmtsobjects", DOCSIFMIB.DocsIfCmtsObjects)), ("docsIfDownstreamChannelTable", ("docsifdownstreamchanneltable", DOCSIFMIB.DocsIfDownstreamChannelTable)), ("docsIfUpstreamChannelTable", ("docsifupstreamchanneltable", DOCSIFMIB.DocsIfUpstreamChannelTable)), ("docsIfQosProfileTable", ("docsifqosprofiletable", DOCSIFMIB.DocsIfQosProfileTable)), ("docsIfSignalQualityTable", ("docsifsignalqualitytable", DOCSIFMIB.DocsIfSignalQualityTable)), ("docsIfCmMacTable", ("docsifcmmactable", DOCSIFMIB.DocsIfCmMacTable)), ("docsIfCmStatusTable", ("docsifcmstatustable", DOCSIFMIB.DocsIfCmStatusTable)), ("docsIfCmServiceTable", ("docsifcmservicetable", DOCSIFMIB.DocsIfCmServiceTable)), ("docsIfCmtsMacTable", ("docsifcmtsmactable", DOCSIFMIB.DocsIfCmtsMacTable)), ("docsIfCmtsStatusTable", ("docsifcmtsstatustable", DOCSIFMIB.DocsIfCmtsStatusTable)), ("docsIfCmtsCmStatusTable", ("docsifcmtscmstatustable", DOCSIFMIB.DocsIfCmtsCmStatusTable)), ("docsIfCmtsServiceTable", ("docsifcmtsservicetable", DOCSIFMIB.DocsIfCmtsServiceTable)), ("docsIfCmtsModulationTable", ("docsifcmtsmodulationtable", DOCSIFMIB.DocsIfCmtsModulationTable)), ("docsIfCmtsMacToCmTable", ("docsifcmtsmactocmtable", DOCSIFMIB.DocsIfCmtsMacToCmTable)), ("docsIfCmtsChannelUtilizationTable", ("docsifcmtschannelutilizationtable", DOCSIFMIB.DocsIfCmtsChannelUtilizationTable)), ("docsIfCmtsDownChannelCounterTable", ("docsifcmtsdownchannelcountertable", DOCSIFMIB.DocsIfCmtsDownChannelCounterTable)), ("docsIfCmtsUpChannelCounterTable", ("docsifcmtsupchannelcountertable", DOCSIFMIB.DocsIfCmtsUpChannelCounterTable))])
        self._leafs = OrderedDict()

        self.docsifbaseobjects = DOCSIFMIB.DocsIfBaseObjects()
        self.docsifbaseobjects.parent = self
        self._children_name_map["docsifbaseobjects"] = "docsIfBaseObjects"

        self.docsifcmtsobjects = DOCSIFMIB.DocsIfCmtsObjects()
        self.docsifcmtsobjects.parent = self
        self._children_name_map["docsifcmtsobjects"] = "docsIfCmtsObjects"

        self.docsifdownstreamchanneltable = DOCSIFMIB.DocsIfDownstreamChannelTable()
        self.docsifdownstreamchanneltable.parent = self
        self._children_name_map["docsifdownstreamchanneltable"] = "docsIfDownstreamChannelTable"

        self.docsifupstreamchanneltable = DOCSIFMIB.DocsIfUpstreamChannelTable()
        self.docsifupstreamchanneltable.parent = self
        self._children_name_map["docsifupstreamchanneltable"] = "docsIfUpstreamChannelTable"

        self.docsifqosprofiletable = DOCSIFMIB.DocsIfQosProfileTable()
        self.docsifqosprofiletable.parent = self
        self._children_name_map["docsifqosprofiletable"] = "docsIfQosProfileTable"

        self.docsifsignalqualitytable = DOCSIFMIB.DocsIfSignalQualityTable()
        self.docsifsignalqualitytable.parent = self
        self._children_name_map["docsifsignalqualitytable"] = "docsIfSignalQualityTable"

        self.docsifcmmactable = DOCSIFMIB.DocsIfCmMacTable()
        self.docsifcmmactable.parent = self
        self._children_name_map["docsifcmmactable"] = "docsIfCmMacTable"

        self.docsifcmstatustable = DOCSIFMIB.DocsIfCmStatusTable()
        self.docsifcmstatustable.parent = self
        self._children_name_map["docsifcmstatustable"] = "docsIfCmStatusTable"

        self.docsifcmservicetable = DOCSIFMIB.DocsIfCmServiceTable()
        self.docsifcmservicetable.parent = self
        self._children_name_map["docsifcmservicetable"] = "docsIfCmServiceTable"

        self.docsifcmtsmactable = DOCSIFMIB.DocsIfCmtsMacTable()
        self.docsifcmtsmactable.parent = self
        self._children_name_map["docsifcmtsmactable"] = "docsIfCmtsMacTable"

        self.docsifcmtsstatustable = DOCSIFMIB.DocsIfCmtsStatusTable()
        self.docsifcmtsstatustable.parent = self
        self._children_name_map["docsifcmtsstatustable"] = "docsIfCmtsStatusTable"

        self.docsifcmtscmstatustable = DOCSIFMIB.DocsIfCmtsCmStatusTable()
        self.docsifcmtscmstatustable.parent = self
        self._children_name_map["docsifcmtscmstatustable"] = "docsIfCmtsCmStatusTable"

        self.docsifcmtsservicetable = DOCSIFMIB.DocsIfCmtsServiceTable()
        self.docsifcmtsservicetable.parent = self
        self._children_name_map["docsifcmtsservicetable"] = "docsIfCmtsServiceTable"

        self.docsifcmtsmodulationtable = DOCSIFMIB.DocsIfCmtsModulationTable()
        self.docsifcmtsmodulationtable.parent = self
        self._children_name_map["docsifcmtsmodulationtable"] = "docsIfCmtsModulationTable"

        self.docsifcmtsmactocmtable = DOCSIFMIB.DocsIfCmtsMacToCmTable()
        self.docsifcmtsmactocmtable.parent = self
        self._children_name_map["docsifcmtsmactocmtable"] = "docsIfCmtsMacToCmTable"

        self.docsifcmtschannelutilizationtable = DOCSIFMIB.DocsIfCmtsChannelUtilizationTable()
        self.docsifcmtschannelutilizationtable.parent = self
        self._children_name_map["docsifcmtschannelutilizationtable"] = "docsIfCmtsChannelUtilizationTable"

        self.docsifcmtsdownchannelcountertable = DOCSIFMIB.DocsIfCmtsDownChannelCounterTable()
        self.docsifcmtsdownchannelcountertable.parent = self
        self._children_name_map["docsifcmtsdownchannelcountertable"] = "docsIfCmtsDownChannelCounterTable"

        self.docsifcmtsupchannelcountertable = DOCSIFMIB.DocsIfCmtsUpChannelCounterTable()
        self.docsifcmtsupchannelcountertable.parent = self
        self._children_name_map["docsifcmtsupchannelcountertable"] = "docsIfCmtsUpChannelCounterTable"
        self._segment_path = lambda: "DOCS-IF-MIB:DOCS-IF-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(DOCSIFMIB, [], name, value)


    class DocsIfBaseObjects(Entity):
        """
        
        
        .. attribute:: docsifdocsisbasecapability
        
        	Indication of the DOCSIS capability of the device
        	**type**\:  :py:class:`DocsisVersion <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DocsisVersion>`
        
        

        """

        _prefix = 'DOCS-IF-MIB'
        _revision = '2007-09-12'

        def __init__(self):
            super(DOCSIFMIB.DocsIfBaseObjects, self).__init__()

            self.yang_name = "docsIfBaseObjects"
            self.yang_parent_name = "DOCS-IF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('docsifdocsisbasecapability', (YLeaf(YType.enumeration, 'docsIfDocsisBaseCapability'), [('ydk.models.cisco_ios_xe.DOCS_IF_MIB', 'DocsisVersion', '')])),
            ])
            self.docsifdocsisbasecapability = None
            self._segment_path = lambda: "docsIfBaseObjects"
            self._absolute_path = lambda: "DOCS-IF-MIB:DOCS-IF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIFMIB.DocsIfBaseObjects, [u'docsifdocsisbasecapability'], name, value)


    class DocsIfCmtsObjects(Entity):
        """
        
        
        .. attribute:: docsifcmtsqosprofilepermissions
        
        	This object specifies permitted methods of creating entries in docsIfQosProfileTable. CreateByManagement(0) is set if entries can be created using SNMP. UpdateByManagement(1) is set if updating entries using SNMP is permitted. CreateByModems(2) is set if entries can be created based on information in REG\-REQ MAC messages received from Cable Modems. Information in this object is only applicable if docsIfQosProfileTable is implemented as read\-create. Otherwise, this object is implemented as read\-only and returns CreateByModems(2). Either CreateByManagement(0) or CreateByModems(1) must be set when writing to this object. Note that BITS objects are encoded most significant bit first. For example, if bit 2 is set, the value of this object is the octet string '20'H
        	**type**\:  :py:class:`DocsIfCmtsQosProfilePermissions <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmtsObjects.DocsIfCmtsQosProfilePermissions>`
        
        .. attribute:: docsifcmtschannelutilizationinterval
        
        	The time interval in seconds over which the channel utilization index is calculated. All upstream/downstream channels use the same docsIfCmtsChannelUtilizationInterval.  Setting a value of zero disables utilization reporting. A channel utilization index is calculated over a fixed window applying to the most recent docsIfCmtsChannelUtilizationInterval. It would therefore be prudent to use a relatively short docsIfCmtsChannelUtilizationInterval
        	**type**\: int
        
        	**range:** 0..86400
        
        	**units**\: seconds
        
        

        """

        _prefix = 'DOCS-IF-MIB'
        _revision = '2007-09-12'

        def __init__(self):
            super(DOCSIFMIB.DocsIfCmtsObjects, self).__init__()

            self.yang_name = "docsIfCmtsObjects"
            self.yang_parent_name = "DOCS-IF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('docsifcmtsqosprofilepermissions', (YLeaf(YType.bits, 'docsIfCmtsQosProfilePermissions'), ['Bits'])),
                ('docsifcmtschannelutilizationinterval', (YLeaf(YType.int32, 'docsIfCmtsChannelUtilizationInterval'), ['int'])),
            ])
            self.docsifcmtsqosprofilepermissions = Bits()
            self.docsifcmtschannelutilizationinterval = None
            self._segment_path = lambda: "docsIfCmtsObjects"
            self._absolute_path = lambda: "DOCS-IF-MIB:DOCS-IF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIFMIB.DocsIfCmtsObjects, [u'docsifcmtsqosprofilepermissions', u'docsifcmtschannelutilizationinterval'], name, value)


    class DocsIfDownstreamChannelTable(Entity):
        """
        This table describes the attributes of downstream
        channels (frequency bands).
        
        .. attribute:: docsifdownstreamchannelentry
        
        	An entry provides a list of attributes for a single Downstream channel. An entry in this table exists for each ifEntry with an ifType of docsCableDownstream(128)
        	**type**\: list of  		 :py:class:`DocsIfDownstreamChannelEntry <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfDownstreamChannelTable.DocsIfDownstreamChannelEntry>`
        
        

        """

        _prefix = 'DOCS-IF-MIB'
        _revision = '2007-09-12'

        def __init__(self):
            super(DOCSIFMIB.DocsIfDownstreamChannelTable, self).__init__()

            self.yang_name = "docsIfDownstreamChannelTable"
            self.yang_parent_name = "DOCS-IF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIfDownstreamChannelEntry", ("docsifdownstreamchannelentry", DOCSIFMIB.DocsIfDownstreamChannelTable.DocsIfDownstreamChannelEntry))])
            self._leafs = OrderedDict()

            self.docsifdownstreamchannelentry = YList(self)
            self._segment_path = lambda: "docsIfDownstreamChannelTable"
            self._absolute_path = lambda: "DOCS-IF-MIB:DOCS-IF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIFMIB.DocsIfDownstreamChannelTable, [], name, value)


        class DocsIfDownstreamChannelEntry(Entity):
            """
            An entry provides a list of attributes for a single
            Downstream channel.
            An entry in this table exists for each ifEntry with an
            ifType of docsCableDownstream(128).
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsifdownchannelid
            
            	The Cable Modem Termination System (CMTS) identification of the downstream channel within this particular MAC interface. If the interface is down, the object returns the most current value. If the downstream channel ID is unknown, this object returns a value of 0
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: docsifdownchannelfrequency
            
            	The center of the downstream frequency associated with this channel. This object will return the current tuner frequency. If a CMTS provides IF output, this object will return 0, unless this CMTS is in control of the final downstream RF frequency.  See the associated compliance object for a description of valid frequencies that may be written to this object
            	**type**\: int
            
            	**range:** 0..1000000000
            
            	**units**\: hertz
            
            .. attribute:: docsifdownchannelwidth
            
            	The bandwidth of this downstream channel. Most implementations are expected to support a channel width of 6 MHz (North America) and/or 8 MHz (Europe).  See the associated compliance object for a description of the valid channel widths for this object
            	**type**\: int
            
            	**range:** 0..16000000
            
            	**units**\: hertz
            
            .. attribute:: docsifdownchannelmodulation
            
            	The modulation type associated with this downstream channel. If the interface is down, this object either returns the configured value (CMTS), the most current value (CM), or the value of unknown(1).  See the associated conformance object for write conditions and limitations. See the reference for specifics on the modulation profiles implied by qam64 and qam256
            	**type**\:  :py:class:`DocsIfDownChannelModulation <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfDownstreamChannelTable.DocsIfDownstreamChannelEntry.DocsIfDownChannelModulation>`
            
            .. attribute:: docsifdownchannelinterleave
            
            	The Forward Error Correction (FEC) interleaving used for this downstream channel. Values are defined as follows\: taps8Increment16(3)\:   protection 5.9/4.1 usec,                        latency .22/.15 msec taps16Increment8(4)\:   protection 12/8.2 usec,                        latency .48/.33 msec taps32Increment4(5)\:   protection 24/16 usec,                        latency .98/.68 msec taps64Increment2(6)\:   protection 47/33 usec,                        latency 2/1.4 msec taps128Increment1(7)\:  protection 95/66 usec,                        latency 4/2.8 msec taps12increment17(8)\:  protection 18/14 usec,                        latency 0.43/0.32 msec                        taps12increment17 is implemented in                         conformance with EuroDOCSIS document                        'Adapted MIB\-definitions \- and a                         clarification for MPEG\-related issues \- for                         EuroDOCSIS cable modem systems' by tComLabs                        and should only be used for a EuroDOCSIS MAC                         interface.     If the interface is down, this object either returns the configured value (CMTS), the most current value (CM), or the value of unknown(1). The value of other(2) is returned if the interleave is known but not defined in the above list. See the associated conformance object for write conditions and limitations. See the reference for the FEC configuration described by the setting of this object
            	**type**\:  :py:class:`DocsIfDownChannelInterleave <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfDownstreamChannelTable.DocsIfDownstreamChannelEntry.DocsIfDownChannelInterleave>`
            
            .. attribute:: docsifdownchannelpower
            
            	At the CMTS, the operational transmit power. At the CM, the received power level. May be set to zero at the CM if power level measurement is not supported. If the interface is down, this object either returns the configured value (CMTS), the most current value (CM) or the value of 0. See the associated conformance object for write conditions and limitations. See the reference for recommended and required power levels
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: dBmV
            
            .. attribute:: docsifdownchannelannex
            
            	The value of this object indicates the conformance of the implementation to important regional cable standards. annexA \: Annex A from ITU\-J83 is used. annexB \: Annex B from ITU\-J83 is used. annexC \: Annex C from ITU\-J83 is used.  AnnexB is used for DOCSIS implementations
            	**type**\:  :py:class:`DocsIfDownChannelAnnex <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfDownstreamChannelTable.DocsIfDownstreamChannelEntry.DocsIfDownChannelAnnex>`
            
            .. attribute:: docsifdownchannelstoragetype
            
            	The storage type for this conceptual row. Entries with this object set to permanent(4) do not require write operations for read\-write objects
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            

            """

            _prefix = 'DOCS-IF-MIB'
            _revision = '2007-09-12'

            def __init__(self):
                super(DOCSIFMIB.DocsIfDownstreamChannelTable.DocsIfDownstreamChannelEntry, self).__init__()

                self.yang_name = "docsIfDownstreamChannelEntry"
                self.yang_parent_name = "docsIfDownstreamChannelTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsifdownchannelid', (YLeaf(YType.int32, 'docsIfDownChannelId'), ['int'])),
                    ('docsifdownchannelfrequency', (YLeaf(YType.int32, 'docsIfDownChannelFrequency'), ['int'])),
                    ('docsifdownchannelwidth', (YLeaf(YType.int32, 'docsIfDownChannelWidth'), ['int'])),
                    ('docsifdownchannelmodulation', (YLeaf(YType.enumeration, 'docsIfDownChannelModulation'), [('ydk.models.cisco_ios_xe.DOCS_IF_MIB', 'DOCSIFMIB', 'DocsIfDownstreamChannelTable.DocsIfDownstreamChannelEntry.DocsIfDownChannelModulation')])),
                    ('docsifdownchannelinterleave', (YLeaf(YType.enumeration, 'docsIfDownChannelInterleave'), [('ydk.models.cisco_ios_xe.DOCS_IF_MIB', 'DOCSIFMIB', 'DocsIfDownstreamChannelTable.DocsIfDownstreamChannelEntry.DocsIfDownChannelInterleave')])),
                    ('docsifdownchannelpower', (YLeaf(YType.int32, 'docsIfDownChannelPower'), ['int'])),
                    ('docsifdownchannelannex', (YLeaf(YType.enumeration, 'docsIfDownChannelAnnex'), [('ydk.models.cisco_ios_xe.DOCS_IF_MIB', 'DOCSIFMIB', 'DocsIfDownstreamChannelTable.DocsIfDownstreamChannelEntry.DocsIfDownChannelAnnex')])),
                    ('docsifdownchannelstoragetype', (YLeaf(YType.enumeration, 'docsIfDownChannelStorageType'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                ])
                self.ifindex = None
                self.docsifdownchannelid = None
                self.docsifdownchannelfrequency = None
                self.docsifdownchannelwidth = None
                self.docsifdownchannelmodulation = None
                self.docsifdownchannelinterleave = None
                self.docsifdownchannelpower = None
                self.docsifdownchannelannex = None
                self.docsifdownchannelstoragetype = None
                self._segment_path = lambda: "docsIfDownstreamChannelEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "DOCS-IF-MIB:DOCS-IF-MIB/docsIfDownstreamChannelTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIFMIB.DocsIfDownstreamChannelTable.DocsIfDownstreamChannelEntry, [u'ifindex', u'docsifdownchannelid', u'docsifdownchannelfrequency', u'docsifdownchannelwidth', u'docsifdownchannelmodulation', u'docsifdownchannelinterleave', u'docsifdownchannelpower', u'docsifdownchannelannex', u'docsifdownchannelstoragetype'], name, value)

            class DocsIfDownChannelAnnex(Enum):
                """
                DocsIfDownChannelAnnex (Enum Class)

                The value of this object indicates the conformance of

                the implementation to important regional cable standards.

                annexA \: Annex A from ITU\-J83 is used.

                annexB \: Annex B from ITU\-J83 is used.

                annexC \: Annex C from ITU\-J83 is used. 

                AnnexB is used for DOCSIS implementations

                .. data:: unknown = 1

                .. data:: other = 2

                .. data:: annexA = 3

                .. data:: annexB = 4

                .. data:: annexC = 5

                """

                unknown = Enum.YLeaf(1, "unknown")

                other = Enum.YLeaf(2, "other")

                annexA = Enum.YLeaf(3, "annexA")

                annexB = Enum.YLeaf(4, "annexB")

                annexC = Enum.YLeaf(5, "annexC")


            class DocsIfDownChannelInterleave(Enum):
                """
                DocsIfDownChannelInterleave (Enum Class)

                The Forward Error Correction (FEC) interleaving used

                for this downstream channel.

                Values are defined as follows\:

                taps8Increment16(3)\:   protection 5.9/4.1 usec,

                                       latency .22/.15 msec

                taps16Increment8(4)\:   protection 12/8.2 usec,

                                       latency .48/.33 msec

                taps32Increment4(5)\:   protection 24/16 usec,

                                       latency .98/.68 msec

                taps64Increment2(6)\:   protection 47/33 usec,

                                       latency 2/1.4 msec

                taps128Increment1(7)\:  protection 95/66 usec,

                                       latency 4/2.8 msec

                taps12increment17(8)\:  protection 18/14 usec,

                                       latency 0.43/0.32 msec

                                       taps12increment17 is implemented in 

                                       conformance with EuroDOCSIS document

                                       'Adapted MIB\-definitions \- and a 

                                       clarification for MPEG\-related issues \- for 

                                       EuroDOCSIS cable modem systems' by tComLabs

                                       and should only be used for a EuroDOCSIS MAC 

                                       interface.   

                If the interface is down, this object either returns

                the configured value (CMTS), the most current value (CM),

                or the value of unknown(1).

                The value of other(2) is returned if the interleave

                is known but not defined in the above list.

                See the associated conformance object for write

                conditions and limitations. See the reference for the FEC

                configuration described by the setting of this object.

                .. data:: unknown = 1

                .. data:: other = 2

                .. data:: taps8Increment16 = 3

                .. data:: taps16Increment8 = 4

                .. data:: taps32Increment4 = 5

                .. data:: taps64Increment2 = 6

                .. data:: taps128Increment1 = 7

                .. data:: taps12increment17 = 8

                """

                unknown = Enum.YLeaf(1, "unknown")

                other = Enum.YLeaf(2, "other")

                taps8Increment16 = Enum.YLeaf(3, "taps8Increment16")

                taps16Increment8 = Enum.YLeaf(4, "taps16Increment8")

                taps32Increment4 = Enum.YLeaf(5, "taps32Increment4")

                taps64Increment2 = Enum.YLeaf(6, "taps64Increment2")

                taps128Increment1 = Enum.YLeaf(7, "taps128Increment1")

                taps12increment17 = Enum.YLeaf(8, "taps12increment17")


            class DocsIfDownChannelModulation(Enum):
                """
                DocsIfDownChannelModulation (Enum Class)

                The modulation type associated with this downstream

                channel. If the interface is down, this object either

                returns the configured value (CMTS), the most current

                value (CM), or the value of unknown(1).  See the

                associated conformance object for write conditions and

                limitations. See the reference for specifics on the

                modulation profiles implied by qam64 and qam256.

                .. data:: unknown = 1

                .. data:: other = 2

                .. data:: qam64 = 3

                .. data:: qam256 = 4

                """

                unknown = Enum.YLeaf(1, "unknown")

                other = Enum.YLeaf(2, "other")

                qam64 = Enum.YLeaf(3, "qam64")

                qam256 = Enum.YLeaf(4, "qam256")



    class DocsIfUpstreamChannelTable(Entity):
        """
        This table describes the attributes of attached upstream
        channels.
        
        .. attribute:: docsifupstreamchannelentry
        
        	List of attributes for a single upstream channel. For Docsis 2.0 CMTSs, an entry in this table exists for  each ifEntry with an ifType of docsCableUpstreamChannel (205). For Docsis 1.x CM/CMTSs and Docsis 2.0 CMs, an entry in this table exists  for each ifEntry with an ifType of docsCableUpstreamInterface (129)
        	**type**\: list of  		 :py:class:`DocsIfUpstreamChannelEntry <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfUpstreamChannelTable.DocsIfUpstreamChannelEntry>`
        
        

        """

        _prefix = 'DOCS-IF-MIB'
        _revision = '2007-09-12'

        def __init__(self):
            super(DOCSIFMIB.DocsIfUpstreamChannelTable, self).__init__()

            self.yang_name = "docsIfUpstreamChannelTable"
            self.yang_parent_name = "DOCS-IF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIfUpstreamChannelEntry", ("docsifupstreamchannelentry", DOCSIFMIB.DocsIfUpstreamChannelTable.DocsIfUpstreamChannelEntry))])
            self._leafs = OrderedDict()

            self.docsifupstreamchannelentry = YList(self)
            self._segment_path = lambda: "docsIfUpstreamChannelTable"
            self._absolute_path = lambda: "DOCS-IF-MIB:DOCS-IF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIFMIB.DocsIfUpstreamChannelTable, [], name, value)


        class DocsIfUpstreamChannelEntry(Entity):
            """
            List of attributes for a single upstream channel. For
            Docsis 2.0 CMTSs, an entry in this table exists for 
            each ifEntry with an ifType of docsCableUpstreamChannel (205).
            For Docsis 1.x CM/CMTSs and Docsis 2.0 CMs, an entry in this table exists 
            for each ifEntry with an ifType of docsCableUpstreamInterface (129).
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsifupchannelid
            
            	The CMTS identification of the upstream channel
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: docsifupchannelfrequency
            
            	The center of the frequency band associated with this upstream interface. This object returns 0 if the frequency is undefined or unknown. Minimum permitted upstream frequency is 5,000,000 Hz for current technology.  See the associated conformance object for write conditions and limitations
            	**type**\: int
            
            	**range:** 0..1000000000
            
            	**units**\: hertz
            
            .. attribute:: docsifupchannelwidth
            
            	The bandwidth of this upstream interface. This object returns 0 if the interface width is undefined or unknown. Minimum permitted interface width is 200,000 Hz currently. See the associated conformance object for write conditions and limitations
            	**type**\: int
            
            	**range:** 0..64000000
            
            	**units**\: hertz
            
            .. attribute:: docsifupchannelmodulationprofile
            
            	An entry identical to the docsIfModIndex in the docsIfCmtsModulationTable that describes this channel. This channel is further instantiated there by a grouping of interval usage codes which together fully describe the channel modulation. This object returns 0 if the docsIfCmtsModulationTable entry does not exist or docsIfCmtsModulationTable is empty. See the associated conformance object for write conditions and limitations
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifupchannelslotsize
            
            	Applicable to TDMA and ATDMA channel types only. The number of 6.25 microsecond ticks in each upstream mini\- slot. Returns zero if the value is undefined, unknown or in case of an SCDMA channel. See the associated conformance object for write conditions and limitations. 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifupchanneltxtimingoffset
            
            	At the CM, a measure of the current round trip time obtained from the ranging offset (initial ranging offset + ranging offset adjustments). At the CMTS, the maximum of timing offset, among all the CMs that  are/were present on the channel, taking into account all ( initial +  periodic )timing offset corrections that were sent for each of the CMs. Generally, these measurements are positive, but if the  measurements are negative, the value of this object is zero. Used for  timing of CM upstream transmissions to ensure synchronized arrivals at  the CMTS. Units are in terms of (6.25 microseconds/64)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifupchannelrangingbackoffstart
            
            	The initial random backoff window to use when retrying Ranging Requests. Expressed as a power of 2. A value of 16 at the CMTS indicates that a proprietary adaptive retry mechanism is to be used. See the associated conformance object for write conditions and limitations
            	**type**\: int
            
            	**range:** 0..16
            
            .. attribute:: docsifupchannelrangingbackoffend
            
            	The final random backoff window to use when retrying Ranging Requests. Expressed as a power of 2. A value of 16 at the CMTS indicates that a proprietary adaptive retry mechanism is to be used. See the associated conformance object for write conditions and limitations
            	**type**\: int
            
            	**range:** 0..16
            
            .. attribute:: docsifupchanneltxbackoffstart
            
            	The initial random backoff window to use when retrying transmissions. Expressed as a power of 2. A value of 16 at the CMTS indicates that a proprietary adaptive retry mechanism is to be used. See the associated conformance object for write conditions and limitations
            	**type**\: int
            
            	**range:** 0..16
            
            .. attribute:: docsifupchanneltxbackoffend
            
            	The final random backoff window to use when retrying transmissions. Expressed as a power of 2. A value of 16 at the CMTS indicates that a proprietary adaptive retry mechanism is to be used. See the associated conformance object for write conditions and limitations
            	**type**\: int
            
            	**range:** 0..16
            
            .. attribute:: docsifupchannelscdmaactivecodes
            
            	Applicable for SCDMA channel types only. Number of active codes. Returns zero for Non\-SCDMA channel types. Note that legal  values from 64..128 MUST be non\-prime
            	**type**\: int
            
            	**range:** 0..None \| 64..128
            
            .. attribute:: docsifupchannelscdmacodesperslot
            
            	Applicable for SCDMA channel types only. The number of SCDMA codes per mini\-slot. Returns zero if the value is undefined, unknown or in case of a TDMA or ATDMA channel
            	**type**\: int
            
            	**range:** 0..None \| 2..32
            
            .. attribute:: docsifupchannelscdmaframesize
            
            	Applicable for SCDMA channel types only. SCDMA Frame size in units of spreading intervals.  This value returns zero for non SCDMA Profiles
            	**type**\: int
            
            	**range:** 0..32
            
            .. attribute:: docsifupchannelscdmahoppingseed
            
            	Applicable for SCDMA channel types only. 15 bit seed used for code hopping sequence initialization. Returns zero for non\-SCDMA channel types
            	**type**\: int
            
            	**range:** 0..32767
            
            .. attribute:: docsifupchanneltype
            
            	Defines the Upstream channel type. Given the channel type, other channel attributes can be checked for value validity at the time of entry creation and update
            	**type**\:  :py:class:`DocsisUpstreamType <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DocsisUpstreamType>`
            
            .. attribute:: docsifupchannelclonefrom
            
            	Intended for use when a temporary inactive upstream table row is created for the purpose of manipulating SCDMA parameters for an active row. Refer to the descriptions of docsIfUpChannelStatus  and docsIfUpChannelUpdate for details of this procedure. This object contains the ifIndex value of the active upstream row whose SCDMA parameters are to be adjusted. Although this object was created to facilitate SCDMA parameter adjustment, it may also be used at the vendor's discretion for non\-SCDMA parameter adjustment. This object must contain a value of zero for active upstream rows
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: docsifupchannelupdate
            
            	Used to perform the transfer of adjusted SCDMA parameters from the temporary upstream row to the active upstream row indicated by the docsIfUpChannelCloneFrom object. The transfer is initiated through  an SNMP SET of TRUE to this object. The SNMP SET will fail with a GEN\_ERROR (snmpv1) or COMMIT\_FAILED\_ERROR (snmpv2c/v3) if the adjusted SCDMA parameter values are not compatible with each other. Although this object was created to facilitate SCDMA parameter adjustment, it may also be used at the vendor's discretion for non\-SCDMA parameter adjustment. An SNMP GET of this object always returns FALSE
            	**type**\: bool
            
            .. attribute:: docsifupchannelstatus
            
            	This object is generally intended to be used for the creation of a temporary inactive upstream row for the purpose of adjusting the SCDMA channel parameters of an active upstream row.  The recommended procedure is\: 1) Create an inactive row through an SNMP SET using createAndWait(5).    Use an ifIndex value outside the operational range of the system. 2) Set the docsIfUpChannelCloneFrom field to the ifIndex value of    the active row whose SCDMA parameters require adjustment. 3) Adjust the SCDMA parameter values using the new temporary inactive    row. 4) Update the active row by setting object docsIfUpChannelUpdate to    TRUE. This SET will fail if the adjusted SCDMA parameters are not    compatible with each other. 5) Delete the temporary row through an SNMP SET using DELETE.  The following restrictions apply to this object\: 1) This object must contain a value of active(1) for active rows. 2) Temporary inactive rows must be created using createAndWait(5). 3) The only possible status change of a row created using     createAndWait(5) (ie notInService(2)) is to destroy(6).    These temporary rows must never become active. 4) A status transition from active (1) to destroy (6) is not    permitted. Entries with docsIfUpChannelStatus set to active(1)     are logically linked to a physical interface, not temporarily     created to clone parameters. The Interface MIB (RFC 2863)    ifAdminStatus should be used to take an Upstream Channel offline.  Although this object was created to facilitate SCDMA parameter adjustment, it may also be used at the vendor's discretion for non\-SCDMA parameter adjustment
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: docsifupchannelpreeqenable
            
            	At the CMTS, used to enable or disable pre\-equalization on the upstream channel represented by this table instance.  At the CM, this object is read\-only and reflects the status of  pre\-equalization as represented in the RNG\-RSP
            	**type**\: bool
            
            

            """

            _prefix = 'DOCS-IF-MIB'
            _revision = '2007-09-12'

            def __init__(self):
                super(DOCSIFMIB.DocsIfUpstreamChannelTable.DocsIfUpstreamChannelEntry, self).__init__()

                self.yang_name = "docsIfUpstreamChannelEntry"
                self.yang_parent_name = "docsIfUpstreamChannelTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsifupchannelid', (YLeaf(YType.int32, 'docsIfUpChannelId'), ['int'])),
                    ('docsifupchannelfrequency', (YLeaf(YType.int32, 'docsIfUpChannelFrequency'), ['int'])),
                    ('docsifupchannelwidth', (YLeaf(YType.int32, 'docsIfUpChannelWidth'), ['int'])),
                    ('docsifupchannelmodulationprofile', (YLeaf(YType.uint32, 'docsIfUpChannelModulationProfile'), ['int'])),
                    ('docsifupchannelslotsize', (YLeaf(YType.uint32, 'docsIfUpChannelSlotSize'), ['int'])),
                    ('docsifupchanneltxtimingoffset', (YLeaf(YType.uint32, 'docsIfUpChannelTxTimingOffset'), ['int'])),
                    ('docsifupchannelrangingbackoffstart', (YLeaf(YType.int32, 'docsIfUpChannelRangingBackoffStart'), ['int'])),
                    ('docsifupchannelrangingbackoffend', (YLeaf(YType.int32, 'docsIfUpChannelRangingBackoffEnd'), ['int'])),
                    ('docsifupchanneltxbackoffstart', (YLeaf(YType.int32, 'docsIfUpChannelTxBackoffStart'), ['int'])),
                    ('docsifupchanneltxbackoffend', (YLeaf(YType.int32, 'docsIfUpChannelTxBackoffEnd'), ['int'])),
                    ('docsifupchannelscdmaactivecodes', (YLeaf(YType.uint32, 'docsIfUpChannelScdmaActiveCodes'), ['int'])),
                    ('docsifupchannelscdmacodesperslot', (YLeaf(YType.int32, 'docsIfUpChannelScdmaCodesPerSlot'), ['int'])),
                    ('docsifupchannelscdmaframesize', (YLeaf(YType.uint32, 'docsIfUpChannelScdmaFrameSize'), ['int'])),
                    ('docsifupchannelscdmahoppingseed', (YLeaf(YType.uint32, 'docsIfUpChannelScdmaHoppingSeed'), ['int'])),
                    ('docsifupchanneltype', (YLeaf(YType.enumeration, 'docsIfUpChannelType'), [('ydk.models.cisco_ios_xe.DOCS_IF_MIB', 'DocsisUpstreamType', '')])),
                    ('docsifupchannelclonefrom', (YLeaf(YType.int32, 'docsIfUpChannelCloneFrom'), ['int'])),
                    ('docsifupchannelupdate', (YLeaf(YType.boolean, 'docsIfUpChannelUpdate'), ['bool'])),
                    ('docsifupchannelstatus', (YLeaf(YType.enumeration, 'docsIfUpChannelStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('docsifupchannelpreeqenable', (YLeaf(YType.boolean, 'docsIfUpChannelPreEqEnable'), ['bool'])),
                ])
                self.ifindex = None
                self.docsifupchannelid = None
                self.docsifupchannelfrequency = None
                self.docsifupchannelwidth = None
                self.docsifupchannelmodulationprofile = None
                self.docsifupchannelslotsize = None
                self.docsifupchanneltxtimingoffset = None
                self.docsifupchannelrangingbackoffstart = None
                self.docsifupchannelrangingbackoffend = None
                self.docsifupchanneltxbackoffstart = None
                self.docsifupchanneltxbackoffend = None
                self.docsifupchannelscdmaactivecodes = None
                self.docsifupchannelscdmacodesperslot = None
                self.docsifupchannelscdmaframesize = None
                self.docsifupchannelscdmahoppingseed = None
                self.docsifupchanneltype = None
                self.docsifupchannelclonefrom = None
                self.docsifupchannelupdate = None
                self.docsifupchannelstatus = None
                self.docsifupchannelpreeqenable = None
                self._segment_path = lambda: "docsIfUpstreamChannelEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "DOCS-IF-MIB:DOCS-IF-MIB/docsIfUpstreamChannelTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIFMIB.DocsIfUpstreamChannelTable.DocsIfUpstreamChannelEntry, [u'ifindex', u'docsifupchannelid', u'docsifupchannelfrequency', u'docsifupchannelwidth', u'docsifupchannelmodulationprofile', u'docsifupchannelslotsize', u'docsifupchanneltxtimingoffset', u'docsifupchannelrangingbackoffstart', u'docsifupchannelrangingbackoffend', u'docsifupchanneltxbackoffstart', u'docsifupchanneltxbackoffend', u'docsifupchannelscdmaactivecodes', u'docsifupchannelscdmacodesperslot', u'docsifupchannelscdmaframesize', u'docsifupchannelscdmahoppingseed', u'docsifupchanneltype', u'docsifupchannelclonefrom', u'docsifupchannelupdate', u'docsifupchannelstatus', u'docsifupchannelpreeqenable'], name, value)


    class DocsIfQosProfileTable(Entity):
        """
        Describes the attributes for each class of service.
        
        .. attribute:: docsifqosprofileentry
        
        	Describes the attributes for a single class of service.  If implemented as read\-create in the Cable Modem Termination System, creation of entries in this table is controlled by the value of docsIfCmtsQosProfilePermissions.  If implemented as read\-only, entries are created based on information in REG\-REQ MAC messages received from Cable Modems (Cable Modem Termination System implementation), or based on information extracted from the TFTP option file (Cable Modem implementation). In the Cable Modem Termination system, read\-only entries are removed if no longer referenced by docsIfCmtsServiceTable.  An entry in this table must not be removed while it is referenced by an entry in docsIfCmServiceTable (Cable Modem) or docsIfCmtsServiceTable (Cable Modem Termination System).  An entry in this table should not be changeable while it is referenced by an entry in docsIfCmtsServiceTable.  If this table is created automatically, there should only be a single entry for each Class of Service. Multiple entries with the same Class of Service parameters are not recommended
        	**type**\: list of  		 :py:class:`DocsIfQosProfileEntry <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfQosProfileTable.DocsIfQosProfileEntry>`
        
        

        """

        _prefix = 'DOCS-IF-MIB'
        _revision = '2007-09-12'

        def __init__(self):
            super(DOCSIFMIB.DocsIfQosProfileTable, self).__init__()

            self.yang_name = "docsIfQosProfileTable"
            self.yang_parent_name = "DOCS-IF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIfQosProfileEntry", ("docsifqosprofileentry", DOCSIFMIB.DocsIfQosProfileTable.DocsIfQosProfileEntry))])
            self._leafs = OrderedDict()

            self.docsifqosprofileentry = YList(self)
            self._segment_path = lambda: "docsIfQosProfileTable"
            self._absolute_path = lambda: "DOCS-IF-MIB:DOCS-IF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIFMIB.DocsIfQosProfileTable, [], name, value)


        class DocsIfQosProfileEntry(Entity):
            """
            Describes the attributes for a single class of service.
            
            If implemented as read\-create in the Cable Modem
            Termination System, creation of entries in this table is
            controlled by the value of docsIfCmtsQosProfilePermissions.
            
            If implemented as read\-only, entries are created based
            on information in REG\-REQ MAC messages received from
            Cable Modems (Cable Modem Termination System
            implementation), or based on information extracted from
            the TFTP option file (Cable Modem implementation).
            In the Cable Modem Termination system, read\-only entries
            are removed if no longer referenced by
            docsIfCmtsServiceTable.
            
            An entry in this table must not be removed while it is
            referenced by an entry in docsIfCmServiceTable (Cable Modem)
            or docsIfCmtsServiceTable (Cable Modem Termination System).
            
            An entry in this table should not be changeable while
            it is referenced by an entry in docsIfCmtsServiceTable.
            
            If this table is created automatically, there should only
            be a single entry for each Class of Service. Multiple
            entries with the same Class of Service parameters are not
            recommended.
            
            .. attribute:: docsifqosprofindex  (key)
            
            	The index value that uniquely identifies an entry in the docsIfQosProfileTable
            	**type**\: int
            
            	**range:** 1..16383
            
            .. attribute:: docsifqosprofpriority
            
            	A relative priority assigned to this service when allocating bandwidth. Zero indicates lowest priority and seven indicates highest priority. Interpretation of priority is device\-specific. MUST NOT be changed while this row is active
            	**type**\: int
            
            	**range:** 0..7
            
            .. attribute:: docsifqosprofmaxupbandwidth
            
            	The maximum upstream bandwidth, in bits per second, allowed for a service with this service class. Zero if there is no restriction of upstream bandwidth. MUST NOT be changed while this row is active
            	**type**\: int
            
            	**range:** 0..100000000
            
            .. attribute:: docsifqosprofguarupbandwidth
            
            	Minimum guaranteed upstream bandwidth, in bits per second, allowed for a service with this service class. MUST NOT be changed while this row is active
            	**type**\: int
            
            	**range:** 0..100000000
            
            .. attribute:: docsifqosprofmaxdownbandwidth
            
            	The maximum downstream bandwidth, in bits per second, allowed for a service with this service class. Zero if there is no restriction of downstream bandwidth. MUST NOT be changed while this row is active
            	**type**\: int
            
            	**range:** 0..100000000
            
            .. attribute:: docsifqosprofmaxtxburst
            
            	The maximum number of mini\-slots that may be requested for a single upstream transmission. A value of zero means there is no limit. MUST NOT be changed while this row is active. This object has been deprecated and replaced by  docsIfQosProfMaxTransmitBurst, to fix a mismatch of the units and value range with respect to the DOCSIS Maximum Upstream Channel Transmit Burst Configuration Setting
            	**type**\: int
            
            	**range:** 0..255
            
            	**status**\: deprecated
            
            .. attribute:: docsifqosprofbaselineprivacy
            
            	Indicates whether Baseline Privacy is enabled for this service class. MUST NOT be changed while this row is active
            	**type**\: bool
            
            .. attribute:: docsifqosprofstatus
            
            	This is object is to used to create or delete rows in this table.  This object MUST NOT be changed from active while the row is referenced by the any entry in either docsIfCmServiceTable (on the CM), or the docsIfCmtsServiceTable (on the CMTS)
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: docsifqosprofmaxtransmitburst
            
            	The maximum number of bytes that may be requested for a  single upstream transmission. A value of zero means there  is no limit. Note\: This value does not include any  physical layer overhead. MUST NOT be changed while this row is active
            	**type**\: int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'DOCS-IF-MIB'
            _revision = '2007-09-12'

            def __init__(self):
                super(DOCSIFMIB.DocsIfQosProfileTable.DocsIfQosProfileEntry, self).__init__()

                self.yang_name = "docsIfQosProfileEntry"
                self.yang_parent_name = "docsIfQosProfileTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['docsifqosprofindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('docsifqosprofindex', (YLeaf(YType.int32, 'docsIfQosProfIndex'), ['int'])),
                    ('docsifqosprofpriority', (YLeaf(YType.int32, 'docsIfQosProfPriority'), ['int'])),
                    ('docsifqosprofmaxupbandwidth', (YLeaf(YType.int32, 'docsIfQosProfMaxUpBandwidth'), ['int'])),
                    ('docsifqosprofguarupbandwidth', (YLeaf(YType.int32, 'docsIfQosProfGuarUpBandwidth'), ['int'])),
                    ('docsifqosprofmaxdownbandwidth', (YLeaf(YType.int32, 'docsIfQosProfMaxDownBandwidth'), ['int'])),
                    ('docsifqosprofmaxtxburst', (YLeaf(YType.int32, 'docsIfQosProfMaxTxBurst'), ['int'])),
                    ('docsifqosprofbaselineprivacy', (YLeaf(YType.boolean, 'docsIfQosProfBaselinePrivacy'), ['bool'])),
                    ('docsifqosprofstatus', (YLeaf(YType.enumeration, 'docsIfQosProfStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('docsifqosprofmaxtransmitburst', (YLeaf(YType.int32, 'docsIfQosProfMaxTransmitBurst'), ['int'])),
                ])
                self.docsifqosprofindex = None
                self.docsifqosprofpriority = None
                self.docsifqosprofmaxupbandwidth = None
                self.docsifqosprofguarupbandwidth = None
                self.docsifqosprofmaxdownbandwidth = None
                self.docsifqosprofmaxtxburst = None
                self.docsifqosprofbaselineprivacy = None
                self.docsifqosprofstatus = None
                self.docsifqosprofmaxtransmitburst = None
                self._segment_path = lambda: "docsIfQosProfileEntry" + "[docsIfQosProfIndex='" + str(self.docsifqosprofindex) + "']"
                self._absolute_path = lambda: "DOCS-IF-MIB:DOCS-IF-MIB/docsIfQosProfileTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIFMIB.DocsIfQosProfileTable.DocsIfQosProfileEntry, [u'docsifqosprofindex', u'docsifqosprofpriority', u'docsifqosprofmaxupbandwidth', u'docsifqosprofguarupbandwidth', u'docsifqosprofmaxdownbandwidth', u'docsifqosprofmaxtxburst', u'docsifqosprofbaselineprivacy', u'docsifqosprofstatus', u'docsifqosprofmaxtransmitburst'], name, value)


    class DocsIfSignalQualityTable(Entity):
        """
        At the CM, describes the PHY signal quality of downstream
        channels. At the CMTS, describes the PHY signal quality of
        upstream channels. At the CMTS, this table may exclude
        contention intervals.
        
        .. attribute:: docsifsignalqualityentry
        
        	At the CM, describes the PHY characteristics of a downstream channel. At the CMTS, describes the PHY signal quality of an upstream channel. An entry in this table exists for each ifEntry with an ifType of docsCableUpstreamChannel(205) for Cable Modem Termination Systems and docsCableDownstream(128) for Cable Modems
        	**type**\: list of  		 :py:class:`DocsIfSignalQualityEntry <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfSignalQualityTable.DocsIfSignalQualityEntry>`
        
        

        """

        _prefix = 'DOCS-IF-MIB'
        _revision = '2007-09-12'

        def __init__(self):
            super(DOCSIFMIB.DocsIfSignalQualityTable, self).__init__()

            self.yang_name = "docsIfSignalQualityTable"
            self.yang_parent_name = "DOCS-IF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIfSignalQualityEntry", ("docsifsignalqualityentry", DOCSIFMIB.DocsIfSignalQualityTable.DocsIfSignalQualityEntry))])
            self._leafs = OrderedDict()

            self.docsifsignalqualityentry = YList(self)
            self._segment_path = lambda: "docsIfSignalQualityTable"
            self._absolute_path = lambda: "DOCS-IF-MIB:DOCS-IF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIFMIB.DocsIfSignalQualityTable, [], name, value)


        class DocsIfSignalQualityEntry(Entity):
            """
            At the CM, describes the PHY characteristics of a
            downstream channel. At the CMTS, describes the PHY signal
            quality of an upstream channel.
            An entry in this table exists for each ifEntry with an
            ifType of docsCableUpstreamChannel(205) for Cable Modem Termination
            Systems and docsCableDownstream(128) for Cable Modems.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsifsigqincludescontention
            
            	true(1) if this CMTS includes contention intervals in the counters in this table. Always false(2) for CMs
            	**type**\: bool
            
            .. attribute:: docsifsigqunerroreds
            
            	Codewords received on this channel without error. This includes all codewords, whether or not they were part of frames destined for this device
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifsigqcorrecteds
            
            	Codewords received on this channel with correctable errors. This includes all codewords, whether or not they were part of frames destined for this device
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifsigquncorrectables
            
            	Codewords received on this channel with uncorrectable errors. This includes all codewords, whether or not they were part of frames destined for this device
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifsigqsignalnoise
            
            	Signal/Noise ratio as perceived for this channel. At the CM, describes the Signal/Noise of the downstream channel.  At the CMTS, describes the average Signal/Noise of the upstream channel
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: dB
            
            .. attribute:: docsifsigqmicroreflections
            
            	Total microreflections including in\-channel response as perceived on this interface, measured in dBc below the signal level. This object is not assumed to return an absolutely accurate value, but should give a rough indication of microreflections received on this interface. It is up to the implementer to provide information as accurate as possible
            	**type**\: int
            
            	**range:** 0..255
            
            	**units**\: dBc
            
            .. attribute:: docsifsigqequalizationdata
            
            	At the CM, returns the equalization data for the downstream channel. At the CMTS, returns the average equalization data for the upstream channel. Returns an empty string if the value is unknown or if there is no equalization data available or defined
            	**type**\: str
            
            .. attribute:: docsifsigqextunerroreds
            
            	Codewords received on this channel without error. This includes all codewords, whether or not they were part of frames destined for this device. This is the 64 bit version of docsIfSigQUnerroreds
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: docsifsigqextcorrecteds
            
            	Codewords received on this channel with correctable errors. This includes all codewords, whether or not they were part of frames destined for this device. This is the 64 bit version of docsIfSigQCorrecteds
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: docsifsigqextuncorrectables
            
            	Codewords received on this channel with uncorrectable errors. This includes all codewords, whether or not they were part of frames destined for this device. This is the 64 bit version of docsIfSigQUncorrectables
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'DOCS-IF-MIB'
            _revision = '2007-09-12'

            def __init__(self):
                super(DOCSIFMIB.DocsIfSignalQualityTable.DocsIfSignalQualityEntry, self).__init__()

                self.yang_name = "docsIfSignalQualityEntry"
                self.yang_parent_name = "docsIfSignalQualityTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsifsigqincludescontention', (YLeaf(YType.boolean, 'docsIfSigQIncludesContention'), ['bool'])),
                    ('docsifsigqunerroreds', (YLeaf(YType.uint32, 'docsIfSigQUnerroreds'), ['int'])),
                    ('docsifsigqcorrecteds', (YLeaf(YType.uint32, 'docsIfSigQCorrecteds'), ['int'])),
                    ('docsifsigquncorrectables', (YLeaf(YType.uint32, 'docsIfSigQUncorrectables'), ['int'])),
                    ('docsifsigqsignalnoise', (YLeaf(YType.int32, 'docsIfSigQSignalNoise'), ['int'])),
                    ('docsifsigqmicroreflections', (YLeaf(YType.int32, 'docsIfSigQMicroreflections'), ['int'])),
                    ('docsifsigqequalizationdata', (YLeaf(YType.str, 'docsIfSigQEqualizationData'), ['str'])),
                    ('docsifsigqextunerroreds', (YLeaf(YType.uint64, 'docsIfSigQExtUnerroreds'), ['int'])),
                    ('docsifsigqextcorrecteds', (YLeaf(YType.uint64, 'docsIfSigQExtCorrecteds'), ['int'])),
                    ('docsifsigqextuncorrectables', (YLeaf(YType.uint64, 'docsIfSigQExtUncorrectables'), ['int'])),
                ])
                self.ifindex = None
                self.docsifsigqincludescontention = None
                self.docsifsigqunerroreds = None
                self.docsifsigqcorrecteds = None
                self.docsifsigquncorrectables = None
                self.docsifsigqsignalnoise = None
                self.docsifsigqmicroreflections = None
                self.docsifsigqequalizationdata = None
                self.docsifsigqextunerroreds = None
                self.docsifsigqextcorrecteds = None
                self.docsifsigqextuncorrectables = None
                self._segment_path = lambda: "docsIfSignalQualityEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "DOCS-IF-MIB:DOCS-IF-MIB/docsIfSignalQualityTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIFMIB.DocsIfSignalQualityTable.DocsIfSignalQualityEntry, [u'ifindex', u'docsifsigqincludescontention', u'docsifsigqunerroreds', u'docsifsigqcorrecteds', u'docsifsigquncorrectables', u'docsifsigqsignalnoise', u'docsifsigqmicroreflections', u'docsifsigqequalizationdata', u'docsifsigqextunerroreds', u'docsifsigqextcorrecteds', u'docsifsigqextuncorrectables'], name, value)


    class DocsIfCmMacTable(Entity):
        """
        Describes the attributes of each CM MAC interface,
        extending the information available from ifEntry.
        
        .. attribute:: docsifcmmacentry
        
        	An entry containing objects describing attributes of each MAC entry, extending the information in ifEntry. An entry in this table exists for each ifEntry with an ifType of docsCableMaclayer(127)
        	**type**\: list of  		 :py:class:`DocsIfCmMacEntry <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmMacTable.DocsIfCmMacEntry>`
        
        

        """

        _prefix = 'DOCS-IF-MIB'
        _revision = '2007-09-12'

        def __init__(self):
            super(DOCSIFMIB.DocsIfCmMacTable, self).__init__()

            self.yang_name = "docsIfCmMacTable"
            self.yang_parent_name = "DOCS-IF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIfCmMacEntry", ("docsifcmmacentry", DOCSIFMIB.DocsIfCmMacTable.DocsIfCmMacEntry))])
            self._leafs = OrderedDict()

            self.docsifcmmacentry = YList(self)
            self._segment_path = lambda: "docsIfCmMacTable"
            self._absolute_path = lambda: "DOCS-IF-MIB:DOCS-IF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIFMIB.DocsIfCmMacTable, [], name, value)


        class DocsIfCmMacEntry(Entity):
            """
            An entry containing objects describing attributes of
            each MAC entry, extending the information in ifEntry.
            An entry in this table exists for each ifEntry with an
            ifType of docsCableMaclayer(127).
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsifcmcmtsaddress
            
            	Identifies the CMTS that is believed to control this MAC domain. At the CM, this will be the source address from SYNC, MAP, and other MAC\-layer messages. If the CMTS is unknown, returns 00\-00\-00\-00\-00\-00
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: docsifcmcapabilities
            
            	Identifies the capabilities of the MAC implementation at this interface. Note that packet transmission is always supported. Therefore, there is no specific bit required to explicitly indicate this capability. Note that BITS objects are encoded most significant bit first. For example, if bit 1 is set, the value of this object is the octet string '40'H
            	**type**\:  :py:class:`DocsIfCmCapabilities <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmMacTable.DocsIfCmMacEntry.DocsIfCmCapabilities>`
            
            .. attribute:: docsifcmrangingresptimeout
            
            	Waiting time for a Ranging Response packet
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: docsifcmrangingtimeout
            
            	Waiting time for a Ranging Response packet
            	**type**\: int
            
            	**range:** 0..2147483647
            
            

            """

            _prefix = 'DOCS-IF-MIB'
            _revision = '2007-09-12'

            def __init__(self):
                super(DOCSIFMIB.DocsIfCmMacTable.DocsIfCmMacEntry, self).__init__()

                self.yang_name = "docsIfCmMacEntry"
                self.yang_parent_name = "docsIfCmMacTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsifcmcmtsaddress', (YLeaf(YType.str, 'docsIfCmCmtsAddress'), ['str'])),
                    ('docsifcmcapabilities', (YLeaf(YType.bits, 'docsIfCmCapabilities'), ['Bits'])),
                    ('docsifcmrangingresptimeout', (YLeaf(YType.uint32, 'docsIfCmRangingRespTimeout'), ['int'])),
                    ('docsifcmrangingtimeout', (YLeaf(YType.int32, 'docsIfCmRangingTimeout'), ['int'])),
                ])
                self.ifindex = None
                self.docsifcmcmtsaddress = None
                self.docsifcmcapabilities = Bits()
                self.docsifcmrangingresptimeout = None
                self.docsifcmrangingtimeout = None
                self._segment_path = lambda: "docsIfCmMacEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "DOCS-IF-MIB:DOCS-IF-MIB/docsIfCmMacTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIFMIB.DocsIfCmMacTable.DocsIfCmMacEntry, [u'ifindex', u'docsifcmcmtsaddress', u'docsifcmcapabilities', u'docsifcmrangingresptimeout', u'docsifcmrangingtimeout'], name, value)


    class DocsIfCmStatusTable(Entity):
        """
        This table maintains a number of status objects
        and counters for Cable Modems.
        
        .. attribute:: docsifcmstatusentry
        
        	A set of status objects and counters for a single MAC layer instance in a Cable Modem. An entry in this table exists for each ifEntry with an ifType of docsCableMaclayer(127)
        	**type**\: list of  		 :py:class:`DocsIfCmStatusEntry <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmStatusTable.DocsIfCmStatusEntry>`
        
        

        """

        _prefix = 'DOCS-IF-MIB'
        _revision = '2007-09-12'

        def __init__(self):
            super(DOCSIFMIB.DocsIfCmStatusTable, self).__init__()

            self.yang_name = "docsIfCmStatusTable"
            self.yang_parent_name = "DOCS-IF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIfCmStatusEntry", ("docsifcmstatusentry", DOCSIFMIB.DocsIfCmStatusTable.DocsIfCmStatusEntry))])
            self._leafs = OrderedDict()

            self.docsifcmstatusentry = YList(self)
            self._segment_path = lambda: "docsIfCmStatusTable"
            self._absolute_path = lambda: "DOCS-IF-MIB:DOCS-IF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIFMIB.DocsIfCmStatusTable, [], name, value)


        class DocsIfCmStatusEntry(Entity):
            """
            A set of status objects and counters for a single MAC
            layer instance in a Cable Modem.
            An entry in this table exists for each ifEntry with an
            ifType of docsCableMaclayer(127).
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsifcmstatusvalue
            
            	Current Cable Modem connectivity state, as specified in the RF Interface Specification. Interpretations for state values 1\-12 are clearly outlined in the Document [25] reference given below. As stated in the description for object docsIfCmtsCmStatusValue, accessDenied(13)indicates the CMTS has sent a Registration Aborted message to the CM
            	**type**\:  :py:class:`DocsIfCmStatusValue <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmStatusTable.DocsIfCmStatusEntry.DocsIfCmStatusValue>`
            
            .. attribute:: docsifcmstatuscode
            
            	Status code for this Cable Modem as defined in the RF Interface Specification. The status code consists of a single character indicating error groups, followed by a two\- or three\-digit number indicating the status condition
            	**type**\: str
            
            .. attribute:: docsifcmstatustxpower
            
            	The operational transmit power for the attached upstream channel
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: dBmV
            
            .. attribute:: docsifcmstatusresets
            
            	Number of times the CM reset or initialized this interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmstatuslostsyncs
            
            	Number of times the CM lost synchronization with the downstream channel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmstatusinvalidmaps
            
            	Number of times the CM received invalid MAP messages
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmstatusinvaliducds
            
            	Number of times the CM received invalid UCD messages
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmstatusinvalidrangingresponses
            
            	Number of times the CM received invalid ranging response messages
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmstatusinvalidregistrationresponses
            
            	Number of times the CM received invalid registration response messages
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmstatust1timeouts
            
            	Number of times counter T1 expired in the CM
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmstatust2timeouts
            
            	Number of times counter T2 expired in the CM
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmstatust3timeouts
            
            	Number of times counter T3 expired in the CM
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmstatust4timeouts
            
            	Number of times counter T4 expired in the CM
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmstatusrangingaborteds
            
            	Number of times the ranging process was aborted by the CMTS
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmstatusdocsisopermode
            
            	Indication whether the device has registered using 1.0 Class of Service or 1.1 Quality of Service. An unregistered CM should indicate 1.1 QOS for a  docsIfDocsisBaseCapability value of Docsis 1.1/2.0. An unregistered 	  CM should indicate 1.0 COS for a docsIfDocsisBaseCapability value  of Docsis 1.0. This object mirrors docsIfCmDocsisOperMode from the docsIfExt mib
            	**type**\:  :py:class:`DocsisQosVersion <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DocsisQosVersion>`
            
            .. attribute:: docsifcmstatusmodulationtype
            
            	Indicates modulation type status currently used by the CM. Since this object specifically identifies PHY mode, the shared upstream channel type is not permitted
            	**type**\:  :py:class:`DocsisUpstreamTypeStatus <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DocsisUpstreamTypeStatus>`
            
            .. attribute:: docsifcmstatusequalizationdata
            
            	Pre\-equalization data for this CM after convolution with  data indicated in the RNG\-RSP. Returns an empty string if the value is unknown or if there  is no equalization data available or defined. The value should  be formatted as defined in the following REFERENCE
            	**type**\: str
            
            

            """

            _prefix = 'DOCS-IF-MIB'
            _revision = '2007-09-12'

            def __init__(self):
                super(DOCSIFMIB.DocsIfCmStatusTable.DocsIfCmStatusEntry, self).__init__()

                self.yang_name = "docsIfCmStatusEntry"
                self.yang_parent_name = "docsIfCmStatusTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsifcmstatusvalue', (YLeaf(YType.enumeration, 'docsIfCmStatusValue'), [('ydk.models.cisco_ios_xe.DOCS_IF_MIB', 'DOCSIFMIB', 'DocsIfCmStatusTable.DocsIfCmStatusEntry.DocsIfCmStatusValue')])),
                    ('docsifcmstatuscode', (YLeaf(YType.str, 'docsIfCmStatusCode'), ['str'])),
                    ('docsifcmstatustxpower', (YLeaf(YType.int32, 'docsIfCmStatusTxPower'), ['int'])),
                    ('docsifcmstatusresets', (YLeaf(YType.uint32, 'docsIfCmStatusResets'), ['int'])),
                    ('docsifcmstatuslostsyncs', (YLeaf(YType.uint32, 'docsIfCmStatusLostSyncs'), ['int'])),
                    ('docsifcmstatusinvalidmaps', (YLeaf(YType.uint32, 'docsIfCmStatusInvalidMaps'), ['int'])),
                    ('docsifcmstatusinvaliducds', (YLeaf(YType.uint32, 'docsIfCmStatusInvalidUcds'), ['int'])),
                    ('docsifcmstatusinvalidrangingresponses', (YLeaf(YType.uint32, 'docsIfCmStatusInvalidRangingResponses'), ['int'])),
                    ('docsifcmstatusinvalidregistrationresponses', (YLeaf(YType.uint32, 'docsIfCmStatusInvalidRegistrationResponses'), ['int'])),
                    ('docsifcmstatust1timeouts', (YLeaf(YType.uint32, 'docsIfCmStatusT1Timeouts'), ['int'])),
                    ('docsifcmstatust2timeouts', (YLeaf(YType.uint32, 'docsIfCmStatusT2Timeouts'), ['int'])),
                    ('docsifcmstatust3timeouts', (YLeaf(YType.uint32, 'docsIfCmStatusT3Timeouts'), ['int'])),
                    ('docsifcmstatust4timeouts', (YLeaf(YType.uint32, 'docsIfCmStatusT4Timeouts'), ['int'])),
                    ('docsifcmstatusrangingaborteds', (YLeaf(YType.uint32, 'docsIfCmStatusRangingAborteds'), ['int'])),
                    ('docsifcmstatusdocsisopermode', (YLeaf(YType.enumeration, 'docsIfCmStatusDocsisOperMode'), [('ydk.models.cisco_ios_xe.DOCS_IF_MIB', 'DocsisQosVersion', '')])),
                    ('docsifcmstatusmodulationtype', (YLeaf(YType.enumeration, 'docsIfCmStatusModulationType'), [('ydk.models.cisco_ios_xe.DOCS_IF_MIB', 'DocsisUpstreamTypeStatus', '')])),
                    ('docsifcmstatusequalizationdata', (YLeaf(YType.str, 'docsIfCmStatusEqualizationData'), ['str'])),
                ])
                self.ifindex = None
                self.docsifcmstatusvalue = None
                self.docsifcmstatuscode = None
                self.docsifcmstatustxpower = None
                self.docsifcmstatusresets = None
                self.docsifcmstatuslostsyncs = None
                self.docsifcmstatusinvalidmaps = None
                self.docsifcmstatusinvaliducds = None
                self.docsifcmstatusinvalidrangingresponses = None
                self.docsifcmstatusinvalidregistrationresponses = None
                self.docsifcmstatust1timeouts = None
                self.docsifcmstatust2timeouts = None
                self.docsifcmstatust3timeouts = None
                self.docsifcmstatust4timeouts = None
                self.docsifcmstatusrangingaborteds = None
                self.docsifcmstatusdocsisopermode = None
                self.docsifcmstatusmodulationtype = None
                self.docsifcmstatusequalizationdata = None
                self._segment_path = lambda: "docsIfCmStatusEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "DOCS-IF-MIB:DOCS-IF-MIB/docsIfCmStatusTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIFMIB.DocsIfCmStatusTable.DocsIfCmStatusEntry, [u'ifindex', u'docsifcmstatusvalue', u'docsifcmstatuscode', u'docsifcmstatustxpower', u'docsifcmstatusresets', u'docsifcmstatuslostsyncs', u'docsifcmstatusinvalidmaps', u'docsifcmstatusinvaliducds', u'docsifcmstatusinvalidrangingresponses', u'docsifcmstatusinvalidregistrationresponses', u'docsifcmstatust1timeouts', u'docsifcmstatust2timeouts', u'docsifcmstatust3timeouts', u'docsifcmstatust4timeouts', u'docsifcmstatusrangingaborteds', u'docsifcmstatusdocsisopermode', u'docsifcmstatusmodulationtype', u'docsifcmstatusequalizationdata'], name, value)

            class DocsIfCmStatusValue(Enum):
                """
                DocsIfCmStatusValue (Enum Class)

                Current Cable Modem connectivity state, as specified

                in the RF Interface Specification. Interpretations for

                state values 1\-12 are clearly outlined in the Document [25]

                reference given below.

                As stated in the description for object docsIfCmtsCmStatusValue,

                accessDenied(13)indicates the CMTS has sent a Registration

                Aborted message to the CM.

                .. data:: other = 1

                .. data:: notReady = 2

                .. data:: notSynchronized = 3

                .. data:: phySynchronized = 4

                .. data:: usParametersAcquired = 5

                .. data:: rangingComplete = 6

                .. data:: ipComplete = 7

                .. data:: todEstablished = 8

                .. data:: securityEstablished = 9

                .. data:: paramTransferComplete = 10

                .. data:: registrationComplete = 11

                .. data:: operational = 12

                .. data:: accessDenied = 13

                """

                other = Enum.YLeaf(1, "other")

                notReady = Enum.YLeaf(2, "notReady")

                notSynchronized = Enum.YLeaf(3, "notSynchronized")

                phySynchronized = Enum.YLeaf(4, "phySynchronized")

                usParametersAcquired = Enum.YLeaf(5, "usParametersAcquired")

                rangingComplete = Enum.YLeaf(6, "rangingComplete")

                ipComplete = Enum.YLeaf(7, "ipComplete")

                todEstablished = Enum.YLeaf(8, "todEstablished")

                securityEstablished = Enum.YLeaf(9, "securityEstablished")

                paramTransferComplete = Enum.YLeaf(10, "paramTransferComplete")

                registrationComplete = Enum.YLeaf(11, "registrationComplete")

                operational = Enum.YLeaf(12, "operational")

                accessDenied = Enum.YLeaf(13, "accessDenied")



    class DocsIfCmServiceTable(Entity):
        """
        Describes the attributes of each upstream service queue
        on a CM.
        
        .. attribute:: docsifcmserviceentry
        
        	Describes the attributes of an upstream bandwidth service queue. An entry in this table exists for each Service ID. The primary index is an ifIndex with an ifType of docsCableMaclayer(127)
        	**type**\: list of  		 :py:class:`DocsIfCmServiceEntry <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmServiceTable.DocsIfCmServiceEntry>`
        
        

        """

        _prefix = 'DOCS-IF-MIB'
        _revision = '2007-09-12'

        def __init__(self):
            super(DOCSIFMIB.DocsIfCmServiceTable, self).__init__()

            self.yang_name = "docsIfCmServiceTable"
            self.yang_parent_name = "DOCS-IF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIfCmServiceEntry", ("docsifcmserviceentry", DOCSIFMIB.DocsIfCmServiceTable.DocsIfCmServiceEntry))])
            self._leafs = OrderedDict()

            self.docsifcmserviceentry = YList(self)
            self._segment_path = lambda: "docsIfCmServiceTable"
            self._absolute_path = lambda: "DOCS-IF-MIB:DOCS-IF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIFMIB.DocsIfCmServiceTable, [], name, value)


        class DocsIfCmServiceEntry(Entity):
            """
            Describes the attributes of an upstream bandwidth service
            queue.
            An entry in this table exists for each Service ID.
            The primary index is an ifIndex with an ifType of
            docsCableMaclayer(127).
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsifcmserviceid  (key)
            
            	Identifies a service queue for upstream bandwidth. The attributes of this service queue are shared between the CM and the CMTS. The CMTS allocates upstream bandwidth to this service queue based on requests from the CM and on the class of service associated with this queue
            	**type**\: int
            
            	**range:** 1..16383
            
            .. attribute:: docsifcmserviceqosprofile
            
            	The index in docsIfQosProfileTable describing the quality of service attributes associated with this particular service. If no associated entry in docsIfQosProfileTable exists, this object returns a value of zero
            	**type**\: int
            
            	**range:** 0..16383
            
            .. attribute:: docsifcmservicetxslotsimmed
            
            	The number of upstream mini\-slots which have been used to transmit data PDUs in immediate (contention) mode. This includes only those PDUs that are presumed to have arrived at the headend (i.e., those which were explicitly acknowledged.) It does not include retransmission attempts or mini\-slots used by Requests
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmservicetxslotsded
            
            	The number of upstream mini\-slots which have been used to transmit data PDUs in dedicated mode (i.e., as a result of a unicast Data Grant)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmservicetxretries
            
            	The number of attempts to transmit data PDUs containing requests for acknowledgment that did not result in acknowledgment
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmservicetxexceededs
            
            	The number of data PDUs transmission failures due to excessive retries without acknowledgment
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmservicerqretries
            
            	The number of attempts to transmit bandwidth requests which did not result in acknowledgment
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmservicerqexceededs
            
            	The number of requests for bandwidth which failed due to excessive retries without acknowledgment
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmserviceexttxslotsimmed
            
            	The number of upstream mini\-slots which have been used to transmit data PDUs in immediate (contention) mode. This includes only those PDUs that are presumed to have arrived at the headend (i.e., those which were explicitly acknowledged.) It does not include retransmission attempts or mini\-slots used by Requests
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: docsifcmserviceexttxslotsded
            
            	The number of upstream mini\-slots which have been used to transmit data PDUs in dedicated mode (i.e., as a result of a unicast Data Grant)
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'DOCS-IF-MIB'
            _revision = '2007-09-12'

            def __init__(self):
                super(DOCSIFMIB.DocsIfCmServiceTable.DocsIfCmServiceEntry, self).__init__()

                self.yang_name = "docsIfCmServiceEntry"
                self.yang_parent_name = "docsIfCmServiceTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','docsifcmserviceid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsifcmserviceid', (YLeaf(YType.int32, 'docsIfCmServiceId'), ['int'])),
                    ('docsifcmserviceqosprofile', (YLeaf(YType.int32, 'docsIfCmServiceQosProfile'), ['int'])),
                    ('docsifcmservicetxslotsimmed', (YLeaf(YType.uint32, 'docsIfCmServiceTxSlotsImmed'), ['int'])),
                    ('docsifcmservicetxslotsded', (YLeaf(YType.uint32, 'docsIfCmServiceTxSlotsDed'), ['int'])),
                    ('docsifcmservicetxretries', (YLeaf(YType.uint32, 'docsIfCmServiceTxRetries'), ['int'])),
                    ('docsifcmservicetxexceededs', (YLeaf(YType.uint32, 'docsIfCmServiceTxExceededs'), ['int'])),
                    ('docsifcmservicerqretries', (YLeaf(YType.uint32, 'docsIfCmServiceRqRetries'), ['int'])),
                    ('docsifcmservicerqexceededs', (YLeaf(YType.uint32, 'docsIfCmServiceRqExceededs'), ['int'])),
                    ('docsifcmserviceexttxslotsimmed', (YLeaf(YType.uint64, 'docsIfCmServiceExtTxSlotsImmed'), ['int'])),
                    ('docsifcmserviceexttxslotsded', (YLeaf(YType.uint64, 'docsIfCmServiceExtTxSlotsDed'), ['int'])),
                ])
                self.ifindex = None
                self.docsifcmserviceid = None
                self.docsifcmserviceqosprofile = None
                self.docsifcmservicetxslotsimmed = None
                self.docsifcmservicetxslotsded = None
                self.docsifcmservicetxretries = None
                self.docsifcmservicetxexceededs = None
                self.docsifcmservicerqretries = None
                self.docsifcmservicerqexceededs = None
                self.docsifcmserviceexttxslotsimmed = None
                self.docsifcmserviceexttxslotsded = None
                self._segment_path = lambda: "docsIfCmServiceEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[docsIfCmServiceId='" + str(self.docsifcmserviceid) + "']"
                self._absolute_path = lambda: "DOCS-IF-MIB:DOCS-IF-MIB/docsIfCmServiceTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIFMIB.DocsIfCmServiceTable.DocsIfCmServiceEntry, [u'ifindex', u'docsifcmserviceid', u'docsifcmserviceqosprofile', u'docsifcmservicetxslotsimmed', u'docsifcmservicetxslotsded', u'docsifcmservicetxretries', u'docsifcmservicetxexceededs', u'docsifcmservicerqretries', u'docsifcmservicerqexceededs', u'docsifcmserviceexttxslotsimmed', u'docsifcmserviceexttxslotsded'], name, value)


    class DocsIfCmtsMacTable(Entity):
        """
        Describes the attributes of each CMTS MAC interface,
        extending the information available from ifEntry.
        Mandatory for all CMTS devices.
        
        .. attribute:: docsifcmtsmacentry
        
        	An entry containing objects describing attributes of each MAC entry, extending the information in ifEntry. An entry in this table exists for each ifEntry with an ifType of docsCableMaclayer(127)
        	**type**\: list of  		 :py:class:`DocsIfCmtsMacEntry <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmtsMacTable.DocsIfCmtsMacEntry>`
        
        

        """

        _prefix = 'DOCS-IF-MIB'
        _revision = '2007-09-12'

        def __init__(self):
            super(DOCSIFMIB.DocsIfCmtsMacTable, self).__init__()

            self.yang_name = "docsIfCmtsMacTable"
            self.yang_parent_name = "DOCS-IF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIfCmtsMacEntry", ("docsifcmtsmacentry", DOCSIFMIB.DocsIfCmtsMacTable.DocsIfCmtsMacEntry))])
            self._leafs = OrderedDict()

            self.docsifcmtsmacentry = YList(self)
            self._segment_path = lambda: "docsIfCmtsMacTable"
            self._absolute_path = lambda: "DOCS-IF-MIB:DOCS-IF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIFMIB.DocsIfCmtsMacTable, [], name, value)


        class DocsIfCmtsMacEntry(Entity):
            """
            An entry containing objects describing attributes of each
            MAC entry, extending the information in ifEntry.
            An entry in this table exists for each ifEntry with an
            ifType of docsCableMaclayer(127).
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsifcmtscapabilities
            
            	Identifies the capabilities of the CMTS MAC implementation at this interface. Note that packet transmission is always supported. Therefore, there is no specific bit required to explicitly indicate this capability. Note that BITS objects are encoded most significant bit first. For example, if bit 1 is set, the value of this object is the octet string '40'H
            	**type**\:  :py:class:`DocsIfCmtsCapabilities <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmtsMacTable.DocsIfCmtsMacEntry.DocsIfCmtsCapabilities>`
            
            .. attribute:: docsifcmtssyncinterval
            
            	The interval between CMTS transmission of successive SYNC messages at this interface
            	**type**\: int
            
            	**range:** 1..200
            
            	**units**\: Milliseconds
            
            .. attribute:: docsifcmtsucdinterval
            
            	The interval between CMTS transmission of successive Upstream Channel Descriptor messages for each upstream channel at this interface
            	**type**\: int
            
            	**range:** 1..2000
            
            	**units**\: Milliseconds
            
            .. attribute:: docsifcmtsmaxserviceids
            
            	The maximum number of service IDs that may be simultaneously active
            	**type**\: int
            
            	**range:** 1..16383
            
            .. attribute:: docsifcmtsinsertioninterval
            
            	The amount of time to elapse between each broadcast station maintenance grant. Broadcast station maintenance grants are used to allow new cable modems to join the network. Zero indicates that a vendor\-specific algorithm is used instead of a fixed time. Maximum amount of time permitted by the specification is 2 seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: docsifcmtsinvitedrangingattempts
            
            	The maximum number of attempts to make on invitations for ranging requests. A value of zero means the system should attempt to range forever
            	**type**\: int
            
            	**range:** 0..1024
            
            .. attribute:: docsifcmtsinsertinterval
            
            	The amount of time to elapse between each broadcast station maintenance grant. Broadcast station maintenance grants are used to allow new cable modems to join the network. Zero indicates that a vendor\-specific algorithm is used instead of a fixed time. Maximum amount of time permitted by the specification is 2 seconds
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: docsifcmtsmacstoragetype
            
            	The storage type for this conceptual row. Entries with this object set to permanent(4) do not require write operations for read\-write objects
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            

            """

            _prefix = 'DOCS-IF-MIB'
            _revision = '2007-09-12'

            def __init__(self):
                super(DOCSIFMIB.DocsIfCmtsMacTable.DocsIfCmtsMacEntry, self).__init__()

                self.yang_name = "docsIfCmtsMacEntry"
                self.yang_parent_name = "docsIfCmtsMacTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsifcmtscapabilities', (YLeaf(YType.bits, 'docsIfCmtsCapabilities'), ['Bits'])),
                    ('docsifcmtssyncinterval', (YLeaf(YType.int32, 'docsIfCmtsSyncInterval'), ['int'])),
                    ('docsifcmtsucdinterval', (YLeaf(YType.int32, 'docsIfCmtsUcdInterval'), ['int'])),
                    ('docsifcmtsmaxserviceids', (YLeaf(YType.int32, 'docsIfCmtsMaxServiceIds'), ['int'])),
                    ('docsifcmtsinsertioninterval', (YLeaf(YType.uint32, 'docsIfCmtsInsertionInterval'), ['int'])),
                    ('docsifcmtsinvitedrangingattempts', (YLeaf(YType.int32, 'docsIfCmtsInvitedRangingAttempts'), ['int'])),
                    ('docsifcmtsinsertinterval', (YLeaf(YType.int32, 'docsIfCmtsInsertInterval'), ['int'])),
                    ('docsifcmtsmacstoragetype', (YLeaf(YType.enumeration, 'docsIfCmtsMacStorageType'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                ])
                self.ifindex = None
                self.docsifcmtscapabilities = Bits()
                self.docsifcmtssyncinterval = None
                self.docsifcmtsucdinterval = None
                self.docsifcmtsmaxserviceids = None
                self.docsifcmtsinsertioninterval = None
                self.docsifcmtsinvitedrangingattempts = None
                self.docsifcmtsinsertinterval = None
                self.docsifcmtsmacstoragetype = None
                self._segment_path = lambda: "docsIfCmtsMacEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "DOCS-IF-MIB:DOCS-IF-MIB/docsIfCmtsMacTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIFMIB.DocsIfCmtsMacTable.DocsIfCmtsMacEntry, [u'ifindex', u'docsifcmtscapabilities', u'docsifcmtssyncinterval', u'docsifcmtsucdinterval', u'docsifcmtsmaxserviceids', u'docsifcmtsinsertioninterval', u'docsifcmtsinvitedrangingattempts', u'docsifcmtsinsertinterval', u'docsifcmtsmacstoragetype'], name, value)


    class DocsIfCmtsStatusTable(Entity):
        """
        For the MAC layer, this group maintains a number of
        status objects and counters.
        
        .. attribute:: docsifcmtsstatusentry
        
        	Status entry for a single MAC layer. An entry in this table exists for each ifEntry with an ifType of docsCableMaclayer(127)
        	**type**\: list of  		 :py:class:`DocsIfCmtsStatusEntry <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmtsStatusTable.DocsIfCmtsStatusEntry>`
        
        

        """

        _prefix = 'DOCS-IF-MIB'
        _revision = '2007-09-12'

        def __init__(self):
            super(DOCSIFMIB.DocsIfCmtsStatusTable, self).__init__()

            self.yang_name = "docsIfCmtsStatusTable"
            self.yang_parent_name = "DOCS-IF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIfCmtsStatusEntry", ("docsifcmtsstatusentry", DOCSIFMIB.DocsIfCmtsStatusTable.DocsIfCmtsStatusEntry))])
            self._leafs = OrderedDict()

            self.docsifcmtsstatusentry = YList(self)
            self._segment_path = lambda: "docsIfCmtsStatusTable"
            self._absolute_path = lambda: "DOCS-IF-MIB:DOCS-IF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIFMIB.DocsIfCmtsStatusTable, [], name, value)


        class DocsIfCmtsStatusEntry(Entity):
            """
            Status entry for a single MAC layer.
            An entry in this table exists for each ifEntry with an
            ifType of docsCableMaclayer(127).
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsifcmtsstatusinvalidrangereqs
            
            	This object counts invalid RNG\-REQ messages received on this interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmtsstatusrangingaborteds
            
            	This object counts ranging attempts that were explicitly aborted by the CMTS
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmtsstatusinvalidregreqs
            
            	This object counts invalid REG\-REQ messages received on this interface. That is, syntax, out of range parameters, or erroneous requests
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmtsstatusfailedregreqs
            
            	This object counts failed registration attempts. Included are docsIfCmtsStatusInvalidRegReqs, authentication and class of  service failures
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmtsstatusinvaliddatareqs
            
            	This object counts invalid data request messages received on this interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmtsstatust5timeouts
            
            	This object counts the number of times counter T5 expired on this interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'DOCS-IF-MIB'
            _revision = '2007-09-12'

            def __init__(self):
                super(DOCSIFMIB.DocsIfCmtsStatusTable.DocsIfCmtsStatusEntry, self).__init__()

                self.yang_name = "docsIfCmtsStatusEntry"
                self.yang_parent_name = "docsIfCmtsStatusTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsifcmtsstatusinvalidrangereqs', (YLeaf(YType.uint32, 'docsIfCmtsStatusInvalidRangeReqs'), ['int'])),
                    ('docsifcmtsstatusrangingaborteds', (YLeaf(YType.uint32, 'docsIfCmtsStatusRangingAborteds'), ['int'])),
                    ('docsifcmtsstatusinvalidregreqs', (YLeaf(YType.uint32, 'docsIfCmtsStatusInvalidRegReqs'), ['int'])),
                    ('docsifcmtsstatusfailedregreqs', (YLeaf(YType.uint32, 'docsIfCmtsStatusFailedRegReqs'), ['int'])),
                    ('docsifcmtsstatusinvaliddatareqs', (YLeaf(YType.uint32, 'docsIfCmtsStatusInvalidDataReqs'), ['int'])),
                    ('docsifcmtsstatust5timeouts', (YLeaf(YType.uint32, 'docsIfCmtsStatusT5Timeouts'), ['int'])),
                ])
                self.ifindex = None
                self.docsifcmtsstatusinvalidrangereqs = None
                self.docsifcmtsstatusrangingaborteds = None
                self.docsifcmtsstatusinvalidregreqs = None
                self.docsifcmtsstatusfailedregreqs = None
                self.docsifcmtsstatusinvaliddatareqs = None
                self.docsifcmtsstatust5timeouts = None
                self._segment_path = lambda: "docsIfCmtsStatusEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "DOCS-IF-MIB:DOCS-IF-MIB/docsIfCmtsStatusTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIFMIB.DocsIfCmtsStatusTable.DocsIfCmtsStatusEntry, [u'ifindex', u'docsifcmtsstatusinvalidrangereqs', u'docsifcmtsstatusrangingaborteds', u'docsifcmtsstatusinvalidregreqs', u'docsifcmtsstatusfailedregreqs', u'docsifcmtsstatusinvaliddatareqs', u'docsifcmtsstatust5timeouts'], name, value)


    class DocsIfCmtsCmStatusTable(Entity):
        """
        A set of objects in the CMTS, maintained for each
        Cable Modem connected to this CMTS.
        
        .. attribute:: docsifcmtscmstatusentry
        
        	Status information for a single Cable Modem. An entry in this table exists for each Cable Modem that is connected to the CMTS implementing this table
        	**type**\: list of  		 :py:class:`DocsIfCmtsCmStatusEntry <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmtsCmStatusTable.DocsIfCmtsCmStatusEntry>`
        
        

        """

        _prefix = 'DOCS-IF-MIB'
        _revision = '2007-09-12'

        def __init__(self):
            super(DOCSIFMIB.DocsIfCmtsCmStatusTable, self).__init__()

            self.yang_name = "docsIfCmtsCmStatusTable"
            self.yang_parent_name = "DOCS-IF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIfCmtsCmStatusEntry", ("docsifcmtscmstatusentry", DOCSIFMIB.DocsIfCmtsCmStatusTable.DocsIfCmtsCmStatusEntry))])
            self._leafs = OrderedDict()

            self.docsifcmtscmstatusentry = YList(self)
            self._segment_path = lambda: "docsIfCmtsCmStatusTable"
            self._absolute_path = lambda: "DOCS-IF-MIB:DOCS-IF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIFMIB.DocsIfCmtsCmStatusTable, [], name, value)


        class DocsIfCmtsCmStatusEntry(Entity):
            """
            Status information for a single Cable Modem.
            An entry in this table exists for each Cable Modem
            that is connected to the CMTS implementing this table.
            
            .. attribute:: docsifcmtscmstatusindex  (key)
            
            	Index value to uniquely identify an entry in this table. For an individual Cable Modem, this index value should not change during CMTS uptime
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: docsifcmtscmstatusmacaddress
            
            	MAC address of this Cable Modem. If the Cable Modem has multiple MAC addresses, this is the MAC address associated with the Cable interface
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: docsifcmtscmstatusipaddress
            
            	IP address of this Cable Modem. If the Cable Modem has no IP address assigned, or the IP address is unknown, this object returns a value of 0.0.0.0. If the Cable Modem has multiple IP addresses, this object returns the IP address associated with the Cable interface. This object has been deprecated and replaced by docsIfCmtsCmStatusInetAddressType and docsIfCmtsCmStatusInetAddress, to enable IPv6 addressing in the future
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: docsifcmtscmstatusdownchannelifindex
            
            	IfIndex of the downstream channel this CM is connected to. If the downstream channel is unknown, this object returns a value of zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: docsifcmtscmstatusupchannelifindex
            
            	IfIndex of the upstream channel this CM is connected to. If the upstream channel is unknown, this object returns a value of zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: docsifcmtscmstatusrxpower
            
            	The receive power as perceived for upstream data from this Cable Modem. If the receive power is unknown, this object returns a value of zero
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: dBmV
            
            .. attribute:: docsifcmtscmstatustimingoffset
            
            	A measure of the current round trip time for this CM. Used for timing of CM upstream transmissions to ensure synchronized arrivals at the CMTS. Units are in terms of 6.25 microseconds/(64\*256). Returns zero if the value is unknown
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmtscmstatusequalizationdata
            
            	Equalization data for this CM. Returns an empty string if the value is unknown or if there is no equalization data available or defined
            	**type**\: str
            
            .. attribute:: docsifcmtscmstatusvalue
            
            	Current Cable Modem connectivity state, as specified in the RF Interface Specification. Returned status information is the CM status as assumed by the CMTS, and indicates the following events\: other(1)    Any state other than below. ranging(2)    The CMTS has received an Initial Ranging Request    message from the CM, and the ranging process is not  yet     complete. rangingAborted(3)    The CMTS has sent a Ranging Abort message to the CM. rangingComplete(4)    The CMTS has sent a Ranging Complete message to the CM. ipComplete(5)    The CMTS has received a DHCP reply message and forwarded    it to the CM. registrationComplete(6)    The CMTS has sent a Registration Response message to the CM. accessDenied(7)    The CMTS has sent a Registration Aborted message    to the CM. \-\-           deprecated value \-\-           operational(8) \-\-              If Baseline Privacy is enabled for the CM, the CMTS \-\-              has completed Baseline Privacy initialization. If Baseline \-\-              Privacy is not enabled, equivalent to registrationComplete. registeredBPIInitializing(9)    Baseline Privacy is enabled, CMTS is in the process of     completing the Baseline Privacy initialization. This state     can last for a significant time in the case of failures     during The process. After Baseline Privacy initialization     Complete, the CMTS will report back the value    registrationComplete(6).     The CMTS only needs to report states it is able to detect
            	**type**\:  :py:class:`DocsIfCmtsCmStatusValue <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmtsCmStatusTable.DocsIfCmtsCmStatusEntry.DocsIfCmtsCmStatusValue>`
            
            .. attribute:: docsifcmtscmstatusunerroreds
            
            	Codewords received without error from this Cable Modem
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmtscmstatuscorrecteds
            
            	Codewords received with correctable errors from this Cable Modem
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmtscmstatusuncorrectables
            
            	Codewords received with uncorrectable errors from this Cable Modem
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmtscmstatussignalnoise
            
            	Signal/Noise ratio as perceived for upstream data from this Cable Modem. If the Signal/Noise is unknown, this object returns a value of zero
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: dB
            
            .. attribute:: docsifcmtscmstatusmicroreflections
            
            	Total microreflections including in\-channel response as perceived on this interface, measured in dBc below the signal level. This object is not assumed to return an absolutely accurate value, but should give a rough indication of microreflections received on this interface. It is up to the implementer to provide information as accurate as possible
            	**type**\: int
            
            	**range:** 0..255
            
            	**units**\: dBc
            
            .. attribute:: docsifcmtscmstatusextunerroreds
            
            	Codewords received without error from this Cable Modem
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: docsifcmtscmstatusextcorrecteds
            
            	Codewords received with correctable errors from this Cable Modem
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: docsifcmtscmstatusextuncorrectables
            
            	Codewords received with uncorrectable errors from this Cable Modem
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: docsifcmtscmstatusdocsisregmode
            
            	 Indication whether the CM has registered using 1.0 Class of Service or 1.1 Quality of Service. This object mirrors docsIfCmtsCmStatusDocsisMode from the  docsIfExt mib
            	**type**\:  :py:class:`DocsisQosVersion <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DocsisQosVersion>`
            
            .. attribute:: docsifcmtscmstatusmodulationtype
            
            	Indicates modulation type currently used by the CM. Since this object specifically identifies PHY mode, the shared type is not permitted. If the upstream channel is unknown,  this object returns a value of zero
            	**type**\:  :py:class:`DocsisUpstreamTypeStatus <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DocsisUpstreamTypeStatus>`
            
            .. attribute:: docsifcmtscmstatusinetaddresstype
            
            	The type of internet address of docsIfCmtsCmStatusInetAddress. If the cable modem Internet address is unassigned or unknown, then the value of this object is unknown(0)
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: docsifcmtscmstatusinetaddress
            
            	Internet address of this Cable Modem. If the Cable Modem has no Internet address assigned, or the Internet address is unknown, the value of this object is the empty string. If the Cable Modem has multiple Internet addresses, this object returns the Internet address associated with the Cable (i.e. RF MAC) interface
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: docsifcmtscmstatusvaluelastupdate
            
            	The value of sysUpTime when docsIfCmtsCmStatusValue was last updated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'DOCS-IF-MIB'
            _revision = '2007-09-12'

            def __init__(self):
                super(DOCSIFMIB.DocsIfCmtsCmStatusTable.DocsIfCmtsCmStatusEntry, self).__init__()

                self.yang_name = "docsIfCmtsCmStatusEntry"
                self.yang_parent_name = "docsIfCmtsCmStatusTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['docsifcmtscmstatusindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('docsifcmtscmstatusindex', (YLeaf(YType.int32, 'docsIfCmtsCmStatusIndex'), ['int'])),
                    ('docsifcmtscmstatusmacaddress', (YLeaf(YType.str, 'docsIfCmtsCmStatusMacAddress'), ['str'])),
                    ('docsifcmtscmstatusipaddress', (YLeaf(YType.str, 'docsIfCmtsCmStatusIpAddress'), ['str'])),
                    ('docsifcmtscmstatusdownchannelifindex', (YLeaf(YType.int32, 'docsIfCmtsCmStatusDownChannelIfIndex'), ['int'])),
                    ('docsifcmtscmstatusupchannelifindex', (YLeaf(YType.int32, 'docsIfCmtsCmStatusUpChannelIfIndex'), ['int'])),
                    ('docsifcmtscmstatusrxpower', (YLeaf(YType.int32, 'docsIfCmtsCmStatusRxPower'), ['int'])),
                    ('docsifcmtscmstatustimingoffset', (YLeaf(YType.uint32, 'docsIfCmtsCmStatusTimingOffset'), ['int'])),
                    ('docsifcmtscmstatusequalizationdata', (YLeaf(YType.str, 'docsIfCmtsCmStatusEqualizationData'), ['str'])),
                    ('docsifcmtscmstatusvalue', (YLeaf(YType.enumeration, 'docsIfCmtsCmStatusValue'), [('ydk.models.cisco_ios_xe.DOCS_IF_MIB', 'DOCSIFMIB', 'DocsIfCmtsCmStatusTable.DocsIfCmtsCmStatusEntry.DocsIfCmtsCmStatusValue')])),
                    ('docsifcmtscmstatusunerroreds', (YLeaf(YType.uint32, 'docsIfCmtsCmStatusUnerroreds'), ['int'])),
                    ('docsifcmtscmstatuscorrecteds', (YLeaf(YType.uint32, 'docsIfCmtsCmStatusCorrecteds'), ['int'])),
                    ('docsifcmtscmstatusuncorrectables', (YLeaf(YType.uint32, 'docsIfCmtsCmStatusUncorrectables'), ['int'])),
                    ('docsifcmtscmstatussignalnoise', (YLeaf(YType.int32, 'docsIfCmtsCmStatusSignalNoise'), ['int'])),
                    ('docsifcmtscmstatusmicroreflections', (YLeaf(YType.int32, 'docsIfCmtsCmStatusMicroreflections'), ['int'])),
                    ('docsifcmtscmstatusextunerroreds', (YLeaf(YType.uint64, 'docsIfCmtsCmStatusExtUnerroreds'), ['int'])),
                    ('docsifcmtscmstatusextcorrecteds', (YLeaf(YType.uint64, 'docsIfCmtsCmStatusExtCorrecteds'), ['int'])),
                    ('docsifcmtscmstatusextuncorrectables', (YLeaf(YType.uint64, 'docsIfCmtsCmStatusExtUncorrectables'), ['int'])),
                    ('docsifcmtscmstatusdocsisregmode', (YLeaf(YType.enumeration, 'docsIfCmtsCmStatusDocsisRegMode'), [('ydk.models.cisco_ios_xe.DOCS_IF_MIB', 'DocsisQosVersion', '')])),
                    ('docsifcmtscmstatusmodulationtype', (YLeaf(YType.enumeration, 'docsIfCmtsCmStatusModulationType'), [('ydk.models.cisco_ios_xe.DOCS_IF_MIB', 'DocsisUpstreamTypeStatus', '')])),
                    ('docsifcmtscmstatusinetaddresstype', (YLeaf(YType.enumeration, 'docsIfCmtsCmStatusInetAddressType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('docsifcmtscmstatusinetaddress', (YLeaf(YType.str, 'docsIfCmtsCmStatusInetAddress'), ['str'])),
                    ('docsifcmtscmstatusvaluelastupdate', (YLeaf(YType.uint32, 'docsIfCmtsCmStatusValueLastUpdate'), ['int'])),
                ])
                self.docsifcmtscmstatusindex = None
                self.docsifcmtscmstatusmacaddress = None
                self.docsifcmtscmstatusipaddress = None
                self.docsifcmtscmstatusdownchannelifindex = None
                self.docsifcmtscmstatusupchannelifindex = None
                self.docsifcmtscmstatusrxpower = None
                self.docsifcmtscmstatustimingoffset = None
                self.docsifcmtscmstatusequalizationdata = None
                self.docsifcmtscmstatusvalue = None
                self.docsifcmtscmstatusunerroreds = None
                self.docsifcmtscmstatuscorrecteds = None
                self.docsifcmtscmstatusuncorrectables = None
                self.docsifcmtscmstatussignalnoise = None
                self.docsifcmtscmstatusmicroreflections = None
                self.docsifcmtscmstatusextunerroreds = None
                self.docsifcmtscmstatusextcorrecteds = None
                self.docsifcmtscmstatusextuncorrectables = None
                self.docsifcmtscmstatusdocsisregmode = None
                self.docsifcmtscmstatusmodulationtype = None
                self.docsifcmtscmstatusinetaddresstype = None
                self.docsifcmtscmstatusinetaddress = None
                self.docsifcmtscmstatusvaluelastupdate = None
                self._segment_path = lambda: "docsIfCmtsCmStatusEntry" + "[docsIfCmtsCmStatusIndex='" + str(self.docsifcmtscmstatusindex) + "']"
                self._absolute_path = lambda: "DOCS-IF-MIB:DOCS-IF-MIB/docsIfCmtsCmStatusTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIFMIB.DocsIfCmtsCmStatusTable.DocsIfCmtsCmStatusEntry, [u'docsifcmtscmstatusindex', u'docsifcmtscmstatusmacaddress', u'docsifcmtscmstatusipaddress', u'docsifcmtscmstatusdownchannelifindex', u'docsifcmtscmstatusupchannelifindex', u'docsifcmtscmstatusrxpower', u'docsifcmtscmstatustimingoffset', u'docsifcmtscmstatusequalizationdata', u'docsifcmtscmstatusvalue', u'docsifcmtscmstatusunerroreds', u'docsifcmtscmstatuscorrecteds', u'docsifcmtscmstatusuncorrectables', u'docsifcmtscmstatussignalnoise', u'docsifcmtscmstatusmicroreflections', u'docsifcmtscmstatusextunerroreds', u'docsifcmtscmstatusextcorrecteds', u'docsifcmtscmstatusextuncorrectables', u'docsifcmtscmstatusdocsisregmode', u'docsifcmtscmstatusmodulationtype', u'docsifcmtscmstatusinetaddresstype', u'docsifcmtscmstatusinetaddress', u'docsifcmtscmstatusvaluelastupdate'], name, value)

            class DocsIfCmtsCmStatusValue(Enum):
                """
                DocsIfCmtsCmStatusValue (Enum Class)

                Current Cable Modem connectivity state, as specified

                in the RF Interface Specification. Returned status

                information is the CM status as assumed by the CMTS,

                and indicates the following events\:

                other(1)

                   Any state other than below.

                ranging(2)

                   The CMTS has received an Initial Ranging Request

                   message from the CM, and the ranging process is not  yet 

                   complete.

                rangingAborted(3)

                   The CMTS has sent a Ranging Abort message to the CM.

                rangingComplete(4)

                   The CMTS has sent a Ranging Complete message to the CM.

                ipComplete(5)

                   The CMTS has received a DHCP reply message and forwarded

                   it to the CM.

                registrationComplete(6)

                   The CMTS has sent a Registration Response message to the CM.

                accessDenied(7)

                   The CMTS has sent a Registration Aborted message

                   to the CM.

                \-\-           deprecated value

                \-\-           operational(8)

                \-\-              If Baseline Privacy is enabled for the CM, the CMTS

                \-\-              has completed Baseline Privacy initialization. If Baseline

                \-\-              Privacy is not enabled, equivalent to registrationComplete.

                registeredBPIInitializing(9)

                   Baseline Privacy is enabled, CMTS is in the process of 

                   completing the Baseline Privacy initialization. This state 

                   can last for a significant time in the case of failures 

                   during The process. After Baseline Privacy initialization 

                   Complete, the CMTS will report back the value

                   registrationComplete(6).

                   The CMTS only needs to report states it is able to detect.

                .. data:: other = 1

                .. data:: ranging = 2

                .. data:: rangingAborted = 3

                .. data:: rangingComplete = 4

                .. data:: ipComplete = 5

                .. data:: registrationComplete = 6

                .. data:: accessDenied = 7

                .. data:: operational = 8

                .. data:: registeredBPIInitializing = 9

                """

                other = Enum.YLeaf(1, "other")

                ranging = Enum.YLeaf(2, "ranging")

                rangingAborted = Enum.YLeaf(3, "rangingAborted")

                rangingComplete = Enum.YLeaf(4, "rangingComplete")

                ipComplete = Enum.YLeaf(5, "ipComplete")

                registrationComplete = Enum.YLeaf(6, "registrationComplete")

                accessDenied = Enum.YLeaf(7, "accessDenied")

                operational = Enum.YLeaf(8, "operational")

                registeredBPIInitializing = Enum.YLeaf(9, "registeredBPIInitializing")



    class DocsIfCmtsServiceTable(Entity):
        """
        Describes the attributes of upstream service queues
        in a Cable Modem Termination System.
        
        .. attribute:: docsifcmtsserviceentry
        
        	Describes the attributes of a single upstream bandwidth service queue. Entries in this table exist for each ifEntry with an ifType of docsCableMaclayer(127), and for each service queue (Service ID) within this MAC layer. Entries in this table are created with the creation of individual Service IDs by the MAC layer and removed when a Service ID is removed
        	**type**\: list of  		 :py:class:`DocsIfCmtsServiceEntry <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmtsServiceTable.DocsIfCmtsServiceEntry>`
        
        

        """

        _prefix = 'DOCS-IF-MIB'
        _revision = '2007-09-12'

        def __init__(self):
            super(DOCSIFMIB.DocsIfCmtsServiceTable, self).__init__()

            self.yang_name = "docsIfCmtsServiceTable"
            self.yang_parent_name = "DOCS-IF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIfCmtsServiceEntry", ("docsifcmtsserviceentry", DOCSIFMIB.DocsIfCmtsServiceTable.DocsIfCmtsServiceEntry))])
            self._leafs = OrderedDict()

            self.docsifcmtsserviceentry = YList(self)
            self._segment_path = lambda: "docsIfCmtsServiceTable"
            self._absolute_path = lambda: "DOCS-IF-MIB:DOCS-IF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIFMIB.DocsIfCmtsServiceTable, [], name, value)


        class DocsIfCmtsServiceEntry(Entity):
            """
            Describes the attributes of a single upstream bandwidth
            service queue.
            Entries in this table exist for each ifEntry with an
            ifType of docsCableMaclayer(127), and for each service
            queue (Service ID) within this MAC layer.
            Entries in this table are created with the creation of
            individual Service IDs by the MAC layer and removed
            when a Service ID is removed.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsifcmtsserviceid  (key)
            
            	Identifies a service queue for upstream bandwidth. The attributes of this service queue are shared between the Cable Modem and the Cable Modem Termination System. The CMTS allocates upstream bandwidth to this service queue based on requests from the CM and on the class of service associated with this queue
            	**type**\: int
            
            	**range:** 1..16383
            
            .. attribute:: docsifcmtsservicecmstatusindex
            
            	Pointer to an entry in docsIfCmtsCmStatusTable identifying the Cable Modem using this Service Queue. If multiple Cable Modems are using this Service Queue, the value of this object is zero. This object has been deprecated and replaced by docsIfCmtsServiceNewCmStatusIndex, to fix a mismatch of the value range with respect to docsIfCmtsCmStatusIndex (1..2147483647)
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**status**\: deprecated
            
            .. attribute:: docsifcmtsserviceadminstatus
            
            	Allows a service class for a particular modem to be suppressed, (re\-)enabled, or deleted altogether
            	**type**\:  :py:class:`DocsIfCmtsServiceAdminStatus <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmtsServiceTable.DocsIfCmtsServiceEntry.DocsIfCmtsServiceAdminStatus>`
            
            .. attribute:: docsifcmtsserviceqosprofile
            
            	The index in docsIfQosProfileTable describing the quality of service attributes associated with this particular service. If no associated docsIfQosProfileTable entry exists, this object returns a value of zero
            	**type**\: int
            
            	**range:** 0..16383
            
            .. attribute:: docsifcmtsservicecreatetime
            
            	The value of sysUpTime when this entry was created
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmtsserviceinoctets
            
            	The cumulative number of Packet Data octets received on this Service ID. The count does not include the size of the Cable MAC header
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmtsserviceinpackets
            
            	The cumulative number of Packet Data packets received on this Service ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmtsservicenewcmstatusindex
            
            	Pointer (via docsIfCmtsCmStatusIndex) to an entry in docsIfCmtsCmStatusTable identifying the Cable Modem using this Service Queue. If multiple Cable Modems are using this Service Queue, the value of this object is zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            

            """

            _prefix = 'DOCS-IF-MIB'
            _revision = '2007-09-12'

            def __init__(self):
                super(DOCSIFMIB.DocsIfCmtsServiceTable.DocsIfCmtsServiceEntry, self).__init__()

                self.yang_name = "docsIfCmtsServiceEntry"
                self.yang_parent_name = "docsIfCmtsServiceTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','docsifcmtsserviceid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsifcmtsserviceid', (YLeaf(YType.int32, 'docsIfCmtsServiceId'), ['int'])),
                    ('docsifcmtsservicecmstatusindex', (YLeaf(YType.int32, 'docsIfCmtsServiceCmStatusIndex'), ['int'])),
                    ('docsifcmtsserviceadminstatus', (YLeaf(YType.enumeration, 'docsIfCmtsServiceAdminStatus'), [('ydk.models.cisco_ios_xe.DOCS_IF_MIB', 'DOCSIFMIB', 'DocsIfCmtsServiceTable.DocsIfCmtsServiceEntry.DocsIfCmtsServiceAdminStatus')])),
                    ('docsifcmtsserviceqosprofile', (YLeaf(YType.int32, 'docsIfCmtsServiceQosProfile'), ['int'])),
                    ('docsifcmtsservicecreatetime', (YLeaf(YType.uint32, 'docsIfCmtsServiceCreateTime'), ['int'])),
                    ('docsifcmtsserviceinoctets', (YLeaf(YType.uint32, 'docsIfCmtsServiceInOctets'), ['int'])),
                    ('docsifcmtsserviceinpackets', (YLeaf(YType.uint32, 'docsIfCmtsServiceInPackets'), ['int'])),
                    ('docsifcmtsservicenewcmstatusindex', (YLeaf(YType.int32, 'docsIfCmtsServiceNewCmStatusIndex'), ['int'])),
                ])
                self.ifindex = None
                self.docsifcmtsserviceid = None
                self.docsifcmtsservicecmstatusindex = None
                self.docsifcmtsserviceadminstatus = None
                self.docsifcmtsserviceqosprofile = None
                self.docsifcmtsservicecreatetime = None
                self.docsifcmtsserviceinoctets = None
                self.docsifcmtsserviceinpackets = None
                self.docsifcmtsservicenewcmstatusindex = None
                self._segment_path = lambda: "docsIfCmtsServiceEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[docsIfCmtsServiceId='" + str(self.docsifcmtsserviceid) + "']"
                self._absolute_path = lambda: "DOCS-IF-MIB:DOCS-IF-MIB/docsIfCmtsServiceTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIFMIB.DocsIfCmtsServiceTable.DocsIfCmtsServiceEntry, [u'ifindex', u'docsifcmtsserviceid', u'docsifcmtsservicecmstatusindex', u'docsifcmtsserviceadminstatus', u'docsifcmtsserviceqosprofile', u'docsifcmtsservicecreatetime', u'docsifcmtsserviceinoctets', u'docsifcmtsserviceinpackets', u'docsifcmtsservicenewcmstatusindex'], name, value)

            class DocsIfCmtsServiceAdminStatus(Enum):
                """
                DocsIfCmtsServiceAdminStatus (Enum Class)

                Allows a service class for a particular modem to be

                suppressed, (re\-)enabled, or deleted altogether.

                .. data:: enabled = 1

                .. data:: disabled = 2

                .. data:: destroyed = 3

                """

                enabled = Enum.YLeaf(1, "enabled")

                disabled = Enum.YLeaf(2, "disabled")

                destroyed = Enum.YLeaf(3, "destroyed")



    class DocsIfCmtsModulationTable(Entity):
        """
        Describes a modulation profile associated with one or more
        upstream channels.
        
        .. attribute:: docsifcmtsmodulationentry
        
        	Describes a modulation profile for an Interval Usage Code for one or more upstream channels. Entries in this table are created by the operator. Initial default entries may be created at system initialization time. No individual objects have to be specified in order to create an entry in this table. Note that some objects do not have DEFVALs, but do have calculated defaults and need not be specified during row creation. There is no restriction on the changing of values in this table while their associated rows are active
        	**type**\: list of  		 :py:class:`DocsIfCmtsModulationEntry <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmtsModulationTable.DocsIfCmtsModulationEntry>`
        
        

        """

        _prefix = 'DOCS-IF-MIB'
        _revision = '2007-09-12'

        def __init__(self):
            super(DOCSIFMIB.DocsIfCmtsModulationTable, self).__init__()

            self.yang_name = "docsIfCmtsModulationTable"
            self.yang_parent_name = "DOCS-IF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIfCmtsModulationEntry", ("docsifcmtsmodulationentry", DOCSIFMIB.DocsIfCmtsModulationTable.DocsIfCmtsModulationEntry))])
            self._leafs = OrderedDict()

            self.docsifcmtsmodulationentry = YList(self)
            self._segment_path = lambda: "docsIfCmtsModulationTable"
            self._absolute_path = lambda: "DOCS-IF-MIB:DOCS-IF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIFMIB.DocsIfCmtsModulationTable, [], name, value)


        class DocsIfCmtsModulationEntry(Entity):
            """
            Describes a modulation profile for an Interval Usage Code
            for one or more upstream channels.
            Entries in this table are created by the operator. Initial
            default entries may be created at system initialization
            time. No individual objects have to be specified in order
            to create an entry in this table.
            Note that some objects do not have DEFVALs, but do have
            calculated defaults and need not be specified during row
            creation.
            There is no restriction on the changing of values in this
            table while their associated rows are active.
            
            .. attribute:: docsifcmtsmodindex  (key)
            
            	An index into the Channel Modulation table representing a group of Interval Usage Codes, all associated with the same channel
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: docsifcmtsmodintervalusagecode  (key)
            
            	An index into the Channel Modulation table which, when grouped with other Interval Usage Codes, fully instantiate all modulation sets for a given upstream channel
            	**type**\:  :py:class:`DocsIfCmtsModIntervalUsageCode <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmtsModulationTable.DocsIfCmtsModulationEntry.DocsIfCmtsModIntervalUsageCode>`
            
            .. attribute:: docsifcmtsmodcontrol
            
            	Controls and reflects the status of rows in this table
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: docsifcmtsmodtype
            
            	The modulation type used on this channel. Returns other(1) if the modulation type is neither  qpsk, qam16, qam8, qam32, qam64 or qam128. Type qam128 is used for SCDMA channels only. See the reference for the modulation profiles implied by different modulation types
            	**type**\:  :py:class:`DocsIfCmtsModType <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmtsModulationTable.DocsIfCmtsModulationEntry.DocsIfCmtsModType>`
            
            .. attribute:: docsifcmtsmodpreamblelen
            
            	The preamble length for this modulation profile in bits. Default value is the minimum needed by the implementation at the CMTS for the given modulation profile
            	**type**\: int
            
            	**range:** 0..1536
            
            .. attribute:: docsifcmtsmoddifferentialencoding
            
            	Specifies whether or not differential encoding is used on this channel
            	**type**\: bool
            
            .. attribute:: docsifcmtsmodfecerrorcorrection
            
            	The number of correctable errored bytes (t) used in forward error correction code. The value of 0 indicates no correction is employed. The number of check bytes appended will be twice this value
            	**type**\: int
            
            	**range:** 0..16
            
            .. attribute:: docsifcmtsmodfeccodewordlength
            
            	The number of data bytes (k) in the forward error correction codeword. This object is not used if docsIfCmtsModFECErrorCorrection is zero
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: docsifcmtsmodscramblerseed
            
            	The 15 bit seed value for the scrambler polynomial
            	**type**\: int
            
            	**range:** 0..32767
            
            .. attribute:: docsifcmtsmodmaxburstsize
            
            	The maximum number of mini\-slots that can be transmitted during this channel's burst time. Returns zero if the burst length is bounded by the allocation MAP rather than this profile. Default value is 0 except for shortData, where it is 8
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: docsifcmtsmodguardtimesize
            
            	The number of symbol\-times which must follow the end of this channel's burst. Default value is the minimum time needed by the implementation for this modulation profile
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmtsmodlastcodewordshortened
            
            	Indicates if the last FEC codeword is truncated
            	**type**\: bool
            
            .. attribute:: docsifcmtsmodscrambler
            
            	Indicates if the scrambler is employed
            	**type**\: bool
            
            .. attribute:: docsifcmtsmodbyteinterleaverdepth
            
            	 ATDMA Byte Interleaver Depth (Ir). This object returns 1 for                     non ATDMA profiles. 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmtsmodbyteinterleaverblocksize
            
            	 ATDMA Byte Interleaver Block size (Br). This object returns  zero for non ATDMA profiles 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmtsmodpreambletype
            
            	Preamble type for DOCSIS 2.0 bursts. The value 'unknown(0)'  represents a row entry consisting only of DOCSIS 1.x bursts
            	**type**\:  :py:class:`DocsIfCmtsModPreambleType <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmtsModulationTable.DocsIfCmtsModulationEntry.DocsIfCmtsModPreambleType>`
            
            .. attribute:: docsifcmtsmodtcmerrorcorrectionon
            
            	 Trellis Code Modulation (TCM) On/Off. This value returns false for  non S\-CDMA profiles
            	**type**\: bool
            
            .. attribute:: docsifcmtsmodscdmainterleaverstepsize
            
            	 S\-CDMA Interleaver step size. This value returns zero  for non S\-CDMA profiles
            	**type**\: int
            
            	**range:** 0..32
            
            .. attribute:: docsifcmtsmodscdmaspreaderenable
            
            	 S\-CDMA spreader. This value returns false for non S\-CDMA profiles. Default value for IUC 3 and 4 is OFF, for  all other IUCs it is ON
            	**type**\: bool
            
            .. attribute:: docsifcmtsmodscdmasubframecodes
            
            	 S\-CDMA sub\-frame size. This value returns zero  for non S\-CDMA profiles
            	**type**\: int
            
            	**range:** 0..128
            
            .. attribute:: docsifcmtsmodchanneltype
            
            	Describes the modulation channel type for this modulation entry
            	**type**\:  :py:class:`DocsisUpstreamType <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DocsisUpstreamType>`
            
            

            """

            _prefix = 'DOCS-IF-MIB'
            _revision = '2007-09-12'

            def __init__(self):
                super(DOCSIFMIB.DocsIfCmtsModulationTable.DocsIfCmtsModulationEntry, self).__init__()

                self.yang_name = "docsIfCmtsModulationEntry"
                self.yang_parent_name = "docsIfCmtsModulationTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['docsifcmtsmodindex','docsifcmtsmodintervalusagecode']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('docsifcmtsmodindex', (YLeaf(YType.int32, 'docsIfCmtsModIndex'), ['int'])),
                    ('docsifcmtsmodintervalusagecode', (YLeaf(YType.enumeration, 'docsIfCmtsModIntervalUsageCode'), [('ydk.models.cisco_ios_xe.DOCS_IF_MIB', 'DOCSIFMIB', 'DocsIfCmtsModulationTable.DocsIfCmtsModulationEntry.DocsIfCmtsModIntervalUsageCode')])),
                    ('docsifcmtsmodcontrol', (YLeaf(YType.enumeration, 'docsIfCmtsModControl'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('docsifcmtsmodtype', (YLeaf(YType.enumeration, 'docsIfCmtsModType'), [('ydk.models.cisco_ios_xe.DOCS_IF_MIB', 'DOCSIFMIB', 'DocsIfCmtsModulationTable.DocsIfCmtsModulationEntry.DocsIfCmtsModType')])),
                    ('docsifcmtsmodpreamblelen', (YLeaf(YType.int32, 'docsIfCmtsModPreambleLen'), ['int'])),
                    ('docsifcmtsmoddifferentialencoding', (YLeaf(YType.boolean, 'docsIfCmtsModDifferentialEncoding'), ['bool'])),
                    ('docsifcmtsmodfecerrorcorrection', (YLeaf(YType.int32, 'docsIfCmtsModFECErrorCorrection'), ['int'])),
                    ('docsifcmtsmodfeccodewordlength', (YLeaf(YType.int32, 'docsIfCmtsModFECCodewordLength'), ['int'])),
                    ('docsifcmtsmodscramblerseed', (YLeaf(YType.int32, 'docsIfCmtsModScramblerSeed'), ['int'])),
                    ('docsifcmtsmodmaxburstsize', (YLeaf(YType.int32, 'docsIfCmtsModMaxBurstSize'), ['int'])),
                    ('docsifcmtsmodguardtimesize', (YLeaf(YType.uint32, 'docsIfCmtsModGuardTimeSize'), ['int'])),
                    ('docsifcmtsmodlastcodewordshortened', (YLeaf(YType.boolean, 'docsIfCmtsModLastCodewordShortened'), ['bool'])),
                    ('docsifcmtsmodscrambler', (YLeaf(YType.boolean, 'docsIfCmtsModScrambler'), ['bool'])),
                    ('docsifcmtsmodbyteinterleaverdepth', (YLeaf(YType.uint32, 'docsIfCmtsModByteInterleaverDepth'), ['int'])),
                    ('docsifcmtsmodbyteinterleaverblocksize', (YLeaf(YType.uint32, 'docsIfCmtsModByteInterleaverBlockSize'), ['int'])),
                    ('docsifcmtsmodpreambletype', (YLeaf(YType.enumeration, 'docsIfCmtsModPreambleType'), [('ydk.models.cisco_ios_xe.DOCS_IF_MIB', 'DOCSIFMIB', 'DocsIfCmtsModulationTable.DocsIfCmtsModulationEntry.DocsIfCmtsModPreambleType')])),
                    ('docsifcmtsmodtcmerrorcorrectionon', (YLeaf(YType.boolean, 'docsIfCmtsModTcmErrorCorrectionOn'), ['bool'])),
                    ('docsifcmtsmodscdmainterleaverstepsize', (YLeaf(YType.uint32, 'docsIfCmtsModScdmaInterleaverStepSize'), ['int'])),
                    ('docsifcmtsmodscdmaspreaderenable', (YLeaf(YType.boolean, 'docsIfCmtsModScdmaSpreaderEnable'), ['bool'])),
                    ('docsifcmtsmodscdmasubframecodes', (YLeaf(YType.uint32, 'docsIfCmtsModScdmaSubframeCodes'), ['int'])),
                    ('docsifcmtsmodchanneltype', (YLeaf(YType.enumeration, 'docsIfCmtsModChannelType'), [('ydk.models.cisco_ios_xe.DOCS_IF_MIB', 'DocsisUpstreamType', '')])),
                ])
                self.docsifcmtsmodindex = None
                self.docsifcmtsmodintervalusagecode = None
                self.docsifcmtsmodcontrol = None
                self.docsifcmtsmodtype = None
                self.docsifcmtsmodpreamblelen = None
                self.docsifcmtsmoddifferentialencoding = None
                self.docsifcmtsmodfecerrorcorrection = None
                self.docsifcmtsmodfeccodewordlength = None
                self.docsifcmtsmodscramblerseed = None
                self.docsifcmtsmodmaxburstsize = None
                self.docsifcmtsmodguardtimesize = None
                self.docsifcmtsmodlastcodewordshortened = None
                self.docsifcmtsmodscrambler = None
                self.docsifcmtsmodbyteinterleaverdepth = None
                self.docsifcmtsmodbyteinterleaverblocksize = None
                self.docsifcmtsmodpreambletype = None
                self.docsifcmtsmodtcmerrorcorrectionon = None
                self.docsifcmtsmodscdmainterleaverstepsize = None
                self.docsifcmtsmodscdmaspreaderenable = None
                self.docsifcmtsmodscdmasubframecodes = None
                self.docsifcmtsmodchanneltype = None
                self._segment_path = lambda: "docsIfCmtsModulationEntry" + "[docsIfCmtsModIndex='" + str(self.docsifcmtsmodindex) + "']" + "[docsIfCmtsModIntervalUsageCode='" + str(self.docsifcmtsmodintervalusagecode) + "']"
                self._absolute_path = lambda: "DOCS-IF-MIB:DOCS-IF-MIB/docsIfCmtsModulationTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIFMIB.DocsIfCmtsModulationTable.DocsIfCmtsModulationEntry, [u'docsifcmtsmodindex', u'docsifcmtsmodintervalusagecode', u'docsifcmtsmodcontrol', u'docsifcmtsmodtype', u'docsifcmtsmodpreamblelen', u'docsifcmtsmoddifferentialencoding', u'docsifcmtsmodfecerrorcorrection', u'docsifcmtsmodfeccodewordlength', u'docsifcmtsmodscramblerseed', u'docsifcmtsmodmaxburstsize', u'docsifcmtsmodguardtimesize', u'docsifcmtsmodlastcodewordshortened', u'docsifcmtsmodscrambler', u'docsifcmtsmodbyteinterleaverdepth', u'docsifcmtsmodbyteinterleaverblocksize', u'docsifcmtsmodpreambletype', u'docsifcmtsmodtcmerrorcorrectionon', u'docsifcmtsmodscdmainterleaverstepsize', u'docsifcmtsmodscdmaspreaderenable', u'docsifcmtsmodscdmasubframecodes', u'docsifcmtsmodchanneltype'], name, value)

            class DocsIfCmtsModIntervalUsageCode(Enum):
                """
                DocsIfCmtsModIntervalUsageCode (Enum Class)

                An index into the Channel Modulation table which, when

                grouped with other Interval Usage Codes, fully

                instantiate all modulation sets for a given upstream

                channel.

                .. data:: request = 1

                .. data:: requestData = 2

                .. data:: initialRanging = 3

                .. data:: periodicRanging = 4

                .. data:: shortData = 5

                .. data:: longData = 6

                .. data:: advPhyShortData = 9

                .. data:: advPhyLongData = 10

                .. data:: ugs = 11

                """

                request = Enum.YLeaf(1, "request")

                requestData = Enum.YLeaf(2, "requestData")

                initialRanging = Enum.YLeaf(3, "initialRanging")

                periodicRanging = Enum.YLeaf(4, "periodicRanging")

                shortData = Enum.YLeaf(5, "shortData")

                longData = Enum.YLeaf(6, "longData")

                advPhyShortData = Enum.YLeaf(9, "advPhyShortData")

                advPhyLongData = Enum.YLeaf(10, "advPhyLongData")

                ugs = Enum.YLeaf(11, "ugs")


            class DocsIfCmtsModPreambleType(Enum):
                """
                DocsIfCmtsModPreambleType (Enum Class)

                Preamble type for DOCSIS 2.0 bursts. The value 'unknown(0)' 

                represents a row entry consisting only of DOCSIS 1.x bursts.

                .. data:: unknown = 0

                .. data:: qpsk0 = 1

                .. data:: qpsk1 = 2

                """

                unknown = Enum.YLeaf(0, "unknown")

                qpsk0 = Enum.YLeaf(1, "qpsk0")

                qpsk1 = Enum.YLeaf(2, "qpsk1")


            class DocsIfCmtsModType(Enum):
                """
                DocsIfCmtsModType (Enum Class)

                The modulation type used on this channel. Returns

                other(1) if the modulation type is neither 

                qpsk, qam16, qam8, qam32, qam64 or qam128.

                Type qam128 is used for SCDMA channels only.

                See the reference for the modulation profiles

                implied by different modulation types.

                .. data:: other = 1

                .. data:: qpsk = 2

                .. data:: qam16 = 3

                .. data:: qam8 = 4

                .. data:: qam32 = 5

                .. data:: qam64 = 6

                .. data:: qam128 = 7

                """

                other = Enum.YLeaf(1, "other")

                qpsk = Enum.YLeaf(2, "qpsk")

                qam16 = Enum.YLeaf(3, "qam16")

                qam8 = Enum.YLeaf(4, "qam8")

                qam32 = Enum.YLeaf(5, "qam32")

                qam64 = Enum.YLeaf(6, "qam64")

                qam128 = Enum.YLeaf(7, "qam128")



    class DocsIfCmtsMacToCmTable(Entity):
        """
        This is a table to provide a quick access index into the
        docsIfCmtsCmStatusTable. There is exactly one row in this
        table for each row in the docsIfCmtsCmStatusTable. In
        general, the management station should use this table only
        to get a pointer into the docsIfCmtsCmStatusTable (which
        corresponds to the CM's RF interface MAC address), and
        should not iterate (e.g. GetNext through) this table.
        
        .. attribute:: docsifcmtsmactocmentry
        
        	A row in the docsIfCmtsMacToCmTable. An entry in this table exists for each Cable Modem that is connected to the CMTS implementing this table
        	**type**\: list of  		 :py:class:`DocsIfCmtsMacToCmEntry <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmtsMacToCmTable.DocsIfCmtsMacToCmEntry>`
        
        

        """

        _prefix = 'DOCS-IF-MIB'
        _revision = '2007-09-12'

        def __init__(self):
            super(DOCSIFMIB.DocsIfCmtsMacToCmTable, self).__init__()

            self.yang_name = "docsIfCmtsMacToCmTable"
            self.yang_parent_name = "DOCS-IF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIfCmtsMacToCmEntry", ("docsifcmtsmactocmentry", DOCSIFMIB.DocsIfCmtsMacToCmTable.DocsIfCmtsMacToCmEntry))])
            self._leafs = OrderedDict()

            self.docsifcmtsmactocmentry = YList(self)
            self._segment_path = lambda: "docsIfCmtsMacToCmTable"
            self._absolute_path = lambda: "DOCS-IF-MIB:DOCS-IF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIFMIB.DocsIfCmtsMacToCmTable, [], name, value)


        class DocsIfCmtsMacToCmEntry(Entity):
            """
            A row in the docsIfCmtsMacToCmTable.
            An entry in this table exists for each Cable Modem
            that is connected to the CMTS implementing this table.
            
            .. attribute:: docsifcmtscmmac  (key)
            
            	The RF side MAC address for the referenced CM. (E.g. the interface on the CM that has docsCableMacLayer(127) as its ifType
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: docsifcmtscmptr
            
            	An row index into docsIfCmtsCmStatusTable. When queried with the correct instance value (e.g. a CM's MAC address), returns the index in docsIfCmtsCmStatusTable which represents that CM
            	**type**\: int
            
            	**range:** 1..2147483647
            
            

            """

            _prefix = 'DOCS-IF-MIB'
            _revision = '2007-09-12'

            def __init__(self):
                super(DOCSIFMIB.DocsIfCmtsMacToCmTable.DocsIfCmtsMacToCmEntry, self).__init__()

                self.yang_name = "docsIfCmtsMacToCmEntry"
                self.yang_parent_name = "docsIfCmtsMacToCmTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['docsifcmtscmmac']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('docsifcmtscmmac', (YLeaf(YType.str, 'docsIfCmtsCmMac'), ['str'])),
                    ('docsifcmtscmptr', (YLeaf(YType.int32, 'docsIfCmtsCmPtr'), ['int'])),
                ])
                self.docsifcmtscmmac = None
                self.docsifcmtscmptr = None
                self._segment_path = lambda: "docsIfCmtsMacToCmEntry" + "[docsIfCmtsCmMac='" + str(self.docsifcmtscmmac) + "']"
                self._absolute_path = lambda: "DOCS-IF-MIB:DOCS-IF-MIB/docsIfCmtsMacToCmTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIFMIB.DocsIfCmtsMacToCmTable.DocsIfCmtsMacToCmEntry, [u'docsifcmtscmmac', u'docsifcmtscmptr'], name, value)


    class DocsIfCmtsChannelUtilizationTable(Entity):
        """
        Reports utilization statistics for attached upstream and
        downstream physical channels.
        
        .. attribute:: docsifcmtschannelutilizationentry
        
        	Utilization statistics for a single upstream or downstream physical channel. An entry exists in this table for each ifEntry with an ifType equal to docsCableDownstreamInterface (128) or docsCableUpstreamInterface (129)
        	**type**\: list of  		 :py:class:`DocsIfCmtsChannelUtilizationEntry <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmtsChannelUtilizationTable.DocsIfCmtsChannelUtilizationEntry>`
        
        

        """

        _prefix = 'DOCS-IF-MIB'
        _revision = '2007-09-12'

        def __init__(self):
            super(DOCSIFMIB.DocsIfCmtsChannelUtilizationTable, self).__init__()

            self.yang_name = "docsIfCmtsChannelUtilizationTable"
            self.yang_parent_name = "DOCS-IF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIfCmtsChannelUtilizationEntry", ("docsifcmtschannelutilizationentry", DOCSIFMIB.DocsIfCmtsChannelUtilizationTable.DocsIfCmtsChannelUtilizationEntry))])
            self._leafs = OrderedDict()

            self.docsifcmtschannelutilizationentry = YList(self)
            self._segment_path = lambda: "docsIfCmtsChannelUtilizationTable"
            self._absolute_path = lambda: "DOCS-IF-MIB:DOCS-IF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIFMIB.DocsIfCmtsChannelUtilizationTable, [], name, value)


        class DocsIfCmtsChannelUtilizationEntry(Entity):
            """
            Utilization statistics for a single upstream or downstream
            physical channel. An entry exists in this table for each
            ifEntry with an ifType equal to docsCableDownstreamInterface
            (128) or docsCableUpstreamInterface (129).
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsifcmtschannelutiftype  (key)
            
            	The secondary index into this table. Indicates the IANA interface type associated with this physical channel. Only docsCableDownstreamInterface (128) and docsCableUpstreamInterface (129) are valid
            	**type**\:  :py:class:`IANAifType <ydk.models.cisco_ios_xe.IANAifType_MIB.IANAifType>`
            
            .. attribute:: docsifcmtschannelutid  (key)
            
            	The tertiary index into this table. Indicates the CMTS identifier for this physical channel
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: docsifcmtschannelututilization
            
            	The calculated and truncated utilization index for this physical upstream or downstream channel, accurate as of  the most recent docsIfCmtsChannelUtilizationInterval.  Upstream Channel Utilization Index\: The upstream channel utilization index is expressed as a  percentage of minislots utilized on the physical channel, regardless  of burst type. For an Initial Maintenance region, the minislots  for the complete region are considered utilized if the CMTS  received an upstream burst within the region from any CM on the  physical channel.  For contention REQ and REQ/DATA regions, the     minislots for a transmission opportunity within the region are  considered utilized if the CMTS received an upstream burst within  the opportunity from any CM on the physical channel. For all other  regions, utilized minislots are those in which the CMTS granted bandwidth to any unicast SID on the physical channel.  For an upstream interface that has multiple logical upstream  channels enabled, the utilization index is a weighted sum of  utilization indices for the logical channels. The weight for  each utilization index is the percentage of upstream minislots  allocated for the corresponding logical channel. Example\:  If 75% of bandwidth is allocated to the first logical channel  and 25% to the second, and the utilization indices for each are  60 and 40 respectively, the utilization index for the upstream  physical channel is (60 \* 0.75) + (40 \* 0.25) = 55. This figure  applies to the most recent utilization interval.   Downstream Channel Utilization Index\: The downstream channel utilization index is a percentage expressing  the ratio between bytes used to transmit data versus the total number  of bytes transmitted in the raw bandwidth of the MPEG channel. As with the upstream utilization index, the calculated value represents  the most recent utilization interval. Formula\: Downstream utilization index =  (100 \* (data bytes / raw bytes)) =  (100 \* ((raw bytes \- stuffed bytes) / raw bytes))  Definitions\: Data bytes\: Number of bytes transmitted as data in the                                         docsIfCmtsChannelUtilizationInterval.  Stuffed bytes\: Number of filler bytes transmitted as non\-data in the                 DocsIfCmtsChannelUtilizationInterval. Raw bandwidth\: Total number of bytes available for transmitting data,                not including bytes used for headers and other overhead. Raw bytes\: (raw bandwidth \* docsIfCmtsChannelUtilizationInterval)
            	**type**\: int
            
            	**range:** 0..100
            
            	**units**\: percent
            
            

            """

            _prefix = 'DOCS-IF-MIB'
            _revision = '2007-09-12'

            def __init__(self):
                super(DOCSIFMIB.DocsIfCmtsChannelUtilizationTable.DocsIfCmtsChannelUtilizationEntry, self).__init__()

                self.yang_name = "docsIfCmtsChannelUtilizationEntry"
                self.yang_parent_name = "docsIfCmtsChannelUtilizationTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','docsifcmtschannelutiftype','docsifcmtschannelutid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsifcmtschannelutiftype', (YLeaf(YType.enumeration, 'docsIfCmtsChannelUtIfType'), [('ydk.models.cisco_ios_xe.IANAifType_MIB', 'IANAifType', '')])),
                    ('docsifcmtschannelutid', (YLeaf(YType.int32, 'docsIfCmtsChannelUtId'), ['int'])),
                    ('docsifcmtschannelututilization', (YLeaf(YType.int32, 'docsIfCmtsChannelUtUtilization'), ['int'])),
                ])
                self.ifindex = None
                self.docsifcmtschannelutiftype = None
                self.docsifcmtschannelutid = None
                self.docsifcmtschannelututilization = None
                self._segment_path = lambda: "docsIfCmtsChannelUtilizationEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[docsIfCmtsChannelUtIfType='" + str(self.docsifcmtschannelutiftype) + "']" + "[docsIfCmtsChannelUtId='" + str(self.docsifcmtschannelutid) + "']"
                self._absolute_path = lambda: "DOCS-IF-MIB:DOCS-IF-MIB/docsIfCmtsChannelUtilizationTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIFMIB.DocsIfCmtsChannelUtilizationTable.DocsIfCmtsChannelUtilizationEntry, [u'ifindex', u'docsifcmtschannelutiftype', u'docsifcmtschannelutid', u'docsifcmtschannelututilization'], name, value)


    class DocsIfCmtsDownChannelCounterTable(Entity):
        """
        This table is implemented at the CMTS to collect downstream
        channel statistics for utilization calculations.
        
        .. attribute:: docsifcmtsdownchannelcounterentry
        
        	An entry provides a list of traffic counters for a single downstream channel. An entry in this table exists for each ifEntry with an ifType of docsCableDownstream(128)
        	**type**\: list of  		 :py:class:`DocsIfCmtsDownChannelCounterEntry <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmtsDownChannelCounterTable.DocsIfCmtsDownChannelCounterEntry>`
        
        

        """

        _prefix = 'DOCS-IF-MIB'
        _revision = '2007-09-12'

        def __init__(self):
            super(DOCSIFMIB.DocsIfCmtsDownChannelCounterTable, self).__init__()

            self.yang_name = "docsIfCmtsDownChannelCounterTable"
            self.yang_parent_name = "DOCS-IF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIfCmtsDownChannelCounterEntry", ("docsifcmtsdownchannelcounterentry", DOCSIFMIB.DocsIfCmtsDownChannelCounterTable.DocsIfCmtsDownChannelCounterEntry))])
            self._leafs = OrderedDict()

            self.docsifcmtsdownchannelcounterentry = YList(self)
            self._segment_path = lambda: "docsIfCmtsDownChannelCounterTable"
            self._absolute_path = lambda: "DOCS-IF-MIB:DOCS-IF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIFMIB.DocsIfCmtsDownChannelCounterTable, [], name, value)


        class DocsIfCmtsDownChannelCounterEntry(Entity):
            """
            An entry provides a list of traffic counters for a single
            downstream channel.
            An entry in this table exists for each ifEntry with an
            ifType of docsCableDownstream(128).
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsifcmtsdownchnlctrid
            
            	The Cable Modem Termination System (CMTS) identification of the downstream channel within this particular MAC interface. If the interface is down, the object returns the most current value. If the downstream channel ID is unknown, this object returns a value of 0
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: docsifcmtsdownchnlctrtotalbytes
            
            	At the CMTS, the total number of bytes in the Payload portion of MPEG Packets (ie. not including MPEG header or pointer\_field) transported by this downstream channel since CMTS initialization. This is the 32 bit version of docsIfCmtsDownChnlCtrExtTotalBytes, included to provide back compatibility with SNMPv1 managers
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmtsdownchnlctrusedbytes
            
            	At the CMTS, the total number of DOCSIS data bytes transported by this downstream channel since CMTS initialization. The number of data bytes is defined as the total number of bytes transported in DOCSIS payloads minus the number of stuff bytes transported in DOCSIS payloads. This is the 32 bit version of docsIfCmtsDownChnlCtrExtUsedBytes, included to provide back compatibility with SNMPv1 managers
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmtsdownchnlctrexttotalbytes
            
            	At the CMTS, the total number of bytes in the Payload portion of MPEG Packets (ie. not including MPEG header or pointer\_field) transported by this downstream channel since CMTS initialization. This is the 64 bit version of docsIfCmtsDownChnlCtrTotalBytes, and will not be accessible to SNMPv1 managers
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: docsifcmtsdownchnlctrextusedbytes
            
            	At the CMTS, the total number of DOCSIS data bytes transported by this downstream channel since CMTS initialization. The number of data bytes is defined as the total number of bytes transported in DOCSIS payloads minus the number of stuff bytes transported in DOCSIS payloads. This is the 64 bit version of docsIfCmtsDownChnlCtrUsedBytes, and will not be accessible to SNMPv1 managers
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'DOCS-IF-MIB'
            _revision = '2007-09-12'

            def __init__(self):
                super(DOCSIFMIB.DocsIfCmtsDownChannelCounterTable.DocsIfCmtsDownChannelCounterEntry, self).__init__()

                self.yang_name = "docsIfCmtsDownChannelCounterEntry"
                self.yang_parent_name = "docsIfCmtsDownChannelCounterTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsifcmtsdownchnlctrid', (YLeaf(YType.int32, 'docsIfCmtsDownChnlCtrId'), ['int'])),
                    ('docsifcmtsdownchnlctrtotalbytes', (YLeaf(YType.uint32, 'docsIfCmtsDownChnlCtrTotalBytes'), ['int'])),
                    ('docsifcmtsdownchnlctrusedbytes', (YLeaf(YType.uint32, 'docsIfCmtsDownChnlCtrUsedBytes'), ['int'])),
                    ('docsifcmtsdownchnlctrexttotalbytes', (YLeaf(YType.uint64, 'docsIfCmtsDownChnlCtrExtTotalBytes'), ['int'])),
                    ('docsifcmtsdownchnlctrextusedbytes', (YLeaf(YType.uint64, 'docsIfCmtsDownChnlCtrExtUsedBytes'), ['int'])),
                ])
                self.ifindex = None
                self.docsifcmtsdownchnlctrid = None
                self.docsifcmtsdownchnlctrtotalbytes = None
                self.docsifcmtsdownchnlctrusedbytes = None
                self.docsifcmtsdownchnlctrexttotalbytes = None
                self.docsifcmtsdownchnlctrextusedbytes = None
                self._segment_path = lambda: "docsIfCmtsDownChannelCounterEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "DOCS-IF-MIB:DOCS-IF-MIB/docsIfCmtsDownChannelCounterTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIFMIB.DocsIfCmtsDownChannelCounterTable.DocsIfCmtsDownChannelCounterEntry, [u'ifindex', u'docsifcmtsdownchnlctrid', u'docsifcmtsdownchnlctrtotalbytes', u'docsifcmtsdownchnlctrusedbytes', u'docsifcmtsdownchnlctrexttotalbytes', u'docsifcmtsdownchnlctrextusedbytes'], name, value)


    class DocsIfCmtsUpChannelCounterTable(Entity):
        """
        This table is implemented at the CMTS to provide upstream
        channel statistics appropriate for channel utilization
        calculations.
        
        .. attribute:: docsifcmtsupchannelcounterentry
        
        	List of traffic statistics for a single upstream channel. For Docsis 2.0 CMTSs, an entry in this table exists for  each ifEntry with an ifType of docsCableUpstreamChannel (205). For Docsis 1.x CMTSs, an entry in this table exists for each ifEntry with an ifType of docsCableUpstreamInterface (129)
        	**type**\: list of  		 :py:class:`DocsIfCmtsUpChannelCounterEntry <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmtsUpChannelCounterTable.DocsIfCmtsUpChannelCounterEntry>`
        
        

        """

        _prefix = 'DOCS-IF-MIB'
        _revision = '2007-09-12'

        def __init__(self):
            super(DOCSIFMIB.DocsIfCmtsUpChannelCounterTable, self).__init__()

            self.yang_name = "docsIfCmtsUpChannelCounterTable"
            self.yang_parent_name = "DOCS-IF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIfCmtsUpChannelCounterEntry", ("docsifcmtsupchannelcounterentry", DOCSIFMIB.DocsIfCmtsUpChannelCounterTable.DocsIfCmtsUpChannelCounterEntry))])
            self._leafs = OrderedDict()

            self.docsifcmtsupchannelcounterentry = YList(self)
            self._segment_path = lambda: "docsIfCmtsUpChannelCounterTable"
            self._absolute_path = lambda: "DOCS-IF-MIB:DOCS-IF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIFMIB.DocsIfCmtsUpChannelCounterTable, [], name, value)


        class DocsIfCmtsUpChannelCounterEntry(Entity):
            """
            List of traffic statistics for a single upstream channel.
            For Docsis 2.0 CMTSs, an entry in this table exists for 
            each ifEntry with an ifType of docsCableUpstreamChannel (205).
            For Docsis 1.x CMTSs, an entry in this table exists for each
            ifEntry with an ifType of docsCableUpstreamInterface (129).
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsifcmtsupchnlctrid
            
            	The CMTS identification of the upstream channel
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: docsifcmtsupchnlctrtotalmslots
            
            	Current count, from CMTS initialization, of all minislots defined for this upstream logical channel. This count includes all IUCs and SIDs, even those allocated to the NULL SID for a 2.0 logical channel which is inactive. This is the 32 bit version of docsIfCmtsUpChnlCtrExtTotalMslots, and is included for back compatibility with SNMPv1 managers. Support for this object is mandatory
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmtsupchnlctrucastgrantedmslots
            
            	Current count, from CMTS initialization, of unicast granted minislots on the upstream logical channel, regardless of burst type. Unicast granted minislots are those in which the CMTS assigned bandwidth to any unicast SID on the logical channel. This is the 32 bit version of docsIfCmtsUpChnlCtrExtUcastGrantedMslots, and is included for back compatibility with SNMPv1 managers. Support for this object is mandatory
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmtsupchnlctrtotalcntnmslots
            
            	Current count, from CMTS initialization, of contention minislots defined for this upstream logical channel. This count includes all minislots assigned to a broadcast or multicast SID on the logical channel.  This is the 32 bit version of docsIfCmtsUpChnlCtrExtTotalCntnMslots, and is included for back compatibility with SNMPv1 managers. Support for this object is mandatory
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmtsupchnlctrusedcntnmslots
            
            	Current count, from CMTS initialization, of contention minislots utilized on the upstream logical channel. For contention regions, utilized minislots are those in which the CMTS correctly received an upstream burst from any CM on the upstream logical channel. This is the 32 bit version of docsIfCmtsUpChnlCtrExtUsedCntnMslots, and is included for back compatibility with SNMPv1 managers. Support for this object is mandatory
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmtsupchnlctrexttotalmslots
            
            	Current count, from CMTS initialization, of all minislots defined for this upstream logical channel. This count includes all IUCs and SIDs, even those allocated to the NULL SID for a 2.0 logical channel which is inactive. This is the 64 bit version of docsIfCmtsUpChnlCtrTotalMslots, and will not be accessible to SNMPv1 managers. Support for this object is mandatory
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: docsifcmtsupchnlctrextucastgrantedmslots
            
            	Current count, from CMTS initialization, of unicast granted minislots on the upstream logical channel, regardless of burst type. Unicast granted minislots are those in which the CMTS assigned bandwidth to any unicast SID on the logical channel. This is the 64 bit version of docsIfCmtsUpChnlCtrUcastGrantedMslots, and will not be accessible to SNMPv1 managers. Support for this object is mandatory
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: docsifcmtsupchnlctrexttotalcntnmslots
            
            	Current count, from CMTS initialization, of contention minislots defined for this upstream logical channel. This count includes all minislots assigned to a broadcast or multicast SID on the logical channel.  This is the 64 bit version of docsIfCmtsUpChnlCtrTotalCntnMslots, and will not be accessible to SNMPv1 managers. Support for this object is mandatory
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: docsifcmtsupchnlctrextusedcntnmslots
            
            	Current count, from CMTS initialization, of contention minislots utilized on the upstream logical channel. For contention regions, utilized minislots are those in which the CMTS correctly received an upstream burst from any CM on the upstream logical channel. This is the 64 bit version of docsIfCmtsUpChnlCtrUsedCntnMslots, and will not be accessible to SNMPv1 managers. Support for this object is mandatory
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: docsifcmtsupchnlctrcollcntnmslots
            
            	Current count, from CMTS initialization, of contention minislots  subjected to collisions on the upstream logical channel. For  contention regions, these are the minislots applicable to bursts  that the CMTS detected, but could not correctly receive.   This is the 32 bit version of docsIfCmtsUpChnlCtrExtCollCntnMslots, and is included for back compatibility with SNMPv1 managers. Support for this object is optional. If the object is not supported, a value of zero is returned
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmtsupchnlctrtotalcntnreqmslots
            
            	Current count, from CMTS initialization, of contention request minislots defined for this upstream logical channel. This count  includes all minislots for IUC1 assigned to a broadcast or multicast  SID on the logical channel.  This is the 32 bit version of docsIfCmtsUpChnlCtrExtTotalCntnReqMslots, and is included for back compatibility with SNMPv1 managers. Support for this object is optional. If the object is not supported, A value of zero is returned
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmtsupchnlctrusedcntnreqmslots
            
            	Current count, from CMTS initialization, of contention request minislots utilized on this upstream logical channel. This count  includes all contention minislots for IUC1 applicable to bursts that the CMTS correctly received.              This is the 32 bit version of docsIfCmtsUpChnlCtrExtUsedCntnReqMslots, and is included for back compatibility with SNMPv1 managers. Support for this object is optional. If the object is not supported, A value of zero is returned
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmtsupchnlctrcollcntnreqmslots
            
            	Current count, from CMTS initialization, of contention request minislots subjected to collisions on this upstream logical channel.   This includes all contention minislots for IUC1 applicable to bursts that the CMTS detected, but could not correctly receive.              This is the 32 bit version of docsIfCmtsUpChnlCtrExtCollCntnReqMslots, and is included for back compatibility with SNMPv1 managers. Support for this object is optional. If the object is not supported, A value of zero is returned
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmtsupchnlctrtotalcntnreqdatamslots
            
            	Current count, from CMTS initialization, of contention request data minislots defined for this upstream logical channel. This count  includes all minislots for IUC2 assigned to a broadcast or multicast  SID on the logical channel.  This is the 32 bit version of docsIfCmtsUpChnlCtrExtTotalCntnReqDataMslots, and is included for back compatibility with SNMPv1 managers. Support for this object is optional. If the object is not supported, A value of zero is returned
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmtsupchnlctrusedcntnreqdatamslots
            
            	Current count, from CMTS initialization, of contention request data minislots utilized on this upstream logical channel. This   includes all contention minislots for IUC2 applicable to bursts that the CMTS correctly received.              This is the 32 bit version of  docsIfCmtsUpChnlCtrExtUsedCntnReqDataMslots, and is included for back compatibility with SNMPv1 managers. Support for this object is optional. If the object is not supported, A value of zero is returned
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmtsupchnlctrcollcntnreqdatamslots
            
            	Current count, from CMTS initialization, of contention request data minislots subjected to collisions on this upstream logical  channel. This includes all contention minislots for IUC2 applicable  to bursts that the CMTS detected, but could not correctly receive.              This is the 32 bit version of  docsIfCmtsUpChnlCtrExtCollCntnReqDataMslots, and is included for back compatibility with SNMPv1 managers. Support for this object is optional. If the object is not supported, A value of zero is returned
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmtsupchnlctrtotalcntninitmaintmslots
            
            	Current count, from CMTS initialization, of contention initial maintenance minislots defined for this upstream logical channel.  This includes all minislots for IUC3 assigned to a broadcast or  multicast SID on the logical channel.  This is the 32 bit version of docsIfCmtsUpChnlCtrExtTotalCntnInitMaintMslots, and is included for back compatibility with SNMPv1 managers. Support for this object is optional. If the object is not supported, A value of zero is returned
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmtsupchnlctrusedcntninitmaintmslots
            
            	Current count, from CMTS initialization, of contention initial maintenance minislots utilized on this upstream logical channel.    This includes all contention minislots for IUC3 applicable to bursts that the CMTS correctly received.              This is the 32 bit version of  docsIfCmtsUpChnlCtrExtUsedCntnInitMaintMslots, and is included for back compatibility with SNMPv1 managers. Support for this object is optional. If the object is not supported, A value of zero is returned
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmtsupchnlctrcollcntninitmaintmslots
            
            	Current count, from CMTS initialization, of contention initial maintenance minislots subjected to collisions on this upstream  logical channel. This includes all contention minislots for IUC3 applicable to bursts that the CMTS detected, but could not correctly receive.              This is the 32 bit version of  docsIfCmtsUpChnlCtrExtCollCntnInitMaintMslots, and is included for back compatibility with SNMPv1 managers. Support for this object is optional. If the object is not supported, A value of zero is returned
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsifcmtsupchnlctrextcollcntnmslots
            
            	Current count, from CMTS initialization, of collision contention  minislots on the upstream logical channel. For contention regions, these are the minislots applicable to bursts that the CMTS detected,   but could not correctly receive. This is the 64 bit version of docsIfCmtsUpChnlCtrCollCntnMslots, and will not be accessible to SNMPv1 managers. Support for this object is optional. If the object is not supported, a value of zero is returned
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: docsifcmtsupchnlctrexttotalcntnreqmslots
            
            	Current count, from CMTS initialization, of contention request minislots defined for this upstream logical channel. This count  includes all minislots for IUC1 assigned to a broadcast or multicast  SID on the logical channel.  This is the 64 bit version of docsIfCmtsUpChnlCtrTotalCntnReqMslots, and will not be accessible to SNMPv1 managers. Support for this object is optional. If the object is not supported, A value of zero is returned
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: docsifcmtsupchnlctrextusedcntnreqmslots
            
            	Current count, from CMTS initialization, of contention request minislots utilized on this upstream logical channel. This count  includes all contention minislots for IUC1 applicable to bursts that the CMTS correctly received.              This is the 64 bit version of docsIfCmtsUpChnlCtrUsedCntnReqMslots, and will not be accessible to SNMPv1 managers. Support for this object is optional. If the object is not supported, A value of zero is returned
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: docsifcmtsupchnlctrextcollcntnreqmslots
            
            	Current count, from CMTS initialization, of contention request minislots subjected to collisions on this upstream logical channel. This includes all contention minislots for IUC1 applicable to bursts that the CMTS detected, but could not correctly receive.              This is the 64 bit version of docsIfCmtsUpChnlCtrCollCntnReqMslots, and will not be accessible to SNMPv1 managers. Support for this object is optional. If the object is not supported, A value of zero is returned
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: docsifcmtsupchnlctrexttotalcntnreqdatamslots
            
            	Current count, from CMTS initialization, of contention request data minislots defined for this upstream logical channel. This count  includes all minislots for IUC2 assigned to a broadcast or multicast  SID on the logical channel.  This is the 64 bit version of docsIfCmtsUpChnlCtrTotalCntnReqDataMslots, and will not be accessible to SNMPv1 managers. Support for this object is optional. If the object is not supported, A value of zero is returned
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: docsifcmtsupchnlctrextusedcntnreqdatamslots
            
            	Current count, from CMTS initialization, of contention request data minislots utilized on this upstream logical channel. This   includes all contention minislots for IUC2 applicable to bursts that the CMTS correctly received.              This is the 64 bit version of docsIfCmtsUpChnlCtrUsedCntnReqDataMslots, and will not be accessible to SNMPv1 managers. Support for this object is optional. If the object is not supported, A value of zero is returned
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: docsifcmtsupchnlctrextcollcntnreqdatamslots
            
            	Current count, from CMTS initialization, of contention request data minislots subjected to collisions on this upstream logical  channel. This includes all contention minislots for IUC2 applicable  to bursts that the CMTS detected, but could not correctly receive.              This is the 64 bit version of docsIfCmtsUpChnlCtrCollCntnReqDataMslots, and will not be accessible to SNMPv1 managers. Support for this object is optional. If the object is not supported, A value of zero is returned
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: docsifcmtsupchnlctrexttotalcntninitmaintmslots
            
            	Current count, from CMTS initialization, of initial maintenance minislots defined for this upstream logical channel. This count  includes all minislots for IUC3 assigned to a broadcast or multicast  SID on the logical channel.  This is the 64 bit version of  docsIfCmtsUpChnlCtrTotalCntnInitMaintMslots, and will not be accessible to SNMPv1 managers. Support for this object is optional. If the object is not supported, A value of zero is returned
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: docsifcmtsupchnlctrextusedcntninitmaintmslots
            
            	Current count, from CMTS initialization, of initial maintenance minislots utilized on this upstream logical channel. This   includes all contention minislots for IUC3 applicable to bursts that the CMTS correctly received.              This is the 64 bit version of docsIfCmtsUpChnlCtrUsedCntnInitMaintMslots, and will not be accessible to SNMPv1 managers. Support for this object is optional. If the object is not supported, A value of zero is returned
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: docsifcmtsupchnlctrextcollcntninitmaintmslots
            
            	Current count, from CMTS initialization, of contention initial maintenance minislots subjected to collisions on this upstream  logical channel. This includes all contention minislots for IUC3 applicable to bursts that the CMTS detected, but could not correctly receive.              This is the 64 bit version of docsIfCmtsUpChnlCtrCollCntnInitMaintMslots, and will not be accessible to SNMPv1 managers. Support for this object is optional. If the object is not supported, A value of zero is returned
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'DOCS-IF-MIB'
            _revision = '2007-09-12'

            def __init__(self):
                super(DOCSIFMIB.DocsIfCmtsUpChannelCounterTable.DocsIfCmtsUpChannelCounterEntry, self).__init__()

                self.yang_name = "docsIfCmtsUpChannelCounterEntry"
                self.yang_parent_name = "docsIfCmtsUpChannelCounterTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsifcmtsupchnlctrid', (YLeaf(YType.int32, 'docsIfCmtsUpChnlCtrId'), ['int'])),
                    ('docsifcmtsupchnlctrtotalmslots', (YLeaf(YType.uint32, 'docsIfCmtsUpChnlCtrTotalMslots'), ['int'])),
                    ('docsifcmtsupchnlctrucastgrantedmslots', (YLeaf(YType.uint32, 'docsIfCmtsUpChnlCtrUcastGrantedMslots'), ['int'])),
                    ('docsifcmtsupchnlctrtotalcntnmslots', (YLeaf(YType.uint32, 'docsIfCmtsUpChnlCtrTotalCntnMslots'), ['int'])),
                    ('docsifcmtsupchnlctrusedcntnmslots', (YLeaf(YType.uint32, 'docsIfCmtsUpChnlCtrUsedCntnMslots'), ['int'])),
                    ('docsifcmtsupchnlctrexttotalmslots', (YLeaf(YType.uint64, 'docsIfCmtsUpChnlCtrExtTotalMslots'), ['int'])),
                    ('docsifcmtsupchnlctrextucastgrantedmslots', (YLeaf(YType.uint64, 'docsIfCmtsUpChnlCtrExtUcastGrantedMslots'), ['int'])),
                    ('docsifcmtsupchnlctrexttotalcntnmslots', (YLeaf(YType.uint64, 'docsIfCmtsUpChnlCtrExtTotalCntnMslots'), ['int'])),
                    ('docsifcmtsupchnlctrextusedcntnmslots', (YLeaf(YType.uint64, 'docsIfCmtsUpChnlCtrExtUsedCntnMslots'), ['int'])),
                    ('docsifcmtsupchnlctrcollcntnmslots', (YLeaf(YType.uint32, 'docsIfCmtsUpChnlCtrCollCntnMslots'), ['int'])),
                    ('docsifcmtsupchnlctrtotalcntnreqmslots', (YLeaf(YType.uint32, 'docsIfCmtsUpChnlCtrTotalCntnReqMslots'), ['int'])),
                    ('docsifcmtsupchnlctrusedcntnreqmslots', (YLeaf(YType.uint32, 'docsIfCmtsUpChnlCtrUsedCntnReqMslots'), ['int'])),
                    ('docsifcmtsupchnlctrcollcntnreqmslots', (YLeaf(YType.uint32, 'docsIfCmtsUpChnlCtrCollCntnReqMslots'), ['int'])),
                    ('docsifcmtsupchnlctrtotalcntnreqdatamslots', (YLeaf(YType.uint32, 'docsIfCmtsUpChnlCtrTotalCntnReqDataMslots'), ['int'])),
                    ('docsifcmtsupchnlctrusedcntnreqdatamslots', (YLeaf(YType.uint32, 'docsIfCmtsUpChnlCtrUsedCntnReqDataMslots'), ['int'])),
                    ('docsifcmtsupchnlctrcollcntnreqdatamslots', (YLeaf(YType.uint32, 'docsIfCmtsUpChnlCtrCollCntnReqDataMslots'), ['int'])),
                    ('docsifcmtsupchnlctrtotalcntninitmaintmslots', (YLeaf(YType.uint32, 'docsIfCmtsUpChnlCtrTotalCntnInitMaintMslots'), ['int'])),
                    ('docsifcmtsupchnlctrusedcntninitmaintmslots', (YLeaf(YType.uint32, 'docsIfCmtsUpChnlCtrUsedCntnInitMaintMslots'), ['int'])),
                    ('docsifcmtsupchnlctrcollcntninitmaintmslots', (YLeaf(YType.uint32, 'docsIfCmtsUpChnlCtrCollCntnInitMaintMslots'), ['int'])),
                    ('docsifcmtsupchnlctrextcollcntnmslots', (YLeaf(YType.uint64, 'docsIfCmtsUpChnlCtrExtCollCntnMslots'), ['int'])),
                    ('docsifcmtsupchnlctrexttotalcntnreqmslots', (YLeaf(YType.uint64, 'docsIfCmtsUpChnlCtrExtTotalCntnReqMslots'), ['int'])),
                    ('docsifcmtsupchnlctrextusedcntnreqmslots', (YLeaf(YType.uint64, 'docsIfCmtsUpChnlCtrExtUsedCntnReqMslots'), ['int'])),
                    ('docsifcmtsupchnlctrextcollcntnreqmslots', (YLeaf(YType.uint64, 'docsIfCmtsUpChnlCtrExtCollCntnReqMslots'), ['int'])),
                    ('docsifcmtsupchnlctrexttotalcntnreqdatamslots', (YLeaf(YType.uint64, 'docsIfCmtsUpChnlCtrExtTotalCntnReqDataMslots'), ['int'])),
                    ('docsifcmtsupchnlctrextusedcntnreqdatamslots', (YLeaf(YType.uint64, 'docsIfCmtsUpChnlCtrExtUsedCntnReqDataMslots'), ['int'])),
                    ('docsifcmtsupchnlctrextcollcntnreqdatamslots', (YLeaf(YType.uint64, 'docsIfCmtsUpChnlCtrExtCollCntnReqDataMslots'), ['int'])),
                    ('docsifcmtsupchnlctrexttotalcntninitmaintmslots', (YLeaf(YType.uint64, 'docsIfCmtsUpChnlCtrExtTotalCntnInitMaintMslots'), ['int'])),
                    ('docsifcmtsupchnlctrextusedcntninitmaintmslots', (YLeaf(YType.uint64, 'docsIfCmtsUpChnlCtrExtUsedCntnInitMaintMslots'), ['int'])),
                    ('docsifcmtsupchnlctrextcollcntninitmaintmslots', (YLeaf(YType.uint64, 'docsIfCmtsUpChnlCtrExtCollCntnInitMaintMslots'), ['int'])),
                ])
                self.ifindex = None
                self.docsifcmtsupchnlctrid = None
                self.docsifcmtsupchnlctrtotalmslots = None
                self.docsifcmtsupchnlctrucastgrantedmslots = None
                self.docsifcmtsupchnlctrtotalcntnmslots = None
                self.docsifcmtsupchnlctrusedcntnmslots = None
                self.docsifcmtsupchnlctrexttotalmslots = None
                self.docsifcmtsupchnlctrextucastgrantedmslots = None
                self.docsifcmtsupchnlctrexttotalcntnmslots = None
                self.docsifcmtsupchnlctrextusedcntnmslots = None
                self.docsifcmtsupchnlctrcollcntnmslots = None
                self.docsifcmtsupchnlctrtotalcntnreqmslots = None
                self.docsifcmtsupchnlctrusedcntnreqmslots = None
                self.docsifcmtsupchnlctrcollcntnreqmslots = None
                self.docsifcmtsupchnlctrtotalcntnreqdatamslots = None
                self.docsifcmtsupchnlctrusedcntnreqdatamslots = None
                self.docsifcmtsupchnlctrcollcntnreqdatamslots = None
                self.docsifcmtsupchnlctrtotalcntninitmaintmslots = None
                self.docsifcmtsupchnlctrusedcntninitmaintmslots = None
                self.docsifcmtsupchnlctrcollcntninitmaintmslots = None
                self.docsifcmtsupchnlctrextcollcntnmslots = None
                self.docsifcmtsupchnlctrexttotalcntnreqmslots = None
                self.docsifcmtsupchnlctrextusedcntnreqmslots = None
                self.docsifcmtsupchnlctrextcollcntnreqmslots = None
                self.docsifcmtsupchnlctrexttotalcntnreqdatamslots = None
                self.docsifcmtsupchnlctrextusedcntnreqdatamslots = None
                self.docsifcmtsupchnlctrextcollcntnreqdatamslots = None
                self.docsifcmtsupchnlctrexttotalcntninitmaintmslots = None
                self.docsifcmtsupchnlctrextusedcntninitmaintmslots = None
                self.docsifcmtsupchnlctrextcollcntninitmaintmslots = None
                self._segment_path = lambda: "docsIfCmtsUpChannelCounterEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "DOCS-IF-MIB:DOCS-IF-MIB/docsIfCmtsUpChannelCounterTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIFMIB.DocsIfCmtsUpChannelCounterTable.DocsIfCmtsUpChannelCounterEntry, [u'ifindex', u'docsifcmtsupchnlctrid', u'docsifcmtsupchnlctrtotalmslots', u'docsifcmtsupchnlctrucastgrantedmslots', u'docsifcmtsupchnlctrtotalcntnmslots', u'docsifcmtsupchnlctrusedcntnmslots', u'docsifcmtsupchnlctrexttotalmslots', u'docsifcmtsupchnlctrextucastgrantedmslots', u'docsifcmtsupchnlctrexttotalcntnmslots', u'docsifcmtsupchnlctrextusedcntnmslots', u'docsifcmtsupchnlctrcollcntnmslots', u'docsifcmtsupchnlctrtotalcntnreqmslots', u'docsifcmtsupchnlctrusedcntnreqmslots', u'docsifcmtsupchnlctrcollcntnreqmslots', u'docsifcmtsupchnlctrtotalcntnreqdatamslots', u'docsifcmtsupchnlctrusedcntnreqdatamslots', u'docsifcmtsupchnlctrcollcntnreqdatamslots', u'docsifcmtsupchnlctrtotalcntninitmaintmslots', u'docsifcmtsupchnlctrusedcntninitmaintmslots', u'docsifcmtsupchnlctrcollcntninitmaintmslots', u'docsifcmtsupchnlctrextcollcntnmslots', u'docsifcmtsupchnlctrexttotalcntnreqmslots', u'docsifcmtsupchnlctrextusedcntnreqmslots', u'docsifcmtsupchnlctrextcollcntnreqmslots', u'docsifcmtsupchnlctrexttotalcntnreqdatamslots', u'docsifcmtsupchnlctrextusedcntnreqdatamslots', u'docsifcmtsupchnlctrextcollcntnreqdatamslots', u'docsifcmtsupchnlctrexttotalcntninitmaintmslots', u'docsifcmtsupchnlctrextusedcntninitmaintmslots', u'docsifcmtsupchnlctrextcollcntninitmaintmslots'], name, value)

    def clone_ptr(self):
        self._top_entity = DOCSIFMIB()
        return self._top_entity


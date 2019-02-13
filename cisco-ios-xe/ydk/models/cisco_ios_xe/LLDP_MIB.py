""" LLDP_MIB 

Management Information Base module for LLDP configuration,
statistics, local system data and remote systems data
components.

Copyright (C) IEEE (2005).  This version of this MIB module
is published as subclause 12.1 of IEEE Std 802.1AB\-2005;
see the standard itself for full legal notices.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class LldpChassisIdSubtype(Enum):
    """
    LldpChassisIdSubtype (Enum Class)

    This TC describes the source of a chassis identifier.

    The enumeration 'chassisComponent(1)' represents a chassis

    identifier based on the value of entPhysicalAlias object

    (defined in IETF RFC 2737) for a chassis component (i.e.,

    an entPhysicalClass value of 'chassis(3)').

    The enumeration 'interfaceAlias(2)' represents a chassis

    identifier based on the value of ifAlias object (defined in

    IETF RFC 2863) for an interface on the containing chassis.

    The enumeration 'portComponent(3)' represents a chassis

    identifier based on the value of entPhysicalAlias object

    (defined in IETF RFC 2737) for a port or backplane

    component (i.e., entPhysicalClass value of 'port(10)' or

    'backplane(4)'), within the containing chassis.

    The enumeration 'macAddress(4)' represents a chassis

    identifier based on the value of a unicast source address

    (encoded in network byte order and IEEE 802.3 canonical bit

    order), of a port on the containing chassis as defined in

    IEEE Std 802\-2001.

    The enumeration 'networkAddress(5)' represents a chassis

    identifier based on a network address, associated with

    a particular chassis.  The encoded address is actually

    composed of two fields.  The first field is a single octet,

    representing the IANA AddressFamilyNumbers value for the

    specific address type, and the second field is the network

    address value.

    The enumeration 'interfaceName(6)' represents a chassis

    identifier based on the value of ifName object (defined in

    IETF RFC 2863) for an interface on the containing chassis.

    The enumeration 'local(7)' represents a chassis identifier

    based on a locally defined value.

    .. data:: chassisComponent = 1

    .. data:: interfaceAlias = 2

    .. data:: portComponent = 3

    .. data:: macAddress = 4

    .. data:: networkAddress = 5

    .. data:: interfaceName = 6

    .. data:: local = 7

    """

    chassisComponent = Enum.YLeaf(1, "chassisComponent")

    interfaceAlias = Enum.YLeaf(2, "interfaceAlias")

    portComponent = Enum.YLeaf(3, "portComponent")

    macAddress = Enum.YLeaf(4, "macAddress")

    networkAddress = Enum.YLeaf(5, "networkAddress")

    interfaceName = Enum.YLeaf(6, "interfaceName")

    local = Enum.YLeaf(7, "local")


class LldpManAddrIfSubtype(Enum):
    """
    LldpManAddrIfSubtype (Enum Class)

    This TC describes the basis of a particular type of

    interface associated with the management address.

    The enumeration 'unknown(1)' represents the case where the

    interface is not known.

    The enumeration 'ifIndex(2)' represents interface identifier

    based on the ifIndex MIB object.

    The enumeration 'systemPortNumber(3)' represents interface

    identifier based on the system port numbering convention.

    .. data:: unknown = 1

    .. data:: ifIndex = 2

    .. data:: systemPortNumber = 3

    """

    unknown = Enum.YLeaf(1, "unknown")

    ifIndex = Enum.YLeaf(2, "ifIndex")

    systemPortNumber = Enum.YLeaf(3, "systemPortNumber")


class LldpPortIdSubtype(Enum):
    """
    LldpPortIdSubtype (Enum Class)

    This TC describes the source of a particular type of port

    identifier used in the LLDP MIB.

    The enumeration 'interfaceAlias(1)' represents a port

    identifier based on the ifAlias MIB object, defined in IETF

    RFC 2863.

    The enumeration 'portComponent(2)' represents a port

    identifier based on the value of entPhysicalAlias (defined in

    IETF RFC 2737) for a port component (i.e., entPhysicalClass

    value of 'port(10)'), within the containing chassis.

    The enumeration 'macAddress(3)' represents a port identifier

    based on a unicast source address (encoded in network

    byte order and IEEE 802.3 canonical bit order), which has

    been detected by the agent and associated with a particular

    port (IEEE Std 802\-2001).

    The enumeration 'networkAddress(4)' represents a port

    identifier based on a network address, detected by the agent

    and associated with a particular port.

    The enumeration 'interfaceName(5)' represents a port

    identifier based on the ifName MIB object, defined in IETF

    RFC 2863.

    The enumeration 'agentCircuitId(6)' represents a port

    identifier based on the agent\-local identifier of the circuit

    (defined in RFC 3046), detected by the agent and associated

    with a particular port.

    The enumeration 'local(7)' represents a port identifier

    based on a value locally assigned.

    .. data:: interfaceAlias = 1

    .. data:: portComponent = 2

    .. data:: macAddress = 3

    .. data:: networkAddress = 4

    .. data:: interfaceName = 5

    .. data:: agentCircuitId = 6

    .. data:: local = 7

    """

    interfaceAlias = Enum.YLeaf(1, "interfaceAlias")

    portComponent = Enum.YLeaf(2, "portComponent")

    macAddress = Enum.YLeaf(3, "macAddress")

    networkAddress = Enum.YLeaf(4, "networkAddress")

    interfaceName = Enum.YLeaf(5, "interfaceName")

    agentCircuitId = Enum.YLeaf(6, "agentCircuitId")

    local = Enum.YLeaf(7, "local")



class LLDPMIB(Entity):
    """
    
    
    .. attribute:: lldpconfiguration
    
    	
    	**type**\:  :py:class:`LldpConfiguration <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.LldpConfiguration>`
    
    	**config**\: False
    
    .. attribute:: lldpstatistics
    
    	
    	**type**\:  :py:class:`LldpStatistics <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.LldpStatistics>`
    
    	**config**\: False
    
    .. attribute:: lldplocalsystemdata
    
    	
    	**type**\:  :py:class:`LldpLocalSystemData <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.LldpLocalSystemData>`
    
    	**config**\: False
    
    .. attribute:: lldpportconfigtable
    
    	The table that controls LLDP frame transmission on individual ports
    	**type**\:  :py:class:`LldpPortConfigTable <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.LldpPortConfigTable>`
    
    	**config**\: False
    
    .. attribute:: lldpstatstxporttable
    
    	A table containing LLDP transmission statistics for individual ports.  Entries are not required to exist in this table while the lldpPortConfigEntry object is equal to 'disabled(4)'
    	**type**\:  :py:class:`LldpStatsTxPortTable <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.LldpStatsTxPortTable>`
    
    	**config**\: False
    
    .. attribute:: lldpstatsrxporttable
    
    	A table containing LLDP reception statistics for individual ports.  Entries are not required to exist in this table while the lldpPortConfigEntry object is equal to 'disabled(4)'
    	**type**\:  :py:class:`LldpStatsRxPortTable <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.LldpStatsRxPortTable>`
    
    	**config**\: False
    
    .. attribute:: lldplocporttable
    
    	This table contains one or more rows per port information associated with the local system known to this agent
    	**type**\:  :py:class:`LldpLocPortTable <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.LldpLocPortTable>`
    
    	**config**\: False
    
    .. attribute:: lldplocmanaddrtable
    
    	This table contains management address information on the local system known to this agent
    	**type**\:  :py:class:`LldpLocManAddrTable <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.LldpLocManAddrTable>`
    
    	**config**\: False
    
    .. attribute:: lldpremtable
    
    	This table contains one or more rows per physical network connection known to this agent.  The agent may wish to ensure that only one lldpRemEntry is present for each local port, or it may choose to maintain multiple lldpRemEntries for the same local port.  The following procedure may be used to retrieve remote systems information updates from an LLDP agent\:     1. NMS polls all tables associated with remote systems       and keeps a local copy of the information retrieved.       NMS polls periodically the values of the following       objects\:          a. lldpStatsRemTablesInserts          b. lldpStatsRemTablesDeletes          c. lldpStatsRemTablesDrops          d. lldpStatsRemTablesAgeouts          e. lldpStatsRxPortAgeoutsTotal for all ports.     2. LLDP agent updates remote systems MIB objects, and       sends out notifications to a list of notification       destinations.     3. NMS receives the notifications and compares the new       values of objects listed in step 1.          Periodically, NMS should poll the object       lldpStatsRemTablesLastChangeTime to find out if anything       has changed since the last poll.  if something has       changed, NMS will poll the objects listed in step 1 to       figure out what kind of changes occurred in the tables.        if value of lldpStatsRemTablesInserts has changed,       then NMS will walk all tables by employing TimeFilter       with the last\-polled time value.  This request will       return new objects or objects whose values are updated       since the last poll.        if value of lldpStatsRemTablesAgeouts has changed,       then NMS will walk the lldpStatsRxPortAgeoutsTotal and       compare the new values with previously recorded ones.       For ports whose lldpStatsRxPortAgeoutsTotal value is       greater than the recorded value, NMS will have to       retrieve objects associated with those ports from       table(s) without employing a TimeFilter (which is       performed by specifying 0 for the TimeFilter.)        lldpStatsRemTablesDeletes and lldpStatsRemTablesDrops       objects are provided for informational purposes
    	**type**\:  :py:class:`LldpRemTable <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.LldpRemTable>`
    
    	**config**\: False
    
    .. attribute:: lldpremmanaddrtable
    
    	This table contains one or more rows per management address information on the remote system learned on a particular port contained in the local chassis known to this agent
    	**type**\:  :py:class:`LldpRemManAddrTable <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.LldpRemManAddrTable>`
    
    	**config**\: False
    
    .. attribute:: lldpremunknowntlvtable
    
    	This table contains information about an incoming TLV which is not recognized by the receiving LLDP agent.  The TLV may be from a later version of the basic management set.  This table should only contain TLVs that are found in a single LLDP frame.  Entries in this table, associated with an MAC service access point (MSAP, the access point for MAC services provided to the LCC sublayer, defined in IEEE 100, which is also identified with a particular lldpRemLocalPortNum, lldpRemIndex pair) are overwritten with most recently received unrecognized TLV from the same MSAP, or they will naturally age out when the rxInfoTTL timer (associated with the MSAP) expires
    	**type**\:  :py:class:`LldpRemUnknownTLVTable <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.LldpRemUnknownTLVTable>`
    
    	**config**\: False
    
    .. attribute:: lldpremorgdefinfotable
    
    	This table contains one or more rows per physical network connection which advertises the organizationally defined information.  Note that this table contains one or more rows of organizationally defined information that is not recognized by the local agent.  If the local system is capable of recognizing any organizationally defined information, appropriate extension MIBs from the organization should be used for information retrieval
    	**type**\:  :py:class:`LldpRemOrgDefInfoTable <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.LldpRemOrgDefInfoTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'LLDP-MIB'
    _revision = '2005-05-06'

    def __init__(self):
        super(LLDPMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "LLDP-MIB"
        self.yang_parent_name = "LLDP-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("lldpConfiguration", ("lldpconfiguration", LLDPMIB.LldpConfiguration)), ("lldpStatistics", ("lldpstatistics", LLDPMIB.LldpStatistics)), ("lldpLocalSystemData", ("lldplocalsystemdata", LLDPMIB.LldpLocalSystemData)), ("lldpPortConfigTable", ("lldpportconfigtable", LLDPMIB.LldpPortConfigTable)), ("lldpStatsTxPortTable", ("lldpstatstxporttable", LLDPMIB.LldpStatsTxPortTable)), ("lldpStatsRxPortTable", ("lldpstatsrxporttable", LLDPMIB.LldpStatsRxPortTable)), ("lldpLocPortTable", ("lldplocporttable", LLDPMIB.LldpLocPortTable)), ("lldpLocManAddrTable", ("lldplocmanaddrtable", LLDPMIB.LldpLocManAddrTable)), ("lldpRemTable", ("lldpremtable", LLDPMIB.LldpRemTable)), ("lldpRemManAddrTable", ("lldpremmanaddrtable", LLDPMIB.LldpRemManAddrTable)), ("lldpRemUnknownTLVTable", ("lldpremunknowntlvtable", LLDPMIB.LldpRemUnknownTLVTable)), ("lldpRemOrgDefInfoTable", ("lldpremorgdefinfotable", LLDPMIB.LldpRemOrgDefInfoTable))])
        self._leafs = OrderedDict()

        self.lldpconfiguration = LLDPMIB.LldpConfiguration()
        self.lldpconfiguration.parent = self
        self._children_name_map["lldpconfiguration"] = "lldpConfiguration"

        self.lldpstatistics = LLDPMIB.LldpStatistics()
        self.lldpstatistics.parent = self
        self._children_name_map["lldpstatistics"] = "lldpStatistics"

        self.lldplocalsystemdata = LLDPMIB.LldpLocalSystemData()
        self.lldplocalsystemdata.parent = self
        self._children_name_map["lldplocalsystemdata"] = "lldpLocalSystemData"

        self.lldpportconfigtable = LLDPMIB.LldpPortConfigTable()
        self.lldpportconfigtable.parent = self
        self._children_name_map["lldpportconfigtable"] = "lldpPortConfigTable"

        self.lldpstatstxporttable = LLDPMIB.LldpStatsTxPortTable()
        self.lldpstatstxporttable.parent = self
        self._children_name_map["lldpstatstxporttable"] = "lldpStatsTxPortTable"

        self.lldpstatsrxporttable = LLDPMIB.LldpStatsRxPortTable()
        self.lldpstatsrxporttable.parent = self
        self._children_name_map["lldpstatsrxporttable"] = "lldpStatsRxPortTable"

        self.lldplocporttable = LLDPMIB.LldpLocPortTable()
        self.lldplocporttable.parent = self
        self._children_name_map["lldplocporttable"] = "lldpLocPortTable"

        self.lldplocmanaddrtable = LLDPMIB.LldpLocManAddrTable()
        self.lldplocmanaddrtable.parent = self
        self._children_name_map["lldplocmanaddrtable"] = "lldpLocManAddrTable"

        self.lldpremtable = LLDPMIB.LldpRemTable()
        self.lldpremtable.parent = self
        self._children_name_map["lldpremtable"] = "lldpRemTable"

        self.lldpremmanaddrtable = LLDPMIB.LldpRemManAddrTable()
        self.lldpremmanaddrtable.parent = self
        self._children_name_map["lldpremmanaddrtable"] = "lldpRemManAddrTable"

        self.lldpremunknowntlvtable = LLDPMIB.LldpRemUnknownTLVTable()
        self.lldpremunknowntlvtable.parent = self
        self._children_name_map["lldpremunknowntlvtable"] = "lldpRemUnknownTLVTable"

        self.lldpremorgdefinfotable = LLDPMIB.LldpRemOrgDefInfoTable()
        self.lldpremorgdefinfotable.parent = self
        self._children_name_map["lldpremorgdefinfotable"] = "lldpRemOrgDefInfoTable"
        self._segment_path = lambda: "LLDP-MIB:LLDP-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(LLDPMIB, [], name, value)


    class LldpConfiguration(Entity):
        """
        
        
        .. attribute:: lldpmessagetxinterval
        
        	The interval at which LLDP frames are transmitted on behalf of this LLDP agent.  The default value for lldpMessageTxInterval object is 30 seconds.  The value of this object must be restored from non\-volatile storage after a re\-initialization of the management system
        	**type**\: int
        
        	**range:** 5..32768
        
        	**config**\: False
        
        	**units**\: seconds
        
        .. attribute:: lldpmessagetxholdmultiplier
        
        	The time\-to\-live value expressed as a multiple of the lldpMessageTxInterval object.  The actual time\-to\-live value used in LLDP frames, transmitted on behalf of this LLDP agent, can be expressed by the following formula\: TTL = min(65535, (lldpMessageTxInterval \* lldpMessageTxHoldMultiplier)) For example, if the value of lldpMessageTxInterval is '30', and the value of lldpMessageTxHoldMultiplier is '4', then the value '120' is encoded in the TTL field in the LLDP header.  The default value for lldpMessageTxHoldMultiplier object is 4.  The value of this object must be restored from non\-volatile storage after a re\-initialization of the management system
        	**type**\: int
        
        	**range:** 2..10
        
        	**config**\: False
        
        .. attribute:: lldpreinitdelay
        
        	The lldpReinitDelay indicates the delay (in units of seconds) from when lldpPortConfigAdminStatus object of a particular port becomes 'disabled' until re\-initialization will be attempted.  The default value for lldpReintDelay object is two seconds.  The value of this object must be restored from non\-volatile storage after a re\-initialization of the management system
        	**type**\: int
        
        	**range:** 1..10
        
        	**config**\: False
        
        	**units**\: seconds
        
        .. attribute:: lldptxdelay
        
        	The lldpTxDelay indicates the delay (in units of seconds) between successive LLDP frame transmissions  initiated by value/status changes in the LLDP local systems MIB.  The recommended value for the lldpTxDelay is set by the following  formula\:     1 <= lldpTxDelay <= (0.25 \* lldpMessageTxInterval)  The default value for lldpTxDelay object is two seconds.  The value of this object must be restored from non\-volatile storage after a re\-initialization of the management system
        	**type**\: int
        
        	**range:** 1..8192
        
        	**config**\: False
        
        	**units**\: seconds
        
        .. attribute:: lldpnotificationinterval
        
        	This object controls the transmission of LLDP notifications.  the agent must not generate more than one lldpRemTablesChange notification\-event in the indicated period, where a 'notification\-event' is the transmission of a single notification PDU type to a list of notification destinations. If additional changes in lldpRemoteSystemsData object groups occur within the indicated throttling period, then these trap\- events must be suppressed by the agent. An NMS should periodically check the value of lldpStatsRemTableLastChangeTime to detect any missed lldpRemTablesChange notification\-events, e.g. due to throttling or transmission loss.  If notification transmission is enabled for particular ports, the suggested default throttling period is 5 seconds.  The value of this object must be restored from non\-volatile storage after a re\-initialization of the management system
        	**type**\: int
        
        	**range:** 5..3600
        
        	**config**\: False
        
        	**units**\: seconds
        
        

        """

        _prefix = 'LLDP-MIB'
        _revision = '2005-05-06'

        def __init__(self):
            super(LLDPMIB.LldpConfiguration, self).__init__()

            self.yang_name = "lldpConfiguration"
            self.yang_parent_name = "LLDP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('lldpmessagetxinterval', (YLeaf(YType.int32, 'lldpMessageTxInterval'), ['int'])),
                ('lldpmessagetxholdmultiplier', (YLeaf(YType.int32, 'lldpMessageTxHoldMultiplier'), ['int'])),
                ('lldpreinitdelay', (YLeaf(YType.int32, 'lldpReinitDelay'), ['int'])),
                ('lldptxdelay', (YLeaf(YType.int32, 'lldpTxDelay'), ['int'])),
                ('lldpnotificationinterval', (YLeaf(YType.int32, 'lldpNotificationInterval'), ['int'])),
            ])
            self.lldpmessagetxinterval = None
            self.lldpmessagetxholdmultiplier = None
            self.lldpreinitdelay = None
            self.lldptxdelay = None
            self.lldpnotificationinterval = None
            self._segment_path = lambda: "lldpConfiguration"
            self._absolute_path = lambda: "LLDP-MIB:LLDP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(LLDPMIB.LldpConfiguration, ['lldpmessagetxinterval', 'lldpmessagetxholdmultiplier', 'lldpreinitdelay', 'lldptxdelay', 'lldpnotificationinterval'], name, value)



    class LldpStatistics(Entity):
        """
        
        
        .. attribute:: lldpstatsremtableslastchangetime
        
        	The value of sysUpTime object (defined in IETF RFC 3418) at the time an entry is created, modified, or deleted in the in tables associated with the lldpRemoteSystemsData objects and all LLDP extension objects associated with remote systems.  An NMS can use this object to reduce polling of the lldpRemoteSystemsData objects
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: lldpstatsremtablesinserts
        
        	The number of times the complete set of information advertised by a particular MSAP has been inserted into tables contained in lldpRemoteSystemsData and lldpExtensions objects.  The complete set of information received from a particular MSAP should be inserted into related tables.  If partial information cannot be inserted for a reason such as lack of resources, all of the complete set of information should be removed.  This counter should be incremented only once after the complete set of information is successfully recorded in all related tables.  Any failures during inserting information set which result in deletion of previously inserted information should not trigger any changes in lldpStatsRemTablesInserts since the insert is not completed yet or or in lldpStatsRemTablesDeletes, since the deletion would only be a partial deletion. If the failure was the result of lack of resources, the lldpStatsRemTablesDrops counter should be incremented once
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: table entries
        
        .. attribute:: lldpstatsremtablesdeletes
        
        	The number of times the complete set of information advertised by a particular MSAP has been deleted from tables contained in lldpRemoteSystemsData and lldpExtensions objects.  This counter should be incremented only once when the complete set of information is completely deleted from all related tables.  Partial deletions, such as deletion of rows associated with a particular MSAP from some tables, but not from all tables are not allowed, thus should not change the value of this counter
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: table entries
        
        .. attribute:: lldpstatsremtablesdrops
        
        	The number of times the complete set of information advertised by a particular MSAP could not be entered into tables contained in lldpRemoteSystemsData and lldpExtensions objects because of insufficient resources
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: table entries
        
        .. attribute:: lldpstatsremtablesageouts
        
        	The number of times the complete set of information advertised by a particular MSAP has been deleted from tables contained in lldpRemoteSystemsData and lldpExtensions objects because the information timeliness interval has expired.  This counter should be incremented only once when the complete set of information is completely invalidated (aged out) from all related tables.  Partial aging, similar to deletion case, is not allowed, and thus, should not change the value of this counter
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        

        """

        _prefix = 'LLDP-MIB'
        _revision = '2005-05-06'

        def __init__(self):
            super(LLDPMIB.LldpStatistics, self).__init__()

            self.yang_name = "lldpStatistics"
            self.yang_parent_name = "LLDP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('lldpstatsremtableslastchangetime', (YLeaf(YType.uint32, 'lldpStatsRemTablesLastChangeTime'), ['int'])),
                ('lldpstatsremtablesinserts', (YLeaf(YType.uint32, 'lldpStatsRemTablesInserts'), ['int'])),
                ('lldpstatsremtablesdeletes', (YLeaf(YType.uint32, 'lldpStatsRemTablesDeletes'), ['int'])),
                ('lldpstatsremtablesdrops', (YLeaf(YType.uint32, 'lldpStatsRemTablesDrops'), ['int'])),
                ('lldpstatsremtablesageouts', (YLeaf(YType.uint32, 'lldpStatsRemTablesAgeouts'), ['int'])),
            ])
            self.lldpstatsremtableslastchangetime = None
            self.lldpstatsremtablesinserts = None
            self.lldpstatsremtablesdeletes = None
            self.lldpstatsremtablesdrops = None
            self.lldpstatsremtablesageouts = None
            self._segment_path = lambda: "lldpStatistics"
            self._absolute_path = lambda: "LLDP-MIB:LLDP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(LLDPMIB.LldpStatistics, ['lldpstatsremtableslastchangetime', 'lldpstatsremtablesinserts', 'lldpstatsremtablesdeletes', 'lldpstatsremtablesdrops', 'lldpstatsremtablesageouts'], name, value)



    class LldpLocalSystemData(Entity):
        """
        
        
        .. attribute:: lldplocchassisidsubtype
        
        	The type of encoding used to identify the chassis associated with the local system
        	**type**\:  :py:class:`LldpChassisIdSubtype <ydk.models.cisco_ios_xe.LLDP_MIB.LldpChassisIdSubtype>`
        
        	**config**\: False
        
        .. attribute:: lldplocchassisid
        
        	The string value used to identify the chassis component associated with the local system
        	**type**\: str
        
        	**length:** 1..255
        
        	**config**\: False
        
        .. attribute:: lldplocsysname
        
        	The string value used to identify the system name of the local system.  If the local agent supports IETF RFC 3418, lldpLocSysName object should have the same value of sysName object
        	**type**\: str
        
        	**length:** 0..255
        
        	**config**\: False
        
        .. attribute:: lldplocsysdesc
        
        	The string value used to identify the system description of the local system.  If the local agent supports IETF RFC 3418, lldpLocSysDesc object should have the same value of sysDesc object
        	**type**\: str
        
        	**length:** 0..255
        
        	**config**\: False
        
        .. attribute:: lldplocsyscapsupported
        
        	The bitmap value used to identify which system capabilities are supported on the local system
        	**type**\:  :py:class:`LldpSystemCapabilitiesMap <ydk.models.cisco_ios_xe.LLDP_MIB.LldpSystemCapabilitiesMap>`
        
        	**config**\: False
        
        .. attribute:: lldplocsyscapenabled
        
        	The bitmap value used to identify which system capabilities are enabled on the local system
        	**type**\:  :py:class:`LldpSystemCapabilitiesMap <ydk.models.cisco_ios_xe.LLDP_MIB.LldpSystemCapabilitiesMap>`
        
        	**config**\: False
        
        

        """

        _prefix = 'LLDP-MIB'
        _revision = '2005-05-06'

        def __init__(self):
            super(LLDPMIB.LldpLocalSystemData, self).__init__()

            self.yang_name = "lldpLocalSystemData"
            self.yang_parent_name = "LLDP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('lldplocchassisidsubtype', (YLeaf(YType.enumeration, 'lldpLocChassisIdSubtype'), [('ydk.models.cisco_ios_xe.LLDP_MIB', 'LldpChassisIdSubtype', '')])),
                ('lldplocchassisid', (YLeaf(YType.str, 'lldpLocChassisId'), ['str'])),
                ('lldplocsysname', (YLeaf(YType.str, 'lldpLocSysName'), ['str'])),
                ('lldplocsysdesc', (YLeaf(YType.str, 'lldpLocSysDesc'), ['str'])),
                ('lldplocsyscapsupported', (YLeaf(YType.bits, 'lldpLocSysCapSupported'), ['Bits'])),
                ('lldplocsyscapenabled', (YLeaf(YType.bits, 'lldpLocSysCapEnabled'), ['Bits'])),
            ])
            self.lldplocchassisidsubtype = None
            self.lldplocchassisid = None
            self.lldplocsysname = None
            self.lldplocsysdesc = None
            self.lldplocsyscapsupported = Bits()
            self.lldplocsyscapenabled = Bits()
            self._segment_path = lambda: "lldpLocalSystemData"
            self._absolute_path = lambda: "LLDP-MIB:LLDP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(LLDPMIB.LldpLocalSystemData, ['lldplocchassisidsubtype', 'lldplocchassisid', 'lldplocsysname', 'lldplocsysdesc', 'lldplocsyscapsupported', 'lldplocsyscapenabled'], name, value)



    class LldpPortConfigTable(Entity):
        """
        The table that controls LLDP frame transmission on individual
        ports.
        
        .. attribute:: lldpportconfigentry
        
        	LLDP configuration information for a particular port. This configuration parameter controls the transmission and the reception of LLDP frames on those ports whose rows are created in this table
        	**type**\: list of  		 :py:class:`LldpPortConfigEntry <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.LldpPortConfigTable.LldpPortConfigEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'LLDP-MIB'
        _revision = '2005-05-06'

        def __init__(self):
            super(LLDPMIB.LldpPortConfigTable, self).__init__()

            self.yang_name = "lldpPortConfigTable"
            self.yang_parent_name = "LLDP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("lldpPortConfigEntry", ("lldpportconfigentry", LLDPMIB.LldpPortConfigTable.LldpPortConfigEntry))])
            self._leafs = OrderedDict()

            self.lldpportconfigentry = YList(self)
            self._segment_path = lambda: "lldpPortConfigTable"
            self._absolute_path = lambda: "LLDP-MIB:LLDP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(LLDPMIB.LldpPortConfigTable, [], name, value)


        class LldpPortConfigEntry(Entity):
            """
            LLDP configuration information for a particular port.
            This configuration parameter controls the transmission and
            the reception of LLDP frames on those ports whose rows are
            created in this table.
            
            .. attribute:: lldpportconfigportnum  (key)
            
            	The index value used to identify the port component (contained in the local chassis with the LLDP agent) associated with this entry.  The value of this object is used as a port index to the lldpPortConfigTable
            	**type**\: int
            
            	**range:** 1..4096
            
            	**config**\: False
            
            .. attribute:: lldpportconfigadminstatus
            
            	The administratively desired status of the local LLDP agent.  If the associated lldpPortConfigAdminStatus object has a value of 'txOnly(1)', then LLDP agent will transmit LLDP frames on this port and it will not store any information about the remote systems connected.  If the associated lldpPortConfigAdminStatus object has a value of 'rxOnly(2)', then the LLDP agent will receive, but it will not transmit LLDP frames on this port.  If the associated lldpPortConfigAdminStatus object has a value of 'txAndRx(3)', then the LLDP agent will transmit and receive LLDP frames on this port.  If the associated lldpPortConfigAdminStatus object has a value of 'disabled(4)', then LLDP agent will not transmit or receive LLDP frames on this port.  If there is remote systems information which is received on this port and stored in other tables, before the port's lldpPortConfigAdminStatus becomes disabled, then the information will naturally age out
            	**type**\:  :py:class:`LldpPortConfigAdminStatus <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.LldpPortConfigTable.LldpPortConfigEntry.LldpPortConfigAdminStatus>`
            
            	**config**\: False
            
            .. attribute:: lldpportconfignotificationenable
            
            	The lldpPortConfigNotificationEnable controls, on a per port basis,  whether or not notifications from the agent are enabled. The value true(1) means that notifications are enabled; the value false(2) means that they are not
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: lldpportconfigtlvstxenable
            
            	The lldpPortConfigTLVsTxEnable, defined as a bitmap, includes the basic set of LLDP TLVs whose transmission is allowed on the local LLDP agent by the network management. Each bit in the bitmap corresponds to a TLV type associated with a specific optional TLV.  It should be noted that the organizationally\-specific TLVs are excluded from the lldpTLVsTxEnable bitmap.  LLDP Organization Specific Information Extension MIBs should have similar configuration object to control transmission of their organizationally defined TLVs.  The bit 'portDesc(0)' indicates that LLDP agent should transmit 'Port Description TLV'.  The bit 'sysName(1)' indicates that LLDP agent should transmit 'System Name TLV'.  The bit 'sysDesc(2)' indicates that LLDP agent should transmit 'System Description TLV'.  The bit 'sysCap(3)' indicates that LLDP agent should transmit 'System Capabilities TLV'.  There is no bit reserved for the management address TLV type since transmission of management address TLVs are controlled by another object, lldpConfigManAddrTable.  The default value for lldpPortConfigTLVsTxEnable object is empty set, which means no enumerated values are set.  The value of this object must be restored from non\-volatile storage after a re\-initialization of the management system
            	**type**\:  :py:class:`LldpPortConfigTLVsTxEnable <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.LldpPortConfigTable.LldpPortConfigEntry.LldpPortConfigTLVsTxEnable>`
            
            	**config**\: False
            
            

            """

            _prefix = 'LLDP-MIB'
            _revision = '2005-05-06'

            def __init__(self):
                super(LLDPMIB.LldpPortConfigTable.LldpPortConfigEntry, self).__init__()

                self.yang_name = "lldpPortConfigEntry"
                self.yang_parent_name = "lldpPortConfigTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['lldpportconfigportnum']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('lldpportconfigportnum', (YLeaf(YType.int32, 'lldpPortConfigPortNum'), ['int'])),
                    ('lldpportconfigadminstatus', (YLeaf(YType.enumeration, 'lldpPortConfigAdminStatus'), [('ydk.models.cisco_ios_xe.LLDP_MIB', 'LLDPMIB', 'LldpPortConfigTable.LldpPortConfigEntry.LldpPortConfigAdminStatus')])),
                    ('lldpportconfignotificationenable', (YLeaf(YType.boolean, 'lldpPortConfigNotificationEnable'), ['bool'])),
                    ('lldpportconfigtlvstxenable', (YLeaf(YType.bits, 'lldpPortConfigTLVsTxEnable'), ['Bits'])),
                ])
                self.lldpportconfigportnum = None
                self.lldpportconfigadminstatus = None
                self.lldpportconfignotificationenable = None
                self.lldpportconfigtlvstxenable = Bits()
                self._segment_path = lambda: "lldpPortConfigEntry" + "[lldpPortConfigPortNum='" + str(self.lldpportconfigportnum) + "']"
                self._absolute_path = lambda: "LLDP-MIB:LLDP-MIB/lldpPortConfigTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(LLDPMIB.LldpPortConfigTable.LldpPortConfigEntry, ['lldpportconfigportnum', 'lldpportconfigadminstatus', 'lldpportconfignotificationenable', 'lldpportconfigtlvstxenable'], name, value)

            class LldpPortConfigAdminStatus(Enum):
                """
                LldpPortConfigAdminStatus (Enum Class)

                The administratively desired status of the local LLDP agent.

                If the associated lldpPortConfigAdminStatus object has a

                value of 'txOnly(1)', then LLDP agent will transmit LLDP

                frames on this port and it will not store any information

                about the remote systems connected.

                If the associated lldpPortConfigAdminStatus object has a

                value of 'rxOnly(2)', then the LLDP agent will receive,

                but it will not transmit LLDP frames on this port.

                If the associated lldpPortConfigAdminStatus object has a

                value of 'txAndRx(3)', then the LLDP agent will transmit

                and receive LLDP frames on this port.

                If the associated lldpPortConfigAdminStatus object has a

                value of 'disabled(4)', then LLDP agent will not transmit or

                receive LLDP frames on this port.  If there is remote systems

                information which is received on this port and stored in

                other tables, before the port's lldpPortConfigAdminStatus

                becomes disabled, then the information will naturally age out.

                .. data:: txOnly = 1

                .. data:: rxOnly = 2

                .. data:: txAndRx = 3

                .. data:: disabled = 4

                """

                txOnly = Enum.YLeaf(1, "txOnly")

                rxOnly = Enum.YLeaf(2, "rxOnly")

                txAndRx = Enum.YLeaf(3, "txAndRx")

                disabled = Enum.YLeaf(4, "disabled")





    class LldpStatsTxPortTable(Entity):
        """
        A table containing LLDP transmission statistics for
        individual ports.  Entries are not required to exist in
        this table while the lldpPortConfigEntry object is equal to
        'disabled(4)'.
        
        .. attribute:: lldpstatstxportentry
        
        	LLDP frame transmission statistics for a particular port. The port must be contained in the same chassis as the LLDP agent.  All counter values in a particular entry shall be maintained on a continuing basis and shall not be deleted upon expiration of rxInfoTTL timing counters in the LLDP remote systems MIB of the receipt of a shutdown frame from a remote LLDP agent.  All statistical counters associated with a particular port on the local LLDP agent become frozen whenever the adminStatus is disabled for the same port
        	**type**\: list of  		 :py:class:`LldpStatsTxPortEntry <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.LldpStatsTxPortTable.LldpStatsTxPortEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'LLDP-MIB'
        _revision = '2005-05-06'

        def __init__(self):
            super(LLDPMIB.LldpStatsTxPortTable, self).__init__()

            self.yang_name = "lldpStatsTxPortTable"
            self.yang_parent_name = "LLDP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("lldpStatsTxPortEntry", ("lldpstatstxportentry", LLDPMIB.LldpStatsTxPortTable.LldpStatsTxPortEntry))])
            self._leafs = OrderedDict()

            self.lldpstatstxportentry = YList(self)
            self._segment_path = lambda: "lldpStatsTxPortTable"
            self._absolute_path = lambda: "LLDP-MIB:LLDP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(LLDPMIB.LldpStatsTxPortTable, [], name, value)


        class LldpStatsTxPortEntry(Entity):
            """
            LLDP frame transmission statistics for a particular port.
            The port must be contained in the same chassis as the
            LLDP agent.
            
            All counter values in a particular entry shall be
            maintained on a continuing basis and shall not be deleted
            upon expiration of rxInfoTTL timing counters in the LLDP
            remote systems MIB of the receipt of a shutdown frame from
            a remote LLDP agent.
            
            All statistical counters associated with a particular
            port on the local LLDP agent become frozen whenever the
            adminStatus is disabled for the same port.
            
            .. attribute:: lldpstatstxportnum  (key)
            
            	The index value used to identify the port component (contained in the local chassis with the LLDP agent) associated with this entry.  The value of this object is used as a port index to the lldpStatsTable
            	**type**\: int
            
            	**range:** 1..4096
            
            	**config**\: False
            
            .. attribute:: lldpstatstxportframestotal
            
            	The number of LLDP frames transmitted by this LLDP agent on the indicated port
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'LLDP-MIB'
            _revision = '2005-05-06'

            def __init__(self):
                super(LLDPMIB.LldpStatsTxPortTable.LldpStatsTxPortEntry, self).__init__()

                self.yang_name = "lldpStatsTxPortEntry"
                self.yang_parent_name = "lldpStatsTxPortTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['lldpstatstxportnum']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('lldpstatstxportnum', (YLeaf(YType.int32, 'lldpStatsTxPortNum'), ['int'])),
                    ('lldpstatstxportframestotal', (YLeaf(YType.uint32, 'lldpStatsTxPortFramesTotal'), ['int'])),
                ])
                self.lldpstatstxportnum = None
                self.lldpstatstxportframestotal = None
                self._segment_path = lambda: "lldpStatsTxPortEntry" + "[lldpStatsTxPortNum='" + str(self.lldpstatstxportnum) + "']"
                self._absolute_path = lambda: "LLDP-MIB:LLDP-MIB/lldpStatsTxPortTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(LLDPMIB.LldpStatsTxPortTable.LldpStatsTxPortEntry, ['lldpstatstxportnum', 'lldpstatstxportframestotal'], name, value)




    class LldpStatsRxPortTable(Entity):
        """
        A table containing LLDP reception statistics for individual
        ports.  Entries are not required to exist in this table while
        the lldpPortConfigEntry object is equal to 'disabled(4)'.
        
        .. attribute:: lldpstatsrxportentry
        
        	LLDP frame reception statistics for a particular port. The port must be contained in the same chassis as the LLDP agent.  All counter values in a particular entry shall be maintained on a continuing basis and shall not be deleted upon expiration of rxInfoTTL timing counters in the LLDP remote systems MIB of the receipt of a shutdown frame from a remote LLDP agent.  All statistical counters associated with a particular port on the local LLDP agent become frozen whenever the adminStatus is disabled for the same port
        	**type**\: list of  		 :py:class:`LldpStatsRxPortEntry <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.LldpStatsRxPortTable.LldpStatsRxPortEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'LLDP-MIB'
        _revision = '2005-05-06'

        def __init__(self):
            super(LLDPMIB.LldpStatsRxPortTable, self).__init__()

            self.yang_name = "lldpStatsRxPortTable"
            self.yang_parent_name = "LLDP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("lldpStatsRxPortEntry", ("lldpstatsrxportentry", LLDPMIB.LldpStatsRxPortTable.LldpStatsRxPortEntry))])
            self._leafs = OrderedDict()

            self.lldpstatsrxportentry = YList(self)
            self._segment_path = lambda: "lldpStatsRxPortTable"
            self._absolute_path = lambda: "LLDP-MIB:LLDP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(LLDPMIB.LldpStatsRxPortTable, [], name, value)


        class LldpStatsRxPortEntry(Entity):
            """
            LLDP frame reception statistics for a particular port.
            The port must be contained in the same chassis as the
            LLDP agent.
            
            All counter values in a particular entry shall be
            maintained on a continuing basis and shall not be deleted
            upon expiration of rxInfoTTL timing counters in the LLDP
            remote systems MIB of the receipt of a shutdown frame from
            a remote LLDP agent.
            
            All statistical counters associated with a particular
            port on the local LLDP agent become frozen whenever the
            adminStatus is disabled for the same port.
            
            .. attribute:: lldpstatsrxportnum  (key)
            
            	The index value used to identify the port component (contained in the local chassis with the LLDP agent) associated with this entry.  The value of this object is used as a port index to the lldpStatsTable
            	**type**\: int
            
            	**range:** 1..4096
            
            	**config**\: False
            
            .. attribute:: lldpstatsrxportframesdiscardedtotal
            
            	The number of LLDP frames received by this LLDP agent on the indicated port, and then discarded for any reason. This counter can provide an indication that LLDP header formating problems may exist with the local LLDP agent in the sending system or that LLDPDU validation problems may exist with the local LLDP agent in the receiving system
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: lldpstatsrxportframeserrors
            
            	The number of invalid LLDP frames received by this LLDP agent on the indicated port, while this LLDP agent is enabled
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: lldpstatsrxportframestotal
            
            	The number of valid LLDP frames received by this LLDP agent on the indicated port, while this LLDP agent is enabled
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: lldpstatsrxporttlvsdiscardedtotal
            
            	The number of LLDP TLVs discarded for any reason by this LLDP agent on the indicated port
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: lldpstatsrxporttlvsunrecognizedtotal
            
            	The number of LLDP TLVs received on the given port that are not recognized by this LLDP agent on the indicated port.  An unrecognized TLV is referred to as the TLV whose type value is in the range of reserved TLV types (000 1001 \- 111 1110) in Table 9.1 of IEEE Std 802.1AB\-2005.  An unrecognized TLV may be a basic management TLV from a later LLDP version
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: lldpstatsrxportageoutstotal
            
            	The counter that represents the number of age\-outs that occurred on a given port.  An age\-out is the number of times the complete set of information advertised by a particular MSAP has been deleted from tables contained in lldpRemoteSystemsData and lldpExtensions objects because the information timeliness interval has expired.  This counter is similar to lldpStatsRemTablesAgeouts, except that the counter is on a per port basis.  This enables NMS to poll tables associated with the lldpRemoteSystemsData objects and all LLDP extension objects associated with remote systems on the indicated port only.  This counter should be set to zero during agent initialization and its value should not be saved in non\-volatile storage. When a port's admin status changes from 'disabled' to 'rxOnly', 'txOnly' or 'txAndRx', the counter associated with the same port should reset to 0.  The agent should also flush all remote system information associated with the same port.  This counter should be incremented only once when the complete set of information is invalidated (aged out) from all related tables on a particular port.  Partial aging is not allowed, and thus, should not change the value of this counter
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'LLDP-MIB'
            _revision = '2005-05-06'

            def __init__(self):
                super(LLDPMIB.LldpStatsRxPortTable.LldpStatsRxPortEntry, self).__init__()

                self.yang_name = "lldpStatsRxPortEntry"
                self.yang_parent_name = "lldpStatsRxPortTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['lldpstatsrxportnum']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('lldpstatsrxportnum', (YLeaf(YType.int32, 'lldpStatsRxPortNum'), ['int'])),
                    ('lldpstatsrxportframesdiscardedtotal', (YLeaf(YType.uint32, 'lldpStatsRxPortFramesDiscardedTotal'), ['int'])),
                    ('lldpstatsrxportframeserrors', (YLeaf(YType.uint32, 'lldpStatsRxPortFramesErrors'), ['int'])),
                    ('lldpstatsrxportframestotal', (YLeaf(YType.uint32, 'lldpStatsRxPortFramesTotal'), ['int'])),
                    ('lldpstatsrxporttlvsdiscardedtotal', (YLeaf(YType.uint32, 'lldpStatsRxPortTLVsDiscardedTotal'), ['int'])),
                    ('lldpstatsrxporttlvsunrecognizedtotal', (YLeaf(YType.uint32, 'lldpStatsRxPortTLVsUnrecognizedTotal'), ['int'])),
                    ('lldpstatsrxportageoutstotal', (YLeaf(YType.uint32, 'lldpStatsRxPortAgeoutsTotal'), ['int'])),
                ])
                self.lldpstatsrxportnum = None
                self.lldpstatsrxportframesdiscardedtotal = None
                self.lldpstatsrxportframeserrors = None
                self.lldpstatsrxportframestotal = None
                self.lldpstatsrxporttlvsdiscardedtotal = None
                self.lldpstatsrxporttlvsunrecognizedtotal = None
                self.lldpstatsrxportageoutstotal = None
                self._segment_path = lambda: "lldpStatsRxPortEntry" + "[lldpStatsRxPortNum='" + str(self.lldpstatsrxportnum) + "']"
                self._absolute_path = lambda: "LLDP-MIB:LLDP-MIB/lldpStatsRxPortTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(LLDPMIB.LldpStatsRxPortTable.LldpStatsRxPortEntry, ['lldpstatsrxportnum', 'lldpstatsrxportframesdiscardedtotal', 'lldpstatsrxportframeserrors', 'lldpstatsrxportframestotal', 'lldpstatsrxporttlvsdiscardedtotal', 'lldpstatsrxporttlvsunrecognizedtotal', 'lldpstatsrxportageoutstotal'], name, value)




    class LldpLocPortTable(Entity):
        """
        This table contains one or more rows per port information
        associated with the local system known to this agent.
        
        .. attribute:: lldplocportentry
        
        	Information about a particular port component.  Entries may be created and deleted in this table by the agent
        	**type**\: list of  		 :py:class:`LldpLocPortEntry <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.LldpLocPortTable.LldpLocPortEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'LLDP-MIB'
        _revision = '2005-05-06'

        def __init__(self):
            super(LLDPMIB.LldpLocPortTable, self).__init__()

            self.yang_name = "lldpLocPortTable"
            self.yang_parent_name = "LLDP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("lldpLocPortEntry", ("lldplocportentry", LLDPMIB.LldpLocPortTable.LldpLocPortEntry))])
            self._leafs = OrderedDict()

            self.lldplocportentry = YList(self)
            self._segment_path = lambda: "lldpLocPortTable"
            self._absolute_path = lambda: "LLDP-MIB:LLDP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(LLDPMIB.LldpLocPortTable, [], name, value)


        class LldpLocPortEntry(Entity):
            """
            Information about a particular port component.
            
            Entries may be created and deleted in this table by the
            agent.
            
            .. attribute:: lldplocportnum  (key)
            
            	The index value used to identify the port component (contained in the local chassis with the LLDP agent) associated with this entry.  The value of this object is used as a port index to the lldpLocPortTable
            	**type**\: int
            
            	**range:** 1..4096
            
            	**config**\: False
            
            .. attribute:: lldplocportidsubtype
            
            	The type of port identifier encoding used in the associated 'lldpLocPortId' object
            	**type**\:  :py:class:`LldpPortIdSubtype <ydk.models.cisco_ios_xe.LLDP_MIB.LldpPortIdSubtype>`
            
            	**config**\: False
            
            .. attribute:: lldplocportid
            
            	The string value used to identify the port component associated with a given port in the local system
            	**type**\: str
            
            	**length:** 1..255
            
            	**config**\: False
            
            .. attribute:: lldplocportdesc
            
            	The string value used to identify the 802 LAN station's port description associated with the local system.  If the local agent supports IETF RFC 2863, lldpLocPortDesc object should have the same value of ifDescr object
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            

            """

            _prefix = 'LLDP-MIB'
            _revision = '2005-05-06'

            def __init__(self):
                super(LLDPMIB.LldpLocPortTable.LldpLocPortEntry, self).__init__()

                self.yang_name = "lldpLocPortEntry"
                self.yang_parent_name = "lldpLocPortTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['lldplocportnum']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('lldplocportnum', (YLeaf(YType.int32, 'lldpLocPortNum'), ['int'])),
                    ('lldplocportidsubtype', (YLeaf(YType.enumeration, 'lldpLocPortIdSubtype'), [('ydk.models.cisco_ios_xe.LLDP_MIB', 'LldpPortIdSubtype', '')])),
                    ('lldplocportid', (YLeaf(YType.str, 'lldpLocPortId'), ['str'])),
                    ('lldplocportdesc', (YLeaf(YType.str, 'lldpLocPortDesc'), ['str'])),
                ])
                self.lldplocportnum = None
                self.lldplocportidsubtype = None
                self.lldplocportid = None
                self.lldplocportdesc = None
                self._segment_path = lambda: "lldpLocPortEntry" + "[lldpLocPortNum='" + str(self.lldplocportnum) + "']"
                self._absolute_path = lambda: "LLDP-MIB:LLDP-MIB/lldpLocPortTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(LLDPMIB.LldpLocPortTable.LldpLocPortEntry, ['lldplocportnum', 'lldplocportidsubtype', 'lldplocportid', 'lldplocportdesc'], name, value)




    class LldpLocManAddrTable(Entity):
        """
        This table contains management address information on the
        local system known to this agent.
        
        .. attribute:: lldplocmanaddrentry
        
        	Management address information about a particular chassis component.  There may be multiple management addresses configured on the system identified by a particular lldpLocChassisId.  Each management address should have distinct 'management address type' (lldpLocManAddrSubtype) and 'management address' (lldpLocManAddr.)  Entries may be created and deleted in this table by the agent
        	**type**\: list of  		 :py:class:`LldpLocManAddrEntry <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.LldpLocManAddrTable.LldpLocManAddrEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'LLDP-MIB'
        _revision = '2005-05-06'

        def __init__(self):
            super(LLDPMIB.LldpLocManAddrTable, self).__init__()

            self.yang_name = "lldpLocManAddrTable"
            self.yang_parent_name = "LLDP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("lldpLocManAddrEntry", ("lldplocmanaddrentry", LLDPMIB.LldpLocManAddrTable.LldpLocManAddrEntry))])
            self._leafs = OrderedDict()

            self.lldplocmanaddrentry = YList(self)
            self._segment_path = lambda: "lldpLocManAddrTable"
            self._absolute_path = lambda: "LLDP-MIB:LLDP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(LLDPMIB.LldpLocManAddrTable, [], name, value)


        class LldpLocManAddrEntry(Entity):
            """
            Management address information about a particular chassis
            component.  There may be multiple management addresses
            configured on the system identified by a particular
            lldpLocChassisId.  Each management address should have
            distinct 'management address type' (lldpLocManAddrSubtype) and
            'management address' (lldpLocManAddr.)
            
            Entries may be created and deleted in this table by the
            agent.
            
            .. attribute:: lldplocmanaddrsubtype  (key)
            
            	The type of management address identifier encoding used in the associated 'lldpLocManagmentAddr' object
            	**type**\:  :py:class:`AddressFamilyNumbers <ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB.AddressFamilyNumbers>`
            
            	**config**\: False
            
            .. attribute:: lldplocmanaddr  (key)
            
            	The string value used to identify the management address component associated with the local system.  The purpose of this address is to contact the management entity
            	**type**\: str
            
            	**length:** 1..31
            
            	**config**\: False
            
            .. attribute:: lldplocmanaddrlen
            
            	The total length of the management address subtype and the management address fields in LLDPDUs transmitted by the local LLDP agent.  The management address length field is needed so that the receiving systems that do not implement SNMP will not be required to implement an iana family numbers/address length equivalency table in order to decode the management adress
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: lldplocmanaddrifsubtype
            
            	The enumeration value that identifies the interface numbering method used for defining the interface number, associated with the local system
            	**type**\:  :py:class:`LldpManAddrIfSubtype <ydk.models.cisco_ios_xe.LLDP_MIB.LldpManAddrIfSubtype>`
            
            	**config**\: False
            
            .. attribute:: lldplocmanaddrifid
            
            	The integer value used to identify the interface number regarding the management address component associated with the local system
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: lldplocmanaddroid
            
            	The OID value used to identify the type of hardware component or protocol entity associated with the management address advertised by the local system agent
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            .. attribute:: lldpconfigmanaddrportstxenable
            
            	A set of ports that are identified by a PortList, in which each port is represented as a bit.  The corresponding local system management address instance will be transmitted on the member ports of the lldpManAddrPortsTxEnable.    The default value for lldpConfigManAddrPortsTxEnable object is empty binary string, which means no ports are specified for advertising indicated management address instance
            	**type**\: str
            
            	**length:** 0..512
            
            	**config**\: False
            
            

            """

            _prefix = 'LLDP-MIB'
            _revision = '2005-05-06'

            def __init__(self):
                super(LLDPMIB.LldpLocManAddrTable.LldpLocManAddrEntry, self).__init__()

                self.yang_name = "lldpLocManAddrEntry"
                self.yang_parent_name = "lldpLocManAddrTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['lldplocmanaddrsubtype','lldplocmanaddr']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('lldplocmanaddrsubtype', (YLeaf(YType.enumeration, 'lldpLocManAddrSubtype'), [('ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB', 'AddressFamilyNumbers', '')])),
                    ('lldplocmanaddr', (YLeaf(YType.str, 'lldpLocManAddr'), ['str'])),
                    ('lldplocmanaddrlen', (YLeaf(YType.int32, 'lldpLocManAddrLen'), ['int'])),
                    ('lldplocmanaddrifsubtype', (YLeaf(YType.enumeration, 'lldpLocManAddrIfSubtype'), [('ydk.models.cisco_ios_xe.LLDP_MIB', 'LldpManAddrIfSubtype', '')])),
                    ('lldplocmanaddrifid', (YLeaf(YType.int32, 'lldpLocManAddrIfId'), ['int'])),
                    ('lldplocmanaddroid', (YLeaf(YType.str, 'lldpLocManAddrOID'), ['str'])),
                    ('lldpconfigmanaddrportstxenable', (YLeaf(YType.str, 'lldpConfigManAddrPortsTxEnable'), ['str'])),
                ])
                self.lldplocmanaddrsubtype = None
                self.lldplocmanaddr = None
                self.lldplocmanaddrlen = None
                self.lldplocmanaddrifsubtype = None
                self.lldplocmanaddrifid = None
                self.lldplocmanaddroid = None
                self.lldpconfigmanaddrportstxenable = None
                self._segment_path = lambda: "lldpLocManAddrEntry" + "[lldpLocManAddrSubtype='" + str(self.lldplocmanaddrsubtype) + "']" + "[lldpLocManAddr='" + str(self.lldplocmanaddr) + "']"
                self._absolute_path = lambda: "LLDP-MIB:LLDP-MIB/lldpLocManAddrTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(LLDPMIB.LldpLocManAddrTable.LldpLocManAddrEntry, ['lldplocmanaddrsubtype', 'lldplocmanaddr', 'lldplocmanaddrlen', 'lldplocmanaddrifsubtype', 'lldplocmanaddrifid', 'lldplocmanaddroid', 'lldpconfigmanaddrportstxenable'], name, value)




    class LldpRemTable(Entity):
        """
        This table contains one or more rows per physical network
        connection known to this agent.  The agent may wish to ensure
        that only one lldpRemEntry is present for each local port,
        or it may choose to maintain multiple lldpRemEntries for
        the same local port.
        
        The following procedure may be used to retrieve remote
        systems information updates from an LLDP agent\:
        
           1. NMS polls all tables associated with remote systems
              and keeps a local copy of the information retrieved.
              NMS polls periodically the values of the following
              objects\:
                 a. lldpStatsRemTablesInserts
                 b. lldpStatsRemTablesDeletes
                 c. lldpStatsRemTablesDrops
                 d. lldpStatsRemTablesAgeouts
                 e. lldpStatsRxPortAgeoutsTotal for all ports.
        
           2. LLDP agent updates remote systems MIB objects, and
              sends out notifications to a list of notification
              destinations.
        
           3. NMS receives the notifications and compares the new
              values of objects listed in step 1.  
        
              Periodically, NMS should poll the object
              lldpStatsRemTablesLastChangeTime to find out if anything
              has changed since the last poll.  if something has
              changed, NMS will poll the objects listed in step 1 to
              figure out what kind of changes occurred in the tables.
        
              if value of lldpStatsRemTablesInserts has changed,
              then NMS will walk all tables by employing TimeFilter
              with the last\-polled time value.  This request will
              return new objects or objects whose values are updated
              since the last poll.
        
              if value of lldpStatsRemTablesAgeouts has changed,
              then NMS will walk the lldpStatsRxPortAgeoutsTotal and
              compare the new values with previously recorded ones.
              For ports whose lldpStatsRxPortAgeoutsTotal value is
              greater than the recorded value, NMS will have to
              retrieve objects associated with those ports from
              table(s) without employing a TimeFilter (which is
              performed by specifying 0 for the TimeFilter.)
        
              lldpStatsRemTablesDeletes and lldpStatsRemTablesDrops
              objects are provided for informational purposes.
        
        .. attribute:: lldprementry
        
        	Information about a particular physical network connection. Entries may be created and deleted in this table by the agent, if a physical topology discovery process is active
        	**type**\: list of  		 :py:class:`LldpRemEntry <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.LldpRemTable.LldpRemEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'LLDP-MIB'
        _revision = '2005-05-06'

        def __init__(self):
            super(LLDPMIB.LldpRemTable, self).__init__()

            self.yang_name = "lldpRemTable"
            self.yang_parent_name = "LLDP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("lldpRemEntry", ("lldprementry", LLDPMIB.LldpRemTable.LldpRemEntry))])
            self._leafs = OrderedDict()

            self.lldprementry = YList(self)
            self._segment_path = lambda: "lldpRemTable"
            self._absolute_path = lambda: "LLDP-MIB:LLDP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(LLDPMIB.LldpRemTable, [], name, value)


        class LldpRemEntry(Entity):
            """
            Information about a particular physical network connection.
            Entries may be created and deleted in this table by the agent,
            if a physical topology discovery process is active.
            
            .. attribute:: lldpremtimemark  (key)
            
            	A TimeFilter for this entry.  See the TimeFilter textual convention in IETF RFC 2021 and  http\://www.ietf.org/IESG/Implementations/RFC2021\-Implementation.txt to see how TimeFilter works
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: lldpremlocalportnum  (key)
            
            	The index value used to identify the port component (contained in the local chassis with the LLDP agent) associated with this entry.  The lldpRemLocalPortNum identifies the port on which the remote system information is received.  The value of this object is used as a port index to the lldpRemTable
            	**type**\: int
            
            	**range:** 1..4096
            
            	**config**\: False
            
            .. attribute:: lldpremindex  (key)
            
            	This object represents an arbitrary local integer value used by this agent to identify a particular connection instance, unique only for the indicated remote system.  An agent is encouraged to assign monotonically increasing index values to new entries, starting with one, after each reboot.  It is considered unlikely that the lldpRemIndex will wrap between reboots
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: lldpremchassisidsubtype
            
            	The type of encoding used to identify the chassis associated with the remote system
            	**type**\:  :py:class:`LldpChassisIdSubtype <ydk.models.cisco_ios_xe.LLDP_MIB.LldpChassisIdSubtype>`
            
            	**config**\: False
            
            .. attribute:: lldpremchassisid
            
            	The string value used to identify the chassis component associated with the remote system
            	**type**\: str
            
            	**length:** 1..255
            
            	**config**\: False
            
            .. attribute:: lldpremportidsubtype
            
            	The type of port identifier encoding used in the associated 'lldpRemPortId' object
            	**type**\:  :py:class:`LldpPortIdSubtype <ydk.models.cisco_ios_xe.LLDP_MIB.LldpPortIdSubtype>`
            
            	**config**\: False
            
            .. attribute:: lldpremportid
            
            	The string value used to identify the port component associated with the remote system
            	**type**\: str
            
            	**length:** 1..255
            
            	**config**\: False
            
            .. attribute:: lldpremportdesc
            
            	The string value used to identify the description of the given port associated with the remote system
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: lldpremsysname
            
            	The string value used to identify the system name of the remote system
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: lldpremsysdesc
            
            	The string value used to identify the system description of the remote system
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: lldpremsyscapsupported
            
            	The bitmap value used to identify which system capabilities are supported on the remote system
            	**type**\:  :py:class:`LldpSystemCapabilitiesMap <ydk.models.cisco_ios_xe.LLDP_MIB.LldpSystemCapabilitiesMap>`
            
            	**config**\: False
            
            .. attribute:: lldpremsyscapenabled
            
            	The bitmap value used to identify which system capabilities are enabled on the remote system
            	**type**\:  :py:class:`LldpSystemCapabilitiesMap <ydk.models.cisco_ios_xe.LLDP_MIB.LldpSystemCapabilitiesMap>`
            
            	**config**\: False
            
            

            """

            _prefix = 'LLDP-MIB'
            _revision = '2005-05-06'

            def __init__(self):
                super(LLDPMIB.LldpRemTable.LldpRemEntry, self).__init__()

                self.yang_name = "lldpRemEntry"
                self.yang_parent_name = "lldpRemTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['lldpremtimemark','lldpremlocalportnum','lldpremindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('lldpremtimemark', (YLeaf(YType.uint32, 'lldpRemTimeMark'), ['int'])),
                    ('lldpremlocalportnum', (YLeaf(YType.int32, 'lldpRemLocalPortNum'), ['int'])),
                    ('lldpremindex', (YLeaf(YType.int32, 'lldpRemIndex'), ['int'])),
                    ('lldpremchassisidsubtype', (YLeaf(YType.enumeration, 'lldpRemChassisIdSubtype'), [('ydk.models.cisco_ios_xe.LLDP_MIB', 'LldpChassisIdSubtype', '')])),
                    ('lldpremchassisid', (YLeaf(YType.str, 'lldpRemChassisId'), ['str'])),
                    ('lldpremportidsubtype', (YLeaf(YType.enumeration, 'lldpRemPortIdSubtype'), [('ydk.models.cisco_ios_xe.LLDP_MIB', 'LldpPortIdSubtype', '')])),
                    ('lldpremportid', (YLeaf(YType.str, 'lldpRemPortId'), ['str'])),
                    ('lldpremportdesc', (YLeaf(YType.str, 'lldpRemPortDesc'), ['str'])),
                    ('lldpremsysname', (YLeaf(YType.str, 'lldpRemSysName'), ['str'])),
                    ('lldpremsysdesc', (YLeaf(YType.str, 'lldpRemSysDesc'), ['str'])),
                    ('lldpremsyscapsupported', (YLeaf(YType.bits, 'lldpRemSysCapSupported'), ['Bits'])),
                    ('lldpremsyscapenabled', (YLeaf(YType.bits, 'lldpRemSysCapEnabled'), ['Bits'])),
                ])
                self.lldpremtimemark = None
                self.lldpremlocalportnum = None
                self.lldpremindex = None
                self.lldpremchassisidsubtype = None
                self.lldpremchassisid = None
                self.lldpremportidsubtype = None
                self.lldpremportid = None
                self.lldpremportdesc = None
                self.lldpremsysname = None
                self.lldpremsysdesc = None
                self.lldpremsyscapsupported = Bits()
                self.lldpremsyscapenabled = Bits()
                self._segment_path = lambda: "lldpRemEntry" + "[lldpRemTimeMark='" + str(self.lldpremtimemark) + "']" + "[lldpRemLocalPortNum='" + str(self.lldpremlocalportnum) + "']" + "[lldpRemIndex='" + str(self.lldpremindex) + "']"
                self._absolute_path = lambda: "LLDP-MIB:LLDP-MIB/lldpRemTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(LLDPMIB.LldpRemTable.LldpRemEntry, ['lldpremtimemark', 'lldpremlocalportnum', 'lldpremindex', 'lldpremchassisidsubtype', 'lldpremchassisid', 'lldpremportidsubtype', 'lldpremportid', 'lldpremportdesc', 'lldpremsysname', 'lldpremsysdesc', 'lldpremsyscapsupported', 'lldpremsyscapenabled'], name, value)




    class LldpRemManAddrTable(Entity):
        """
        This table contains one or more rows per management address
        information on the remote system learned on a particular port
        contained in the local chassis known to this agent.
        
        .. attribute:: lldpremmanaddrentry
        
        	Management address information about a particular chassis component.  There may be multiple management addresses configured on the remote system identified by a particular lldpRemIndex whose information is received on lldpRemLocalPortNum of the local system.  Each management address should have distinct 'management address type' (lldpRemManAddrSubtype) and 'management address' (lldpRemManAddr.)  Entries may be created and deleted in this table by the agent
        	**type**\: list of  		 :py:class:`LldpRemManAddrEntry <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.LldpRemManAddrTable.LldpRemManAddrEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'LLDP-MIB'
        _revision = '2005-05-06'

        def __init__(self):
            super(LLDPMIB.LldpRemManAddrTable, self).__init__()

            self.yang_name = "lldpRemManAddrTable"
            self.yang_parent_name = "LLDP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("lldpRemManAddrEntry", ("lldpremmanaddrentry", LLDPMIB.LldpRemManAddrTable.LldpRemManAddrEntry))])
            self._leafs = OrderedDict()

            self.lldpremmanaddrentry = YList(self)
            self._segment_path = lambda: "lldpRemManAddrTable"
            self._absolute_path = lambda: "LLDP-MIB:LLDP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(LLDPMIB.LldpRemManAddrTable, [], name, value)


        class LldpRemManAddrEntry(Entity):
            """
            Management address information about a particular chassis
            component.  There may be multiple management addresses
            configured on the remote system identified by a particular
            lldpRemIndex whose information is received on
            lldpRemLocalPortNum of the local system.  Each management
            address should have distinct 'management address
            type' (lldpRemManAddrSubtype) and 'management address'
            (lldpRemManAddr.)
            
            Entries may be created and deleted in this table by the
            agent.
            
            .. attribute:: lldpremtimemark  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`lldpremtimemark <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.LldpRemTable.LldpRemEntry>`
            
            	**config**\: False
            
            .. attribute:: lldpremlocalportnum  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4096
            
            	**refers to**\:  :py:class:`lldpremlocalportnum <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.LldpRemTable.LldpRemEntry>`
            
            	**config**\: False
            
            .. attribute:: lldpremindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`lldpremindex <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.LldpRemTable.LldpRemEntry>`
            
            	**config**\: False
            
            .. attribute:: lldpremmanaddrsubtype  (key)
            
            	The type of management address identifier encoding used in the associated 'lldpRemManagmentAddr' object
            	**type**\:  :py:class:`AddressFamilyNumbers <ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB.AddressFamilyNumbers>`
            
            	**config**\: False
            
            .. attribute:: lldpremmanaddr  (key)
            
            	The string value used to identify the management address component associated with the remote system.  The purpose of this address is to contact the management entity
            	**type**\: str
            
            	**length:** 1..31
            
            	**config**\: False
            
            .. attribute:: lldpremmanaddrifsubtype
            
            	The enumeration value that identifies the interface numbering method used for defining the interface number, associated with the remote system
            	**type**\:  :py:class:`LldpManAddrIfSubtype <ydk.models.cisco_ios_xe.LLDP_MIB.LldpManAddrIfSubtype>`
            
            	**config**\: False
            
            .. attribute:: lldpremmanaddrifid
            
            	The integer value used to identify the interface number regarding the management address component associated with the remote system
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: lldpremmanaddroid
            
            	The OID value used to identify the type of hardware component or protocol entity associated with the management address advertised by the remote system agent
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            

            """

            _prefix = 'LLDP-MIB'
            _revision = '2005-05-06'

            def __init__(self):
                super(LLDPMIB.LldpRemManAddrTable.LldpRemManAddrEntry, self).__init__()

                self.yang_name = "lldpRemManAddrEntry"
                self.yang_parent_name = "lldpRemManAddrTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['lldpremtimemark','lldpremlocalportnum','lldpremindex','lldpremmanaddrsubtype','lldpremmanaddr']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('lldpremtimemark', (YLeaf(YType.str, 'lldpRemTimeMark'), ['int'])),
                    ('lldpremlocalportnum', (YLeaf(YType.str, 'lldpRemLocalPortNum'), ['int'])),
                    ('lldpremindex', (YLeaf(YType.str, 'lldpRemIndex'), ['int'])),
                    ('lldpremmanaddrsubtype', (YLeaf(YType.enumeration, 'lldpRemManAddrSubtype'), [('ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB', 'AddressFamilyNumbers', '')])),
                    ('lldpremmanaddr', (YLeaf(YType.str, 'lldpRemManAddr'), ['str'])),
                    ('lldpremmanaddrifsubtype', (YLeaf(YType.enumeration, 'lldpRemManAddrIfSubtype'), [('ydk.models.cisco_ios_xe.LLDP_MIB', 'LldpManAddrIfSubtype', '')])),
                    ('lldpremmanaddrifid', (YLeaf(YType.int32, 'lldpRemManAddrIfId'), ['int'])),
                    ('lldpremmanaddroid', (YLeaf(YType.str, 'lldpRemManAddrOID'), ['str'])),
                ])
                self.lldpremtimemark = None
                self.lldpremlocalportnum = None
                self.lldpremindex = None
                self.lldpremmanaddrsubtype = None
                self.lldpremmanaddr = None
                self.lldpremmanaddrifsubtype = None
                self.lldpremmanaddrifid = None
                self.lldpremmanaddroid = None
                self._segment_path = lambda: "lldpRemManAddrEntry" + "[lldpRemTimeMark='" + str(self.lldpremtimemark) + "']" + "[lldpRemLocalPortNum='" + str(self.lldpremlocalportnum) + "']" + "[lldpRemIndex='" + str(self.lldpremindex) + "']" + "[lldpRemManAddrSubtype='" + str(self.lldpremmanaddrsubtype) + "']" + "[lldpRemManAddr='" + str(self.lldpremmanaddr) + "']"
                self._absolute_path = lambda: "LLDP-MIB:LLDP-MIB/lldpRemManAddrTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(LLDPMIB.LldpRemManAddrTable.LldpRemManAddrEntry, ['lldpremtimemark', 'lldpremlocalportnum', 'lldpremindex', 'lldpremmanaddrsubtype', 'lldpremmanaddr', 'lldpremmanaddrifsubtype', 'lldpremmanaddrifid', 'lldpremmanaddroid'], name, value)




    class LldpRemUnknownTLVTable(Entity):
        """
        This table contains information about an incoming TLV which
        is not recognized by the receiving LLDP agent.  The TLV may
        be from a later version of the basic management set.
        
        This table should only contain TLVs that are found in
        a single LLDP frame.  Entries in this table, associated
        with an MAC service access point (MSAP, the access point
        for MAC services provided to the LCC sublayer, defined
        in IEEE 100, which is also identified with a particular
        lldpRemLocalPortNum, lldpRemIndex pair) are overwritten with
        most recently received unrecognized TLV from the same MSAP,
        or they will naturally age out when the rxInfoTTL timer
        (associated with the MSAP) expires.
        
        .. attribute:: lldpremunknowntlventry
        
        	Information about an unrecognized TLV received from a physical network connection.  Entries may be created and deleted in this table by the agent, if a physical topology discovery process is active
        	**type**\: list of  		 :py:class:`LldpRemUnknownTLVEntry <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.LldpRemUnknownTLVTable.LldpRemUnknownTLVEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'LLDP-MIB'
        _revision = '2005-05-06'

        def __init__(self):
            super(LLDPMIB.LldpRemUnknownTLVTable, self).__init__()

            self.yang_name = "lldpRemUnknownTLVTable"
            self.yang_parent_name = "LLDP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("lldpRemUnknownTLVEntry", ("lldpremunknowntlventry", LLDPMIB.LldpRemUnknownTLVTable.LldpRemUnknownTLVEntry))])
            self._leafs = OrderedDict()

            self.lldpremunknowntlventry = YList(self)
            self._segment_path = lambda: "lldpRemUnknownTLVTable"
            self._absolute_path = lambda: "LLDP-MIB:LLDP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(LLDPMIB.LldpRemUnknownTLVTable, [], name, value)


        class LldpRemUnknownTLVEntry(Entity):
            """
            Information about an unrecognized TLV received from a
            physical network connection.  Entries may be created and
            deleted in this table by the agent, if a physical topology
            discovery process is active.
            
            .. attribute:: lldpremtimemark  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`lldpremtimemark <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.LldpRemTable.LldpRemEntry>`
            
            	**config**\: False
            
            .. attribute:: lldpremlocalportnum  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4096
            
            	**refers to**\:  :py:class:`lldpremlocalportnum <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.LldpRemTable.LldpRemEntry>`
            
            	**config**\: False
            
            .. attribute:: lldpremindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`lldpremindex <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.LldpRemTable.LldpRemEntry>`
            
            	**config**\: False
            
            .. attribute:: lldpremunknowntlvtype  (key)
            
            	This object represents the value extracted from the type field of the TLV
            	**type**\: int
            
            	**range:** 9..126
            
            	**config**\: False
            
            .. attribute:: lldpremunknowntlvinfo
            
            	This object represents the value extracted from the value field of the TLV
            	**type**\: str
            
            	**length:** 0..511
            
            	**config**\: False
            
            

            """

            _prefix = 'LLDP-MIB'
            _revision = '2005-05-06'

            def __init__(self):
                super(LLDPMIB.LldpRemUnknownTLVTable.LldpRemUnknownTLVEntry, self).__init__()

                self.yang_name = "lldpRemUnknownTLVEntry"
                self.yang_parent_name = "lldpRemUnknownTLVTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['lldpremtimemark','lldpremlocalportnum','lldpremindex','lldpremunknowntlvtype']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('lldpremtimemark', (YLeaf(YType.str, 'lldpRemTimeMark'), ['int'])),
                    ('lldpremlocalportnum', (YLeaf(YType.str, 'lldpRemLocalPortNum'), ['int'])),
                    ('lldpremindex', (YLeaf(YType.str, 'lldpRemIndex'), ['int'])),
                    ('lldpremunknowntlvtype', (YLeaf(YType.int32, 'lldpRemUnknownTLVType'), ['int'])),
                    ('lldpremunknowntlvinfo', (YLeaf(YType.str, 'lldpRemUnknownTLVInfo'), ['str'])),
                ])
                self.lldpremtimemark = None
                self.lldpremlocalportnum = None
                self.lldpremindex = None
                self.lldpremunknowntlvtype = None
                self.lldpremunknowntlvinfo = None
                self._segment_path = lambda: "lldpRemUnknownTLVEntry" + "[lldpRemTimeMark='" + str(self.lldpremtimemark) + "']" + "[lldpRemLocalPortNum='" + str(self.lldpremlocalportnum) + "']" + "[lldpRemIndex='" + str(self.lldpremindex) + "']" + "[lldpRemUnknownTLVType='" + str(self.lldpremunknowntlvtype) + "']"
                self._absolute_path = lambda: "LLDP-MIB:LLDP-MIB/lldpRemUnknownTLVTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(LLDPMIB.LldpRemUnknownTLVTable.LldpRemUnknownTLVEntry, ['lldpremtimemark', 'lldpremlocalportnum', 'lldpremindex', 'lldpremunknowntlvtype', 'lldpremunknowntlvinfo'], name, value)




    class LldpRemOrgDefInfoTable(Entity):
        """
        This table contains one or more rows per physical network
        connection which advertises the organizationally defined
        information.
        
        Note that this table contains one or more rows of
        organizationally defined information that is not recognized
        by the local agent.
        
        If the local system is capable of recognizing any
        organizationally defined information, appropriate extension
        MIBs from the organization should be used for information
        retrieval.
        
        .. attribute:: lldpremorgdefinfoentry
        
        	Information about the unrecognized organizationally defined information advertised by the remote system. The lldpRemTimeMark, lldpRemLocalPortNum, lldpRemIndex, lldpRemOrgDefInfoOUI, lldpRemOrgDefInfoSubtype, and lldpRemOrgDefInfoIndex are indexes to this table.  If there is an lldpRemOrgDefInfoEntry associated with a particular remote system identified by the lldpRemLocalPortNum and lldpRemIndex, there must be an lldpRemEntry associated with the same instance (i.e, using same indexes.)  When the lldpRemEntry for the same index is removed from the lldpRemTable, the associated lldpRemOrgDefInfoEntry should be removed from the lldpRemOrgDefInfoTable.  Entries may be created and deleted in this table by the agent
        	**type**\: list of  		 :py:class:`LldpRemOrgDefInfoEntry <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.LldpRemOrgDefInfoTable.LldpRemOrgDefInfoEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'LLDP-MIB'
        _revision = '2005-05-06'

        def __init__(self):
            super(LLDPMIB.LldpRemOrgDefInfoTable, self).__init__()

            self.yang_name = "lldpRemOrgDefInfoTable"
            self.yang_parent_name = "LLDP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("lldpRemOrgDefInfoEntry", ("lldpremorgdefinfoentry", LLDPMIB.LldpRemOrgDefInfoTable.LldpRemOrgDefInfoEntry))])
            self._leafs = OrderedDict()

            self.lldpremorgdefinfoentry = YList(self)
            self._segment_path = lambda: "lldpRemOrgDefInfoTable"
            self._absolute_path = lambda: "LLDP-MIB:LLDP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(LLDPMIB.LldpRemOrgDefInfoTable, [], name, value)


        class LldpRemOrgDefInfoEntry(Entity):
            """
            Information about the unrecognized organizationally
            defined information advertised by the remote system.
            The lldpRemTimeMark, lldpRemLocalPortNum, lldpRemIndex,
            lldpRemOrgDefInfoOUI, lldpRemOrgDefInfoSubtype, and
            lldpRemOrgDefInfoIndex are indexes to this table.  If there is
            an lldpRemOrgDefInfoEntry associated with a particular remote
            system identified by the lldpRemLocalPortNum and lldpRemIndex,
            there must be an lldpRemEntry associated with the same
            instance (i.e, using same indexes.)  When the lldpRemEntry
            for the same index is removed from the lldpRemTable, the
            associated lldpRemOrgDefInfoEntry should be removed from
            the lldpRemOrgDefInfoTable.
            
            Entries may be created and deleted in this table by the
            agent.
            
            .. attribute:: lldpremtimemark  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`lldpremtimemark <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.LldpRemTable.LldpRemEntry>`
            
            	**config**\: False
            
            .. attribute:: lldpremlocalportnum  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4096
            
            	**refers to**\:  :py:class:`lldpremlocalportnum <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.LldpRemTable.LldpRemEntry>`
            
            	**config**\: False
            
            .. attribute:: lldpremindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`lldpremindex <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.LldpRemTable.LldpRemEntry>`
            
            	**config**\: False
            
            .. attribute:: lldpremorgdefinfooui  (key)
            
            	The Organizationally Unique Identifier (OUI), as defined in IEEE std 802\-2001, is a 24 bit (three octets) globally unique assigned number referenced by various standards, of the information received from the remote system
            	**type**\: str
            
            	**length:** 3
            
            	**config**\: False
            
            .. attribute:: lldpremorgdefinfosubtype  (key)
            
            	The integer value used to identify the subtype of the organizationally defined information received from the remote system.  The subtype value is required to identify different instances of organizationally defined information that could not be retrieved without a unique identifier that indicates the particular type of information contained in the information string
            	**type**\: int
            
            	**range:** 1..255
            
            	**config**\: False
            
            .. attribute:: lldpremorgdefinfoindex  (key)
            
            	This object represents an arbitrary local integer value used by this agent to identify a particular unrecognized organizationally defined information instance, unique only for the lldpRemOrgDefInfoOUI and lldpRemOrgDefInfoSubtype from the same remote system.  An agent is encouraged to assign monotonically increasing index values to new entries, starting with one, after each reboot.  It is considered unlikely that the lldpRemOrgDefInfoIndex will wrap between reboots
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: lldpremorgdefinfo
            
            	The string value used to identify the organizationally defined information of the remote system.  The encoding for this object should be as defined for SnmpAdminString TC
            	**type**\: str
            
            	**length:** 0..507
            
            	**config**\: False
            
            

            """

            _prefix = 'LLDP-MIB'
            _revision = '2005-05-06'

            def __init__(self):
                super(LLDPMIB.LldpRemOrgDefInfoTable.LldpRemOrgDefInfoEntry, self).__init__()

                self.yang_name = "lldpRemOrgDefInfoEntry"
                self.yang_parent_name = "lldpRemOrgDefInfoTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['lldpremtimemark','lldpremlocalportnum','lldpremindex','lldpremorgdefinfooui','lldpremorgdefinfosubtype','lldpremorgdefinfoindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('lldpremtimemark', (YLeaf(YType.str, 'lldpRemTimeMark'), ['int'])),
                    ('lldpremlocalportnum', (YLeaf(YType.str, 'lldpRemLocalPortNum'), ['int'])),
                    ('lldpremindex', (YLeaf(YType.str, 'lldpRemIndex'), ['int'])),
                    ('lldpremorgdefinfooui', (YLeaf(YType.str, 'lldpRemOrgDefInfoOUI'), ['str'])),
                    ('lldpremorgdefinfosubtype', (YLeaf(YType.int32, 'lldpRemOrgDefInfoSubtype'), ['int'])),
                    ('lldpremorgdefinfoindex', (YLeaf(YType.int32, 'lldpRemOrgDefInfoIndex'), ['int'])),
                    ('lldpremorgdefinfo', (YLeaf(YType.str, 'lldpRemOrgDefInfo'), ['str'])),
                ])
                self.lldpremtimemark = None
                self.lldpremlocalportnum = None
                self.lldpremindex = None
                self.lldpremorgdefinfooui = None
                self.lldpremorgdefinfosubtype = None
                self.lldpremorgdefinfoindex = None
                self.lldpremorgdefinfo = None
                self._segment_path = lambda: "lldpRemOrgDefInfoEntry" + "[lldpRemTimeMark='" + str(self.lldpremtimemark) + "']" + "[lldpRemLocalPortNum='" + str(self.lldpremlocalportnum) + "']" + "[lldpRemIndex='" + str(self.lldpremindex) + "']" + "[lldpRemOrgDefInfoOUI='" + str(self.lldpremorgdefinfooui) + "']" + "[lldpRemOrgDefInfoSubtype='" + str(self.lldpremorgdefinfosubtype) + "']" + "[lldpRemOrgDefInfoIndex='" + str(self.lldpremorgdefinfoindex) + "']"
                self._absolute_path = lambda: "LLDP-MIB:LLDP-MIB/lldpRemOrgDefInfoTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(LLDPMIB.LldpRemOrgDefInfoTable.LldpRemOrgDefInfoEntry, ['lldpremtimemark', 'lldpremlocalportnum', 'lldpremindex', 'lldpremorgdefinfooui', 'lldpremorgdefinfosubtype', 'lldpremorgdefinfoindex', 'lldpremorgdefinfo'], name, value)



    def clone_ptr(self):
        self._top_entity = LLDPMIB()
        return self._top_entity




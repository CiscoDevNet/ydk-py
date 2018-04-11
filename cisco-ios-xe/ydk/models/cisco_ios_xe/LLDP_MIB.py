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
    
    	
    	**type**\:  :py:class:`Lldpconfiguration <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.Lldpconfiguration>`
    
    .. attribute:: lldpstatistics
    
    	
    	**type**\:  :py:class:`Lldpstatistics <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.Lldpstatistics>`
    
    .. attribute:: lldplocalsystemdata
    
    	
    	**type**\:  :py:class:`Lldplocalsystemdata <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.Lldplocalsystemdata>`
    
    .. attribute:: lldpportconfigtable
    
    	The table that controls LLDP frame transmission on individual ports
    	**type**\:  :py:class:`Lldpportconfigtable <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.Lldpportconfigtable>`
    
    .. attribute:: lldpstatstxporttable
    
    	A table containing LLDP transmission statistics for individual ports.  Entries are not required to exist in this table while the lldpPortConfigEntry object is equal to 'disabled(4)'
    	**type**\:  :py:class:`Lldpstatstxporttable <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.Lldpstatstxporttable>`
    
    .. attribute:: lldpstatsrxporttable
    
    	A table containing LLDP reception statistics for individual ports.  Entries are not required to exist in this table while the lldpPortConfigEntry object is equal to 'disabled(4)'
    	**type**\:  :py:class:`Lldpstatsrxporttable <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.Lldpstatsrxporttable>`
    
    .. attribute:: lldplocporttable
    
    	This table contains one or more rows per port information associated with the local system known to this agent
    	**type**\:  :py:class:`Lldplocporttable <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.Lldplocporttable>`
    
    .. attribute:: lldplocmanaddrtable
    
    	This table contains management address information on the local system known to this agent
    	**type**\:  :py:class:`Lldplocmanaddrtable <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.Lldplocmanaddrtable>`
    
    .. attribute:: lldpremtable
    
    	This table contains one or more rows per physical network connection known to this agent.  The agent may wish to ensure that only one lldpRemEntry is present for each local port, or it may choose to maintain multiple lldpRemEntries for the same local port.  The following procedure may be used to retrieve remote systems information updates from an LLDP agent\:     1. NMS polls all tables associated with remote systems       and keeps a local copy of the information retrieved.       NMS polls periodically the values of the following       objects\:          a. lldpStatsRemTablesInserts          b. lldpStatsRemTablesDeletes          c. lldpStatsRemTablesDrops          d. lldpStatsRemTablesAgeouts          e. lldpStatsRxPortAgeoutsTotal for all ports.     2. LLDP agent updates remote systems MIB objects, and       sends out notifications to a list of notification       destinations.     3. NMS receives the notifications and compares the new       values of objects listed in step 1.          Periodically, NMS should poll the object       lldpStatsRemTablesLastChangeTime to find out if anything       has changed since the last poll.  if something has       changed, NMS will poll the objects listed in step 1 to       figure out what kind of changes occurred in the tables.        if value of lldpStatsRemTablesInserts has changed,       then NMS will walk all tables by employing TimeFilter       with the last\-polled time value.  This request will       return new objects or objects whose values are updated       since the last poll.        if value of lldpStatsRemTablesAgeouts has changed,       then NMS will walk the lldpStatsRxPortAgeoutsTotal and       compare the new values with previously recorded ones.       For ports whose lldpStatsRxPortAgeoutsTotal value is       greater than the recorded value, NMS will have to       retrieve objects associated with those ports from       table(s) without employing a TimeFilter (which is       performed by specifying 0 for the TimeFilter.)        lldpStatsRemTablesDeletes and lldpStatsRemTablesDrops       objects are provided for informational purposes
    	**type**\:  :py:class:`Lldpremtable <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.Lldpremtable>`
    
    .. attribute:: lldpremmanaddrtable
    
    	This table contains one or more rows per management address information on the remote system learned on a particular port contained in the local chassis known to this agent
    	**type**\:  :py:class:`Lldpremmanaddrtable <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.Lldpremmanaddrtable>`
    
    .. attribute:: lldpremunknowntlvtable
    
    	This table contains information about an incoming TLV which is not recognized by the receiving LLDP agent.  The TLV may be from a later version of the basic management set.  This table should only contain TLVs that are found in a single LLDP frame.  Entries in this table, associated with an MAC service access point (MSAP, the access point for MAC services provided to the LCC sublayer, defined in IEEE 100, which is also identified with a particular lldpRemLocalPortNum, lldpRemIndex pair) are overwritten with most recently received unrecognized TLV from the same MSAP, or they will naturally age out when the rxInfoTTL timer (associated with the MSAP) expires
    	**type**\:  :py:class:`Lldpremunknowntlvtable <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.Lldpremunknowntlvtable>`
    
    .. attribute:: lldpremorgdefinfotable
    
    	This table contains one or more rows per physical network connection which advertises the organizationally defined information.  Note that this table contains one or more rows of organizationally defined information that is not recognized by the local agent.  If the local system is capable of recognizing any organizationally defined information, appropriate extension MIBs from the organization should be used for information retrieval
    	**type**\:  :py:class:`Lldpremorgdefinfotable <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.Lldpremorgdefinfotable>`
    
    

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
        self._child_container_classes = OrderedDict([("lldpConfiguration", ("lldpconfiguration", LLDPMIB.Lldpconfiguration)), ("lldpStatistics", ("lldpstatistics", LLDPMIB.Lldpstatistics)), ("lldpLocalSystemData", ("lldplocalsystemdata", LLDPMIB.Lldplocalsystemdata)), ("lldpPortConfigTable", ("lldpportconfigtable", LLDPMIB.Lldpportconfigtable)), ("lldpStatsTxPortTable", ("lldpstatstxporttable", LLDPMIB.Lldpstatstxporttable)), ("lldpStatsRxPortTable", ("lldpstatsrxporttable", LLDPMIB.Lldpstatsrxporttable)), ("lldpLocPortTable", ("lldplocporttable", LLDPMIB.Lldplocporttable)), ("lldpLocManAddrTable", ("lldplocmanaddrtable", LLDPMIB.Lldplocmanaddrtable)), ("lldpRemTable", ("lldpremtable", LLDPMIB.Lldpremtable)), ("lldpRemManAddrTable", ("lldpremmanaddrtable", LLDPMIB.Lldpremmanaddrtable)), ("lldpRemUnknownTLVTable", ("lldpremunknowntlvtable", LLDPMIB.Lldpremunknowntlvtable)), ("lldpRemOrgDefInfoTable", ("lldpremorgdefinfotable", LLDPMIB.Lldpremorgdefinfotable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.lldpconfiguration = LLDPMIB.Lldpconfiguration()
        self.lldpconfiguration.parent = self
        self._children_name_map["lldpconfiguration"] = "lldpConfiguration"
        self._children_yang_names.add("lldpConfiguration")

        self.lldpstatistics = LLDPMIB.Lldpstatistics()
        self.lldpstatistics.parent = self
        self._children_name_map["lldpstatistics"] = "lldpStatistics"
        self._children_yang_names.add("lldpStatistics")

        self.lldplocalsystemdata = LLDPMIB.Lldplocalsystemdata()
        self.lldplocalsystemdata.parent = self
        self._children_name_map["lldplocalsystemdata"] = "lldpLocalSystemData"
        self._children_yang_names.add("lldpLocalSystemData")

        self.lldpportconfigtable = LLDPMIB.Lldpportconfigtable()
        self.lldpportconfigtable.parent = self
        self._children_name_map["lldpportconfigtable"] = "lldpPortConfigTable"
        self._children_yang_names.add("lldpPortConfigTable")

        self.lldpstatstxporttable = LLDPMIB.Lldpstatstxporttable()
        self.lldpstatstxporttable.parent = self
        self._children_name_map["lldpstatstxporttable"] = "lldpStatsTxPortTable"
        self._children_yang_names.add("lldpStatsTxPortTable")

        self.lldpstatsrxporttable = LLDPMIB.Lldpstatsrxporttable()
        self.lldpstatsrxporttable.parent = self
        self._children_name_map["lldpstatsrxporttable"] = "lldpStatsRxPortTable"
        self._children_yang_names.add("lldpStatsRxPortTable")

        self.lldplocporttable = LLDPMIB.Lldplocporttable()
        self.lldplocporttable.parent = self
        self._children_name_map["lldplocporttable"] = "lldpLocPortTable"
        self._children_yang_names.add("lldpLocPortTable")

        self.lldplocmanaddrtable = LLDPMIB.Lldplocmanaddrtable()
        self.lldplocmanaddrtable.parent = self
        self._children_name_map["lldplocmanaddrtable"] = "lldpLocManAddrTable"
        self._children_yang_names.add("lldpLocManAddrTable")

        self.lldpremtable = LLDPMIB.Lldpremtable()
        self.lldpremtable.parent = self
        self._children_name_map["lldpremtable"] = "lldpRemTable"
        self._children_yang_names.add("lldpRemTable")

        self.lldpremmanaddrtable = LLDPMIB.Lldpremmanaddrtable()
        self.lldpremmanaddrtable.parent = self
        self._children_name_map["lldpremmanaddrtable"] = "lldpRemManAddrTable"
        self._children_yang_names.add("lldpRemManAddrTable")

        self.lldpremunknowntlvtable = LLDPMIB.Lldpremunknowntlvtable()
        self.lldpremunknowntlvtable.parent = self
        self._children_name_map["lldpremunknowntlvtable"] = "lldpRemUnknownTLVTable"
        self._children_yang_names.add("lldpRemUnknownTLVTable")

        self.lldpremorgdefinfotable = LLDPMIB.Lldpremorgdefinfotable()
        self.lldpremorgdefinfotable.parent = self
        self._children_name_map["lldpremorgdefinfotable"] = "lldpRemOrgDefInfoTable"
        self._children_yang_names.add("lldpRemOrgDefInfoTable")
        self._segment_path = lambda: "LLDP-MIB:LLDP-MIB"


    class Lldpconfiguration(Entity):
        """
        
        
        .. attribute:: lldpmessagetxinterval
        
        	The interval at which LLDP frames are transmitted on behalf of this LLDP agent.  The default value for lldpMessageTxInterval object is 30 seconds.  The value of this object must be restored from non\-volatile storage after a re\-initialization of the management system
        	**type**\: int
        
        	**range:** 5..32768
        
        	**units**\: seconds
        
        .. attribute:: lldpmessagetxholdmultiplier
        
        	The time\-to\-live value expressed as a multiple of the lldpMessageTxInterval object.  The actual time\-to\-live value used in LLDP frames, transmitted on behalf of this LLDP agent, can be expressed by the following formula\: TTL = min(65535, (lldpMessageTxInterval \* lldpMessageTxHoldMultiplier)) For example, if the value of lldpMessageTxInterval is '30', and the value of lldpMessageTxHoldMultiplier is '4', then the value '120' is encoded in the TTL field in the LLDP header.  The default value for lldpMessageTxHoldMultiplier object is 4.  The value of this object must be restored from non\-volatile storage after a re\-initialization of the management system
        	**type**\: int
        
        	**range:** 2..10
        
        .. attribute:: lldpreinitdelay
        
        	The lldpReinitDelay indicates the delay (in units of seconds) from when lldpPortConfigAdminStatus object of a particular port becomes 'disabled' until re\-initialization will be attempted.  The default value for lldpReintDelay object is two seconds.  The value of this object must be restored from non\-volatile storage after a re\-initialization of the management system
        	**type**\: int
        
        	**range:** 1..10
        
        	**units**\: seconds
        
        .. attribute:: lldptxdelay
        
        	The lldpTxDelay indicates the delay (in units of seconds) between successive LLDP frame transmissions  initiated by value/status changes in the LLDP local systems MIB.  The recommended value for the lldpTxDelay is set by the following  formula\:     1 <= lldpTxDelay <= (0.25 \* lldpMessageTxInterval)  The default value for lldpTxDelay object is two seconds.  The value of this object must be restored from non\-volatile storage after a re\-initialization of the management system
        	**type**\: int
        
        	**range:** 1..8192
        
        	**units**\: seconds
        
        .. attribute:: lldpnotificationinterval
        
        	This object controls the transmission of LLDP notifications.  the agent must not generate more than one lldpRemTablesChange notification\-event in the indicated period, where a 'notification\-event' is the transmission of a single notification PDU type to a list of notification destinations. If additional changes in lldpRemoteSystemsData object groups occur within the indicated throttling period, then these trap\- events must be suppressed by the agent. An NMS should periodically check the value of lldpStatsRemTableLastChangeTime to detect any missed lldpRemTablesChange notification\-events, e.g. due to throttling or transmission loss.  If notification transmission is enabled for particular ports, the suggested default throttling period is 5 seconds.  The value of this object must be restored from non\-volatile storage after a re\-initialization of the management system
        	**type**\: int
        
        	**range:** 5..3600
        
        	**units**\: seconds
        
        

        """

        _prefix = 'LLDP-MIB'
        _revision = '2005-05-06'

        def __init__(self):
            super(LLDPMIB.Lldpconfiguration, self).__init__()

            self.yang_name = "lldpConfiguration"
            self.yang_parent_name = "LLDP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('lldpmessagetxinterval', YLeaf(YType.int32, 'lldpMessageTxInterval')),
                ('lldpmessagetxholdmultiplier', YLeaf(YType.int32, 'lldpMessageTxHoldMultiplier')),
                ('lldpreinitdelay', YLeaf(YType.int32, 'lldpReinitDelay')),
                ('lldptxdelay', YLeaf(YType.int32, 'lldpTxDelay')),
                ('lldpnotificationinterval', YLeaf(YType.int32, 'lldpNotificationInterval')),
            ])
            self.lldpmessagetxinterval = None
            self.lldpmessagetxholdmultiplier = None
            self.lldpreinitdelay = None
            self.lldptxdelay = None
            self.lldpnotificationinterval = None
            self._segment_path = lambda: "lldpConfiguration"
            self._absolute_path = lambda: "LLDP-MIB:LLDP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(LLDPMIB.Lldpconfiguration, ['lldpmessagetxinterval', 'lldpmessagetxholdmultiplier', 'lldpreinitdelay', 'lldptxdelay', 'lldpnotificationinterval'], name, value)


    class Lldpstatistics(Entity):
        """
        
        
        .. attribute:: lldpstatsremtableslastchangetime
        
        	The value of sysUpTime object (defined in IETF RFC 3418) at the time an entry is created, modified, or deleted in the in tables associated with the lldpRemoteSystemsData objects and all LLDP extension objects associated with remote systems.  An NMS can use this object to reduce polling of the lldpRemoteSystemsData objects
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: lldpstatsremtablesinserts
        
        	The number of times the complete set of information advertised by a particular MSAP has been inserted into tables contained in lldpRemoteSystemsData and lldpExtensions objects.  The complete set of information received from a particular MSAP should be inserted into related tables.  If partial information cannot be inserted for a reason such as lack of resources, all of the complete set of information should be removed.  This counter should be incremented only once after the complete set of information is successfully recorded in all related tables.  Any failures during inserting information set which result in deletion of previously inserted information should not trigger any changes in lldpStatsRemTablesInserts since the insert is not completed yet or or in lldpStatsRemTablesDeletes, since the deletion would only be a partial deletion. If the failure was the result of lack of resources, the lldpStatsRemTablesDrops counter should be incremented once
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: table entries
        
        .. attribute:: lldpstatsremtablesdeletes
        
        	The number of times the complete set of information advertised by a particular MSAP has been deleted from tables contained in lldpRemoteSystemsData and lldpExtensions objects.  This counter should be incremented only once when the complete set of information is completely deleted from all related tables.  Partial deletions, such as deletion of rows associated with a particular MSAP from some tables, but not from all tables are not allowed, thus should not change the value of this counter
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: table entries
        
        .. attribute:: lldpstatsremtablesdrops
        
        	The number of times the complete set of information advertised by a particular MSAP could not be entered into tables contained in lldpRemoteSystemsData and lldpExtensions objects because of insufficient resources
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: table entries
        
        .. attribute:: lldpstatsremtablesageouts
        
        	The number of times the complete set of information advertised by a particular MSAP has been deleted from tables contained in lldpRemoteSystemsData and lldpExtensions objects because the information timeliness interval has expired.  This counter should be incremented only once when the complete set of information is completely invalidated (aged out) from all related tables.  Partial aging, similar to deletion case, is not allowed, and thus, should not change the value of this counter
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'LLDP-MIB'
        _revision = '2005-05-06'

        def __init__(self):
            super(LLDPMIB.Lldpstatistics, self).__init__()

            self.yang_name = "lldpStatistics"
            self.yang_parent_name = "LLDP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('lldpstatsremtableslastchangetime', YLeaf(YType.uint32, 'lldpStatsRemTablesLastChangeTime')),
                ('lldpstatsremtablesinserts', YLeaf(YType.uint32, 'lldpStatsRemTablesInserts')),
                ('lldpstatsremtablesdeletes', YLeaf(YType.uint32, 'lldpStatsRemTablesDeletes')),
                ('lldpstatsremtablesdrops', YLeaf(YType.uint32, 'lldpStatsRemTablesDrops')),
                ('lldpstatsremtablesageouts', YLeaf(YType.uint32, 'lldpStatsRemTablesAgeouts')),
            ])
            self.lldpstatsremtableslastchangetime = None
            self.lldpstatsremtablesinserts = None
            self.lldpstatsremtablesdeletes = None
            self.lldpstatsremtablesdrops = None
            self.lldpstatsremtablesageouts = None
            self._segment_path = lambda: "lldpStatistics"
            self._absolute_path = lambda: "LLDP-MIB:LLDP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(LLDPMIB.Lldpstatistics, ['lldpstatsremtableslastchangetime', 'lldpstatsremtablesinserts', 'lldpstatsremtablesdeletes', 'lldpstatsremtablesdrops', 'lldpstatsremtablesageouts'], name, value)


    class Lldplocalsystemdata(Entity):
        """
        
        
        .. attribute:: lldplocchassisidsubtype
        
        	The type of encoding used to identify the chassis associated with the local system
        	**type**\:  :py:class:`LldpChassisIdSubtype <ydk.models.cisco_ios_xe.LLDP_MIB.LldpChassisIdSubtype>`
        
        .. attribute:: lldplocchassisid
        
        	The string value used to identify the chassis component associated with the local system
        	**type**\: str
        
        	**length:** 1..255
        
        .. attribute:: lldplocsysname
        
        	The string value used to identify the system name of the local system.  If the local agent supports IETF RFC 3418, lldpLocSysName object should have the same value of sysName object
        	**type**\: str
        
        	**length:** 0..255
        
        .. attribute:: lldplocsysdesc
        
        	The string value used to identify the system description of the local system.  If the local agent supports IETF RFC 3418, lldpLocSysDesc object should have the same value of sysDesc object
        	**type**\: str
        
        	**length:** 0..255
        
        .. attribute:: lldplocsyscapsupported
        
        	The bitmap value used to identify which system capabilities are supported on the local system
        	**type**\:  :py:class:`LldpSystemCapabilitiesMap <ydk.models.cisco_ios_xe.LLDP_MIB.LldpSystemCapabilitiesMap>`
        
        .. attribute:: lldplocsyscapenabled
        
        	The bitmap value used to identify which system capabilities are enabled on the local system
        	**type**\:  :py:class:`LldpSystemCapabilitiesMap <ydk.models.cisco_ios_xe.LLDP_MIB.LldpSystemCapabilitiesMap>`
        
        

        """

        _prefix = 'LLDP-MIB'
        _revision = '2005-05-06'

        def __init__(self):
            super(LLDPMIB.Lldplocalsystemdata, self).__init__()

            self.yang_name = "lldpLocalSystemData"
            self.yang_parent_name = "LLDP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('lldplocchassisidsubtype', YLeaf(YType.enumeration, 'lldpLocChassisIdSubtype')),
                ('lldplocchassisid', YLeaf(YType.str, 'lldpLocChassisId')),
                ('lldplocsysname', YLeaf(YType.str, 'lldpLocSysName')),
                ('lldplocsysdesc', YLeaf(YType.str, 'lldpLocSysDesc')),
                ('lldplocsyscapsupported', YLeaf(YType.bits, 'lldpLocSysCapSupported')),
                ('lldplocsyscapenabled', YLeaf(YType.bits, 'lldpLocSysCapEnabled')),
            ])
            self.lldplocchassisidsubtype = None
            self.lldplocchassisid = None
            self.lldplocsysname = None
            self.lldplocsysdesc = None
            self.lldplocsyscapsupported = Bits()
            self.lldplocsyscapenabled = Bits()
            self._segment_path = lambda: "lldpLocalSystemData"
            self._absolute_path = lambda: "LLDP-MIB:LLDP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(LLDPMIB.Lldplocalsystemdata, ['lldplocchassisidsubtype', 'lldplocchassisid', 'lldplocsysname', 'lldplocsysdesc', 'lldplocsyscapsupported', 'lldplocsyscapenabled'], name, value)


    class Lldpportconfigtable(Entity):
        """
        The table that controls LLDP frame transmission on individual
        ports.
        
        .. attribute:: lldpportconfigentry
        
        	LLDP configuration information for a particular port. This configuration parameter controls the transmission and the reception of LLDP frames on those ports whose rows are created in this table
        	**type**\: list of  		 :py:class:`Lldpportconfigentry <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.Lldpportconfigtable.Lldpportconfigentry>`
        
        

        """

        _prefix = 'LLDP-MIB'
        _revision = '2005-05-06'

        def __init__(self):
            super(LLDPMIB.Lldpportconfigtable, self).__init__()

            self.yang_name = "lldpPortConfigTable"
            self.yang_parent_name = "LLDP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("lldpPortConfigEntry", ("lldpportconfigentry", LLDPMIB.Lldpportconfigtable.Lldpportconfigentry))])
            self._leafs = OrderedDict()

            self.lldpportconfigentry = YList(self)
            self._segment_path = lambda: "lldpPortConfigTable"
            self._absolute_path = lambda: "LLDP-MIB:LLDP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(LLDPMIB.Lldpportconfigtable, [], name, value)


        class Lldpportconfigentry(Entity):
            """
            LLDP configuration information for a particular port.
            This configuration parameter controls the transmission and
            the reception of LLDP frames on those ports whose rows are
            created in this table.
            
            .. attribute:: lldpportconfigportnum  (key)
            
            	The index value used to identify the port component (contained in the local chassis with the LLDP agent) associated with this entry.  The value of this object is used as a port index to the lldpPortConfigTable
            	**type**\: int
            
            	**range:** 1..4096
            
            .. attribute:: lldpportconfigadminstatus
            
            	The administratively desired status of the local LLDP agent.  If the associated lldpPortConfigAdminStatus object has a value of 'txOnly(1)', then LLDP agent will transmit LLDP frames on this port and it will not store any information about the remote systems connected.  If the associated lldpPortConfigAdminStatus object has a value of 'rxOnly(2)', then the LLDP agent will receive, but it will not transmit LLDP frames on this port.  If the associated lldpPortConfigAdminStatus object has a value of 'txAndRx(3)', then the LLDP agent will transmit and receive LLDP frames on this port.  If the associated lldpPortConfigAdminStatus object has a value of 'disabled(4)', then LLDP agent will not transmit or receive LLDP frames on this port.  If there is remote systems information which is received on this port and stored in other tables, before the port's lldpPortConfigAdminStatus becomes disabled, then the information will naturally age out
            	**type**\:  :py:class:`Lldpportconfigadminstatus <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.Lldpportconfigtable.Lldpportconfigentry.Lldpportconfigadminstatus>`
            
            .. attribute:: lldpportconfignotificationenable
            
            	The lldpPortConfigNotificationEnable controls, on a per port basis,  whether or not notifications from the agent are enabled. The value true(1) means that notifications are enabled; the value false(2) means that they are not
            	**type**\: bool
            
            .. attribute:: lldpportconfigtlvstxenable
            
            	The lldpPortConfigTLVsTxEnable, defined as a bitmap, includes the basic set of LLDP TLVs whose transmission is allowed on the local LLDP agent by the network management. Each bit in the bitmap corresponds to a TLV type associated with a specific optional TLV.  It should be noted that the organizationally\-specific TLVs are excluded from the lldpTLVsTxEnable bitmap.  LLDP Organization Specific Information Extension MIBs should have similar configuration object to control transmission of their organizationally defined TLVs.  The bit 'portDesc(0)' indicates that LLDP agent should transmit 'Port Description TLV'.  The bit 'sysName(1)' indicates that LLDP agent should transmit 'System Name TLV'.  The bit 'sysDesc(2)' indicates that LLDP agent should transmit 'System Description TLV'.  The bit 'sysCap(3)' indicates that LLDP agent should transmit 'System Capabilities TLV'.  There is no bit reserved for the management address TLV type since transmission of management address TLVs are controlled by another object, lldpConfigManAddrTable.  The default value for lldpPortConfigTLVsTxEnable object is empty set, which means no enumerated values are set.  The value of this object must be restored from non\-volatile storage after a re\-initialization of the management system
            	**type**\:  :py:class:`Lldpportconfigtlvstxenable <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.Lldpportconfigtable.Lldpportconfigentry.Lldpportconfigtlvstxenable>`
            
            

            """

            _prefix = 'LLDP-MIB'
            _revision = '2005-05-06'

            def __init__(self):
                super(LLDPMIB.Lldpportconfigtable.Lldpportconfigentry, self).__init__()

                self.yang_name = "lldpPortConfigEntry"
                self.yang_parent_name = "lldpPortConfigTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['lldpportconfigportnum']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('lldpportconfigportnum', YLeaf(YType.int32, 'lldpPortConfigPortNum')),
                    ('lldpportconfigadminstatus', YLeaf(YType.enumeration, 'lldpPortConfigAdminStatus')),
                    ('lldpportconfignotificationenable', YLeaf(YType.boolean, 'lldpPortConfigNotificationEnable')),
                    ('lldpportconfigtlvstxenable', YLeaf(YType.bits, 'lldpPortConfigTLVsTxEnable')),
                ])
                self.lldpportconfigportnum = None
                self.lldpportconfigadminstatus = None
                self.lldpportconfignotificationenable = None
                self.lldpportconfigtlvstxenable = Bits()
                self._segment_path = lambda: "lldpPortConfigEntry" + "[lldpPortConfigPortNum='" + str(self.lldpportconfigportnum) + "']"
                self._absolute_path = lambda: "LLDP-MIB:LLDP-MIB/lldpPortConfigTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(LLDPMIB.Lldpportconfigtable.Lldpportconfigentry, ['lldpportconfigportnum', 'lldpportconfigadminstatus', 'lldpportconfignotificationenable', 'lldpportconfigtlvstxenable'], name, value)

            class Lldpportconfigadminstatus(Enum):
                """
                Lldpportconfigadminstatus (Enum Class)

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



    class Lldpstatstxporttable(Entity):
        """
        A table containing LLDP transmission statistics for
        individual ports.  Entries are not required to exist in
        this table while the lldpPortConfigEntry object is equal to
        'disabled(4)'.
        
        .. attribute:: lldpstatstxportentry
        
        	LLDP frame transmission statistics for a particular port. The port must be contained in the same chassis as the LLDP agent.  All counter values in a particular entry shall be maintained on a continuing basis and shall not be deleted upon expiration of rxInfoTTL timing counters in the LLDP remote systems MIB of the receipt of a shutdown frame from a remote LLDP agent.  All statistical counters associated with a particular port on the local LLDP agent become frozen whenever the adminStatus is disabled for the same port
        	**type**\: list of  		 :py:class:`Lldpstatstxportentry <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.Lldpstatstxporttable.Lldpstatstxportentry>`
        
        

        """

        _prefix = 'LLDP-MIB'
        _revision = '2005-05-06'

        def __init__(self):
            super(LLDPMIB.Lldpstatstxporttable, self).__init__()

            self.yang_name = "lldpStatsTxPortTable"
            self.yang_parent_name = "LLDP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("lldpStatsTxPortEntry", ("lldpstatstxportentry", LLDPMIB.Lldpstatstxporttable.Lldpstatstxportentry))])
            self._leafs = OrderedDict()

            self.lldpstatstxportentry = YList(self)
            self._segment_path = lambda: "lldpStatsTxPortTable"
            self._absolute_path = lambda: "LLDP-MIB:LLDP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(LLDPMIB.Lldpstatstxporttable, [], name, value)


        class Lldpstatstxportentry(Entity):
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
            
            .. attribute:: lldpstatstxportframestotal
            
            	The number of LLDP frames transmitted by this LLDP agent on the indicated port
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'LLDP-MIB'
            _revision = '2005-05-06'

            def __init__(self):
                super(LLDPMIB.Lldpstatstxporttable.Lldpstatstxportentry, self).__init__()

                self.yang_name = "lldpStatsTxPortEntry"
                self.yang_parent_name = "lldpStatsTxPortTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['lldpstatstxportnum']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('lldpstatstxportnum', YLeaf(YType.int32, 'lldpStatsTxPortNum')),
                    ('lldpstatstxportframestotal', YLeaf(YType.uint32, 'lldpStatsTxPortFramesTotal')),
                ])
                self.lldpstatstxportnum = None
                self.lldpstatstxportframestotal = None
                self._segment_path = lambda: "lldpStatsTxPortEntry" + "[lldpStatsTxPortNum='" + str(self.lldpstatstxportnum) + "']"
                self._absolute_path = lambda: "LLDP-MIB:LLDP-MIB/lldpStatsTxPortTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(LLDPMIB.Lldpstatstxporttable.Lldpstatstxportentry, ['lldpstatstxportnum', 'lldpstatstxportframestotal'], name, value)


    class Lldpstatsrxporttable(Entity):
        """
        A table containing LLDP reception statistics for individual
        ports.  Entries are not required to exist in this table while
        the lldpPortConfigEntry object is equal to 'disabled(4)'.
        
        .. attribute:: lldpstatsrxportentry
        
        	LLDP frame reception statistics for a particular port. The port must be contained in the same chassis as the LLDP agent.  All counter values in a particular entry shall be maintained on a continuing basis and shall not be deleted upon expiration of rxInfoTTL timing counters in the LLDP remote systems MIB of the receipt of a shutdown frame from a remote LLDP agent.  All statistical counters associated with a particular port on the local LLDP agent become frozen whenever the adminStatus is disabled for the same port
        	**type**\: list of  		 :py:class:`Lldpstatsrxportentry <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.Lldpstatsrxporttable.Lldpstatsrxportentry>`
        
        

        """

        _prefix = 'LLDP-MIB'
        _revision = '2005-05-06'

        def __init__(self):
            super(LLDPMIB.Lldpstatsrxporttable, self).__init__()

            self.yang_name = "lldpStatsRxPortTable"
            self.yang_parent_name = "LLDP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("lldpStatsRxPortEntry", ("lldpstatsrxportentry", LLDPMIB.Lldpstatsrxporttable.Lldpstatsrxportentry))])
            self._leafs = OrderedDict()

            self.lldpstatsrxportentry = YList(self)
            self._segment_path = lambda: "lldpStatsRxPortTable"
            self._absolute_path = lambda: "LLDP-MIB:LLDP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(LLDPMIB.Lldpstatsrxporttable, [], name, value)


        class Lldpstatsrxportentry(Entity):
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
            
            .. attribute:: lldpstatsrxportframesdiscardedtotal
            
            	The number of LLDP frames received by this LLDP agent on the indicated port, and then discarded for any reason. This counter can provide an indication that LLDP header formating problems may exist with the local LLDP agent in the sending system or that LLDPDU validation problems may exist with the local LLDP agent in the receiving system
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: lldpstatsrxportframeserrors
            
            	The number of invalid LLDP frames received by this LLDP agent on the indicated port, while this LLDP agent is enabled
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: lldpstatsrxportframestotal
            
            	The number of valid LLDP frames received by this LLDP agent on the indicated port, while this LLDP agent is enabled
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: lldpstatsrxporttlvsdiscardedtotal
            
            	The number of LLDP TLVs discarded for any reason by this LLDP agent on the indicated port
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: lldpstatsrxporttlvsunrecognizedtotal
            
            	The number of LLDP TLVs received on the given port that are not recognized by this LLDP agent on the indicated port.  An unrecognized TLV is referred to as the TLV whose type value is in the range of reserved TLV types (000 1001 \- 111 1110) in Table 9.1 of IEEE Std 802.1AB\-2005.  An unrecognized TLV may be a basic management TLV from a later LLDP version
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: lldpstatsrxportageoutstotal
            
            	The counter that represents the number of age\-outs that occurred on a given port.  An age\-out is the number of times the complete set of information advertised by a particular MSAP has been deleted from tables contained in lldpRemoteSystemsData and lldpExtensions objects because the information timeliness interval has expired.  This counter is similar to lldpStatsRemTablesAgeouts, except that the counter is on a per port basis.  This enables NMS to poll tables associated with the lldpRemoteSystemsData objects and all LLDP extension objects associated with remote systems on the indicated port only.  This counter should be set to zero during agent initialization and its value should not be saved in non\-volatile storage. When a port's admin status changes from 'disabled' to 'rxOnly', 'txOnly' or 'txAndRx', the counter associated with the same port should reset to 0.  The agent should also flush all remote system information associated with the same port.  This counter should be incremented only once when the complete set of information is invalidated (aged out) from all related tables on a particular port.  Partial aging is not allowed, and thus, should not change the value of this counter
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'LLDP-MIB'
            _revision = '2005-05-06'

            def __init__(self):
                super(LLDPMIB.Lldpstatsrxporttable.Lldpstatsrxportentry, self).__init__()

                self.yang_name = "lldpStatsRxPortEntry"
                self.yang_parent_name = "lldpStatsRxPortTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['lldpstatsrxportnum']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('lldpstatsrxportnum', YLeaf(YType.int32, 'lldpStatsRxPortNum')),
                    ('lldpstatsrxportframesdiscardedtotal', YLeaf(YType.uint32, 'lldpStatsRxPortFramesDiscardedTotal')),
                    ('lldpstatsrxportframeserrors', YLeaf(YType.uint32, 'lldpStatsRxPortFramesErrors')),
                    ('lldpstatsrxportframestotal', YLeaf(YType.uint32, 'lldpStatsRxPortFramesTotal')),
                    ('lldpstatsrxporttlvsdiscardedtotal', YLeaf(YType.uint32, 'lldpStatsRxPortTLVsDiscardedTotal')),
                    ('lldpstatsrxporttlvsunrecognizedtotal', YLeaf(YType.uint32, 'lldpStatsRxPortTLVsUnrecognizedTotal')),
                    ('lldpstatsrxportageoutstotal', YLeaf(YType.uint32, 'lldpStatsRxPortAgeoutsTotal')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(LLDPMIB.Lldpstatsrxporttable.Lldpstatsrxportentry, ['lldpstatsrxportnum', 'lldpstatsrxportframesdiscardedtotal', 'lldpstatsrxportframeserrors', 'lldpstatsrxportframestotal', 'lldpstatsrxporttlvsdiscardedtotal', 'lldpstatsrxporttlvsunrecognizedtotal', 'lldpstatsrxportageoutstotal'], name, value)


    class Lldplocporttable(Entity):
        """
        This table contains one or more rows per port information
        associated with the local system known to this agent.
        
        .. attribute:: lldplocportentry
        
        	Information about a particular port component.  Entries may be created and deleted in this table by the agent
        	**type**\: list of  		 :py:class:`Lldplocportentry <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.Lldplocporttable.Lldplocportentry>`
        
        

        """

        _prefix = 'LLDP-MIB'
        _revision = '2005-05-06'

        def __init__(self):
            super(LLDPMIB.Lldplocporttable, self).__init__()

            self.yang_name = "lldpLocPortTable"
            self.yang_parent_name = "LLDP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("lldpLocPortEntry", ("lldplocportentry", LLDPMIB.Lldplocporttable.Lldplocportentry))])
            self._leafs = OrderedDict()

            self.lldplocportentry = YList(self)
            self._segment_path = lambda: "lldpLocPortTable"
            self._absolute_path = lambda: "LLDP-MIB:LLDP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(LLDPMIB.Lldplocporttable, [], name, value)


        class Lldplocportentry(Entity):
            """
            Information about a particular port component.
            
            Entries may be created and deleted in this table by the
            agent.
            
            .. attribute:: lldplocportnum  (key)
            
            	The index value used to identify the port component (contained in the local chassis with the LLDP agent) associated with this entry.  The value of this object is used as a port index to the lldpLocPortTable
            	**type**\: int
            
            	**range:** 1..4096
            
            .. attribute:: lldplocportidsubtype
            
            	The type of port identifier encoding used in the associated 'lldpLocPortId' object
            	**type**\:  :py:class:`LldpPortIdSubtype <ydk.models.cisco_ios_xe.LLDP_MIB.LldpPortIdSubtype>`
            
            .. attribute:: lldplocportid
            
            	The string value used to identify the port component associated with a given port in the local system
            	**type**\: str
            
            	**length:** 1..255
            
            .. attribute:: lldplocportdesc
            
            	The string value used to identify the 802 LAN station's port description associated with the local system.  If the local agent supports IETF RFC 2863, lldpLocPortDesc object should have the same value of ifDescr object
            	**type**\: str
            
            	**length:** 0..255
            
            

            """

            _prefix = 'LLDP-MIB'
            _revision = '2005-05-06'

            def __init__(self):
                super(LLDPMIB.Lldplocporttable.Lldplocportentry, self).__init__()

                self.yang_name = "lldpLocPortEntry"
                self.yang_parent_name = "lldpLocPortTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['lldplocportnum']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('lldplocportnum', YLeaf(YType.int32, 'lldpLocPortNum')),
                    ('lldplocportidsubtype', YLeaf(YType.enumeration, 'lldpLocPortIdSubtype')),
                    ('lldplocportid', YLeaf(YType.str, 'lldpLocPortId')),
                    ('lldplocportdesc', YLeaf(YType.str, 'lldpLocPortDesc')),
                ])
                self.lldplocportnum = None
                self.lldplocportidsubtype = None
                self.lldplocportid = None
                self.lldplocportdesc = None
                self._segment_path = lambda: "lldpLocPortEntry" + "[lldpLocPortNum='" + str(self.lldplocportnum) + "']"
                self._absolute_path = lambda: "LLDP-MIB:LLDP-MIB/lldpLocPortTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(LLDPMIB.Lldplocporttable.Lldplocportentry, ['lldplocportnum', 'lldplocportidsubtype', 'lldplocportid', 'lldplocportdesc'], name, value)


    class Lldplocmanaddrtable(Entity):
        """
        This table contains management address information on the
        local system known to this agent.
        
        .. attribute:: lldplocmanaddrentry
        
        	Management address information about a particular chassis component.  There may be multiple management addresses configured on the system identified by a particular lldpLocChassisId.  Each management address should have distinct 'management address type' (lldpLocManAddrSubtype) and 'management address' (lldpLocManAddr.)  Entries may be created and deleted in this table by the agent
        	**type**\: list of  		 :py:class:`Lldplocmanaddrentry <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.Lldplocmanaddrtable.Lldplocmanaddrentry>`
        
        

        """

        _prefix = 'LLDP-MIB'
        _revision = '2005-05-06'

        def __init__(self):
            super(LLDPMIB.Lldplocmanaddrtable, self).__init__()

            self.yang_name = "lldpLocManAddrTable"
            self.yang_parent_name = "LLDP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("lldpLocManAddrEntry", ("lldplocmanaddrentry", LLDPMIB.Lldplocmanaddrtable.Lldplocmanaddrentry))])
            self._leafs = OrderedDict()

            self.lldplocmanaddrentry = YList(self)
            self._segment_path = lambda: "lldpLocManAddrTable"
            self._absolute_path = lambda: "LLDP-MIB:LLDP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(LLDPMIB.Lldplocmanaddrtable, [], name, value)


        class Lldplocmanaddrentry(Entity):
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
            
            .. attribute:: lldplocmanaddr  (key)
            
            	The string value used to identify the management address component associated with the local system.  The purpose of this address is to contact the management entity
            	**type**\: str
            
            	**length:** 1..31
            
            .. attribute:: lldplocmanaddrlen
            
            	The total length of the management address subtype and the management address fields in LLDPDUs transmitted by the local LLDP agent.  The management address length field is needed so that the receiving systems that do not implement SNMP will not be required to implement an iana family numbers/address length equivalency table in order to decode the management adress
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: lldplocmanaddrifsubtype
            
            	The enumeration value that identifies the interface numbering method used for defining the interface number, associated with the local system
            	**type**\:  :py:class:`LldpManAddrIfSubtype <ydk.models.cisco_ios_xe.LLDP_MIB.LldpManAddrIfSubtype>`
            
            .. attribute:: lldplocmanaddrifid
            
            	The integer value used to identify the interface number regarding the management address component associated with the local system
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: lldplocmanaddroid
            
            	The OID value used to identify the type of hardware component or protocol entity associated with the management address advertised by the local system agent
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: lldpconfigmanaddrportstxenable
            
            	A set of ports that are identified by a PortList, in which each port is represented as a bit.  The corresponding local system management address instance will be transmitted on the member ports of the lldpManAddrPortsTxEnable.    The default value for lldpConfigManAddrPortsTxEnable object is empty binary string, which means no ports are specified for advertising indicated management address instance
            	**type**\: str
            
            	**length:** 0..512
            
            

            """

            _prefix = 'LLDP-MIB'
            _revision = '2005-05-06'

            def __init__(self):
                super(LLDPMIB.Lldplocmanaddrtable.Lldplocmanaddrentry, self).__init__()

                self.yang_name = "lldpLocManAddrEntry"
                self.yang_parent_name = "lldpLocManAddrTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['lldplocmanaddrsubtype','lldplocmanaddr']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('lldplocmanaddrsubtype', YLeaf(YType.enumeration, 'lldpLocManAddrSubtype')),
                    ('lldplocmanaddr', YLeaf(YType.str, 'lldpLocManAddr')),
                    ('lldplocmanaddrlen', YLeaf(YType.int32, 'lldpLocManAddrLen')),
                    ('lldplocmanaddrifsubtype', YLeaf(YType.enumeration, 'lldpLocManAddrIfSubtype')),
                    ('lldplocmanaddrifid', YLeaf(YType.int32, 'lldpLocManAddrIfId')),
                    ('lldplocmanaddroid', YLeaf(YType.str, 'lldpLocManAddrOID')),
                    ('lldpconfigmanaddrportstxenable', YLeaf(YType.str, 'lldpConfigManAddrPortsTxEnable')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(LLDPMIB.Lldplocmanaddrtable.Lldplocmanaddrentry, ['lldplocmanaddrsubtype', 'lldplocmanaddr', 'lldplocmanaddrlen', 'lldplocmanaddrifsubtype', 'lldplocmanaddrifid', 'lldplocmanaddroid', 'lldpconfigmanaddrportstxenable'], name, value)


    class Lldpremtable(Entity):
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
        	**type**\: list of  		 :py:class:`Lldprementry <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.Lldpremtable.Lldprementry>`
        
        

        """

        _prefix = 'LLDP-MIB'
        _revision = '2005-05-06'

        def __init__(self):
            super(LLDPMIB.Lldpremtable, self).__init__()

            self.yang_name = "lldpRemTable"
            self.yang_parent_name = "LLDP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("lldpRemEntry", ("lldprementry", LLDPMIB.Lldpremtable.Lldprementry))])
            self._leafs = OrderedDict()

            self.lldprementry = YList(self)
            self._segment_path = lambda: "lldpRemTable"
            self._absolute_path = lambda: "LLDP-MIB:LLDP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(LLDPMIB.Lldpremtable, [], name, value)


        class Lldprementry(Entity):
            """
            Information about a particular physical network connection.
            Entries may be created and deleted in this table by the agent,
            if a physical topology discovery process is active.
            
            .. attribute:: lldpremtimemark  (key)
            
            	A TimeFilter for this entry.  See the TimeFilter textual convention in IETF RFC 2021 and  http\://www.ietf.org/IESG/Implementations/RFC2021\-Implementation.txt to see how TimeFilter works
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: lldpremlocalportnum  (key)
            
            	The index value used to identify the port component (contained in the local chassis with the LLDP agent) associated with this entry.  The lldpRemLocalPortNum identifies the port on which the remote system information is received.  The value of this object is used as a port index to the lldpRemTable
            	**type**\: int
            
            	**range:** 1..4096
            
            .. attribute:: lldpremindex  (key)
            
            	This object represents an arbitrary local integer value used by this agent to identify a particular connection instance, unique only for the indicated remote system.  An agent is encouraged to assign monotonically increasing index values to new entries, starting with one, after each reboot.  It is considered unlikely that the lldpRemIndex will wrap between reboots
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: lldpremchassisidsubtype
            
            	The type of encoding used to identify the chassis associated with the remote system
            	**type**\:  :py:class:`LldpChassisIdSubtype <ydk.models.cisco_ios_xe.LLDP_MIB.LldpChassisIdSubtype>`
            
            .. attribute:: lldpremchassisid
            
            	The string value used to identify the chassis component associated with the remote system
            	**type**\: str
            
            	**length:** 1..255
            
            .. attribute:: lldpremportidsubtype
            
            	The type of port identifier encoding used in the associated 'lldpRemPortId' object
            	**type**\:  :py:class:`LldpPortIdSubtype <ydk.models.cisco_ios_xe.LLDP_MIB.LldpPortIdSubtype>`
            
            .. attribute:: lldpremportid
            
            	The string value used to identify the port component associated with the remote system
            	**type**\: str
            
            	**length:** 1..255
            
            .. attribute:: lldpremportdesc
            
            	The string value used to identify the description of the given port associated with the remote system
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: lldpremsysname
            
            	The string value used to identify the system name of the remote system
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: lldpremsysdesc
            
            	The string value used to identify the system description of the remote system
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: lldpremsyscapsupported
            
            	The bitmap value used to identify which system capabilities are supported on the remote system
            	**type**\:  :py:class:`LldpSystemCapabilitiesMap <ydk.models.cisco_ios_xe.LLDP_MIB.LldpSystemCapabilitiesMap>`
            
            .. attribute:: lldpremsyscapenabled
            
            	The bitmap value used to identify which system capabilities are enabled on the remote system
            	**type**\:  :py:class:`LldpSystemCapabilitiesMap <ydk.models.cisco_ios_xe.LLDP_MIB.LldpSystemCapabilitiesMap>`
            
            

            """

            _prefix = 'LLDP-MIB'
            _revision = '2005-05-06'

            def __init__(self):
                super(LLDPMIB.Lldpremtable.Lldprementry, self).__init__()

                self.yang_name = "lldpRemEntry"
                self.yang_parent_name = "lldpRemTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['lldpremtimemark','lldpremlocalportnum','lldpremindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('lldpremtimemark', YLeaf(YType.uint32, 'lldpRemTimeMark')),
                    ('lldpremlocalportnum', YLeaf(YType.int32, 'lldpRemLocalPortNum')),
                    ('lldpremindex', YLeaf(YType.int32, 'lldpRemIndex')),
                    ('lldpremchassisidsubtype', YLeaf(YType.enumeration, 'lldpRemChassisIdSubtype')),
                    ('lldpremchassisid', YLeaf(YType.str, 'lldpRemChassisId')),
                    ('lldpremportidsubtype', YLeaf(YType.enumeration, 'lldpRemPortIdSubtype')),
                    ('lldpremportid', YLeaf(YType.str, 'lldpRemPortId')),
                    ('lldpremportdesc', YLeaf(YType.str, 'lldpRemPortDesc')),
                    ('lldpremsysname', YLeaf(YType.str, 'lldpRemSysName')),
                    ('lldpremsysdesc', YLeaf(YType.str, 'lldpRemSysDesc')),
                    ('lldpremsyscapsupported', YLeaf(YType.bits, 'lldpRemSysCapSupported')),
                    ('lldpremsyscapenabled', YLeaf(YType.bits, 'lldpRemSysCapEnabled')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(LLDPMIB.Lldpremtable.Lldprementry, ['lldpremtimemark', 'lldpremlocalportnum', 'lldpremindex', 'lldpremchassisidsubtype', 'lldpremchassisid', 'lldpremportidsubtype', 'lldpremportid', 'lldpremportdesc', 'lldpremsysname', 'lldpremsysdesc', 'lldpremsyscapsupported', 'lldpremsyscapenabled'], name, value)


    class Lldpremmanaddrtable(Entity):
        """
        This table contains one or more rows per management address
        information on the remote system learned on a particular port
        contained in the local chassis known to this agent.
        
        .. attribute:: lldpremmanaddrentry
        
        	Management address information about a particular chassis component.  There may be multiple management addresses configured on the remote system identified by a particular lldpRemIndex whose information is received on lldpRemLocalPortNum of the local system.  Each management address should have distinct 'management address type' (lldpRemManAddrSubtype) and 'management address' (lldpRemManAddr.)  Entries may be created and deleted in this table by the agent
        	**type**\: list of  		 :py:class:`Lldpremmanaddrentry <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.Lldpremmanaddrtable.Lldpremmanaddrentry>`
        
        

        """

        _prefix = 'LLDP-MIB'
        _revision = '2005-05-06'

        def __init__(self):
            super(LLDPMIB.Lldpremmanaddrtable, self).__init__()

            self.yang_name = "lldpRemManAddrTable"
            self.yang_parent_name = "LLDP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("lldpRemManAddrEntry", ("lldpremmanaddrentry", LLDPMIB.Lldpremmanaddrtable.Lldpremmanaddrentry))])
            self._leafs = OrderedDict()

            self.lldpremmanaddrentry = YList(self)
            self._segment_path = lambda: "lldpRemManAddrTable"
            self._absolute_path = lambda: "LLDP-MIB:LLDP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(LLDPMIB.Lldpremmanaddrtable, [], name, value)


        class Lldpremmanaddrentry(Entity):
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
            
            	**refers to**\:  :py:class:`lldpremtimemark <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.Lldpremtable.Lldprementry>`
            
            .. attribute:: lldpremlocalportnum  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4096
            
            	**refers to**\:  :py:class:`lldpremlocalportnum <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.Lldpremtable.Lldprementry>`
            
            .. attribute:: lldpremindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`lldpremindex <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.Lldpremtable.Lldprementry>`
            
            .. attribute:: lldpremmanaddrsubtype  (key)
            
            	The type of management address identifier encoding used in the associated 'lldpRemManagmentAddr' object
            	**type**\:  :py:class:`AddressFamilyNumbers <ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB.AddressFamilyNumbers>`
            
            .. attribute:: lldpremmanaddr  (key)
            
            	The string value used to identify the management address component associated with the remote system.  The purpose of this address is to contact the management entity
            	**type**\: str
            
            	**length:** 1..31
            
            .. attribute:: lldpremmanaddrifsubtype
            
            	The enumeration value that identifies the interface numbering method used for defining the interface number, associated with the remote system
            	**type**\:  :py:class:`LldpManAddrIfSubtype <ydk.models.cisco_ios_xe.LLDP_MIB.LldpManAddrIfSubtype>`
            
            .. attribute:: lldpremmanaddrifid
            
            	The integer value used to identify the interface number regarding the management address component associated with the remote system
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: lldpremmanaddroid
            
            	The OID value used to identify the type of hardware component or protocol entity associated with the management address advertised by the remote system agent
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            

            """

            _prefix = 'LLDP-MIB'
            _revision = '2005-05-06'

            def __init__(self):
                super(LLDPMIB.Lldpremmanaddrtable.Lldpremmanaddrentry, self).__init__()

                self.yang_name = "lldpRemManAddrEntry"
                self.yang_parent_name = "lldpRemManAddrTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['lldpremtimemark','lldpremlocalportnum','lldpremindex','lldpremmanaddrsubtype','lldpremmanaddr']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('lldpremtimemark', YLeaf(YType.str, 'lldpRemTimeMark')),
                    ('lldpremlocalportnum', YLeaf(YType.str, 'lldpRemLocalPortNum')),
                    ('lldpremindex', YLeaf(YType.str, 'lldpRemIndex')),
                    ('lldpremmanaddrsubtype', YLeaf(YType.enumeration, 'lldpRemManAddrSubtype')),
                    ('lldpremmanaddr', YLeaf(YType.str, 'lldpRemManAddr')),
                    ('lldpremmanaddrifsubtype', YLeaf(YType.enumeration, 'lldpRemManAddrIfSubtype')),
                    ('lldpremmanaddrifid', YLeaf(YType.int32, 'lldpRemManAddrIfId')),
                    ('lldpremmanaddroid', YLeaf(YType.str, 'lldpRemManAddrOID')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(LLDPMIB.Lldpremmanaddrtable.Lldpremmanaddrentry, ['lldpremtimemark', 'lldpremlocalportnum', 'lldpremindex', 'lldpremmanaddrsubtype', 'lldpremmanaddr', 'lldpremmanaddrifsubtype', 'lldpremmanaddrifid', 'lldpremmanaddroid'], name, value)


    class Lldpremunknowntlvtable(Entity):
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
        	**type**\: list of  		 :py:class:`Lldpremunknowntlventry <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.Lldpremunknowntlvtable.Lldpremunknowntlventry>`
        
        

        """

        _prefix = 'LLDP-MIB'
        _revision = '2005-05-06'

        def __init__(self):
            super(LLDPMIB.Lldpremunknowntlvtable, self).__init__()

            self.yang_name = "lldpRemUnknownTLVTable"
            self.yang_parent_name = "LLDP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("lldpRemUnknownTLVEntry", ("lldpremunknowntlventry", LLDPMIB.Lldpremunknowntlvtable.Lldpremunknowntlventry))])
            self._leafs = OrderedDict()

            self.lldpremunknowntlventry = YList(self)
            self._segment_path = lambda: "lldpRemUnknownTLVTable"
            self._absolute_path = lambda: "LLDP-MIB:LLDP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(LLDPMIB.Lldpremunknowntlvtable, [], name, value)


        class Lldpremunknowntlventry(Entity):
            """
            Information about an unrecognized TLV received from a
            physical network connection.  Entries may be created and
            deleted in this table by the agent, if a physical topology
            discovery process is active.
            
            .. attribute:: lldpremtimemark  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`lldpremtimemark <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.Lldpremtable.Lldprementry>`
            
            .. attribute:: lldpremlocalportnum  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4096
            
            	**refers to**\:  :py:class:`lldpremlocalportnum <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.Lldpremtable.Lldprementry>`
            
            .. attribute:: lldpremindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`lldpremindex <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.Lldpremtable.Lldprementry>`
            
            .. attribute:: lldpremunknowntlvtype  (key)
            
            	This object represents the value extracted from the type field of the TLV
            	**type**\: int
            
            	**range:** 9..126
            
            .. attribute:: lldpremunknowntlvinfo
            
            	This object represents the value extracted from the value field of the TLV
            	**type**\: str
            
            	**length:** 0..511
            
            

            """

            _prefix = 'LLDP-MIB'
            _revision = '2005-05-06'

            def __init__(self):
                super(LLDPMIB.Lldpremunknowntlvtable.Lldpremunknowntlventry, self).__init__()

                self.yang_name = "lldpRemUnknownTLVEntry"
                self.yang_parent_name = "lldpRemUnknownTLVTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['lldpremtimemark','lldpremlocalportnum','lldpremindex','lldpremunknowntlvtype']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('lldpremtimemark', YLeaf(YType.str, 'lldpRemTimeMark')),
                    ('lldpremlocalportnum', YLeaf(YType.str, 'lldpRemLocalPortNum')),
                    ('lldpremindex', YLeaf(YType.str, 'lldpRemIndex')),
                    ('lldpremunknowntlvtype', YLeaf(YType.int32, 'lldpRemUnknownTLVType')),
                    ('lldpremunknowntlvinfo', YLeaf(YType.str, 'lldpRemUnknownTLVInfo')),
                ])
                self.lldpremtimemark = None
                self.lldpremlocalportnum = None
                self.lldpremindex = None
                self.lldpremunknowntlvtype = None
                self.lldpremunknowntlvinfo = None
                self._segment_path = lambda: "lldpRemUnknownTLVEntry" + "[lldpRemTimeMark='" + str(self.lldpremtimemark) + "']" + "[lldpRemLocalPortNum='" + str(self.lldpremlocalportnum) + "']" + "[lldpRemIndex='" + str(self.lldpremindex) + "']" + "[lldpRemUnknownTLVType='" + str(self.lldpremunknowntlvtype) + "']"
                self._absolute_path = lambda: "LLDP-MIB:LLDP-MIB/lldpRemUnknownTLVTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(LLDPMIB.Lldpremunknowntlvtable.Lldpremunknowntlventry, ['lldpremtimemark', 'lldpremlocalportnum', 'lldpremindex', 'lldpremunknowntlvtype', 'lldpremunknowntlvinfo'], name, value)


    class Lldpremorgdefinfotable(Entity):
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
        	**type**\: list of  		 :py:class:`Lldpremorgdefinfoentry <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.Lldpremorgdefinfotable.Lldpremorgdefinfoentry>`
        
        

        """

        _prefix = 'LLDP-MIB'
        _revision = '2005-05-06'

        def __init__(self):
            super(LLDPMIB.Lldpremorgdefinfotable, self).__init__()

            self.yang_name = "lldpRemOrgDefInfoTable"
            self.yang_parent_name = "LLDP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("lldpRemOrgDefInfoEntry", ("lldpremorgdefinfoentry", LLDPMIB.Lldpremorgdefinfotable.Lldpremorgdefinfoentry))])
            self._leafs = OrderedDict()

            self.lldpremorgdefinfoentry = YList(self)
            self._segment_path = lambda: "lldpRemOrgDefInfoTable"
            self._absolute_path = lambda: "LLDP-MIB:LLDP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(LLDPMIB.Lldpremorgdefinfotable, [], name, value)


        class Lldpremorgdefinfoentry(Entity):
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
            
            	**refers to**\:  :py:class:`lldpremtimemark <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.Lldpremtable.Lldprementry>`
            
            .. attribute:: lldpremlocalportnum  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4096
            
            	**refers to**\:  :py:class:`lldpremlocalportnum <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.Lldpremtable.Lldprementry>`
            
            .. attribute:: lldpremindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`lldpremindex <ydk.models.cisco_ios_xe.LLDP_MIB.LLDPMIB.Lldpremtable.Lldprementry>`
            
            .. attribute:: lldpremorgdefinfooui  (key)
            
            	The Organizationally Unique Identifier (OUI), as defined in IEEE std 802\-2001, is a 24 bit (three octets) globally unique assigned number referenced by various standards, of the information received from the remote system
            	**type**\: str
            
            	**length:** 3
            
            .. attribute:: lldpremorgdefinfosubtype  (key)
            
            	The integer value used to identify the subtype of the organizationally defined information received from the remote system.  The subtype value is required to identify different instances of organizationally defined information that could not be retrieved without a unique identifier that indicates the particular type of information contained in the information string
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: lldpremorgdefinfoindex  (key)
            
            	This object represents an arbitrary local integer value used by this agent to identify a particular unrecognized organizationally defined information instance, unique only for the lldpRemOrgDefInfoOUI and lldpRemOrgDefInfoSubtype from the same remote system.  An agent is encouraged to assign monotonically increasing index values to new entries, starting with one, after each reboot.  It is considered unlikely that the lldpRemOrgDefInfoIndex will wrap between reboots
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: lldpremorgdefinfo
            
            	The string value used to identify the organizationally defined information of the remote system.  The encoding for this object should be as defined for SnmpAdminString TC
            	**type**\: str
            
            	**length:** 0..507
            
            

            """

            _prefix = 'LLDP-MIB'
            _revision = '2005-05-06'

            def __init__(self):
                super(LLDPMIB.Lldpremorgdefinfotable.Lldpremorgdefinfoentry, self).__init__()

                self.yang_name = "lldpRemOrgDefInfoEntry"
                self.yang_parent_name = "lldpRemOrgDefInfoTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['lldpremtimemark','lldpremlocalportnum','lldpremindex','lldpremorgdefinfooui','lldpremorgdefinfosubtype','lldpremorgdefinfoindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('lldpremtimemark', YLeaf(YType.str, 'lldpRemTimeMark')),
                    ('lldpremlocalportnum', YLeaf(YType.str, 'lldpRemLocalPortNum')),
                    ('lldpremindex', YLeaf(YType.str, 'lldpRemIndex')),
                    ('lldpremorgdefinfooui', YLeaf(YType.str, 'lldpRemOrgDefInfoOUI')),
                    ('lldpremorgdefinfosubtype', YLeaf(YType.int32, 'lldpRemOrgDefInfoSubtype')),
                    ('lldpremorgdefinfoindex', YLeaf(YType.int32, 'lldpRemOrgDefInfoIndex')),
                    ('lldpremorgdefinfo', YLeaf(YType.str, 'lldpRemOrgDefInfo')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(LLDPMIB.Lldpremorgdefinfotable.Lldpremorgdefinfoentry, ['lldpremtimemark', 'lldpremlocalportnum', 'lldpremindex', 'lldpremorgdefinfooui', 'lldpremorgdefinfosubtype', 'lldpremorgdefinfoindex', 'lldpremorgdefinfo'], name, value)

    def clone_ptr(self):
        self._top_entity = LLDPMIB()
        return self._top_entity


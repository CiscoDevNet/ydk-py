""" Cisco_IOS_XR_snmp_agent_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR snmp\-agent package operational data.

This module contains definitions
for the following management objects\:
  snmp\: SNMP operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class DupReqDropStatus(Enum):
    """
    DupReqDropStatus (Enum Class)

    Dup req drop status

    .. data:: disabled = 0

    	Disabled

    .. data:: enabled = 1

    	Enabled

    """

    disabled = Enum.YLeaf(0, "disabled")

    enabled = Enum.YLeaf(1, "enabled")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
        return meta._meta_table['DupReqDropStatus']


class SnmpCorrRuleState(Enum):
    """
    SnmpCorrRuleState (Enum Class)

    Snmp corr rule state

    .. data:: rule_unapplied = 0

    	Rule is in Unapplied state

    .. data:: rule_applied = 1

    	Rule is Applied to specified hosts

    .. data:: rule_applied_all = 2

    	Rule is Applied to all of router

    """

    rule_unapplied = Enum.YLeaf(0, "rule-unapplied")

    rule_applied = Enum.YLeaf(1, "rule-applied")

    rule_applied_all = Enum.YLeaf(2, "rule-applied-all")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
        return meta._meta_table['SnmpCorrRuleState']


class SnmpCorrVbindMatch(Enum):
    """
    SnmpCorrVbindMatch (Enum Class)

    Snmp corr vbind match

    .. data:: index = 0

    	Match regexp to varbind index

    .. data:: value = 1

    	Match regexp to varbind value

    """

    index = Enum.YLeaf(0, "index")

    value = Enum.YLeaf(1, "value")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
        return meta._meta_table['SnmpCorrVbindMatch']



class Snmp(_Entity_):
    """
    SNMP operational data
    
    .. attribute:: trap_servers
    
    	List of trap hosts
    	**type**\:  :py:class:`TrapServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.TrapServers>`
    
    	**config**\: False
    
    .. attribute:: information
    
    	SNMP operational information
    	**type**\:  :py:class:`Information <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information>`
    
    	**config**\: False
    
    .. attribute:: interfaces
    
    	List of interfaces
    	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Interfaces>`
    
    	**config**\: False
    
    .. attribute:: correlator
    
    	Trap Correlator operational data
    	**type**\:  :py:class:`Correlator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Correlator>`
    
    	**config**\: False
    
    .. attribute:: interface_indexes
    
    	List of index
    	**type**\:  :py:class:`InterfaceIndexes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.InterfaceIndexes>`
    
    	**config**\: False
    
    .. attribute:: if_indexes
    
    	List of ifnames
    	**type**\:  :py:class:`IfIndexes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.IfIndexes>`
    
    	**config**\: False
    
    .. attribute:: sensor_mib
    
    	SNMP sensor MIB information
    	**type**\:  :py:class:`SensorMib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.SensorMib>`
    
    	**config**\: False
    
    .. attribute:: entity_mib
    
    	SNMP entity mib
    	**type**\:  :py:class:`EntityMib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.EntityMib>`
    
    	**config**\: False
    
    .. attribute:: interface_mib
    
    	SNMP IF\-MIB information
    	**type**\:  :py:class:`InterfaceMib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.InterfaceMib>`
    
    	**config**\: False
    
    

    """

    _prefix = 'snmp-agent-oper'
    _revision = '2018-07-20'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Snmp, self).__init__()
        self._top_entity = None

        self.yang_name = "snmp"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-agent-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("trap-servers", ("trap_servers", Snmp.TrapServers)), ("information", ("information", Snmp.Information)), ("interfaces", ("interfaces", Snmp.Interfaces)), ("correlator", ("correlator", Snmp.Correlator)), ("interface-indexes", ("interface_indexes", Snmp.InterfaceIndexes)), ("if-indexes", ("if_indexes", Snmp.IfIndexes)), ("Cisco-IOS-XR-snmp-sensormib-oper:sensor-mib", ("sensor_mib", Snmp.SensorMib)), ("Cisco-IOS-XR-snmp-entitymib-oper:entity-mib", ("entity_mib", Snmp.EntityMib)), ("Cisco-IOS-XR-snmp-ifmib-oper:interface-mib", ("interface_mib", Snmp.InterfaceMib))])
        self._leafs = OrderedDict()

        self.trap_servers = Snmp.TrapServers()
        self.trap_servers.parent = self
        self._children_name_map["trap_servers"] = "trap-servers"

        self.information = Snmp.Information()
        self.information.parent = self
        self._children_name_map["information"] = "information"

        self.interfaces = Snmp.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"

        self.correlator = Snmp.Correlator()
        self.correlator.parent = self
        self._children_name_map["correlator"] = "correlator"

        self.interface_indexes = Snmp.InterfaceIndexes()
        self.interface_indexes.parent = self
        self._children_name_map["interface_indexes"] = "interface-indexes"

        self.if_indexes = Snmp.IfIndexes()
        self.if_indexes.parent = self
        self._children_name_map["if_indexes"] = "if-indexes"

        self.sensor_mib = Snmp.SensorMib()
        self.sensor_mib.parent = self
        self._children_name_map["sensor_mib"] = "Cisco-IOS-XR-snmp-sensormib-oper:sensor-mib"

        self.entity_mib = Snmp.EntityMib()
        self.entity_mib.parent = self
        self._children_name_map["entity_mib"] = "Cisco-IOS-XR-snmp-entitymib-oper:entity-mib"

        self.interface_mib = Snmp.InterfaceMib()
        self.interface_mib.parent = self
        self._children_name_map["interface_mib"] = "Cisco-IOS-XR-snmp-ifmib-oper:interface-mib"
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Snmp, [], name, value)


    class TrapServers(_Entity_):
        """
        List of trap hosts
        
        .. attribute:: trap_server
        
        	Trap server and port to which the trap is to be sent and statistics
        	**type**\: list of  		 :py:class:`TrapServer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.TrapServers.TrapServer>`
        
        	**config**\: False
        
        

        """

        _prefix = 'snmp-agent-oper'
        _revision = '2018-07-20'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Snmp.TrapServers, self).__init__()

            self.yang_name = "trap-servers"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("trap-server", ("trap_server", Snmp.TrapServers.TrapServer))])
            self._leafs = OrderedDict()

            self.trap_server = YList(self)
            self._segment_path = lambda: "trap-servers"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.TrapServers, [], name, value)


        class TrapServer(_Entity_):
            """
            Trap server and port to which the trap is to be
            sent and statistics
            
            .. attribute:: trap_host
            
            	Trap Host
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: port
            
            	Trap port
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: number_of_pkts_in_trap_q
            
            	No. of trap packets in trapQ
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: max_q_length_of_trap_q
            
            	Maximum Queue length of trapQ
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: number_of_pkts_sent
            
            	No. of trap packets sent
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: number_of_pkts_dropped
            
            	No. of trap packets dropped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2018-07-20'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.TrapServers.TrapServer, self).__init__()

                self.yang_name = "trap-server"
                self.yang_parent_name = "trap-servers"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('trap_host', (YLeaf(YType.str, 'trap-host'), ['str'])),
                    ('port', (YLeaf(YType.uint16, 'port'), ['int'])),
                    ('number_of_pkts_in_trap_q', (YLeaf(YType.uint32, 'number-of-pkts-in-trap-q'), ['int'])),
                    ('max_q_length_of_trap_q', (YLeaf(YType.uint32, 'max-q-length-of-trap-q'), ['int'])),
                    ('number_of_pkts_sent', (YLeaf(YType.uint32, 'number-of-pkts-sent'), ['int'])),
                    ('number_of_pkts_dropped', (YLeaf(YType.uint32, 'number-of-pkts-dropped'), ['int'])),
                ])
                self.trap_host = None
                self.port = None
                self.number_of_pkts_in_trap_q = None
                self.max_q_length_of_trap_q = None
                self.number_of_pkts_sent = None
                self.number_of_pkts_dropped = None
                self._segment_path = lambda: "trap-server"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/trap-servers/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.TrapServers.TrapServer, ['trap_host', 'port', 'number_of_pkts_in_trap_q', 'max_q_length_of_trap_q', 'number_of_pkts_sent', 'number_of_pkts_dropped'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.TrapServers.TrapServer']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
            return meta._meta_table['Snmp.TrapServers']['meta_info']


    class Information(_Entity_):
        """
        SNMP operational information
        
        .. attribute:: hosts
        
        	SNMP host information
        	**type**\:  :py:class:`Hosts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Hosts>`
        
        	**config**\: False
        
        .. attribute:: system_up_time
        
        	System up time
        	**type**\:  :py:class:`SystemUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.SystemUpTime>`
        
        	**config**\: False
        
        .. attribute:: nms_addresses
        
        	SNMP request type summary 
        	**type**\:  :py:class:`NmsAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.NmsAddresses>`
        
        	**config**\: False
        
        .. attribute:: engine_id
        
        	SNMP engine ID
        	**type**\:  :py:class:`EngineId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.EngineId>`
        
        	**config**\: False
        
        .. attribute:: rx_queue
        
        	SNMP rx queue statistics
        	**type**\:  :py:class:`RxQueue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.RxQueue>`
        
        	**config**\: False
        
        .. attribute:: system_name
        
        	System name
        	**type**\:  :py:class:`SystemName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.SystemName>`
        
        	**config**\: False
        
        .. attribute:: request_type_detail
        
        	SNMP request type details 
        	**type**\:  :py:class:`RequestTypeDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.RequestTypeDetail>`
        
        	**config**\: False
        
        .. attribute:: duplicate_drop
        
        	Duplicate request status, count, time 
        	**type**\:  :py:class:`DuplicateDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.DuplicateDrop>`
        
        	**config**\: False
        
        .. attribute:: bulk_stats_transfers
        
        	List of bulkstats transfer on the system
        	**type**\:  :py:class:`BulkStatsTransfers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.BulkStatsTransfers>`
        
        	**config**\: False
        
        .. attribute:: trap_infos
        
        	SNMP trap OID
        	**type**\:  :py:class:`TrapInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.TrapInfos>`
        
        	**config**\: False
        
        .. attribute:: poll_oids
        
        	OID list for poll PDU
        	**type**\:  :py:class:`PollOids <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.PollOids>`
        
        	**config**\: False
        
        .. attribute:: infom_details
        
        	SNMP trap OID
        	**type**\:  :py:class:`InfomDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.InfomDetails>`
        
        	**config**\: False
        
        .. attribute:: statistics
        
        	SNMP statistics
        	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Statistics>`
        
        	**config**\: False
        
        .. attribute:: incoming_queue
        
        	Incoming queue details 
        	**type**\:  :py:class:`IncomingQueue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.IncomingQueue>`
        
        	**config**\: False
        
        .. attribute:: context_mapping
        
        	Context name, features name, topology name, instance
        	**type**\:  :py:class:`ContextMapping <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.ContextMapping>`
        
        	**config**\: False
        
        .. attribute:: trap_oids
        
        	SNMP trap OID
        	**type**\:  :py:class:`TrapOids <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.TrapOids>`
        
        	**config**\: False
        
        .. attribute:: nm_spackets
        
        	SNMP overload statistics 
        	**type**\:  :py:class:`NmSpackets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.NmSpackets>`
        
        	**config**\: False
        
        .. attribute:: mibs
        
        	List of MIBS supported on the system
        	**type**\:  :py:class:`Mibs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Mibs>`
        
        	**config**\: False
        
        .. attribute:: serial_numbers
        
        	SNMP statistics pdu 
        	**type**\:  :py:class:`SerialNumbers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.SerialNumbers>`
        
        	**config**\: False
        
        .. attribute:: drop_nms_addresses
        
        	NMS list for drop PDU
        	**type**\:  :py:class:`DropNmsAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.DropNmsAddresses>`
        
        	**config**\: False
        
        .. attribute:: views
        
        	SNMP view information
        	**type**\:  :py:class:`Views <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Views>`
        
        	**config**\: False
        
        .. attribute:: system_descr
        
        	System description
        	**type**\:  :py:class:`SystemDescr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.SystemDescr>`
        
        	**config**\: False
        
        .. attribute:: tables
        
        	List of table
        	**type**\:  :py:class:`Tables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Tables>`
        
        	**config**\: False
        
        .. attribute:: system_oid
        
        	System object ID
        	**type**\:  :py:class:`SystemOid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.SystemOid>`
        
        	**config**\: False
        
        .. attribute:: trap_queue
        
        	SNMP trap queue statistics
        	**type**\:  :py:class:`TrapQueue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.TrapQueue>`
        
        	**config**\: False
        
        

        """

        _prefix = 'snmp-agent-oper'
        _revision = '2018-07-20'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Snmp.Information, self).__init__()

            self.yang_name = "information"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("hosts", ("hosts", Snmp.Information.Hosts)), ("system-up-time", ("system_up_time", Snmp.Information.SystemUpTime)), ("nms-addresses", ("nms_addresses", Snmp.Information.NmsAddresses)), ("engine-id", ("engine_id", Snmp.Information.EngineId)), ("rx-queue", ("rx_queue", Snmp.Information.RxQueue)), ("system-name", ("system_name", Snmp.Information.SystemName)), ("request-type-detail", ("request_type_detail", Snmp.Information.RequestTypeDetail)), ("duplicate-drop", ("duplicate_drop", Snmp.Information.DuplicateDrop)), ("bulk-stats-transfers", ("bulk_stats_transfers", Snmp.Information.BulkStatsTransfers)), ("trap-infos", ("trap_infos", Snmp.Information.TrapInfos)), ("poll-oids", ("poll_oids", Snmp.Information.PollOids)), ("infom-details", ("infom_details", Snmp.Information.InfomDetails)), ("statistics", ("statistics", Snmp.Information.Statistics)), ("incoming-queue", ("incoming_queue", Snmp.Information.IncomingQueue)), ("context-mapping", ("context_mapping", Snmp.Information.ContextMapping)), ("trap-oids", ("trap_oids", Snmp.Information.TrapOids)), ("nm-spackets", ("nm_spackets", Snmp.Information.NmSpackets)), ("mibs", ("mibs", Snmp.Information.Mibs)), ("serial-numbers", ("serial_numbers", Snmp.Information.SerialNumbers)), ("drop-nms-addresses", ("drop_nms_addresses", Snmp.Information.DropNmsAddresses)), ("views", ("views", Snmp.Information.Views)), ("system-descr", ("system_descr", Snmp.Information.SystemDescr)), ("tables", ("tables", Snmp.Information.Tables)), ("system-oid", ("system_oid", Snmp.Information.SystemOid)), ("trap-queue", ("trap_queue", Snmp.Information.TrapQueue))])
            self._leafs = OrderedDict()

            self.hosts = Snmp.Information.Hosts()
            self.hosts.parent = self
            self._children_name_map["hosts"] = "hosts"

            self.system_up_time = Snmp.Information.SystemUpTime()
            self.system_up_time.parent = self
            self._children_name_map["system_up_time"] = "system-up-time"

            self.nms_addresses = Snmp.Information.NmsAddresses()
            self.nms_addresses.parent = self
            self._children_name_map["nms_addresses"] = "nms-addresses"

            self.engine_id = Snmp.Information.EngineId()
            self.engine_id.parent = self
            self._children_name_map["engine_id"] = "engine-id"

            self.rx_queue = Snmp.Information.RxQueue()
            self.rx_queue.parent = self
            self._children_name_map["rx_queue"] = "rx-queue"

            self.system_name = Snmp.Information.SystemName()
            self.system_name.parent = self
            self._children_name_map["system_name"] = "system-name"

            self.request_type_detail = Snmp.Information.RequestTypeDetail()
            self.request_type_detail.parent = self
            self._children_name_map["request_type_detail"] = "request-type-detail"

            self.duplicate_drop = Snmp.Information.DuplicateDrop()
            self.duplicate_drop.parent = self
            self._children_name_map["duplicate_drop"] = "duplicate-drop"

            self.bulk_stats_transfers = Snmp.Information.BulkStatsTransfers()
            self.bulk_stats_transfers.parent = self
            self._children_name_map["bulk_stats_transfers"] = "bulk-stats-transfers"

            self.trap_infos = Snmp.Information.TrapInfos()
            self.trap_infos.parent = self
            self._children_name_map["trap_infos"] = "trap-infos"

            self.poll_oids = Snmp.Information.PollOids()
            self.poll_oids.parent = self
            self._children_name_map["poll_oids"] = "poll-oids"

            self.infom_details = Snmp.Information.InfomDetails()
            self.infom_details.parent = self
            self._children_name_map["infom_details"] = "infom-details"

            self.statistics = Snmp.Information.Statistics()
            self.statistics.parent = self
            self._children_name_map["statistics"] = "statistics"

            self.incoming_queue = Snmp.Information.IncomingQueue()
            self.incoming_queue.parent = self
            self._children_name_map["incoming_queue"] = "incoming-queue"

            self.context_mapping = Snmp.Information.ContextMapping()
            self.context_mapping.parent = self
            self._children_name_map["context_mapping"] = "context-mapping"

            self.trap_oids = Snmp.Information.TrapOids()
            self.trap_oids.parent = self
            self._children_name_map["trap_oids"] = "trap-oids"

            self.nm_spackets = Snmp.Information.NmSpackets()
            self.nm_spackets.parent = self
            self._children_name_map["nm_spackets"] = "nm-spackets"

            self.mibs = Snmp.Information.Mibs()
            self.mibs.parent = self
            self._children_name_map["mibs"] = "mibs"

            self.serial_numbers = Snmp.Information.SerialNumbers()
            self.serial_numbers.parent = self
            self._children_name_map["serial_numbers"] = "serial-numbers"

            self.drop_nms_addresses = Snmp.Information.DropNmsAddresses()
            self.drop_nms_addresses.parent = self
            self._children_name_map["drop_nms_addresses"] = "drop-nms-addresses"

            self.views = Snmp.Information.Views()
            self.views.parent = self
            self._children_name_map["views"] = "views"

            self.system_descr = Snmp.Information.SystemDescr()
            self.system_descr.parent = self
            self._children_name_map["system_descr"] = "system-descr"

            self.tables = Snmp.Information.Tables()
            self.tables.parent = self
            self._children_name_map["tables"] = "tables"

            self.system_oid = Snmp.Information.SystemOid()
            self.system_oid.parent = self
            self._children_name_map["system_oid"] = "system-oid"

            self.trap_queue = Snmp.Information.TrapQueue()
            self.trap_queue.parent = self
            self._children_name_map["trap_queue"] = "trap-queue"
            self._segment_path = lambda: "information"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.Information, [], name, value)


        class Hosts(_Entity_):
            """
            SNMP host information
            
            .. attribute:: host
            
            	SNMP target host name
            	**type**\: list of  		 :py:class:`Host <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Hosts.Host>`
            
            	**config**\: False
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2018-07-20'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Information.Hosts, self).__init__()

                self.yang_name = "hosts"
                self.yang_parent_name = "information"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("host", ("host", Snmp.Information.Hosts.Host))])
                self._leafs = OrderedDict()

                self.host = YList(self)
                self._segment_path = lambda: "hosts"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Information.Hosts, [], name, value)


            class Host(_Entity_):
                """
                SNMP target host name
                
                .. attribute:: name  (key)
                
                	Group name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                	**config**\: False
                
                .. attribute:: host_information
                
                	Host name ,udp\-port , user, security model and level
                	**type**\: list of  		 :py:class:`HostInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Hosts.Host.HostInformation>`
                
                	**config**\: False
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2018-07-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.Information.Hosts.Host, self).__init__()

                    self.yang_name = "host"
                    self.yang_parent_name = "hosts"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['name']
                    self._child_classes = OrderedDict([("host-information", ("host_information", Snmp.Information.Hosts.Host.HostInformation))])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ])
                    self.name = None

                    self.host_information = YList(self)
                    self._segment_path = lambda: "host" + "[name='" + str(self.name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/hosts/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Information.Hosts.Host, ['name'], name, value)


                class HostInformation(_Entity_):
                    """
                    Host name ,udp\-port , user, security model
                    and level
                    
                    .. attribute:: user  (key)
                    
                    	SNMP host user
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    	**config**\: False
                    
                    .. attribute:: snmp_target_address_t_host
                    
                    	Transport type of address
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: snmp_target_address_port
                    
                    	Target UDP port
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: snmp_target_addresstype
                    
                    	Target host type (Inform or Trap)
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: snmp_target_params_security_model
                    
                    	Security model
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: snmp_target_params_security_name
                    
                    	Security name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: snmp_target_params_security_level
                    
                    	Security level
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'snmp-agent-oper'
                    _revision = '2018-07-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Snmp.Information.Hosts.Host.HostInformation, self).__init__()

                        self.yang_name = "host-information"
                        self.yang_parent_name = "host"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['user']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('user', (YLeaf(YType.str, 'user'), ['str'])),
                            ('snmp_target_address_t_host', (YLeaf(YType.str, 'snmp-target-address-t-host'), ['str'])),
                            ('snmp_target_address_port', (YLeaf(YType.str, 'snmp-target-address-port'), ['str'])),
                            ('snmp_target_addresstype', (YLeaf(YType.str, 'snmp-target-addresstype'), ['str'])),
                            ('snmp_target_params_security_model', (YLeaf(YType.str, 'snmp-target-params-security-model'), ['str'])),
                            ('snmp_target_params_security_name', (YLeaf(YType.str, 'snmp-target-params-security-name'), ['str'])),
                            ('snmp_target_params_security_level', (YLeaf(YType.str, 'snmp-target-params-security-level'), ['str'])),
                        ])
                        self.user = None
                        self.snmp_target_address_t_host = None
                        self.snmp_target_address_port = None
                        self.snmp_target_addresstype = None
                        self.snmp_target_params_security_model = None
                        self.snmp_target_params_security_name = None
                        self.snmp_target_params_security_level = None
                        self._segment_path = lambda: "host-information" + "[user='" + str(self.user) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.Information.Hosts.Host.HostInformation, ['user', 'snmp_target_address_t_host', 'snmp_target_address_port', 'snmp_target_addresstype', 'snmp_target_params_security_model', 'snmp_target_params_security_name', 'snmp_target_params_security_level'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                        return meta._meta_table['Snmp.Information.Hosts.Host.HostInformation']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.Information.Hosts.Host']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.Hosts']['meta_info']


        class SystemUpTime(_Entity_):
            """
            System up time
            
            .. attribute:: system_up_time_edm
            
            	sysUpTime  1.3.6.1.2.1.1.3
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2018-07-20'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Information.SystemUpTime, self).__init__()

                self.yang_name = "system-up-time"
                self.yang_parent_name = "information"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('system_up_time_edm', (YLeaf(YType.str, 'system-up-time-edm'), ['str'])),
                ])
                self.system_up_time_edm = None
                self._segment_path = lambda: "system-up-time"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Information.SystemUpTime, ['system_up_time_edm'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.SystemUpTime']['meta_info']


        class NmsAddresses(_Entity_):
            """
            SNMP request type summary 
            
            .. attribute:: nms_address
            
            	NMS address
            	**type**\: list of  		 :py:class:`NmsAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.NmsAddresses.NmsAddress>`
            
            	**config**\: False
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2018-07-20'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Information.NmsAddresses, self).__init__()

                self.yang_name = "nms-addresses"
                self.yang_parent_name = "information"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("nms-address", ("nms_address", Snmp.Information.NmsAddresses.NmsAddress))])
                self._leafs = OrderedDict()

                self.nms_address = YList(self)
                self._segment_path = lambda: "nms-addresses"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Information.NmsAddresses, [], name, value)


            class NmsAddress(_Entity_):
                """
                NMS address
                
                .. attribute:: nms_addr  (key)
                
                	NMS address
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                	**config**\: False
                
                .. attribute:: nms_address
                
                	NMS address of server
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: get_request_count
                
                	Get Request Count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: getnext_request_count
                
                	Getnext Request Count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: getbulk_request_count
                
                	Getbulk Request Count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: set_request_count
                
                	Set Request Count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: test_request_count
                
                	Test Request Count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2018-07-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.Information.NmsAddresses.NmsAddress, self).__init__()

                    self.yang_name = "nms-address"
                    self.yang_parent_name = "nms-addresses"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['nms_addr']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('nms_addr', (YLeaf(YType.str, 'nms-addr'), ['str'])),
                        ('nms_address', (YLeaf(YType.str, 'nms-address'), ['str'])),
                        ('get_request_count', (YLeaf(YType.uint32, 'get-request-count'), ['int'])),
                        ('getnext_request_count', (YLeaf(YType.uint32, 'getnext-request-count'), ['int'])),
                        ('getbulk_request_count', (YLeaf(YType.uint32, 'getbulk-request-count'), ['int'])),
                        ('set_request_count', (YLeaf(YType.uint32, 'set-request-count'), ['int'])),
                        ('test_request_count', (YLeaf(YType.uint32, 'test-request-count'), ['int'])),
                    ])
                    self.nms_addr = None
                    self.nms_address = None
                    self.get_request_count = None
                    self.getnext_request_count = None
                    self.getbulk_request_count = None
                    self.set_request_count = None
                    self.test_request_count = None
                    self._segment_path = lambda: "nms-address" + "[nms-addr='" + str(self.nms_addr) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/nms-addresses/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Information.NmsAddresses.NmsAddress, ['nms_addr', 'nms_address', 'get_request_count', 'getnext_request_count', 'getbulk_request_count', 'set_request_count', 'test_request_count'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.Information.NmsAddresses.NmsAddress']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.NmsAddresses']['meta_info']


        class EngineId(_Entity_):
            """
            SNMP engine ID
            
            .. attribute:: engine_id
            
            	SNMPv3 engineID
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2018-07-20'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Information.EngineId, self).__init__()

                self.yang_name = "engine-id"
                self.yang_parent_name = "information"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('engine_id', (YLeaf(YType.str, 'engine-id'), ['str'])),
                ])
                self.engine_id = None
                self._segment_path = lambda: "engine-id"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Information.EngineId, ['engine_id'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.EngineId']['meta_info']


        class RxQueue(_Entity_):
            """
            SNMP rx queue statistics
            
            .. attribute:: qlen
            
            	qlen
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: in_min
            
            	in min
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: in_avg
            
            	in avg
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: in_max
            
            	in max
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: pend_min
            
            	pend min
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: pend_avg
            
            	pend avg
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: pend_max
            
            	pend max
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: incoming_q
            
            	incoming q
            	**type**\: list of  		 :py:class:`IncomingQ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.RxQueue.IncomingQ>`
            
            	**config**\: False
            
            .. attribute:: pending_q
            
            	pending q
            	**type**\: list of  		 :py:class:`PendingQ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.RxQueue.PendingQ>`
            
            	**config**\: False
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2018-07-20'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Information.RxQueue, self).__init__()

                self.yang_name = "rx-queue"
                self.yang_parent_name = "information"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("incoming-q", ("incoming_q", Snmp.Information.RxQueue.IncomingQ)), ("pending-q", ("pending_q", Snmp.Information.RxQueue.PendingQ))])
                self._leafs = OrderedDict([
                    ('qlen', (YLeaf(YType.uint32, 'qlen'), ['int'])),
                    ('in_min', (YLeaf(YType.uint32, 'in-min'), ['int'])),
                    ('in_avg', (YLeaf(YType.uint32, 'in-avg'), ['int'])),
                    ('in_max', (YLeaf(YType.uint32, 'in-max'), ['int'])),
                    ('pend_min', (YLeaf(YType.uint32, 'pend-min'), ['int'])),
                    ('pend_avg', (YLeaf(YType.uint32, 'pend-avg'), ['int'])),
                    ('pend_max', (YLeaf(YType.uint32, 'pend-max'), ['int'])),
                ])
                self.qlen = None
                self.in_min = None
                self.in_avg = None
                self.in_max = None
                self.pend_min = None
                self.pend_avg = None
                self.pend_max = None

                self.incoming_q = YList(self)
                self.pending_q = YList(self)
                self._segment_path = lambda: "rx-queue"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Information.RxQueue, ['qlen', 'in_min', 'in_avg', 'in_max', 'pend_min', 'pend_avg', 'pend_max'], name, value)


            class IncomingQ(_Entity_):
                """
                incoming q
                
                .. attribute:: min
                
                	min
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: avg
                
                	avg
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: max
                
                	max
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2018-07-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.Information.RxQueue.IncomingQ, self).__init__()

                    self.yang_name = "incoming-q"
                    self.yang_parent_name = "rx-queue"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('min', (YLeaf(YType.uint32, 'min'), ['int'])),
                        ('avg', (YLeaf(YType.uint32, 'avg'), ['int'])),
                        ('max', (YLeaf(YType.uint32, 'max'), ['int'])),
                    ])
                    self.min = None
                    self.avg = None
                    self.max = None
                    self._segment_path = lambda: "incoming-q"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/rx-queue/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Information.RxQueue.IncomingQ, ['min', 'avg', 'max'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.Information.RxQueue.IncomingQ']['meta_info']


            class PendingQ(_Entity_):
                """
                pending q
                
                .. attribute:: min
                
                	min
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: avg
                
                	avg
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: max
                
                	max
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2018-07-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.Information.RxQueue.PendingQ, self).__init__()

                    self.yang_name = "pending-q"
                    self.yang_parent_name = "rx-queue"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('min', (YLeaf(YType.uint32, 'min'), ['int'])),
                        ('avg', (YLeaf(YType.uint32, 'avg'), ['int'])),
                        ('max', (YLeaf(YType.uint32, 'max'), ['int'])),
                    ])
                    self.min = None
                    self.avg = None
                    self.max = None
                    self._segment_path = lambda: "pending-q"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/rx-queue/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Information.RxQueue.PendingQ, ['min', 'avg', 'max'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.Information.RxQueue.PendingQ']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.RxQueue']['meta_info']


        class SystemName(_Entity_):
            """
            System name
            
            .. attribute:: system_name
            
            	sysName  1.3.6.1.2.1.1.5
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2018-07-20'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Information.SystemName, self).__init__()

                self.yang_name = "system-name"
                self.yang_parent_name = "information"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('system_name', (YLeaf(YType.str, 'system-name'), ['str'])),
                ])
                self.system_name = None
                self._segment_path = lambda: "system-name"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Information.SystemName, ['system_name'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.SystemName']['meta_info']


        class RequestTypeDetail(_Entity_):
            """
            SNMP request type details 
            
            .. attribute:: nms_addresses
            
            	snmp request type details 
            	**type**\:  :py:class:`NmsAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.RequestTypeDetail.NmsAddresses>`
            
            	**config**\: False
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2018-07-20'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Information.RequestTypeDetail, self).__init__()

                self.yang_name = "request-type-detail"
                self.yang_parent_name = "information"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("nms-addresses", ("nms_addresses", Snmp.Information.RequestTypeDetail.NmsAddresses))])
                self._leafs = OrderedDict()

                self.nms_addresses = Snmp.Information.RequestTypeDetail.NmsAddresses()
                self.nms_addresses.parent = self
                self._children_name_map["nms_addresses"] = "nms-addresses"
                self._segment_path = lambda: "request-type-detail"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Information.RequestTypeDetail, [], name, value)


            class NmsAddresses(_Entity_):
                """
                snmp request type details 
                
                .. attribute:: nms_address
                
                	NMS address
                	**type**\: list of  		 :py:class:`NmsAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.RequestTypeDetail.NmsAddresses.NmsAddress>`
                
                	**config**\: False
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2018-07-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.Information.RequestTypeDetail.NmsAddresses, self).__init__()

                    self.yang_name = "nms-addresses"
                    self.yang_parent_name = "request-type-detail"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("nms-address", ("nms_address", Snmp.Information.RequestTypeDetail.NmsAddresses.NmsAddress))])
                    self._leafs = OrderedDict()

                    self.nms_address = YList(self)
                    self._segment_path = lambda: "nms-addresses"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/request-type-detail/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Information.RequestTypeDetail.NmsAddresses, [], name, value)


                class NmsAddress(_Entity_):
                    """
                    NMS address
                    
                    .. attribute:: nms_addr  (key)
                    
                    	NMS address
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    	**config**\: False
                    
                    .. attribute:: total_count
                    
                    	Total request count for each managment station or client
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: agent_request_count
                    
                    	Processing agent request count for each client for particluar managment station
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: interface_request_count
                    
                    	Processing interfce request count for each client for particluar managment station
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: entity_request_count
                    
                    	Processing entity request count for each client for particluar managment station
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: route_request_count
                    
                    	Processing route request count for each client for particluar Managment station
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: infra_request_count
                    
                    	Processing infra request count for each client for particluar Managment station
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'snmp-agent-oper'
                    _revision = '2018-07-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Snmp.Information.RequestTypeDetail.NmsAddresses.NmsAddress, self).__init__()

                        self.yang_name = "nms-address"
                        self.yang_parent_name = "nms-addresses"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['nms_addr']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('nms_addr', (YLeaf(YType.str, 'nms-addr'), ['str'])),
                            ('total_count', (YLeaf(YType.uint32, 'total-count'), ['int'])),
                            ('agent_request_count', (YLeaf(YType.uint32, 'agent-request-count'), ['int'])),
                            ('interface_request_count', (YLeaf(YType.uint32, 'interface-request-count'), ['int'])),
                            ('entity_request_count', (YLeaf(YType.uint32, 'entity-request-count'), ['int'])),
                            ('route_request_count', (YLeaf(YType.uint32, 'route-request-count'), ['int'])),
                            ('infra_request_count', (YLeaf(YType.uint32, 'infra-request-count'), ['int'])),
                        ])
                        self.nms_addr = None
                        self.total_count = None
                        self.agent_request_count = None
                        self.interface_request_count = None
                        self.entity_request_count = None
                        self.route_request_count = None
                        self.infra_request_count = None
                        self._segment_path = lambda: "nms-address" + "[nms-addr='" + str(self.nms_addr) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/request-type-detail/nms-addresses/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.Information.RequestTypeDetail.NmsAddresses.NmsAddress, ['nms_addr', 'total_count', 'agent_request_count', 'interface_request_count', 'entity_request_count', 'route_request_count', 'infra_request_count'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                        return meta._meta_table['Snmp.Information.RequestTypeDetail.NmsAddresses.NmsAddress']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.Information.RequestTypeDetail.NmsAddresses']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.RequestTypeDetail']['meta_info']


        class DuplicateDrop(_Entity_):
            """
            Duplicate request status, count, time 
            
            .. attribute:: duplicate_request_status
            
            	Duplicate requests drop feature status
            	**type**\:  :py:class:`DupReqDropStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.DupReqDropStatus>`
            
            	**config**\: False
            
            .. attribute:: last_status_change_time
            
            	Duplicate request drop feature last enable disable time (Day Mon Date HH\:MM\:SS)
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: duplicate_drop_configured_timeout
            
            	Configured Duplicate Drop feature Timeout
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: duplicate_dropped_requests
            
            	Number of duplicate SNMP requests are dropped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: retry_processed_requests
            
            	Number of Retry SNMP requests are Processed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: first_enable_time
            
            	Duplicate request drop feature first  enable time (Day Mon Date HH\:MM\:SS)
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: latest_duplicate_dropped_requests
            
            	Number of duplicate SNMP requests dropped, from the last enable time
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: latest_retry_processed_requests
            
            	Number of retry SNMP requests processed, from the last enable time
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: duplicate_request_latest_enable_time
            
            	Duplicate request drop feature last enable time(Day Mon Date HH\:MM\:SS)
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: duplicate_drop_enable_count
            
            	 Number of times duplicate request drop feature is enabled
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: duplicate_drop_disable_count
            
            	 Number of times duplicate request drop feature is disabled
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2018-07-20'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Information.DuplicateDrop, self).__init__()

                self.yang_name = "duplicate-drop"
                self.yang_parent_name = "information"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('duplicate_request_status', (YLeaf(YType.enumeration, 'duplicate-request-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'DupReqDropStatus', '')])),
                    ('last_status_change_time', (YLeaf(YType.str, 'last-status-change-time'), ['str'])),
                    ('duplicate_drop_configured_timeout', (YLeaf(YType.uint32, 'duplicate-drop-configured-timeout'), ['int'])),
                    ('duplicate_dropped_requests', (YLeaf(YType.uint32, 'duplicate-dropped-requests'), ['int'])),
                    ('retry_processed_requests', (YLeaf(YType.uint32, 'retry-processed-requests'), ['int'])),
                    ('first_enable_time', (YLeaf(YType.str, 'first-enable-time'), ['str'])),
                    ('latest_duplicate_dropped_requests', (YLeaf(YType.uint32, 'latest-duplicate-dropped-requests'), ['int'])),
                    ('latest_retry_processed_requests', (YLeaf(YType.uint32, 'latest-retry-processed-requests'), ['int'])),
                    ('duplicate_request_latest_enable_time', (YLeaf(YType.str, 'duplicate-request-latest-enable-time'), ['str'])),
                    ('duplicate_drop_enable_count', (YLeaf(YType.uint32, 'duplicate-drop-enable-count'), ['int'])),
                    ('duplicate_drop_disable_count', (YLeaf(YType.uint32, 'duplicate-drop-disable-count'), ['int'])),
                ])
                self.duplicate_request_status = None
                self.last_status_change_time = None
                self.duplicate_drop_configured_timeout = None
                self.duplicate_dropped_requests = None
                self.retry_processed_requests = None
                self.first_enable_time = None
                self.latest_duplicate_dropped_requests = None
                self.latest_retry_processed_requests = None
                self.duplicate_request_latest_enable_time = None
                self.duplicate_drop_enable_count = None
                self.duplicate_drop_disable_count = None
                self._segment_path = lambda: "duplicate-drop"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Information.DuplicateDrop, ['duplicate_request_status', 'last_status_change_time', 'duplicate_drop_configured_timeout', 'duplicate_dropped_requests', 'retry_processed_requests', 'first_enable_time', 'latest_duplicate_dropped_requests', 'latest_retry_processed_requests', 'duplicate_request_latest_enable_time', 'duplicate_drop_enable_count', 'duplicate_drop_disable_count'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.DuplicateDrop']['meta_info']


        class BulkStatsTransfers(_Entity_):
            """
            List of bulkstats transfer on the system
            
            .. attribute:: bulk_stats_transfer
            
            	SNMP bulkstats transfer name
            	**type**\: list of  		 :py:class:`BulkStatsTransfer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.BulkStatsTransfers.BulkStatsTransfer>`
            
            	**config**\: False
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2018-07-20'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Information.BulkStatsTransfers, self).__init__()

                self.yang_name = "bulk-stats-transfers"
                self.yang_parent_name = "information"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("bulk-stats-transfer", ("bulk_stats_transfer", Snmp.Information.BulkStatsTransfers.BulkStatsTransfer))])
                self._leafs = OrderedDict()

                self.bulk_stats_transfer = YList(self)
                self._segment_path = lambda: "bulk-stats-transfers"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Information.BulkStatsTransfers, [], name, value)


            class BulkStatsTransfer(_Entity_):
                """
                SNMP bulkstats transfer name
                
                .. attribute:: transfer_name  (key)
                
                	Transfer name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                	**config**\: False
                
                .. attribute:: transfer_name_xr
                
                	Name of the bulkstats transfer session
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: url_primary
                
                	Bulkstats transfer primary URL
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: url_secondary
                
                	Bulkstats transfer secondary URL
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: retained_file
                
                	Bulkstats transfer retained file name
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: time_left
                
                	Bulkstats transfer retry time left in seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                	**units**\: second
                
                .. attribute:: retry_left
                
                	Bulkstats transfer retry attempt left
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2018-07-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.Information.BulkStatsTransfers.BulkStatsTransfer, self).__init__()

                    self.yang_name = "bulk-stats-transfer"
                    self.yang_parent_name = "bulk-stats-transfers"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['transfer_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('transfer_name', (YLeaf(YType.str, 'transfer-name'), ['str'])),
                        ('transfer_name_xr', (YLeaf(YType.str, 'transfer-name-xr'), ['str'])),
                        ('url_primary', (YLeaf(YType.str, 'url-primary'), ['str'])),
                        ('url_secondary', (YLeaf(YType.str, 'url-secondary'), ['str'])),
                        ('retained_file', (YLeaf(YType.str, 'retained-file'), ['str'])),
                        ('time_left', (YLeaf(YType.uint32, 'time-left'), ['int'])),
                        ('retry_left', (YLeaf(YType.uint32, 'retry-left'), ['int'])),
                    ])
                    self.transfer_name = None
                    self.transfer_name_xr = None
                    self.url_primary = None
                    self.url_secondary = None
                    self.retained_file = None
                    self.time_left = None
                    self.retry_left = None
                    self._segment_path = lambda: "bulk-stats-transfer" + "[transfer-name='" + str(self.transfer_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/bulk-stats-transfers/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Information.BulkStatsTransfers.BulkStatsTransfer, ['transfer_name', 'transfer_name_xr', 'url_primary', 'url_secondary', 'retained_file', 'time_left', 'retry_left'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.Information.BulkStatsTransfers.BulkStatsTransfer']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.BulkStatsTransfers']['meta_info']


        class TrapInfos(_Entity_):
            """
            SNMP trap OID
            
            .. attribute:: trap_info
            
            	SNMP Trap infomation like server , port and trapOID
            	**type**\: list of  		 :py:class:`TrapInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.TrapInfos.TrapInfo>`
            
            	**config**\: False
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2018-07-20'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Information.TrapInfos, self).__init__()

                self.yang_name = "trap-infos"
                self.yang_parent_name = "information"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("trap-info", ("trap_info", Snmp.Information.TrapInfos.TrapInfo))])
                self._leafs = OrderedDict()

                self.trap_info = YList(self)
                self._segment_path = lambda: "trap-infos"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Information.TrapInfos, [], name, value)


            class TrapInfo(_Entity_):
                """
                SNMP Trap infomation like server , port and
                trapOID
                
                .. attribute:: trap_host
                
                	Trap Host
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: port
                
                	Trap port
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                .. attribute:: host
                
                	NMS/Host address
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: port_xr
                
                	udp port number
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                .. attribute:: trap_oid_count
                
                	Total number of OID's sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: trap_oi_dinfo
                
                	Per trap OID statistics
                	**type**\: list of  		 :py:class:`TrapOiDinfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.TrapInfos.TrapInfo.TrapOiDinfo>`
                
                	**config**\: False
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2018-07-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.Information.TrapInfos.TrapInfo, self).__init__()

                    self.yang_name = "trap-info"
                    self.yang_parent_name = "trap-infos"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("trap-oi-dinfo", ("trap_oi_dinfo", Snmp.Information.TrapInfos.TrapInfo.TrapOiDinfo))])
                    self._leafs = OrderedDict([
                        ('trap_host', (YLeaf(YType.str, 'trap-host'), ['str'])),
                        ('port', (YLeaf(YType.uint16, 'port'), ['int'])),
                        ('host', (YLeaf(YType.str, 'host'), ['str'])),
                        ('port_xr', (YLeaf(YType.uint16, 'port-xr'), ['int'])),
                        ('trap_oid_count', (YLeaf(YType.uint32, 'trap-oid-count'), ['int'])),
                    ])
                    self.trap_host = None
                    self.port = None
                    self.host = None
                    self.port_xr = None
                    self.trap_oid_count = None

                    self.trap_oi_dinfo = YList(self)
                    self._segment_path = lambda: "trap-info"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/trap-infos/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Information.TrapInfos.TrapInfo, ['trap_host', 'port', 'host', 'port_xr', 'trap_oid_count'], name, value)


                class TrapOiDinfo(_Entity_):
                    """
                    Per trap OID statistics
                    
                    .. attribute:: trap_oid
                    
                    	TRAP OID
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: count
                    
                    	Number of traps sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: drop_count
                    
                    	Number of Traps Dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: retry_count
                    
                    	Num of times retry
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: lastsent_time
                    
                    	Timestamp of latest successfully sent
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: lasrdrop_time
                    
                    	Timestamp of latest droped
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'snmp-agent-oper'
                    _revision = '2018-07-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Snmp.Information.TrapInfos.TrapInfo.TrapOiDinfo, self).__init__()

                        self.yang_name = "trap-oi-dinfo"
                        self.yang_parent_name = "trap-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('trap_oid', (YLeaf(YType.str, 'trap-oid'), ['str'])),
                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                            ('drop_count', (YLeaf(YType.uint32, 'drop-count'), ['int'])),
                            ('retry_count', (YLeaf(YType.uint32, 'retry-count'), ['int'])),
                            ('lastsent_time', (YLeaf(YType.str, 'lastsent-time'), ['str'])),
                            ('lasrdrop_time', (YLeaf(YType.str, 'lasrdrop-time'), ['str'])),
                        ])
                        self.trap_oid = None
                        self.count = None
                        self.drop_count = None
                        self.retry_count = None
                        self.lastsent_time = None
                        self.lasrdrop_time = None
                        self._segment_path = lambda: "trap-oi-dinfo"
                        self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/trap-infos/trap-info/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.Information.TrapInfos.TrapInfo.TrapOiDinfo, ['trap_oid', 'count', 'drop_count', 'retry_count', 'lastsent_time', 'lasrdrop_time'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                        return meta._meta_table['Snmp.Information.TrapInfos.TrapInfo.TrapOiDinfo']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.Information.TrapInfos.TrapInfo']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.TrapInfos']['meta_info']


        class PollOids(_Entity_):
            """
            OID list for poll PDU
            
            .. attribute:: poll_oid
            
            	PDU drop info for OID
            	**type**\: list of  		 :py:class:`PollOid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.PollOids.PollOid>`
            
            	**config**\: False
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2018-07-20'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Information.PollOids, self).__init__()

                self.yang_name = "poll-oids"
                self.yang_parent_name = "information"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("poll-oid", ("poll_oid", Snmp.Information.PollOids.PollOid))])
                self._leafs = OrderedDict()

                self.poll_oid = YList(self)
                self._segment_path = lambda: "poll-oids"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Information.PollOids, [], name, value)


            class PollOid(_Entity_):
                """
                PDU drop info for OID
                
                .. attribute:: object_id  (key)
                
                	Object ID
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                	**config**\: False
                
                .. attribute:: nms_count
                
                	 Managment station count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: nms
                
                	Network Managment station ipadress
                	**type**\: list of str
                
                	**config**\: False
                
                .. attribute:: request_count
                
                	OID request count for each Managment station 
                	**type**\: list of int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2018-07-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.Information.PollOids.PollOid, self).__init__()

                    self.yang_name = "poll-oid"
                    self.yang_parent_name = "poll-oids"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['object_id']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object_id', (YLeaf(YType.str, 'object-id'), ['str'])),
                        ('nms_count', (YLeaf(YType.uint32, 'nms-count'), ['int'])),
                        ('nms', (YLeafList(YType.str, 'nms'), ['str'])),
                        ('request_count', (YLeafList(YType.uint32, 'request-count'), ['int'])),
                    ])
                    self.object_id = None
                    self.nms_count = None
                    self.nms = []
                    self.request_count = []
                    self._segment_path = lambda: "poll-oid" + "[object-id='" + str(self.object_id) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/poll-oids/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Information.PollOids.PollOid, ['object_id', 'nms_count', 'nms', 'request_count'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.Information.PollOids.PollOid']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.PollOids']['meta_info']


        class InfomDetails(_Entity_):
            """
            SNMP trap OID
            
            .. attribute:: infom_detail
            
            	SNMP Trap infomation like server , port and trapOID
            	**type**\: list of  		 :py:class:`InfomDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.InfomDetails.InfomDetail>`
            
            	**config**\: False
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2018-07-20'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Information.InfomDetails, self).__init__()

                self.yang_name = "infom-details"
                self.yang_parent_name = "information"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("infom-detail", ("infom_detail", Snmp.Information.InfomDetails.InfomDetail))])
                self._leafs = OrderedDict()

                self.infom_detail = YList(self)
                self._segment_path = lambda: "infom-details"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Information.InfomDetails, [], name, value)


            class InfomDetail(_Entity_):
                """
                SNMP Trap infomation like server , port and
                trapOID
                
                .. attribute:: trap_host
                
                	Trap Host
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: port
                
                	Trap port
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                .. attribute:: host
                
                	NMS/Host address
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: port_xr
                
                	udp port number
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                .. attribute:: trap_oid_count
                
                	Total number of OID's sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: trap_oi_dinfo
                
                	Per trap OID statistics
                	**type**\: list of  		 :py:class:`TrapOiDinfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.InfomDetails.InfomDetail.TrapOiDinfo>`
                
                	**config**\: False
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2018-07-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.Information.InfomDetails.InfomDetail, self).__init__()

                    self.yang_name = "infom-detail"
                    self.yang_parent_name = "infom-details"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("trap-oi-dinfo", ("trap_oi_dinfo", Snmp.Information.InfomDetails.InfomDetail.TrapOiDinfo))])
                    self._leafs = OrderedDict([
                        ('trap_host', (YLeaf(YType.str, 'trap-host'), ['str'])),
                        ('port', (YLeaf(YType.uint16, 'port'), ['int'])),
                        ('host', (YLeaf(YType.str, 'host'), ['str'])),
                        ('port_xr', (YLeaf(YType.uint16, 'port-xr'), ['int'])),
                        ('trap_oid_count', (YLeaf(YType.uint32, 'trap-oid-count'), ['int'])),
                    ])
                    self.trap_host = None
                    self.port = None
                    self.host = None
                    self.port_xr = None
                    self.trap_oid_count = None

                    self.trap_oi_dinfo = YList(self)
                    self._segment_path = lambda: "infom-detail"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/infom-details/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Information.InfomDetails.InfomDetail, ['trap_host', 'port', 'host', 'port_xr', 'trap_oid_count'], name, value)


                class TrapOiDinfo(_Entity_):
                    """
                    Per trap OID statistics
                    
                    .. attribute:: trap_oid
                    
                    	TRAP OID
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: count
                    
                    	Number of traps sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: drop_count
                    
                    	Number of Traps Dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: retry_count
                    
                    	Num of times retry
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: lastsent_time
                    
                    	Timestamp of latest successfully sent
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: lasrdrop_time
                    
                    	Timestamp of latest droped
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'snmp-agent-oper'
                    _revision = '2018-07-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Snmp.Information.InfomDetails.InfomDetail.TrapOiDinfo, self).__init__()

                        self.yang_name = "trap-oi-dinfo"
                        self.yang_parent_name = "infom-detail"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('trap_oid', (YLeaf(YType.str, 'trap-oid'), ['str'])),
                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                            ('drop_count', (YLeaf(YType.uint32, 'drop-count'), ['int'])),
                            ('retry_count', (YLeaf(YType.uint32, 'retry-count'), ['int'])),
                            ('lastsent_time', (YLeaf(YType.str, 'lastsent-time'), ['str'])),
                            ('lasrdrop_time', (YLeaf(YType.str, 'lasrdrop-time'), ['str'])),
                        ])
                        self.trap_oid = None
                        self.count = None
                        self.drop_count = None
                        self.retry_count = None
                        self.lastsent_time = None
                        self.lasrdrop_time = None
                        self._segment_path = lambda: "trap-oi-dinfo"
                        self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/infom-details/infom-detail/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.Information.InfomDetails.InfomDetail.TrapOiDinfo, ['trap_oid', 'count', 'drop_count', 'retry_count', 'lastsent_time', 'lasrdrop_time'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                        return meta._meta_table['Snmp.Information.InfomDetails.InfomDetail.TrapOiDinfo']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.Information.InfomDetails.InfomDetail']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.InfomDetails']['meta_info']


        class Statistics(_Entity_):
            """
            SNMP statistics
            
            .. attribute:: packets_received
            
            	snmpInPkts
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: bad_versions_received
            
            	snmpInBadVersions
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: bad_community_names_received
            
            	snmpInBadCommunityNames
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: bad_community_uses_received
            
            	snmpInBadCommunityUses
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: asn_parse_errors_received
            
            	snmpInASNParseErrs
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: silent_drop_count
            
            	snmpSilentDrops
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: proxy_drop_count
            
            	snmpProxyDrops
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: too_big_packet_received
            
            	snmpInTooBigs
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: max_packet_size
            
            	snmp maximum packet size
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: no_such_names_received
            
            	snmpInNoSuchNames
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: bad_values_received
            
            	snmpInBadValues
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: read_only_received
            
            	snmpInReadOnlys
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: total_general_errors
            
            	snmpInGenErrs
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: total_requested_variables
            
            	snmpInTotalReqVars
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: total_set_variables_received
            
            	snmpInTotalSetVars
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: get_requests_received
            
            	snmpInGetRequests
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: get_next_requests_received
            
            	snmpInGetNexts
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: set_requests_received
            
            	snmpInSetRequests
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: get_responses_received
            
            	snmpInGetResponses
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: traps_received
            
            	snmpInTraps
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: total_packets_sent
            
            	snmpOutPkts
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: too_big_packets_sent
            
            	snmpOutTooBigs
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: no_such_names_sent
            
            	snmpOutNoSuchNames
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: bad_values_sent
            
            	snmpOutBadValues
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: general_errors_sent
            
            	snmpOutGenErrs
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: get_requests_sent
            
            	snmpOutGetRequests
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: get_next_request_sent
            
            	snmpOutGetNexts
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: set_requests_sent
            
            	snmpOutSetRequests
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: get_responses_sent
            
            	snmpOutGetResponses
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: traps_sent
            
            	snmpOutTraps
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2018-07-20'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Information.Statistics, self).__init__()

                self.yang_name = "statistics"
                self.yang_parent_name = "information"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('packets_received', (YLeaf(YType.uint32, 'packets-received'), ['int'])),
                    ('bad_versions_received', (YLeaf(YType.uint32, 'bad-versions-received'), ['int'])),
                    ('bad_community_names_received', (YLeaf(YType.uint32, 'bad-community-names-received'), ['int'])),
                    ('bad_community_uses_received', (YLeaf(YType.uint32, 'bad-community-uses-received'), ['int'])),
                    ('asn_parse_errors_received', (YLeaf(YType.uint32, 'asn-parse-errors-received'), ['int'])),
                    ('silent_drop_count', (YLeaf(YType.uint32, 'silent-drop-count'), ['int'])),
                    ('proxy_drop_count', (YLeaf(YType.uint32, 'proxy-drop-count'), ['int'])),
                    ('too_big_packet_received', (YLeaf(YType.uint32, 'too-big-packet-received'), ['int'])),
                    ('max_packet_size', (YLeaf(YType.uint32, 'max-packet-size'), ['int'])),
                    ('no_such_names_received', (YLeaf(YType.uint32, 'no-such-names-received'), ['int'])),
                    ('bad_values_received', (YLeaf(YType.uint32, 'bad-values-received'), ['int'])),
                    ('read_only_received', (YLeaf(YType.uint32, 'read-only-received'), ['int'])),
                    ('total_general_errors', (YLeaf(YType.uint32, 'total-general-errors'), ['int'])),
                    ('total_requested_variables', (YLeaf(YType.uint32, 'total-requested-variables'), ['int'])),
                    ('total_set_variables_received', (YLeaf(YType.uint32, 'total-set-variables-received'), ['int'])),
                    ('get_requests_received', (YLeaf(YType.uint32, 'get-requests-received'), ['int'])),
                    ('get_next_requests_received', (YLeaf(YType.uint32, 'get-next-requests-received'), ['int'])),
                    ('set_requests_received', (YLeaf(YType.uint32, 'set-requests-received'), ['int'])),
                    ('get_responses_received', (YLeaf(YType.uint32, 'get-responses-received'), ['int'])),
                    ('traps_received', (YLeaf(YType.uint32, 'traps-received'), ['int'])),
                    ('total_packets_sent', (YLeaf(YType.uint32, 'total-packets-sent'), ['int'])),
                    ('too_big_packets_sent', (YLeaf(YType.uint32, 'too-big-packets-sent'), ['int'])),
                    ('no_such_names_sent', (YLeaf(YType.uint32, 'no-such-names-sent'), ['int'])),
                    ('bad_values_sent', (YLeaf(YType.uint32, 'bad-values-sent'), ['int'])),
                    ('general_errors_sent', (YLeaf(YType.uint32, 'general-errors-sent'), ['int'])),
                    ('get_requests_sent', (YLeaf(YType.uint32, 'get-requests-sent'), ['int'])),
                    ('get_next_request_sent', (YLeaf(YType.uint32, 'get-next-request-sent'), ['int'])),
                    ('set_requests_sent', (YLeaf(YType.uint32, 'set-requests-sent'), ['int'])),
                    ('get_responses_sent', (YLeaf(YType.uint32, 'get-responses-sent'), ['int'])),
                    ('traps_sent', (YLeaf(YType.uint32, 'traps-sent'), ['int'])),
                ])
                self.packets_received = None
                self.bad_versions_received = None
                self.bad_community_names_received = None
                self.bad_community_uses_received = None
                self.asn_parse_errors_received = None
                self.silent_drop_count = None
                self.proxy_drop_count = None
                self.too_big_packet_received = None
                self.max_packet_size = None
                self.no_such_names_received = None
                self.bad_values_received = None
                self.read_only_received = None
                self.total_general_errors = None
                self.total_requested_variables = None
                self.total_set_variables_received = None
                self.get_requests_received = None
                self.get_next_requests_received = None
                self.set_requests_received = None
                self.get_responses_received = None
                self.traps_received = None
                self.total_packets_sent = None
                self.too_big_packets_sent = None
                self.no_such_names_sent = None
                self.bad_values_sent = None
                self.general_errors_sent = None
                self.get_requests_sent = None
                self.get_next_request_sent = None
                self.set_requests_sent = None
                self.get_responses_sent = None
                self.traps_sent = None
                self._segment_path = lambda: "statistics"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Information.Statistics, ['packets_received', 'bad_versions_received', 'bad_community_names_received', 'bad_community_uses_received', 'asn_parse_errors_received', 'silent_drop_count', 'proxy_drop_count', 'too_big_packet_received', 'max_packet_size', 'no_such_names_received', 'bad_values_received', 'read_only_received', 'total_general_errors', 'total_requested_variables', 'total_set_variables_received', 'get_requests_received', 'get_next_requests_received', 'set_requests_received', 'get_responses_received', 'traps_received', 'total_packets_sent', 'too_big_packets_sent', 'no_such_names_sent', 'bad_values_sent', 'general_errors_sent', 'get_requests_sent', 'get_next_request_sent', 'set_requests_sent', 'get_responses_sent', 'traps_sent'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.Statistics']['meta_info']


        class IncomingQueue(_Entity_):
            """
            Incoming queue details 
            
            .. attribute:: queue_count
            
            	Number of NMS Queues Exist
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: inq_entry
            
            	Each Entry Details
            	**type**\: list of  		 :py:class:`InqEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.IncomingQueue.InqEntry>`
            
            	**config**\: False
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2018-07-20'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Information.IncomingQueue, self).__init__()

                self.yang_name = "incoming-queue"
                self.yang_parent_name = "information"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("inq-entry", ("inq_entry", Snmp.Information.IncomingQueue.InqEntry))])
                self._leafs = OrderedDict([
                    ('queue_count', (YLeaf(YType.uint32, 'queue-count'), ['int'])),
                ])
                self.queue_count = None

                self.inq_entry = YList(self)
                self._segment_path = lambda: "incoming-queue"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Information.IncomingQueue, ['queue_count'], name, value)


            class InqEntry(_Entity_):
                """
                Each Entry Details.
                
                .. attribute:: address_of_queue
                
                	Address of NMS Q
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: request_count
                
                	Request Count of Each Queue
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: processed_request_count
                
                	Processed request Count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: last_access_time
                
                	Last Access time of Each Queue
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: priority
                
                	Priority of Each Queue
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2018-07-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.Information.IncomingQueue.InqEntry, self).__init__()

                    self.yang_name = "inq-entry"
                    self.yang_parent_name = "incoming-queue"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('address_of_queue', (YLeaf(YType.str, 'address-of-queue'), ['str'])),
                        ('request_count', (YLeaf(YType.uint32, 'request-count'), ['int'])),
                        ('processed_request_count', (YLeaf(YType.uint32, 'processed-request-count'), ['int'])),
                        ('last_access_time', (YLeaf(YType.str, 'last-access-time'), ['str'])),
                        ('priority', (YLeaf(YType.uint8, 'priority'), ['int'])),
                    ])
                    self.address_of_queue = None
                    self.request_count = None
                    self.processed_request_count = None
                    self.last_access_time = None
                    self.priority = None
                    self._segment_path = lambda: "inq-entry"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/incoming-queue/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Information.IncomingQueue.InqEntry, ['address_of_queue', 'request_count', 'processed_request_count', 'last_access_time', 'priority'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.Information.IncomingQueue.InqEntry']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.IncomingQueue']['meta_info']


        class ContextMapping(_Entity_):
            """
            Context name, features name, topology name,
            instance
            
            .. attribute:: contex_mapping
            
            	Context Mapping
            	**type**\: list of  		 :py:class:`ContexMapping <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.ContextMapping.ContexMapping>`
            
            	**config**\: False
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2018-07-20'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Information.ContextMapping, self).__init__()

                self.yang_name = "context-mapping"
                self.yang_parent_name = "information"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("contex-mapping", ("contex_mapping", Snmp.Information.ContextMapping.ContexMapping))])
                self._leafs = OrderedDict()

                self.contex_mapping = YList(self)
                self._segment_path = lambda: "context-mapping"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Information.ContextMapping, [], name, value)


            class ContexMapping(_Entity_):
                """
                Context Mapping
                
                .. attribute:: context
                
                	Context name
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: feature_name
                
                	Feature name
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: instance
                
                	Instance name
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: topology
                
                	Topology name
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: feature
                
                	Feature
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2018-07-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.Information.ContextMapping.ContexMapping, self).__init__()

                    self.yang_name = "contex-mapping"
                    self.yang_parent_name = "context-mapping"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('context', (YLeaf(YType.str, 'context'), ['str'])),
                        ('feature_name', (YLeaf(YType.str, 'feature-name'), ['str'])),
                        ('instance', (YLeaf(YType.str, 'instance'), ['str'])),
                        ('topology', (YLeaf(YType.str, 'topology'), ['str'])),
                        ('feature', (YLeaf(YType.str, 'feature'), ['str'])),
                    ])
                    self.context = None
                    self.feature_name = None
                    self.instance = None
                    self.topology = None
                    self.feature = None
                    self._segment_path = lambda: "contex-mapping"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/context-mapping/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Information.ContextMapping.ContexMapping, ['context', 'feature_name', 'instance', 'topology', 'feature'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.Information.ContextMapping.ContexMapping']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.ContextMapping']['meta_info']


        class TrapOids(_Entity_):
            """
            SNMP trap OID
            
            .. attribute:: trap_oid
            
            	SNMP trap 
            	**type**\: list of  		 :py:class:`TrapOid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.TrapOids.TrapOid>`
            
            	**config**\: False
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2018-07-20'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Information.TrapOids, self).__init__()

                self.yang_name = "trap-oids"
                self.yang_parent_name = "information"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("trap-oid", ("trap_oid", Snmp.Information.TrapOids.TrapOid))])
                self._leafs = OrderedDict()

                self.trap_oid = YList(self)
                self._segment_path = lambda: "trap-oids"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Information.TrapOids, [], name, value)


            class TrapOid(_Entity_):
                """
                SNMP trap 
                
                .. attribute:: trap_oid  (key)
                
                	Trap object ID
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                	**config**\: False
                
                .. attribute:: trap_oid_count
                
                	Total number of OID's sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: trap_oid_xr
                
                	TRAP OID
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2018-07-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.Information.TrapOids.TrapOid, self).__init__()

                    self.yang_name = "trap-oid"
                    self.yang_parent_name = "trap-oids"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['trap_oid']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('trap_oid', (YLeaf(YType.str, 'trap-oid'), ['str'])),
                        ('trap_oid_count', (YLeaf(YType.uint32, 'trap-oid-count'), ['int'])),
                        ('trap_oid_xr', (YLeaf(YType.str, 'trap-oid-xr'), ['str'])),
                    ])
                    self.trap_oid = None
                    self.trap_oid_count = None
                    self.trap_oid_xr = None
                    self._segment_path = lambda: "trap-oid" + "[trap-oid='" + str(self.trap_oid) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/trap-oids/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Information.TrapOids.TrapOid, ['trap_oid', 'trap_oid_count', 'trap_oid_xr'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.Information.TrapOids.TrapOid']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.TrapOids']['meta_info']


        class NmSpackets(_Entity_):
            """
            SNMP overload statistics 
            
            .. attribute:: nm_spacket
            
            	NMS packet drop count
            	**type**\: list of  		 :py:class:`NmSpacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.NmSpackets.NmSpacket>`
            
            	**config**\: False
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2018-07-20'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Information.NmSpackets, self).__init__()

                self.yang_name = "nm-spackets"
                self.yang_parent_name = "information"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("nm-spacket", ("nm_spacket", Snmp.Information.NmSpackets.NmSpacket))])
                self._leafs = OrderedDict()

                self.nm_spacket = YList(self)
                self._segment_path = lambda: "nm-spackets"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Information.NmSpackets, [], name, value)


            class NmSpacket(_Entity_):
                """
                NMS packet drop count
                
                .. attribute:: packetcount  (key)
                
                	NMS packet drop count
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                	**config**\: False
                
                .. attribute:: number_of_nmsq_pkts_dropped
                
                	Number of packets which are currently enqueued within the NMS queues
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: number_of_pkts_dropped
                
                	Number of packets dropped
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: overload_start_time
                
                	Time of overload contol begin
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: overload_end_time
                
                	Time of overload contol End
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2018-07-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.Information.NmSpackets.NmSpacket, self).__init__()

                    self.yang_name = "nm-spacket"
                    self.yang_parent_name = "nm-spackets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['packetcount']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('packetcount', (YLeaf(YType.str, 'packetcount'), ['str'])),
                        ('number_of_nmsq_pkts_dropped', (YLeaf(YType.uint32, 'number-of-nmsq-pkts-dropped'), ['int'])),
                        ('number_of_pkts_dropped', (YLeaf(YType.uint32, 'number-of-pkts-dropped'), ['int'])),
                        ('overload_start_time', (YLeaf(YType.str, 'overload-start-time'), ['str'])),
                        ('overload_end_time', (YLeaf(YType.str, 'overload-end-time'), ['str'])),
                    ])
                    self.packetcount = None
                    self.number_of_nmsq_pkts_dropped = None
                    self.number_of_pkts_dropped = None
                    self.overload_start_time = None
                    self.overload_end_time = None
                    self._segment_path = lambda: "nm-spacket" + "[packetcount='" + str(self.packetcount) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/nm-spackets/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Information.NmSpackets.NmSpacket, ['packetcount', 'number_of_nmsq_pkts_dropped', 'number_of_pkts_dropped', 'overload_start_time', 'overload_end_time'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.Information.NmSpackets.NmSpacket']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.NmSpackets']['meta_info']


        class Mibs(_Entity_):
            """
            List of MIBS supported on the system
            
            .. attribute:: mib
            
            	SNMP MIB Name
            	**type**\: list of  		 :py:class:`Mib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Mibs.Mib>`
            
            	**config**\: False
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2018-07-20'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Information.Mibs, self).__init__()

                self.yang_name = "mibs"
                self.yang_parent_name = "information"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("mib", ("mib", Snmp.Information.Mibs.Mib))])
                self._leafs = OrderedDict()

                self.mib = YList(self)
                self._segment_path = lambda: "mibs"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Information.Mibs, [], name, value)


            class Mib(_Entity_):
                """
                SNMP MIB Name
                
                .. attribute:: name  (key)
                
                	MIB Name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                	**config**\: False
                
                .. attribute:: oids
                
                	List of OIDs per MIB
                	**type**\:  :py:class:`Oids <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Mibs.Mib.Oids>`
                
                	**config**\: False
                
                .. attribute:: mib_information
                
                	MIB state and information
                	**type**\:  :py:class:`MibInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Mibs.Mib.MibInformation>`
                
                	**config**\: False
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2018-07-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.Information.Mibs.Mib, self).__init__()

                    self.yang_name = "mib"
                    self.yang_parent_name = "mibs"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['name']
                    self._child_classes = OrderedDict([("oids", ("oids", Snmp.Information.Mibs.Mib.Oids)), ("mib-information", ("mib_information", Snmp.Information.Mibs.Mib.MibInformation))])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ])
                    self.name = None

                    self.oids = Snmp.Information.Mibs.Mib.Oids()
                    self.oids.parent = self
                    self._children_name_map["oids"] = "oids"

                    self.mib_information = Snmp.Information.Mibs.Mib.MibInformation()
                    self.mib_information.parent = self
                    self._children_name_map["mib_information"] = "mib-information"
                    self._segment_path = lambda: "mib" + "[name='" + str(self.name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/mibs/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Information.Mibs.Mib, ['name'], name, value)


                class Oids(_Entity_):
                    """
                    List of OIDs per MIB
                    
                    .. attribute:: oid
                    
                    	Object identifiers of a mib
                    	**type**\: list of  		 :py:class:`Oid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Mibs.Mib.Oids.Oid>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'snmp-agent-oper'
                    _revision = '2018-07-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Snmp.Information.Mibs.Mib.Oids, self).__init__()

                        self.yang_name = "oids"
                        self.yang_parent_name = "mib"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("oid", ("oid", Snmp.Information.Mibs.Mib.Oids.Oid))])
                        self._leafs = OrderedDict()

                        self.oid = YList(self)
                        self._segment_path = lambda: "oids"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.Information.Mibs.Mib.Oids, [], name, value)


                    class Oid(_Entity_):
                        """
                        Object identifiers of a mib
                        
                        .. attribute:: oid  (key)
                        
                        	Object Identifier
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: oid_name
                        
                        	MIB OID Name
                        	**type**\: str
                        
                        	**mandatory**\: True
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'snmp-agent-oper'
                        _revision = '2018-07-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Snmp.Information.Mibs.Mib.Oids.Oid, self).__init__()

                            self.yang_name = "oid"
                            self.yang_parent_name = "oids"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['oid']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('oid', (YLeaf(YType.str, 'oid'), ['str'])),
                                ('oid_name', (YLeaf(YType.str, 'oid-name'), ['str'])),
                            ])
                            self.oid = None
                            self.oid_name = None
                            self._segment_path = lambda: "oid" + "[oid='" + str(self.oid) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Snmp.Information.Mibs.Mib.Oids.Oid, ['oid', 'oid_name'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                            return meta._meta_table['Snmp.Information.Mibs.Mib.Oids.Oid']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                        return meta._meta_table['Snmp.Information.Mibs.Mib.Oids']['meta_info']


                class MibInformation(_Entity_):
                    """
                    MIB state and information
                    
                    .. attribute:: mib_name
                    
                    	Name of the MIB module
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: dll_name
                    
                    	MIB DLL filename, non\-DLL MIBs will have no value
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: mib_config_filename
                    
                    	MIB config filename, non\-DLL MIBs will have no value
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: is_mib_loaded
                    
                    	TRUE if MIB DLL is currently loaded, will always be TRUE for non\-DLL MIBs
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: dll_capabilities
                    
                    	DLL capabilities
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: trap_strings
                    
                    	List of trapstring configured
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: timeout
                    
                    	TRUE is mib is in phase 1 timeout
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: load_time
                    
                    	Load time
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'snmp-agent-oper'
                    _revision = '2018-07-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Snmp.Information.Mibs.Mib.MibInformation, self).__init__()

                        self.yang_name = "mib-information"
                        self.yang_parent_name = "mib"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('mib_name', (YLeaf(YType.str, 'mib-name'), ['str'])),
                            ('dll_name', (YLeaf(YType.str, 'dll-name'), ['str'])),
                            ('mib_config_filename', (YLeaf(YType.str, 'mib-config-filename'), ['str'])),
                            ('is_mib_loaded', (YLeaf(YType.boolean, 'is-mib-loaded'), ['bool'])),
                            ('dll_capabilities', (YLeaf(YType.uint32, 'dll-capabilities'), ['int'])),
                            ('trap_strings', (YLeaf(YType.str, 'trap-strings'), ['str'])),
                            ('timeout', (YLeaf(YType.boolean, 'timeout'), ['bool'])),
                            ('load_time', (YLeaf(YType.uint32, 'load-time'), ['int'])),
                        ])
                        self.mib_name = None
                        self.dll_name = None
                        self.mib_config_filename = None
                        self.is_mib_loaded = None
                        self.dll_capabilities = None
                        self.trap_strings = None
                        self.timeout = None
                        self.load_time = None
                        self._segment_path = lambda: "mib-information"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.Information.Mibs.Mib.MibInformation, ['mib_name', 'dll_name', 'mib_config_filename', 'is_mib_loaded', 'dll_capabilities', 'trap_strings', 'timeout', 'load_time'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                        return meta._meta_table['Snmp.Information.Mibs.Mib.MibInformation']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.Information.Mibs.Mib']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.Mibs']['meta_info']


        class SerialNumbers(_Entity_):
            """
            SNMP statistics pdu 
            
            .. attribute:: serial_number
            
            	Serial number
            	**type**\: list of  		 :py:class:`SerialNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.SerialNumbers.SerialNumber>`
            
            	**config**\: False
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2018-07-20'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Information.SerialNumbers, self).__init__()

                self.yang_name = "serial-numbers"
                self.yang_parent_name = "information"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("serial-number", ("serial_number", Snmp.Information.SerialNumbers.SerialNumber))])
                self._leafs = OrderedDict()

                self.serial_number = YList(self)
                self._segment_path = lambda: "serial-numbers"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Information.SerialNumbers, [], name, value)


            class SerialNumber(_Entity_):
                """
                Serial number
                
                .. attribute:: number
                
                	Serial number
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                	**config**\: False
                
                .. attribute:: req_id
                
                	Request ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: port
                
                	Port
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                .. attribute:: nms
                
                	 NMS address Rx PDU
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: request_id
                
                	 SNMP request id per PDU
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: port_xr
                
                	NMS port number
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                .. attribute:: pdu_type
                
                	 PDU type
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                .. attribute:: error_status
                
                	Is reques dropped due to error
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                .. attribute:: serial_num
                
                	Serial number per PDU processing
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: input_q
                
                	Request inserted into input queue
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: output_q
                
                	De\-queue the request from the input queue
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: pending_q
                
                	Enqueue the request into pending queue
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: response_out
                
                	Response sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2018-07-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.Information.SerialNumbers.SerialNumber, self).__init__()

                    self.yang_name = "serial-number"
                    self.yang_parent_name = "serial-numbers"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('number', (YLeaf(YType.str, 'number'), ['str'])),
                        ('req_id', (YLeaf(YType.uint32, 'req-id'), ['int'])),
                        ('port', (YLeaf(YType.uint16, 'port'), ['int'])),
                        ('nms', (YLeaf(YType.str, 'nms'), ['str'])),
                        ('request_id', (YLeaf(YType.uint32, 'request-id'), ['int'])),
                        ('port_xr', (YLeaf(YType.uint16, 'port-xr'), ['int'])),
                        ('pdu_type', (YLeaf(YType.uint16, 'pdu-type'), ['int'])),
                        ('error_status', (YLeaf(YType.uint16, 'error-status'), ['int'])),
                        ('serial_num', (YLeaf(YType.uint32, 'serial-num'), ['int'])),
                        ('input_q', (YLeaf(YType.str, 'input-q'), ['str'])),
                        ('output_q', (YLeaf(YType.uint32, 'output-q'), ['int'])),
                        ('pending_q', (YLeaf(YType.uint32, 'pending-q'), ['int'])),
                        ('response_out', (YLeaf(YType.uint32, 'response-out'), ['int'])),
                    ])
                    self.number = None
                    self.req_id = None
                    self.port = None
                    self.nms = None
                    self.request_id = None
                    self.port_xr = None
                    self.pdu_type = None
                    self.error_status = None
                    self.serial_num = None
                    self.input_q = None
                    self.output_q = None
                    self.pending_q = None
                    self.response_out = None
                    self._segment_path = lambda: "serial-number"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/serial-numbers/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Information.SerialNumbers.SerialNumber, ['number', 'req_id', 'port', 'nms', 'request_id', 'port_xr', 'pdu_type', 'error_status', 'serial_num', 'input_q', 'output_q', 'pending_q', 'response_out'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.Information.SerialNumbers.SerialNumber']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.SerialNumbers']['meta_info']


        class DropNmsAddresses(_Entity_):
            """
            NMS list for drop PDU
            
            .. attribute:: drop_nms_address
            
            	PDU drop info for NMS
            	**type**\: list of  		 :py:class:`DropNmsAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.DropNmsAddresses.DropNmsAddress>`
            
            	**config**\: False
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2018-07-20'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Information.DropNmsAddresses, self).__init__()

                self.yang_name = "drop-nms-addresses"
                self.yang_parent_name = "information"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("drop-nms-address", ("drop_nms_address", Snmp.Information.DropNmsAddresses.DropNmsAddress))])
                self._leafs = OrderedDict()

                self.drop_nms_address = YList(self)
                self._segment_path = lambda: "drop-nms-addresses"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Information.DropNmsAddresses, [], name, value)


            class DropNmsAddress(_Entity_):
                """
                PDU drop info for NMS
                
                .. attribute:: nms_addr  (key)
                
                	NMS address
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                	**config**\: False
                
                .. attribute:: nms_address
                
                	NMS address of server
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: incoming_q_count
                
                	Drop Count at Incoming Q
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: threshold_incoming_q_count
                
                	Drop Count at Incoming Q after threshold limit
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: encode_count
                
                	Drop Count with Encode errors
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: duplicate_count
                
                	Duplicate request drop count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: stack_count
                
                	Drop Count at snmp Stack
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: aipc_count
                
                	drop count with AIPC Buffer Full
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: overload_count
                
                	Drop Count with overload notification
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: timeout_count
                
                	Drop count with timeout
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: internal_count
                
                	 drop with Internal Errors
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2018-07-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.Information.DropNmsAddresses.DropNmsAddress, self).__init__()

                    self.yang_name = "drop-nms-address"
                    self.yang_parent_name = "drop-nms-addresses"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['nms_addr']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('nms_addr', (YLeaf(YType.str, 'nms-addr'), ['str'])),
                        ('nms_address', (YLeaf(YType.str, 'nms-address'), ['str'])),
                        ('incoming_q_count', (YLeaf(YType.uint32, 'incoming-q-count'), ['int'])),
                        ('threshold_incoming_q_count', (YLeaf(YType.uint32, 'threshold-incoming-q-count'), ['int'])),
                        ('encode_count', (YLeaf(YType.uint32, 'encode-count'), ['int'])),
                        ('duplicate_count', (YLeaf(YType.uint32, 'duplicate-count'), ['int'])),
                        ('stack_count', (YLeaf(YType.uint32, 'stack-count'), ['int'])),
                        ('aipc_count', (YLeaf(YType.uint32, 'aipc-count'), ['int'])),
                        ('overload_count', (YLeaf(YType.uint32, 'overload-count'), ['int'])),
                        ('timeout_count', (YLeaf(YType.uint32, 'timeout-count'), ['int'])),
                        ('internal_count', (YLeaf(YType.uint32, 'internal-count'), ['int'])),
                    ])
                    self.nms_addr = None
                    self.nms_address = None
                    self.incoming_q_count = None
                    self.threshold_incoming_q_count = None
                    self.encode_count = None
                    self.duplicate_count = None
                    self.stack_count = None
                    self.aipc_count = None
                    self.overload_count = None
                    self.timeout_count = None
                    self.internal_count = None
                    self._segment_path = lambda: "drop-nms-address" + "[nms-addr='" + str(self.nms_addr) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/drop-nms-addresses/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Information.DropNmsAddresses.DropNmsAddress, ['nms_addr', 'nms_address', 'incoming_q_count', 'threshold_incoming_q_count', 'encode_count', 'duplicate_count', 'stack_count', 'aipc_count', 'overload_count', 'timeout_count', 'internal_count'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.Information.DropNmsAddresses.DropNmsAddress']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.DropNmsAddresses']['meta_info']


        class Views(_Entity_):
            """
            SNMP view information
            
            .. attribute:: view
            
            	SNMP target view name
            	**type**\: list of  		 :py:class:`View <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Views.View>`
            
            	**config**\: False
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2018-07-20'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Information.Views, self).__init__()

                self.yang_name = "views"
                self.yang_parent_name = "information"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("view", ("view", Snmp.Information.Views.View))])
                self._leafs = OrderedDict()

                self.view = YList(self)
                self._segment_path = lambda: "views"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Information.Views, [], name, value)


            class View(_Entity_):
                """
                SNMP target view name
                
                .. attribute:: name  (key)
                
                	View name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                	**config**\: False
                
                .. attribute:: view_information
                
                	View name ,familytype, storagetype and status
                	**type**\: list of  		 :py:class:`ViewInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Views.View.ViewInformation>`
                
                	**config**\: False
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2018-07-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.Information.Views.View, self).__init__()

                    self.yang_name = "view"
                    self.yang_parent_name = "views"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['name']
                    self._child_classes = OrderedDict([("view-information", ("view_information", Snmp.Information.Views.View.ViewInformation))])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ])
                    self.name = None

                    self.view_information = YList(self)
                    self._segment_path = lambda: "view" + "[name='" + str(self.name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/views/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Information.Views.View, ['name'], name, value)


                class ViewInformation(_Entity_):
                    """
                    View name ,familytype, storagetype and status
                    
                    .. attribute:: object_id  (key)
                    
                    	SNMP view OID
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    	**config**\: False
                    
                    .. attribute:: snmp_view_family_type
                    
                    	Include or exclude
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: snmp_view_family_storage_type
                    
                    	Storage type
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: snmp_view_family_status
                    
                    	Status of this entry
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'snmp-agent-oper'
                    _revision = '2018-07-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Snmp.Information.Views.View.ViewInformation, self).__init__()

                        self.yang_name = "view-information"
                        self.yang_parent_name = "view"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['object_id']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('object_id', (YLeaf(YType.str, 'object-id'), ['str'])),
                            ('snmp_view_family_type', (YLeaf(YType.str, 'snmp-view-family-type'), ['str'])),
                            ('snmp_view_family_storage_type', (YLeaf(YType.str, 'snmp-view-family-storage-type'), ['str'])),
                            ('snmp_view_family_status', (YLeaf(YType.str, 'snmp-view-family-status'), ['str'])),
                        ])
                        self.object_id = None
                        self.snmp_view_family_type = None
                        self.snmp_view_family_storage_type = None
                        self.snmp_view_family_status = None
                        self._segment_path = lambda: "view-information" + "[object-id='" + str(self.object_id) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.Information.Views.View.ViewInformation, ['object_id', 'snmp_view_family_type', 'snmp_view_family_storage_type', 'snmp_view_family_status'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                        return meta._meta_table['Snmp.Information.Views.View.ViewInformation']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.Information.Views.View']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.Views']['meta_info']


        class SystemDescr(_Entity_):
            """
            System description
            
            .. attribute:: sys_descr
            
            	sysDescr  1.3.6.1.2.1.1.1
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2018-07-20'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Information.SystemDescr, self).__init__()

                self.yang_name = "system-descr"
                self.yang_parent_name = "information"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('sys_descr', (YLeaf(YType.str, 'sys-descr'), ['str'])),
                ])
                self.sys_descr = None
                self._segment_path = lambda: "system-descr"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Information.SystemDescr, ['sys_descr'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.SystemDescr']['meta_info']


        class Tables(_Entity_):
            """
            List of table
            
            .. attribute:: groups
            
            	List of vacmAccessTable
            	**type**\:  :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Tables.Groups>`
            
            	**config**\: False
            
            .. attribute:: user_engine_ids
            
            	List of User
            	**type**\:  :py:class:`UserEngineIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Tables.UserEngineIds>`
            
            	**config**\: False
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2018-07-20'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Information.Tables, self).__init__()

                self.yang_name = "tables"
                self.yang_parent_name = "information"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("groups", ("groups", Snmp.Information.Tables.Groups)), ("user-engine-ids", ("user_engine_ids", Snmp.Information.Tables.UserEngineIds))])
                self._leafs = OrderedDict()

                self.groups = Snmp.Information.Tables.Groups()
                self.groups.parent = self
                self._children_name_map["groups"] = "groups"

                self.user_engine_ids = Snmp.Information.Tables.UserEngineIds()
                self.user_engine_ids.parent = self
                self._children_name_map["user_engine_ids"] = "user-engine-ids"
                self._segment_path = lambda: "tables"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Information.Tables, [], name, value)


            class Groups(_Entity_):
                """
                List of vacmAccessTable
                
                .. attribute:: group
                
                	SNMP group name
                	**type**\: list of  		 :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Tables.Groups.Group>`
                
                	**config**\: False
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2018-07-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.Information.Tables.Groups, self).__init__()

                    self.yang_name = "groups"
                    self.yang_parent_name = "tables"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("group", ("group", Snmp.Information.Tables.Groups.Group))])
                    self._leafs = OrderedDict()

                    self.group = YList(self)
                    self._segment_path = lambda: "groups"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/tables/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Information.Tables.Groups, [], name, value)


                class Group(_Entity_):
                    """
                    SNMP group name
                    
                    .. attribute:: name  (key)
                    
                    	Group Name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    	**config**\: False
                    
                    .. attribute:: group_informations
                    
                    	Group Model
                    	**type**\:  :py:class:`GroupInformations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Tables.Groups.Group.GroupInformations>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'snmp-agent-oper'
                    _revision = '2018-07-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Snmp.Information.Tables.Groups.Group, self).__init__()

                        self.yang_name = "group"
                        self.yang_parent_name = "groups"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['name']
                        self._child_classes = OrderedDict([("group-informations", ("group_informations", Snmp.Information.Tables.Groups.Group.GroupInformations))])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ])
                        self.name = None

                        self.group_informations = Snmp.Information.Tables.Groups.Group.GroupInformations()
                        self.group_informations.parent = self
                        self._children_name_map["group_informations"] = "group-informations"
                        self._segment_path = lambda: "group" + "[name='" + str(self.name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/tables/groups/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.Information.Tables.Groups.Group, ['name'], name, value)


                    class GroupInformations(_Entity_):
                        """
                        Group Model
                        
                        .. attribute:: group_information
                        
                        	Group name ,status  and information
                        	**type**\: list of  		 :py:class:`GroupInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Tables.Groups.Group.GroupInformations.GroupInformation>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'snmp-agent-oper'
                        _revision = '2018-07-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Snmp.Information.Tables.Groups.Group.GroupInformations, self).__init__()

                            self.yang_name = "group-informations"
                            self.yang_parent_name = "group"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("group-information", ("group_information", Snmp.Information.Tables.Groups.Group.GroupInformations.GroupInformation))])
                            self._leafs = OrderedDict()

                            self.group_information = YList(self)
                            self._segment_path = lambda: "group-informations"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Snmp.Information.Tables.Groups.Group.GroupInformations, [], name, value)


                        class GroupInformation(_Entity_):
                            """
                            Group name ,status  and information
                            
                            .. attribute:: modelnumber
                            
                            	Model number
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            	**config**\: False
                            
                            .. attribute:: level
                            
                            	Level
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            	**config**\: False
                            
                            .. attribute:: vacm_access_read_view_name
                            
                            	Read view name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: vacm_access_write_view_name
                            
                            	Write view name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: vacm_access_notify_view_name
                            
                            	Notify view name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: vacm_access_status
                            
                            	Status of this view configuration
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'snmp-agent-oper'
                            _revision = '2018-07-20'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Snmp.Information.Tables.Groups.Group.GroupInformations.GroupInformation, self).__init__()

                                self.yang_name = "group-information"
                                self.yang_parent_name = "group-informations"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('modelnumber', (YLeaf(YType.str, 'modelnumber'), ['str'])),
                                    ('level', (YLeaf(YType.str, 'level'), ['str'])),
                                    ('vacm_access_read_view_name', (YLeaf(YType.str, 'vacm-access-read-view-name'), ['str'])),
                                    ('vacm_access_write_view_name', (YLeaf(YType.str, 'vacm-access-write-view-name'), ['str'])),
                                    ('vacm_access_notify_view_name', (YLeaf(YType.str, 'vacm-access-notify-view-name'), ['str'])),
                                    ('vacm_access_status', (YLeaf(YType.uint32, 'vacm-access-status'), ['int'])),
                                ])
                                self.modelnumber = None
                                self.level = None
                                self.vacm_access_read_view_name = None
                                self.vacm_access_write_view_name = None
                                self.vacm_access_notify_view_name = None
                                self.vacm_access_status = None
                                self._segment_path = lambda: "group-information"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Snmp.Information.Tables.Groups.Group.GroupInformations.GroupInformation, ['modelnumber', 'level', 'vacm_access_read_view_name', 'vacm_access_write_view_name', 'vacm_access_notify_view_name', 'vacm_access_status'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                                return meta._meta_table['Snmp.Information.Tables.Groups.Group.GroupInformations.GroupInformation']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                            return meta._meta_table['Snmp.Information.Tables.Groups.Group.GroupInformations']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                        return meta._meta_table['Snmp.Information.Tables.Groups.Group']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.Information.Tables.Groups']['meta_info']


            class UserEngineIds(_Entity_):
                """
                List of User
                
                .. attribute:: user_engine_id
                
                	SNMP engineId
                	**type**\: list of  		 :py:class:`UserEngineId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Tables.UserEngineIds.UserEngineId>`
                
                	**config**\: False
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2018-07-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.Information.Tables.UserEngineIds, self).__init__()

                    self.yang_name = "user-engine-ids"
                    self.yang_parent_name = "tables"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("user-engine-id", ("user_engine_id", Snmp.Information.Tables.UserEngineIds.UserEngineId))])
                    self._leafs = OrderedDict()

                    self.user_engine_id = YList(self)
                    self._segment_path = lambda: "user-engine-ids"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/tables/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Information.Tables.UserEngineIds, [], name, value)


                class UserEngineId(_Entity_):
                    """
                    SNMP engineId
                    
                    .. attribute:: engine_id  (key)
                    
                    	SNMP Engine ID
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    	**config**\: False
                    
                    .. attribute:: user_name
                    
                    	User name ,storage type ,status 
                    	**type**\: list of  		 :py:class:`UserName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Tables.UserEngineIds.UserEngineId.UserName>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'snmp-agent-oper'
                    _revision = '2018-07-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Snmp.Information.Tables.UserEngineIds.UserEngineId, self).__init__()

                        self.yang_name = "user-engine-id"
                        self.yang_parent_name = "user-engine-ids"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['engine_id']
                        self._child_classes = OrderedDict([("user-name", ("user_name", Snmp.Information.Tables.UserEngineIds.UserEngineId.UserName))])
                        self._leafs = OrderedDict([
                            ('engine_id', (YLeaf(YType.str, 'engine-id'), ['str'])),
                        ])
                        self.engine_id = None

                        self.user_name = YList(self)
                        self._segment_path = lambda: "user-engine-id" + "[engine-id='" + str(self.engine_id) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/tables/user-engine-ids/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.Information.Tables.UserEngineIds.UserEngineId, ['engine_id'], name, value)


                    class UserName(_Entity_):
                        """
                        User name ,storage type ,status 
                        
                        .. attribute:: user_name  (key)
                        
                        	User name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        	**config**\: False
                        
                        .. attribute:: usm_user_storage_type
                        
                        	Storage type
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: usm_user_status
                        
                        	Status of this user
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'snmp-agent-oper'
                        _revision = '2018-07-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Snmp.Information.Tables.UserEngineIds.UserEngineId.UserName, self).__init__()

                            self.yang_name = "user-name"
                            self.yang_parent_name = "user-engine-id"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['user_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('user_name', (YLeaf(YType.str, 'user-name'), ['str'])),
                                ('usm_user_storage_type', (YLeaf(YType.uint32, 'usm-user-storage-type'), ['int'])),
                                ('usm_user_status', (YLeaf(YType.uint32, 'usm-user-status'), ['int'])),
                            ])
                            self.user_name = None
                            self.usm_user_storage_type = None
                            self.usm_user_status = None
                            self._segment_path = lambda: "user-name" + "[user-name='" + str(self.user_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Snmp.Information.Tables.UserEngineIds.UserEngineId.UserName, ['user_name', 'usm_user_storage_type', 'usm_user_status'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                            return meta._meta_table['Snmp.Information.Tables.UserEngineIds.UserEngineId.UserName']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                        return meta._meta_table['Snmp.Information.Tables.UserEngineIds.UserEngineId']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.Information.Tables.UserEngineIds']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.Tables']['meta_info']


        class SystemOid(_Entity_):
            """
            System object ID
            
            .. attribute:: sys_obj_id
            
            	sysObjID  1.3.6.1.2.1.1.2
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2018-07-20'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Information.SystemOid, self).__init__()

                self.yang_name = "system-oid"
                self.yang_parent_name = "information"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('sys_obj_id', (YLeaf(YType.str, 'sys-obj-id'), ['str'])),
                ])
                self.sys_obj_id = None
                self._segment_path = lambda: "system-oid"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Information.SystemOid, ['sys_obj_id'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.SystemOid']['meta_info']


        class TrapQueue(_Entity_):
            """
            SNMP trap queue statistics
            
            .. attribute:: trap_min
            
            	trap min
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: trap_avg
            
            	trap avg
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: trap_max
            
            	trap max
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: trap_q
            
            	trap q
            	**type**\: list of  		 :py:class:`TrapQ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.TrapQueue.TrapQ>`
            
            	**config**\: False
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2018-07-20'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Information.TrapQueue, self).__init__()

                self.yang_name = "trap-queue"
                self.yang_parent_name = "information"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("trap-q", ("trap_q", Snmp.Information.TrapQueue.TrapQ))])
                self._leafs = OrderedDict([
                    ('trap_min', (YLeaf(YType.uint32, 'trap-min'), ['int'])),
                    ('trap_avg', (YLeaf(YType.uint32, 'trap-avg'), ['int'])),
                    ('trap_max', (YLeaf(YType.uint32, 'trap-max'), ['int'])),
                ])
                self.trap_min = None
                self.trap_avg = None
                self.trap_max = None

                self.trap_q = YList(self)
                self._segment_path = lambda: "trap-queue"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Information.TrapQueue, ['trap_min', 'trap_avg', 'trap_max'], name, value)


            class TrapQ(_Entity_):
                """
                trap q
                
                .. attribute:: min
                
                	min
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: avg
                
                	avg
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: max
                
                	max
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2018-07-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.Information.TrapQueue.TrapQ, self).__init__()

                    self.yang_name = "trap-q"
                    self.yang_parent_name = "trap-queue"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('min', (YLeaf(YType.uint32, 'min'), ['int'])),
                        ('avg', (YLeaf(YType.uint32, 'avg'), ['int'])),
                        ('max', (YLeaf(YType.uint32, 'max'), ['int'])),
                    ])
                    self.min = None
                    self.avg = None
                    self.max = None
                    self._segment_path = lambda: "trap-q"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/information/trap-queue/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Information.TrapQueue.TrapQ, ['min', 'avg', 'max'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.Information.TrapQueue.TrapQ']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.TrapQueue']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
            return meta._meta_table['Snmp.Information']['meta_info']


    class Interfaces(_Entity_):
        """
        List of interfaces
        
        .. attribute:: interface
        
        	Interface Name
        	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Interfaces.Interface>`
        
        	**config**\: False
        
        

        """

        _prefix = 'snmp-agent-oper'
        _revision = '2018-07-20'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Snmp.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interface", ("interface", Snmp.Interfaces.Interface))])
            self._leafs = OrderedDict()

            self.interface = YList(self)
            self._segment_path = lambda: "interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.Interfaces, [], name, value)


        class Interface(_Entity_):
            """
            Interface Name
            
            .. attribute:: name  (key)
            
            	Interface Name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            	**config**\: False
            
            .. attribute:: interface_index
            
            	Interface Index as used by MIB tables
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**mandatory**\: True
            
            	**config**\: False
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2018-07-20'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ('interface_index', (YLeaf(YType.uint32, 'interface-index'), ['int'])),
                ])
                self.name = None
                self.interface_index = None
                self._segment_path = lambda: "interface" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/interfaces/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Interfaces.Interface, ['name', 'interface_index'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Interfaces.Interface']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
            return meta._meta_table['Snmp.Interfaces']['meta_info']


    class Correlator(_Entity_):
        """
        Trap Correlator operational data
        
        .. attribute:: rule_details
        
        	Table that contains the database of correlation rule details
        	**type**\:  :py:class:`RuleDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Correlator.RuleDetails>`
        
        	**config**\: False
        
        .. attribute:: buffer_status
        
        	Describes buffer utilization and parameters configured
        	**type**\:  :py:class:`BufferStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Correlator.BufferStatus>`
        
        	**config**\: False
        
        .. attribute:: rule_set_details
        
        	Table that contains the ruleset detail info
        	**type**\:  :py:class:`RuleSetDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Correlator.RuleSetDetails>`
        
        	**config**\: False
        
        .. attribute:: traps
        
        	Correlated traps Table
        	**type**\:  :py:class:`Traps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Correlator.Traps>`
        
        	**config**\: False
        
        

        """

        _prefix = 'snmp-agent-oper'
        _revision = '2018-07-20'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Snmp.Correlator, self).__init__()

            self.yang_name = "correlator"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rule-details", ("rule_details", Snmp.Correlator.RuleDetails)), ("buffer-status", ("buffer_status", Snmp.Correlator.BufferStatus)), ("rule-set-details", ("rule_set_details", Snmp.Correlator.RuleSetDetails)), ("traps", ("traps", Snmp.Correlator.Traps))])
            self._leafs = OrderedDict()

            self.rule_details = Snmp.Correlator.RuleDetails()
            self.rule_details.parent = self
            self._children_name_map["rule_details"] = "rule-details"

            self.buffer_status = Snmp.Correlator.BufferStatus()
            self.buffer_status.parent = self
            self._children_name_map["buffer_status"] = "buffer-status"

            self.rule_set_details = Snmp.Correlator.RuleSetDetails()
            self.rule_set_details.parent = self
            self._children_name_map["rule_set_details"] = "rule-set-details"

            self.traps = Snmp.Correlator.Traps()
            self.traps.parent = self
            self._children_name_map["traps"] = "traps"
            self._segment_path = lambda: "correlator"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.Correlator, [], name, value)


        class RuleDetails(_Entity_):
            """
            Table that contains the database of correlation
            rule details
            
            .. attribute:: rule_detail
            
            	Details of one of the correlation rules
            	**type**\: list of  		 :py:class:`RuleDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Correlator.RuleDetails.RuleDetail>`
            
            	**config**\: False
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2018-07-20'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Correlator.RuleDetails, self).__init__()

                self.yang_name = "rule-details"
                self.yang_parent_name = "correlator"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("rule-detail", ("rule_detail", Snmp.Correlator.RuleDetails.RuleDetail))])
                self._leafs = OrderedDict()

                self.rule_detail = YList(self)
                self._segment_path = lambda: "rule-details"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/correlator/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Correlator.RuleDetails, [], name, value)


            class RuleDetail(_Entity_):
                """
                Details of one of the correlation rules
                
                .. attribute:: rule_name  (key)
                
                	Correlation Rule Name
                	**type**\: str
                
                	**length:** 1..32
                
                	**config**\: False
                
                .. attribute:: rule_summary
                
                	Rule summary, name, etc
                	**type**\:  :py:class:`RuleSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Correlator.RuleDetails.RuleDetail.RuleSummary>`
                
                	**config**\: False
                
                .. attribute:: root_cause
                
                	OID/VarBinds defining the rootcause match conditions
                	**type**\:  :py:class:`RootCause <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Correlator.RuleDetails.RuleDetail.RootCause>`
                
                	**config**\: False
                
                .. attribute:: timeout
                
                	Time window (in ms) for which root/all messages are kept in correlater before sending them to hosts
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: non_root_cause
                
                	OIDs/VarBinds defining the nonrootcause match conditions
                	**type**\: list of  		 :py:class:`NonRootCause <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Correlator.RuleDetails.RuleDetail.NonRootCause>`
                
                	**config**\: False
                
                .. attribute:: apply_host
                
                	Hosts (IP/port) to which the rule is applied
                	**type**\: list of  		 :py:class:`ApplyHost <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Correlator.RuleDetails.RuleDetail.ApplyHost>`
                
                	**config**\: False
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2018-07-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.Correlator.RuleDetails.RuleDetail, self).__init__()

                    self.yang_name = "rule-detail"
                    self.yang_parent_name = "rule-details"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['rule_name']
                    self._child_classes = OrderedDict([("rule-summary", ("rule_summary", Snmp.Correlator.RuleDetails.RuleDetail.RuleSummary)), ("root-cause", ("root_cause", Snmp.Correlator.RuleDetails.RuleDetail.RootCause)), ("non-root-cause", ("non_root_cause", Snmp.Correlator.RuleDetails.RuleDetail.NonRootCause)), ("apply-host", ("apply_host", Snmp.Correlator.RuleDetails.RuleDetail.ApplyHost))])
                    self._leafs = OrderedDict([
                        ('rule_name', (YLeaf(YType.str, 'rule-name'), ['str'])),
                        ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                    ])
                    self.rule_name = None
                    self.timeout = None

                    self.rule_summary = Snmp.Correlator.RuleDetails.RuleDetail.RuleSummary()
                    self.rule_summary.parent = self
                    self._children_name_map["rule_summary"] = "rule-summary"

                    self.root_cause = Snmp.Correlator.RuleDetails.RuleDetail.RootCause()
                    self.root_cause.parent = self
                    self._children_name_map["root_cause"] = "root-cause"

                    self.non_root_cause = YList(self)
                    self.apply_host = YList(self)
                    self._segment_path = lambda: "rule-detail" + "[rule-name='" + str(self.rule_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/correlator/rule-details/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Correlator.RuleDetails.RuleDetail, ['rule_name', 'timeout'], name, value)


                class RuleSummary(_Entity_):
                    """
                    Rule summary, name, etc
                    
                    .. attribute:: rule_name
                    
                    	Correlation Rule Name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: rule_state
                    
                    	Applied state of the rule It could be not applied, applied or applied to all
                    	**type**\:  :py:class:`SnmpCorrRuleState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.SnmpCorrRuleState>`
                    
                    	**config**\: False
                    
                    .. attribute:: buffered_traps_count
                    
                    	Number of buffered traps correlated to this rule
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'snmp-agent-oper'
                    _revision = '2018-07-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Snmp.Correlator.RuleDetails.RuleDetail.RuleSummary, self).__init__()

                        self.yang_name = "rule-summary"
                        self.yang_parent_name = "rule-detail"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('rule_name', (YLeaf(YType.str, 'rule-name'), ['str'])),
                            ('rule_state', (YLeaf(YType.enumeration, 'rule-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'SnmpCorrRuleState', '')])),
                            ('buffered_traps_count', (YLeaf(YType.uint32, 'buffered-traps-count'), ['int'])),
                        ])
                        self.rule_name = None
                        self.rule_state = None
                        self.buffered_traps_count = None
                        self._segment_path = lambda: "rule-summary"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.Correlator.RuleDetails.RuleDetail.RuleSummary, ['rule_name', 'rule_state', 'buffered_traps_count'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                        return meta._meta_table['Snmp.Correlator.RuleDetails.RuleDetail.RuleSummary']['meta_info']


                class RootCause(_Entity_):
                    """
                    OID/VarBinds defining the rootcause match
                    conditions.
                    
                    .. attribute:: oid
                    
                    	OID of the trap
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: var_bind
                    
                    	VarBinds of the trap
                    	**type**\: list of  		 :py:class:`VarBind <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Correlator.RuleDetails.RuleDetail.RootCause.VarBind>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'snmp-agent-oper'
                    _revision = '2018-07-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Snmp.Correlator.RuleDetails.RuleDetail.RootCause, self).__init__()

                        self.yang_name = "root-cause"
                        self.yang_parent_name = "rule-detail"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("var-bind", ("var_bind", Snmp.Correlator.RuleDetails.RuleDetail.RootCause.VarBind))])
                        self._leafs = OrderedDict([
                            ('oid', (YLeaf(YType.str, 'oid'), ['str'])),
                        ])
                        self.oid = None

                        self.var_bind = YList(self)
                        self._segment_path = lambda: "root-cause"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.Correlator.RuleDetails.RuleDetail.RootCause, ['oid'], name, value)


                    class VarBind(_Entity_):
                        """
                        VarBinds of the trap
                        
                        .. attribute:: oid
                        
                        	OID of the varbind
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: match_type
                        
                        	Varbind match type
                        	**type**\:  :py:class:`SnmpCorrVbindMatch <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.SnmpCorrVbindMatch>`
                        
                        	**config**\: False
                        
                        .. attribute:: reg_exp
                        
                        	Regular expression to match
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'snmp-agent-oper'
                        _revision = '2018-07-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Snmp.Correlator.RuleDetails.RuleDetail.RootCause.VarBind, self).__init__()

                            self.yang_name = "var-bind"
                            self.yang_parent_name = "root-cause"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('oid', (YLeaf(YType.str, 'oid'), ['str'])),
                                ('match_type', (YLeaf(YType.enumeration, 'match-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'SnmpCorrVbindMatch', '')])),
                                ('reg_exp', (YLeaf(YType.str, 'reg-exp'), ['str'])),
                            ])
                            self.oid = None
                            self.match_type = None
                            self.reg_exp = None
                            self._segment_path = lambda: "var-bind"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Snmp.Correlator.RuleDetails.RuleDetail.RootCause.VarBind, ['oid', 'match_type', 'reg_exp'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                            return meta._meta_table['Snmp.Correlator.RuleDetails.RuleDetail.RootCause.VarBind']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                        return meta._meta_table['Snmp.Correlator.RuleDetails.RuleDetail.RootCause']['meta_info']


                class NonRootCause(_Entity_):
                    """
                    OIDs/VarBinds defining the nonrootcause match
                    conditions.
                    
                    .. attribute:: oid
                    
                    	OID of the trap
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: var_bind
                    
                    	VarBinds of the trap
                    	**type**\: list of  		 :py:class:`VarBind <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Correlator.RuleDetails.RuleDetail.NonRootCause.VarBind>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'snmp-agent-oper'
                    _revision = '2018-07-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Snmp.Correlator.RuleDetails.RuleDetail.NonRootCause, self).__init__()

                        self.yang_name = "non-root-cause"
                        self.yang_parent_name = "rule-detail"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("var-bind", ("var_bind", Snmp.Correlator.RuleDetails.RuleDetail.NonRootCause.VarBind))])
                        self._leafs = OrderedDict([
                            ('oid', (YLeaf(YType.str, 'oid'), ['str'])),
                        ])
                        self.oid = None

                        self.var_bind = YList(self)
                        self._segment_path = lambda: "non-root-cause"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.Correlator.RuleDetails.RuleDetail.NonRootCause, ['oid'], name, value)


                    class VarBind(_Entity_):
                        """
                        VarBinds of the trap
                        
                        .. attribute:: oid
                        
                        	OID of the varbind
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: match_type
                        
                        	Varbind match type
                        	**type**\:  :py:class:`SnmpCorrVbindMatch <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.SnmpCorrVbindMatch>`
                        
                        	**config**\: False
                        
                        .. attribute:: reg_exp
                        
                        	Regular expression to match
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'snmp-agent-oper'
                        _revision = '2018-07-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Snmp.Correlator.RuleDetails.RuleDetail.NonRootCause.VarBind, self).__init__()

                            self.yang_name = "var-bind"
                            self.yang_parent_name = "non-root-cause"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('oid', (YLeaf(YType.str, 'oid'), ['str'])),
                                ('match_type', (YLeaf(YType.enumeration, 'match-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'SnmpCorrVbindMatch', '')])),
                                ('reg_exp', (YLeaf(YType.str, 'reg-exp'), ['str'])),
                            ])
                            self.oid = None
                            self.match_type = None
                            self.reg_exp = None
                            self._segment_path = lambda: "var-bind"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Snmp.Correlator.RuleDetails.RuleDetail.NonRootCause.VarBind, ['oid', 'match_type', 'reg_exp'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                            return meta._meta_table['Snmp.Correlator.RuleDetails.RuleDetail.NonRootCause.VarBind']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                        return meta._meta_table['Snmp.Correlator.RuleDetails.RuleDetail.NonRootCause']['meta_info']


                class ApplyHost(_Entity_):
                    """
                    Hosts (IP/port) to which the rule is applied
                    
                    .. attribute:: ip_address
                    
                    	IP address of the host
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: port
                    
                    	Port of the host
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'snmp-agent-oper'
                    _revision = '2018-07-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Snmp.Correlator.RuleDetails.RuleDetail.ApplyHost, self).__init__()

                        self.yang_name = "apply-host"
                        self.yang_parent_name = "rule-detail"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str'])),
                            ('port', (YLeaf(YType.uint16, 'port'), ['int'])),
                        ])
                        self.ip_address = None
                        self.port = None
                        self._segment_path = lambda: "apply-host"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.Correlator.RuleDetails.RuleDetail.ApplyHost, ['ip_address', 'port'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                        return meta._meta_table['Snmp.Correlator.RuleDetails.RuleDetail.ApplyHost']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.Correlator.RuleDetails.RuleDetail']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Correlator.RuleDetails']['meta_info']


        class BufferStatus(_Entity_):
            """
            Describes buffer utilization and parameters
            configured
            
            .. attribute:: current_size
            
            	Current buffer usage
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: configured_size
            
            	Configured buffer size
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2018-07-20'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Correlator.BufferStatus, self).__init__()

                self.yang_name = "buffer-status"
                self.yang_parent_name = "correlator"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('current_size', (YLeaf(YType.uint32, 'current-size'), ['int'])),
                    ('configured_size', (YLeaf(YType.uint32, 'configured-size'), ['int'])),
                ])
                self.current_size = None
                self.configured_size = None
                self._segment_path = lambda: "buffer-status"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/correlator/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Correlator.BufferStatus, ['current_size', 'configured_size'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Correlator.BufferStatus']['meta_info']


        class RuleSetDetails(_Entity_):
            """
            Table that contains the ruleset detail info
            
            .. attribute:: rule_set_detail
            
            	Detail of one of the correlation rulesets
            	**type**\: list of  		 :py:class:`RuleSetDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Correlator.RuleSetDetails.RuleSetDetail>`
            
            	**config**\: False
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2018-07-20'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Correlator.RuleSetDetails, self).__init__()

                self.yang_name = "rule-set-details"
                self.yang_parent_name = "correlator"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("rule-set-detail", ("rule_set_detail", Snmp.Correlator.RuleSetDetails.RuleSetDetail))])
                self._leafs = OrderedDict()

                self.rule_set_detail = YList(self)
                self._segment_path = lambda: "rule-set-details"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/correlator/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Correlator.RuleSetDetails, [], name, value)


            class RuleSetDetail(_Entity_):
                """
                Detail of one of the correlation rulesets
                
                .. attribute:: rule_set_name  (key)
                
                	Ruleset Name
                	**type**\: str
                
                	**length:** 1..32
                
                	**config**\: False
                
                .. attribute:: rule_set_name_xr
                
                	Ruleset Name
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: rules
                
                	Rules contained in a ruleset
                	**type**\: list of  		 :py:class:`Rules <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Correlator.RuleSetDetails.RuleSetDetail.Rules>`
                
                	**config**\: False
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2018-07-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.Correlator.RuleSetDetails.RuleSetDetail, self).__init__()

                    self.yang_name = "rule-set-detail"
                    self.yang_parent_name = "rule-set-details"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['rule_set_name']
                    self._child_classes = OrderedDict([("rules", ("rules", Snmp.Correlator.RuleSetDetails.RuleSetDetail.Rules))])
                    self._leafs = OrderedDict([
                        ('rule_set_name', (YLeaf(YType.str, 'rule-set-name'), ['str'])),
                        ('rule_set_name_xr', (YLeaf(YType.str, 'rule-set-name-xr'), ['str'])),
                    ])
                    self.rule_set_name = None
                    self.rule_set_name_xr = None

                    self.rules = YList(self)
                    self._segment_path = lambda: "rule-set-detail" + "[rule-set-name='" + str(self.rule_set_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/correlator/rule-set-details/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Correlator.RuleSetDetails.RuleSetDetail, ['rule_set_name', 'rule_set_name_xr'], name, value)


                class Rules(_Entity_):
                    """
                    Rules contained in a ruleset
                    
                    .. attribute:: rule_name
                    
                    	Correlation Rule Name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: rule_state
                    
                    	Applied state of the rule It could be not applied, applied or applied to all
                    	**type**\:  :py:class:`SnmpCorrRuleState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.SnmpCorrRuleState>`
                    
                    	**config**\: False
                    
                    .. attribute:: buffered_traps_count
                    
                    	Number of buffered traps correlated to this rule
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'snmp-agent-oper'
                    _revision = '2018-07-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Snmp.Correlator.RuleSetDetails.RuleSetDetail.Rules, self).__init__()

                        self.yang_name = "rules"
                        self.yang_parent_name = "rule-set-detail"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('rule_name', (YLeaf(YType.str, 'rule-name'), ['str'])),
                            ('rule_state', (YLeaf(YType.enumeration, 'rule-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'SnmpCorrRuleState', '')])),
                            ('buffered_traps_count', (YLeaf(YType.uint32, 'buffered-traps-count'), ['int'])),
                        ])
                        self.rule_name = None
                        self.rule_state = None
                        self.buffered_traps_count = None
                        self._segment_path = lambda: "rules"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.Correlator.RuleSetDetails.RuleSetDetail.Rules, ['rule_name', 'rule_state', 'buffered_traps_count'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                        return meta._meta_table['Snmp.Correlator.RuleSetDetails.RuleSetDetail.Rules']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.Correlator.RuleSetDetails.RuleSetDetail']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Correlator.RuleSetDetails']['meta_info']


        class Traps(_Entity_):
            """
            Correlated traps Table
            
            .. attribute:: trap
            
            	One of the correlated traps
            	**type**\: list of  		 :py:class:`Trap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Correlator.Traps.Trap>`
            
            	**config**\: False
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2018-07-20'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Correlator.Traps, self).__init__()

                self.yang_name = "traps"
                self.yang_parent_name = "correlator"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("trap", ("trap", Snmp.Correlator.Traps.Trap))])
                self._leafs = OrderedDict()

                self.trap = YList(self)
                self._segment_path = lambda: "traps"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/correlator/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Correlator.Traps, [], name, value)


            class Trap(_Entity_):
                """
                One of the correlated traps
                
                .. attribute:: entry_id  (key)
                
                	Entry ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: trap_info
                
                	Correlated trap information
                	**type**\:  :py:class:`TrapInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Correlator.Traps.Trap.TrapInfo>`
                
                	**config**\: False
                
                .. attribute:: correlation_id
                
                	Correlation ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: is_root_cause
                
                	True if this is the rootcause
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: rule_name
                
                	Correlation rule name
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2018-07-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.Correlator.Traps.Trap, self).__init__()

                    self.yang_name = "trap"
                    self.yang_parent_name = "traps"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['entry_id']
                    self._child_classes = OrderedDict([("trap-info", ("trap_info", Snmp.Correlator.Traps.Trap.TrapInfo))])
                    self._leafs = OrderedDict([
                        ('entry_id', (YLeaf(YType.uint32, 'entry-id'), ['int'])),
                        ('correlation_id', (YLeaf(YType.uint32, 'correlation-id'), ['int'])),
                        ('is_root_cause', (YLeaf(YType.boolean, 'is-root-cause'), ['bool'])),
                        ('rule_name', (YLeaf(YType.str, 'rule-name'), ['str'])),
                    ])
                    self.entry_id = None
                    self.correlation_id = None
                    self.is_root_cause = None
                    self.rule_name = None

                    self.trap_info = Snmp.Correlator.Traps.Trap.TrapInfo()
                    self.trap_info.parent = self
                    self._children_name_map["trap_info"] = "trap-info"
                    self._segment_path = lambda: "trap" + "[entry-id='" + str(self.entry_id) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/correlator/traps/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Correlator.Traps.Trap, ['entry_id', 'correlation_id', 'is_root_cause', 'rule_name'], name, value)


                class TrapInfo(_Entity_):
                    """
                    Correlated trap information
                    
                    .. attribute:: oid
                    
                    	Object ID
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: relative_timestamp
                    
                    	Number of hsecs elapsed since snmpd was started
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: second
                    
                    .. attribute:: timestamp
                    
                    	Time when the trap was generated. It is expressed in number of milliseconds since 00\:00 \:00 UTC, January 1, 1970
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    	**units**\: millisecond
                    
                    .. attribute:: var_bind
                    
                    	VarBinds on the trap
                    	**type**\: list of  		 :py:class:`VarBind <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Correlator.Traps.Trap.TrapInfo.VarBind>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'snmp-agent-oper'
                    _revision = '2018-07-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Snmp.Correlator.Traps.Trap.TrapInfo, self).__init__()

                        self.yang_name = "trap-info"
                        self.yang_parent_name = "trap"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("var-bind", ("var_bind", Snmp.Correlator.Traps.Trap.TrapInfo.VarBind))])
                        self._leafs = OrderedDict([
                            ('oid', (YLeaf(YType.str, 'oid'), ['str'])),
                            ('relative_timestamp', (YLeaf(YType.uint32, 'relative-timestamp'), ['int'])),
                            ('timestamp', (YLeaf(YType.uint64, 'timestamp'), ['int'])),
                        ])
                        self.oid = None
                        self.relative_timestamp = None
                        self.timestamp = None

                        self.var_bind = YList(self)
                        self._segment_path = lambda: "trap-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.Correlator.Traps.Trap.TrapInfo, ['oid', 'relative_timestamp', 'timestamp'], name, value)


                    class VarBind(_Entity_):
                        """
                        VarBinds on the trap
                        
                        .. attribute:: oid
                        
                        	OID of the varbind
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: value
                        
                        	Value of the varbind
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'snmp-agent-oper'
                        _revision = '2018-07-20'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Snmp.Correlator.Traps.Trap.TrapInfo.VarBind, self).__init__()

                            self.yang_name = "var-bind"
                            self.yang_parent_name = "trap-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('oid', (YLeaf(YType.str, 'oid'), ['str'])),
                                ('value', (YLeaf(YType.str, 'value'), ['str'])),
                            ])
                            self.oid = None
                            self.value = None
                            self._segment_path = lambda: "var-bind"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Snmp.Correlator.Traps.Trap.TrapInfo.VarBind, ['oid', 'value'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                            return meta._meta_table['Snmp.Correlator.Traps.Trap.TrapInfo.VarBind']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                        return meta._meta_table['Snmp.Correlator.Traps.Trap.TrapInfo']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.Correlator.Traps.Trap']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Correlator.Traps']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
            return meta._meta_table['Snmp.Correlator']['meta_info']


    class InterfaceIndexes(_Entity_):
        """
        List of index
        
        .. attribute:: interface_index
        
        	Interface Index
        	**type**\: list of  		 :py:class:`InterfaceIndex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.InterfaceIndexes.InterfaceIndex>`
        
        	**config**\: False
        
        

        """

        _prefix = 'snmp-agent-oper'
        _revision = '2018-07-20'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Snmp.InterfaceIndexes, self).__init__()

            self.yang_name = "interface-indexes"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interface-index", ("interface_index", Snmp.InterfaceIndexes.InterfaceIndex))])
            self._leafs = OrderedDict()

            self.interface_index = YList(self)
            self._segment_path = lambda: "interface-indexes"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.InterfaceIndexes, [], name, value)


        class InterfaceIndex(_Entity_):
            """
            Interface Index
            
            .. attribute:: interface_index  (key)
            
            	Interface Index as used by MIB tables
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: interface_name
            
            	Interface Name
            	**type**\: str
            
            	**mandatory**\: True
            
            	**config**\: False
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2018-07-20'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.InterfaceIndexes.InterfaceIndex, self).__init__()

                self.yang_name = "interface-index"
                self.yang_parent_name = "interface-indexes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['interface_index']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('interface_index', (YLeaf(YType.uint32, 'interface-index'), ['int'])),
                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                ])
                self.interface_index = None
                self.interface_name = None
                self._segment_path = lambda: "interface-index" + "[interface-index='" + str(self.interface_index) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/interface-indexes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.InterfaceIndexes.InterfaceIndex, ['interface_index', 'interface_name'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.InterfaceIndexes.InterfaceIndex']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
            return meta._meta_table['Snmp.InterfaceIndexes']['meta_info']


    class IfIndexes(_Entity_):
        """
        List of ifnames
        
        .. attribute:: if_index
        
        	Interface Index
        	**type**\: list of  		 :py:class:`IfIndex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.IfIndexes.IfIndex>`
        
        	**config**\: False
        
        

        """

        _prefix = 'snmp-agent-oper'
        _revision = '2018-07-20'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Snmp.IfIndexes, self).__init__()

            self.yang_name = "if-indexes"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("if-index", ("if_index", Snmp.IfIndexes.IfIndex))])
            self._leafs = OrderedDict()

            self.if_index = YList(self)
            self._segment_path = lambda: "if-indexes"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.IfIndexes, [], name, value)


        class IfIndex(_Entity_):
            """
            Interface Index
            
            .. attribute:: interface_index  (key)
            
            	Interface Index as used by MIB tables
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: interface_name
            
            	Interface Name
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2018-07-20'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.IfIndexes.IfIndex, self).__init__()

                self.yang_name = "if-index"
                self.yang_parent_name = "if-indexes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['interface_index']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('interface_index', (YLeaf(YType.uint32, 'interface-index'), ['int'])),
                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                ])
                self.interface_index = None
                self.interface_name = None
                self._segment_path = lambda: "if-index" + "[interface-index='" + str(self.interface_index) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/if-indexes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.IfIndexes.IfIndex, ['interface_index', 'interface_name'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.IfIndexes.IfIndex']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
            return meta._meta_table['Snmp.IfIndexes']['meta_info']


    class SensorMib(_Entity_):
        """
        SNMP sensor MIB information
        
        .. attribute:: physical_indexes
        
        	List of physical index table for threshold value
        	**type**\:  :py:class:`PhysicalIndexes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.SensorMib.PhysicalIndexes>`
        
        	**config**\: False
        
        .. attribute:: ent_phy_indexes
        
        	List of physical index 
        	**type**\:  :py:class:`EntPhyIndexes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.SensorMib.EntPhyIndexes>`
        
        	**config**\: False
        
        

        """

        _prefix = 'snmp-sensormib-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Snmp.SensorMib, self).__init__()

            self.yang_name = "sensor-mib"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("physical-indexes", ("physical_indexes", Snmp.SensorMib.PhysicalIndexes)), ("ent-phy-indexes", ("ent_phy_indexes", Snmp.SensorMib.EntPhyIndexes))])
            self._leafs = OrderedDict()

            self.physical_indexes = Snmp.SensorMib.PhysicalIndexes()
            self.physical_indexes.parent = self
            self._children_name_map["physical_indexes"] = "physical-indexes"

            self.ent_phy_indexes = Snmp.SensorMib.EntPhyIndexes()
            self.ent_phy_indexes.parent = self
            self._children_name_map["ent_phy_indexes"] = "ent-phy-indexes"
            self._segment_path = lambda: "Cisco-IOS-XR-snmp-sensormib-oper:sensor-mib"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.SensorMib, [], name, value)


        class PhysicalIndexes(_Entity_):
            """
            List of physical index table for threshold
            value
            
            .. attribute:: physical_index
            
            	Threshold value for physical index
            	**type**\: list of  		 :py:class:`PhysicalIndex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.SensorMib.PhysicalIndexes.PhysicalIndex>`
            
            	**config**\: False
            
            

            """

            _prefix = 'snmp-sensormib-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.SensorMib.PhysicalIndexes, self).__init__()

                self.yang_name = "physical-indexes"
                self.yang_parent_name = "sensor-mib"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("physical-index", ("physical_index", Snmp.SensorMib.PhysicalIndexes.PhysicalIndex))])
                self._leafs = OrderedDict()

                self.physical_index = YList(self)
                self._segment_path = lambda: "physical-indexes"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-sensormib-oper:sensor-mib/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.SensorMib.PhysicalIndexes, [], name, value)


            class PhysicalIndex(_Entity_):
                """
                Threshold value for physical index
                
                .. attribute:: index  (key)
                
                	Physical index
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                	**config**\: False
                
                .. attribute:: threshold_indexes
                
                	List of threshold index
                	**type**\:  :py:class:`ThresholdIndexes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.SensorMib.PhysicalIndexes.PhysicalIndex.ThresholdIndexes>`
                
                	**config**\: False
                
                

                """

                _prefix = 'snmp-sensormib-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.SensorMib.PhysicalIndexes.PhysicalIndex, self).__init__()

                    self.yang_name = "physical-index"
                    self.yang_parent_name = "physical-indexes"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['index']
                    self._child_classes = OrderedDict([("threshold-indexes", ("threshold_indexes", Snmp.SensorMib.PhysicalIndexes.PhysicalIndex.ThresholdIndexes))])
                    self._leafs = OrderedDict([
                        ('index', (YLeaf(YType.str, 'index'), ['str'])),
                    ])
                    self.index = None

                    self.threshold_indexes = Snmp.SensorMib.PhysicalIndexes.PhysicalIndex.ThresholdIndexes()
                    self.threshold_indexes.parent = self
                    self._children_name_map["threshold_indexes"] = "threshold-indexes"
                    self._segment_path = lambda: "physical-index" + "[index='" + str(self.index) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-sensormib-oper:sensor-mib/physical-indexes/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.SensorMib.PhysicalIndexes.PhysicalIndex, ['index'], name, value)


                class ThresholdIndexes(_Entity_):
                    """
                    List of threshold index
                    
                    .. attribute:: threshold_index
                    
                    	Threshold value for threshold index
                    	**type**\: list of  		 :py:class:`ThresholdIndex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.SensorMib.PhysicalIndexes.PhysicalIndex.ThresholdIndexes.ThresholdIndex>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'snmp-sensormib-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Snmp.SensorMib.PhysicalIndexes.PhysicalIndex.ThresholdIndexes, self).__init__()

                        self.yang_name = "threshold-indexes"
                        self.yang_parent_name = "physical-index"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("threshold-index", ("threshold_index", Snmp.SensorMib.PhysicalIndexes.PhysicalIndex.ThresholdIndexes.ThresholdIndex))])
                        self._leafs = OrderedDict()

                        self.threshold_index = YList(self)
                        self._segment_path = lambda: "threshold-indexes"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.SensorMib.PhysicalIndexes.PhysicalIndex.ThresholdIndexes, [], name, value)


                    class ThresholdIndex(_Entity_):
                        """
                        Threshold value for threshold index
                        
                        .. attribute:: phy_index
                        
                        	Physical Index
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        	**config**\: False
                        
                        .. attribute:: thre_index
                        
                        	Threshold index
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        	**config**\: False
                        
                        .. attribute:: threshold_severity
                        
                        	Indicates minor, major, critical severities
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: threshold_relation
                        
                        	Indicates relation between sensor value and threshold
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: threshold_value
                        
                        	Value of the configured threshold
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: threshold_evaluation
                        
                        	Indicates the result of the most recent evaluation of the thresholD
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: threshold_notification_enabled
                        
                        	Indicates whether or not a notification should result, in case of threshold violation
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'snmp-sensormib-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Snmp.SensorMib.PhysicalIndexes.PhysicalIndex.ThresholdIndexes.ThresholdIndex, self).__init__()

                            self.yang_name = "threshold-index"
                            self.yang_parent_name = "threshold-indexes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('phy_index', (YLeaf(YType.str, 'phy-index'), ['str'])),
                                ('thre_index', (YLeaf(YType.str, 'thre-index'), ['str'])),
                                ('threshold_severity', (YLeaf(YType.uint32, 'threshold-severity'), ['int'])),
                                ('threshold_relation', (YLeaf(YType.uint32, 'threshold-relation'), ['int'])),
                                ('threshold_value', (YLeaf(YType.uint32, 'threshold-value'), ['int'])),
                                ('threshold_evaluation', (YLeaf(YType.boolean, 'threshold-evaluation'), ['bool'])),
                                ('threshold_notification_enabled', (YLeaf(YType.boolean, 'threshold-notification-enabled'), ['bool'])),
                            ])
                            self.phy_index = None
                            self.thre_index = None
                            self.threshold_severity = None
                            self.threshold_relation = None
                            self.threshold_value = None
                            self.threshold_evaluation = None
                            self.threshold_notification_enabled = None
                            self._segment_path = lambda: "threshold-index"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Snmp.SensorMib.PhysicalIndexes.PhysicalIndex.ThresholdIndexes.ThresholdIndex, ['phy_index', 'thre_index', 'threshold_severity', 'threshold_relation', 'threshold_value', 'threshold_evaluation', 'threshold_notification_enabled'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                            return meta._meta_table['Snmp.SensorMib.PhysicalIndexes.PhysicalIndex.ThresholdIndexes.ThresholdIndex']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                        return meta._meta_table['Snmp.SensorMib.PhysicalIndexes.PhysicalIndex.ThresholdIndexes']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.SensorMib.PhysicalIndexes.PhysicalIndex']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.SensorMib.PhysicalIndexes']['meta_info']


        class EntPhyIndexes(_Entity_):
            """
            List of physical index 
            
            .. attribute:: ent_phy_index
            
            	Sensor value for physical index
            	**type**\: list of  		 :py:class:`EntPhyIndex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.SensorMib.EntPhyIndexes.EntPhyIndex>`
            
            	**config**\: False
            
            

            """

            _prefix = 'snmp-sensormib-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.SensorMib.EntPhyIndexes, self).__init__()

                self.yang_name = "ent-phy-indexes"
                self.yang_parent_name = "sensor-mib"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("ent-phy-index", ("ent_phy_index", Snmp.SensorMib.EntPhyIndexes.EntPhyIndex))])
                self._leafs = OrderedDict()

                self.ent_phy_index = YList(self)
                self._segment_path = lambda: "ent-phy-indexes"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-sensormib-oper:sensor-mib/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.SensorMib.EntPhyIndexes, [], name, value)


            class EntPhyIndex(_Entity_):
                """
                Sensor value for physical index
                
                .. attribute:: index  (key)
                
                	Physical index
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                	**config**\: False
                
                .. attribute:: field_validity_bitmap
                
                	Sensor valid bitmap
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: device_description
                
                	Device Name
                	**type**\: str
                
                	**length:** 0..64
                
                	**config**\: False
                
                .. attribute:: units
                
                	Units of variable being read
                	**type**\: str
                
                	**length:** 0..64
                
                	**config**\: False
                
                .. attribute:: device_id
                
                	Identifier for this device
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: value
                
                	Current reading of sensor
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: alarm_type
                
                	Indicates threshold violation
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: data_type
                
                	Sensor data type enums
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: scale
                
                	Sensor scale enums
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: precision
                
                	Sensor precision range
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: status
                
                	Sensor operation state enums
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: age_time_stamp
                
                	Age of the sensor value; set to the current time if directly access the value from sensor
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: update_rate
                
                	Sensor value update rate;set to 0 if sensor value is updated and evaluated immediately
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: measured_entity
                
                	physical entity for which the sensor is taking measurements
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'snmp-sensormib-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.SensorMib.EntPhyIndexes.EntPhyIndex, self).__init__()

                    self.yang_name = "ent-phy-index"
                    self.yang_parent_name = "ent-phy-indexes"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['index']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('index', (YLeaf(YType.str, 'index'), ['str'])),
                        ('field_validity_bitmap', (YLeaf(YType.uint32, 'field-validity-bitmap'), ['int'])),
                        ('device_description', (YLeaf(YType.str, 'device-description'), ['str'])),
                        ('units', (YLeaf(YType.str, 'units'), ['str'])),
                        ('device_id', (YLeaf(YType.uint32, 'device-id'), ['int'])),
                        ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                        ('alarm_type', (YLeaf(YType.uint32, 'alarm-type'), ['int'])),
                        ('data_type', (YLeaf(YType.uint32, 'data-type'), ['int'])),
                        ('scale', (YLeaf(YType.uint32, 'scale'), ['int'])),
                        ('precision', (YLeaf(YType.uint32, 'precision'), ['int'])),
                        ('status', (YLeaf(YType.uint32, 'status'), ['int'])),
                        ('age_time_stamp', (YLeaf(YType.uint32, 'age-time-stamp'), ['int'])),
                        ('update_rate', (YLeaf(YType.uint32, 'update-rate'), ['int'])),
                        ('measured_entity', (YLeaf(YType.uint32, 'measured-entity'), ['int'])),
                    ])
                    self.index = None
                    self.field_validity_bitmap = None
                    self.device_description = None
                    self.units = None
                    self.device_id = None
                    self.value = None
                    self.alarm_type = None
                    self.data_type = None
                    self.scale = None
                    self.precision = None
                    self.status = None
                    self.age_time_stamp = None
                    self.update_rate = None
                    self.measured_entity = None
                    self._segment_path = lambda: "ent-phy-index" + "[index='" + str(self.index) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-sensormib-oper:sensor-mib/ent-phy-indexes/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.SensorMib.EntPhyIndexes.EntPhyIndex, ['index', 'field_validity_bitmap', 'device_description', 'units', 'device_id', 'value', 'alarm_type', 'data_type', 'scale', 'precision', 'status', 'age_time_stamp', 'update_rate', 'measured_entity'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.SensorMib.EntPhyIndexes.EntPhyIndex']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.SensorMib.EntPhyIndexes']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
            return meta._meta_table['Snmp.SensorMib']['meta_info']


    class EntityMib(_Entity_):
        """
        SNMP entity mib
        
        .. attribute:: entity_physical_indexes
        
        	SNMP entity mib
        	**type**\:  :py:class:`EntityPhysicalIndexes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.EntityMib.EntityPhysicalIndexes>`
        
        	**config**\: False
        
        

        """

        _prefix = 'snmp-entitymib-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Snmp.EntityMib, self).__init__()

            self.yang_name = "entity-mib"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("entity-physical-indexes", ("entity_physical_indexes", Snmp.EntityMib.EntityPhysicalIndexes))])
            self._leafs = OrderedDict()

            self.entity_physical_indexes = Snmp.EntityMib.EntityPhysicalIndexes()
            self.entity_physical_indexes.parent = self
            self._children_name_map["entity_physical_indexes"] = "entity-physical-indexes"
            self._segment_path = lambda: "Cisco-IOS-XR-snmp-entitymib-oper:entity-mib"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.EntityMib, [], name, value)


        class EntityPhysicalIndexes(_Entity_):
            """
            SNMP entity mib
            
            .. attribute:: entity_physical_index
            
            	SNMP entPhysical index number
            	**type**\: list of  		 :py:class:`EntityPhysicalIndex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.EntityMib.EntityPhysicalIndexes.EntityPhysicalIndex>`
            
            	**config**\: False
            
            

            """

            _prefix = 'snmp-entitymib-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.EntityMib.EntityPhysicalIndexes, self).__init__()

                self.yang_name = "entity-physical-indexes"
                self.yang_parent_name = "entity-mib"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("entity-physical-index", ("entity_physical_index", Snmp.EntityMib.EntityPhysicalIndexes.EntityPhysicalIndex))])
                self._leafs = OrderedDict()

                self.entity_physical_index = YList(self)
                self._segment_path = lambda: "entity-physical-indexes"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-entitymib-oper:entity-mib/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.EntityMib.EntityPhysicalIndexes, [], name, value)


            class EntityPhysicalIndex(_Entity_):
                """
                SNMP entPhysical index number
                
                .. attribute:: entity_phynum  (key)
                
                	Entity physical index
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                	**config**\: False
                
                .. attribute:: physical_index
                
                	entPhysicalIndex
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: ent_physical_name
                
                	entPhysicalName
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: location
                
                	invmgr EDM path
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: ent_physical_descr
                
                	EntPhysicalDescription
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: ent_physical_firmware_rev
                
                	entphysicalFirmwareRev
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: ent_physical_hardware_rev
                
                	entphysicalHardwareRev
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: ent_physical_modelname
                
                	entphysicalModelName
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: ent_physical_serial_num
                
                	entphysicalSerialNum
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: ent_physical_software_rev
                
                	entphysicalSoftwareRev
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: ent_physical_mfg_name
                
                	entphysicalMfgName
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'snmp-entitymib-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.EntityMib.EntityPhysicalIndexes.EntityPhysicalIndex, self).__init__()

                    self.yang_name = "entity-physical-index"
                    self.yang_parent_name = "entity-physical-indexes"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['entity_phynum']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('entity_phynum', (YLeaf(YType.str, 'entity-phynum'), ['str'])),
                        ('physical_index', (YLeaf(YType.uint32, 'physical-index'), ['int'])),
                        ('ent_physical_name', (YLeaf(YType.str, 'ent-physical-name'), ['str'])),
                        ('location', (YLeaf(YType.str, 'location'), ['str'])),
                        ('ent_physical_descr', (YLeaf(YType.str, 'ent-physical-descr'), ['str'])),
                        ('ent_physical_firmware_rev', (YLeaf(YType.str, 'ent-physical-firmware-rev'), ['str'])),
                        ('ent_physical_hardware_rev', (YLeaf(YType.str, 'ent-physical-hardware-rev'), ['str'])),
                        ('ent_physical_modelname', (YLeaf(YType.str, 'ent-physical-modelname'), ['str'])),
                        ('ent_physical_serial_num', (YLeaf(YType.str, 'ent-physical-serial-num'), ['str'])),
                        ('ent_physical_software_rev', (YLeaf(YType.str, 'ent-physical-software-rev'), ['str'])),
                        ('ent_physical_mfg_name', (YLeaf(YType.str, 'ent-physical-mfg-name'), ['str'])),
                    ])
                    self.entity_phynum = None
                    self.physical_index = None
                    self.ent_physical_name = None
                    self.location = None
                    self.ent_physical_descr = None
                    self.ent_physical_firmware_rev = None
                    self.ent_physical_hardware_rev = None
                    self.ent_physical_modelname = None
                    self.ent_physical_serial_num = None
                    self.ent_physical_software_rev = None
                    self.ent_physical_mfg_name = None
                    self._segment_path = lambda: "entity-physical-index" + "[entity-phynum='" + str(self.entity_phynum) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-entitymib-oper:entity-mib/entity-physical-indexes/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.EntityMib.EntityPhysicalIndexes.EntityPhysicalIndex, ['entity_phynum', 'physical_index', 'ent_physical_name', 'location', 'ent_physical_descr', 'ent_physical_firmware_rev', 'ent_physical_hardware_rev', 'ent_physical_modelname', 'ent_physical_serial_num', 'ent_physical_software_rev', 'ent_physical_mfg_name'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.EntityMib.EntityPhysicalIndexes.EntityPhysicalIndex']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.EntityMib.EntityPhysicalIndexes']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
            return meta._meta_table['Snmp.EntityMib']['meta_info']


    class InterfaceMib(_Entity_):
        """
        SNMP IF\-MIB information
        
        .. attribute:: interfaces
        
        	Interfaces ifIndex information
        	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.InterfaceMib.Interfaces>`
        
        	**config**\: False
        
        .. attribute:: interface_connectors
        
        	Interfaces ifConnectorPresent information
        	**type**\:  :py:class:`InterfaceConnectors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.InterfaceMib.InterfaceConnectors>`
        
        	**config**\: False
        
        .. attribute:: interface_aliases
        
        	Interfaces ifAlias information
        	**type**\:  :py:class:`InterfaceAliases <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.InterfaceMib.InterfaceAliases>`
        
        	**config**\: False
        
        .. attribute:: notification_interfaces
        
        	Interfaces Notification information
        	**type**\:  :py:class:`NotificationInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.InterfaceMib.NotificationInterfaces>`
        
        	**config**\: False
        
        .. attribute:: interface_stack_statuses
        
        	Interfaces ifstackstatus information
        	**type**\:  :py:class:`InterfaceStackStatuses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.InterfaceMib.InterfaceStackStatuses>`
        
        	**config**\: False
        
        

        """

        _prefix = 'snmp-ifmib-oper'
        _revision = '2015-01-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Snmp.InterfaceMib, self).__init__()

            self.yang_name = "interface-mib"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interfaces", ("interfaces", Snmp.InterfaceMib.Interfaces)), ("interface-connectors", ("interface_connectors", Snmp.InterfaceMib.InterfaceConnectors)), ("interface-aliases", ("interface_aliases", Snmp.InterfaceMib.InterfaceAliases)), ("notification-interfaces", ("notification_interfaces", Snmp.InterfaceMib.NotificationInterfaces)), ("interface-stack-statuses", ("interface_stack_statuses", Snmp.InterfaceMib.InterfaceStackStatuses))])
            self._leafs = OrderedDict()

            self.interfaces = Snmp.InterfaceMib.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"

            self.interface_connectors = Snmp.InterfaceMib.InterfaceConnectors()
            self.interface_connectors.parent = self
            self._children_name_map["interface_connectors"] = "interface-connectors"

            self.interface_aliases = Snmp.InterfaceMib.InterfaceAliases()
            self.interface_aliases.parent = self
            self._children_name_map["interface_aliases"] = "interface-aliases"

            self.notification_interfaces = Snmp.InterfaceMib.NotificationInterfaces()
            self.notification_interfaces.parent = self
            self._children_name_map["notification_interfaces"] = "notification-interfaces"

            self.interface_stack_statuses = Snmp.InterfaceMib.InterfaceStackStatuses()
            self.interface_stack_statuses.parent = self
            self._children_name_map["interface_stack_statuses"] = "interface-stack-statuses"
            self._segment_path = lambda: "Cisco-IOS-XR-snmp-ifmib-oper:interface-mib"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.InterfaceMib, [], name, value)


        class Interfaces(_Entity_):
            """
            Interfaces ifIndex information
            
            .. attribute:: interface
            
            	ifIndex for a specific Interface Name
            	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.InterfaceMib.Interfaces.Interface>`
            
            	**config**\: False
            
            

            """

            _prefix = 'snmp-ifmib-oper'
            _revision = '2015-01-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.InterfaceMib.Interfaces, self).__init__()

                self.yang_name = "interfaces"
                self.yang_parent_name = "interface-mib"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("interface", ("interface", Snmp.InterfaceMib.Interfaces.Interface))])
                self._leafs = OrderedDict()

                self.interface = YList(self)
                self._segment_path = lambda: "interfaces"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-ifmib-oper:interface-mib/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.InterfaceMib.Interfaces, [], name, value)


            class Interface(_Entity_):
                """
                ifIndex for a specific Interface Name
                
                .. attribute:: interface_name  (key)
                
                	Interface Name
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                	**config**\: False
                
                .. attribute:: if_index
                
                	Interface Index
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'snmp-ifmib-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.InterfaceMib.Interfaces.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interfaces"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['interface_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ('if_index', (YLeaf(YType.uint32, 'if-index'), ['int'])),
                    ])
                    self.interface_name = None
                    self.if_index = None
                    self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-ifmib-oper:interface-mib/interfaces/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.InterfaceMib.Interfaces.Interface, ['interface_name', 'if_index'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.InterfaceMib.Interfaces.Interface']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.InterfaceMib.Interfaces']['meta_info']


        class InterfaceConnectors(_Entity_):
            """
            Interfaces ifConnectorPresent information
            
            .. attribute:: interface_connector
            
            	ifConnectorPresent for a specific Interface Name
            	**type**\: list of  		 :py:class:`InterfaceConnector <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.InterfaceMib.InterfaceConnectors.InterfaceConnector>`
            
            	**config**\: False
            
            

            """

            _prefix = 'snmp-ifmib-oper'
            _revision = '2015-01-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.InterfaceMib.InterfaceConnectors, self).__init__()

                self.yang_name = "interface-connectors"
                self.yang_parent_name = "interface-mib"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("interface-connector", ("interface_connector", Snmp.InterfaceMib.InterfaceConnectors.InterfaceConnector))])
                self._leafs = OrderedDict()

                self.interface_connector = YList(self)
                self._segment_path = lambda: "interface-connectors"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-ifmib-oper:interface-mib/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.InterfaceMib.InterfaceConnectors, [], name, value)


            class InterfaceConnector(_Entity_):
                """
                ifConnectorPresent for a specific Interface
                Name
                
                .. attribute:: interface_name  (key)
                
                	Interface Name
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                	**config**\: False
                
                .. attribute:: if_connector_present
                
                	Interface ifConnector
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'snmp-ifmib-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.InterfaceMib.InterfaceConnectors.InterfaceConnector, self).__init__()

                    self.yang_name = "interface-connector"
                    self.yang_parent_name = "interface-connectors"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['interface_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ('if_connector_present', (YLeaf(YType.str, 'if-connector-present'), ['str'])),
                    ])
                    self.interface_name = None
                    self.if_connector_present = None
                    self._segment_path = lambda: "interface-connector" + "[interface-name='" + str(self.interface_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-ifmib-oper:interface-mib/interface-connectors/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.InterfaceMib.InterfaceConnectors.InterfaceConnector, ['interface_name', 'if_connector_present'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.InterfaceMib.InterfaceConnectors.InterfaceConnector']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.InterfaceMib.InterfaceConnectors']['meta_info']


        class InterfaceAliases(_Entity_):
            """
            Interfaces ifAlias information
            
            .. attribute:: interface_alias
            
            	ifAlias for a specific Interface Name
            	**type**\: list of  		 :py:class:`InterfaceAlias <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.InterfaceMib.InterfaceAliases.InterfaceAlias>`
            
            	**config**\: False
            
            

            """

            _prefix = 'snmp-ifmib-oper'
            _revision = '2015-01-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.InterfaceMib.InterfaceAliases, self).__init__()

                self.yang_name = "interface-aliases"
                self.yang_parent_name = "interface-mib"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("interface-alias", ("interface_alias", Snmp.InterfaceMib.InterfaceAliases.InterfaceAlias))])
                self._leafs = OrderedDict()

                self.interface_alias = YList(self)
                self._segment_path = lambda: "interface-aliases"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-ifmib-oper:interface-mib/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.InterfaceMib.InterfaceAliases, [], name, value)


            class InterfaceAlias(_Entity_):
                """
                ifAlias for a specific Interface Name
                
                .. attribute:: interface_name  (key)
                
                	Interface Name
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                	**config**\: False
                
                .. attribute:: if_alias
                
                	Interface ifAlias
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'snmp-ifmib-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.InterfaceMib.InterfaceAliases.InterfaceAlias, self).__init__()

                    self.yang_name = "interface-alias"
                    self.yang_parent_name = "interface-aliases"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['interface_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ('if_alias', (YLeaf(YType.str, 'if-alias'), ['str'])),
                    ])
                    self.interface_name = None
                    self.if_alias = None
                    self._segment_path = lambda: "interface-alias" + "[interface-name='" + str(self.interface_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-ifmib-oper:interface-mib/interface-aliases/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.InterfaceMib.InterfaceAliases.InterfaceAlias, ['interface_name', 'if_alias'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.InterfaceMib.InterfaceAliases.InterfaceAlias']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.InterfaceMib.InterfaceAliases']['meta_info']


        class NotificationInterfaces(_Entity_):
            """
            Interfaces Notification information
            
            .. attribute:: notification_interface
            
            	Notification for specific Interface Name
            	**type**\: list of  		 :py:class:`NotificationInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.InterfaceMib.NotificationInterfaces.NotificationInterface>`
            
            	**config**\: False
            
            

            """

            _prefix = 'snmp-ifmib-oper'
            _revision = '2015-01-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.InterfaceMib.NotificationInterfaces, self).__init__()

                self.yang_name = "notification-interfaces"
                self.yang_parent_name = "interface-mib"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("notification-interface", ("notification_interface", Snmp.InterfaceMib.NotificationInterfaces.NotificationInterface))])
                self._leafs = OrderedDict()

                self.notification_interface = YList(self)
                self._segment_path = lambda: "notification-interfaces"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-ifmib-oper:interface-mib/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.InterfaceMib.NotificationInterfaces, [], name, value)


            class NotificationInterface(_Entity_):
                """
                Notification for specific Interface Name
                
                .. attribute:: interface_name  (key)
                
                	Interface Name
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                	**config**\: False
                
                .. attribute:: link_up_down_notif_status
                
                	LinkUpDown notification status
                	**type**\:  :py:class:`LinkUpDownStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_ifmib_oper.LinkUpDownStatus>`
                
                	**config**\: False
                
                

                """

                _prefix = 'snmp-ifmib-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.InterfaceMib.NotificationInterfaces.NotificationInterface, self).__init__()

                    self.yang_name = "notification-interface"
                    self.yang_parent_name = "notification-interfaces"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['interface_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ('link_up_down_notif_status', (YLeaf(YType.enumeration, 'link-up-down-notif-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_ifmib_oper', 'LinkUpDownStatus', '')])),
                    ])
                    self.interface_name = None
                    self.link_up_down_notif_status = None
                    self._segment_path = lambda: "notification-interface" + "[interface-name='" + str(self.interface_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-ifmib-oper:interface-mib/notification-interfaces/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.InterfaceMib.NotificationInterfaces.NotificationInterface, ['interface_name', 'link_up_down_notif_status'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.InterfaceMib.NotificationInterfaces.NotificationInterface']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.InterfaceMib.NotificationInterfaces']['meta_info']


        class InterfaceStackStatuses(_Entity_):
            """
            Interfaces ifstackstatus information
            
            .. attribute:: interface_stack_status
            
            	ifstatus for a pair of Interface
            	**type**\: list of  		 :py:class:`InterfaceStackStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.InterfaceMib.InterfaceStackStatuses.InterfaceStackStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'snmp-ifmib-oper'
            _revision = '2015-01-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.InterfaceMib.InterfaceStackStatuses, self).__init__()

                self.yang_name = "interface-stack-statuses"
                self.yang_parent_name = "interface-mib"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("interface-stack-status", ("interface_stack_status", Snmp.InterfaceMib.InterfaceStackStatuses.InterfaceStackStatus))])
                self._leafs = OrderedDict()

                self.interface_stack_status = YList(self)
                self._segment_path = lambda: "interface-stack-statuses"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-ifmib-oper:interface-mib/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.InterfaceMib.InterfaceStackStatuses, [], name, value)


            class InterfaceStackStatus(_Entity_):
                """
                ifstatus for a pair of Interface
                
                .. attribute:: interface_stack_status  (key)
                
                	StackHigherLayer.StackLowerLayer
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                	**config**\: False
                
                .. attribute:: if_stack_higher_layer
                
                	Higher Layer Index
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: if_stack_lower_layer
                
                	Lowyer Layer Index
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: if_stack_status
                
                	Interface ifStackStaus info
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'snmp-ifmib-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.InterfaceMib.InterfaceStackStatuses.InterfaceStackStatus, self).__init__()

                    self.yang_name = "interface-stack-status"
                    self.yang_parent_name = "interface-stack-statuses"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['interface_stack_status']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('interface_stack_status', (YLeaf(YType.str, 'interface-stack-status'), ['str'])),
                        ('if_stack_higher_layer', (YLeaf(YType.str, 'if-stack-higher-layer'), ['str'])),
                        ('if_stack_lower_layer', (YLeaf(YType.str, 'if-stack-lower-layer'), ['str'])),
                        ('if_stack_status', (YLeaf(YType.str, 'if-stack-status'), ['str'])),
                    ])
                    self.interface_stack_status = None
                    self.if_stack_higher_layer = None
                    self.if_stack_lower_layer = None
                    self.if_stack_status = None
                    self._segment_path = lambda: "interface-stack-status" + "[interface-stack-status='" + str(self.interface_stack_status) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-ifmib-oper:interface-mib/interface-stack-statuses/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.InterfaceMib.InterfaceStackStatuses.InterfaceStackStatus, ['interface_stack_status', 'if_stack_higher_layer', 'if_stack_lower_layer', 'if_stack_status'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.InterfaceMib.InterfaceStackStatuses.InterfaceStackStatus']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.InterfaceMib.InterfaceStackStatuses']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
            return meta._meta_table['Snmp.InterfaceMib']['meta_info']

    def clone_ptr(self):
        self._top_entity = Snmp()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
        return meta._meta_table['Snmp']['meta_info']



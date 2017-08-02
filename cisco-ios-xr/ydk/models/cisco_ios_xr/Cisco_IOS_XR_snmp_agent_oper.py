""" Cisco_IOS_XR_snmp_agent_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR snmp\-agent package operational data.

This module contains definitions
for the following management objects\:
  snmp\: SNMP operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class DupReqDropStatus(Enum):
    """
    DupReqDropStatus

    Dup req drop status

    .. data:: disabled = 0

    	Disabled

    .. data:: enabled = 1

    	Enabled

    """

    disabled = Enum.YLeaf(0, "disabled")

    enabled = Enum.YLeaf(1, "enabled")


class SnmpCorrRuleState(Enum):
    """
    SnmpCorrRuleState

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


class SnmpCorrVbindMatch(Enum):
    """
    SnmpCorrVbindMatch

    Snmp corr vbind match

    .. data:: index = 0

    	Match regexp to varbind index

    .. data:: value = 1

    	Match regexp to varbind value

    """

    index = Enum.YLeaf(0, "index")

    value = Enum.YLeaf(1, "value")



class Snmp(Entity):
    """
    SNMP operational data
    
    .. attribute:: correlator
    
    	Trap Correlator operational data
    	**type**\:   :py:class:`Correlator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Correlator>`
    
    .. attribute:: entity_mib
    
    	SNMP entity mib
    	**type**\:   :py:class:`EntityMib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.EntityMib>`
    
    .. attribute:: if_indexes
    
    	List of ifnames
    	**type**\:   :py:class:`IfIndexes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.IfIndexes>`
    
    .. attribute:: information
    
    	SNMP operational information
    	**type**\:   :py:class:`Information <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information>`
    
    .. attribute:: interface_indexes
    
    	List of index
    	**type**\:   :py:class:`InterfaceIndexes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.InterfaceIndexes>`
    
    .. attribute:: interface_mib
    
    	SNMP IF\-MIB information
    	**type**\:   :py:class:`InterfaceMib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.InterfaceMib>`
    
    .. attribute:: interfaces
    
    	List of interfaces
    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Interfaces>`
    
    .. attribute:: sensor_mib
    
    	SNMP sensor MIB information
    	**type**\:   :py:class:`SensorMib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.SensorMib>`
    
    .. attribute:: trap_servers
    
    	List of trap hosts
    	**type**\:   :py:class:`TrapServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.TrapServers>`
    
    

    """

    _prefix = 'snmp-agent-oper'
    _revision = '2016-06-01'

    def __init__(self):
        super(Snmp, self).__init__()
        self._top_entity = None

        self.yang_name = "snmp"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-agent-oper"

        self.correlator = Snmp.Correlator()
        self.correlator.parent = self
        self._children_name_map["correlator"] = "correlator"
        self._children_yang_names.add("correlator")

        self.entity_mib = Snmp.EntityMib()
        self.entity_mib.parent = self
        self._children_name_map["entity_mib"] = "entity-mib"
        self._children_yang_names.add("entity-mib")

        self.if_indexes = Snmp.IfIndexes()
        self.if_indexes.parent = self
        self._children_name_map["if_indexes"] = "if-indexes"
        self._children_yang_names.add("if-indexes")

        self.information = Snmp.Information()
        self.information.parent = self
        self._children_name_map["information"] = "information"
        self._children_yang_names.add("information")

        self.interface_indexes = Snmp.InterfaceIndexes()
        self.interface_indexes.parent = self
        self._children_name_map["interface_indexes"] = "interface-indexes"
        self._children_yang_names.add("interface-indexes")

        self.interface_mib = Snmp.InterfaceMib()
        self.interface_mib.parent = self
        self._children_name_map["interface_mib"] = "interface-mib"
        self._children_yang_names.add("interface-mib")

        self.interfaces = Snmp.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._children_yang_names.add("interfaces")

        self.sensor_mib = Snmp.SensorMib()
        self.sensor_mib.parent = self
        self._children_name_map["sensor_mib"] = "sensor-mib"
        self._children_yang_names.add("sensor-mib")

        self.trap_servers = Snmp.TrapServers()
        self.trap_servers.parent = self
        self._children_name_map["trap_servers"] = "trap-servers"
        self._children_yang_names.add("trap-servers")


    class TrapServers(Entity):
        """
        List of trap hosts
        
        .. attribute:: trap_server
        
        	Trap server and port to which the trap is to be sent and statistics
        	**type**\: list of    :py:class:`TrapServer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.TrapServers.TrapServer>`
        
        

        """

        _prefix = 'snmp-agent-oper'
        _revision = '2016-06-01'

        def __init__(self):
            super(Snmp.TrapServers, self).__init__()

            self.yang_name = "trap-servers"
            self.yang_parent_name = "snmp"

            self.trap_server = YList(self)

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
                        super(Snmp.TrapServers, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Snmp.TrapServers, self).__setattr__(name, value)


        class TrapServer(Entity):
            """
            Trap server and port to which the trap is to be
            sent and statistics
            
            .. attribute:: max_q_length_of_trap_q
            
            	Maximum Queue length of trapQ
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: number_of_pkts_dropped
            
            	No. of trap packets dropped
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: number_of_pkts_in_trap_q
            
            	No. of trap packets in trapQ
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: number_of_pkts_sent
            
            	No. of trap packets sent
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: port
            
            	Trap port
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: trap_host
            
            	Trap Host
            	**type**\:  str
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                super(Snmp.TrapServers.TrapServer, self).__init__()

                self.yang_name = "trap-server"
                self.yang_parent_name = "trap-servers"

                self.max_q_length_of_trap_q = YLeaf(YType.uint32, "max-q-length-of-trap-q")

                self.number_of_pkts_dropped = YLeaf(YType.uint32, "number-of-pkts-dropped")

                self.number_of_pkts_in_trap_q = YLeaf(YType.uint32, "number-of-pkts-in-trap-q")

                self.number_of_pkts_sent = YLeaf(YType.uint32, "number-of-pkts-sent")

                self.port = YLeaf(YType.uint16, "port")

                self.trap_host = YLeaf(YType.str, "trap-host")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("max_q_length_of_trap_q",
                                "number_of_pkts_dropped",
                                "number_of_pkts_in_trap_q",
                                "number_of_pkts_sent",
                                "port",
                                "trap_host") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Snmp.TrapServers.TrapServer, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Snmp.TrapServers.TrapServer, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.max_q_length_of_trap_q.is_set or
                    self.number_of_pkts_dropped.is_set or
                    self.number_of_pkts_in_trap_q.is_set or
                    self.number_of_pkts_sent.is_set or
                    self.port.is_set or
                    self.trap_host.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.max_q_length_of_trap_q.yfilter != YFilter.not_set or
                    self.number_of_pkts_dropped.yfilter != YFilter.not_set or
                    self.number_of_pkts_in_trap_q.yfilter != YFilter.not_set or
                    self.number_of_pkts_sent.yfilter != YFilter.not_set or
                    self.port.yfilter != YFilter.not_set or
                    self.trap_host.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "trap-server" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/trap-servers/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.max_q_length_of_trap_q.is_set or self.max_q_length_of_trap_q.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.max_q_length_of_trap_q.get_name_leafdata())
                if (self.number_of_pkts_dropped.is_set or self.number_of_pkts_dropped.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.number_of_pkts_dropped.get_name_leafdata())
                if (self.number_of_pkts_in_trap_q.is_set or self.number_of_pkts_in_trap_q.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.number_of_pkts_in_trap_q.get_name_leafdata())
                if (self.number_of_pkts_sent.is_set or self.number_of_pkts_sent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.number_of_pkts_sent.get_name_leafdata())
                if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.port.get_name_leafdata())
                if (self.trap_host.is_set or self.trap_host.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.trap_host.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "max-q-length-of-trap-q" or name == "number-of-pkts-dropped" or name == "number-of-pkts-in-trap-q" or name == "number-of-pkts-sent" or name == "port" or name == "trap-host"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "max-q-length-of-trap-q"):
                    self.max_q_length_of_trap_q = value
                    self.max_q_length_of_trap_q.value_namespace = name_space
                    self.max_q_length_of_trap_q.value_namespace_prefix = name_space_prefix
                if(value_path == "number-of-pkts-dropped"):
                    self.number_of_pkts_dropped = value
                    self.number_of_pkts_dropped.value_namespace = name_space
                    self.number_of_pkts_dropped.value_namespace_prefix = name_space_prefix
                if(value_path == "number-of-pkts-in-trap-q"):
                    self.number_of_pkts_in_trap_q = value
                    self.number_of_pkts_in_trap_q.value_namespace = name_space
                    self.number_of_pkts_in_trap_q.value_namespace_prefix = name_space_prefix
                if(value_path == "number-of-pkts-sent"):
                    self.number_of_pkts_sent = value
                    self.number_of_pkts_sent.value_namespace = name_space
                    self.number_of_pkts_sent.value_namespace_prefix = name_space_prefix
                if(value_path == "port"):
                    self.port = value
                    self.port.value_namespace = name_space
                    self.port.value_namespace_prefix = name_space_prefix
                if(value_path == "trap-host"):
                    self.trap_host = value
                    self.trap_host.value_namespace = name_space
                    self.trap_host.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.trap_server:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.trap_server:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "trap-servers" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "trap-server"):
                for c in self.trap_server:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Snmp.TrapServers.TrapServer()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.trap_server.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "trap-server"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Information(Entity):
        """
        SNMP operational information
        
        .. attribute:: bulk_stats_transfers
        
        	List of bulkstats transfer on the system
        	**type**\:   :py:class:`BulkStatsTransfers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.BulkStatsTransfers>`
        
        .. attribute:: context_mapping
        
        	Context name, features name, topology name, instance
        	**type**\:   :py:class:`ContextMapping <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.ContextMapping>`
        
        .. attribute:: drop_nms_addresses
        
        	NMS list for drop PDU
        	**type**\:   :py:class:`DropNmsAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.DropNmsAddresses>`
        
        .. attribute:: duplicate_drop
        
        	Duplicate request status, count, time 
        	**type**\:   :py:class:`DuplicateDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.DuplicateDrop>`
        
        .. attribute:: engine_id
        
        	SNMP engine ID
        	**type**\:   :py:class:`EngineId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.EngineId>`
        
        .. attribute:: hosts
        
        	SNMP host information
        	**type**\:   :py:class:`Hosts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Hosts>`
        
        .. attribute:: incoming_queue
        
        	Incoming queue details 
        	**type**\:   :py:class:`IncomingQueue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.IncomingQueue>`
        
        .. attribute:: infom_details
        
        	SNMP trap OID
        	**type**\:   :py:class:`InfomDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.InfomDetails>`
        
        .. attribute:: mibs
        
        	List of MIBS supported on the system
        	**type**\:   :py:class:`Mibs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Mibs>`
        
        .. attribute:: nm_spackets
        
        	SNMP overload statistics 
        	**type**\:   :py:class:`NmSpackets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.NmSpackets>`
        
        .. attribute:: nms_addresses
        
        	SNMP request type summary 
        	**type**\:   :py:class:`NmsAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.NmsAddresses>`
        
        .. attribute:: poll_oids
        
        	OID list for poll PDU
        	**type**\:   :py:class:`PollOids <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.PollOids>`
        
        .. attribute:: request_type_detail
        
        	SNMP request type details 
        	**type**\:   :py:class:`RequestTypeDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.RequestTypeDetail>`
        
        .. attribute:: rx_queue
        
        	SNMP rx queue statistics
        	**type**\:   :py:class:`RxQueue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.RxQueue>`
        
        .. attribute:: serial_numbers
        
        	SNMP statistics pdu 
        	**type**\:   :py:class:`SerialNumbers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.SerialNumbers>`
        
        .. attribute:: statistics
        
        	SNMP statistics
        	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Statistics>`
        
        .. attribute:: system_descr
        
        	System description
        	**type**\:   :py:class:`SystemDescr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.SystemDescr>`
        
        .. attribute:: system_name
        
        	System name
        	**type**\:   :py:class:`SystemName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.SystemName>`
        
        .. attribute:: system_oid
        
        	System object ID
        	**type**\:   :py:class:`SystemOid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.SystemOid>`
        
        .. attribute:: system_up_time
        
        	System up time
        	**type**\:   :py:class:`SystemUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.SystemUpTime>`
        
        .. attribute:: tables
        
        	List of table
        	**type**\:   :py:class:`Tables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Tables>`
        
        .. attribute:: trap_infos
        
        	SNMP trap OID
        	**type**\:   :py:class:`TrapInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.TrapInfos>`
        
        .. attribute:: trap_oids
        
        	SNMP trap OID
        	**type**\:   :py:class:`TrapOids <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.TrapOids>`
        
        .. attribute:: trap_queue
        
        	SNMP trap queue statistics
        	**type**\:   :py:class:`TrapQueue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.TrapQueue>`
        
        .. attribute:: views
        
        	SNMP view information
        	**type**\:   :py:class:`Views <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Views>`
        
        

        """

        _prefix = 'snmp-agent-oper'
        _revision = '2016-06-01'

        def __init__(self):
            super(Snmp.Information, self).__init__()

            self.yang_name = "information"
            self.yang_parent_name = "snmp"

            self.bulk_stats_transfers = Snmp.Information.BulkStatsTransfers()
            self.bulk_stats_transfers.parent = self
            self._children_name_map["bulk_stats_transfers"] = "bulk-stats-transfers"
            self._children_yang_names.add("bulk-stats-transfers")

            self.context_mapping = Snmp.Information.ContextMapping()
            self.context_mapping.parent = self
            self._children_name_map["context_mapping"] = "context-mapping"
            self._children_yang_names.add("context-mapping")

            self.drop_nms_addresses = Snmp.Information.DropNmsAddresses()
            self.drop_nms_addresses.parent = self
            self._children_name_map["drop_nms_addresses"] = "drop-nms-addresses"
            self._children_yang_names.add("drop-nms-addresses")

            self.duplicate_drop = Snmp.Information.DuplicateDrop()
            self.duplicate_drop.parent = self
            self._children_name_map["duplicate_drop"] = "duplicate-drop"
            self._children_yang_names.add("duplicate-drop")

            self.engine_id = Snmp.Information.EngineId()
            self.engine_id.parent = self
            self._children_name_map["engine_id"] = "engine-id"
            self._children_yang_names.add("engine-id")

            self.hosts = Snmp.Information.Hosts()
            self.hosts.parent = self
            self._children_name_map["hosts"] = "hosts"
            self._children_yang_names.add("hosts")

            self.incoming_queue = Snmp.Information.IncomingQueue()
            self.incoming_queue.parent = self
            self._children_name_map["incoming_queue"] = "incoming-queue"
            self._children_yang_names.add("incoming-queue")

            self.infom_details = Snmp.Information.InfomDetails()
            self.infom_details.parent = self
            self._children_name_map["infom_details"] = "infom-details"
            self._children_yang_names.add("infom-details")

            self.mibs = Snmp.Information.Mibs()
            self.mibs.parent = self
            self._children_name_map["mibs"] = "mibs"
            self._children_yang_names.add("mibs")

            self.nm_spackets = Snmp.Information.NmSpackets()
            self.nm_spackets.parent = self
            self._children_name_map["nm_spackets"] = "nm-spackets"
            self._children_yang_names.add("nm-spackets")

            self.nms_addresses = Snmp.Information.NmsAddresses()
            self.nms_addresses.parent = self
            self._children_name_map["nms_addresses"] = "nms-addresses"
            self._children_yang_names.add("nms-addresses")

            self.poll_oids = Snmp.Information.PollOids()
            self.poll_oids.parent = self
            self._children_name_map["poll_oids"] = "poll-oids"
            self._children_yang_names.add("poll-oids")

            self.request_type_detail = Snmp.Information.RequestTypeDetail()
            self.request_type_detail.parent = self
            self._children_name_map["request_type_detail"] = "request-type-detail"
            self._children_yang_names.add("request-type-detail")

            self.rx_queue = Snmp.Information.RxQueue()
            self.rx_queue.parent = self
            self._children_name_map["rx_queue"] = "rx-queue"
            self._children_yang_names.add("rx-queue")

            self.serial_numbers = Snmp.Information.SerialNumbers()
            self.serial_numbers.parent = self
            self._children_name_map["serial_numbers"] = "serial-numbers"
            self._children_yang_names.add("serial-numbers")

            self.statistics = Snmp.Information.Statistics()
            self.statistics.parent = self
            self._children_name_map["statistics"] = "statistics"
            self._children_yang_names.add("statistics")

            self.system_descr = Snmp.Information.SystemDescr()
            self.system_descr.parent = self
            self._children_name_map["system_descr"] = "system-descr"
            self._children_yang_names.add("system-descr")

            self.system_name = Snmp.Information.SystemName()
            self.system_name.parent = self
            self._children_name_map["system_name"] = "system-name"
            self._children_yang_names.add("system-name")

            self.system_oid = Snmp.Information.SystemOid()
            self.system_oid.parent = self
            self._children_name_map["system_oid"] = "system-oid"
            self._children_yang_names.add("system-oid")

            self.system_up_time = Snmp.Information.SystemUpTime()
            self.system_up_time.parent = self
            self._children_name_map["system_up_time"] = "system-up-time"
            self._children_yang_names.add("system-up-time")

            self.tables = Snmp.Information.Tables()
            self.tables.parent = self
            self._children_name_map["tables"] = "tables"
            self._children_yang_names.add("tables")

            self.trap_infos = Snmp.Information.TrapInfos()
            self.trap_infos.parent = self
            self._children_name_map["trap_infos"] = "trap-infos"
            self._children_yang_names.add("trap-infos")

            self.trap_oids = Snmp.Information.TrapOids()
            self.trap_oids.parent = self
            self._children_name_map["trap_oids"] = "trap-oids"
            self._children_yang_names.add("trap-oids")

            self.trap_queue = Snmp.Information.TrapQueue()
            self.trap_queue.parent = self
            self._children_name_map["trap_queue"] = "trap-queue"
            self._children_yang_names.add("trap-queue")

            self.views = Snmp.Information.Views()
            self.views.parent = self
            self._children_name_map["views"] = "views"
            self._children_yang_names.add("views")


        class Hosts(Entity):
            """
            SNMP host information
            
            .. attribute:: host
            
            	SNMP target host name
            	**type**\: list of    :py:class:`Host <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Hosts.Host>`
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                super(Snmp.Information.Hosts, self).__init__()

                self.yang_name = "hosts"
                self.yang_parent_name = "information"

                self.host = YList(self)

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
                            super(Snmp.Information.Hosts, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Snmp.Information.Hosts, self).__setattr__(name, value)


            class Host(Entity):
                """
                SNMP target host name
                
                .. attribute:: name  <key>
                
                	Group name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: host_information
                
                	Host name ,udp\-port , user, security model and level
                	**type**\: list of    :py:class:`HostInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Hosts.Host.HostInformation>`
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2016-06-01'

                def __init__(self):
                    super(Snmp.Information.Hosts.Host, self).__init__()

                    self.yang_name = "host"
                    self.yang_parent_name = "hosts"

                    self.name = YLeaf(YType.str, "name")

                    self.host_information = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Snmp.Information.Hosts.Host, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Snmp.Information.Hosts.Host, self).__setattr__(name, value)


                class HostInformation(Entity):
                    """
                    Host name ,udp\-port , user, security model
                    and level
                    
                    .. attribute:: user  <key>
                    
                    	SNMP host user
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: snmp_target_address_port
                    
                    	Target UDP port
                    	**type**\:  str
                    
                    .. attribute:: snmp_target_address_t_host
                    
                    	Transport type of address
                    	**type**\:  str
                    
                    .. attribute:: snmp_target_addresstype
                    
                    	Target host type (Inform or Trap)
                    	**type**\:  str
                    
                    .. attribute:: snmp_target_params_security_level
                    
                    	Security level
                    	**type**\:  str
                    
                    .. attribute:: snmp_target_params_security_model
                    
                    	Security model
                    	**type**\:  str
                    
                    .. attribute:: snmp_target_params_security_name
                    
                    	Security name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'snmp-agent-oper'
                    _revision = '2016-06-01'

                    def __init__(self):
                        super(Snmp.Information.Hosts.Host.HostInformation, self).__init__()

                        self.yang_name = "host-information"
                        self.yang_parent_name = "host"

                        self.user = YLeaf(YType.str, "user")

                        self.snmp_target_address_port = YLeaf(YType.str, "snmp-target-address-port")

                        self.snmp_target_address_t_host = YLeaf(YType.str, "snmp-target-address-t-host")

                        self.snmp_target_addresstype = YLeaf(YType.str, "snmp-target-addresstype")

                        self.snmp_target_params_security_level = YLeaf(YType.str, "snmp-target-params-security-level")

                        self.snmp_target_params_security_model = YLeaf(YType.str, "snmp-target-params-security-model")

                        self.snmp_target_params_security_name = YLeaf(YType.str, "snmp-target-params-security-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("user",
                                        "snmp_target_address_port",
                                        "snmp_target_address_t_host",
                                        "snmp_target_addresstype",
                                        "snmp_target_params_security_level",
                                        "snmp_target_params_security_model",
                                        "snmp_target_params_security_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Snmp.Information.Hosts.Host.HostInformation, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Snmp.Information.Hosts.Host.HostInformation, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.user.is_set or
                            self.snmp_target_address_port.is_set or
                            self.snmp_target_address_t_host.is_set or
                            self.snmp_target_addresstype.is_set or
                            self.snmp_target_params_security_level.is_set or
                            self.snmp_target_params_security_model.is_set or
                            self.snmp_target_params_security_name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.user.yfilter != YFilter.not_set or
                            self.snmp_target_address_port.yfilter != YFilter.not_set or
                            self.snmp_target_address_t_host.yfilter != YFilter.not_set or
                            self.snmp_target_addresstype.yfilter != YFilter.not_set or
                            self.snmp_target_params_security_level.yfilter != YFilter.not_set or
                            self.snmp_target_params_security_model.yfilter != YFilter.not_set or
                            self.snmp_target_params_security_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "host-information" + "[user='" + self.user.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.user.is_set or self.user.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.user.get_name_leafdata())
                        if (self.snmp_target_address_port.is_set or self.snmp_target_address_port.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.snmp_target_address_port.get_name_leafdata())
                        if (self.snmp_target_address_t_host.is_set or self.snmp_target_address_t_host.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.snmp_target_address_t_host.get_name_leafdata())
                        if (self.snmp_target_addresstype.is_set or self.snmp_target_addresstype.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.snmp_target_addresstype.get_name_leafdata())
                        if (self.snmp_target_params_security_level.is_set or self.snmp_target_params_security_level.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.snmp_target_params_security_level.get_name_leafdata())
                        if (self.snmp_target_params_security_model.is_set or self.snmp_target_params_security_model.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.snmp_target_params_security_model.get_name_leafdata())
                        if (self.snmp_target_params_security_name.is_set or self.snmp_target_params_security_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.snmp_target_params_security_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "user" or name == "snmp-target-address-port" or name == "snmp-target-address-t-host" or name == "snmp-target-addresstype" or name == "snmp-target-params-security-level" or name == "snmp-target-params-security-model" or name == "snmp-target-params-security-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "user"):
                            self.user = value
                            self.user.value_namespace = name_space
                            self.user.value_namespace_prefix = name_space_prefix
                        if(value_path == "snmp-target-address-port"):
                            self.snmp_target_address_port = value
                            self.snmp_target_address_port.value_namespace = name_space
                            self.snmp_target_address_port.value_namespace_prefix = name_space_prefix
                        if(value_path == "snmp-target-address-t-host"):
                            self.snmp_target_address_t_host = value
                            self.snmp_target_address_t_host.value_namespace = name_space
                            self.snmp_target_address_t_host.value_namespace_prefix = name_space_prefix
                        if(value_path == "snmp-target-addresstype"):
                            self.snmp_target_addresstype = value
                            self.snmp_target_addresstype.value_namespace = name_space
                            self.snmp_target_addresstype.value_namespace_prefix = name_space_prefix
                        if(value_path == "snmp-target-params-security-level"):
                            self.snmp_target_params_security_level = value
                            self.snmp_target_params_security_level.value_namespace = name_space
                            self.snmp_target_params_security_level.value_namespace_prefix = name_space_prefix
                        if(value_path == "snmp-target-params-security-model"):
                            self.snmp_target_params_security_model = value
                            self.snmp_target_params_security_model.value_namespace = name_space
                            self.snmp_target_params_security_model.value_namespace_prefix = name_space_prefix
                        if(value_path == "snmp-target-params-security-name"):
                            self.snmp_target_params_security_name = value
                            self.snmp_target_params_security_name.value_namespace = name_space
                            self.snmp_target_params_security_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.host_information:
                        if (c.has_data()):
                            return True
                    return self.name.is_set

                def has_operation(self):
                    for c in self.host_information:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "host" + "[name='" + self.name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/hosts/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "host-information"):
                        for c in self.host_information:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Snmp.Information.Hosts.Host.HostInformation()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.host_information.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "host-information" or name == "name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.host:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.host:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "hosts" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "host"):
                    for c in self.host:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Snmp.Information.Hosts.Host()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.host.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "host"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class SystemUpTime(Entity):
            """
            System up time
            
            .. attribute:: system_up_time_edm
            
            	sysUpTime  1.3.6.1.2.1.1.3
            	**type**\:  str
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                super(Snmp.Information.SystemUpTime, self).__init__()

                self.yang_name = "system-up-time"
                self.yang_parent_name = "information"

                self.system_up_time_edm = YLeaf(YType.str, "system-up-time-edm")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("system_up_time_edm") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Snmp.Information.SystemUpTime, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Snmp.Information.SystemUpTime, self).__setattr__(name, value)

            def has_data(self):
                return self.system_up_time_edm.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.system_up_time_edm.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "system-up-time" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.system_up_time_edm.is_set or self.system_up_time_edm.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.system_up_time_edm.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "system-up-time-edm"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "system-up-time-edm"):
                    self.system_up_time_edm = value
                    self.system_up_time_edm.value_namespace = name_space
                    self.system_up_time_edm.value_namespace_prefix = name_space_prefix


        class NmsAddresses(Entity):
            """
            SNMP request type summary 
            
            .. attribute:: nms_address
            
            	NMS address
            	**type**\: list of    :py:class:`NmsAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.NmsAddresses.NmsAddress>`
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                super(Snmp.Information.NmsAddresses, self).__init__()

                self.yang_name = "nms-addresses"
                self.yang_parent_name = "information"

                self.nms_address = YList(self)

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
                            super(Snmp.Information.NmsAddresses, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Snmp.Information.NmsAddresses, self).__setattr__(name, value)


            class NmsAddress(Entity):
                """
                NMS address
                
                .. attribute:: nms_addr  <key>
                
                	NMS address
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: get_request_count
                
                	Get Request Count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: getbulk_request_count
                
                	Getbulk Request Count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: getnext_request_count
                
                	Getnext Request Count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: nms_address
                
                	NMS address of server
                	**type**\:  str
                
                .. attribute:: set_request_count
                
                	Set Request Count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: test_request_count
                
                	Test Request Count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2016-06-01'

                def __init__(self):
                    super(Snmp.Information.NmsAddresses.NmsAddress, self).__init__()

                    self.yang_name = "nms-address"
                    self.yang_parent_name = "nms-addresses"

                    self.nms_addr = YLeaf(YType.str, "nms-addr")

                    self.get_request_count = YLeaf(YType.uint32, "get-request-count")

                    self.getbulk_request_count = YLeaf(YType.uint32, "getbulk-request-count")

                    self.getnext_request_count = YLeaf(YType.uint32, "getnext-request-count")

                    self.nms_address = YLeaf(YType.str, "nms-address")

                    self.set_request_count = YLeaf(YType.uint32, "set-request-count")

                    self.test_request_count = YLeaf(YType.uint32, "test-request-count")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("nms_addr",
                                    "get_request_count",
                                    "getbulk_request_count",
                                    "getnext_request_count",
                                    "nms_address",
                                    "set_request_count",
                                    "test_request_count") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Snmp.Information.NmsAddresses.NmsAddress, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Snmp.Information.NmsAddresses.NmsAddress, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.nms_addr.is_set or
                        self.get_request_count.is_set or
                        self.getbulk_request_count.is_set or
                        self.getnext_request_count.is_set or
                        self.nms_address.is_set or
                        self.set_request_count.is_set or
                        self.test_request_count.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.nms_addr.yfilter != YFilter.not_set or
                        self.get_request_count.yfilter != YFilter.not_set or
                        self.getbulk_request_count.yfilter != YFilter.not_set or
                        self.getnext_request_count.yfilter != YFilter.not_set or
                        self.nms_address.yfilter != YFilter.not_set or
                        self.set_request_count.yfilter != YFilter.not_set or
                        self.test_request_count.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "nms-address" + "[nms-addr='" + self.nms_addr.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/nms-addresses/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.nms_addr.is_set or self.nms_addr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.nms_addr.get_name_leafdata())
                    if (self.get_request_count.is_set or self.get_request_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.get_request_count.get_name_leafdata())
                    if (self.getbulk_request_count.is_set or self.getbulk_request_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.getbulk_request_count.get_name_leafdata())
                    if (self.getnext_request_count.is_set or self.getnext_request_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.getnext_request_count.get_name_leafdata())
                    if (self.nms_address.is_set or self.nms_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.nms_address.get_name_leafdata())
                    if (self.set_request_count.is_set or self.set_request_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.set_request_count.get_name_leafdata())
                    if (self.test_request_count.is_set or self.test_request_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.test_request_count.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "nms-addr" or name == "get-request-count" or name == "getbulk-request-count" or name == "getnext-request-count" or name == "nms-address" or name == "set-request-count" or name == "test-request-count"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "nms-addr"):
                        self.nms_addr = value
                        self.nms_addr.value_namespace = name_space
                        self.nms_addr.value_namespace_prefix = name_space_prefix
                    if(value_path == "get-request-count"):
                        self.get_request_count = value
                        self.get_request_count.value_namespace = name_space
                        self.get_request_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "getbulk-request-count"):
                        self.getbulk_request_count = value
                        self.getbulk_request_count.value_namespace = name_space
                        self.getbulk_request_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "getnext-request-count"):
                        self.getnext_request_count = value
                        self.getnext_request_count.value_namespace = name_space
                        self.getnext_request_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "nms-address"):
                        self.nms_address = value
                        self.nms_address.value_namespace = name_space
                        self.nms_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "set-request-count"):
                        self.set_request_count = value
                        self.set_request_count.value_namespace = name_space
                        self.set_request_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "test-request-count"):
                        self.test_request_count = value
                        self.test_request_count.value_namespace = name_space
                        self.test_request_count.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.nms_address:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.nms_address:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "nms-addresses" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "nms-address"):
                    for c in self.nms_address:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Snmp.Information.NmsAddresses.NmsAddress()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.nms_address.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "nms-address"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class EngineId(Entity):
            """
            SNMP engine ID
            
            .. attribute:: engine_id
            
            	SNMPv3 engineID
            	**type**\:  str
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                super(Snmp.Information.EngineId, self).__init__()

                self.yang_name = "engine-id"
                self.yang_parent_name = "information"

                self.engine_id = YLeaf(YType.str, "engine-id")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("engine_id") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Snmp.Information.EngineId, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Snmp.Information.EngineId, self).__setattr__(name, value)

            def has_data(self):
                return self.engine_id.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.engine_id.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "engine-id" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.engine_id.is_set or self.engine_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.engine_id.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "engine-id"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "engine-id"):
                    self.engine_id = value
                    self.engine_id.value_namespace = name_space
                    self.engine_id.value_namespace_prefix = name_space_prefix


        class RxQueue(Entity):
            """
            SNMP rx queue statistics
            
            .. attribute:: in_avg
            
            	in avg
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: in_max
            
            	in max
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: in_min
            
            	in min
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: incoming_q
            
            	incomingQ
            	**type**\:  str
            
            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
            
            .. attribute:: pend_avg
            
            	pend avg
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: pend_max
            
            	pend max
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: pend_min
            
            	pend min
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: pending_q
            
            	pendingQ
            	**type**\:  str
            
            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
            
            .. attribute:: qlen
            
            	qlen
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                super(Snmp.Information.RxQueue, self).__init__()

                self.yang_name = "rx-queue"
                self.yang_parent_name = "information"

                self.in_avg = YLeaf(YType.uint32, "in-avg")

                self.in_max = YLeaf(YType.uint32, "in-max")

                self.in_min = YLeaf(YType.uint32, "in-min")

                self.incoming_q = YLeaf(YType.str, "incoming-q")

                self.pend_avg = YLeaf(YType.uint32, "pend-avg")

                self.pend_max = YLeaf(YType.uint32, "pend-max")

                self.pend_min = YLeaf(YType.uint32, "pend-min")

                self.pending_q = YLeaf(YType.str, "pending-q")

                self.qlen = YLeaf(YType.uint32, "qlen")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("in_avg",
                                "in_max",
                                "in_min",
                                "incoming_q",
                                "pend_avg",
                                "pend_max",
                                "pend_min",
                                "pending_q",
                                "qlen") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Snmp.Information.RxQueue, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Snmp.Information.RxQueue, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.in_avg.is_set or
                    self.in_max.is_set or
                    self.in_min.is_set or
                    self.incoming_q.is_set or
                    self.pend_avg.is_set or
                    self.pend_max.is_set or
                    self.pend_min.is_set or
                    self.pending_q.is_set or
                    self.qlen.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.in_avg.yfilter != YFilter.not_set or
                    self.in_max.yfilter != YFilter.not_set or
                    self.in_min.yfilter != YFilter.not_set or
                    self.incoming_q.yfilter != YFilter.not_set or
                    self.pend_avg.yfilter != YFilter.not_set or
                    self.pend_max.yfilter != YFilter.not_set or
                    self.pend_min.yfilter != YFilter.not_set or
                    self.pending_q.yfilter != YFilter.not_set or
                    self.qlen.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rx-queue" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.in_avg.is_set or self.in_avg.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.in_avg.get_name_leafdata())
                if (self.in_max.is_set or self.in_max.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.in_max.get_name_leafdata())
                if (self.in_min.is_set or self.in_min.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.in_min.get_name_leafdata())
                if (self.incoming_q.is_set or self.incoming_q.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.incoming_q.get_name_leafdata())
                if (self.pend_avg.is_set or self.pend_avg.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pend_avg.get_name_leafdata())
                if (self.pend_max.is_set or self.pend_max.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pend_max.get_name_leafdata())
                if (self.pend_min.is_set or self.pend_min.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pend_min.get_name_leafdata())
                if (self.pending_q.is_set or self.pending_q.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pending_q.get_name_leafdata())
                if (self.qlen.is_set or self.qlen.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qlen.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "in-avg" or name == "in-max" or name == "in-min" or name == "incoming-q" or name == "pend-avg" or name == "pend-max" or name == "pend-min" or name == "pending-q" or name == "qlen"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "in-avg"):
                    self.in_avg = value
                    self.in_avg.value_namespace = name_space
                    self.in_avg.value_namespace_prefix = name_space_prefix
                if(value_path == "in-max"):
                    self.in_max = value
                    self.in_max.value_namespace = name_space
                    self.in_max.value_namespace_prefix = name_space_prefix
                if(value_path == "in-min"):
                    self.in_min = value
                    self.in_min.value_namespace = name_space
                    self.in_min.value_namespace_prefix = name_space_prefix
                if(value_path == "incoming-q"):
                    self.incoming_q = value
                    self.incoming_q.value_namespace = name_space
                    self.incoming_q.value_namespace_prefix = name_space_prefix
                if(value_path == "pend-avg"):
                    self.pend_avg = value
                    self.pend_avg.value_namespace = name_space
                    self.pend_avg.value_namespace_prefix = name_space_prefix
                if(value_path == "pend-max"):
                    self.pend_max = value
                    self.pend_max.value_namespace = name_space
                    self.pend_max.value_namespace_prefix = name_space_prefix
                if(value_path == "pend-min"):
                    self.pend_min = value
                    self.pend_min.value_namespace = name_space
                    self.pend_min.value_namespace_prefix = name_space_prefix
                if(value_path == "pending-q"):
                    self.pending_q = value
                    self.pending_q.value_namespace = name_space
                    self.pending_q.value_namespace_prefix = name_space_prefix
                if(value_path == "qlen"):
                    self.qlen = value
                    self.qlen.value_namespace = name_space
                    self.qlen.value_namespace_prefix = name_space_prefix


        class SystemName(Entity):
            """
            System name
            
            .. attribute:: system_name
            
            	sysName  1.3.6.1.2.1.1.5
            	**type**\:  str
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                super(Snmp.Information.SystemName, self).__init__()

                self.yang_name = "system-name"
                self.yang_parent_name = "information"

                self.system_name = YLeaf(YType.str, "system-name")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("system_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Snmp.Information.SystemName, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Snmp.Information.SystemName, self).__setattr__(name, value)

            def has_data(self):
                return self.system_name.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.system_name.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "system-name" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.system_name.is_set or self.system_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.system_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "system-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "system-name"):
                    self.system_name = value
                    self.system_name.value_namespace = name_space
                    self.system_name.value_namespace_prefix = name_space_prefix


        class RequestTypeDetail(Entity):
            """
            SNMP request type details 
            
            .. attribute:: nms_addresses
            
            	snmp request type details 
            	**type**\:   :py:class:`NmsAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.RequestTypeDetail.NmsAddresses>`
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                super(Snmp.Information.RequestTypeDetail, self).__init__()

                self.yang_name = "request-type-detail"
                self.yang_parent_name = "information"

                self.nms_addresses = Snmp.Information.RequestTypeDetail.NmsAddresses()
                self.nms_addresses.parent = self
                self._children_name_map["nms_addresses"] = "nms-addresses"
                self._children_yang_names.add("nms-addresses")


            class NmsAddresses(Entity):
                """
                snmp request type details 
                
                .. attribute:: nms_address
                
                	NMS address
                	**type**\: list of    :py:class:`NmsAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.RequestTypeDetail.NmsAddresses.NmsAddress>`
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2016-06-01'

                def __init__(self):
                    super(Snmp.Information.RequestTypeDetail.NmsAddresses, self).__init__()

                    self.yang_name = "nms-addresses"
                    self.yang_parent_name = "request-type-detail"

                    self.nms_address = YList(self)

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
                                super(Snmp.Information.RequestTypeDetail.NmsAddresses, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Snmp.Information.RequestTypeDetail.NmsAddresses, self).__setattr__(name, value)


                class NmsAddress(Entity):
                    """
                    NMS address
                    
                    .. attribute:: nms_addr  <key>
                    
                    	NMS address
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: agent_request_count
                    
                    	Processing agent request count for each client for particluar managment station
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: entity_request_count
                    
                    	Processing entity request count for each client for particluar managment station
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: infra_request_count
                    
                    	Processing infra request count for each client for particluar Managment station
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_request_count
                    
                    	Processing interfce request count for each client for particluar managment station
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: route_request_count
                    
                    	Processing route request count for each client for particluar Managment station
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_count
                    
                    	Total request count for each managment station or client
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'snmp-agent-oper'
                    _revision = '2016-06-01'

                    def __init__(self):
                        super(Snmp.Information.RequestTypeDetail.NmsAddresses.NmsAddress, self).__init__()

                        self.yang_name = "nms-address"
                        self.yang_parent_name = "nms-addresses"

                        self.nms_addr = YLeaf(YType.str, "nms-addr")

                        self.agent_request_count = YLeaf(YType.uint32, "agent-request-count")

                        self.entity_request_count = YLeaf(YType.uint32, "entity-request-count")

                        self.infra_request_count = YLeaf(YType.uint32, "infra-request-count")

                        self.interface_request_count = YLeaf(YType.uint32, "interface-request-count")

                        self.route_request_count = YLeaf(YType.uint32, "route-request-count")

                        self.total_count = YLeaf(YType.uint32, "total-count")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("nms_addr",
                                        "agent_request_count",
                                        "entity_request_count",
                                        "infra_request_count",
                                        "interface_request_count",
                                        "route_request_count",
                                        "total_count") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Snmp.Information.RequestTypeDetail.NmsAddresses.NmsAddress, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Snmp.Information.RequestTypeDetail.NmsAddresses.NmsAddress, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.nms_addr.is_set or
                            self.agent_request_count.is_set or
                            self.entity_request_count.is_set or
                            self.infra_request_count.is_set or
                            self.interface_request_count.is_set or
                            self.route_request_count.is_set or
                            self.total_count.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.nms_addr.yfilter != YFilter.not_set or
                            self.agent_request_count.yfilter != YFilter.not_set or
                            self.entity_request_count.yfilter != YFilter.not_set or
                            self.infra_request_count.yfilter != YFilter.not_set or
                            self.interface_request_count.yfilter != YFilter.not_set or
                            self.route_request_count.yfilter != YFilter.not_set or
                            self.total_count.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "nms-address" + "[nms-addr='" + self.nms_addr.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/request-type-detail/nms-addresses/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.nms_addr.is_set or self.nms_addr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.nms_addr.get_name_leafdata())
                        if (self.agent_request_count.is_set or self.agent_request_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.agent_request_count.get_name_leafdata())
                        if (self.entity_request_count.is_set or self.entity_request_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.entity_request_count.get_name_leafdata())
                        if (self.infra_request_count.is_set or self.infra_request_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.infra_request_count.get_name_leafdata())
                        if (self.interface_request_count.is_set or self.interface_request_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_request_count.get_name_leafdata())
                        if (self.route_request_count.is_set or self.route_request_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.route_request_count.get_name_leafdata())
                        if (self.total_count.is_set or self.total_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.total_count.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "nms-addr" or name == "agent-request-count" or name == "entity-request-count" or name == "infra-request-count" or name == "interface-request-count" or name == "route-request-count" or name == "total-count"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "nms-addr"):
                            self.nms_addr = value
                            self.nms_addr.value_namespace = name_space
                            self.nms_addr.value_namespace_prefix = name_space_prefix
                        if(value_path == "agent-request-count"):
                            self.agent_request_count = value
                            self.agent_request_count.value_namespace = name_space
                            self.agent_request_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "entity-request-count"):
                            self.entity_request_count = value
                            self.entity_request_count.value_namespace = name_space
                            self.entity_request_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "infra-request-count"):
                            self.infra_request_count = value
                            self.infra_request_count.value_namespace = name_space
                            self.infra_request_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-request-count"):
                            self.interface_request_count = value
                            self.interface_request_count.value_namespace = name_space
                            self.interface_request_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "route-request-count"):
                            self.route_request_count = value
                            self.route_request_count.value_namespace = name_space
                            self.route_request_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "total-count"):
                            self.total_count = value
                            self.total_count.value_namespace = name_space
                            self.total_count.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.nms_address:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.nms_address:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "nms-addresses" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/request-type-detail/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "nms-address"):
                        for c in self.nms_address:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Snmp.Information.RequestTypeDetail.NmsAddresses.NmsAddress()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.nms_address.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "nms-address"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (self.nms_addresses is not None and self.nms_addresses.has_data())

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.nms_addresses is not None and self.nms_addresses.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "request-type-detail" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "nms-addresses"):
                    if (self.nms_addresses is None):
                        self.nms_addresses = Snmp.Information.RequestTypeDetail.NmsAddresses()
                        self.nms_addresses.parent = self
                        self._children_name_map["nms_addresses"] = "nms-addresses"
                    return self.nms_addresses

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "nms-addresses"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class DuplicateDrop(Entity):
            """
            Duplicate request status, count, time 
            
            .. attribute:: duplicate_drop_configured_timeout
            
            	Configured Duplicate Drop feature Timeout
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: duplicate_drop_disable_count
            
            	 Number of times duplicate request drop feature is disabled
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: duplicate_drop_enable_count
            
            	 Number of times duplicate request drop feature is enabled
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: duplicate_dropped_requests
            
            	Number of duplicate SNMP requests are dropped
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: duplicate_request_latest_enable_time
            
            	Duplicate request drop feature last enable time(Day Mon Date HH\:MM\:SS)
            	**type**\:  str
            
            .. attribute:: duplicate_request_status
            
            	Duplicate requests drop feature status
            	**type**\:   :py:class:`DupReqDropStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.DupReqDropStatus>`
            
            .. attribute:: first_enable_time
            
            	Duplicate request drop feature first  enable time (Day Mon Date HH\:MM\:SS)
            	**type**\:  str
            
            .. attribute:: last_status_change_time
            
            	Duplicate request drop feature last enable disable time (Day Mon Date HH\:MM\:SS)
            	**type**\:  str
            
            .. attribute:: latest_duplicate_dropped_requests
            
            	Number of duplicate SNMP requests dropped, from the last enable time
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: latest_retry_processed_requests
            
            	Number of retry SNMP requests processed, from the last enable time
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: retry_processed_requests
            
            	Number of Retry SNMP requests are Processed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                super(Snmp.Information.DuplicateDrop, self).__init__()

                self.yang_name = "duplicate-drop"
                self.yang_parent_name = "information"

                self.duplicate_drop_configured_timeout = YLeaf(YType.uint32, "duplicate-drop-configured-timeout")

                self.duplicate_drop_disable_count = YLeaf(YType.uint32, "duplicate-drop-disable-count")

                self.duplicate_drop_enable_count = YLeaf(YType.uint32, "duplicate-drop-enable-count")

                self.duplicate_dropped_requests = YLeaf(YType.uint32, "duplicate-dropped-requests")

                self.duplicate_request_latest_enable_time = YLeaf(YType.str, "duplicate-request-latest-enable-time")

                self.duplicate_request_status = YLeaf(YType.enumeration, "duplicate-request-status")

                self.first_enable_time = YLeaf(YType.str, "first-enable-time")

                self.last_status_change_time = YLeaf(YType.str, "last-status-change-time")

                self.latest_duplicate_dropped_requests = YLeaf(YType.uint32, "latest-duplicate-dropped-requests")

                self.latest_retry_processed_requests = YLeaf(YType.uint32, "latest-retry-processed-requests")

                self.retry_processed_requests = YLeaf(YType.uint32, "retry-processed-requests")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("duplicate_drop_configured_timeout",
                                "duplicate_drop_disable_count",
                                "duplicate_drop_enable_count",
                                "duplicate_dropped_requests",
                                "duplicate_request_latest_enable_time",
                                "duplicate_request_status",
                                "first_enable_time",
                                "last_status_change_time",
                                "latest_duplicate_dropped_requests",
                                "latest_retry_processed_requests",
                                "retry_processed_requests") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Snmp.Information.DuplicateDrop, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Snmp.Information.DuplicateDrop, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.duplicate_drop_configured_timeout.is_set or
                    self.duplicate_drop_disable_count.is_set or
                    self.duplicate_drop_enable_count.is_set or
                    self.duplicate_dropped_requests.is_set or
                    self.duplicate_request_latest_enable_time.is_set or
                    self.duplicate_request_status.is_set or
                    self.first_enable_time.is_set or
                    self.last_status_change_time.is_set or
                    self.latest_duplicate_dropped_requests.is_set or
                    self.latest_retry_processed_requests.is_set or
                    self.retry_processed_requests.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.duplicate_drop_configured_timeout.yfilter != YFilter.not_set or
                    self.duplicate_drop_disable_count.yfilter != YFilter.not_set or
                    self.duplicate_drop_enable_count.yfilter != YFilter.not_set or
                    self.duplicate_dropped_requests.yfilter != YFilter.not_set or
                    self.duplicate_request_latest_enable_time.yfilter != YFilter.not_set or
                    self.duplicate_request_status.yfilter != YFilter.not_set or
                    self.first_enable_time.yfilter != YFilter.not_set or
                    self.last_status_change_time.yfilter != YFilter.not_set or
                    self.latest_duplicate_dropped_requests.yfilter != YFilter.not_set or
                    self.latest_retry_processed_requests.yfilter != YFilter.not_set or
                    self.retry_processed_requests.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "duplicate-drop" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.duplicate_drop_configured_timeout.is_set or self.duplicate_drop_configured_timeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.duplicate_drop_configured_timeout.get_name_leafdata())
                if (self.duplicate_drop_disable_count.is_set or self.duplicate_drop_disable_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.duplicate_drop_disable_count.get_name_leafdata())
                if (self.duplicate_drop_enable_count.is_set or self.duplicate_drop_enable_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.duplicate_drop_enable_count.get_name_leafdata())
                if (self.duplicate_dropped_requests.is_set or self.duplicate_dropped_requests.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.duplicate_dropped_requests.get_name_leafdata())
                if (self.duplicate_request_latest_enable_time.is_set or self.duplicate_request_latest_enable_time.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.duplicate_request_latest_enable_time.get_name_leafdata())
                if (self.duplicate_request_status.is_set or self.duplicate_request_status.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.duplicate_request_status.get_name_leafdata())
                if (self.first_enable_time.is_set or self.first_enable_time.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.first_enable_time.get_name_leafdata())
                if (self.last_status_change_time.is_set or self.last_status_change_time.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.last_status_change_time.get_name_leafdata())
                if (self.latest_duplicate_dropped_requests.is_set or self.latest_duplicate_dropped_requests.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.latest_duplicate_dropped_requests.get_name_leafdata())
                if (self.latest_retry_processed_requests.is_set or self.latest_retry_processed_requests.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.latest_retry_processed_requests.get_name_leafdata())
                if (self.retry_processed_requests.is_set or self.retry_processed_requests.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.retry_processed_requests.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "duplicate-drop-configured-timeout" or name == "duplicate-drop-disable-count" or name == "duplicate-drop-enable-count" or name == "duplicate-dropped-requests" or name == "duplicate-request-latest-enable-time" or name == "duplicate-request-status" or name == "first-enable-time" or name == "last-status-change-time" or name == "latest-duplicate-dropped-requests" or name == "latest-retry-processed-requests" or name == "retry-processed-requests"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "duplicate-drop-configured-timeout"):
                    self.duplicate_drop_configured_timeout = value
                    self.duplicate_drop_configured_timeout.value_namespace = name_space
                    self.duplicate_drop_configured_timeout.value_namespace_prefix = name_space_prefix
                if(value_path == "duplicate-drop-disable-count"):
                    self.duplicate_drop_disable_count = value
                    self.duplicate_drop_disable_count.value_namespace = name_space
                    self.duplicate_drop_disable_count.value_namespace_prefix = name_space_prefix
                if(value_path == "duplicate-drop-enable-count"):
                    self.duplicate_drop_enable_count = value
                    self.duplicate_drop_enable_count.value_namespace = name_space
                    self.duplicate_drop_enable_count.value_namespace_prefix = name_space_prefix
                if(value_path == "duplicate-dropped-requests"):
                    self.duplicate_dropped_requests = value
                    self.duplicate_dropped_requests.value_namespace = name_space
                    self.duplicate_dropped_requests.value_namespace_prefix = name_space_prefix
                if(value_path == "duplicate-request-latest-enable-time"):
                    self.duplicate_request_latest_enable_time = value
                    self.duplicate_request_latest_enable_time.value_namespace = name_space
                    self.duplicate_request_latest_enable_time.value_namespace_prefix = name_space_prefix
                if(value_path == "duplicate-request-status"):
                    self.duplicate_request_status = value
                    self.duplicate_request_status.value_namespace = name_space
                    self.duplicate_request_status.value_namespace_prefix = name_space_prefix
                if(value_path == "first-enable-time"):
                    self.first_enable_time = value
                    self.first_enable_time.value_namespace = name_space
                    self.first_enable_time.value_namespace_prefix = name_space_prefix
                if(value_path == "last-status-change-time"):
                    self.last_status_change_time = value
                    self.last_status_change_time.value_namespace = name_space
                    self.last_status_change_time.value_namespace_prefix = name_space_prefix
                if(value_path == "latest-duplicate-dropped-requests"):
                    self.latest_duplicate_dropped_requests = value
                    self.latest_duplicate_dropped_requests.value_namespace = name_space
                    self.latest_duplicate_dropped_requests.value_namespace_prefix = name_space_prefix
                if(value_path == "latest-retry-processed-requests"):
                    self.latest_retry_processed_requests = value
                    self.latest_retry_processed_requests.value_namespace = name_space
                    self.latest_retry_processed_requests.value_namespace_prefix = name_space_prefix
                if(value_path == "retry-processed-requests"):
                    self.retry_processed_requests = value
                    self.retry_processed_requests.value_namespace = name_space
                    self.retry_processed_requests.value_namespace_prefix = name_space_prefix


        class BulkStatsTransfers(Entity):
            """
            List of bulkstats transfer on the system
            
            .. attribute:: bulk_stats_transfer
            
            	SNMP bulkstats transfer name
            	**type**\: list of    :py:class:`BulkStatsTransfer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.BulkStatsTransfers.BulkStatsTransfer>`
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                super(Snmp.Information.BulkStatsTransfers, self).__init__()

                self.yang_name = "bulk-stats-transfers"
                self.yang_parent_name = "information"

                self.bulk_stats_transfer = YList(self)

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
                            super(Snmp.Information.BulkStatsTransfers, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Snmp.Information.BulkStatsTransfers, self).__setattr__(name, value)


            class BulkStatsTransfer(Entity):
                """
                SNMP bulkstats transfer name
                
                .. attribute:: transfer_name  <key>
                
                	Transfer name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: retained_file
                
                	Bulkstats transfer retained file name
                	**type**\:  str
                
                .. attribute:: retry_left
                
                	Bulkstats transfer retry attempt left
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: time_left
                
                	Bulkstats transfer retry time left in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: transfer_name_xr
                
                	Name of the bulkstats transfer session
                	**type**\:  str
                
                .. attribute:: url_primary
                
                	Bulkstats transfer primary URL
                	**type**\:  str
                
                .. attribute:: url_secondary
                
                	Bulkstats transfer secondary URL
                	**type**\:  str
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2016-06-01'

                def __init__(self):
                    super(Snmp.Information.BulkStatsTransfers.BulkStatsTransfer, self).__init__()

                    self.yang_name = "bulk-stats-transfer"
                    self.yang_parent_name = "bulk-stats-transfers"

                    self.transfer_name = YLeaf(YType.str, "transfer-name")

                    self.retained_file = YLeaf(YType.str, "retained-file")

                    self.retry_left = YLeaf(YType.uint32, "retry-left")

                    self.time_left = YLeaf(YType.uint32, "time-left")

                    self.transfer_name_xr = YLeaf(YType.str, "transfer-name-xr")

                    self.url_primary = YLeaf(YType.str, "url-primary")

                    self.url_secondary = YLeaf(YType.str, "url-secondary")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("transfer_name",
                                    "retained_file",
                                    "retry_left",
                                    "time_left",
                                    "transfer_name_xr",
                                    "url_primary",
                                    "url_secondary") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Snmp.Information.BulkStatsTransfers.BulkStatsTransfer, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Snmp.Information.BulkStatsTransfers.BulkStatsTransfer, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.transfer_name.is_set or
                        self.retained_file.is_set or
                        self.retry_left.is_set or
                        self.time_left.is_set or
                        self.transfer_name_xr.is_set or
                        self.url_primary.is_set or
                        self.url_secondary.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.transfer_name.yfilter != YFilter.not_set or
                        self.retained_file.yfilter != YFilter.not_set or
                        self.retry_left.yfilter != YFilter.not_set or
                        self.time_left.yfilter != YFilter.not_set or
                        self.transfer_name_xr.yfilter != YFilter.not_set or
                        self.url_primary.yfilter != YFilter.not_set or
                        self.url_secondary.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "bulk-stats-transfer" + "[transfer-name='" + self.transfer_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/bulk-stats-transfers/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.transfer_name.is_set or self.transfer_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.transfer_name.get_name_leafdata())
                    if (self.retained_file.is_set or self.retained_file.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.retained_file.get_name_leafdata())
                    if (self.retry_left.is_set or self.retry_left.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.retry_left.get_name_leafdata())
                    if (self.time_left.is_set or self.time_left.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.time_left.get_name_leafdata())
                    if (self.transfer_name_xr.is_set or self.transfer_name_xr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.transfer_name_xr.get_name_leafdata())
                    if (self.url_primary.is_set or self.url_primary.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.url_primary.get_name_leafdata())
                    if (self.url_secondary.is_set or self.url_secondary.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.url_secondary.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "transfer-name" or name == "retained-file" or name == "retry-left" or name == "time-left" or name == "transfer-name-xr" or name == "url-primary" or name == "url-secondary"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "transfer-name"):
                        self.transfer_name = value
                        self.transfer_name.value_namespace = name_space
                        self.transfer_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "retained-file"):
                        self.retained_file = value
                        self.retained_file.value_namespace = name_space
                        self.retained_file.value_namespace_prefix = name_space_prefix
                    if(value_path == "retry-left"):
                        self.retry_left = value
                        self.retry_left.value_namespace = name_space
                        self.retry_left.value_namespace_prefix = name_space_prefix
                    if(value_path == "time-left"):
                        self.time_left = value
                        self.time_left.value_namespace = name_space
                        self.time_left.value_namespace_prefix = name_space_prefix
                    if(value_path == "transfer-name-xr"):
                        self.transfer_name_xr = value
                        self.transfer_name_xr.value_namespace = name_space
                        self.transfer_name_xr.value_namespace_prefix = name_space_prefix
                    if(value_path == "url-primary"):
                        self.url_primary = value
                        self.url_primary.value_namespace = name_space
                        self.url_primary.value_namespace_prefix = name_space_prefix
                    if(value_path == "url-secondary"):
                        self.url_secondary = value
                        self.url_secondary.value_namespace = name_space
                        self.url_secondary.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.bulk_stats_transfer:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.bulk_stats_transfer:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "bulk-stats-transfers" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "bulk-stats-transfer"):
                    for c in self.bulk_stats_transfer:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Snmp.Information.BulkStatsTransfers.BulkStatsTransfer()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.bulk_stats_transfer.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "bulk-stats-transfer"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class TrapInfos(Entity):
            """
            SNMP trap OID
            
            .. attribute:: trap_info
            
            	SNMP Trap infomation like server , port and trapOID
            	**type**\: list of    :py:class:`TrapInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.TrapInfos.TrapInfo>`
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                super(Snmp.Information.TrapInfos, self).__init__()

                self.yang_name = "trap-infos"
                self.yang_parent_name = "information"

                self.trap_info = YList(self)

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
                            super(Snmp.Information.TrapInfos, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Snmp.Information.TrapInfos, self).__setattr__(name, value)


            class TrapInfo(Entity):
                """
                SNMP Trap infomation like server , port and
                trapOID
                
                .. attribute:: host
                
                	NMS/Host address
                	**type**\:  str
                
                .. attribute:: port
                
                	Trap port
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: port_xr
                
                	udp port number
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: trap_host
                
                	Trap Host
                	**type**\:  str
                
                .. attribute:: trap_oi_dinfo
                
                	Per trap OID statistics
                	**type**\: list of    :py:class:`TrapOiDinfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.TrapInfos.TrapInfo.TrapOiDinfo>`
                
                .. attribute:: trap_oid_count
                
                	Total number of OID's sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2016-06-01'

                def __init__(self):
                    super(Snmp.Information.TrapInfos.TrapInfo, self).__init__()

                    self.yang_name = "trap-info"
                    self.yang_parent_name = "trap-infos"

                    self.host = YLeaf(YType.str, "host")

                    self.port = YLeaf(YType.uint16, "port")

                    self.port_xr = YLeaf(YType.uint16, "port-xr")

                    self.trap_host = YLeaf(YType.str, "trap-host")

                    self.trap_oid_count = YLeaf(YType.uint32, "trap-oid-count")

                    self.trap_oi_dinfo = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("host",
                                    "port",
                                    "port_xr",
                                    "trap_host",
                                    "trap_oid_count") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Snmp.Information.TrapInfos.TrapInfo, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Snmp.Information.TrapInfos.TrapInfo, self).__setattr__(name, value)


                class TrapOiDinfo(Entity):
                    """
                    Per trap OID statistics
                    
                    .. attribute:: count
                    
                    	Number of traps sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: drop_count
                    
                    	Number of Traps Dropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: lasrdrop_time
                    
                    	Timestamp of latest droped
                    	**type**\:  str
                    
                    .. attribute:: lastsent_time
                    
                    	Timestamp of latest successfully sent
                    	**type**\:  str
                    
                    .. attribute:: retry_count
                    
                    	Num of times retry
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: trap_oid
                    
                    	TRAP OID
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'snmp-agent-oper'
                    _revision = '2016-06-01'

                    def __init__(self):
                        super(Snmp.Information.TrapInfos.TrapInfo.TrapOiDinfo, self).__init__()

                        self.yang_name = "trap-oi-dinfo"
                        self.yang_parent_name = "trap-info"

                        self.count = YLeaf(YType.uint32, "count")

                        self.drop_count = YLeaf(YType.uint32, "drop-count")

                        self.lasrdrop_time = YLeaf(YType.str, "lasrdrop-time")

                        self.lastsent_time = YLeaf(YType.str, "lastsent-time")

                        self.retry_count = YLeaf(YType.uint32, "retry-count")

                        self.trap_oid = YLeaf(YType.str, "trap-oid")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("count",
                                        "drop_count",
                                        "lasrdrop_time",
                                        "lastsent_time",
                                        "retry_count",
                                        "trap_oid") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Snmp.Information.TrapInfos.TrapInfo.TrapOiDinfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Snmp.Information.TrapInfos.TrapInfo.TrapOiDinfo, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.count.is_set or
                            self.drop_count.is_set or
                            self.lasrdrop_time.is_set or
                            self.lastsent_time.is_set or
                            self.retry_count.is_set or
                            self.trap_oid.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.count.yfilter != YFilter.not_set or
                            self.drop_count.yfilter != YFilter.not_set or
                            self.lasrdrop_time.yfilter != YFilter.not_set or
                            self.lastsent_time.yfilter != YFilter.not_set or
                            self.retry_count.yfilter != YFilter.not_set or
                            self.trap_oid.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "trap-oi-dinfo" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/trap-infos/trap-info/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.count.is_set or self.count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.count.get_name_leafdata())
                        if (self.drop_count.is_set or self.drop_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.drop_count.get_name_leafdata())
                        if (self.lasrdrop_time.is_set or self.lasrdrop_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.lasrdrop_time.get_name_leafdata())
                        if (self.lastsent_time.is_set or self.lastsent_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.lastsent_time.get_name_leafdata())
                        if (self.retry_count.is_set or self.retry_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.retry_count.get_name_leafdata())
                        if (self.trap_oid.is_set or self.trap_oid.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.trap_oid.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "count" or name == "drop-count" or name == "lasrdrop-time" or name == "lastsent-time" or name == "retry-count" or name == "trap-oid"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "count"):
                            self.count = value
                            self.count.value_namespace = name_space
                            self.count.value_namespace_prefix = name_space_prefix
                        if(value_path == "drop-count"):
                            self.drop_count = value
                            self.drop_count.value_namespace = name_space
                            self.drop_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "lasrdrop-time"):
                            self.lasrdrop_time = value
                            self.lasrdrop_time.value_namespace = name_space
                            self.lasrdrop_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "lastsent-time"):
                            self.lastsent_time = value
                            self.lastsent_time.value_namespace = name_space
                            self.lastsent_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "retry-count"):
                            self.retry_count = value
                            self.retry_count.value_namespace = name_space
                            self.retry_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "trap-oid"):
                            self.trap_oid = value
                            self.trap_oid.value_namespace = name_space
                            self.trap_oid.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.trap_oi_dinfo:
                        if (c.has_data()):
                            return True
                    return (
                        self.host.is_set or
                        self.port.is_set or
                        self.port_xr.is_set or
                        self.trap_host.is_set or
                        self.trap_oid_count.is_set)

                def has_operation(self):
                    for c in self.trap_oi_dinfo:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.host.yfilter != YFilter.not_set or
                        self.port.yfilter != YFilter.not_set or
                        self.port_xr.yfilter != YFilter.not_set or
                        self.trap_host.yfilter != YFilter.not_set or
                        self.trap_oid_count.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "trap-info" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/trap-infos/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.host.is_set or self.host.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.host.get_name_leafdata())
                    if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.port.get_name_leafdata())
                    if (self.port_xr.is_set or self.port_xr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.port_xr.get_name_leafdata())
                    if (self.trap_host.is_set or self.trap_host.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.trap_host.get_name_leafdata())
                    if (self.trap_oid_count.is_set or self.trap_oid_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.trap_oid_count.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "trap-oi-dinfo"):
                        for c in self.trap_oi_dinfo:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Snmp.Information.TrapInfos.TrapInfo.TrapOiDinfo()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.trap_oi_dinfo.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "trap-oi-dinfo" or name == "host" or name == "port" or name == "port-xr" or name == "trap-host" or name == "trap-oid-count"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "host"):
                        self.host = value
                        self.host.value_namespace = name_space
                        self.host.value_namespace_prefix = name_space_prefix
                    if(value_path == "port"):
                        self.port = value
                        self.port.value_namespace = name_space
                        self.port.value_namespace_prefix = name_space_prefix
                    if(value_path == "port-xr"):
                        self.port_xr = value
                        self.port_xr.value_namespace = name_space
                        self.port_xr.value_namespace_prefix = name_space_prefix
                    if(value_path == "trap-host"):
                        self.trap_host = value
                        self.trap_host.value_namespace = name_space
                        self.trap_host.value_namespace_prefix = name_space_prefix
                    if(value_path == "trap-oid-count"):
                        self.trap_oid_count = value
                        self.trap_oid_count.value_namespace = name_space
                        self.trap_oid_count.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.trap_info:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.trap_info:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "trap-infos" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "trap-info"):
                    for c in self.trap_info:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Snmp.Information.TrapInfos.TrapInfo()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.trap_info.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "trap-info"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class PollOids(Entity):
            """
            OID list for poll PDU
            
            .. attribute:: poll_oid
            
            	PDU drop info for OID
            	**type**\: list of    :py:class:`PollOid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.PollOids.PollOid>`
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                super(Snmp.Information.PollOids, self).__init__()

                self.yang_name = "poll-oids"
                self.yang_parent_name = "information"

                self.poll_oid = YList(self)

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
                            super(Snmp.Information.PollOids, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Snmp.Information.PollOids, self).__setattr__(name, value)


            class PollOid(Entity):
                """
                PDU drop info for OID
                
                .. attribute:: object_id  <key>
                
                	Object ID
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: nms
                
                	Network Managment station ipadress
                	**type**\:  list of str
                
                .. attribute:: nms_count
                
                	 Managment station count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: request_count
                
                	OID request count for each Managment station 
                	**type**\:  list of int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2016-06-01'

                def __init__(self):
                    super(Snmp.Information.PollOids.PollOid, self).__init__()

                    self.yang_name = "poll-oid"
                    self.yang_parent_name = "poll-oids"

                    self.object_id = YLeaf(YType.str, "object-id")

                    self.nms = YLeafList(YType.str, "nms")

                    self.nms_count = YLeaf(YType.uint32, "nms-count")

                    self.request_count = YLeafList(YType.uint32, "request-count")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("object_id",
                                    "nms",
                                    "nms_count",
                                    "request_count") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Snmp.Information.PollOids.PollOid, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Snmp.Information.PollOids.PollOid, self).__setattr__(name, value)

                def has_data(self):
                    for leaf in self.nms.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.request_count.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    return (
                        self.object_id.is_set or
                        self.nms_count.is_set)

                def has_operation(self):
                    for leaf in self.nms.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.request_count.getYLeafs():
                        if (leaf.is_set):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.object_id.yfilter != YFilter.not_set or
                        self.nms.yfilter != YFilter.not_set or
                        self.nms_count.yfilter != YFilter.not_set or
                        self.request_count.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "poll-oid" + "[object-id='" + self.object_id.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/poll-oids/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.object_id.is_set or self.object_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.object_id.get_name_leafdata())
                    if (self.nms_count.is_set or self.nms_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.nms_count.get_name_leafdata())

                    leaf_name_data.extend(self.nms.get_name_leafdata())

                    leaf_name_data.extend(self.request_count.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "object-id" or name == "nms" or name == "nms-count" or name == "request-count"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "object-id"):
                        self.object_id = value
                        self.object_id.value_namespace = name_space
                        self.object_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "nms"):
                        self.nms.append(value)
                    if(value_path == "nms-count"):
                        self.nms_count = value
                        self.nms_count.value_namespace = name_space
                        self.nms_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "request-count"):
                        self.request_count.append(value)

            def has_data(self):
                for c in self.poll_oid:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.poll_oid:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "poll-oids" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "poll-oid"):
                    for c in self.poll_oid:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Snmp.Information.PollOids.PollOid()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.poll_oid.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "poll-oid"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class InfomDetails(Entity):
            """
            SNMP trap OID
            
            .. attribute:: infom_detail
            
            	SNMP Trap infomation like server , port and trapOID
            	**type**\: list of    :py:class:`InfomDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.InfomDetails.InfomDetail>`
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                super(Snmp.Information.InfomDetails, self).__init__()

                self.yang_name = "infom-details"
                self.yang_parent_name = "information"

                self.infom_detail = YList(self)

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
                            super(Snmp.Information.InfomDetails, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Snmp.Information.InfomDetails, self).__setattr__(name, value)


            class InfomDetail(Entity):
                """
                SNMP Trap infomation like server , port and
                trapOID
                
                .. attribute:: host
                
                	NMS/Host address
                	**type**\:  str
                
                .. attribute:: port
                
                	Trap port
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: port_xr
                
                	udp port number
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: trap_host
                
                	Trap Host
                	**type**\:  str
                
                .. attribute:: trap_oi_dinfo
                
                	Per trap OID statistics
                	**type**\: list of    :py:class:`TrapOiDinfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.InfomDetails.InfomDetail.TrapOiDinfo>`
                
                .. attribute:: trap_oid_count
                
                	Total number of OID's sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2016-06-01'

                def __init__(self):
                    super(Snmp.Information.InfomDetails.InfomDetail, self).__init__()

                    self.yang_name = "infom-detail"
                    self.yang_parent_name = "infom-details"

                    self.host = YLeaf(YType.str, "host")

                    self.port = YLeaf(YType.uint16, "port")

                    self.port_xr = YLeaf(YType.uint16, "port-xr")

                    self.trap_host = YLeaf(YType.str, "trap-host")

                    self.trap_oid_count = YLeaf(YType.uint32, "trap-oid-count")

                    self.trap_oi_dinfo = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("host",
                                    "port",
                                    "port_xr",
                                    "trap_host",
                                    "trap_oid_count") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Snmp.Information.InfomDetails.InfomDetail, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Snmp.Information.InfomDetails.InfomDetail, self).__setattr__(name, value)


                class TrapOiDinfo(Entity):
                    """
                    Per trap OID statistics
                    
                    .. attribute:: count
                    
                    	Number of traps sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: drop_count
                    
                    	Number of Traps Dropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: lasrdrop_time
                    
                    	Timestamp of latest droped
                    	**type**\:  str
                    
                    .. attribute:: lastsent_time
                    
                    	Timestamp of latest successfully sent
                    	**type**\:  str
                    
                    .. attribute:: retry_count
                    
                    	Num of times retry
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: trap_oid
                    
                    	TRAP OID
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'snmp-agent-oper'
                    _revision = '2016-06-01'

                    def __init__(self):
                        super(Snmp.Information.InfomDetails.InfomDetail.TrapOiDinfo, self).__init__()

                        self.yang_name = "trap-oi-dinfo"
                        self.yang_parent_name = "infom-detail"

                        self.count = YLeaf(YType.uint32, "count")

                        self.drop_count = YLeaf(YType.uint32, "drop-count")

                        self.lasrdrop_time = YLeaf(YType.str, "lasrdrop-time")

                        self.lastsent_time = YLeaf(YType.str, "lastsent-time")

                        self.retry_count = YLeaf(YType.uint32, "retry-count")

                        self.trap_oid = YLeaf(YType.str, "trap-oid")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("count",
                                        "drop_count",
                                        "lasrdrop_time",
                                        "lastsent_time",
                                        "retry_count",
                                        "trap_oid") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Snmp.Information.InfomDetails.InfomDetail.TrapOiDinfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Snmp.Information.InfomDetails.InfomDetail.TrapOiDinfo, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.count.is_set or
                            self.drop_count.is_set or
                            self.lasrdrop_time.is_set or
                            self.lastsent_time.is_set or
                            self.retry_count.is_set or
                            self.trap_oid.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.count.yfilter != YFilter.not_set or
                            self.drop_count.yfilter != YFilter.not_set or
                            self.lasrdrop_time.yfilter != YFilter.not_set or
                            self.lastsent_time.yfilter != YFilter.not_set or
                            self.retry_count.yfilter != YFilter.not_set or
                            self.trap_oid.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "trap-oi-dinfo" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/infom-details/infom-detail/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.count.is_set or self.count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.count.get_name_leafdata())
                        if (self.drop_count.is_set or self.drop_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.drop_count.get_name_leafdata())
                        if (self.lasrdrop_time.is_set or self.lasrdrop_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.lasrdrop_time.get_name_leafdata())
                        if (self.lastsent_time.is_set or self.lastsent_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.lastsent_time.get_name_leafdata())
                        if (self.retry_count.is_set or self.retry_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.retry_count.get_name_leafdata())
                        if (self.trap_oid.is_set or self.trap_oid.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.trap_oid.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "count" or name == "drop-count" or name == "lasrdrop-time" or name == "lastsent-time" or name == "retry-count" or name == "trap-oid"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "count"):
                            self.count = value
                            self.count.value_namespace = name_space
                            self.count.value_namespace_prefix = name_space_prefix
                        if(value_path == "drop-count"):
                            self.drop_count = value
                            self.drop_count.value_namespace = name_space
                            self.drop_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "lasrdrop-time"):
                            self.lasrdrop_time = value
                            self.lasrdrop_time.value_namespace = name_space
                            self.lasrdrop_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "lastsent-time"):
                            self.lastsent_time = value
                            self.lastsent_time.value_namespace = name_space
                            self.lastsent_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "retry-count"):
                            self.retry_count = value
                            self.retry_count.value_namespace = name_space
                            self.retry_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "trap-oid"):
                            self.trap_oid = value
                            self.trap_oid.value_namespace = name_space
                            self.trap_oid.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.trap_oi_dinfo:
                        if (c.has_data()):
                            return True
                    return (
                        self.host.is_set or
                        self.port.is_set or
                        self.port_xr.is_set or
                        self.trap_host.is_set or
                        self.trap_oid_count.is_set)

                def has_operation(self):
                    for c in self.trap_oi_dinfo:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.host.yfilter != YFilter.not_set or
                        self.port.yfilter != YFilter.not_set or
                        self.port_xr.yfilter != YFilter.not_set or
                        self.trap_host.yfilter != YFilter.not_set or
                        self.trap_oid_count.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "infom-detail" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/infom-details/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.host.is_set or self.host.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.host.get_name_leafdata())
                    if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.port.get_name_leafdata())
                    if (self.port_xr.is_set or self.port_xr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.port_xr.get_name_leafdata())
                    if (self.trap_host.is_set or self.trap_host.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.trap_host.get_name_leafdata())
                    if (self.trap_oid_count.is_set or self.trap_oid_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.trap_oid_count.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "trap-oi-dinfo"):
                        for c in self.trap_oi_dinfo:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Snmp.Information.InfomDetails.InfomDetail.TrapOiDinfo()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.trap_oi_dinfo.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "trap-oi-dinfo" or name == "host" or name == "port" or name == "port-xr" or name == "trap-host" or name == "trap-oid-count"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "host"):
                        self.host = value
                        self.host.value_namespace = name_space
                        self.host.value_namespace_prefix = name_space_prefix
                    if(value_path == "port"):
                        self.port = value
                        self.port.value_namespace = name_space
                        self.port.value_namespace_prefix = name_space_prefix
                    if(value_path == "port-xr"):
                        self.port_xr = value
                        self.port_xr.value_namespace = name_space
                        self.port_xr.value_namespace_prefix = name_space_prefix
                    if(value_path == "trap-host"):
                        self.trap_host = value
                        self.trap_host.value_namespace = name_space
                        self.trap_host.value_namespace_prefix = name_space_prefix
                    if(value_path == "trap-oid-count"):
                        self.trap_oid_count = value
                        self.trap_oid_count.value_namespace = name_space
                        self.trap_oid_count.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.infom_detail:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.infom_detail:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "infom-details" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "infom-detail"):
                    for c in self.infom_detail:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Snmp.Information.InfomDetails.InfomDetail()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.infom_detail.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "infom-detail"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Statistics(Entity):
            """
            SNMP statistics
            
            .. attribute:: asn_parse_errors_received
            
            	snmpInASNParseErrs
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: bad_community_names_received
            
            	snmpInBadCommunityNames
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: bad_community_uses_received
            
            	snmpInBadCommunityUses
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: bad_values_received
            
            	snmpInBadValues
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: bad_values_sent
            
            	snmpOutBadValues
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: bad_versions_received
            
            	snmpInBadVersions
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: general_errors_sent
            
            	snmpOutGenErrs
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: get_next_request_sent
            
            	snmpOutGetNexts
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: get_next_requests_received
            
            	snmpInGetNexts
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: get_requests_received
            
            	snmpInGetRequests
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: get_requests_sent
            
            	snmpOutGetRequests
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: get_responses_received
            
            	snmpInGetResponses
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: get_responses_sent
            
            	snmpOutGetResponses
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: max_packet_size
            
            	snmp maximum packet size
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: no_such_names_received
            
            	snmpInNoSuchNames
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: no_such_names_sent
            
            	snmpOutNoSuchNames
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: packets_received
            
            	snmpInPkts
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: proxy_drop_count
            
            	snmpProxyDrops
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: read_only_received
            
            	snmpInReadOnlys
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: set_requests_received
            
            	snmpInSetRequests
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: set_requests_sent
            
            	snmpOutSetRequests
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: silent_drop_count
            
            	snmpSilentDrops
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: too_big_packet_received
            
            	snmpInTooBigs
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: too_big_packets_sent
            
            	snmpOutTooBigs
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: total_general_errors
            
            	snmpInGenErrs
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: total_packets_sent
            
            	snmpOutPkts
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: total_requested_variables
            
            	snmpInTotalReqVars
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: total_set_variables_received
            
            	snmpInTotalSetVars
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: traps_received
            
            	snmpInTraps
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: traps_sent
            
            	snmpOutTraps
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                super(Snmp.Information.Statistics, self).__init__()

                self.yang_name = "statistics"
                self.yang_parent_name = "information"

                self.asn_parse_errors_received = YLeaf(YType.uint32, "asn-parse-errors-received")

                self.bad_community_names_received = YLeaf(YType.uint32, "bad-community-names-received")

                self.bad_community_uses_received = YLeaf(YType.uint32, "bad-community-uses-received")

                self.bad_values_received = YLeaf(YType.uint32, "bad-values-received")

                self.bad_values_sent = YLeaf(YType.uint32, "bad-values-sent")

                self.bad_versions_received = YLeaf(YType.uint32, "bad-versions-received")

                self.general_errors_sent = YLeaf(YType.uint32, "general-errors-sent")

                self.get_next_request_sent = YLeaf(YType.uint32, "get-next-request-sent")

                self.get_next_requests_received = YLeaf(YType.uint32, "get-next-requests-received")

                self.get_requests_received = YLeaf(YType.uint32, "get-requests-received")

                self.get_requests_sent = YLeaf(YType.uint32, "get-requests-sent")

                self.get_responses_received = YLeaf(YType.uint32, "get-responses-received")

                self.get_responses_sent = YLeaf(YType.uint32, "get-responses-sent")

                self.max_packet_size = YLeaf(YType.uint32, "max-packet-size")

                self.no_such_names_received = YLeaf(YType.uint32, "no-such-names-received")

                self.no_such_names_sent = YLeaf(YType.uint32, "no-such-names-sent")

                self.packets_received = YLeaf(YType.uint32, "packets-received")

                self.proxy_drop_count = YLeaf(YType.uint32, "proxy-drop-count")

                self.read_only_received = YLeaf(YType.uint32, "read-only-received")

                self.set_requests_received = YLeaf(YType.uint32, "set-requests-received")

                self.set_requests_sent = YLeaf(YType.uint32, "set-requests-sent")

                self.silent_drop_count = YLeaf(YType.uint32, "silent-drop-count")

                self.too_big_packet_received = YLeaf(YType.uint32, "too-big-packet-received")

                self.too_big_packets_sent = YLeaf(YType.uint32, "too-big-packets-sent")

                self.total_general_errors = YLeaf(YType.uint32, "total-general-errors")

                self.total_packets_sent = YLeaf(YType.uint32, "total-packets-sent")

                self.total_requested_variables = YLeaf(YType.uint32, "total-requested-variables")

                self.total_set_variables_received = YLeaf(YType.uint32, "total-set-variables-received")

                self.traps_received = YLeaf(YType.uint32, "traps-received")

                self.traps_sent = YLeaf(YType.uint32, "traps-sent")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("asn_parse_errors_received",
                                "bad_community_names_received",
                                "bad_community_uses_received",
                                "bad_values_received",
                                "bad_values_sent",
                                "bad_versions_received",
                                "general_errors_sent",
                                "get_next_request_sent",
                                "get_next_requests_received",
                                "get_requests_received",
                                "get_requests_sent",
                                "get_responses_received",
                                "get_responses_sent",
                                "max_packet_size",
                                "no_such_names_received",
                                "no_such_names_sent",
                                "packets_received",
                                "proxy_drop_count",
                                "read_only_received",
                                "set_requests_received",
                                "set_requests_sent",
                                "silent_drop_count",
                                "too_big_packet_received",
                                "too_big_packets_sent",
                                "total_general_errors",
                                "total_packets_sent",
                                "total_requested_variables",
                                "total_set_variables_received",
                                "traps_received",
                                "traps_sent") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Snmp.Information.Statistics, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Snmp.Information.Statistics, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.asn_parse_errors_received.is_set or
                    self.bad_community_names_received.is_set or
                    self.bad_community_uses_received.is_set or
                    self.bad_values_received.is_set or
                    self.bad_values_sent.is_set or
                    self.bad_versions_received.is_set or
                    self.general_errors_sent.is_set or
                    self.get_next_request_sent.is_set or
                    self.get_next_requests_received.is_set or
                    self.get_requests_received.is_set or
                    self.get_requests_sent.is_set or
                    self.get_responses_received.is_set or
                    self.get_responses_sent.is_set or
                    self.max_packet_size.is_set or
                    self.no_such_names_received.is_set or
                    self.no_such_names_sent.is_set or
                    self.packets_received.is_set or
                    self.proxy_drop_count.is_set or
                    self.read_only_received.is_set or
                    self.set_requests_received.is_set or
                    self.set_requests_sent.is_set or
                    self.silent_drop_count.is_set or
                    self.too_big_packet_received.is_set or
                    self.too_big_packets_sent.is_set or
                    self.total_general_errors.is_set or
                    self.total_packets_sent.is_set or
                    self.total_requested_variables.is_set or
                    self.total_set_variables_received.is_set or
                    self.traps_received.is_set or
                    self.traps_sent.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.asn_parse_errors_received.yfilter != YFilter.not_set or
                    self.bad_community_names_received.yfilter != YFilter.not_set or
                    self.bad_community_uses_received.yfilter != YFilter.not_set or
                    self.bad_values_received.yfilter != YFilter.not_set or
                    self.bad_values_sent.yfilter != YFilter.not_set or
                    self.bad_versions_received.yfilter != YFilter.not_set or
                    self.general_errors_sent.yfilter != YFilter.not_set or
                    self.get_next_request_sent.yfilter != YFilter.not_set or
                    self.get_next_requests_received.yfilter != YFilter.not_set or
                    self.get_requests_received.yfilter != YFilter.not_set or
                    self.get_requests_sent.yfilter != YFilter.not_set or
                    self.get_responses_received.yfilter != YFilter.not_set or
                    self.get_responses_sent.yfilter != YFilter.not_set or
                    self.max_packet_size.yfilter != YFilter.not_set or
                    self.no_such_names_received.yfilter != YFilter.not_set or
                    self.no_such_names_sent.yfilter != YFilter.not_set or
                    self.packets_received.yfilter != YFilter.not_set or
                    self.proxy_drop_count.yfilter != YFilter.not_set or
                    self.read_only_received.yfilter != YFilter.not_set or
                    self.set_requests_received.yfilter != YFilter.not_set or
                    self.set_requests_sent.yfilter != YFilter.not_set or
                    self.silent_drop_count.yfilter != YFilter.not_set or
                    self.too_big_packet_received.yfilter != YFilter.not_set or
                    self.too_big_packets_sent.yfilter != YFilter.not_set or
                    self.total_general_errors.yfilter != YFilter.not_set or
                    self.total_packets_sent.yfilter != YFilter.not_set or
                    self.total_requested_variables.yfilter != YFilter.not_set or
                    self.total_set_variables_received.yfilter != YFilter.not_set or
                    self.traps_received.yfilter != YFilter.not_set or
                    self.traps_sent.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "statistics" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.asn_parse_errors_received.is_set or self.asn_parse_errors_received.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.asn_parse_errors_received.get_name_leafdata())
                if (self.bad_community_names_received.is_set or self.bad_community_names_received.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bad_community_names_received.get_name_leafdata())
                if (self.bad_community_uses_received.is_set or self.bad_community_uses_received.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bad_community_uses_received.get_name_leafdata())
                if (self.bad_values_received.is_set or self.bad_values_received.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bad_values_received.get_name_leafdata())
                if (self.bad_values_sent.is_set or self.bad_values_sent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bad_values_sent.get_name_leafdata())
                if (self.bad_versions_received.is_set or self.bad_versions_received.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bad_versions_received.get_name_leafdata())
                if (self.general_errors_sent.is_set or self.general_errors_sent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.general_errors_sent.get_name_leafdata())
                if (self.get_next_request_sent.is_set or self.get_next_request_sent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.get_next_request_sent.get_name_leafdata())
                if (self.get_next_requests_received.is_set or self.get_next_requests_received.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.get_next_requests_received.get_name_leafdata())
                if (self.get_requests_received.is_set or self.get_requests_received.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.get_requests_received.get_name_leafdata())
                if (self.get_requests_sent.is_set or self.get_requests_sent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.get_requests_sent.get_name_leafdata())
                if (self.get_responses_received.is_set or self.get_responses_received.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.get_responses_received.get_name_leafdata())
                if (self.get_responses_sent.is_set or self.get_responses_sent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.get_responses_sent.get_name_leafdata())
                if (self.max_packet_size.is_set or self.max_packet_size.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.max_packet_size.get_name_leafdata())
                if (self.no_such_names_received.is_set or self.no_such_names_received.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.no_such_names_received.get_name_leafdata())
                if (self.no_such_names_sent.is_set or self.no_such_names_sent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.no_such_names_sent.get_name_leafdata())
                if (self.packets_received.is_set or self.packets_received.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.packets_received.get_name_leafdata())
                if (self.proxy_drop_count.is_set or self.proxy_drop_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.proxy_drop_count.get_name_leafdata())
                if (self.read_only_received.is_set or self.read_only_received.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.read_only_received.get_name_leafdata())
                if (self.set_requests_received.is_set or self.set_requests_received.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.set_requests_received.get_name_leafdata())
                if (self.set_requests_sent.is_set or self.set_requests_sent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.set_requests_sent.get_name_leafdata())
                if (self.silent_drop_count.is_set or self.silent_drop_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.silent_drop_count.get_name_leafdata())
                if (self.too_big_packet_received.is_set or self.too_big_packet_received.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.too_big_packet_received.get_name_leafdata())
                if (self.too_big_packets_sent.is_set or self.too_big_packets_sent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.too_big_packets_sent.get_name_leafdata())
                if (self.total_general_errors.is_set or self.total_general_errors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.total_general_errors.get_name_leafdata())
                if (self.total_packets_sent.is_set or self.total_packets_sent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.total_packets_sent.get_name_leafdata())
                if (self.total_requested_variables.is_set or self.total_requested_variables.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.total_requested_variables.get_name_leafdata())
                if (self.total_set_variables_received.is_set or self.total_set_variables_received.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.total_set_variables_received.get_name_leafdata())
                if (self.traps_received.is_set or self.traps_received.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.traps_received.get_name_leafdata())
                if (self.traps_sent.is_set or self.traps_sent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.traps_sent.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "asn-parse-errors-received" or name == "bad-community-names-received" or name == "bad-community-uses-received" or name == "bad-values-received" or name == "bad-values-sent" or name == "bad-versions-received" or name == "general-errors-sent" or name == "get-next-request-sent" or name == "get-next-requests-received" or name == "get-requests-received" or name == "get-requests-sent" or name == "get-responses-received" or name == "get-responses-sent" or name == "max-packet-size" or name == "no-such-names-received" or name == "no-such-names-sent" or name == "packets-received" or name == "proxy-drop-count" or name == "read-only-received" or name == "set-requests-received" or name == "set-requests-sent" or name == "silent-drop-count" or name == "too-big-packet-received" or name == "too-big-packets-sent" or name == "total-general-errors" or name == "total-packets-sent" or name == "total-requested-variables" or name == "total-set-variables-received" or name == "traps-received" or name == "traps-sent"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "asn-parse-errors-received"):
                    self.asn_parse_errors_received = value
                    self.asn_parse_errors_received.value_namespace = name_space
                    self.asn_parse_errors_received.value_namespace_prefix = name_space_prefix
                if(value_path == "bad-community-names-received"):
                    self.bad_community_names_received = value
                    self.bad_community_names_received.value_namespace = name_space
                    self.bad_community_names_received.value_namespace_prefix = name_space_prefix
                if(value_path == "bad-community-uses-received"):
                    self.bad_community_uses_received = value
                    self.bad_community_uses_received.value_namespace = name_space
                    self.bad_community_uses_received.value_namespace_prefix = name_space_prefix
                if(value_path == "bad-values-received"):
                    self.bad_values_received = value
                    self.bad_values_received.value_namespace = name_space
                    self.bad_values_received.value_namespace_prefix = name_space_prefix
                if(value_path == "bad-values-sent"):
                    self.bad_values_sent = value
                    self.bad_values_sent.value_namespace = name_space
                    self.bad_values_sent.value_namespace_prefix = name_space_prefix
                if(value_path == "bad-versions-received"):
                    self.bad_versions_received = value
                    self.bad_versions_received.value_namespace = name_space
                    self.bad_versions_received.value_namespace_prefix = name_space_prefix
                if(value_path == "general-errors-sent"):
                    self.general_errors_sent = value
                    self.general_errors_sent.value_namespace = name_space
                    self.general_errors_sent.value_namespace_prefix = name_space_prefix
                if(value_path == "get-next-request-sent"):
                    self.get_next_request_sent = value
                    self.get_next_request_sent.value_namespace = name_space
                    self.get_next_request_sent.value_namespace_prefix = name_space_prefix
                if(value_path == "get-next-requests-received"):
                    self.get_next_requests_received = value
                    self.get_next_requests_received.value_namespace = name_space
                    self.get_next_requests_received.value_namespace_prefix = name_space_prefix
                if(value_path == "get-requests-received"):
                    self.get_requests_received = value
                    self.get_requests_received.value_namespace = name_space
                    self.get_requests_received.value_namespace_prefix = name_space_prefix
                if(value_path == "get-requests-sent"):
                    self.get_requests_sent = value
                    self.get_requests_sent.value_namespace = name_space
                    self.get_requests_sent.value_namespace_prefix = name_space_prefix
                if(value_path == "get-responses-received"):
                    self.get_responses_received = value
                    self.get_responses_received.value_namespace = name_space
                    self.get_responses_received.value_namespace_prefix = name_space_prefix
                if(value_path == "get-responses-sent"):
                    self.get_responses_sent = value
                    self.get_responses_sent.value_namespace = name_space
                    self.get_responses_sent.value_namespace_prefix = name_space_prefix
                if(value_path == "max-packet-size"):
                    self.max_packet_size = value
                    self.max_packet_size.value_namespace = name_space
                    self.max_packet_size.value_namespace_prefix = name_space_prefix
                if(value_path == "no-such-names-received"):
                    self.no_such_names_received = value
                    self.no_such_names_received.value_namespace = name_space
                    self.no_such_names_received.value_namespace_prefix = name_space_prefix
                if(value_path == "no-such-names-sent"):
                    self.no_such_names_sent = value
                    self.no_such_names_sent.value_namespace = name_space
                    self.no_such_names_sent.value_namespace_prefix = name_space_prefix
                if(value_path == "packets-received"):
                    self.packets_received = value
                    self.packets_received.value_namespace = name_space
                    self.packets_received.value_namespace_prefix = name_space_prefix
                if(value_path == "proxy-drop-count"):
                    self.proxy_drop_count = value
                    self.proxy_drop_count.value_namespace = name_space
                    self.proxy_drop_count.value_namespace_prefix = name_space_prefix
                if(value_path == "read-only-received"):
                    self.read_only_received = value
                    self.read_only_received.value_namespace = name_space
                    self.read_only_received.value_namespace_prefix = name_space_prefix
                if(value_path == "set-requests-received"):
                    self.set_requests_received = value
                    self.set_requests_received.value_namespace = name_space
                    self.set_requests_received.value_namespace_prefix = name_space_prefix
                if(value_path == "set-requests-sent"):
                    self.set_requests_sent = value
                    self.set_requests_sent.value_namespace = name_space
                    self.set_requests_sent.value_namespace_prefix = name_space_prefix
                if(value_path == "silent-drop-count"):
                    self.silent_drop_count = value
                    self.silent_drop_count.value_namespace = name_space
                    self.silent_drop_count.value_namespace_prefix = name_space_prefix
                if(value_path == "too-big-packet-received"):
                    self.too_big_packet_received = value
                    self.too_big_packet_received.value_namespace = name_space
                    self.too_big_packet_received.value_namespace_prefix = name_space_prefix
                if(value_path == "too-big-packets-sent"):
                    self.too_big_packets_sent = value
                    self.too_big_packets_sent.value_namespace = name_space
                    self.too_big_packets_sent.value_namespace_prefix = name_space_prefix
                if(value_path == "total-general-errors"):
                    self.total_general_errors = value
                    self.total_general_errors.value_namespace = name_space
                    self.total_general_errors.value_namespace_prefix = name_space_prefix
                if(value_path == "total-packets-sent"):
                    self.total_packets_sent = value
                    self.total_packets_sent.value_namespace = name_space
                    self.total_packets_sent.value_namespace_prefix = name_space_prefix
                if(value_path == "total-requested-variables"):
                    self.total_requested_variables = value
                    self.total_requested_variables.value_namespace = name_space
                    self.total_requested_variables.value_namespace_prefix = name_space_prefix
                if(value_path == "total-set-variables-received"):
                    self.total_set_variables_received = value
                    self.total_set_variables_received.value_namespace = name_space
                    self.total_set_variables_received.value_namespace_prefix = name_space_prefix
                if(value_path == "traps-received"):
                    self.traps_received = value
                    self.traps_received.value_namespace = name_space
                    self.traps_received.value_namespace_prefix = name_space_prefix
                if(value_path == "traps-sent"):
                    self.traps_sent = value
                    self.traps_sent.value_namespace = name_space
                    self.traps_sent.value_namespace_prefix = name_space_prefix


        class IncomingQueue(Entity):
            """
            Incoming queue details 
            
            .. attribute:: inq_entry
            
            	Each Entry Details
            	**type**\: list of    :py:class:`InqEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.IncomingQueue.InqEntry>`
            
            .. attribute:: queue_count
            
            	Number of NMS Queues Exist
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                super(Snmp.Information.IncomingQueue, self).__init__()

                self.yang_name = "incoming-queue"
                self.yang_parent_name = "information"

                self.queue_count = YLeaf(YType.uint32, "queue-count")

                self.inq_entry = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("queue_count") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Snmp.Information.IncomingQueue, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Snmp.Information.IncomingQueue, self).__setattr__(name, value)


            class InqEntry(Entity):
                """
                Each Entry Details.
                
                .. attribute:: address_of_queue
                
                	Address of NMS Q
                	**type**\:  str
                
                .. attribute:: last_access_time
                
                	Last Access time of Each Queue
                	**type**\:  str
                
                .. attribute:: priority
                
                	Priority of Each Queue
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: processed_request_count
                
                	Processed request Count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: request_count
                
                	Request Count of Each Queue
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2016-06-01'

                def __init__(self):
                    super(Snmp.Information.IncomingQueue.InqEntry, self).__init__()

                    self.yang_name = "inq-entry"
                    self.yang_parent_name = "incoming-queue"

                    self.address_of_queue = YLeaf(YType.str, "address-of-queue")

                    self.last_access_time = YLeaf(YType.str, "last-access-time")

                    self.priority = YLeaf(YType.uint8, "priority")

                    self.processed_request_count = YLeaf(YType.uint32, "processed-request-count")

                    self.request_count = YLeaf(YType.uint32, "request-count")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("address_of_queue",
                                    "last_access_time",
                                    "priority",
                                    "processed_request_count",
                                    "request_count") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Snmp.Information.IncomingQueue.InqEntry, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Snmp.Information.IncomingQueue.InqEntry, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.address_of_queue.is_set or
                        self.last_access_time.is_set or
                        self.priority.is_set or
                        self.processed_request_count.is_set or
                        self.request_count.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.address_of_queue.yfilter != YFilter.not_set or
                        self.last_access_time.yfilter != YFilter.not_set or
                        self.priority.yfilter != YFilter.not_set or
                        self.processed_request_count.yfilter != YFilter.not_set or
                        self.request_count.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "inq-entry" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/incoming-queue/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.address_of_queue.is_set or self.address_of_queue.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.address_of_queue.get_name_leafdata())
                    if (self.last_access_time.is_set or self.last_access_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.last_access_time.get_name_leafdata())
                    if (self.priority.is_set or self.priority.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.priority.get_name_leafdata())
                    if (self.processed_request_count.is_set or self.processed_request_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.processed_request_count.get_name_leafdata())
                    if (self.request_count.is_set or self.request_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.request_count.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "address-of-queue" or name == "last-access-time" or name == "priority" or name == "processed-request-count" or name == "request-count"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "address-of-queue"):
                        self.address_of_queue = value
                        self.address_of_queue.value_namespace = name_space
                        self.address_of_queue.value_namespace_prefix = name_space_prefix
                    if(value_path == "last-access-time"):
                        self.last_access_time = value
                        self.last_access_time.value_namespace = name_space
                        self.last_access_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "priority"):
                        self.priority = value
                        self.priority.value_namespace = name_space
                        self.priority.value_namespace_prefix = name_space_prefix
                    if(value_path == "processed-request-count"):
                        self.processed_request_count = value
                        self.processed_request_count.value_namespace = name_space
                        self.processed_request_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "request-count"):
                        self.request_count = value
                        self.request_count.value_namespace = name_space
                        self.request_count.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.inq_entry:
                    if (c.has_data()):
                        return True
                return self.queue_count.is_set

            def has_operation(self):
                for c in self.inq_entry:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.queue_count.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "incoming-queue" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.queue_count.is_set or self.queue_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.queue_count.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "inq-entry"):
                    for c in self.inq_entry:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Snmp.Information.IncomingQueue.InqEntry()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.inq_entry.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "inq-entry" or name == "queue-count"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "queue-count"):
                    self.queue_count = value
                    self.queue_count.value_namespace = name_space
                    self.queue_count.value_namespace_prefix = name_space_prefix


        class ContextMapping(Entity):
            """
            Context name, features name, topology name,
            instance
            
            .. attribute:: contex_mapping
            
            	Context Mapping
            	**type**\: list of    :py:class:`ContexMapping <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.ContextMapping.ContexMapping>`
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                super(Snmp.Information.ContextMapping, self).__init__()

                self.yang_name = "context-mapping"
                self.yang_parent_name = "information"

                self.contex_mapping = YList(self)

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
                            super(Snmp.Information.ContextMapping, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Snmp.Information.ContextMapping, self).__setattr__(name, value)


            class ContexMapping(Entity):
                """
                Context Mapping
                
                .. attribute:: context
                
                	Context name
                	**type**\:  str
                
                .. attribute:: feature
                
                	Feature
                	**type**\:  str
                
                .. attribute:: feature_name
                
                	Feature name
                	**type**\:  str
                
                .. attribute:: instance
                
                	Instance name
                	**type**\:  str
                
                .. attribute:: topology
                
                	Topology name
                	**type**\:  str
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2016-06-01'

                def __init__(self):
                    super(Snmp.Information.ContextMapping.ContexMapping, self).__init__()

                    self.yang_name = "contex-mapping"
                    self.yang_parent_name = "context-mapping"

                    self.context = YLeaf(YType.str, "context")

                    self.feature = YLeaf(YType.str, "feature")

                    self.feature_name = YLeaf(YType.str, "feature-name")

                    self.instance = YLeaf(YType.str, "instance")

                    self.topology = YLeaf(YType.str, "topology")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("context",
                                    "feature",
                                    "feature_name",
                                    "instance",
                                    "topology") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Snmp.Information.ContextMapping.ContexMapping, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Snmp.Information.ContextMapping.ContexMapping, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.context.is_set or
                        self.feature.is_set or
                        self.feature_name.is_set or
                        self.instance.is_set or
                        self.topology.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.context.yfilter != YFilter.not_set or
                        self.feature.yfilter != YFilter.not_set or
                        self.feature_name.yfilter != YFilter.not_set or
                        self.instance.yfilter != YFilter.not_set or
                        self.topology.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "contex-mapping" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/context-mapping/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.context.is_set or self.context.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.context.get_name_leafdata())
                    if (self.feature.is_set or self.feature.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.feature.get_name_leafdata())
                    if (self.feature_name.is_set or self.feature_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.feature_name.get_name_leafdata())
                    if (self.instance.is_set or self.instance.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.instance.get_name_leafdata())
                    if (self.topology.is_set or self.topology.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.topology.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "context" or name == "feature" or name == "feature-name" or name == "instance" or name == "topology"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "context"):
                        self.context = value
                        self.context.value_namespace = name_space
                        self.context.value_namespace_prefix = name_space_prefix
                    if(value_path == "feature"):
                        self.feature = value
                        self.feature.value_namespace = name_space
                        self.feature.value_namespace_prefix = name_space_prefix
                    if(value_path == "feature-name"):
                        self.feature_name = value
                        self.feature_name.value_namespace = name_space
                        self.feature_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "instance"):
                        self.instance = value
                        self.instance.value_namespace = name_space
                        self.instance.value_namespace_prefix = name_space_prefix
                    if(value_path == "topology"):
                        self.topology = value
                        self.topology.value_namespace = name_space
                        self.topology.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.contex_mapping:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.contex_mapping:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "context-mapping" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "contex-mapping"):
                    for c in self.contex_mapping:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Snmp.Information.ContextMapping.ContexMapping()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.contex_mapping.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "contex-mapping"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class TrapOids(Entity):
            """
            SNMP trap OID
            
            .. attribute:: trap_oid
            
            	SNMP trap 
            	**type**\: list of    :py:class:`TrapOid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.TrapOids.TrapOid>`
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                super(Snmp.Information.TrapOids, self).__init__()

                self.yang_name = "trap-oids"
                self.yang_parent_name = "information"

                self.trap_oid = YList(self)

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
                            super(Snmp.Information.TrapOids, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Snmp.Information.TrapOids, self).__setattr__(name, value)


            class TrapOid(Entity):
                """
                SNMP trap 
                
                .. attribute:: trap_oid  <key>
                
                	Trap object ID
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: trap_oid_count
                
                	Total number of OID's sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: trap_oid_xr
                
                	TRAP OID
                	**type**\:  str
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2016-06-01'

                def __init__(self):
                    super(Snmp.Information.TrapOids.TrapOid, self).__init__()

                    self.yang_name = "trap-oid"
                    self.yang_parent_name = "trap-oids"

                    self.trap_oid = YLeaf(YType.str, "trap-oid")

                    self.trap_oid_count = YLeaf(YType.uint32, "trap-oid-count")

                    self.trap_oid_xr = YLeaf(YType.str, "trap-oid-xr")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("trap_oid",
                                    "trap_oid_count",
                                    "trap_oid_xr") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Snmp.Information.TrapOids.TrapOid, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Snmp.Information.TrapOids.TrapOid, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.trap_oid.is_set or
                        self.trap_oid_count.is_set or
                        self.trap_oid_xr.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.trap_oid.yfilter != YFilter.not_set or
                        self.trap_oid_count.yfilter != YFilter.not_set or
                        self.trap_oid_xr.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "trap-oid" + "[trap-oid='" + self.trap_oid.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/trap-oids/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.trap_oid.is_set or self.trap_oid.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.trap_oid.get_name_leafdata())
                    if (self.trap_oid_count.is_set or self.trap_oid_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.trap_oid_count.get_name_leafdata())
                    if (self.trap_oid_xr.is_set or self.trap_oid_xr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.trap_oid_xr.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "trap-oid" or name == "trap-oid-count" or name == "trap-oid-xr"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "trap-oid"):
                        self.trap_oid = value
                        self.trap_oid.value_namespace = name_space
                        self.trap_oid.value_namespace_prefix = name_space_prefix
                    if(value_path == "trap-oid-count"):
                        self.trap_oid_count = value
                        self.trap_oid_count.value_namespace = name_space
                        self.trap_oid_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "trap-oid-xr"):
                        self.trap_oid_xr = value
                        self.trap_oid_xr.value_namespace = name_space
                        self.trap_oid_xr.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.trap_oid:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.trap_oid:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "trap-oids" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "trap-oid"):
                    for c in self.trap_oid:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Snmp.Information.TrapOids.TrapOid()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.trap_oid.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "trap-oid"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class NmSpackets(Entity):
            """
            SNMP overload statistics 
            
            .. attribute:: nm_spacket
            
            	NMS packet drop count
            	**type**\: list of    :py:class:`NmSpacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.NmSpackets.NmSpacket>`
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                super(Snmp.Information.NmSpackets, self).__init__()

                self.yang_name = "nm-spackets"
                self.yang_parent_name = "information"

                self.nm_spacket = YList(self)

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
                            super(Snmp.Information.NmSpackets, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Snmp.Information.NmSpackets, self).__setattr__(name, value)


            class NmSpacket(Entity):
                """
                NMS packet drop count
                
                .. attribute:: packetcount  <key>
                
                	NMS packet drop count
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: number_of_nmsq_pkts_dropped
                
                	Number of packets which are currently enqueued within the NMS queues
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: number_of_pkts_dropped
                
                	Number of packets dropped
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: overload_end_time
                
                	Time of overload contol End
                	**type**\:  str
                
                .. attribute:: overload_start_time
                
                	Time of overload contol begin
                	**type**\:  str
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2016-06-01'

                def __init__(self):
                    super(Snmp.Information.NmSpackets.NmSpacket, self).__init__()

                    self.yang_name = "nm-spacket"
                    self.yang_parent_name = "nm-spackets"

                    self.packetcount = YLeaf(YType.str, "packetcount")

                    self.number_of_nmsq_pkts_dropped = YLeaf(YType.uint32, "number-of-nmsq-pkts-dropped")

                    self.number_of_pkts_dropped = YLeaf(YType.uint32, "number-of-pkts-dropped")

                    self.overload_end_time = YLeaf(YType.str, "overload-end-time")

                    self.overload_start_time = YLeaf(YType.str, "overload-start-time")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("packetcount",
                                    "number_of_nmsq_pkts_dropped",
                                    "number_of_pkts_dropped",
                                    "overload_end_time",
                                    "overload_start_time") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Snmp.Information.NmSpackets.NmSpacket, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Snmp.Information.NmSpackets.NmSpacket, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.packetcount.is_set or
                        self.number_of_nmsq_pkts_dropped.is_set or
                        self.number_of_pkts_dropped.is_set or
                        self.overload_end_time.is_set or
                        self.overload_start_time.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.packetcount.yfilter != YFilter.not_set or
                        self.number_of_nmsq_pkts_dropped.yfilter != YFilter.not_set or
                        self.number_of_pkts_dropped.yfilter != YFilter.not_set or
                        self.overload_end_time.yfilter != YFilter.not_set or
                        self.overload_start_time.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "nm-spacket" + "[packetcount='" + self.packetcount.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/nm-spackets/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.packetcount.is_set or self.packetcount.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.packetcount.get_name_leafdata())
                    if (self.number_of_nmsq_pkts_dropped.is_set or self.number_of_nmsq_pkts_dropped.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.number_of_nmsq_pkts_dropped.get_name_leafdata())
                    if (self.number_of_pkts_dropped.is_set or self.number_of_pkts_dropped.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.number_of_pkts_dropped.get_name_leafdata())
                    if (self.overload_end_time.is_set or self.overload_end_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.overload_end_time.get_name_leafdata())
                    if (self.overload_start_time.is_set or self.overload_start_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.overload_start_time.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "packetcount" or name == "number-of-nmsq-pkts-dropped" or name == "number-of-pkts-dropped" or name == "overload-end-time" or name == "overload-start-time"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "packetcount"):
                        self.packetcount = value
                        self.packetcount.value_namespace = name_space
                        self.packetcount.value_namespace_prefix = name_space_prefix
                    if(value_path == "number-of-nmsq-pkts-dropped"):
                        self.number_of_nmsq_pkts_dropped = value
                        self.number_of_nmsq_pkts_dropped.value_namespace = name_space
                        self.number_of_nmsq_pkts_dropped.value_namespace_prefix = name_space_prefix
                    if(value_path == "number-of-pkts-dropped"):
                        self.number_of_pkts_dropped = value
                        self.number_of_pkts_dropped.value_namespace = name_space
                        self.number_of_pkts_dropped.value_namespace_prefix = name_space_prefix
                    if(value_path == "overload-end-time"):
                        self.overload_end_time = value
                        self.overload_end_time.value_namespace = name_space
                        self.overload_end_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "overload-start-time"):
                        self.overload_start_time = value
                        self.overload_start_time.value_namespace = name_space
                        self.overload_start_time.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.nm_spacket:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.nm_spacket:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "nm-spackets" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "nm-spacket"):
                    for c in self.nm_spacket:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Snmp.Information.NmSpackets.NmSpacket()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.nm_spacket.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "nm-spacket"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Mibs(Entity):
            """
            List of MIBS supported on the system
            
            .. attribute:: mib
            
            	SNMP MIB Name
            	**type**\: list of    :py:class:`Mib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Mibs.Mib>`
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                super(Snmp.Information.Mibs, self).__init__()

                self.yang_name = "mibs"
                self.yang_parent_name = "information"

                self.mib = YList(self)

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
                            super(Snmp.Information.Mibs, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Snmp.Information.Mibs, self).__setattr__(name, value)


            class Mib(Entity):
                """
                SNMP MIB Name
                
                .. attribute:: name  <key>
                
                	MIB Name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: mib_information
                
                	MIB state and information
                	**type**\:   :py:class:`MibInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Mibs.Mib.MibInformation>`
                
                .. attribute:: oids
                
                	List of OIDs per MIB
                	**type**\:   :py:class:`Oids <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Mibs.Mib.Oids>`
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2016-06-01'

                def __init__(self):
                    super(Snmp.Information.Mibs.Mib, self).__init__()

                    self.yang_name = "mib"
                    self.yang_parent_name = "mibs"

                    self.name = YLeaf(YType.str, "name")

                    self.mib_information = Snmp.Information.Mibs.Mib.MibInformation()
                    self.mib_information.parent = self
                    self._children_name_map["mib_information"] = "mib-information"
                    self._children_yang_names.add("mib-information")

                    self.oids = Snmp.Information.Mibs.Mib.Oids()
                    self.oids.parent = self
                    self._children_name_map["oids"] = "oids"
                    self._children_yang_names.add("oids")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Snmp.Information.Mibs.Mib, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Snmp.Information.Mibs.Mib, self).__setattr__(name, value)


                class Oids(Entity):
                    """
                    List of OIDs per MIB
                    
                    .. attribute:: oid
                    
                    	Object identifiers of a mib
                    	**type**\: list of    :py:class:`Oid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Mibs.Mib.Oids.Oid>`
                    
                    

                    """

                    _prefix = 'snmp-agent-oper'
                    _revision = '2016-06-01'

                    def __init__(self):
                        super(Snmp.Information.Mibs.Mib.Oids, self).__init__()

                        self.yang_name = "oids"
                        self.yang_parent_name = "mib"

                        self.oid = YList(self)

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
                                    super(Snmp.Information.Mibs.Mib.Oids, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Snmp.Information.Mibs.Mib.Oids, self).__setattr__(name, value)


                    class Oid(Entity):
                        """
                        Object identifiers of a mib
                        
                        .. attribute:: oid  <key>
                        
                        	Object Identifier
                        	**type**\:  str
                        
                        .. attribute:: oid_name
                        
                        	MIB OID Name
                        	**type**\:  str
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'snmp-agent-oper'
                        _revision = '2016-06-01'

                        def __init__(self):
                            super(Snmp.Information.Mibs.Mib.Oids.Oid, self).__init__()

                            self.yang_name = "oid"
                            self.yang_parent_name = "oids"

                            self.oid = YLeaf(YType.str, "oid")

                            self.oid_name = YLeaf(YType.str, "oid-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("oid",
                                            "oid_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Snmp.Information.Mibs.Mib.Oids.Oid, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Snmp.Information.Mibs.Mib.Oids.Oid, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.oid.is_set or
                                self.oid_name.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.oid.yfilter != YFilter.not_set or
                                self.oid_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "oid" + "[oid='" + self.oid.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.oid.is_set or self.oid.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.oid.get_name_leafdata())
                            if (self.oid_name.is_set or self.oid_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.oid_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "oid" or name == "oid-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "oid"):
                                self.oid = value
                                self.oid.value_namespace = name_space
                                self.oid.value_namespace_prefix = name_space_prefix
                            if(value_path == "oid-name"):
                                self.oid_name = value
                                self.oid_name.value_namespace = name_space
                                self.oid_name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.oid:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.oid:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "oids" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "oid"):
                            for c in self.oid:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Snmp.Information.Mibs.Mib.Oids.Oid()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.oid.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "oid"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class MibInformation(Entity):
                    """
                    MIB state and information
                    
                    .. attribute:: dll_capabilities
                    
                    	DLL capabilities
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: dll_name
                    
                    	MIB DLL filename, non\-DLL MIBs will have no value
                    	**type**\:  str
                    
                    .. attribute:: is_mib_loaded
                    
                    	TRUE if MIB DLL is currently loaded, will always be TRUE for non\-DLL MIBs
                    	**type**\:  bool
                    
                    .. attribute:: load_time
                    
                    	Load time
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: mib_config_filename
                    
                    	MIB config filename, non\-DLL MIBs will have no value
                    	**type**\:  str
                    
                    .. attribute:: mib_name
                    
                    	Name of the MIB module
                    	**type**\:  str
                    
                    .. attribute:: timeout
                    
                    	TRUE is mib is in phase 1 timeout
                    	**type**\:  bool
                    
                    .. attribute:: trap_strings
                    
                    	List of trapstring configured
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'snmp-agent-oper'
                    _revision = '2016-06-01'

                    def __init__(self):
                        super(Snmp.Information.Mibs.Mib.MibInformation, self).__init__()

                        self.yang_name = "mib-information"
                        self.yang_parent_name = "mib"

                        self.dll_capabilities = YLeaf(YType.uint32, "dll-capabilities")

                        self.dll_name = YLeaf(YType.str, "dll-name")

                        self.is_mib_loaded = YLeaf(YType.boolean, "is-mib-loaded")

                        self.load_time = YLeaf(YType.uint32, "load-time")

                        self.mib_config_filename = YLeaf(YType.str, "mib-config-filename")

                        self.mib_name = YLeaf(YType.str, "mib-name")

                        self.timeout = YLeaf(YType.boolean, "timeout")

                        self.trap_strings = YLeaf(YType.str, "trap-strings")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("dll_capabilities",
                                        "dll_name",
                                        "is_mib_loaded",
                                        "load_time",
                                        "mib_config_filename",
                                        "mib_name",
                                        "timeout",
                                        "trap_strings") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Snmp.Information.Mibs.Mib.MibInformation, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Snmp.Information.Mibs.Mib.MibInformation, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.dll_capabilities.is_set or
                            self.dll_name.is_set or
                            self.is_mib_loaded.is_set or
                            self.load_time.is_set or
                            self.mib_config_filename.is_set or
                            self.mib_name.is_set or
                            self.timeout.is_set or
                            self.trap_strings.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.dll_capabilities.yfilter != YFilter.not_set or
                            self.dll_name.yfilter != YFilter.not_set or
                            self.is_mib_loaded.yfilter != YFilter.not_set or
                            self.load_time.yfilter != YFilter.not_set or
                            self.mib_config_filename.yfilter != YFilter.not_set or
                            self.mib_name.yfilter != YFilter.not_set or
                            self.timeout.yfilter != YFilter.not_set or
                            self.trap_strings.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "mib-information" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.dll_capabilities.is_set or self.dll_capabilities.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dll_capabilities.get_name_leafdata())
                        if (self.dll_name.is_set or self.dll_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dll_name.get_name_leafdata())
                        if (self.is_mib_loaded.is_set or self.is_mib_loaded.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_mib_loaded.get_name_leafdata())
                        if (self.load_time.is_set or self.load_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.load_time.get_name_leafdata())
                        if (self.mib_config_filename.is_set or self.mib_config_filename.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mib_config_filename.get_name_leafdata())
                        if (self.mib_name.is_set or self.mib_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mib_name.get_name_leafdata())
                        if (self.timeout.is_set or self.timeout.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.timeout.get_name_leafdata())
                        if (self.trap_strings.is_set or self.trap_strings.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.trap_strings.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "dll-capabilities" or name == "dll-name" or name == "is-mib-loaded" or name == "load-time" or name == "mib-config-filename" or name == "mib-name" or name == "timeout" or name == "trap-strings"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "dll-capabilities"):
                            self.dll_capabilities = value
                            self.dll_capabilities.value_namespace = name_space
                            self.dll_capabilities.value_namespace_prefix = name_space_prefix
                        if(value_path == "dll-name"):
                            self.dll_name = value
                            self.dll_name.value_namespace = name_space
                            self.dll_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-mib-loaded"):
                            self.is_mib_loaded = value
                            self.is_mib_loaded.value_namespace = name_space
                            self.is_mib_loaded.value_namespace_prefix = name_space_prefix
                        if(value_path == "load-time"):
                            self.load_time = value
                            self.load_time.value_namespace = name_space
                            self.load_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "mib-config-filename"):
                            self.mib_config_filename = value
                            self.mib_config_filename.value_namespace = name_space
                            self.mib_config_filename.value_namespace_prefix = name_space_prefix
                        if(value_path == "mib-name"):
                            self.mib_name = value
                            self.mib_name.value_namespace = name_space
                            self.mib_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "timeout"):
                            self.timeout = value
                            self.timeout.value_namespace = name_space
                            self.timeout.value_namespace_prefix = name_space_prefix
                        if(value_path == "trap-strings"):
                            self.trap_strings = value
                            self.trap_strings.value_namespace = name_space
                            self.trap_strings.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.name.is_set or
                        (self.mib_information is not None and self.mib_information.has_data()) or
                        (self.oids is not None and self.oids.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set or
                        (self.mib_information is not None and self.mib_information.has_operation()) or
                        (self.oids is not None and self.oids.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "mib" + "[name='" + self.name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/mibs/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "mib-information"):
                        if (self.mib_information is None):
                            self.mib_information = Snmp.Information.Mibs.Mib.MibInformation()
                            self.mib_information.parent = self
                            self._children_name_map["mib_information"] = "mib-information"
                        return self.mib_information

                    if (child_yang_name == "oids"):
                        if (self.oids is None):
                            self.oids = Snmp.Information.Mibs.Mib.Oids()
                            self.oids.parent = self
                            self._children_name_map["oids"] = "oids"
                        return self.oids

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "mib-information" or name == "oids" or name == "name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.mib:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.mib:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mibs" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "mib"):
                    for c in self.mib:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Snmp.Information.Mibs.Mib()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.mib.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mib"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class SerialNumbers(Entity):
            """
            SNMP statistics pdu 
            
            .. attribute:: serial_number
            
            	Serial number
            	**type**\: list of    :py:class:`SerialNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.SerialNumbers.SerialNumber>`
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                super(Snmp.Information.SerialNumbers, self).__init__()

                self.yang_name = "serial-numbers"
                self.yang_parent_name = "information"

                self.serial_number = YList(self)

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
                            super(Snmp.Information.SerialNumbers, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Snmp.Information.SerialNumbers, self).__setattr__(name, value)


            class SerialNumber(Entity):
                """
                Serial number
                
                .. attribute:: error_status
                
                	Is reques dropped due to error
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: input_q
                
                	Request inserted into input queue
                	**type**\:  str
                
                .. attribute:: nms
                
                	 NMS address Rx PDU
                	**type**\:  str
                
                .. attribute:: number
                
                	Serial number
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: output_q
                
                	De\-queue the request from the input queue
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pdu_type
                
                	 PDU type
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: pending_q
                
                	Enqueue the request into pending queue
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: port
                
                	Port
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: port_xr
                
                	NMS port number
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: req_id
                
                	Request ID
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: request_id
                
                	 SNMP request id per PDU
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: response_out
                
                	Response sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: serial_num
                
                	Serial number per PDU processing
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2016-06-01'

                def __init__(self):
                    super(Snmp.Information.SerialNumbers.SerialNumber, self).__init__()

                    self.yang_name = "serial-number"
                    self.yang_parent_name = "serial-numbers"

                    self.error_status = YLeaf(YType.uint16, "error-status")

                    self.input_q = YLeaf(YType.str, "input-q")

                    self.nms = YLeaf(YType.str, "nms")

                    self.number = YLeaf(YType.str, "number")

                    self.output_q = YLeaf(YType.uint32, "output-q")

                    self.pdu_type = YLeaf(YType.uint16, "pdu-type")

                    self.pending_q = YLeaf(YType.uint32, "pending-q")

                    self.port = YLeaf(YType.uint16, "port")

                    self.port_xr = YLeaf(YType.uint16, "port-xr")

                    self.req_id = YLeaf(YType.int32, "req-id")

                    self.request_id = YLeaf(YType.uint32, "request-id")

                    self.response_out = YLeaf(YType.uint32, "response-out")

                    self.serial_num = YLeaf(YType.uint32, "serial-num")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("error_status",
                                    "input_q",
                                    "nms",
                                    "number",
                                    "output_q",
                                    "pdu_type",
                                    "pending_q",
                                    "port",
                                    "port_xr",
                                    "req_id",
                                    "request_id",
                                    "response_out",
                                    "serial_num") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Snmp.Information.SerialNumbers.SerialNumber, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Snmp.Information.SerialNumbers.SerialNumber, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.error_status.is_set or
                        self.input_q.is_set or
                        self.nms.is_set or
                        self.number.is_set or
                        self.output_q.is_set or
                        self.pdu_type.is_set or
                        self.pending_q.is_set or
                        self.port.is_set or
                        self.port_xr.is_set or
                        self.req_id.is_set or
                        self.request_id.is_set or
                        self.response_out.is_set or
                        self.serial_num.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.error_status.yfilter != YFilter.not_set or
                        self.input_q.yfilter != YFilter.not_set or
                        self.nms.yfilter != YFilter.not_set or
                        self.number.yfilter != YFilter.not_set or
                        self.output_q.yfilter != YFilter.not_set or
                        self.pdu_type.yfilter != YFilter.not_set or
                        self.pending_q.yfilter != YFilter.not_set or
                        self.port.yfilter != YFilter.not_set or
                        self.port_xr.yfilter != YFilter.not_set or
                        self.req_id.yfilter != YFilter.not_set or
                        self.request_id.yfilter != YFilter.not_set or
                        self.response_out.yfilter != YFilter.not_set or
                        self.serial_num.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "serial-number" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/serial-numbers/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.error_status.is_set or self.error_status.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.error_status.get_name_leafdata())
                    if (self.input_q.is_set or self.input_q.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.input_q.get_name_leafdata())
                    if (self.nms.is_set or self.nms.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.nms.get_name_leafdata())
                    if (self.number.is_set or self.number.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.number.get_name_leafdata())
                    if (self.output_q.is_set or self.output_q.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.output_q.get_name_leafdata())
                    if (self.pdu_type.is_set or self.pdu_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.pdu_type.get_name_leafdata())
                    if (self.pending_q.is_set or self.pending_q.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.pending_q.get_name_leafdata())
                    if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.port.get_name_leafdata())
                    if (self.port_xr.is_set or self.port_xr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.port_xr.get_name_leafdata())
                    if (self.req_id.is_set or self.req_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.req_id.get_name_leafdata())
                    if (self.request_id.is_set or self.request_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.request_id.get_name_leafdata())
                    if (self.response_out.is_set or self.response_out.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.response_out.get_name_leafdata())
                    if (self.serial_num.is_set or self.serial_num.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.serial_num.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "error-status" or name == "input-q" or name == "nms" or name == "number" or name == "output-q" or name == "pdu-type" or name == "pending-q" or name == "port" or name == "port-xr" or name == "req-id" or name == "request-id" or name == "response-out" or name == "serial-num"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "error-status"):
                        self.error_status = value
                        self.error_status.value_namespace = name_space
                        self.error_status.value_namespace_prefix = name_space_prefix
                    if(value_path == "input-q"):
                        self.input_q = value
                        self.input_q.value_namespace = name_space
                        self.input_q.value_namespace_prefix = name_space_prefix
                    if(value_path == "nms"):
                        self.nms = value
                        self.nms.value_namespace = name_space
                        self.nms.value_namespace_prefix = name_space_prefix
                    if(value_path == "number"):
                        self.number = value
                        self.number.value_namespace = name_space
                        self.number.value_namespace_prefix = name_space_prefix
                    if(value_path == "output-q"):
                        self.output_q = value
                        self.output_q.value_namespace = name_space
                        self.output_q.value_namespace_prefix = name_space_prefix
                    if(value_path == "pdu-type"):
                        self.pdu_type = value
                        self.pdu_type.value_namespace = name_space
                        self.pdu_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "pending-q"):
                        self.pending_q = value
                        self.pending_q.value_namespace = name_space
                        self.pending_q.value_namespace_prefix = name_space_prefix
                    if(value_path == "port"):
                        self.port = value
                        self.port.value_namespace = name_space
                        self.port.value_namespace_prefix = name_space_prefix
                    if(value_path == "port-xr"):
                        self.port_xr = value
                        self.port_xr.value_namespace = name_space
                        self.port_xr.value_namespace_prefix = name_space_prefix
                    if(value_path == "req-id"):
                        self.req_id = value
                        self.req_id.value_namespace = name_space
                        self.req_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "request-id"):
                        self.request_id = value
                        self.request_id.value_namespace = name_space
                        self.request_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "response-out"):
                        self.response_out = value
                        self.response_out.value_namespace = name_space
                        self.response_out.value_namespace_prefix = name_space_prefix
                    if(value_path == "serial-num"):
                        self.serial_num = value
                        self.serial_num.value_namespace = name_space
                        self.serial_num.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.serial_number:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.serial_number:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "serial-numbers" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "serial-number"):
                    for c in self.serial_number:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Snmp.Information.SerialNumbers.SerialNumber()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.serial_number.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "serial-number"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class DropNmsAddresses(Entity):
            """
            NMS list for drop PDU
            
            .. attribute:: drop_nms_address
            
            	PDU drop info for NMS
            	**type**\: list of    :py:class:`DropNmsAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.DropNmsAddresses.DropNmsAddress>`
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                super(Snmp.Information.DropNmsAddresses, self).__init__()

                self.yang_name = "drop-nms-addresses"
                self.yang_parent_name = "information"

                self.drop_nms_address = YList(self)

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
                            super(Snmp.Information.DropNmsAddresses, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Snmp.Information.DropNmsAddresses, self).__setattr__(name, value)


            class DropNmsAddress(Entity):
                """
                PDU drop info for NMS
                
                .. attribute:: nms_addr  <key>
                
                	NMS address
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: aipc_count
                
                	drop count with AIPC Buffer Full
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: duplicate_count
                
                	Duplicate request drop count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: encode_count
                
                	Drop Count with Encode errors
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: incoming_q_count
                
                	Drop Count at Incoming Q
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: internal_count
                
                	 drop with Internal Errors
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: nms_address
                
                	NMS address of server
                	**type**\:  str
                
                .. attribute:: overload_count
                
                	Drop Count with overload notification
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: stack_count
                
                	Drop Count at snmp Stack
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: threshold_incoming_q_count
                
                	Drop Count at Incoming Q after threshold limit
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: timeout_count
                
                	Drop count with timeout
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2016-06-01'

                def __init__(self):
                    super(Snmp.Information.DropNmsAddresses.DropNmsAddress, self).__init__()

                    self.yang_name = "drop-nms-address"
                    self.yang_parent_name = "drop-nms-addresses"

                    self.nms_addr = YLeaf(YType.str, "nms-addr")

                    self.aipc_count = YLeaf(YType.uint32, "aipc-count")

                    self.duplicate_count = YLeaf(YType.uint32, "duplicate-count")

                    self.encode_count = YLeaf(YType.uint32, "encode-count")

                    self.incoming_q_count = YLeaf(YType.uint32, "incoming-q-count")

                    self.internal_count = YLeaf(YType.uint32, "internal-count")

                    self.nms_address = YLeaf(YType.str, "nms-address")

                    self.overload_count = YLeaf(YType.uint32, "overload-count")

                    self.stack_count = YLeaf(YType.uint32, "stack-count")

                    self.threshold_incoming_q_count = YLeaf(YType.uint32, "threshold-incoming-q-count")

                    self.timeout_count = YLeaf(YType.uint32, "timeout-count")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("nms_addr",
                                    "aipc_count",
                                    "duplicate_count",
                                    "encode_count",
                                    "incoming_q_count",
                                    "internal_count",
                                    "nms_address",
                                    "overload_count",
                                    "stack_count",
                                    "threshold_incoming_q_count",
                                    "timeout_count") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Snmp.Information.DropNmsAddresses.DropNmsAddress, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Snmp.Information.DropNmsAddresses.DropNmsAddress, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.nms_addr.is_set or
                        self.aipc_count.is_set or
                        self.duplicate_count.is_set or
                        self.encode_count.is_set or
                        self.incoming_q_count.is_set or
                        self.internal_count.is_set or
                        self.nms_address.is_set or
                        self.overload_count.is_set or
                        self.stack_count.is_set or
                        self.threshold_incoming_q_count.is_set or
                        self.timeout_count.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.nms_addr.yfilter != YFilter.not_set or
                        self.aipc_count.yfilter != YFilter.not_set or
                        self.duplicate_count.yfilter != YFilter.not_set or
                        self.encode_count.yfilter != YFilter.not_set or
                        self.incoming_q_count.yfilter != YFilter.not_set or
                        self.internal_count.yfilter != YFilter.not_set or
                        self.nms_address.yfilter != YFilter.not_set or
                        self.overload_count.yfilter != YFilter.not_set or
                        self.stack_count.yfilter != YFilter.not_set or
                        self.threshold_incoming_q_count.yfilter != YFilter.not_set or
                        self.timeout_count.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "drop-nms-address" + "[nms-addr='" + self.nms_addr.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/drop-nms-addresses/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.nms_addr.is_set or self.nms_addr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.nms_addr.get_name_leafdata())
                    if (self.aipc_count.is_set or self.aipc_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.aipc_count.get_name_leafdata())
                    if (self.duplicate_count.is_set or self.duplicate_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.duplicate_count.get_name_leafdata())
                    if (self.encode_count.is_set or self.encode_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.encode_count.get_name_leafdata())
                    if (self.incoming_q_count.is_set or self.incoming_q_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.incoming_q_count.get_name_leafdata())
                    if (self.internal_count.is_set or self.internal_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.internal_count.get_name_leafdata())
                    if (self.nms_address.is_set or self.nms_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.nms_address.get_name_leafdata())
                    if (self.overload_count.is_set or self.overload_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.overload_count.get_name_leafdata())
                    if (self.stack_count.is_set or self.stack_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.stack_count.get_name_leafdata())
                    if (self.threshold_incoming_q_count.is_set or self.threshold_incoming_q_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.threshold_incoming_q_count.get_name_leafdata())
                    if (self.timeout_count.is_set or self.timeout_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.timeout_count.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "nms-addr" or name == "aipc-count" or name == "duplicate-count" or name == "encode-count" or name == "incoming-q-count" or name == "internal-count" or name == "nms-address" or name == "overload-count" or name == "stack-count" or name == "threshold-incoming-q-count" or name == "timeout-count"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "nms-addr"):
                        self.nms_addr = value
                        self.nms_addr.value_namespace = name_space
                        self.nms_addr.value_namespace_prefix = name_space_prefix
                    if(value_path == "aipc-count"):
                        self.aipc_count = value
                        self.aipc_count.value_namespace = name_space
                        self.aipc_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "duplicate-count"):
                        self.duplicate_count = value
                        self.duplicate_count.value_namespace = name_space
                        self.duplicate_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "encode-count"):
                        self.encode_count = value
                        self.encode_count.value_namespace = name_space
                        self.encode_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "incoming-q-count"):
                        self.incoming_q_count = value
                        self.incoming_q_count.value_namespace = name_space
                        self.incoming_q_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "internal-count"):
                        self.internal_count = value
                        self.internal_count.value_namespace = name_space
                        self.internal_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "nms-address"):
                        self.nms_address = value
                        self.nms_address.value_namespace = name_space
                        self.nms_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "overload-count"):
                        self.overload_count = value
                        self.overload_count.value_namespace = name_space
                        self.overload_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "stack-count"):
                        self.stack_count = value
                        self.stack_count.value_namespace = name_space
                        self.stack_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "threshold-incoming-q-count"):
                        self.threshold_incoming_q_count = value
                        self.threshold_incoming_q_count.value_namespace = name_space
                        self.threshold_incoming_q_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "timeout-count"):
                        self.timeout_count = value
                        self.timeout_count.value_namespace = name_space
                        self.timeout_count.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.drop_nms_address:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.drop_nms_address:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "drop-nms-addresses" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "drop-nms-address"):
                    for c in self.drop_nms_address:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Snmp.Information.DropNmsAddresses.DropNmsAddress()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.drop_nms_address.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "drop-nms-address"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Views(Entity):
            """
            SNMP view information
            
            .. attribute:: view
            
            	SNMP target view name
            	**type**\: list of    :py:class:`View <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Views.View>`
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                super(Snmp.Information.Views, self).__init__()

                self.yang_name = "views"
                self.yang_parent_name = "information"

                self.view = YList(self)

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
                            super(Snmp.Information.Views, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Snmp.Information.Views, self).__setattr__(name, value)


            class View(Entity):
                """
                SNMP target view name
                
                .. attribute:: name  <key>
                
                	View name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: view_information
                
                	View name ,familytype, storagetype and status
                	**type**\: list of    :py:class:`ViewInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Views.View.ViewInformation>`
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2016-06-01'

                def __init__(self):
                    super(Snmp.Information.Views.View, self).__init__()

                    self.yang_name = "view"
                    self.yang_parent_name = "views"

                    self.name = YLeaf(YType.str, "name")

                    self.view_information = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Snmp.Information.Views.View, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Snmp.Information.Views.View, self).__setattr__(name, value)


                class ViewInformation(Entity):
                    """
                    View name ,familytype, storagetype and status
                    
                    .. attribute:: object_id  <key>
                    
                    	SNMP view OID
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: snmp_view_family_status
                    
                    	Status of this entry
                    	**type**\:  str
                    
                    .. attribute:: snmp_view_family_storage_type
                    
                    	Storage type
                    	**type**\:  str
                    
                    .. attribute:: snmp_view_family_type
                    
                    	Include or exclude
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'snmp-agent-oper'
                    _revision = '2016-06-01'

                    def __init__(self):
                        super(Snmp.Information.Views.View.ViewInformation, self).__init__()

                        self.yang_name = "view-information"
                        self.yang_parent_name = "view"

                        self.object_id = YLeaf(YType.str, "object-id")

                        self.snmp_view_family_status = YLeaf(YType.str, "snmp-view-family-status")

                        self.snmp_view_family_storage_type = YLeaf(YType.str, "snmp-view-family-storage-type")

                        self.snmp_view_family_type = YLeaf(YType.str, "snmp-view-family-type")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("object_id",
                                        "snmp_view_family_status",
                                        "snmp_view_family_storage_type",
                                        "snmp_view_family_type") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Snmp.Information.Views.View.ViewInformation, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Snmp.Information.Views.View.ViewInformation, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.object_id.is_set or
                            self.snmp_view_family_status.is_set or
                            self.snmp_view_family_storage_type.is_set or
                            self.snmp_view_family_type.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.object_id.yfilter != YFilter.not_set or
                            self.snmp_view_family_status.yfilter != YFilter.not_set or
                            self.snmp_view_family_storage_type.yfilter != YFilter.not_set or
                            self.snmp_view_family_type.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "view-information" + "[object-id='" + self.object_id.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.object_id.is_set or self.object_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.object_id.get_name_leafdata())
                        if (self.snmp_view_family_status.is_set or self.snmp_view_family_status.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.snmp_view_family_status.get_name_leafdata())
                        if (self.snmp_view_family_storage_type.is_set or self.snmp_view_family_storage_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.snmp_view_family_storage_type.get_name_leafdata())
                        if (self.snmp_view_family_type.is_set or self.snmp_view_family_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.snmp_view_family_type.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "object-id" or name == "snmp-view-family-status" or name == "snmp-view-family-storage-type" or name == "snmp-view-family-type"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "object-id"):
                            self.object_id = value
                            self.object_id.value_namespace = name_space
                            self.object_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "snmp-view-family-status"):
                            self.snmp_view_family_status = value
                            self.snmp_view_family_status.value_namespace = name_space
                            self.snmp_view_family_status.value_namespace_prefix = name_space_prefix
                        if(value_path == "snmp-view-family-storage-type"):
                            self.snmp_view_family_storage_type = value
                            self.snmp_view_family_storage_type.value_namespace = name_space
                            self.snmp_view_family_storage_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "snmp-view-family-type"):
                            self.snmp_view_family_type = value
                            self.snmp_view_family_type.value_namespace = name_space
                            self.snmp_view_family_type.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.view_information:
                        if (c.has_data()):
                            return True
                    return self.name.is_set

                def has_operation(self):
                    for c in self.view_information:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "view" + "[name='" + self.name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/views/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "view-information"):
                        for c in self.view_information:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Snmp.Information.Views.View.ViewInformation()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.view_information.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "view-information" or name == "name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.view:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.view:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "views" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "view"):
                    for c in self.view:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Snmp.Information.Views.View()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.view.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "view"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class SystemDescr(Entity):
            """
            System description
            
            .. attribute:: sys_descr
            
            	sysDescr  1.3.6.1.2.1.1.1
            	**type**\:  str
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                super(Snmp.Information.SystemDescr, self).__init__()

                self.yang_name = "system-descr"
                self.yang_parent_name = "information"

                self.sys_descr = YLeaf(YType.str, "sys-descr")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("sys_descr") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Snmp.Information.SystemDescr, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Snmp.Information.SystemDescr, self).__setattr__(name, value)

            def has_data(self):
                return self.sys_descr.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.sys_descr.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "system-descr" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.sys_descr.is_set or self.sys_descr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sys_descr.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "sys-descr"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "sys-descr"):
                    self.sys_descr = value
                    self.sys_descr.value_namespace = name_space
                    self.sys_descr.value_namespace_prefix = name_space_prefix


        class Tables(Entity):
            """
            List of table
            
            .. attribute:: groups
            
            	List of vacmAccessTable
            	**type**\:   :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Tables.Groups>`
            
            .. attribute:: user_engine_ids
            
            	List of User
            	**type**\:   :py:class:`UserEngineIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Tables.UserEngineIds>`
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                super(Snmp.Information.Tables, self).__init__()

                self.yang_name = "tables"
                self.yang_parent_name = "information"

                self.groups = Snmp.Information.Tables.Groups()
                self.groups.parent = self
                self._children_name_map["groups"] = "groups"
                self._children_yang_names.add("groups")

                self.user_engine_ids = Snmp.Information.Tables.UserEngineIds()
                self.user_engine_ids.parent = self
                self._children_name_map["user_engine_ids"] = "user-engine-ids"
                self._children_yang_names.add("user-engine-ids")


            class Groups(Entity):
                """
                List of vacmAccessTable
                
                .. attribute:: group
                
                	SNMP group name
                	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Tables.Groups.Group>`
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2016-06-01'

                def __init__(self):
                    super(Snmp.Information.Tables.Groups, self).__init__()

                    self.yang_name = "groups"
                    self.yang_parent_name = "tables"

                    self.group = YList(self)

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
                                super(Snmp.Information.Tables.Groups, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Snmp.Information.Tables.Groups, self).__setattr__(name, value)


                class Group(Entity):
                    """
                    SNMP group name
                    
                    .. attribute:: name  <key>
                    
                    	Group Name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: group_informations
                    
                    	Group Model
                    	**type**\:   :py:class:`GroupInformations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Tables.Groups.Group.GroupInformations>`
                    
                    

                    """

                    _prefix = 'snmp-agent-oper'
                    _revision = '2016-06-01'

                    def __init__(self):
                        super(Snmp.Information.Tables.Groups.Group, self).__init__()

                        self.yang_name = "group"
                        self.yang_parent_name = "groups"

                        self.name = YLeaf(YType.str, "name")

                        self.group_informations = Snmp.Information.Tables.Groups.Group.GroupInformations()
                        self.group_informations.parent = self
                        self._children_name_map["group_informations"] = "group-informations"
                        self._children_yang_names.add("group-informations")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Snmp.Information.Tables.Groups.Group, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Snmp.Information.Tables.Groups.Group, self).__setattr__(name, value)


                    class GroupInformations(Entity):
                        """
                        Group Model
                        
                        .. attribute:: group_information
                        
                        	Group name ,status  and information
                        	**type**\: list of    :py:class:`GroupInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Tables.Groups.Group.GroupInformations.GroupInformation>`
                        
                        

                        """

                        _prefix = 'snmp-agent-oper'
                        _revision = '2016-06-01'

                        def __init__(self):
                            super(Snmp.Information.Tables.Groups.Group.GroupInformations, self).__init__()

                            self.yang_name = "group-informations"
                            self.yang_parent_name = "group"

                            self.group_information = YList(self)

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
                                        super(Snmp.Information.Tables.Groups.Group.GroupInformations, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Snmp.Information.Tables.Groups.Group.GroupInformations, self).__setattr__(name, value)


                        class GroupInformation(Entity):
                            """
                            Group name ,status  and information
                            
                            .. attribute:: level
                            
                            	Level
                            	**type**\:  str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: modelnumber
                            
                            	Model number
                            	**type**\:  str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: vacm_access_notify_view_name
                            
                            	Notify view name
                            	**type**\:  str
                            
                            .. attribute:: vacm_access_read_view_name
                            
                            	Read view name
                            	**type**\:  str
                            
                            .. attribute:: vacm_access_status
                            
                            	Status of this view configuration
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: vacm_access_write_view_name
                            
                            	Write view name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'snmp-agent-oper'
                            _revision = '2016-06-01'

                            def __init__(self):
                                super(Snmp.Information.Tables.Groups.Group.GroupInformations.GroupInformation, self).__init__()

                                self.yang_name = "group-information"
                                self.yang_parent_name = "group-informations"

                                self.level = YLeaf(YType.str, "level")

                                self.modelnumber = YLeaf(YType.str, "modelnumber")

                                self.vacm_access_notify_view_name = YLeaf(YType.str, "vacm-access-notify-view-name")

                                self.vacm_access_read_view_name = YLeaf(YType.str, "vacm-access-read-view-name")

                                self.vacm_access_status = YLeaf(YType.uint32, "vacm-access-status")

                                self.vacm_access_write_view_name = YLeaf(YType.str, "vacm-access-write-view-name")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("level",
                                                "modelnumber",
                                                "vacm_access_notify_view_name",
                                                "vacm_access_read_view_name",
                                                "vacm_access_status",
                                                "vacm_access_write_view_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Snmp.Information.Tables.Groups.Group.GroupInformations.GroupInformation, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Snmp.Information.Tables.Groups.Group.GroupInformations.GroupInformation, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.level.is_set or
                                    self.modelnumber.is_set or
                                    self.vacm_access_notify_view_name.is_set or
                                    self.vacm_access_read_view_name.is_set or
                                    self.vacm_access_status.is_set or
                                    self.vacm_access_write_view_name.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.level.yfilter != YFilter.not_set or
                                    self.modelnumber.yfilter != YFilter.not_set or
                                    self.vacm_access_notify_view_name.yfilter != YFilter.not_set or
                                    self.vacm_access_read_view_name.yfilter != YFilter.not_set or
                                    self.vacm_access_status.yfilter != YFilter.not_set or
                                    self.vacm_access_write_view_name.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "group-information" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.level.is_set or self.level.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.level.get_name_leafdata())
                                if (self.modelnumber.is_set or self.modelnumber.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.modelnumber.get_name_leafdata())
                                if (self.vacm_access_notify_view_name.is_set or self.vacm_access_notify_view_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.vacm_access_notify_view_name.get_name_leafdata())
                                if (self.vacm_access_read_view_name.is_set or self.vacm_access_read_view_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.vacm_access_read_view_name.get_name_leafdata())
                                if (self.vacm_access_status.is_set or self.vacm_access_status.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.vacm_access_status.get_name_leafdata())
                                if (self.vacm_access_write_view_name.is_set or self.vacm_access_write_view_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.vacm_access_write_view_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "level" or name == "modelnumber" or name == "vacm-access-notify-view-name" or name == "vacm-access-read-view-name" or name == "vacm-access-status" or name == "vacm-access-write-view-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "level"):
                                    self.level = value
                                    self.level.value_namespace = name_space
                                    self.level.value_namespace_prefix = name_space_prefix
                                if(value_path == "modelnumber"):
                                    self.modelnumber = value
                                    self.modelnumber.value_namespace = name_space
                                    self.modelnumber.value_namespace_prefix = name_space_prefix
                                if(value_path == "vacm-access-notify-view-name"):
                                    self.vacm_access_notify_view_name = value
                                    self.vacm_access_notify_view_name.value_namespace = name_space
                                    self.vacm_access_notify_view_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "vacm-access-read-view-name"):
                                    self.vacm_access_read_view_name = value
                                    self.vacm_access_read_view_name.value_namespace = name_space
                                    self.vacm_access_read_view_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "vacm-access-status"):
                                    self.vacm_access_status = value
                                    self.vacm_access_status.value_namespace = name_space
                                    self.vacm_access_status.value_namespace_prefix = name_space_prefix
                                if(value_path == "vacm-access-write-view-name"):
                                    self.vacm_access_write_view_name = value
                                    self.vacm_access_write_view_name.value_namespace = name_space
                                    self.vacm_access_write_view_name.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.group_information:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.group_information:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "group-informations" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "group-information"):
                                for c in self.group_information:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Snmp.Information.Tables.Groups.Group.GroupInformations.GroupInformation()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.group_information.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "group-information"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.name.is_set or
                            (self.group_informations is not None and self.group_informations.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set or
                            (self.group_informations is not None and self.group_informations.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "group" + "[name='" + self.name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/tables/groups/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "group-informations"):
                            if (self.group_informations is None):
                                self.group_informations = Snmp.Information.Tables.Groups.Group.GroupInformations()
                                self.group_informations.parent = self
                                self._children_name_map["group_informations"] = "group-informations"
                            return self.group_informations

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "group-informations" or name == "name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.group:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.group:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "groups" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/tables/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "group"):
                        for c in self.group:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Snmp.Information.Tables.Groups.Group()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.group.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "group"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class UserEngineIds(Entity):
                """
                List of User
                
                .. attribute:: user_engine_id
                
                	SNMP engineId
                	**type**\: list of    :py:class:`UserEngineId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Tables.UserEngineIds.UserEngineId>`
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2016-06-01'

                def __init__(self):
                    super(Snmp.Information.Tables.UserEngineIds, self).__init__()

                    self.yang_name = "user-engine-ids"
                    self.yang_parent_name = "tables"

                    self.user_engine_id = YList(self)

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
                                super(Snmp.Information.Tables.UserEngineIds, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Snmp.Information.Tables.UserEngineIds, self).__setattr__(name, value)


                class UserEngineId(Entity):
                    """
                    SNMP engineId
                    
                    .. attribute:: engine_id  <key>
                    
                    	SNMP Engine ID
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: user_name
                    
                    	User name ,storage type ,status 
                    	**type**\: list of    :py:class:`UserName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Tables.UserEngineIds.UserEngineId.UserName>`
                    
                    

                    """

                    _prefix = 'snmp-agent-oper'
                    _revision = '2016-06-01'

                    def __init__(self):
                        super(Snmp.Information.Tables.UserEngineIds.UserEngineId, self).__init__()

                        self.yang_name = "user-engine-id"
                        self.yang_parent_name = "user-engine-ids"

                        self.engine_id = YLeaf(YType.str, "engine-id")

                        self.user_name = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("engine_id") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Snmp.Information.Tables.UserEngineIds.UserEngineId, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Snmp.Information.Tables.UserEngineIds.UserEngineId, self).__setattr__(name, value)


                    class UserName(Entity):
                        """
                        User name ,storage type ,status 
                        
                        .. attribute:: user_name  <key>
                        
                        	User name
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: usm_user_status
                        
                        	Status of this user
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: usm_user_storage_type
                        
                        	Storage type
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'snmp-agent-oper'
                        _revision = '2016-06-01'

                        def __init__(self):
                            super(Snmp.Information.Tables.UserEngineIds.UserEngineId.UserName, self).__init__()

                            self.yang_name = "user-name"
                            self.yang_parent_name = "user-engine-id"

                            self.user_name = YLeaf(YType.str, "user-name")

                            self.usm_user_status = YLeaf(YType.uint32, "usm-user-status")

                            self.usm_user_storage_type = YLeaf(YType.uint32, "usm-user-storage-type")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("user_name",
                                            "usm_user_status",
                                            "usm_user_storage_type") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Snmp.Information.Tables.UserEngineIds.UserEngineId.UserName, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Snmp.Information.Tables.UserEngineIds.UserEngineId.UserName, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.user_name.is_set or
                                self.usm_user_status.is_set or
                                self.usm_user_storage_type.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.user_name.yfilter != YFilter.not_set or
                                self.usm_user_status.yfilter != YFilter.not_set or
                                self.usm_user_storage_type.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "user-name" + "[user-name='" + self.user_name.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.user_name.is_set or self.user_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.user_name.get_name_leafdata())
                            if (self.usm_user_status.is_set or self.usm_user_status.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.usm_user_status.get_name_leafdata())
                            if (self.usm_user_storage_type.is_set or self.usm_user_storage_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.usm_user_storage_type.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "user-name" or name == "usm-user-status" or name == "usm-user-storage-type"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "user-name"):
                                self.user_name = value
                                self.user_name.value_namespace = name_space
                                self.user_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "usm-user-status"):
                                self.usm_user_status = value
                                self.usm_user_status.value_namespace = name_space
                                self.usm_user_status.value_namespace_prefix = name_space_prefix
                            if(value_path == "usm-user-storage-type"):
                                self.usm_user_storage_type = value
                                self.usm_user_storage_type.value_namespace = name_space
                                self.usm_user_storage_type.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.user_name:
                            if (c.has_data()):
                                return True
                        return self.engine_id.is_set

                    def has_operation(self):
                        for c in self.user_name:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.engine_id.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "user-engine-id" + "[engine-id='" + self.engine_id.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/tables/user-engine-ids/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.engine_id.is_set or self.engine_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.engine_id.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "user-name"):
                            for c in self.user_name:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Snmp.Information.Tables.UserEngineIds.UserEngineId.UserName()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.user_name.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "user-name" or name == "engine-id"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "engine-id"):
                            self.engine_id = value
                            self.engine_id.value_namespace = name_space
                            self.engine_id.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.user_engine_id:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.user_engine_id:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "user-engine-ids" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/tables/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "user-engine-id"):
                        for c in self.user_engine_id:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Snmp.Information.Tables.UserEngineIds.UserEngineId()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.user_engine_id.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "user-engine-id"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    (self.groups is not None and self.groups.has_data()) or
                    (self.user_engine_ids is not None and self.user_engine_ids.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.groups is not None and self.groups.has_operation()) or
                    (self.user_engine_ids is not None and self.user_engine_ids.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "tables" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "groups"):
                    if (self.groups is None):
                        self.groups = Snmp.Information.Tables.Groups()
                        self.groups.parent = self
                        self._children_name_map["groups"] = "groups"
                    return self.groups

                if (child_yang_name == "user-engine-ids"):
                    if (self.user_engine_ids is None):
                        self.user_engine_ids = Snmp.Information.Tables.UserEngineIds()
                        self.user_engine_ids.parent = self
                        self._children_name_map["user_engine_ids"] = "user-engine-ids"
                    return self.user_engine_ids

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "groups" or name == "user-engine-ids"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class SystemOid(Entity):
            """
            System object ID
            
            .. attribute:: sys_obj_id
            
            	sysObjID  1.3.6.1.2.1.1.2
            	**type**\:  str
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                super(Snmp.Information.SystemOid, self).__init__()

                self.yang_name = "system-oid"
                self.yang_parent_name = "information"

                self.sys_obj_id = YLeaf(YType.str, "sys-obj-id")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("sys_obj_id") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Snmp.Information.SystemOid, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Snmp.Information.SystemOid, self).__setattr__(name, value)

            def has_data(self):
                return self.sys_obj_id.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.sys_obj_id.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "system-oid" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.sys_obj_id.is_set or self.sys_obj_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sys_obj_id.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "sys-obj-id"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "sys-obj-id"):
                    self.sys_obj_id = value
                    self.sys_obj_id.value_namespace = name_space
                    self.sys_obj_id.value_namespace_prefix = name_space_prefix


        class TrapQueue(Entity):
            """
            SNMP trap queue statistics
            
            .. attribute:: trap_avg
            
            	trap avg
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: trap_max
            
            	trap max
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: trap_min
            
            	trap min
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: trap_q
            
            	trapQ
            	**type**\:  str
            
            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                super(Snmp.Information.TrapQueue, self).__init__()

                self.yang_name = "trap-queue"
                self.yang_parent_name = "information"

                self.trap_avg = YLeaf(YType.uint32, "trap-avg")

                self.trap_max = YLeaf(YType.uint32, "trap-max")

                self.trap_min = YLeaf(YType.uint32, "trap-min")

                self.trap_q = YLeaf(YType.str, "trap-q")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("trap_avg",
                                "trap_max",
                                "trap_min",
                                "trap_q") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Snmp.Information.TrapQueue, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Snmp.Information.TrapQueue, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.trap_avg.is_set or
                    self.trap_max.is_set or
                    self.trap_min.is_set or
                    self.trap_q.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.trap_avg.yfilter != YFilter.not_set or
                    self.trap_max.yfilter != YFilter.not_set or
                    self.trap_min.yfilter != YFilter.not_set or
                    self.trap_q.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "trap-queue" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/information/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.trap_avg.is_set or self.trap_avg.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.trap_avg.get_name_leafdata())
                if (self.trap_max.is_set or self.trap_max.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.trap_max.get_name_leafdata())
                if (self.trap_min.is_set or self.trap_min.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.trap_min.get_name_leafdata())
                if (self.trap_q.is_set or self.trap_q.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.trap_q.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "trap-avg" or name == "trap-max" or name == "trap-min" or name == "trap-q"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "trap-avg"):
                    self.trap_avg = value
                    self.trap_avg.value_namespace = name_space
                    self.trap_avg.value_namespace_prefix = name_space_prefix
                if(value_path == "trap-max"):
                    self.trap_max = value
                    self.trap_max.value_namespace = name_space
                    self.trap_max.value_namespace_prefix = name_space_prefix
                if(value_path == "trap-min"):
                    self.trap_min = value
                    self.trap_min.value_namespace = name_space
                    self.trap_min.value_namespace_prefix = name_space_prefix
                if(value_path == "trap-q"):
                    self.trap_q = value
                    self.trap_q.value_namespace = name_space
                    self.trap_q.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                (self.bulk_stats_transfers is not None and self.bulk_stats_transfers.has_data()) or
                (self.context_mapping is not None and self.context_mapping.has_data()) or
                (self.drop_nms_addresses is not None and self.drop_nms_addresses.has_data()) or
                (self.duplicate_drop is not None and self.duplicate_drop.has_data()) or
                (self.engine_id is not None and self.engine_id.has_data()) or
                (self.hosts is not None and self.hosts.has_data()) or
                (self.incoming_queue is not None and self.incoming_queue.has_data()) or
                (self.infom_details is not None and self.infom_details.has_data()) or
                (self.mibs is not None and self.mibs.has_data()) or
                (self.nm_spackets is not None and self.nm_spackets.has_data()) or
                (self.nms_addresses is not None and self.nms_addresses.has_data()) or
                (self.poll_oids is not None and self.poll_oids.has_data()) or
                (self.request_type_detail is not None and self.request_type_detail.has_data()) or
                (self.rx_queue is not None and self.rx_queue.has_data()) or
                (self.serial_numbers is not None and self.serial_numbers.has_data()) or
                (self.statistics is not None and self.statistics.has_data()) or
                (self.system_descr is not None and self.system_descr.has_data()) or
                (self.system_name is not None and self.system_name.has_data()) or
                (self.system_oid is not None and self.system_oid.has_data()) or
                (self.system_up_time is not None and self.system_up_time.has_data()) or
                (self.tables is not None and self.tables.has_data()) or
                (self.trap_infos is not None and self.trap_infos.has_data()) or
                (self.trap_oids is not None and self.trap_oids.has_data()) or
                (self.trap_queue is not None and self.trap_queue.has_data()) or
                (self.views is not None and self.views.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.bulk_stats_transfers is not None and self.bulk_stats_transfers.has_operation()) or
                (self.context_mapping is not None and self.context_mapping.has_operation()) or
                (self.drop_nms_addresses is not None and self.drop_nms_addresses.has_operation()) or
                (self.duplicate_drop is not None and self.duplicate_drop.has_operation()) or
                (self.engine_id is not None and self.engine_id.has_operation()) or
                (self.hosts is not None and self.hosts.has_operation()) or
                (self.incoming_queue is not None and self.incoming_queue.has_operation()) or
                (self.infom_details is not None and self.infom_details.has_operation()) or
                (self.mibs is not None and self.mibs.has_operation()) or
                (self.nm_spackets is not None and self.nm_spackets.has_operation()) or
                (self.nms_addresses is not None and self.nms_addresses.has_operation()) or
                (self.poll_oids is not None and self.poll_oids.has_operation()) or
                (self.request_type_detail is not None and self.request_type_detail.has_operation()) or
                (self.rx_queue is not None and self.rx_queue.has_operation()) or
                (self.serial_numbers is not None and self.serial_numbers.has_operation()) or
                (self.statistics is not None and self.statistics.has_operation()) or
                (self.system_descr is not None and self.system_descr.has_operation()) or
                (self.system_name is not None and self.system_name.has_operation()) or
                (self.system_oid is not None and self.system_oid.has_operation()) or
                (self.system_up_time is not None and self.system_up_time.has_operation()) or
                (self.tables is not None and self.tables.has_operation()) or
                (self.trap_infos is not None and self.trap_infos.has_operation()) or
                (self.trap_oids is not None and self.trap_oids.has_operation()) or
                (self.trap_queue is not None and self.trap_queue.has_operation()) or
                (self.views is not None and self.views.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "information" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "bulk-stats-transfers"):
                if (self.bulk_stats_transfers is None):
                    self.bulk_stats_transfers = Snmp.Information.BulkStatsTransfers()
                    self.bulk_stats_transfers.parent = self
                    self._children_name_map["bulk_stats_transfers"] = "bulk-stats-transfers"
                return self.bulk_stats_transfers

            if (child_yang_name == "context-mapping"):
                if (self.context_mapping is None):
                    self.context_mapping = Snmp.Information.ContextMapping()
                    self.context_mapping.parent = self
                    self._children_name_map["context_mapping"] = "context-mapping"
                return self.context_mapping

            if (child_yang_name == "drop-nms-addresses"):
                if (self.drop_nms_addresses is None):
                    self.drop_nms_addresses = Snmp.Information.DropNmsAddresses()
                    self.drop_nms_addresses.parent = self
                    self._children_name_map["drop_nms_addresses"] = "drop-nms-addresses"
                return self.drop_nms_addresses

            if (child_yang_name == "duplicate-drop"):
                if (self.duplicate_drop is None):
                    self.duplicate_drop = Snmp.Information.DuplicateDrop()
                    self.duplicate_drop.parent = self
                    self._children_name_map["duplicate_drop"] = "duplicate-drop"
                return self.duplicate_drop

            if (child_yang_name == "engine-id"):
                if (self.engine_id is None):
                    self.engine_id = Snmp.Information.EngineId()
                    self.engine_id.parent = self
                    self._children_name_map["engine_id"] = "engine-id"
                return self.engine_id

            if (child_yang_name == "hosts"):
                if (self.hosts is None):
                    self.hosts = Snmp.Information.Hosts()
                    self.hosts.parent = self
                    self._children_name_map["hosts"] = "hosts"
                return self.hosts

            if (child_yang_name == "incoming-queue"):
                if (self.incoming_queue is None):
                    self.incoming_queue = Snmp.Information.IncomingQueue()
                    self.incoming_queue.parent = self
                    self._children_name_map["incoming_queue"] = "incoming-queue"
                return self.incoming_queue

            if (child_yang_name == "infom-details"):
                if (self.infom_details is None):
                    self.infom_details = Snmp.Information.InfomDetails()
                    self.infom_details.parent = self
                    self._children_name_map["infom_details"] = "infom-details"
                return self.infom_details

            if (child_yang_name == "mibs"):
                if (self.mibs is None):
                    self.mibs = Snmp.Information.Mibs()
                    self.mibs.parent = self
                    self._children_name_map["mibs"] = "mibs"
                return self.mibs

            if (child_yang_name == "nm-spackets"):
                if (self.nm_spackets is None):
                    self.nm_spackets = Snmp.Information.NmSpackets()
                    self.nm_spackets.parent = self
                    self._children_name_map["nm_spackets"] = "nm-spackets"
                return self.nm_spackets

            if (child_yang_name == "nms-addresses"):
                if (self.nms_addresses is None):
                    self.nms_addresses = Snmp.Information.NmsAddresses()
                    self.nms_addresses.parent = self
                    self._children_name_map["nms_addresses"] = "nms-addresses"
                return self.nms_addresses

            if (child_yang_name == "poll-oids"):
                if (self.poll_oids is None):
                    self.poll_oids = Snmp.Information.PollOids()
                    self.poll_oids.parent = self
                    self._children_name_map["poll_oids"] = "poll-oids"
                return self.poll_oids

            if (child_yang_name == "request-type-detail"):
                if (self.request_type_detail is None):
                    self.request_type_detail = Snmp.Information.RequestTypeDetail()
                    self.request_type_detail.parent = self
                    self._children_name_map["request_type_detail"] = "request-type-detail"
                return self.request_type_detail

            if (child_yang_name == "rx-queue"):
                if (self.rx_queue is None):
                    self.rx_queue = Snmp.Information.RxQueue()
                    self.rx_queue.parent = self
                    self._children_name_map["rx_queue"] = "rx-queue"
                return self.rx_queue

            if (child_yang_name == "serial-numbers"):
                if (self.serial_numbers is None):
                    self.serial_numbers = Snmp.Information.SerialNumbers()
                    self.serial_numbers.parent = self
                    self._children_name_map["serial_numbers"] = "serial-numbers"
                return self.serial_numbers

            if (child_yang_name == "statistics"):
                if (self.statistics is None):
                    self.statistics = Snmp.Information.Statistics()
                    self.statistics.parent = self
                    self._children_name_map["statistics"] = "statistics"
                return self.statistics

            if (child_yang_name == "system-descr"):
                if (self.system_descr is None):
                    self.system_descr = Snmp.Information.SystemDescr()
                    self.system_descr.parent = self
                    self._children_name_map["system_descr"] = "system-descr"
                return self.system_descr

            if (child_yang_name == "system-name"):
                if (self.system_name is None):
                    self.system_name = Snmp.Information.SystemName()
                    self.system_name.parent = self
                    self._children_name_map["system_name"] = "system-name"
                return self.system_name

            if (child_yang_name == "system-oid"):
                if (self.system_oid is None):
                    self.system_oid = Snmp.Information.SystemOid()
                    self.system_oid.parent = self
                    self._children_name_map["system_oid"] = "system-oid"
                return self.system_oid

            if (child_yang_name == "system-up-time"):
                if (self.system_up_time is None):
                    self.system_up_time = Snmp.Information.SystemUpTime()
                    self.system_up_time.parent = self
                    self._children_name_map["system_up_time"] = "system-up-time"
                return self.system_up_time

            if (child_yang_name == "tables"):
                if (self.tables is None):
                    self.tables = Snmp.Information.Tables()
                    self.tables.parent = self
                    self._children_name_map["tables"] = "tables"
                return self.tables

            if (child_yang_name == "trap-infos"):
                if (self.trap_infos is None):
                    self.trap_infos = Snmp.Information.TrapInfos()
                    self.trap_infos.parent = self
                    self._children_name_map["trap_infos"] = "trap-infos"
                return self.trap_infos

            if (child_yang_name == "trap-oids"):
                if (self.trap_oids is None):
                    self.trap_oids = Snmp.Information.TrapOids()
                    self.trap_oids.parent = self
                    self._children_name_map["trap_oids"] = "trap-oids"
                return self.trap_oids

            if (child_yang_name == "trap-queue"):
                if (self.trap_queue is None):
                    self.trap_queue = Snmp.Information.TrapQueue()
                    self.trap_queue.parent = self
                    self._children_name_map["trap_queue"] = "trap-queue"
                return self.trap_queue

            if (child_yang_name == "views"):
                if (self.views is None):
                    self.views = Snmp.Information.Views()
                    self.views.parent = self
                    self._children_name_map["views"] = "views"
                return self.views

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "bulk-stats-transfers" or name == "context-mapping" or name == "drop-nms-addresses" or name == "duplicate-drop" or name == "engine-id" or name == "hosts" or name == "incoming-queue" or name == "infom-details" or name == "mibs" or name == "nm-spackets" or name == "nms-addresses" or name == "poll-oids" or name == "request-type-detail" or name == "rx-queue" or name == "serial-numbers" or name == "statistics" or name == "system-descr" or name == "system-name" or name == "system-oid" or name == "system-up-time" or name == "tables" or name == "trap-infos" or name == "trap-oids" or name == "trap-queue" or name == "views"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Interfaces(Entity):
        """
        List of interfaces
        
        .. attribute:: interface
        
        	Interface Name
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Interfaces.Interface>`
        
        

        """

        _prefix = 'snmp-agent-oper'
        _revision = '2016-06-01'

        def __init__(self):
            super(Snmp.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "snmp"

            self.interface = YList(self)

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
                        super(Snmp.Interfaces, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Snmp.Interfaces, self).__setattr__(name, value)


        class Interface(Entity):
            """
            Interface Name
            
            .. attribute:: name  <key>
            
            	Interface Name
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: interface_index
            
            	Interface Index as used by MIB tables
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**mandatory**\: True
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                super(Snmp.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"

                self.name = YLeaf(YType.str, "name")

                self.interface_index = YLeaf(YType.int32, "interface-index")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("name",
                                "interface_index") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Snmp.Interfaces.Interface, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Snmp.Interfaces.Interface, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.name.is_set or
                    self.interface_index.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    self.interface_index.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "interface" + "[name='" + self.name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/interfaces/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())
                if (self.interface_index.is_set or self.interface_index.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface_index.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "name" or name == "interface-index"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix
                if(value_path == "interface-index"):
                    self.interface_index = value
                    self.interface_index.value_namespace = name_space
                    self.interface_index.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.interface:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.interface:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "interfaces" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "interface"):
                for c in self.interface:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Snmp.Interfaces.Interface()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.interface.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "interface"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Correlator(Entity):
        """
        Trap Correlator operational data
        
        .. attribute:: buffer_status
        
        	Describes buffer utilization and parameters configured
        	**type**\:   :py:class:`BufferStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Correlator.BufferStatus>`
        
        .. attribute:: rule_details
        
        	Table that contains the database of correlation rule details
        	**type**\:   :py:class:`RuleDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Correlator.RuleDetails>`
        
        .. attribute:: rule_set_details
        
        	Table that contains the ruleset detail info
        	**type**\:   :py:class:`RuleSetDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Correlator.RuleSetDetails>`
        
        .. attribute:: traps
        
        	Correlated traps Table
        	**type**\:   :py:class:`Traps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Correlator.Traps>`
        
        

        """

        _prefix = 'snmp-agent-oper'
        _revision = '2016-06-01'

        def __init__(self):
            super(Snmp.Correlator, self).__init__()

            self.yang_name = "correlator"
            self.yang_parent_name = "snmp"

            self.buffer_status = Snmp.Correlator.BufferStatus()
            self.buffer_status.parent = self
            self._children_name_map["buffer_status"] = "buffer-status"
            self._children_yang_names.add("buffer-status")

            self.rule_details = Snmp.Correlator.RuleDetails()
            self.rule_details.parent = self
            self._children_name_map["rule_details"] = "rule-details"
            self._children_yang_names.add("rule-details")

            self.rule_set_details = Snmp.Correlator.RuleSetDetails()
            self.rule_set_details.parent = self
            self._children_name_map["rule_set_details"] = "rule-set-details"
            self._children_yang_names.add("rule-set-details")

            self.traps = Snmp.Correlator.Traps()
            self.traps.parent = self
            self._children_name_map["traps"] = "traps"
            self._children_yang_names.add("traps")


        class RuleDetails(Entity):
            """
            Table that contains the database of correlation
            rule details
            
            .. attribute:: rule_detail
            
            	Details of one of the correlation rules
            	**type**\: list of    :py:class:`RuleDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Correlator.RuleDetails.RuleDetail>`
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                super(Snmp.Correlator.RuleDetails, self).__init__()

                self.yang_name = "rule-details"
                self.yang_parent_name = "correlator"

                self.rule_detail = YList(self)

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
                            super(Snmp.Correlator.RuleDetails, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Snmp.Correlator.RuleDetails, self).__setattr__(name, value)


            class RuleDetail(Entity):
                """
                Details of one of the correlation rules
                
                .. attribute:: rule_name  <key>
                
                	Correlation Rule Name
                	**type**\:  str
                
                	**length:** 1..32
                
                .. attribute:: apply_host
                
                	Hosts (IP/port) to which the rule is applied
                	**type**\: list of    :py:class:`ApplyHost <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Correlator.RuleDetails.RuleDetail.ApplyHost>`
                
                .. attribute:: non_rootcaus
                
                	OIDs/VarBinds defining the nonrootcause match conditions
                	**type**\: list of    :py:class:`NonRootcaus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Correlator.RuleDetails.RuleDetail.NonRootcaus>`
                
                .. attribute:: root_cause
                
                	OID/VarBinds defining the rootcause match conditions
                	**type**\:   :py:class:`RootCause <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Correlator.RuleDetails.RuleDetail.RootCause>`
                
                .. attribute:: rule_summary
                
                	Rule summary, name, etc
                	**type**\:   :py:class:`RuleSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Correlator.RuleDetails.RuleDetail.RuleSummary>`
                
                .. attribute:: timeout
                
                	Time window (in ms) for which root/all messages are kept in correlater before sending them to hosts
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2016-06-01'

                def __init__(self):
                    super(Snmp.Correlator.RuleDetails.RuleDetail, self).__init__()

                    self.yang_name = "rule-detail"
                    self.yang_parent_name = "rule-details"

                    self.rule_name = YLeaf(YType.str, "rule-name")

                    self.timeout = YLeaf(YType.uint32, "timeout")

                    self.root_cause = Snmp.Correlator.RuleDetails.RuleDetail.RootCause()
                    self.root_cause.parent = self
                    self._children_name_map["root_cause"] = "root-cause"
                    self._children_yang_names.add("root-cause")

                    self.rule_summary = Snmp.Correlator.RuleDetails.RuleDetail.RuleSummary()
                    self.rule_summary.parent = self
                    self._children_name_map["rule_summary"] = "rule-summary"
                    self._children_yang_names.add("rule-summary")

                    self.apply_host = YList(self)
                    self.non_rootcaus = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("rule_name",
                                    "timeout") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Snmp.Correlator.RuleDetails.RuleDetail, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Snmp.Correlator.RuleDetails.RuleDetail, self).__setattr__(name, value)


                class RuleSummary(Entity):
                    """
                    Rule summary, name, etc
                    
                    .. attribute:: buffered_traps_count
                    
                    	Number of buffered traps correlated to this rule
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rule_name
                    
                    	Correlation Rule Name
                    	**type**\:  str
                    
                    .. attribute:: rule_state
                    
                    	Applied state of the rule It could be not applied, applied or applied to all
                    	**type**\:   :py:class:`SnmpCorrRuleState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.SnmpCorrRuleState>`
                    
                    

                    """

                    _prefix = 'snmp-agent-oper'
                    _revision = '2016-06-01'

                    def __init__(self):
                        super(Snmp.Correlator.RuleDetails.RuleDetail.RuleSummary, self).__init__()

                        self.yang_name = "rule-summary"
                        self.yang_parent_name = "rule-detail"

                        self.buffered_traps_count = YLeaf(YType.uint32, "buffered-traps-count")

                        self.rule_name = YLeaf(YType.str, "rule-name")

                        self.rule_state = YLeaf(YType.enumeration, "rule-state")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("buffered_traps_count",
                                        "rule_name",
                                        "rule_state") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Snmp.Correlator.RuleDetails.RuleDetail.RuleSummary, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Snmp.Correlator.RuleDetails.RuleDetail.RuleSummary, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.buffered_traps_count.is_set or
                            self.rule_name.is_set or
                            self.rule_state.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.buffered_traps_count.yfilter != YFilter.not_set or
                            self.rule_name.yfilter != YFilter.not_set or
                            self.rule_state.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "rule-summary" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.buffered_traps_count.is_set or self.buffered_traps_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.buffered_traps_count.get_name_leafdata())
                        if (self.rule_name.is_set or self.rule_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rule_name.get_name_leafdata())
                        if (self.rule_state.is_set or self.rule_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rule_state.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "buffered-traps-count" or name == "rule-name" or name == "rule-state"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "buffered-traps-count"):
                            self.buffered_traps_count = value
                            self.buffered_traps_count.value_namespace = name_space
                            self.buffered_traps_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "rule-name"):
                            self.rule_name = value
                            self.rule_name.value_namespace = name_space
                            self.rule_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "rule-state"):
                            self.rule_state = value
                            self.rule_state.value_namespace = name_space
                            self.rule_state.value_namespace_prefix = name_space_prefix


                class RootCause(Entity):
                    """
                    OID/VarBinds defining the rootcause match
                    conditions.
                    
                    .. attribute:: oid
                    
                    	OID of the trap
                    	**type**\:  str
                    
                    .. attribute:: var_bind
                    
                    	VarBinds of the trap
                    	**type**\: list of    :py:class:`VarBind <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Correlator.RuleDetails.RuleDetail.RootCause.VarBind>`
                    
                    

                    """

                    _prefix = 'snmp-agent-oper'
                    _revision = '2016-06-01'

                    def __init__(self):
                        super(Snmp.Correlator.RuleDetails.RuleDetail.RootCause, self).__init__()

                        self.yang_name = "root-cause"
                        self.yang_parent_name = "rule-detail"

                        self.oid = YLeaf(YType.str, "oid")

                        self.var_bind = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("oid") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Snmp.Correlator.RuleDetails.RuleDetail.RootCause, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Snmp.Correlator.RuleDetails.RuleDetail.RootCause, self).__setattr__(name, value)


                    class VarBind(Entity):
                        """
                        VarBinds of the trap
                        
                        .. attribute:: match_type
                        
                        	Varbind match type
                        	**type**\:   :py:class:`SnmpCorrVbindMatch <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.SnmpCorrVbindMatch>`
                        
                        .. attribute:: oid
                        
                        	OID of the varbind
                        	**type**\:  str
                        
                        .. attribute:: reg_exp
                        
                        	Regular expression to match
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'snmp-agent-oper'
                        _revision = '2016-06-01'

                        def __init__(self):
                            super(Snmp.Correlator.RuleDetails.RuleDetail.RootCause.VarBind, self).__init__()

                            self.yang_name = "var-bind"
                            self.yang_parent_name = "root-cause"

                            self.match_type = YLeaf(YType.enumeration, "match-type")

                            self.oid = YLeaf(YType.str, "oid")

                            self.reg_exp = YLeaf(YType.str, "reg-exp")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("match_type",
                                            "oid",
                                            "reg_exp") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Snmp.Correlator.RuleDetails.RuleDetail.RootCause.VarBind, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Snmp.Correlator.RuleDetails.RuleDetail.RootCause.VarBind, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.match_type.is_set or
                                self.oid.is_set or
                                self.reg_exp.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.match_type.yfilter != YFilter.not_set or
                                self.oid.yfilter != YFilter.not_set or
                                self.reg_exp.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "var-bind" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.match_type.is_set or self.match_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.match_type.get_name_leafdata())
                            if (self.oid.is_set or self.oid.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.oid.get_name_leafdata())
                            if (self.reg_exp.is_set or self.reg_exp.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.reg_exp.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "match-type" or name == "oid" or name == "reg-exp"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "match-type"):
                                self.match_type = value
                                self.match_type.value_namespace = name_space
                                self.match_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "oid"):
                                self.oid = value
                                self.oid.value_namespace = name_space
                                self.oid.value_namespace_prefix = name_space_prefix
                            if(value_path == "reg-exp"):
                                self.reg_exp = value
                                self.reg_exp.value_namespace = name_space
                                self.reg_exp.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.var_bind:
                            if (c.has_data()):
                                return True
                        return self.oid.is_set

                    def has_operation(self):
                        for c in self.var_bind:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.oid.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "root-cause" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.oid.is_set or self.oid.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.oid.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "var-bind"):
                            for c in self.var_bind:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Snmp.Correlator.RuleDetails.RuleDetail.RootCause.VarBind()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.var_bind.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "var-bind" or name == "oid"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "oid"):
                            self.oid = value
                            self.oid.value_namespace = name_space
                            self.oid.value_namespace_prefix = name_space_prefix


                class NonRootcaus(Entity):
                    """
                    OIDs/VarBinds defining the nonrootcause match
                    conditions.
                    
                    .. attribute:: oid
                    
                    	OID of the trap
                    	**type**\:  str
                    
                    .. attribute:: var_bind
                    
                    	VarBinds of the trap
                    	**type**\: list of    :py:class:`VarBind <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Correlator.RuleDetails.RuleDetail.NonRootcaus.VarBind>`
                    
                    

                    """

                    _prefix = 'snmp-agent-oper'
                    _revision = '2016-06-01'

                    def __init__(self):
                        super(Snmp.Correlator.RuleDetails.RuleDetail.NonRootcaus, self).__init__()

                        self.yang_name = "non-rootcaus"
                        self.yang_parent_name = "rule-detail"

                        self.oid = YLeaf(YType.str, "oid")

                        self.var_bind = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("oid") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Snmp.Correlator.RuleDetails.RuleDetail.NonRootcaus, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Snmp.Correlator.RuleDetails.RuleDetail.NonRootcaus, self).__setattr__(name, value)


                    class VarBind(Entity):
                        """
                        VarBinds of the trap
                        
                        .. attribute:: match_type
                        
                        	Varbind match type
                        	**type**\:   :py:class:`SnmpCorrVbindMatch <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.SnmpCorrVbindMatch>`
                        
                        .. attribute:: oid
                        
                        	OID of the varbind
                        	**type**\:  str
                        
                        .. attribute:: reg_exp
                        
                        	Regular expression to match
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'snmp-agent-oper'
                        _revision = '2016-06-01'

                        def __init__(self):
                            super(Snmp.Correlator.RuleDetails.RuleDetail.NonRootcaus.VarBind, self).__init__()

                            self.yang_name = "var-bind"
                            self.yang_parent_name = "non-rootcaus"

                            self.match_type = YLeaf(YType.enumeration, "match-type")

                            self.oid = YLeaf(YType.str, "oid")

                            self.reg_exp = YLeaf(YType.str, "reg-exp")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("match_type",
                                            "oid",
                                            "reg_exp") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Snmp.Correlator.RuleDetails.RuleDetail.NonRootcaus.VarBind, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Snmp.Correlator.RuleDetails.RuleDetail.NonRootcaus.VarBind, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.match_type.is_set or
                                self.oid.is_set or
                                self.reg_exp.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.match_type.yfilter != YFilter.not_set or
                                self.oid.yfilter != YFilter.not_set or
                                self.reg_exp.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "var-bind" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.match_type.is_set or self.match_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.match_type.get_name_leafdata())
                            if (self.oid.is_set or self.oid.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.oid.get_name_leafdata())
                            if (self.reg_exp.is_set or self.reg_exp.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.reg_exp.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "match-type" or name == "oid" or name == "reg-exp"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "match-type"):
                                self.match_type = value
                                self.match_type.value_namespace = name_space
                                self.match_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "oid"):
                                self.oid = value
                                self.oid.value_namespace = name_space
                                self.oid.value_namespace_prefix = name_space_prefix
                            if(value_path == "reg-exp"):
                                self.reg_exp = value
                                self.reg_exp.value_namespace = name_space
                                self.reg_exp.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.var_bind:
                            if (c.has_data()):
                                return True
                        return self.oid.is_set

                    def has_operation(self):
                        for c in self.var_bind:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.oid.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "non-rootcaus" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.oid.is_set or self.oid.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.oid.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "var-bind"):
                            for c in self.var_bind:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Snmp.Correlator.RuleDetails.RuleDetail.NonRootcaus.VarBind()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.var_bind.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "var-bind" or name == "oid"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "oid"):
                            self.oid = value
                            self.oid.value_namespace = name_space
                            self.oid.value_namespace_prefix = name_space_prefix


                class ApplyHost(Entity):
                    """
                    Hosts (IP/port) to which the rule is applied
                    
                    .. attribute:: ip_address
                    
                    	IP address of the host
                    	**type**\:  str
                    
                    .. attribute:: port
                    
                    	Port of the host
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'snmp-agent-oper'
                    _revision = '2016-06-01'

                    def __init__(self):
                        super(Snmp.Correlator.RuleDetails.RuleDetail.ApplyHost, self).__init__()

                        self.yang_name = "apply-host"
                        self.yang_parent_name = "rule-detail"

                        self.ip_address = YLeaf(YType.str, "ip-address")

                        self.port = YLeaf(YType.uint16, "port")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("ip_address",
                                        "port") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Snmp.Correlator.RuleDetails.RuleDetail.ApplyHost, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Snmp.Correlator.RuleDetails.RuleDetail.ApplyHost, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.ip_address.is_set or
                            self.port.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.ip_address.yfilter != YFilter.not_set or
                            self.port.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "apply-host" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.ip_address.is_set or self.ip_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ip_address.get_name_leafdata())
                        if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.port.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "ip-address" or name == "port"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "ip-address"):
                            self.ip_address = value
                            self.ip_address.value_namespace = name_space
                            self.ip_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "port"):
                            self.port = value
                            self.port.value_namespace = name_space
                            self.port.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.apply_host:
                        if (c.has_data()):
                            return True
                    for c in self.non_rootcaus:
                        if (c.has_data()):
                            return True
                    return (
                        self.rule_name.is_set or
                        self.timeout.is_set or
                        (self.root_cause is not None and self.root_cause.has_data()) or
                        (self.rule_summary is not None and self.rule_summary.has_data()))

                def has_operation(self):
                    for c in self.apply_host:
                        if (c.has_operation()):
                            return True
                    for c in self.non_rootcaus:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.rule_name.yfilter != YFilter.not_set or
                        self.timeout.yfilter != YFilter.not_set or
                        (self.root_cause is not None and self.root_cause.has_operation()) or
                        (self.rule_summary is not None and self.rule_summary.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "rule-detail" + "[rule-name='" + self.rule_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/correlator/rule-details/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.rule_name.is_set or self.rule_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rule_name.get_name_leafdata())
                    if (self.timeout.is_set or self.timeout.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.timeout.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "apply-host"):
                        for c in self.apply_host:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Snmp.Correlator.RuleDetails.RuleDetail.ApplyHost()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.apply_host.append(c)
                        return c

                    if (child_yang_name == "non-rootcaus"):
                        for c in self.non_rootcaus:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Snmp.Correlator.RuleDetails.RuleDetail.NonRootcaus()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.non_rootcaus.append(c)
                        return c

                    if (child_yang_name == "root-cause"):
                        if (self.root_cause is None):
                            self.root_cause = Snmp.Correlator.RuleDetails.RuleDetail.RootCause()
                            self.root_cause.parent = self
                            self._children_name_map["root_cause"] = "root-cause"
                        return self.root_cause

                    if (child_yang_name == "rule-summary"):
                        if (self.rule_summary is None):
                            self.rule_summary = Snmp.Correlator.RuleDetails.RuleDetail.RuleSummary()
                            self.rule_summary.parent = self
                            self._children_name_map["rule_summary"] = "rule-summary"
                        return self.rule_summary

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "apply-host" or name == "non-rootcaus" or name == "root-cause" or name == "rule-summary" or name == "rule-name" or name == "timeout"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "rule-name"):
                        self.rule_name = value
                        self.rule_name.value_namespace = name_space
                        self.rule_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "timeout"):
                        self.timeout = value
                        self.timeout.value_namespace = name_space
                        self.timeout.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.rule_detail:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.rule_detail:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rule-details" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/correlator/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "rule-detail"):
                    for c in self.rule_detail:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Snmp.Correlator.RuleDetails.RuleDetail()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.rule_detail.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "rule-detail"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class BufferStatus(Entity):
            """
            Describes buffer utilization and parameters
            configured
            
            .. attribute:: configured_size
            
            	Configured buffer size
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: current_size
            
            	Current buffer usage
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                super(Snmp.Correlator.BufferStatus, self).__init__()

                self.yang_name = "buffer-status"
                self.yang_parent_name = "correlator"

                self.configured_size = YLeaf(YType.uint32, "configured-size")

                self.current_size = YLeaf(YType.uint32, "current-size")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("configured_size",
                                "current_size") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Snmp.Correlator.BufferStatus, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Snmp.Correlator.BufferStatus, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.configured_size.is_set or
                    self.current_size.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.configured_size.yfilter != YFilter.not_set or
                    self.current_size.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "buffer-status" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/correlator/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.configured_size.is_set or self.configured_size.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.configured_size.get_name_leafdata())
                if (self.current_size.is_set or self.current_size.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.current_size.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "configured-size" or name == "current-size"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "configured-size"):
                    self.configured_size = value
                    self.configured_size.value_namespace = name_space
                    self.configured_size.value_namespace_prefix = name_space_prefix
                if(value_path == "current-size"):
                    self.current_size = value
                    self.current_size.value_namespace = name_space
                    self.current_size.value_namespace_prefix = name_space_prefix


        class RuleSetDetails(Entity):
            """
            Table that contains the ruleset detail info
            
            .. attribute:: rule_set_detail
            
            	Detail of one of the correlation rulesets
            	**type**\: list of    :py:class:`RuleSetDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Correlator.RuleSetDetails.RuleSetDetail>`
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                super(Snmp.Correlator.RuleSetDetails, self).__init__()

                self.yang_name = "rule-set-details"
                self.yang_parent_name = "correlator"

                self.rule_set_detail = YList(self)

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
                            super(Snmp.Correlator.RuleSetDetails, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Snmp.Correlator.RuleSetDetails, self).__setattr__(name, value)


            class RuleSetDetail(Entity):
                """
                Detail of one of the correlation rulesets
                
                .. attribute:: rule_set_name  <key>
                
                	Ruleset Name
                	**type**\:  str
                
                	**length:** 1..32
                
                .. attribute:: rule_set_name_xr
                
                	Ruleset Name
                	**type**\:  str
                
                .. attribute:: rules
                
                	Rules contained in a ruleset
                	**type**\: list of    :py:class:`Rules <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Correlator.RuleSetDetails.RuleSetDetail.Rules>`
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2016-06-01'

                def __init__(self):
                    super(Snmp.Correlator.RuleSetDetails.RuleSetDetail, self).__init__()

                    self.yang_name = "rule-set-detail"
                    self.yang_parent_name = "rule-set-details"

                    self.rule_set_name = YLeaf(YType.str, "rule-set-name")

                    self.rule_set_name_xr = YLeaf(YType.str, "rule-set-name-xr")

                    self.rules = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("rule_set_name",
                                    "rule_set_name_xr") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Snmp.Correlator.RuleSetDetails.RuleSetDetail, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Snmp.Correlator.RuleSetDetails.RuleSetDetail, self).__setattr__(name, value)


                class Rules(Entity):
                    """
                    Rules contained in a ruleset
                    
                    .. attribute:: buffered_traps_count
                    
                    	Number of buffered traps correlated to this rule
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rule_name
                    
                    	Correlation Rule Name
                    	**type**\:  str
                    
                    .. attribute:: rule_state
                    
                    	Applied state of the rule It could be not applied, applied or applied to all
                    	**type**\:   :py:class:`SnmpCorrRuleState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.SnmpCorrRuleState>`
                    
                    

                    """

                    _prefix = 'snmp-agent-oper'
                    _revision = '2016-06-01'

                    def __init__(self):
                        super(Snmp.Correlator.RuleSetDetails.RuleSetDetail.Rules, self).__init__()

                        self.yang_name = "rules"
                        self.yang_parent_name = "rule-set-detail"

                        self.buffered_traps_count = YLeaf(YType.uint32, "buffered-traps-count")

                        self.rule_name = YLeaf(YType.str, "rule-name")

                        self.rule_state = YLeaf(YType.enumeration, "rule-state")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("buffered_traps_count",
                                        "rule_name",
                                        "rule_state") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Snmp.Correlator.RuleSetDetails.RuleSetDetail.Rules, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Snmp.Correlator.RuleSetDetails.RuleSetDetail.Rules, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.buffered_traps_count.is_set or
                            self.rule_name.is_set or
                            self.rule_state.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.buffered_traps_count.yfilter != YFilter.not_set or
                            self.rule_name.yfilter != YFilter.not_set or
                            self.rule_state.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "rules" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.buffered_traps_count.is_set or self.buffered_traps_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.buffered_traps_count.get_name_leafdata())
                        if (self.rule_name.is_set or self.rule_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rule_name.get_name_leafdata())
                        if (self.rule_state.is_set or self.rule_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rule_state.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "buffered-traps-count" or name == "rule-name" or name == "rule-state"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "buffered-traps-count"):
                            self.buffered_traps_count = value
                            self.buffered_traps_count.value_namespace = name_space
                            self.buffered_traps_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "rule-name"):
                            self.rule_name = value
                            self.rule_name.value_namespace = name_space
                            self.rule_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "rule-state"):
                            self.rule_state = value
                            self.rule_state.value_namespace = name_space
                            self.rule_state.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.rules:
                        if (c.has_data()):
                            return True
                    return (
                        self.rule_set_name.is_set or
                        self.rule_set_name_xr.is_set)

                def has_operation(self):
                    for c in self.rules:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.rule_set_name.yfilter != YFilter.not_set or
                        self.rule_set_name_xr.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "rule-set-detail" + "[rule-set-name='" + self.rule_set_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/correlator/rule-set-details/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.rule_set_name.is_set or self.rule_set_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rule_set_name.get_name_leafdata())
                    if (self.rule_set_name_xr.is_set or self.rule_set_name_xr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rule_set_name_xr.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "rules"):
                        for c in self.rules:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Snmp.Correlator.RuleSetDetails.RuleSetDetail.Rules()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.rules.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "rules" or name == "rule-set-name" or name == "rule-set-name-xr"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "rule-set-name"):
                        self.rule_set_name = value
                        self.rule_set_name.value_namespace = name_space
                        self.rule_set_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "rule-set-name-xr"):
                        self.rule_set_name_xr = value
                        self.rule_set_name_xr.value_namespace = name_space
                        self.rule_set_name_xr.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.rule_set_detail:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.rule_set_detail:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rule-set-details" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/correlator/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "rule-set-detail"):
                    for c in self.rule_set_detail:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Snmp.Correlator.RuleSetDetails.RuleSetDetail()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.rule_set_detail.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "rule-set-detail"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Traps(Entity):
            """
            Correlated traps Table
            
            .. attribute:: trap
            
            	One of the correlated traps
            	**type**\: list of    :py:class:`Trap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Correlator.Traps.Trap>`
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                super(Snmp.Correlator.Traps, self).__init__()

                self.yang_name = "traps"
                self.yang_parent_name = "correlator"

                self.trap = YList(self)

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
                            super(Snmp.Correlator.Traps, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Snmp.Correlator.Traps, self).__setattr__(name, value)


            class Trap(Entity):
                """
                One of the correlated traps
                
                .. attribute:: entry_id  <key>
                
                	Entry ID
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: correlation_id
                
                	Correlation ID
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_root_cause
                
                	True if this is the rootcause
                	**type**\:  bool
                
                .. attribute:: rule_name
                
                	Correlation rule name
                	**type**\:  str
                
                .. attribute:: trap_info
                
                	Correlated trap information
                	**type**\:   :py:class:`TrapInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Correlator.Traps.Trap.TrapInfo>`
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2016-06-01'

                def __init__(self):
                    super(Snmp.Correlator.Traps.Trap, self).__init__()

                    self.yang_name = "trap"
                    self.yang_parent_name = "traps"

                    self.entry_id = YLeaf(YType.int32, "entry-id")

                    self.correlation_id = YLeaf(YType.uint32, "correlation-id")

                    self.is_root_cause = YLeaf(YType.boolean, "is-root-cause")

                    self.rule_name = YLeaf(YType.str, "rule-name")

                    self.trap_info = Snmp.Correlator.Traps.Trap.TrapInfo()
                    self.trap_info.parent = self
                    self._children_name_map["trap_info"] = "trap-info"
                    self._children_yang_names.add("trap-info")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("entry_id",
                                    "correlation_id",
                                    "is_root_cause",
                                    "rule_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Snmp.Correlator.Traps.Trap, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Snmp.Correlator.Traps.Trap, self).__setattr__(name, value)


                class TrapInfo(Entity):
                    """
                    Correlated trap information
                    
                    .. attribute:: oid
                    
                    	Object ID
                    	**type**\:  str
                    
                    .. attribute:: relative_timestamp
                    
                    	Number of hsecs elapsed since snmpd was started
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: timestamp
                    
                    	Time when the trap was generated. It is expressed in number of milliseconds since 00\:00 \:00 UTC, January 1, 1970
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: millisecond
                    
                    .. attribute:: var_bind
                    
                    	VarBinds on the trap
                    	**type**\: list of    :py:class:`VarBind <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Correlator.Traps.Trap.TrapInfo.VarBind>`
                    
                    

                    """

                    _prefix = 'snmp-agent-oper'
                    _revision = '2016-06-01'

                    def __init__(self):
                        super(Snmp.Correlator.Traps.Trap.TrapInfo, self).__init__()

                        self.yang_name = "trap-info"
                        self.yang_parent_name = "trap"

                        self.oid = YLeaf(YType.str, "oid")

                        self.relative_timestamp = YLeaf(YType.uint32, "relative-timestamp")

                        self.timestamp = YLeaf(YType.uint64, "timestamp")

                        self.var_bind = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("oid",
                                        "relative_timestamp",
                                        "timestamp") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Snmp.Correlator.Traps.Trap.TrapInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Snmp.Correlator.Traps.Trap.TrapInfo, self).__setattr__(name, value)


                    class VarBind(Entity):
                        """
                        VarBinds on the trap
                        
                        .. attribute:: oid
                        
                        	OID of the varbind
                        	**type**\:  str
                        
                        .. attribute:: value
                        
                        	Value of the varbind
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'snmp-agent-oper'
                        _revision = '2016-06-01'

                        def __init__(self):
                            super(Snmp.Correlator.Traps.Trap.TrapInfo.VarBind, self).__init__()

                            self.yang_name = "var-bind"
                            self.yang_parent_name = "trap-info"

                            self.oid = YLeaf(YType.str, "oid")

                            self.value = YLeaf(YType.str, "value")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("oid",
                                            "value") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Snmp.Correlator.Traps.Trap.TrapInfo.VarBind, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Snmp.Correlator.Traps.Trap.TrapInfo.VarBind, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.oid.is_set or
                                self.value.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.oid.yfilter != YFilter.not_set or
                                self.value.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "var-bind" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.oid.is_set or self.oid.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.oid.get_name_leafdata())
                            if (self.value.is_set or self.value.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.value.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "oid" or name == "value"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "oid"):
                                self.oid = value
                                self.oid.value_namespace = name_space
                                self.oid.value_namespace_prefix = name_space_prefix
                            if(value_path == "value"):
                                self.value = value
                                self.value.value_namespace = name_space
                                self.value.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.var_bind:
                            if (c.has_data()):
                                return True
                        return (
                            self.oid.is_set or
                            self.relative_timestamp.is_set or
                            self.timestamp.is_set)

                    def has_operation(self):
                        for c in self.var_bind:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.oid.yfilter != YFilter.not_set or
                            self.relative_timestamp.yfilter != YFilter.not_set or
                            self.timestamp.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "trap-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.oid.is_set or self.oid.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.oid.get_name_leafdata())
                        if (self.relative_timestamp.is_set or self.relative_timestamp.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.relative_timestamp.get_name_leafdata())
                        if (self.timestamp.is_set or self.timestamp.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.timestamp.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "var-bind"):
                            for c in self.var_bind:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Snmp.Correlator.Traps.Trap.TrapInfo.VarBind()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.var_bind.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "var-bind" or name == "oid" or name == "relative-timestamp" or name == "timestamp"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "oid"):
                            self.oid = value
                            self.oid.value_namespace = name_space
                            self.oid.value_namespace_prefix = name_space_prefix
                        if(value_path == "relative-timestamp"):
                            self.relative_timestamp = value
                            self.relative_timestamp.value_namespace = name_space
                            self.relative_timestamp.value_namespace_prefix = name_space_prefix
                        if(value_path == "timestamp"):
                            self.timestamp = value
                            self.timestamp.value_namespace = name_space
                            self.timestamp.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.entry_id.is_set or
                        self.correlation_id.is_set or
                        self.is_root_cause.is_set or
                        self.rule_name.is_set or
                        (self.trap_info is not None and self.trap_info.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.entry_id.yfilter != YFilter.not_set or
                        self.correlation_id.yfilter != YFilter.not_set or
                        self.is_root_cause.yfilter != YFilter.not_set or
                        self.rule_name.yfilter != YFilter.not_set or
                        (self.trap_info is not None and self.trap_info.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "trap" + "[entry-id='" + self.entry_id.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/correlator/traps/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.entry_id.is_set or self.entry_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.entry_id.get_name_leafdata())
                    if (self.correlation_id.is_set or self.correlation_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.correlation_id.get_name_leafdata())
                    if (self.is_root_cause.is_set or self.is_root_cause.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_root_cause.get_name_leafdata())
                    if (self.rule_name.is_set or self.rule_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rule_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "trap-info"):
                        if (self.trap_info is None):
                            self.trap_info = Snmp.Correlator.Traps.Trap.TrapInfo()
                            self.trap_info.parent = self
                            self._children_name_map["trap_info"] = "trap-info"
                        return self.trap_info

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "trap-info" or name == "entry-id" or name == "correlation-id" or name == "is-root-cause" or name == "rule-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "entry-id"):
                        self.entry_id = value
                        self.entry_id.value_namespace = name_space
                        self.entry_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "correlation-id"):
                        self.correlation_id = value
                        self.correlation_id.value_namespace = name_space
                        self.correlation_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-root-cause"):
                        self.is_root_cause = value
                        self.is_root_cause.value_namespace = name_space
                        self.is_root_cause.value_namespace_prefix = name_space_prefix
                    if(value_path == "rule-name"):
                        self.rule_name = value
                        self.rule_name.value_namespace = name_space
                        self.rule_name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.trap:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.trap:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "traps" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/correlator/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "trap"):
                    for c in self.trap:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Snmp.Correlator.Traps.Trap()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.trap.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "trap"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                (self.buffer_status is not None and self.buffer_status.has_data()) or
                (self.rule_details is not None and self.rule_details.has_data()) or
                (self.rule_set_details is not None and self.rule_set_details.has_data()) or
                (self.traps is not None and self.traps.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.buffer_status is not None and self.buffer_status.has_operation()) or
                (self.rule_details is not None and self.rule_details.has_operation()) or
                (self.rule_set_details is not None and self.rule_set_details.has_operation()) or
                (self.traps is not None and self.traps.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "correlator" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "buffer-status"):
                if (self.buffer_status is None):
                    self.buffer_status = Snmp.Correlator.BufferStatus()
                    self.buffer_status.parent = self
                    self._children_name_map["buffer_status"] = "buffer-status"
                return self.buffer_status

            if (child_yang_name == "rule-details"):
                if (self.rule_details is None):
                    self.rule_details = Snmp.Correlator.RuleDetails()
                    self.rule_details.parent = self
                    self._children_name_map["rule_details"] = "rule-details"
                return self.rule_details

            if (child_yang_name == "rule-set-details"):
                if (self.rule_set_details is None):
                    self.rule_set_details = Snmp.Correlator.RuleSetDetails()
                    self.rule_set_details.parent = self
                    self._children_name_map["rule_set_details"] = "rule-set-details"
                return self.rule_set_details

            if (child_yang_name == "traps"):
                if (self.traps is None):
                    self.traps = Snmp.Correlator.Traps()
                    self.traps.parent = self
                    self._children_name_map["traps"] = "traps"
                return self.traps

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "buffer-status" or name == "rule-details" or name == "rule-set-details" or name == "traps"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class InterfaceIndexes(Entity):
        """
        List of index
        
        .. attribute:: interface_index
        
        	Interface Index
        	**type**\: list of    :py:class:`InterfaceIndex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.InterfaceIndexes.InterfaceIndex>`
        
        

        """

        _prefix = 'snmp-agent-oper'
        _revision = '2016-06-01'

        def __init__(self):
            super(Snmp.InterfaceIndexes, self).__init__()

            self.yang_name = "interface-indexes"
            self.yang_parent_name = "snmp"

            self.interface_index = YList(self)

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
                        super(Snmp.InterfaceIndexes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Snmp.InterfaceIndexes, self).__setattr__(name, value)


        class InterfaceIndex(Entity):
            """
            Interface Index
            
            .. attribute:: interface_index  <key>
            
            	Interface Index as used by MIB tables
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: interface_name
            
            	Interface Name
            	**type**\:  str
            
            	**mandatory**\: True
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                super(Snmp.InterfaceIndexes.InterfaceIndex, self).__init__()

                self.yang_name = "interface-index"
                self.yang_parent_name = "interface-indexes"

                self.interface_index = YLeaf(YType.int32, "interface-index")

                self.interface_name = YLeaf(YType.str, "interface-name")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("interface_index",
                                "interface_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Snmp.InterfaceIndexes.InterfaceIndex, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Snmp.InterfaceIndexes.InterfaceIndex, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.interface_index.is_set or
                    self.interface_name.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.interface_index.yfilter != YFilter.not_set or
                    self.interface_name.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "interface-index" + "[interface-index='" + self.interface_index.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/interface-indexes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.interface_index.is_set or self.interface_index.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface_index.get_name_leafdata())
                if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "interface-index" or name == "interface-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "interface-index"):
                    self.interface_index = value
                    self.interface_index.value_namespace = name_space
                    self.interface_index.value_namespace_prefix = name_space_prefix
                if(value_path == "interface-name"):
                    self.interface_name = value
                    self.interface_name.value_namespace = name_space
                    self.interface_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.interface_index:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.interface_index:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "interface-indexes" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "interface-index"):
                for c in self.interface_index:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Snmp.InterfaceIndexes.InterfaceIndex()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.interface_index.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "interface-index"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class IfIndexes(Entity):
        """
        List of ifnames
        
        .. attribute:: if_index
        
        	Interface Index
        	**type**\: list of    :py:class:`IfIndex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.IfIndexes.IfIndex>`
        
        

        """

        _prefix = 'snmp-agent-oper'
        _revision = '2016-06-01'

        def __init__(self):
            super(Snmp.IfIndexes, self).__init__()

            self.yang_name = "if-indexes"
            self.yang_parent_name = "snmp"

            self.if_index = YList(self)

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
                        super(Snmp.IfIndexes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Snmp.IfIndexes, self).__setattr__(name, value)


        class IfIndex(Entity):
            """
            Interface Index
            
            .. attribute:: interface_index  <key>
            
            	Interface Index as used by MIB tables
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: interface_name
            
            	Interface Name
            	**type**\:  str
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                super(Snmp.IfIndexes.IfIndex, self).__init__()

                self.yang_name = "if-index"
                self.yang_parent_name = "if-indexes"

                self.interface_index = YLeaf(YType.int32, "interface-index")

                self.interface_name = YLeaf(YType.str, "interface-name")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("interface_index",
                                "interface_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Snmp.IfIndexes.IfIndex, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Snmp.IfIndexes.IfIndex, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.interface_index.is_set or
                    self.interface_name.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.interface_index.yfilter != YFilter.not_set or
                    self.interface_name.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "if-index" + "[interface-index='" + self.interface_index.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/if-indexes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.interface_index.is_set or self.interface_index.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface_index.get_name_leafdata())
                if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "interface-index" or name == "interface-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "interface-index"):
                    self.interface_index = value
                    self.interface_index.value_namespace = name_space
                    self.interface_index.value_namespace_prefix = name_space_prefix
                if(value_path == "interface-name"):
                    self.interface_name = value
                    self.interface_name.value_namespace = name_space
                    self.interface_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.if_index:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.if_index:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "if-indexes" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "if-index"):
                for c in self.if_index:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Snmp.IfIndexes.IfIndex()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.if_index.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "if-index"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class EntityMib(Entity):
        """
        SNMP entity mib
        
        .. attribute:: entity_physical_indexes
        
        	SNMP entity mib
        	**type**\:   :py:class:`EntityPhysicalIndexes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.EntityMib.EntityPhysicalIndexes>`
        
        

        """

        _prefix = 'snmp-entitymib-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Snmp.EntityMib, self).__init__()

            self.yang_name = "entity-mib"
            self.yang_parent_name = "snmp"

            self.entity_physical_indexes = Snmp.EntityMib.EntityPhysicalIndexes()
            self.entity_physical_indexes.parent = self
            self._children_name_map["entity_physical_indexes"] = "entity-physical-indexes"
            self._children_yang_names.add("entity-physical-indexes")


        class EntityPhysicalIndexes(Entity):
            """
            SNMP entity mib
            
            .. attribute:: entity_physical_index
            
            	SNMP entPhysical index number
            	**type**\: list of    :py:class:`EntityPhysicalIndex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.EntityMib.EntityPhysicalIndexes.EntityPhysicalIndex>`
            
            

            """

            _prefix = 'snmp-entitymib-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Snmp.EntityMib.EntityPhysicalIndexes, self).__init__()

                self.yang_name = "entity-physical-indexes"
                self.yang_parent_name = "entity-mib"

                self.entity_physical_index = YList(self)

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
                            super(Snmp.EntityMib.EntityPhysicalIndexes, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Snmp.EntityMib.EntityPhysicalIndexes, self).__setattr__(name, value)


            class EntityPhysicalIndex(Entity):
                """
                SNMP entPhysical index number
                
                .. attribute:: entity_phynum  <key>
                
                	Entity physical index
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: ent_physical_descr
                
                	EntPhysicalDescription
                	**type**\:  str
                
                .. attribute:: ent_physical_firmware_rev
                
                	entphysicalFirmwareRev
                	**type**\:  str
                
                .. attribute:: ent_physical_hardware_rev
                
                	entphysicalHardwareRev
                	**type**\:  str
                
                .. attribute:: ent_physical_mfg_name
                
                	entphysicalMfgName
                	**type**\:  str
                
                .. attribute:: ent_physical_modelname
                
                	entphysicalModelName
                	**type**\:  str
                
                .. attribute:: ent_physical_name
                
                	entPhysicalName
                	**type**\:  str
                
                .. attribute:: ent_physical_serial_num
                
                	entphysicalSerialNum
                	**type**\:  str
                
                .. attribute:: ent_physical_software_rev
                
                	entphysicalSoftwareRev
                	**type**\:  str
                
                .. attribute:: location
                
                	invmgr EDM path
                	**type**\:  str
                
                .. attribute:: physical_index
                
                	entPhysicalIndex
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'snmp-entitymib-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Snmp.EntityMib.EntityPhysicalIndexes.EntityPhysicalIndex, self).__init__()

                    self.yang_name = "entity-physical-index"
                    self.yang_parent_name = "entity-physical-indexes"

                    self.entity_phynum = YLeaf(YType.str, "entity-phynum")

                    self.ent_physical_descr = YLeaf(YType.str, "ent-physical-descr")

                    self.ent_physical_firmware_rev = YLeaf(YType.str, "ent-physical-firmware-rev")

                    self.ent_physical_hardware_rev = YLeaf(YType.str, "ent-physical-hardware-rev")

                    self.ent_physical_mfg_name = YLeaf(YType.str, "ent-physical-mfg-name")

                    self.ent_physical_modelname = YLeaf(YType.str, "ent-physical-modelname")

                    self.ent_physical_name = YLeaf(YType.str, "ent-physical-name")

                    self.ent_physical_serial_num = YLeaf(YType.str, "ent-physical-serial-num")

                    self.ent_physical_software_rev = YLeaf(YType.str, "ent-physical-software-rev")

                    self.location = YLeaf(YType.str, "location")

                    self.physical_index = YLeaf(YType.uint32, "physical-index")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("entity_phynum",
                                    "ent_physical_descr",
                                    "ent_physical_firmware_rev",
                                    "ent_physical_hardware_rev",
                                    "ent_physical_mfg_name",
                                    "ent_physical_modelname",
                                    "ent_physical_name",
                                    "ent_physical_serial_num",
                                    "ent_physical_software_rev",
                                    "location",
                                    "physical_index") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Snmp.EntityMib.EntityPhysicalIndexes.EntityPhysicalIndex, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Snmp.EntityMib.EntityPhysicalIndexes.EntityPhysicalIndex, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.entity_phynum.is_set or
                        self.ent_physical_descr.is_set or
                        self.ent_physical_firmware_rev.is_set or
                        self.ent_physical_hardware_rev.is_set or
                        self.ent_physical_mfg_name.is_set or
                        self.ent_physical_modelname.is_set or
                        self.ent_physical_name.is_set or
                        self.ent_physical_serial_num.is_set or
                        self.ent_physical_software_rev.is_set or
                        self.location.is_set or
                        self.physical_index.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.entity_phynum.yfilter != YFilter.not_set or
                        self.ent_physical_descr.yfilter != YFilter.not_set or
                        self.ent_physical_firmware_rev.yfilter != YFilter.not_set or
                        self.ent_physical_hardware_rev.yfilter != YFilter.not_set or
                        self.ent_physical_mfg_name.yfilter != YFilter.not_set or
                        self.ent_physical_modelname.yfilter != YFilter.not_set or
                        self.ent_physical_name.yfilter != YFilter.not_set or
                        self.ent_physical_serial_num.yfilter != YFilter.not_set or
                        self.ent_physical_software_rev.yfilter != YFilter.not_set or
                        self.location.yfilter != YFilter.not_set or
                        self.physical_index.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "entity-physical-index" + "[entity-phynum='" + self.entity_phynum.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-entitymib-oper:entity-mib/entity-physical-indexes/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.entity_phynum.is_set or self.entity_phynum.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.entity_phynum.get_name_leafdata())
                    if (self.ent_physical_descr.is_set or self.ent_physical_descr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ent_physical_descr.get_name_leafdata())
                    if (self.ent_physical_firmware_rev.is_set or self.ent_physical_firmware_rev.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ent_physical_firmware_rev.get_name_leafdata())
                    if (self.ent_physical_hardware_rev.is_set or self.ent_physical_hardware_rev.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ent_physical_hardware_rev.get_name_leafdata())
                    if (self.ent_physical_mfg_name.is_set or self.ent_physical_mfg_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ent_physical_mfg_name.get_name_leafdata())
                    if (self.ent_physical_modelname.is_set or self.ent_physical_modelname.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ent_physical_modelname.get_name_leafdata())
                    if (self.ent_physical_name.is_set or self.ent_physical_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ent_physical_name.get_name_leafdata())
                    if (self.ent_physical_serial_num.is_set or self.ent_physical_serial_num.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ent_physical_serial_num.get_name_leafdata())
                    if (self.ent_physical_software_rev.is_set or self.ent_physical_software_rev.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ent_physical_software_rev.get_name_leafdata())
                    if (self.location.is_set or self.location.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.location.get_name_leafdata())
                    if (self.physical_index.is_set or self.physical_index.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.physical_index.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "entity-phynum" or name == "ent-physical-descr" or name == "ent-physical-firmware-rev" or name == "ent-physical-hardware-rev" or name == "ent-physical-mfg-name" or name == "ent-physical-modelname" or name == "ent-physical-name" or name == "ent-physical-serial-num" or name == "ent-physical-software-rev" or name == "location" or name == "physical-index"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "entity-phynum"):
                        self.entity_phynum = value
                        self.entity_phynum.value_namespace = name_space
                        self.entity_phynum.value_namespace_prefix = name_space_prefix
                    if(value_path == "ent-physical-descr"):
                        self.ent_physical_descr = value
                        self.ent_physical_descr.value_namespace = name_space
                        self.ent_physical_descr.value_namespace_prefix = name_space_prefix
                    if(value_path == "ent-physical-firmware-rev"):
                        self.ent_physical_firmware_rev = value
                        self.ent_physical_firmware_rev.value_namespace = name_space
                        self.ent_physical_firmware_rev.value_namespace_prefix = name_space_prefix
                    if(value_path == "ent-physical-hardware-rev"):
                        self.ent_physical_hardware_rev = value
                        self.ent_physical_hardware_rev.value_namespace = name_space
                        self.ent_physical_hardware_rev.value_namespace_prefix = name_space_prefix
                    if(value_path == "ent-physical-mfg-name"):
                        self.ent_physical_mfg_name = value
                        self.ent_physical_mfg_name.value_namespace = name_space
                        self.ent_physical_mfg_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "ent-physical-modelname"):
                        self.ent_physical_modelname = value
                        self.ent_physical_modelname.value_namespace = name_space
                        self.ent_physical_modelname.value_namespace_prefix = name_space_prefix
                    if(value_path == "ent-physical-name"):
                        self.ent_physical_name = value
                        self.ent_physical_name.value_namespace = name_space
                        self.ent_physical_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "ent-physical-serial-num"):
                        self.ent_physical_serial_num = value
                        self.ent_physical_serial_num.value_namespace = name_space
                        self.ent_physical_serial_num.value_namespace_prefix = name_space_prefix
                    if(value_path == "ent-physical-software-rev"):
                        self.ent_physical_software_rev = value
                        self.ent_physical_software_rev.value_namespace = name_space
                        self.ent_physical_software_rev.value_namespace_prefix = name_space_prefix
                    if(value_path == "location"):
                        self.location = value
                        self.location.value_namespace = name_space
                        self.location.value_namespace_prefix = name_space_prefix
                    if(value_path == "physical-index"):
                        self.physical_index = value
                        self.physical_index.value_namespace = name_space
                        self.physical_index.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.entity_physical_index:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.entity_physical_index:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "entity-physical-indexes" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-entitymib-oper:entity-mib/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "entity-physical-index"):
                    for c in self.entity_physical_index:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Snmp.EntityMib.EntityPhysicalIndexes.EntityPhysicalIndex()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.entity_physical_index.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entity-physical-index"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (self.entity_physical_indexes is not None and self.entity_physical_indexes.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.entity_physical_indexes is not None and self.entity_physical_indexes.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "Cisco-IOS-XR-snmp-entitymib-oper:entity-mib" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "entity-physical-indexes"):
                if (self.entity_physical_indexes is None):
                    self.entity_physical_indexes = Snmp.EntityMib.EntityPhysicalIndexes()
                    self.entity_physical_indexes.parent = self
                    self._children_name_map["entity_physical_indexes"] = "entity-physical-indexes"
                return self.entity_physical_indexes

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "entity-physical-indexes"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class InterfaceMib(Entity):
        """
        SNMP IF\-MIB information
        
        .. attribute:: interface_aliases
        
        	Interfaces ifAlias information
        	**type**\:   :py:class:`InterfaceAliases <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.InterfaceMib.InterfaceAliases>`
        
        .. attribute:: interface_connectors
        
        	Interfaces ifConnectorPresent information
        	**type**\:   :py:class:`InterfaceConnectors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.InterfaceMib.InterfaceConnectors>`
        
        .. attribute:: interface_stack_statuses
        
        	Interfaces ifstackstatus information
        	**type**\:   :py:class:`InterfaceStackStatuses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.InterfaceMib.InterfaceStackStatuses>`
        
        .. attribute:: interfaces
        
        	Interfaces ifIndex information
        	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.InterfaceMib.Interfaces>`
        
        .. attribute:: notification_interfaces
        
        	Interfaces Notification information
        	**type**\:   :py:class:`NotificationInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.InterfaceMib.NotificationInterfaces>`
        
        

        """

        _prefix = 'snmp-ifmib-oper'
        _revision = '2015-01-07'

        def __init__(self):
            super(Snmp.InterfaceMib, self).__init__()

            self.yang_name = "interface-mib"
            self.yang_parent_name = "snmp"

            self.interface_aliases = Snmp.InterfaceMib.InterfaceAliases()
            self.interface_aliases.parent = self
            self._children_name_map["interface_aliases"] = "interface-aliases"
            self._children_yang_names.add("interface-aliases")

            self.interface_connectors = Snmp.InterfaceMib.InterfaceConnectors()
            self.interface_connectors.parent = self
            self._children_name_map["interface_connectors"] = "interface-connectors"
            self._children_yang_names.add("interface-connectors")

            self.interface_stack_statuses = Snmp.InterfaceMib.InterfaceStackStatuses()
            self.interface_stack_statuses.parent = self
            self._children_name_map["interface_stack_statuses"] = "interface-stack-statuses"
            self._children_yang_names.add("interface-stack-statuses")

            self.interfaces = Snmp.InterfaceMib.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"
            self._children_yang_names.add("interfaces")

            self.notification_interfaces = Snmp.InterfaceMib.NotificationInterfaces()
            self.notification_interfaces.parent = self
            self._children_name_map["notification_interfaces"] = "notification-interfaces"
            self._children_yang_names.add("notification-interfaces")


        class Interfaces(Entity):
            """
            Interfaces ifIndex information
            
            .. attribute:: interface
            
            	ifIndex for a specific Interface Name
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.InterfaceMib.Interfaces.Interface>`
            
            

            """

            _prefix = 'snmp-ifmib-oper'
            _revision = '2015-01-07'

            def __init__(self):
                super(Snmp.InterfaceMib.Interfaces, self).__init__()

                self.yang_name = "interfaces"
                self.yang_parent_name = "interface-mib"

                self.interface = YList(self)

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
                            super(Snmp.InterfaceMib.Interfaces, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Snmp.InterfaceMib.Interfaces, self).__setattr__(name, value)


            class Interface(Entity):
                """
                ifIndex for a specific Interface Name
                
                .. attribute:: interface_name  <key>
                
                	Interface Name
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: if_index
                
                	Interface Index
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'snmp-ifmib-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    super(Snmp.InterfaceMib.Interfaces.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interfaces"

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.if_index = YLeaf(YType.uint32, "if-index")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("interface_name",
                                    "if_index") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Snmp.InterfaceMib.Interfaces.Interface, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Snmp.InterfaceMib.Interfaces.Interface, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.interface_name.is_set or
                        self.if_index.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.interface_name.yfilter != YFilter.not_set or
                        self.if_index.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-ifmib-oper:interface-mib/interfaces/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_name.get_name_leafdata())
                    if (self.if_index.is_set or self.if_index.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.if_index.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface-name" or name == "if-index"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "interface-name"):
                        self.interface_name = value
                        self.interface_name.value_namespace = name_space
                        self.interface_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "if-index"):
                        self.if_index = value
                        self.if_index.value_namespace = name_space
                        self.if_index.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.interface:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.interface:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "interfaces" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-ifmib-oper:interface-mib/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "interface"):
                    for c in self.interface:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Snmp.InterfaceMib.Interfaces.Interface()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.interface.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "interface"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class InterfaceConnectors(Entity):
            """
            Interfaces ifConnectorPresent information
            
            .. attribute:: interface_connector
            
            	ifConnectorPresent for a specific Interface Name
            	**type**\: list of    :py:class:`InterfaceConnector <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.InterfaceMib.InterfaceConnectors.InterfaceConnector>`
            
            

            """

            _prefix = 'snmp-ifmib-oper'
            _revision = '2015-01-07'

            def __init__(self):
                super(Snmp.InterfaceMib.InterfaceConnectors, self).__init__()

                self.yang_name = "interface-connectors"
                self.yang_parent_name = "interface-mib"

                self.interface_connector = YList(self)

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
                            super(Snmp.InterfaceMib.InterfaceConnectors, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Snmp.InterfaceMib.InterfaceConnectors, self).__setattr__(name, value)


            class InterfaceConnector(Entity):
                """
                ifConnectorPresent for a specific Interface
                Name
                
                .. attribute:: interface_name  <key>
                
                	Interface Name
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: if_connector_present
                
                	Interface ifConnector
                	**type**\:  str
                
                

                """

                _prefix = 'snmp-ifmib-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    super(Snmp.InterfaceMib.InterfaceConnectors.InterfaceConnector, self).__init__()

                    self.yang_name = "interface-connector"
                    self.yang_parent_name = "interface-connectors"

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.if_connector_present = YLeaf(YType.str, "if-connector-present")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("interface_name",
                                    "if_connector_present") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Snmp.InterfaceMib.InterfaceConnectors.InterfaceConnector, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Snmp.InterfaceMib.InterfaceConnectors.InterfaceConnector, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.interface_name.is_set or
                        self.if_connector_present.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.interface_name.yfilter != YFilter.not_set or
                        self.if_connector_present.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interface-connector" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-ifmib-oper:interface-mib/interface-connectors/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_name.get_name_leafdata())
                    if (self.if_connector_present.is_set or self.if_connector_present.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.if_connector_present.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface-name" or name == "if-connector-present"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "interface-name"):
                        self.interface_name = value
                        self.interface_name.value_namespace = name_space
                        self.interface_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "if-connector-present"):
                        self.if_connector_present = value
                        self.if_connector_present.value_namespace = name_space
                        self.if_connector_present.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.interface_connector:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.interface_connector:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "interface-connectors" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-ifmib-oper:interface-mib/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "interface-connector"):
                    for c in self.interface_connector:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Snmp.InterfaceMib.InterfaceConnectors.InterfaceConnector()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.interface_connector.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "interface-connector"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class InterfaceAliases(Entity):
            """
            Interfaces ifAlias information
            
            .. attribute:: interface_alias
            
            	ifAlias for a specific Interface Name
            	**type**\: list of    :py:class:`InterfaceAlias <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.InterfaceMib.InterfaceAliases.InterfaceAlias>`
            
            

            """

            _prefix = 'snmp-ifmib-oper'
            _revision = '2015-01-07'

            def __init__(self):
                super(Snmp.InterfaceMib.InterfaceAliases, self).__init__()

                self.yang_name = "interface-aliases"
                self.yang_parent_name = "interface-mib"

                self.interface_alias = YList(self)

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
                            super(Snmp.InterfaceMib.InterfaceAliases, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Snmp.InterfaceMib.InterfaceAliases, self).__setattr__(name, value)


            class InterfaceAlias(Entity):
                """
                ifAlias for a specific Interface Name
                
                .. attribute:: interface_name  <key>
                
                	Interface Name
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: if_alias
                
                	Interface ifAlias
                	**type**\:  str
                
                

                """

                _prefix = 'snmp-ifmib-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    super(Snmp.InterfaceMib.InterfaceAliases.InterfaceAlias, self).__init__()

                    self.yang_name = "interface-alias"
                    self.yang_parent_name = "interface-aliases"

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.if_alias = YLeaf(YType.str, "if-alias")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("interface_name",
                                    "if_alias") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Snmp.InterfaceMib.InterfaceAliases.InterfaceAlias, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Snmp.InterfaceMib.InterfaceAliases.InterfaceAlias, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.interface_name.is_set or
                        self.if_alias.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.interface_name.yfilter != YFilter.not_set or
                        self.if_alias.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interface-alias" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-ifmib-oper:interface-mib/interface-aliases/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_name.get_name_leafdata())
                    if (self.if_alias.is_set or self.if_alias.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.if_alias.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface-name" or name == "if-alias"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "interface-name"):
                        self.interface_name = value
                        self.interface_name.value_namespace = name_space
                        self.interface_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "if-alias"):
                        self.if_alias = value
                        self.if_alias.value_namespace = name_space
                        self.if_alias.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.interface_alias:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.interface_alias:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "interface-aliases" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-ifmib-oper:interface-mib/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "interface-alias"):
                    for c in self.interface_alias:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Snmp.InterfaceMib.InterfaceAliases.InterfaceAlias()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.interface_alias.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "interface-alias"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class NotificationInterfaces(Entity):
            """
            Interfaces Notification information
            
            .. attribute:: notification_interface
            
            	Notification for specific Interface Name
            	**type**\: list of    :py:class:`NotificationInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.InterfaceMib.NotificationInterfaces.NotificationInterface>`
            
            

            """

            _prefix = 'snmp-ifmib-oper'
            _revision = '2015-01-07'

            def __init__(self):
                super(Snmp.InterfaceMib.NotificationInterfaces, self).__init__()

                self.yang_name = "notification-interfaces"
                self.yang_parent_name = "interface-mib"

                self.notification_interface = YList(self)

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
                            super(Snmp.InterfaceMib.NotificationInterfaces, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Snmp.InterfaceMib.NotificationInterfaces, self).__setattr__(name, value)


            class NotificationInterface(Entity):
                """
                Notification for specific Interface Name
                
                .. attribute:: interface_name  <key>
                
                	Interface Name
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: link_up_down_notif_status
                
                	LinkUpDown notification status
                	**type**\:   :py:class:`LinkUpDownStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_ifmib_oper.LinkUpDownStatus>`
                
                

                """

                _prefix = 'snmp-ifmib-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    super(Snmp.InterfaceMib.NotificationInterfaces.NotificationInterface, self).__init__()

                    self.yang_name = "notification-interface"
                    self.yang_parent_name = "notification-interfaces"

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.link_up_down_notif_status = YLeaf(YType.enumeration, "link-up-down-notif-status")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("interface_name",
                                    "link_up_down_notif_status") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Snmp.InterfaceMib.NotificationInterfaces.NotificationInterface, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Snmp.InterfaceMib.NotificationInterfaces.NotificationInterface, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.interface_name.is_set or
                        self.link_up_down_notif_status.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.interface_name.yfilter != YFilter.not_set or
                        self.link_up_down_notif_status.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "notification-interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-ifmib-oper:interface-mib/notification-interfaces/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_name.get_name_leafdata())
                    if (self.link_up_down_notif_status.is_set or self.link_up_down_notif_status.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.link_up_down_notif_status.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface-name" or name == "link-up-down-notif-status"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "interface-name"):
                        self.interface_name = value
                        self.interface_name.value_namespace = name_space
                        self.interface_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "link-up-down-notif-status"):
                        self.link_up_down_notif_status = value
                        self.link_up_down_notif_status.value_namespace = name_space
                        self.link_up_down_notif_status.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.notification_interface:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.notification_interface:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "notification-interfaces" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-ifmib-oper:interface-mib/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "notification-interface"):
                    for c in self.notification_interface:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Snmp.InterfaceMib.NotificationInterfaces.NotificationInterface()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.notification_interface.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "notification-interface"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class InterfaceStackStatuses(Entity):
            """
            Interfaces ifstackstatus information
            
            .. attribute:: interface_stack_status
            
            	ifstatus for a pair of Interface
            	**type**\: list of    :py:class:`InterfaceStackStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.InterfaceMib.InterfaceStackStatuses.InterfaceStackStatus>`
            
            

            """

            _prefix = 'snmp-ifmib-oper'
            _revision = '2015-01-07'

            def __init__(self):
                super(Snmp.InterfaceMib.InterfaceStackStatuses, self).__init__()

                self.yang_name = "interface-stack-statuses"
                self.yang_parent_name = "interface-mib"

                self.interface_stack_status = YList(self)

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
                            super(Snmp.InterfaceMib.InterfaceStackStatuses, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Snmp.InterfaceMib.InterfaceStackStatuses, self).__setattr__(name, value)


            class InterfaceStackStatus(Entity):
                """
                ifstatus for a pair of Interface
                
                .. attribute:: interface_stack_status  <key>
                
                	StackHigherLayer.StackLowerLayer
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: if_stack_higher_layer
                
                	Higher Layer Index
                	**type**\:  str
                
                .. attribute:: if_stack_lower_layer
                
                	Lowyer Layer Index
                	**type**\:  str
                
                .. attribute:: if_stack_status
                
                	Interface ifStackStaus info
                	**type**\:  str
                
                

                """

                _prefix = 'snmp-ifmib-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    super(Snmp.InterfaceMib.InterfaceStackStatuses.InterfaceStackStatus, self).__init__()

                    self.yang_name = "interface-stack-status"
                    self.yang_parent_name = "interface-stack-statuses"

                    self.interface_stack_status = YLeaf(YType.str, "interface-stack-status")

                    self.if_stack_higher_layer = YLeaf(YType.str, "if-stack-higher-layer")

                    self.if_stack_lower_layer = YLeaf(YType.str, "if-stack-lower-layer")

                    self.if_stack_status = YLeaf(YType.str, "if-stack-status")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("interface_stack_status",
                                    "if_stack_higher_layer",
                                    "if_stack_lower_layer",
                                    "if_stack_status") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Snmp.InterfaceMib.InterfaceStackStatuses.InterfaceStackStatus, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Snmp.InterfaceMib.InterfaceStackStatuses.InterfaceStackStatus, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.interface_stack_status.is_set or
                        self.if_stack_higher_layer.is_set or
                        self.if_stack_lower_layer.is_set or
                        self.if_stack_status.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.interface_stack_status.yfilter != YFilter.not_set or
                        self.if_stack_higher_layer.yfilter != YFilter.not_set or
                        self.if_stack_lower_layer.yfilter != YFilter.not_set or
                        self.if_stack_status.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interface-stack-status" + "[interface-stack-status='" + self.interface_stack_status.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-ifmib-oper:interface-mib/interface-stack-statuses/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.interface_stack_status.is_set or self.interface_stack_status.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_stack_status.get_name_leafdata())
                    if (self.if_stack_higher_layer.is_set or self.if_stack_higher_layer.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.if_stack_higher_layer.get_name_leafdata())
                    if (self.if_stack_lower_layer.is_set or self.if_stack_lower_layer.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.if_stack_lower_layer.get_name_leafdata())
                    if (self.if_stack_status.is_set or self.if_stack_status.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.if_stack_status.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface-stack-status" or name == "if-stack-higher-layer" or name == "if-stack-lower-layer" or name == "if-stack-status"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "interface-stack-status"):
                        self.interface_stack_status = value
                        self.interface_stack_status.value_namespace = name_space
                        self.interface_stack_status.value_namespace_prefix = name_space_prefix
                    if(value_path == "if-stack-higher-layer"):
                        self.if_stack_higher_layer = value
                        self.if_stack_higher_layer.value_namespace = name_space
                        self.if_stack_higher_layer.value_namespace_prefix = name_space_prefix
                    if(value_path == "if-stack-lower-layer"):
                        self.if_stack_lower_layer = value
                        self.if_stack_lower_layer.value_namespace = name_space
                        self.if_stack_lower_layer.value_namespace_prefix = name_space_prefix
                    if(value_path == "if-stack-status"):
                        self.if_stack_status = value
                        self.if_stack_status.value_namespace = name_space
                        self.if_stack_status.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.interface_stack_status:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.interface_stack_status:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "interface-stack-statuses" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-ifmib-oper:interface-mib/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "interface-stack-status"):
                    for c in self.interface_stack_status:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Snmp.InterfaceMib.InterfaceStackStatuses.InterfaceStackStatus()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.interface_stack_status.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "interface-stack-status"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                (self.interface_aliases is not None and self.interface_aliases.has_data()) or
                (self.interface_connectors is not None and self.interface_connectors.has_data()) or
                (self.interface_stack_statuses is not None and self.interface_stack_statuses.has_data()) or
                (self.interfaces is not None and self.interfaces.has_data()) or
                (self.notification_interfaces is not None and self.notification_interfaces.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.interface_aliases is not None and self.interface_aliases.has_operation()) or
                (self.interface_connectors is not None and self.interface_connectors.has_operation()) or
                (self.interface_stack_statuses is not None and self.interface_stack_statuses.has_operation()) or
                (self.interfaces is not None and self.interfaces.has_operation()) or
                (self.notification_interfaces is not None and self.notification_interfaces.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "Cisco-IOS-XR-snmp-ifmib-oper:interface-mib" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "interface-aliases"):
                if (self.interface_aliases is None):
                    self.interface_aliases = Snmp.InterfaceMib.InterfaceAliases()
                    self.interface_aliases.parent = self
                    self._children_name_map["interface_aliases"] = "interface-aliases"
                return self.interface_aliases

            if (child_yang_name == "interface-connectors"):
                if (self.interface_connectors is None):
                    self.interface_connectors = Snmp.InterfaceMib.InterfaceConnectors()
                    self.interface_connectors.parent = self
                    self._children_name_map["interface_connectors"] = "interface-connectors"
                return self.interface_connectors

            if (child_yang_name == "interface-stack-statuses"):
                if (self.interface_stack_statuses is None):
                    self.interface_stack_statuses = Snmp.InterfaceMib.InterfaceStackStatuses()
                    self.interface_stack_statuses.parent = self
                    self._children_name_map["interface_stack_statuses"] = "interface-stack-statuses"
                return self.interface_stack_statuses

            if (child_yang_name == "interfaces"):
                if (self.interfaces is None):
                    self.interfaces = Snmp.InterfaceMib.Interfaces()
                    self.interfaces.parent = self
                    self._children_name_map["interfaces"] = "interfaces"
                return self.interfaces

            if (child_yang_name == "notification-interfaces"):
                if (self.notification_interfaces is None):
                    self.notification_interfaces = Snmp.InterfaceMib.NotificationInterfaces()
                    self.notification_interfaces.parent = self
                    self._children_name_map["notification_interfaces"] = "notification-interfaces"
                return self.notification_interfaces

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "interface-aliases" or name == "interface-connectors" or name == "interface-stack-statuses" or name == "interfaces" or name == "notification-interfaces"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class SensorMib(Entity):
        """
        SNMP sensor MIB information
        
        .. attribute:: ent_phy_indexes
        
        	List of physical index 
        	**type**\:   :py:class:`EntPhyIndexes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.SensorMib.EntPhyIndexes>`
        
        .. attribute:: physical_indexes
        
        	List of physical index table for threshold value
        	**type**\:   :py:class:`PhysicalIndexes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.SensorMib.PhysicalIndexes>`
        
        

        """

        _prefix = 'snmp-sensormib-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Snmp.SensorMib, self).__init__()

            self.yang_name = "sensor-mib"
            self.yang_parent_name = "snmp"

            self.ent_phy_indexes = Snmp.SensorMib.EntPhyIndexes()
            self.ent_phy_indexes.parent = self
            self._children_name_map["ent_phy_indexes"] = "ent-phy-indexes"
            self._children_yang_names.add("ent-phy-indexes")

            self.physical_indexes = Snmp.SensorMib.PhysicalIndexes()
            self.physical_indexes.parent = self
            self._children_name_map["physical_indexes"] = "physical-indexes"
            self._children_yang_names.add("physical-indexes")


        class PhysicalIndexes(Entity):
            """
            List of physical index table for threshold
            value
            
            .. attribute:: physical_index
            
            	Threshold value for physical index
            	**type**\: list of    :py:class:`PhysicalIndex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.SensorMib.PhysicalIndexes.PhysicalIndex>`
            
            

            """

            _prefix = 'snmp-sensormib-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Snmp.SensorMib.PhysicalIndexes, self).__init__()

                self.yang_name = "physical-indexes"
                self.yang_parent_name = "sensor-mib"

                self.physical_index = YList(self)

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
                            super(Snmp.SensorMib.PhysicalIndexes, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Snmp.SensorMib.PhysicalIndexes, self).__setattr__(name, value)


            class PhysicalIndex(Entity):
                """
                Threshold value for physical index
                
                .. attribute:: index  <key>
                
                	Physical index
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: threshold_indexes
                
                	List of threshold index
                	**type**\:   :py:class:`ThresholdIndexes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.SensorMib.PhysicalIndexes.PhysicalIndex.ThresholdIndexes>`
                
                

                """

                _prefix = 'snmp-sensormib-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Snmp.SensorMib.PhysicalIndexes.PhysicalIndex, self).__init__()

                    self.yang_name = "physical-index"
                    self.yang_parent_name = "physical-indexes"

                    self.index = YLeaf(YType.str, "index")

                    self.threshold_indexes = Snmp.SensorMib.PhysicalIndexes.PhysicalIndex.ThresholdIndexes()
                    self.threshold_indexes.parent = self
                    self._children_name_map["threshold_indexes"] = "threshold-indexes"
                    self._children_yang_names.add("threshold-indexes")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("index") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Snmp.SensorMib.PhysicalIndexes.PhysicalIndex, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Snmp.SensorMib.PhysicalIndexes.PhysicalIndex, self).__setattr__(name, value)


                class ThresholdIndexes(Entity):
                    """
                    List of threshold index
                    
                    .. attribute:: threshold_index
                    
                    	Threshold value for threshold index
                    	**type**\: list of    :py:class:`ThresholdIndex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.SensorMib.PhysicalIndexes.PhysicalIndex.ThresholdIndexes.ThresholdIndex>`
                    
                    

                    """

                    _prefix = 'snmp-sensormib-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Snmp.SensorMib.PhysicalIndexes.PhysicalIndex.ThresholdIndexes, self).__init__()

                        self.yang_name = "threshold-indexes"
                        self.yang_parent_name = "physical-index"

                        self.threshold_index = YList(self)

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
                                    super(Snmp.SensorMib.PhysicalIndexes.PhysicalIndex.ThresholdIndexes, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Snmp.SensorMib.PhysicalIndexes.PhysicalIndex.ThresholdIndexes, self).__setattr__(name, value)


                    class ThresholdIndex(Entity):
                        """
                        Threshold value for threshold index
                        
                        .. attribute:: phy_index
                        
                        	Physical Index
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: thre_index
                        
                        	Threshold index
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: threshold_evaluation
                        
                        	Indicates the result of the most recent evaluation of the thresholD
                        	**type**\:  bool
                        
                        .. attribute:: threshold_notification_enabled
                        
                        	Indicates whether or not a notification should result, in case of threshold violation
                        	**type**\:  bool
                        
                        .. attribute:: threshold_relation
                        
                        	Indicates relation between sensor value and threshold
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: threshold_severity
                        
                        	Indicates minor, major, critical severities
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: threshold_value
                        
                        	Value of the configured threshold
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'snmp-sensormib-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Snmp.SensorMib.PhysicalIndexes.PhysicalIndex.ThresholdIndexes.ThresholdIndex, self).__init__()

                            self.yang_name = "threshold-index"
                            self.yang_parent_name = "threshold-indexes"

                            self.phy_index = YLeaf(YType.str, "phy-index")

                            self.thre_index = YLeaf(YType.str, "thre-index")

                            self.threshold_evaluation = YLeaf(YType.boolean, "threshold-evaluation")

                            self.threshold_notification_enabled = YLeaf(YType.boolean, "threshold-notification-enabled")

                            self.threshold_relation = YLeaf(YType.uint32, "threshold-relation")

                            self.threshold_severity = YLeaf(YType.uint32, "threshold-severity")

                            self.threshold_value = YLeaf(YType.uint32, "threshold-value")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("phy_index",
                                            "thre_index",
                                            "threshold_evaluation",
                                            "threshold_notification_enabled",
                                            "threshold_relation",
                                            "threshold_severity",
                                            "threshold_value") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Snmp.SensorMib.PhysicalIndexes.PhysicalIndex.ThresholdIndexes.ThresholdIndex, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Snmp.SensorMib.PhysicalIndexes.PhysicalIndex.ThresholdIndexes.ThresholdIndex, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.phy_index.is_set or
                                self.thre_index.is_set or
                                self.threshold_evaluation.is_set or
                                self.threshold_notification_enabled.is_set or
                                self.threshold_relation.is_set or
                                self.threshold_severity.is_set or
                                self.threshold_value.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.phy_index.yfilter != YFilter.not_set or
                                self.thre_index.yfilter != YFilter.not_set or
                                self.threshold_evaluation.yfilter != YFilter.not_set or
                                self.threshold_notification_enabled.yfilter != YFilter.not_set or
                                self.threshold_relation.yfilter != YFilter.not_set or
                                self.threshold_severity.yfilter != YFilter.not_set or
                                self.threshold_value.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "threshold-index" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.phy_index.is_set or self.phy_index.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.phy_index.get_name_leafdata())
                            if (self.thre_index.is_set or self.thre_index.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.thre_index.get_name_leafdata())
                            if (self.threshold_evaluation.is_set or self.threshold_evaluation.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.threshold_evaluation.get_name_leafdata())
                            if (self.threshold_notification_enabled.is_set or self.threshold_notification_enabled.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.threshold_notification_enabled.get_name_leafdata())
                            if (self.threshold_relation.is_set or self.threshold_relation.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.threshold_relation.get_name_leafdata())
                            if (self.threshold_severity.is_set or self.threshold_severity.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.threshold_severity.get_name_leafdata())
                            if (self.threshold_value.is_set or self.threshold_value.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.threshold_value.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "phy-index" or name == "thre-index" or name == "threshold-evaluation" or name == "threshold-notification-enabled" or name == "threshold-relation" or name == "threshold-severity" or name == "threshold-value"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "phy-index"):
                                self.phy_index = value
                                self.phy_index.value_namespace = name_space
                                self.phy_index.value_namespace_prefix = name_space_prefix
                            if(value_path == "thre-index"):
                                self.thre_index = value
                                self.thre_index.value_namespace = name_space
                                self.thre_index.value_namespace_prefix = name_space_prefix
                            if(value_path == "threshold-evaluation"):
                                self.threshold_evaluation = value
                                self.threshold_evaluation.value_namespace = name_space
                                self.threshold_evaluation.value_namespace_prefix = name_space_prefix
                            if(value_path == "threshold-notification-enabled"):
                                self.threshold_notification_enabled = value
                                self.threshold_notification_enabled.value_namespace = name_space
                                self.threshold_notification_enabled.value_namespace_prefix = name_space_prefix
                            if(value_path == "threshold-relation"):
                                self.threshold_relation = value
                                self.threshold_relation.value_namespace = name_space
                                self.threshold_relation.value_namespace_prefix = name_space_prefix
                            if(value_path == "threshold-severity"):
                                self.threshold_severity = value
                                self.threshold_severity.value_namespace = name_space
                                self.threshold_severity.value_namespace_prefix = name_space_prefix
                            if(value_path == "threshold-value"):
                                self.threshold_value = value
                                self.threshold_value.value_namespace = name_space
                                self.threshold_value.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.threshold_index:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.threshold_index:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "threshold-indexes" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "threshold-index"):
                            for c in self.threshold_index:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Snmp.SensorMib.PhysicalIndexes.PhysicalIndex.ThresholdIndexes.ThresholdIndex()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.threshold_index.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "threshold-index"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.index.is_set or
                        (self.threshold_indexes is not None and self.threshold_indexes.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.index.yfilter != YFilter.not_set or
                        (self.threshold_indexes is not None and self.threshold_indexes.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "physical-index" + "[index='" + self.index.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-sensormib-oper:sensor-mib/physical-indexes/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.index.is_set or self.index.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.index.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "threshold-indexes"):
                        if (self.threshold_indexes is None):
                            self.threshold_indexes = Snmp.SensorMib.PhysicalIndexes.PhysicalIndex.ThresholdIndexes()
                            self.threshold_indexes.parent = self
                            self._children_name_map["threshold_indexes"] = "threshold-indexes"
                        return self.threshold_indexes

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "threshold-indexes" or name == "index"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "index"):
                        self.index = value
                        self.index.value_namespace = name_space
                        self.index.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.physical_index:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.physical_index:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "physical-indexes" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-sensormib-oper:sensor-mib/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "physical-index"):
                    for c in self.physical_index:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Snmp.SensorMib.PhysicalIndexes.PhysicalIndex()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.physical_index.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "physical-index"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class EntPhyIndexes(Entity):
            """
            List of physical index 
            
            .. attribute:: ent_phy_index
            
            	Sensor value for physical index
            	**type**\: list of    :py:class:`EntPhyIndex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.SensorMib.EntPhyIndexes.EntPhyIndex>`
            
            

            """

            _prefix = 'snmp-sensormib-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Snmp.SensorMib.EntPhyIndexes, self).__init__()

                self.yang_name = "ent-phy-indexes"
                self.yang_parent_name = "sensor-mib"

                self.ent_phy_index = YList(self)

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
                            super(Snmp.SensorMib.EntPhyIndexes, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Snmp.SensorMib.EntPhyIndexes, self).__setattr__(name, value)


            class EntPhyIndex(Entity):
                """
                Sensor value for physical index
                
                .. attribute:: index  <key>
                
                	Physical index
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: age_time_stamp
                
                	Age of the sensor value; set to the current time if directly access the value from sensor
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: alarm_type
                
                	Indicates threshold violation
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: data_type
                
                	Sensor data type enums
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: device_description
                
                	Device Name
                	**type**\:  str
                
                	**length:** 0..64
                
                .. attribute:: device_id
                
                	Identifier for this device
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: field_validity_bitmap
                
                	Sensor valid bitmap
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: measured_entity
                
                	physical entity for which the sensor is taking measurements
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: precision
                
                	Sensor precision range
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: scale
                
                	Sensor scale enums
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: status
                
                	Sensor operation state enums
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: units
                
                	Units of variable being read
                	**type**\:  str
                
                	**length:** 0..64
                
                .. attribute:: update_rate
                
                	Sensor value update rate;set to 0 if sensor value is updated and evaluated immediately
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: value
                
                	Current reading of sensor
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'snmp-sensormib-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Snmp.SensorMib.EntPhyIndexes.EntPhyIndex, self).__init__()

                    self.yang_name = "ent-phy-index"
                    self.yang_parent_name = "ent-phy-indexes"

                    self.index = YLeaf(YType.str, "index")

                    self.age_time_stamp = YLeaf(YType.uint32, "age-time-stamp")

                    self.alarm_type = YLeaf(YType.uint32, "alarm-type")

                    self.data_type = YLeaf(YType.uint32, "data-type")

                    self.device_description = YLeaf(YType.str, "device-description")

                    self.device_id = YLeaf(YType.uint32, "device-id")

                    self.field_validity_bitmap = YLeaf(YType.uint32, "field-validity-bitmap")

                    self.measured_entity = YLeaf(YType.uint32, "measured-entity")

                    self.precision = YLeaf(YType.uint32, "precision")

                    self.scale = YLeaf(YType.uint32, "scale")

                    self.status = YLeaf(YType.uint32, "status")

                    self.units = YLeaf(YType.str, "units")

                    self.update_rate = YLeaf(YType.uint32, "update-rate")

                    self.value = YLeaf(YType.uint32, "value")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("index",
                                    "age_time_stamp",
                                    "alarm_type",
                                    "data_type",
                                    "device_description",
                                    "device_id",
                                    "field_validity_bitmap",
                                    "measured_entity",
                                    "precision",
                                    "scale",
                                    "status",
                                    "units",
                                    "update_rate",
                                    "value") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Snmp.SensorMib.EntPhyIndexes.EntPhyIndex, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Snmp.SensorMib.EntPhyIndexes.EntPhyIndex, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.index.is_set or
                        self.age_time_stamp.is_set or
                        self.alarm_type.is_set or
                        self.data_type.is_set or
                        self.device_description.is_set or
                        self.device_id.is_set or
                        self.field_validity_bitmap.is_set or
                        self.measured_entity.is_set or
                        self.precision.is_set or
                        self.scale.is_set or
                        self.status.is_set or
                        self.units.is_set or
                        self.update_rate.is_set or
                        self.value.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.index.yfilter != YFilter.not_set or
                        self.age_time_stamp.yfilter != YFilter.not_set or
                        self.alarm_type.yfilter != YFilter.not_set or
                        self.data_type.yfilter != YFilter.not_set or
                        self.device_description.yfilter != YFilter.not_set or
                        self.device_id.yfilter != YFilter.not_set or
                        self.field_validity_bitmap.yfilter != YFilter.not_set or
                        self.measured_entity.yfilter != YFilter.not_set or
                        self.precision.yfilter != YFilter.not_set or
                        self.scale.yfilter != YFilter.not_set or
                        self.status.yfilter != YFilter.not_set or
                        self.units.yfilter != YFilter.not_set or
                        self.update_rate.yfilter != YFilter.not_set or
                        self.value.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ent-phy-index" + "[index='" + self.index.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-sensormib-oper:sensor-mib/ent-phy-indexes/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.index.is_set or self.index.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.index.get_name_leafdata())
                    if (self.age_time_stamp.is_set or self.age_time_stamp.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.age_time_stamp.get_name_leafdata())
                    if (self.alarm_type.is_set or self.alarm_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.alarm_type.get_name_leafdata())
                    if (self.data_type.is_set or self.data_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.data_type.get_name_leafdata())
                    if (self.device_description.is_set or self.device_description.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.device_description.get_name_leafdata())
                    if (self.device_id.is_set or self.device_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.device_id.get_name_leafdata())
                    if (self.field_validity_bitmap.is_set or self.field_validity_bitmap.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.field_validity_bitmap.get_name_leafdata())
                    if (self.measured_entity.is_set or self.measured_entity.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.measured_entity.get_name_leafdata())
                    if (self.precision.is_set or self.precision.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.precision.get_name_leafdata())
                    if (self.scale.is_set or self.scale.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.scale.get_name_leafdata())
                    if (self.status.is_set or self.status.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.status.get_name_leafdata())
                    if (self.units.is_set or self.units.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.units.get_name_leafdata())
                    if (self.update_rate.is_set or self.update_rate.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.update_rate.get_name_leafdata())
                    if (self.value.is_set or self.value.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.value.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "index" or name == "age-time-stamp" or name == "alarm-type" or name == "data-type" or name == "device-description" or name == "device-id" or name == "field-validity-bitmap" or name == "measured-entity" or name == "precision" or name == "scale" or name == "status" or name == "units" or name == "update-rate" or name == "value"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "index"):
                        self.index = value
                        self.index.value_namespace = name_space
                        self.index.value_namespace_prefix = name_space_prefix
                    if(value_path == "age-time-stamp"):
                        self.age_time_stamp = value
                        self.age_time_stamp.value_namespace = name_space
                        self.age_time_stamp.value_namespace_prefix = name_space_prefix
                    if(value_path == "alarm-type"):
                        self.alarm_type = value
                        self.alarm_type.value_namespace = name_space
                        self.alarm_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "data-type"):
                        self.data_type = value
                        self.data_type.value_namespace = name_space
                        self.data_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "device-description"):
                        self.device_description = value
                        self.device_description.value_namespace = name_space
                        self.device_description.value_namespace_prefix = name_space_prefix
                    if(value_path == "device-id"):
                        self.device_id = value
                        self.device_id.value_namespace = name_space
                        self.device_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "field-validity-bitmap"):
                        self.field_validity_bitmap = value
                        self.field_validity_bitmap.value_namespace = name_space
                        self.field_validity_bitmap.value_namespace_prefix = name_space_prefix
                    if(value_path == "measured-entity"):
                        self.measured_entity = value
                        self.measured_entity.value_namespace = name_space
                        self.measured_entity.value_namespace_prefix = name_space_prefix
                    if(value_path == "precision"):
                        self.precision = value
                        self.precision.value_namespace = name_space
                        self.precision.value_namespace_prefix = name_space_prefix
                    if(value_path == "scale"):
                        self.scale = value
                        self.scale.value_namespace = name_space
                        self.scale.value_namespace_prefix = name_space_prefix
                    if(value_path == "status"):
                        self.status = value
                        self.status.value_namespace = name_space
                        self.status.value_namespace_prefix = name_space_prefix
                    if(value_path == "units"):
                        self.units = value
                        self.units.value_namespace = name_space
                        self.units.value_namespace_prefix = name_space_prefix
                    if(value_path == "update-rate"):
                        self.update_rate = value
                        self.update_rate.value_namespace = name_space
                        self.update_rate.value_namespace_prefix = name_space_prefix
                    if(value_path == "value"):
                        self.value = value
                        self.value.value_namespace = name_space
                        self.value.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.ent_phy_index:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.ent_phy_index:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ent-phy-indexes" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-sensormib-oper:sensor-mib/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "ent-phy-index"):
                    for c in self.ent_phy_index:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Snmp.SensorMib.EntPhyIndexes.EntPhyIndex()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.ent_phy_index.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ent-phy-index"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                (self.ent_phy_indexes is not None and self.ent_phy_indexes.has_data()) or
                (self.physical_indexes is not None and self.physical_indexes.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.ent_phy_indexes is not None and self.ent_phy_indexes.has_operation()) or
                (self.physical_indexes is not None and self.physical_indexes.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "Cisco-IOS-XR-snmp-sensormib-oper:sensor-mib" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ent-phy-indexes"):
                if (self.ent_phy_indexes is None):
                    self.ent_phy_indexes = Snmp.SensorMib.EntPhyIndexes()
                    self.ent_phy_indexes.parent = self
                    self._children_name_map["ent_phy_indexes"] = "ent-phy-indexes"
                return self.ent_phy_indexes

            if (child_yang_name == "physical-indexes"):
                if (self.physical_indexes is None):
                    self.physical_indexes = Snmp.SensorMib.PhysicalIndexes()
                    self.physical_indexes.parent = self
                    self._children_name_map["physical_indexes"] = "physical-indexes"
                return self.physical_indexes

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ent-phy-indexes" or name == "physical-indexes"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.correlator is not None and self.correlator.has_data()) or
            (self.entity_mib is not None and self.entity_mib.has_data()) or
            (self.if_indexes is not None and self.if_indexes.has_data()) or
            (self.information is not None and self.information.has_data()) or
            (self.interface_indexes is not None and self.interface_indexes.has_data()) or
            (self.interface_mib is not None and self.interface_mib.has_data()) or
            (self.interfaces is not None and self.interfaces.has_data()) or
            (self.sensor_mib is not None and self.sensor_mib.has_data()) or
            (self.trap_servers is not None and self.trap_servers.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.correlator is not None and self.correlator.has_operation()) or
            (self.entity_mib is not None and self.entity_mib.has_operation()) or
            (self.if_indexes is not None and self.if_indexes.has_operation()) or
            (self.information is not None and self.information.has_operation()) or
            (self.interface_indexes is not None and self.interface_indexes.has_operation()) or
            (self.interface_mib is not None and self.interface_mib.has_operation()) or
            (self.interfaces is not None and self.interfaces.has_operation()) or
            (self.sensor_mib is not None and self.sensor_mib.has_operation()) or
            (self.trap_servers is not None and self.trap_servers.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-snmp-agent-oper:snmp" + path_buffer

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

        if (child_yang_name == "correlator"):
            if (self.correlator is None):
                self.correlator = Snmp.Correlator()
                self.correlator.parent = self
                self._children_name_map["correlator"] = "correlator"
            return self.correlator

        if (child_yang_name == "entity-mib"):
            if (self.entity_mib is None):
                self.entity_mib = Snmp.EntityMib()
                self.entity_mib.parent = self
                self._children_name_map["entity_mib"] = "entity-mib"
            return self.entity_mib

        if (child_yang_name == "if-indexes"):
            if (self.if_indexes is None):
                self.if_indexes = Snmp.IfIndexes()
                self.if_indexes.parent = self
                self._children_name_map["if_indexes"] = "if-indexes"
            return self.if_indexes

        if (child_yang_name == "information"):
            if (self.information is None):
                self.information = Snmp.Information()
                self.information.parent = self
                self._children_name_map["information"] = "information"
            return self.information

        if (child_yang_name == "interface-indexes"):
            if (self.interface_indexes is None):
                self.interface_indexes = Snmp.InterfaceIndexes()
                self.interface_indexes.parent = self
                self._children_name_map["interface_indexes"] = "interface-indexes"
            return self.interface_indexes

        if (child_yang_name == "interface-mib"):
            if (self.interface_mib is None):
                self.interface_mib = Snmp.InterfaceMib()
                self.interface_mib.parent = self
                self._children_name_map["interface_mib"] = "interface-mib"
            return self.interface_mib

        if (child_yang_name == "interfaces"):
            if (self.interfaces is None):
                self.interfaces = Snmp.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
            return self.interfaces

        if (child_yang_name == "sensor-mib"):
            if (self.sensor_mib is None):
                self.sensor_mib = Snmp.SensorMib()
                self.sensor_mib.parent = self
                self._children_name_map["sensor_mib"] = "sensor-mib"
            return self.sensor_mib

        if (child_yang_name == "trap-servers"):
            if (self.trap_servers is None):
                self.trap_servers = Snmp.TrapServers()
                self.trap_servers.parent = self
                self._children_name_map["trap_servers"] = "trap-servers"
            return self.trap_servers

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "correlator" or name == "entity-mib" or name == "if-indexes" or name == "information" or name == "interface-indexes" or name == "interface-mib" or name == "interfaces" or name == "sensor-mib" or name == "trap-servers"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Snmp()
        return self._top_entity


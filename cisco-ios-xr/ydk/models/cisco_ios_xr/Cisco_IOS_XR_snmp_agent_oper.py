""" Cisco_IOS_XR_snmp_agent_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR snmp\-agent package operational data.

This module contains definitions
for the following management objects\:
  snmp\: SNMP operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class DupReqDropStatusEnum(Enum):
    """
    DupReqDropStatusEnum

    Dup req drop status

    .. data:: disabled = 0

    	Disabled

    .. data:: enabled = 1

    	Enabled

    """

    disabled = 0

    enabled = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
        return meta._meta_table['DupReqDropStatusEnum']


class SnmpCorrRuleStateEnum(Enum):
    """
    SnmpCorrRuleStateEnum

    Snmp corr rule state

    .. data:: rule_unapplied = 0

    	Rule is in Unapplied state

    .. data:: rule_applied = 1

    	Rule is Applied to specified hosts

    .. data:: rule_applied_all = 2

    	Rule is Applied to all of router

    """

    rule_unapplied = 0

    rule_applied = 1

    rule_applied_all = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
        return meta._meta_table['SnmpCorrRuleStateEnum']


class SnmpCorrVbindMatchEnum(Enum):
    """
    SnmpCorrVbindMatchEnum

    Snmp corr vbind match

    .. data:: index = 0

    	Match regexp to varbind index

    .. data:: value = 1

    	Match regexp to varbind value

    """

    index = 0

    value = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
        return meta._meta_table['SnmpCorrVbindMatchEnum']



class Snmp(object):
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
        self.correlator = Snmp.Correlator()
        self.correlator.parent = self
        self.entity_mib = Snmp.EntityMib()
        self.entity_mib.parent = self
        self.if_indexes = Snmp.IfIndexes()
        self.if_indexes.parent = self
        self.information = Snmp.Information()
        self.information.parent = self
        self.interface_indexes = Snmp.InterfaceIndexes()
        self.interface_indexes.parent = self
        self.interface_mib = Snmp.InterfaceMib()
        self.interface_mib.parent = self
        self.interfaces = Snmp.Interfaces()
        self.interfaces.parent = self
        self.sensor_mib = Snmp.SensorMib()
        self.sensor_mib.parent = self
        self.trap_servers = Snmp.TrapServers()
        self.trap_servers.parent = self


    class TrapServers(object):
        """
        List of trap hosts
        
        .. attribute:: trap_server
        
        	Trap server and port to which the trap is to be sent and statistics
        	**type**\: list of    :py:class:`TrapServer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.TrapServers.TrapServer>`
        
        

        """

        _prefix = 'snmp-agent-oper'
        _revision = '2016-06-01'

        def __init__(self):
            self.parent = None
            self.trap_server = YList()
            self.trap_server.parent = self
            self.trap_server.name = 'trap_server'


        class TrapServer(object):
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
                self.parent = None
                self.max_q_length_of_trap_q = None
                self.number_of_pkts_dropped = None
                self.number_of_pkts_in_trap_q = None
                self.number_of_pkts_sent = None
                self.port = None
                self.trap_host = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:trap-servers/Cisco-IOS-XR-snmp-agent-oper:trap-server'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.max_q_length_of_trap_q is not None:
                    return True

                if self.number_of_pkts_dropped is not None:
                    return True

                if self.number_of_pkts_in_trap_q is not None:
                    return True

                if self.number_of_pkts_sent is not None:
                    return True

                if self.port is not None:
                    return True

                if self.trap_host is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.TrapServers.TrapServer']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:trap-servers'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.trap_server is not None:
                for child_ref in self.trap_server:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
            return meta._meta_table['Snmp.TrapServers']['meta_info']


    class Information(object):
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
            self.parent = None
            self.bulk_stats_transfers = Snmp.Information.BulkStatsTransfers()
            self.bulk_stats_transfers.parent = self
            self.context_mapping = Snmp.Information.ContextMapping()
            self.context_mapping.parent = self
            self.drop_nms_addresses = Snmp.Information.DropNmsAddresses()
            self.drop_nms_addresses.parent = self
            self.duplicate_drop = Snmp.Information.DuplicateDrop()
            self.duplicate_drop.parent = self
            self.engine_id = Snmp.Information.EngineId()
            self.engine_id.parent = self
            self.hosts = Snmp.Information.Hosts()
            self.hosts.parent = self
            self.incoming_queue = Snmp.Information.IncomingQueue()
            self.incoming_queue.parent = self
            self.infom_details = Snmp.Information.InfomDetails()
            self.infom_details.parent = self
            self.mibs = Snmp.Information.Mibs()
            self.mibs.parent = self
            self.nm_spackets = Snmp.Information.NmSpackets()
            self.nm_spackets.parent = self
            self.nms_addresses = Snmp.Information.NmsAddresses()
            self.nms_addresses.parent = self
            self.poll_oids = Snmp.Information.PollOids()
            self.poll_oids.parent = self
            self.request_type_detail = Snmp.Information.RequestTypeDetail()
            self.request_type_detail.parent = self
            self.rx_queue = Snmp.Information.RxQueue()
            self.rx_queue.parent = self
            self.serial_numbers = Snmp.Information.SerialNumbers()
            self.serial_numbers.parent = self
            self.statistics = Snmp.Information.Statistics()
            self.statistics.parent = self
            self.system_descr = Snmp.Information.SystemDescr()
            self.system_descr.parent = self
            self.system_name = Snmp.Information.SystemName()
            self.system_name.parent = self
            self.system_oid = Snmp.Information.SystemOid()
            self.system_oid.parent = self
            self.system_up_time = Snmp.Information.SystemUpTime()
            self.system_up_time.parent = self
            self.tables = Snmp.Information.Tables()
            self.tables.parent = self
            self.trap_infos = Snmp.Information.TrapInfos()
            self.trap_infos.parent = self
            self.trap_oids = Snmp.Information.TrapOids()
            self.trap_oids.parent = self
            self.trap_queue = Snmp.Information.TrapQueue()
            self.trap_queue.parent = self
            self.views = Snmp.Information.Views()
            self.views.parent = self


        class Hosts(object):
            """
            SNMP host information
            
            .. attribute:: host
            
            	SNMP target host name
            	**type**\: list of    :py:class:`Host <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Hosts.Host>`
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                self.parent = None
                self.host = YList()
                self.host.parent = self
                self.host.name = 'host'


            class Host(object):
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
                    self.parent = None
                    self.name = None
                    self.host_information = YList()
                    self.host_information.parent = self
                    self.host_information.name = 'host_information'


                class HostInformation(object):
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
                        self.parent = None
                        self.user = None
                        self.snmp_target_address_port = None
                        self.snmp_target_address_t_host = None
                        self.snmp_target_addresstype = None
                        self.snmp_target_params_security_level = None
                        self.snmp_target_params_security_model = None
                        self.snmp_target_params_security_name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.user is None:
                            raise YPYModelError('Key property user is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-oper:host-information[Cisco-IOS-XR-snmp-agent-oper:user = ' + str(self.user) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.user is not None:
                            return True

                        if self.snmp_target_address_port is not None:
                            return True

                        if self.snmp_target_address_t_host is not None:
                            return True

                        if self.snmp_target_addresstype is not None:
                            return True

                        if self.snmp_target_params_security_level is not None:
                            return True

                        if self.snmp_target_params_security_model is not None:
                            return True

                        if self.snmp_target_params_security_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                        return meta._meta_table['Snmp.Information.Hosts.Host.HostInformation']['meta_info']

                @property
                def _common_path(self):
                    if self.name is None:
                        raise YPYModelError('Key property name is None')

                    return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:hosts/Cisco-IOS-XR-snmp-agent-oper:host[Cisco-IOS-XR-snmp-agent-oper:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.name is not None:
                        return True

                    if self.host_information is not None:
                        for child_ref in self.host_information:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.Information.Hosts.Host']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:hosts'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.host is not None:
                    for child_ref in self.host:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.Hosts']['meta_info']


        class SystemUpTime(object):
            """
            System up time
            
            .. attribute:: system_up_time_edm
            
            	sysUpTime  1.3.6.1.2.1.1.3
            	**type**\:  str
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                self.parent = None
                self.system_up_time_edm = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:system-up-time'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.system_up_time_edm is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.SystemUpTime']['meta_info']


        class NmsAddresses(object):
            """
            SNMP request type summary 
            
            .. attribute:: nms_address
            
            	NMS address
            	**type**\: list of    :py:class:`NmsAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.NmsAddresses.NmsAddress>`
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                self.parent = None
                self.nms_address = YList()
                self.nms_address.parent = self
                self.nms_address.name = 'nms_address'


            class NmsAddress(object):
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
                    self.parent = None
                    self.nms_addr = None
                    self.get_request_count = None
                    self.getbulk_request_count = None
                    self.getnext_request_count = None
                    self.nms_address = None
                    self.set_request_count = None
                    self.test_request_count = None

                @property
                def _common_path(self):
                    if self.nms_addr is None:
                        raise YPYModelError('Key property nms_addr is None')

                    return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:nms-addresses/Cisco-IOS-XR-snmp-agent-oper:nms-address[Cisco-IOS-XR-snmp-agent-oper:nms-addr = ' + str(self.nms_addr) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.nms_addr is not None:
                        return True

                    if self.get_request_count is not None:
                        return True

                    if self.getbulk_request_count is not None:
                        return True

                    if self.getnext_request_count is not None:
                        return True

                    if self.nms_address is not None:
                        return True

                    if self.set_request_count is not None:
                        return True

                    if self.test_request_count is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.Information.NmsAddresses.NmsAddress']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:nms-addresses'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.nms_address is not None:
                    for child_ref in self.nms_address:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.NmsAddresses']['meta_info']


        class EngineId(object):
            """
            SNMP engine ID
            
            .. attribute:: engine_id
            
            	SNMPv3 engineID
            	**type**\:  str
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                self.parent = None
                self.engine_id = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:engine-id'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.engine_id is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.EngineId']['meta_info']


        class RxQueue(object):
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
                self.parent = None
                self.in_avg = None
                self.in_max = None
                self.in_min = None
                self.incoming_q = None
                self.pend_avg = None
                self.pend_max = None
                self.pend_min = None
                self.pending_q = None
                self.qlen = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:rx-queue'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.in_avg is not None:
                    return True

                if self.in_max is not None:
                    return True

                if self.in_min is not None:
                    return True

                if self.incoming_q is not None:
                    return True

                if self.pend_avg is not None:
                    return True

                if self.pend_max is not None:
                    return True

                if self.pend_min is not None:
                    return True

                if self.pending_q is not None:
                    return True

                if self.qlen is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.RxQueue']['meta_info']


        class SystemName(object):
            """
            System name
            
            .. attribute:: system_name
            
            	sysName  1.3.6.1.2.1.1.5
            	**type**\:  str
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                self.parent = None
                self.system_name = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:system-name'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.system_name is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.SystemName']['meta_info']


        class RequestTypeDetail(object):
            """
            SNMP request type details 
            
            .. attribute:: nms_addresses
            
            	snmp request type details 
            	**type**\:   :py:class:`NmsAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.RequestTypeDetail.NmsAddresses>`
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                self.parent = None
                self.nms_addresses = Snmp.Information.RequestTypeDetail.NmsAddresses()
                self.nms_addresses.parent = self


            class NmsAddresses(object):
                """
                snmp request type details 
                
                .. attribute:: nms_address
                
                	NMS address
                	**type**\: list of    :py:class:`NmsAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.RequestTypeDetail.NmsAddresses.NmsAddress>`
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2016-06-01'

                def __init__(self):
                    self.parent = None
                    self.nms_address = YList()
                    self.nms_address.parent = self
                    self.nms_address.name = 'nms_address'


                class NmsAddress(object):
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
                        self.parent = None
                        self.nms_addr = None
                        self.agent_request_count = None
                        self.entity_request_count = None
                        self.infra_request_count = None
                        self.interface_request_count = None
                        self.route_request_count = None
                        self.total_count = None

                    @property
                    def _common_path(self):
                        if self.nms_addr is None:
                            raise YPYModelError('Key property nms_addr is None')

                        return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:request-type-detail/Cisco-IOS-XR-snmp-agent-oper:nms-addresses/Cisco-IOS-XR-snmp-agent-oper:nms-address[Cisco-IOS-XR-snmp-agent-oper:nms-addr = ' + str(self.nms_addr) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.nms_addr is not None:
                            return True

                        if self.agent_request_count is not None:
                            return True

                        if self.entity_request_count is not None:
                            return True

                        if self.infra_request_count is not None:
                            return True

                        if self.interface_request_count is not None:
                            return True

                        if self.route_request_count is not None:
                            return True

                        if self.total_count is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                        return meta._meta_table['Snmp.Information.RequestTypeDetail.NmsAddresses.NmsAddress']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:request-type-detail/Cisco-IOS-XR-snmp-agent-oper:nms-addresses'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.nms_address is not None:
                        for child_ref in self.nms_address:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.Information.RequestTypeDetail.NmsAddresses']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:request-type-detail'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.nms_addresses is not None and self.nms_addresses._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.RequestTypeDetail']['meta_info']


        class DuplicateDrop(object):
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
            	**type**\:   :py:class:`DupReqDropStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.DupReqDropStatusEnum>`
            
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
                self.parent = None
                self.duplicate_drop_configured_timeout = None
                self.duplicate_drop_disable_count = None
                self.duplicate_drop_enable_count = None
                self.duplicate_dropped_requests = None
                self.duplicate_request_latest_enable_time = None
                self.duplicate_request_status = None
                self.first_enable_time = None
                self.last_status_change_time = None
                self.latest_duplicate_dropped_requests = None
                self.latest_retry_processed_requests = None
                self.retry_processed_requests = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:duplicate-drop'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.duplicate_drop_configured_timeout is not None:
                    return True

                if self.duplicate_drop_disable_count is not None:
                    return True

                if self.duplicate_drop_enable_count is not None:
                    return True

                if self.duplicate_dropped_requests is not None:
                    return True

                if self.duplicate_request_latest_enable_time is not None:
                    return True

                if self.duplicate_request_status is not None:
                    return True

                if self.first_enable_time is not None:
                    return True

                if self.last_status_change_time is not None:
                    return True

                if self.latest_duplicate_dropped_requests is not None:
                    return True

                if self.latest_retry_processed_requests is not None:
                    return True

                if self.retry_processed_requests is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.DuplicateDrop']['meta_info']


        class BulkStatsTransfers(object):
            """
            List of bulkstats transfer on the system
            
            .. attribute:: bulk_stats_transfer
            
            	SNMP bulkstats transfer name
            	**type**\: list of    :py:class:`BulkStatsTransfer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.BulkStatsTransfers.BulkStatsTransfer>`
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                self.parent = None
                self.bulk_stats_transfer = YList()
                self.bulk_stats_transfer.parent = self
                self.bulk_stats_transfer.name = 'bulk_stats_transfer'


            class BulkStatsTransfer(object):
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
                    self.parent = None
                    self.transfer_name = None
                    self.retained_file = None
                    self.retry_left = None
                    self.time_left = None
                    self.transfer_name_xr = None
                    self.url_primary = None
                    self.url_secondary = None

                @property
                def _common_path(self):
                    if self.transfer_name is None:
                        raise YPYModelError('Key property transfer_name is None')

                    return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:bulk-stats-transfers/Cisco-IOS-XR-snmp-agent-oper:bulk-stats-transfer[Cisco-IOS-XR-snmp-agent-oper:transfer-name = ' + str(self.transfer_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.transfer_name is not None:
                        return True

                    if self.retained_file is not None:
                        return True

                    if self.retry_left is not None:
                        return True

                    if self.time_left is not None:
                        return True

                    if self.transfer_name_xr is not None:
                        return True

                    if self.url_primary is not None:
                        return True

                    if self.url_secondary is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.Information.BulkStatsTransfers.BulkStatsTransfer']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:bulk-stats-transfers'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.bulk_stats_transfer is not None:
                    for child_ref in self.bulk_stats_transfer:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.BulkStatsTransfers']['meta_info']


        class TrapInfos(object):
            """
            SNMP trap OID
            
            .. attribute:: trap_info
            
            	SNMP Trap infomation like server , port and trapOID
            	**type**\: list of    :py:class:`TrapInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.TrapInfos.TrapInfo>`
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                self.parent = None
                self.trap_info = YList()
                self.trap_info.parent = self
                self.trap_info.name = 'trap_info'


            class TrapInfo(object):
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
                    self.parent = None
                    self.host = None
                    self.port = None
                    self.port_xr = None
                    self.trap_host = None
                    self.trap_oi_dinfo = YList()
                    self.trap_oi_dinfo.parent = self
                    self.trap_oi_dinfo.name = 'trap_oi_dinfo'
                    self.trap_oid_count = None


                class TrapOiDinfo(object):
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
                        self.parent = None
                        self.count = None
                        self.drop_count = None
                        self.lasrdrop_time = None
                        self.lastsent_time = None
                        self.retry_count = None
                        self.trap_oid = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:trap-infos/Cisco-IOS-XR-snmp-agent-oper:trap-info/Cisco-IOS-XR-snmp-agent-oper:trap-oi-dinfo'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.count is not None:
                            return True

                        if self.drop_count is not None:
                            return True

                        if self.lasrdrop_time is not None:
                            return True

                        if self.lastsent_time is not None:
                            return True

                        if self.retry_count is not None:
                            return True

                        if self.trap_oid is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                        return meta._meta_table['Snmp.Information.TrapInfos.TrapInfo.TrapOiDinfo']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:trap-infos/Cisco-IOS-XR-snmp-agent-oper:trap-info'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.host is not None:
                        return True

                    if self.port is not None:
                        return True

                    if self.port_xr is not None:
                        return True

                    if self.trap_host is not None:
                        return True

                    if self.trap_oi_dinfo is not None:
                        for child_ref in self.trap_oi_dinfo:
                            if child_ref._has_data():
                                return True

                    if self.trap_oid_count is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.Information.TrapInfos.TrapInfo']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:trap-infos'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.trap_info is not None:
                    for child_ref in self.trap_info:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.TrapInfos']['meta_info']


        class PollOids(object):
            """
            OID list for poll PDU
            
            .. attribute:: poll_oid
            
            	PDU drop info for OID
            	**type**\: list of    :py:class:`PollOid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.PollOids.PollOid>`
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                self.parent = None
                self.poll_oid = YList()
                self.poll_oid.parent = self
                self.poll_oid.name = 'poll_oid'


            class PollOid(object):
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
                    self.parent = None
                    self.object_id = None
                    self.nms = YLeafList()
                    self.nms.parent = self
                    self.nms.name = 'nms'
                    self.nms_count = None
                    self.request_count = YLeafList()
                    self.request_count.parent = self
                    self.request_count.name = 'request_count'

                @property
                def _common_path(self):
                    if self.object_id is None:
                        raise YPYModelError('Key property object_id is None')

                    return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:poll-oids/Cisco-IOS-XR-snmp-agent-oper:poll-oid[Cisco-IOS-XR-snmp-agent-oper:object-id = ' + str(self.object_id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object_id is not None:
                        return True

                    if self.nms is not None:
                        for child in self.nms:
                            if child is not None:
                                return True

                    if self.nms_count is not None:
                        return True

                    if self.request_count is not None:
                        for child in self.request_count:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.Information.PollOids.PollOid']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:poll-oids'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.poll_oid is not None:
                    for child_ref in self.poll_oid:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.PollOids']['meta_info']


        class InfomDetails(object):
            """
            SNMP trap OID
            
            .. attribute:: infom_detail
            
            	SNMP Trap infomation like server , port and trapOID
            	**type**\: list of    :py:class:`InfomDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.InfomDetails.InfomDetail>`
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                self.parent = None
                self.infom_detail = YList()
                self.infom_detail.parent = self
                self.infom_detail.name = 'infom_detail'


            class InfomDetail(object):
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
                    self.parent = None
                    self.host = None
                    self.port = None
                    self.port_xr = None
                    self.trap_host = None
                    self.trap_oi_dinfo = YList()
                    self.trap_oi_dinfo.parent = self
                    self.trap_oi_dinfo.name = 'trap_oi_dinfo'
                    self.trap_oid_count = None


                class TrapOiDinfo(object):
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
                        self.parent = None
                        self.count = None
                        self.drop_count = None
                        self.lasrdrop_time = None
                        self.lastsent_time = None
                        self.retry_count = None
                        self.trap_oid = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:infom-details/Cisco-IOS-XR-snmp-agent-oper:infom-detail/Cisco-IOS-XR-snmp-agent-oper:trap-oi-dinfo'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.count is not None:
                            return True

                        if self.drop_count is not None:
                            return True

                        if self.lasrdrop_time is not None:
                            return True

                        if self.lastsent_time is not None:
                            return True

                        if self.retry_count is not None:
                            return True

                        if self.trap_oid is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                        return meta._meta_table['Snmp.Information.InfomDetails.InfomDetail.TrapOiDinfo']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:infom-details/Cisco-IOS-XR-snmp-agent-oper:infom-detail'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.host is not None:
                        return True

                    if self.port is not None:
                        return True

                    if self.port_xr is not None:
                        return True

                    if self.trap_host is not None:
                        return True

                    if self.trap_oi_dinfo is not None:
                        for child_ref in self.trap_oi_dinfo:
                            if child_ref._has_data():
                                return True

                    if self.trap_oid_count is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.Information.InfomDetails.InfomDetail']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:infom-details'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.infom_detail is not None:
                    for child_ref in self.infom_detail:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.InfomDetails']['meta_info']


        class Statistics(object):
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
                self.parent = None
                self.asn_parse_errors_received = None
                self.bad_community_names_received = None
                self.bad_community_uses_received = None
                self.bad_values_received = None
                self.bad_values_sent = None
                self.bad_versions_received = None
                self.general_errors_sent = None
                self.get_next_request_sent = None
                self.get_next_requests_received = None
                self.get_requests_received = None
                self.get_requests_sent = None
                self.get_responses_received = None
                self.get_responses_sent = None
                self.max_packet_size = None
                self.no_such_names_received = None
                self.no_such_names_sent = None
                self.packets_received = None
                self.proxy_drop_count = None
                self.read_only_received = None
                self.set_requests_received = None
                self.set_requests_sent = None
                self.silent_drop_count = None
                self.too_big_packet_received = None
                self.too_big_packets_sent = None
                self.total_general_errors = None
                self.total_packets_sent = None
                self.total_requested_variables = None
                self.total_set_variables_received = None
                self.traps_received = None
                self.traps_sent = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:statistics'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.asn_parse_errors_received is not None:
                    return True

                if self.bad_community_names_received is not None:
                    return True

                if self.bad_community_uses_received is not None:
                    return True

                if self.bad_values_received is not None:
                    return True

                if self.bad_values_sent is not None:
                    return True

                if self.bad_versions_received is not None:
                    return True

                if self.general_errors_sent is not None:
                    return True

                if self.get_next_request_sent is not None:
                    return True

                if self.get_next_requests_received is not None:
                    return True

                if self.get_requests_received is not None:
                    return True

                if self.get_requests_sent is not None:
                    return True

                if self.get_responses_received is not None:
                    return True

                if self.get_responses_sent is not None:
                    return True

                if self.max_packet_size is not None:
                    return True

                if self.no_such_names_received is not None:
                    return True

                if self.no_such_names_sent is not None:
                    return True

                if self.packets_received is not None:
                    return True

                if self.proxy_drop_count is not None:
                    return True

                if self.read_only_received is not None:
                    return True

                if self.set_requests_received is not None:
                    return True

                if self.set_requests_sent is not None:
                    return True

                if self.silent_drop_count is not None:
                    return True

                if self.too_big_packet_received is not None:
                    return True

                if self.too_big_packets_sent is not None:
                    return True

                if self.total_general_errors is not None:
                    return True

                if self.total_packets_sent is not None:
                    return True

                if self.total_requested_variables is not None:
                    return True

                if self.total_set_variables_received is not None:
                    return True

                if self.traps_received is not None:
                    return True

                if self.traps_sent is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.Statistics']['meta_info']


        class IncomingQueue(object):
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
                self.parent = None
                self.inq_entry = YList()
                self.inq_entry.parent = self
                self.inq_entry.name = 'inq_entry'
                self.queue_count = None


            class InqEntry(object):
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
                    self.parent = None
                    self.address_of_queue = None
                    self.last_access_time = None
                    self.priority = None
                    self.processed_request_count = None
                    self.request_count = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:incoming-queue/Cisco-IOS-XR-snmp-agent-oper:inq-entry'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.address_of_queue is not None:
                        return True

                    if self.last_access_time is not None:
                        return True

                    if self.priority is not None:
                        return True

                    if self.processed_request_count is not None:
                        return True

                    if self.request_count is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.Information.IncomingQueue.InqEntry']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:incoming-queue'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.inq_entry is not None:
                    for child_ref in self.inq_entry:
                        if child_ref._has_data():
                            return True

                if self.queue_count is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.IncomingQueue']['meta_info']


        class ContextMapping(object):
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
                self.parent = None
                self.contex_mapping = YList()
                self.contex_mapping.parent = self
                self.contex_mapping.name = 'contex_mapping'


            class ContexMapping(object):
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
                    self.parent = None
                    self.context = None
                    self.feature = None
                    self.feature_name = None
                    self.instance = None
                    self.topology = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:context-mapping/Cisco-IOS-XR-snmp-agent-oper:contex-mapping'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.context is not None:
                        return True

                    if self.feature is not None:
                        return True

                    if self.feature_name is not None:
                        return True

                    if self.instance is not None:
                        return True

                    if self.topology is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.Information.ContextMapping.ContexMapping']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:context-mapping'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.contex_mapping is not None:
                    for child_ref in self.contex_mapping:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.ContextMapping']['meta_info']


        class TrapOids(object):
            """
            SNMP trap OID
            
            .. attribute:: trap_oid
            
            	SNMP trap 
            	**type**\: list of    :py:class:`TrapOid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.TrapOids.TrapOid>`
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                self.parent = None
                self.trap_oid = YList()
                self.trap_oid.parent = self
                self.trap_oid.name = 'trap_oid'


            class TrapOid(object):
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
                    self.parent = None
                    self.trap_oid = None
                    self.trap_oid_count = None
                    self.trap_oid_xr = None

                @property
                def _common_path(self):
                    if self.trap_oid is None:
                        raise YPYModelError('Key property trap_oid is None')

                    return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:trap-oids/Cisco-IOS-XR-snmp-agent-oper:trap-oid[Cisco-IOS-XR-snmp-agent-oper:trap-oid = ' + str(self.trap_oid) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.trap_oid is not None:
                        return True

                    if self.trap_oid_count is not None:
                        return True

                    if self.trap_oid_xr is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.Information.TrapOids.TrapOid']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:trap-oids'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.trap_oid is not None:
                    for child_ref in self.trap_oid:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.TrapOids']['meta_info']


        class NmSpackets(object):
            """
            SNMP overload statistics 
            
            .. attribute:: nm_spacket
            
            	NMS packet drop count
            	**type**\: list of    :py:class:`NmSpacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.NmSpackets.NmSpacket>`
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                self.parent = None
                self.nm_spacket = YList()
                self.nm_spacket.parent = self
                self.nm_spacket.name = 'nm_spacket'


            class NmSpacket(object):
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
                    self.parent = None
                    self.packetcount = None
                    self.number_of_nmsq_pkts_dropped = None
                    self.number_of_pkts_dropped = None
                    self.overload_end_time = None
                    self.overload_start_time = None

                @property
                def _common_path(self):
                    if self.packetcount is None:
                        raise YPYModelError('Key property packetcount is None')

                    return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:nm-spackets/Cisco-IOS-XR-snmp-agent-oper:nm-spacket[Cisco-IOS-XR-snmp-agent-oper:packetcount = ' + str(self.packetcount) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.packetcount is not None:
                        return True

                    if self.number_of_nmsq_pkts_dropped is not None:
                        return True

                    if self.number_of_pkts_dropped is not None:
                        return True

                    if self.overload_end_time is not None:
                        return True

                    if self.overload_start_time is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.Information.NmSpackets.NmSpacket']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:nm-spackets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.nm_spacket is not None:
                    for child_ref in self.nm_spacket:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.NmSpackets']['meta_info']


        class Mibs(object):
            """
            List of MIBS supported on the system
            
            .. attribute:: mib
            
            	SNMP MIB Name
            	**type**\: list of    :py:class:`Mib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Mibs.Mib>`
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                self.parent = None
                self.mib = YList()
                self.mib.parent = self
                self.mib.name = 'mib'


            class Mib(object):
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
                    self.parent = None
                    self.name = None
                    self.mib_information = Snmp.Information.Mibs.Mib.MibInformation()
                    self.mib_information.parent = self
                    self.oids = Snmp.Information.Mibs.Mib.Oids()
                    self.oids.parent = self


                class Oids(object):
                    """
                    List of OIDs per MIB
                    
                    .. attribute:: oid
                    
                    	Object identifiers of a mib
                    	**type**\: list of    :py:class:`Oid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Mibs.Mib.Oids.Oid>`
                    
                    

                    """

                    _prefix = 'snmp-agent-oper'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.oid = YList()
                        self.oid.parent = self
                        self.oid.name = 'oid'


                    class Oid(object):
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
                            self.parent = None
                            self.oid = None
                            self.oid_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.oid is None:
                                raise YPYModelError('Key property oid is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-oper:oid[Cisco-IOS-XR-snmp-agent-oper:oid = ' + str(self.oid) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.oid is not None:
                                return True

                            if self.oid_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                            return meta._meta_table['Snmp.Information.Mibs.Mib.Oids.Oid']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-oper:oids'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.oid is not None:
                            for child_ref in self.oid:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                        return meta._meta_table['Snmp.Information.Mibs.Mib.Oids']['meta_info']


                class MibInformation(object):
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
                        self.parent = None
                        self.dll_capabilities = None
                        self.dll_name = None
                        self.is_mib_loaded = None
                        self.load_time = None
                        self.mib_config_filename = None
                        self.mib_name = None
                        self.timeout = None
                        self.trap_strings = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-oper:mib-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.dll_capabilities is not None:
                            return True

                        if self.dll_name is not None:
                            return True

                        if self.is_mib_loaded is not None:
                            return True

                        if self.load_time is not None:
                            return True

                        if self.mib_config_filename is not None:
                            return True

                        if self.mib_name is not None:
                            return True

                        if self.timeout is not None:
                            return True

                        if self.trap_strings is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                        return meta._meta_table['Snmp.Information.Mibs.Mib.MibInformation']['meta_info']

                @property
                def _common_path(self):
                    if self.name is None:
                        raise YPYModelError('Key property name is None')

                    return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:mibs/Cisco-IOS-XR-snmp-agent-oper:mib[Cisco-IOS-XR-snmp-agent-oper:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.name is not None:
                        return True

                    if self.mib_information is not None and self.mib_information._has_data():
                        return True

                    if self.oids is not None and self.oids._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.Information.Mibs.Mib']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:mibs'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.mib is not None:
                    for child_ref in self.mib:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.Mibs']['meta_info']


        class SerialNumbers(object):
            """
            SNMP statistics pdu 
            
            .. attribute:: serial_number
            
            	Serial number
            	**type**\: list of    :py:class:`SerialNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.SerialNumbers.SerialNumber>`
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                self.parent = None
                self.serial_number = YList()
                self.serial_number.parent = self
                self.serial_number.name = 'serial_number'


            class SerialNumber(object):
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
                    self.parent = None
                    self.error_status = None
                    self.input_q = None
                    self.nms = None
                    self.number = None
                    self.output_q = None
                    self.pdu_type = None
                    self.pending_q = None
                    self.port = None
                    self.port_xr = None
                    self.req_id = None
                    self.request_id = None
                    self.response_out = None
                    self.serial_num = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:serial-numbers/Cisco-IOS-XR-snmp-agent-oper:serial-number'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.error_status is not None:
                        return True

                    if self.input_q is not None:
                        return True

                    if self.nms is not None:
                        return True

                    if self.number is not None:
                        return True

                    if self.output_q is not None:
                        return True

                    if self.pdu_type is not None:
                        return True

                    if self.pending_q is not None:
                        return True

                    if self.port is not None:
                        return True

                    if self.port_xr is not None:
                        return True

                    if self.req_id is not None:
                        return True

                    if self.request_id is not None:
                        return True

                    if self.response_out is not None:
                        return True

                    if self.serial_num is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.Information.SerialNumbers.SerialNumber']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:serial-numbers'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.serial_number is not None:
                    for child_ref in self.serial_number:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.SerialNumbers']['meta_info']


        class DropNmsAddresses(object):
            """
            NMS list for drop PDU
            
            .. attribute:: drop_nms_address
            
            	PDU drop info for NMS
            	**type**\: list of    :py:class:`DropNmsAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.DropNmsAddresses.DropNmsAddress>`
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                self.parent = None
                self.drop_nms_address = YList()
                self.drop_nms_address.parent = self
                self.drop_nms_address.name = 'drop_nms_address'


            class DropNmsAddress(object):
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
                    self.parent = None
                    self.nms_addr = None
                    self.aipc_count = None
                    self.duplicate_count = None
                    self.encode_count = None
                    self.incoming_q_count = None
                    self.internal_count = None
                    self.nms_address = None
                    self.overload_count = None
                    self.stack_count = None
                    self.threshold_incoming_q_count = None
                    self.timeout_count = None

                @property
                def _common_path(self):
                    if self.nms_addr is None:
                        raise YPYModelError('Key property nms_addr is None')

                    return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:drop-nms-addresses/Cisco-IOS-XR-snmp-agent-oper:drop-nms-address[Cisco-IOS-XR-snmp-agent-oper:nms-addr = ' + str(self.nms_addr) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.nms_addr is not None:
                        return True

                    if self.aipc_count is not None:
                        return True

                    if self.duplicate_count is not None:
                        return True

                    if self.encode_count is not None:
                        return True

                    if self.incoming_q_count is not None:
                        return True

                    if self.internal_count is not None:
                        return True

                    if self.nms_address is not None:
                        return True

                    if self.overload_count is not None:
                        return True

                    if self.stack_count is not None:
                        return True

                    if self.threshold_incoming_q_count is not None:
                        return True

                    if self.timeout_count is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.Information.DropNmsAddresses.DropNmsAddress']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:drop-nms-addresses'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.drop_nms_address is not None:
                    for child_ref in self.drop_nms_address:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.DropNmsAddresses']['meta_info']


        class Views(object):
            """
            SNMP view information
            
            .. attribute:: view
            
            	SNMP target view name
            	**type**\: list of    :py:class:`View <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Views.View>`
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                self.parent = None
                self.view = YList()
                self.view.parent = self
                self.view.name = 'view'


            class View(object):
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
                    self.parent = None
                    self.name = None
                    self.view_information = YList()
                    self.view_information.parent = self
                    self.view_information.name = 'view_information'


                class ViewInformation(object):
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
                        self.parent = None
                        self.object_id = None
                        self.snmp_view_family_status = None
                        self.snmp_view_family_storage_type = None
                        self.snmp_view_family_type = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.object_id is None:
                            raise YPYModelError('Key property object_id is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-oper:view-information[Cisco-IOS-XR-snmp-agent-oper:object-id = ' + str(self.object_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.object_id is not None:
                            return True

                        if self.snmp_view_family_status is not None:
                            return True

                        if self.snmp_view_family_storage_type is not None:
                            return True

                        if self.snmp_view_family_type is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                        return meta._meta_table['Snmp.Information.Views.View.ViewInformation']['meta_info']

                @property
                def _common_path(self):
                    if self.name is None:
                        raise YPYModelError('Key property name is None')

                    return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:views/Cisco-IOS-XR-snmp-agent-oper:view[Cisco-IOS-XR-snmp-agent-oper:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.name is not None:
                        return True

                    if self.view_information is not None:
                        for child_ref in self.view_information:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.Information.Views.View']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:views'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.view is not None:
                    for child_ref in self.view:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.Views']['meta_info']


        class SystemDescr(object):
            """
            System description
            
            .. attribute:: sys_descr
            
            	sysDescr  1.3.6.1.2.1.1.1
            	**type**\:  str
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                self.parent = None
                self.sys_descr = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:system-descr'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.sys_descr is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.SystemDescr']['meta_info']


        class Tables(object):
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
                self.parent = None
                self.groups = Snmp.Information.Tables.Groups()
                self.groups.parent = self
                self.user_engine_ids = Snmp.Information.Tables.UserEngineIds()
                self.user_engine_ids.parent = self


            class Groups(object):
                """
                List of vacmAccessTable
                
                .. attribute:: group
                
                	SNMP group name
                	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Tables.Groups.Group>`
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2016-06-01'

                def __init__(self):
                    self.parent = None
                    self.group = YList()
                    self.group.parent = self
                    self.group.name = 'group'


                class Group(object):
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
                        self.parent = None
                        self.name = None
                        self.group_informations = Snmp.Information.Tables.Groups.Group.GroupInformations()
                        self.group_informations.parent = self


                    class GroupInformations(object):
                        """
                        Group Model
                        
                        .. attribute:: group_information
                        
                        	Group name ,status  and information
                        	**type**\: list of    :py:class:`GroupInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Tables.Groups.Group.GroupInformations.GroupInformation>`
                        
                        

                        """

                        _prefix = 'snmp-agent-oper'
                        _revision = '2016-06-01'

                        def __init__(self):
                            self.parent = None
                            self.group_information = YList()
                            self.group_information.parent = self
                            self.group_information.name = 'group_information'


                        class GroupInformation(object):
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
                                self.parent = None
                                self.level = None
                                self.modelnumber = None
                                self.vacm_access_notify_view_name = None
                                self.vacm_access_read_view_name = None
                                self.vacm_access_status = None
                                self.vacm_access_write_view_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-oper:group-information'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.level is not None:
                                    return True

                                if self.modelnumber is not None:
                                    return True

                                if self.vacm_access_notify_view_name is not None:
                                    return True

                                if self.vacm_access_read_view_name is not None:
                                    return True

                                if self.vacm_access_status is not None:
                                    return True

                                if self.vacm_access_write_view_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                                return meta._meta_table['Snmp.Information.Tables.Groups.Group.GroupInformations.GroupInformation']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-oper:group-informations'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.group_information is not None:
                                for child_ref in self.group_information:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                            return meta._meta_table['Snmp.Information.Tables.Groups.Group.GroupInformations']['meta_info']

                    @property
                    def _common_path(self):
                        if self.name is None:
                            raise YPYModelError('Key property name is None')

                        return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:tables/Cisco-IOS-XR-snmp-agent-oper:groups/Cisco-IOS-XR-snmp-agent-oper:group[Cisco-IOS-XR-snmp-agent-oper:name = ' + str(self.name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.name is not None:
                            return True

                        if self.group_informations is not None and self.group_informations._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                        return meta._meta_table['Snmp.Information.Tables.Groups.Group']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:tables/Cisco-IOS-XR-snmp-agent-oper:groups'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.group is not None:
                        for child_ref in self.group:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.Information.Tables.Groups']['meta_info']


            class UserEngineIds(object):
                """
                List of User
                
                .. attribute:: user_engine_id
                
                	SNMP engineId
                	**type**\: list of    :py:class:`UserEngineId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Information.Tables.UserEngineIds.UserEngineId>`
                
                

                """

                _prefix = 'snmp-agent-oper'
                _revision = '2016-06-01'

                def __init__(self):
                    self.parent = None
                    self.user_engine_id = YList()
                    self.user_engine_id.parent = self
                    self.user_engine_id.name = 'user_engine_id'


                class UserEngineId(object):
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
                        self.parent = None
                        self.engine_id = None
                        self.user_name = YList()
                        self.user_name.parent = self
                        self.user_name.name = 'user_name'


                    class UserName(object):
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
                            self.parent = None
                            self.user_name = None
                            self.usm_user_status = None
                            self.usm_user_storage_type = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.user_name is None:
                                raise YPYModelError('Key property user_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-oper:user-name[Cisco-IOS-XR-snmp-agent-oper:user-name = ' + str(self.user_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.user_name is not None:
                                return True

                            if self.usm_user_status is not None:
                                return True

                            if self.usm_user_storage_type is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                            return meta._meta_table['Snmp.Information.Tables.UserEngineIds.UserEngineId.UserName']['meta_info']

                    @property
                    def _common_path(self):
                        if self.engine_id is None:
                            raise YPYModelError('Key property engine_id is None')

                        return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:tables/Cisco-IOS-XR-snmp-agent-oper:user-engine-ids/Cisco-IOS-XR-snmp-agent-oper:user-engine-id[Cisco-IOS-XR-snmp-agent-oper:engine-id = ' + str(self.engine_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.engine_id is not None:
                            return True

                        if self.user_name is not None:
                            for child_ref in self.user_name:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                        return meta._meta_table['Snmp.Information.Tables.UserEngineIds.UserEngineId']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:tables/Cisco-IOS-XR-snmp-agent-oper:user-engine-ids'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.user_engine_id is not None:
                        for child_ref in self.user_engine_id:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.Information.Tables.UserEngineIds']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:tables'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.groups is not None and self.groups._has_data():
                    return True

                if self.user_engine_ids is not None and self.user_engine_ids._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.Tables']['meta_info']


        class SystemOid(object):
            """
            System object ID
            
            .. attribute:: sys_obj_id
            
            	sysObjID  1.3.6.1.2.1.1.2
            	**type**\:  str
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                self.parent = None
                self.sys_obj_id = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:system-oid'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.sys_obj_id is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.SystemOid']['meta_info']


        class TrapQueue(object):
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
                self.parent = None
                self.trap_avg = None
                self.trap_max = None
                self.trap_min = None
                self.trap_q = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information/Cisco-IOS-XR-snmp-agent-oper:trap-queue'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.trap_avg is not None:
                    return True

                if self.trap_max is not None:
                    return True

                if self.trap_min is not None:
                    return True

                if self.trap_q is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Information.TrapQueue']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:information'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.bulk_stats_transfers is not None and self.bulk_stats_transfers._has_data():
                return True

            if self.context_mapping is not None and self.context_mapping._has_data():
                return True

            if self.drop_nms_addresses is not None and self.drop_nms_addresses._has_data():
                return True

            if self.duplicate_drop is not None and self.duplicate_drop._has_data():
                return True

            if self.engine_id is not None and self.engine_id._has_data():
                return True

            if self.hosts is not None and self.hosts._has_data():
                return True

            if self.incoming_queue is not None and self.incoming_queue._has_data():
                return True

            if self.infom_details is not None and self.infom_details._has_data():
                return True

            if self.mibs is not None and self.mibs._has_data():
                return True

            if self.nm_spackets is not None and self.nm_spackets._has_data():
                return True

            if self.nms_addresses is not None and self.nms_addresses._has_data():
                return True

            if self.poll_oids is not None and self.poll_oids._has_data():
                return True

            if self.request_type_detail is not None and self.request_type_detail._has_data():
                return True

            if self.rx_queue is not None and self.rx_queue._has_data():
                return True

            if self.serial_numbers is not None and self.serial_numbers._has_data():
                return True

            if self.statistics is not None and self.statistics._has_data():
                return True

            if self.system_descr is not None and self.system_descr._has_data():
                return True

            if self.system_name is not None and self.system_name._has_data():
                return True

            if self.system_oid is not None and self.system_oid._has_data():
                return True

            if self.system_up_time is not None and self.system_up_time._has_data():
                return True

            if self.tables is not None and self.tables._has_data():
                return True

            if self.trap_infos is not None and self.trap_infos._has_data():
                return True

            if self.trap_oids is not None and self.trap_oids._has_data():
                return True

            if self.trap_queue is not None and self.trap_queue._has_data():
                return True

            if self.views is not None and self.views._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
            return meta._meta_table['Snmp.Information']['meta_info']


    class Interfaces(object):
        """
        List of interfaces
        
        .. attribute:: interface
        
        	Interface Name
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Interfaces.Interface>`
        
        

        """

        _prefix = 'snmp-agent-oper'
        _revision = '2016-06-01'

        def __init__(self):
            self.parent = None
            self.interface = YList()
            self.interface.parent = self
            self.interface.name = 'interface'


        class Interface(object):
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
                self.parent = None
                self.name = None
                self.interface_index = None

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:interfaces/Cisco-IOS-XR-snmp-agent-oper:interface[Cisco-IOS-XR-snmp-agent-oper:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.name is not None:
                    return True

                if self.interface_index is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Interfaces.Interface']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:interfaces'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.interface is not None:
                for child_ref in self.interface:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
            return meta._meta_table['Snmp.Interfaces']['meta_info']


    class Correlator(object):
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
            self.parent = None
            self.buffer_status = Snmp.Correlator.BufferStatus()
            self.buffer_status.parent = self
            self.rule_details = Snmp.Correlator.RuleDetails()
            self.rule_details.parent = self
            self.rule_set_details = Snmp.Correlator.RuleSetDetails()
            self.rule_set_details.parent = self
            self.traps = Snmp.Correlator.Traps()
            self.traps.parent = self


        class RuleDetails(object):
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
                self.parent = None
                self.rule_detail = YList()
                self.rule_detail.parent = self
                self.rule_detail.name = 'rule_detail'


            class RuleDetail(object):
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
                    self.parent = None
                    self.rule_name = None
                    self.apply_host = YList()
                    self.apply_host.parent = self
                    self.apply_host.name = 'apply_host'
                    self.non_rootcaus = YList()
                    self.non_rootcaus.parent = self
                    self.non_rootcaus.name = 'non_rootcaus'
                    self.root_cause = Snmp.Correlator.RuleDetails.RuleDetail.RootCause()
                    self.root_cause.parent = self
                    self.rule_summary = Snmp.Correlator.RuleDetails.RuleDetail.RuleSummary()
                    self.rule_summary.parent = self
                    self.timeout = None


                class RuleSummary(object):
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
                    	**type**\:   :py:class:`SnmpCorrRuleStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.SnmpCorrRuleStateEnum>`
                    
                    

                    """

                    _prefix = 'snmp-agent-oper'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.buffered_traps_count = None
                        self.rule_name = None
                        self.rule_state = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-oper:rule-summary'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.buffered_traps_count is not None:
                            return True

                        if self.rule_name is not None:
                            return True

                        if self.rule_state is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                        return meta._meta_table['Snmp.Correlator.RuleDetails.RuleDetail.RuleSummary']['meta_info']


                class RootCause(object):
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
                        self.parent = None
                        self.oid = None
                        self.var_bind = YList()
                        self.var_bind.parent = self
                        self.var_bind.name = 'var_bind'


                    class VarBind(object):
                        """
                        VarBinds of the trap
                        
                        .. attribute:: match_type
                        
                        	Varbind match type
                        	**type**\:   :py:class:`SnmpCorrVbindMatchEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.SnmpCorrVbindMatchEnum>`
                        
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
                            self.parent = None
                            self.match_type = None
                            self.oid = None
                            self.reg_exp = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-oper:var-bind'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.match_type is not None:
                                return True

                            if self.oid is not None:
                                return True

                            if self.reg_exp is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                            return meta._meta_table['Snmp.Correlator.RuleDetails.RuleDetail.RootCause.VarBind']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-oper:root-cause'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.oid is not None:
                            return True

                        if self.var_bind is not None:
                            for child_ref in self.var_bind:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                        return meta._meta_table['Snmp.Correlator.RuleDetails.RuleDetail.RootCause']['meta_info']


                class NonRootcaus(object):
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
                        self.parent = None
                        self.oid = None
                        self.var_bind = YList()
                        self.var_bind.parent = self
                        self.var_bind.name = 'var_bind'


                    class VarBind(object):
                        """
                        VarBinds of the trap
                        
                        .. attribute:: match_type
                        
                        	Varbind match type
                        	**type**\:   :py:class:`SnmpCorrVbindMatchEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.SnmpCorrVbindMatchEnum>`
                        
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
                            self.parent = None
                            self.match_type = None
                            self.oid = None
                            self.reg_exp = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-oper:var-bind'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.match_type is not None:
                                return True

                            if self.oid is not None:
                                return True

                            if self.reg_exp is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                            return meta._meta_table['Snmp.Correlator.RuleDetails.RuleDetail.NonRootcaus.VarBind']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-oper:non-rootcaus'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.oid is not None:
                            return True

                        if self.var_bind is not None:
                            for child_ref in self.var_bind:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                        return meta._meta_table['Snmp.Correlator.RuleDetails.RuleDetail.NonRootcaus']['meta_info']


                class ApplyHost(object):
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
                        self.parent = None
                        self.ip_address = None
                        self.port = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-oper:apply-host'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.ip_address is not None:
                            return True

                        if self.port is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                        return meta._meta_table['Snmp.Correlator.RuleDetails.RuleDetail.ApplyHost']['meta_info']

                @property
                def _common_path(self):
                    if self.rule_name is None:
                        raise YPYModelError('Key property rule_name is None')

                    return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:correlator/Cisco-IOS-XR-snmp-agent-oper:rule-details/Cisco-IOS-XR-snmp-agent-oper:rule-detail[Cisco-IOS-XR-snmp-agent-oper:rule-name = ' + str(self.rule_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.rule_name is not None:
                        return True

                    if self.apply_host is not None:
                        for child_ref in self.apply_host:
                            if child_ref._has_data():
                                return True

                    if self.non_rootcaus is not None:
                        for child_ref in self.non_rootcaus:
                            if child_ref._has_data():
                                return True

                    if self.root_cause is not None and self.root_cause._has_data():
                        return True

                    if self.rule_summary is not None and self.rule_summary._has_data():
                        return True

                    if self.timeout is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.Correlator.RuleDetails.RuleDetail']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:correlator/Cisco-IOS-XR-snmp-agent-oper:rule-details'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.rule_detail is not None:
                    for child_ref in self.rule_detail:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Correlator.RuleDetails']['meta_info']


        class BufferStatus(object):
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
                self.parent = None
                self.configured_size = None
                self.current_size = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:correlator/Cisco-IOS-XR-snmp-agent-oper:buffer-status'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.configured_size is not None:
                    return True

                if self.current_size is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Correlator.BufferStatus']['meta_info']


        class RuleSetDetails(object):
            """
            Table that contains the ruleset detail info
            
            .. attribute:: rule_set_detail
            
            	Detail of one of the correlation rulesets
            	**type**\: list of    :py:class:`RuleSetDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Correlator.RuleSetDetails.RuleSetDetail>`
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                self.parent = None
                self.rule_set_detail = YList()
                self.rule_set_detail.parent = self
                self.rule_set_detail.name = 'rule_set_detail'


            class RuleSetDetail(object):
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
                    self.parent = None
                    self.rule_set_name = None
                    self.rule_set_name_xr = None
                    self.rules = YList()
                    self.rules.parent = self
                    self.rules.name = 'rules'


                class Rules(object):
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
                    	**type**\:   :py:class:`SnmpCorrRuleStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.SnmpCorrRuleStateEnum>`
                    
                    

                    """

                    _prefix = 'snmp-agent-oper'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.buffered_traps_count = None
                        self.rule_name = None
                        self.rule_state = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-oper:rules'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.buffered_traps_count is not None:
                            return True

                        if self.rule_name is not None:
                            return True

                        if self.rule_state is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                        return meta._meta_table['Snmp.Correlator.RuleSetDetails.RuleSetDetail.Rules']['meta_info']

                @property
                def _common_path(self):
                    if self.rule_set_name is None:
                        raise YPYModelError('Key property rule_set_name is None')

                    return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:correlator/Cisco-IOS-XR-snmp-agent-oper:rule-set-details/Cisco-IOS-XR-snmp-agent-oper:rule-set-detail[Cisco-IOS-XR-snmp-agent-oper:rule-set-name = ' + str(self.rule_set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.rule_set_name is not None:
                        return True

                    if self.rule_set_name_xr is not None:
                        return True

                    if self.rules is not None:
                        for child_ref in self.rules:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.Correlator.RuleSetDetails.RuleSetDetail']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:correlator/Cisco-IOS-XR-snmp-agent-oper:rule-set-details'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.rule_set_detail is not None:
                    for child_ref in self.rule_set_detail:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Correlator.RuleSetDetails']['meta_info']


        class Traps(object):
            """
            Correlated traps Table
            
            .. attribute:: trap
            
            	One of the correlated traps
            	**type**\: list of    :py:class:`Trap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.Correlator.Traps.Trap>`
            
            

            """

            _prefix = 'snmp-agent-oper'
            _revision = '2016-06-01'

            def __init__(self):
                self.parent = None
                self.trap = YList()
                self.trap.parent = self
                self.trap.name = 'trap'


            class Trap(object):
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
                    self.parent = None
                    self.entry_id = None
                    self.correlation_id = None
                    self.is_root_cause = None
                    self.rule_name = None
                    self.trap_info = Snmp.Correlator.Traps.Trap.TrapInfo()
                    self.trap_info.parent = self


                class TrapInfo(object):
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
                        self.parent = None
                        self.oid = None
                        self.relative_timestamp = None
                        self.timestamp = None
                        self.var_bind = YList()
                        self.var_bind.parent = self
                        self.var_bind.name = 'var_bind'


                    class VarBind(object):
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
                            self.parent = None
                            self.oid = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-oper:var-bind'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.oid is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                            return meta._meta_table['Snmp.Correlator.Traps.Trap.TrapInfo.VarBind']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-oper:trap-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.oid is not None:
                            return True

                        if self.relative_timestamp is not None:
                            return True

                        if self.timestamp is not None:
                            return True

                        if self.var_bind is not None:
                            for child_ref in self.var_bind:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                        return meta._meta_table['Snmp.Correlator.Traps.Trap.TrapInfo']['meta_info']

                @property
                def _common_path(self):
                    if self.entry_id is None:
                        raise YPYModelError('Key property entry_id is None')

                    return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:correlator/Cisco-IOS-XR-snmp-agent-oper:traps/Cisco-IOS-XR-snmp-agent-oper:trap[Cisco-IOS-XR-snmp-agent-oper:entry-id = ' + str(self.entry_id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.entry_id is not None:
                        return True

                    if self.correlation_id is not None:
                        return True

                    if self.is_root_cause is not None:
                        return True

                    if self.rule_name is not None:
                        return True

                    if self.trap_info is not None and self.trap_info._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.Correlator.Traps.Trap']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:correlator/Cisco-IOS-XR-snmp-agent-oper:traps'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.trap is not None:
                    for child_ref in self.trap:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.Correlator.Traps']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:correlator'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.buffer_status is not None and self.buffer_status._has_data():
                return True

            if self.rule_details is not None and self.rule_details._has_data():
                return True

            if self.rule_set_details is not None and self.rule_set_details._has_data():
                return True

            if self.traps is not None and self.traps._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
            return meta._meta_table['Snmp.Correlator']['meta_info']


    class InterfaceIndexes(object):
        """
        List of index
        
        .. attribute:: interface_index
        
        	Interface Index
        	**type**\: list of    :py:class:`InterfaceIndex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.InterfaceIndexes.InterfaceIndex>`
        
        

        """

        _prefix = 'snmp-agent-oper'
        _revision = '2016-06-01'

        def __init__(self):
            self.parent = None
            self.interface_index = YList()
            self.interface_index.parent = self
            self.interface_index.name = 'interface_index'


        class InterfaceIndex(object):
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
                self.parent = None
                self.interface_index = None
                self.interface_name = None

            @property
            def _common_path(self):
                if self.interface_index is None:
                    raise YPYModelError('Key property interface_index is None')

                return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:interface-indexes/Cisco-IOS-XR-snmp-agent-oper:interface-index[Cisco-IOS-XR-snmp-agent-oper:interface-index = ' + str(self.interface_index) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.interface_index is not None:
                    return True

                if self.interface_name is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.InterfaceIndexes.InterfaceIndex']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:interface-indexes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.interface_index is not None:
                for child_ref in self.interface_index:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
            return meta._meta_table['Snmp.InterfaceIndexes']['meta_info']


    class IfIndexes(object):
        """
        List of ifnames
        
        .. attribute:: if_index
        
        	Interface Index
        	**type**\: list of    :py:class:`IfIndex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.IfIndexes.IfIndex>`
        
        

        """

        _prefix = 'snmp-agent-oper'
        _revision = '2016-06-01'

        def __init__(self):
            self.parent = None
            self.if_index = YList()
            self.if_index.parent = self
            self.if_index.name = 'if_index'


        class IfIndex(object):
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
                self.parent = None
                self.interface_index = None
                self.interface_name = None

            @property
            def _common_path(self):
                if self.interface_index is None:
                    raise YPYModelError('Key property interface_index is None')

                return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:if-indexes/Cisco-IOS-XR-snmp-agent-oper:if-index[Cisco-IOS-XR-snmp-agent-oper:interface-index = ' + str(self.interface_index) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.interface_index is not None:
                    return True

                if self.interface_name is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.IfIndexes.IfIndex']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-agent-oper:if-indexes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.if_index is not None:
                for child_ref in self.if_index:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
            return meta._meta_table['Snmp.IfIndexes']['meta_info']


    class EntityMib(object):
        """
        SNMP entity mib
        
        .. attribute:: entity_physical_indexes
        
        	SNMP entity mib
        	**type**\:   :py:class:`EntityPhysicalIndexes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.EntityMib.EntityPhysicalIndexes>`
        
        

        """

        _prefix = 'snmp-entitymib-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.entity_physical_indexes = Snmp.EntityMib.EntityPhysicalIndexes()
            self.entity_physical_indexes.parent = self


        class EntityPhysicalIndexes(object):
            """
            SNMP entity mib
            
            .. attribute:: entity_physical_index
            
            	SNMP entPhysical index number
            	**type**\: list of    :py:class:`EntityPhysicalIndex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.EntityMib.EntityPhysicalIndexes.EntityPhysicalIndex>`
            
            

            """

            _prefix = 'snmp-entitymib-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.entity_physical_index = YList()
                self.entity_physical_index.parent = self
                self.entity_physical_index.name = 'entity_physical_index'


            class EntityPhysicalIndex(object):
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
                    self.parent = None
                    self.entity_phynum = None
                    self.ent_physical_descr = None
                    self.ent_physical_firmware_rev = None
                    self.ent_physical_hardware_rev = None
                    self.ent_physical_mfg_name = None
                    self.ent_physical_modelname = None
                    self.ent_physical_name = None
                    self.ent_physical_serial_num = None
                    self.ent_physical_software_rev = None
                    self.location = None
                    self.physical_index = None

                @property
                def _common_path(self):
                    if self.entity_phynum is None:
                        raise YPYModelError('Key property entity_phynum is None')

                    return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-entitymib-oper:entity-mib/Cisco-IOS-XR-snmp-entitymib-oper:entity-physical-indexes/Cisco-IOS-XR-snmp-entitymib-oper:entity-physical-index[Cisco-IOS-XR-snmp-entitymib-oper:entity-phynum = ' + str(self.entity_phynum) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.entity_phynum is not None:
                        return True

                    if self.ent_physical_descr is not None:
                        return True

                    if self.ent_physical_firmware_rev is not None:
                        return True

                    if self.ent_physical_hardware_rev is not None:
                        return True

                    if self.ent_physical_mfg_name is not None:
                        return True

                    if self.ent_physical_modelname is not None:
                        return True

                    if self.ent_physical_name is not None:
                        return True

                    if self.ent_physical_serial_num is not None:
                        return True

                    if self.ent_physical_software_rev is not None:
                        return True

                    if self.location is not None:
                        return True

                    if self.physical_index is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.EntityMib.EntityPhysicalIndexes.EntityPhysicalIndex']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-entitymib-oper:entity-mib/Cisco-IOS-XR-snmp-entitymib-oper:entity-physical-indexes'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.entity_physical_index is not None:
                    for child_ref in self.entity_physical_index:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.EntityMib.EntityPhysicalIndexes']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-entitymib-oper:entity-mib'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.entity_physical_indexes is not None and self.entity_physical_indexes._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
            return meta._meta_table['Snmp.EntityMib']['meta_info']


    class InterfaceMib(object):
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
            self.parent = None
            self.interface_aliases = Snmp.InterfaceMib.InterfaceAliases()
            self.interface_aliases.parent = self
            self.interface_connectors = Snmp.InterfaceMib.InterfaceConnectors()
            self.interface_connectors.parent = self
            self.interface_stack_statuses = Snmp.InterfaceMib.InterfaceStackStatuses()
            self.interface_stack_statuses.parent = self
            self.interfaces = Snmp.InterfaceMib.Interfaces()
            self.interfaces.parent = self
            self.notification_interfaces = Snmp.InterfaceMib.NotificationInterfaces()
            self.notification_interfaces.parent = self


        class Interfaces(object):
            """
            Interfaces ifIndex information
            
            .. attribute:: interface
            
            	ifIndex for a specific Interface Name
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.InterfaceMib.Interfaces.Interface>`
            
            

            """

            _prefix = 'snmp-ifmib-oper'
            _revision = '2015-01-07'

            def __init__(self):
                self.parent = None
                self.interface = YList()
                self.interface.parent = self
                self.interface.name = 'interface'


            class Interface(object):
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
                    self.parent = None
                    self.interface_name = None
                    self.if_index = None

                @property
                def _common_path(self):
                    if self.interface_name is None:
                        raise YPYModelError('Key property interface_name is None')

                    return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-ifmib-oper:interface-mib/Cisco-IOS-XR-snmp-ifmib-oper:interfaces/Cisco-IOS-XR-snmp-ifmib-oper:interface[Cisco-IOS-XR-snmp-ifmib-oper:interface-name = ' + str(self.interface_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface_name is not None:
                        return True

                    if self.if_index is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.InterfaceMib.Interfaces.Interface']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-ifmib-oper:interface-mib/Cisco-IOS-XR-snmp-ifmib-oper:interfaces'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.interface is not None:
                    for child_ref in self.interface:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.InterfaceMib.Interfaces']['meta_info']


        class InterfaceConnectors(object):
            """
            Interfaces ifConnectorPresent information
            
            .. attribute:: interface_connector
            
            	ifConnectorPresent for a specific Interface Name
            	**type**\: list of    :py:class:`InterfaceConnector <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.InterfaceMib.InterfaceConnectors.InterfaceConnector>`
            
            

            """

            _prefix = 'snmp-ifmib-oper'
            _revision = '2015-01-07'

            def __init__(self):
                self.parent = None
                self.interface_connector = YList()
                self.interface_connector.parent = self
                self.interface_connector.name = 'interface_connector'


            class InterfaceConnector(object):
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
                    self.parent = None
                    self.interface_name = None
                    self.if_connector_present = None

                @property
                def _common_path(self):
                    if self.interface_name is None:
                        raise YPYModelError('Key property interface_name is None')

                    return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-ifmib-oper:interface-mib/Cisco-IOS-XR-snmp-ifmib-oper:interface-connectors/Cisco-IOS-XR-snmp-ifmib-oper:interface-connector[Cisco-IOS-XR-snmp-ifmib-oper:interface-name = ' + str(self.interface_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface_name is not None:
                        return True

                    if self.if_connector_present is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.InterfaceMib.InterfaceConnectors.InterfaceConnector']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-ifmib-oper:interface-mib/Cisco-IOS-XR-snmp-ifmib-oper:interface-connectors'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.interface_connector is not None:
                    for child_ref in self.interface_connector:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.InterfaceMib.InterfaceConnectors']['meta_info']


        class InterfaceAliases(object):
            """
            Interfaces ifAlias information
            
            .. attribute:: interface_alias
            
            	ifAlias for a specific Interface Name
            	**type**\: list of    :py:class:`InterfaceAlias <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.InterfaceMib.InterfaceAliases.InterfaceAlias>`
            
            

            """

            _prefix = 'snmp-ifmib-oper'
            _revision = '2015-01-07'

            def __init__(self):
                self.parent = None
                self.interface_alias = YList()
                self.interface_alias.parent = self
                self.interface_alias.name = 'interface_alias'


            class InterfaceAlias(object):
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
                    self.parent = None
                    self.interface_name = None
                    self.if_alias = None

                @property
                def _common_path(self):
                    if self.interface_name is None:
                        raise YPYModelError('Key property interface_name is None')

                    return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-ifmib-oper:interface-mib/Cisco-IOS-XR-snmp-ifmib-oper:interface-aliases/Cisco-IOS-XR-snmp-ifmib-oper:interface-alias[Cisco-IOS-XR-snmp-ifmib-oper:interface-name = ' + str(self.interface_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface_name is not None:
                        return True

                    if self.if_alias is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.InterfaceMib.InterfaceAliases.InterfaceAlias']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-ifmib-oper:interface-mib/Cisco-IOS-XR-snmp-ifmib-oper:interface-aliases'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.interface_alias is not None:
                    for child_ref in self.interface_alias:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.InterfaceMib.InterfaceAliases']['meta_info']


        class NotificationInterfaces(object):
            """
            Interfaces Notification information
            
            .. attribute:: notification_interface
            
            	Notification for specific Interface Name
            	**type**\: list of    :py:class:`NotificationInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.InterfaceMib.NotificationInterfaces.NotificationInterface>`
            
            

            """

            _prefix = 'snmp-ifmib-oper'
            _revision = '2015-01-07'

            def __init__(self):
                self.parent = None
                self.notification_interface = YList()
                self.notification_interface.parent = self
                self.notification_interface.name = 'notification_interface'


            class NotificationInterface(object):
                """
                Notification for specific Interface Name
                
                .. attribute:: interface_name  <key>
                
                	Interface Name
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: link_up_down_notif_status
                
                	LinkUpDown notification status
                	**type**\:   :py:class:`LinkUpDownStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_ifmib_oper.LinkUpDownStatusEnum>`
                
                

                """

                _prefix = 'snmp-ifmib-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    self.parent = None
                    self.interface_name = None
                    self.link_up_down_notif_status = None

                @property
                def _common_path(self):
                    if self.interface_name is None:
                        raise YPYModelError('Key property interface_name is None')

                    return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-ifmib-oper:interface-mib/Cisco-IOS-XR-snmp-ifmib-oper:notification-interfaces/Cisco-IOS-XR-snmp-ifmib-oper:notification-interface[Cisco-IOS-XR-snmp-ifmib-oper:interface-name = ' + str(self.interface_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface_name is not None:
                        return True

                    if self.link_up_down_notif_status is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.InterfaceMib.NotificationInterfaces.NotificationInterface']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-ifmib-oper:interface-mib/Cisco-IOS-XR-snmp-ifmib-oper:notification-interfaces'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.notification_interface is not None:
                    for child_ref in self.notification_interface:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.InterfaceMib.NotificationInterfaces']['meta_info']


        class InterfaceStackStatuses(object):
            """
            Interfaces ifstackstatus information
            
            .. attribute:: interface_stack_status
            
            	ifstatus for a pair of Interface
            	**type**\: list of    :py:class:`InterfaceStackStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.InterfaceMib.InterfaceStackStatuses.InterfaceStackStatus>`
            
            

            """

            _prefix = 'snmp-ifmib-oper'
            _revision = '2015-01-07'

            def __init__(self):
                self.parent = None
                self.interface_stack_status = YList()
                self.interface_stack_status.parent = self
                self.interface_stack_status.name = 'interface_stack_status'


            class InterfaceStackStatus(object):
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
                    self.parent = None
                    self.interface_stack_status = None
                    self.if_stack_higher_layer = None
                    self.if_stack_lower_layer = None
                    self.if_stack_status = None

                @property
                def _common_path(self):
                    if self.interface_stack_status is None:
                        raise YPYModelError('Key property interface_stack_status is None')

                    return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-ifmib-oper:interface-mib/Cisco-IOS-XR-snmp-ifmib-oper:interface-stack-statuses/Cisco-IOS-XR-snmp-ifmib-oper:interface-stack-status[Cisco-IOS-XR-snmp-ifmib-oper:interface-stack-status = ' + str(self.interface_stack_status) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface_stack_status is not None:
                        return True

                    if self.if_stack_higher_layer is not None:
                        return True

                    if self.if_stack_lower_layer is not None:
                        return True

                    if self.if_stack_status is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.InterfaceMib.InterfaceStackStatuses.InterfaceStackStatus']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-ifmib-oper:interface-mib/Cisco-IOS-XR-snmp-ifmib-oper:interface-stack-statuses'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.interface_stack_status is not None:
                    for child_ref in self.interface_stack_status:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.InterfaceMib.InterfaceStackStatuses']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-ifmib-oper:interface-mib'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.interface_aliases is not None and self.interface_aliases._has_data():
                return True

            if self.interface_connectors is not None and self.interface_connectors._has_data():
                return True

            if self.interface_stack_statuses is not None and self.interface_stack_statuses._has_data():
                return True

            if self.interfaces is not None and self.interfaces._has_data():
                return True

            if self.notification_interfaces is not None and self.notification_interfaces._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
            return meta._meta_table['Snmp.InterfaceMib']['meta_info']


    class SensorMib(object):
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
            self.parent = None
            self.ent_phy_indexes = Snmp.SensorMib.EntPhyIndexes()
            self.ent_phy_indexes.parent = self
            self.physical_indexes = Snmp.SensorMib.PhysicalIndexes()
            self.physical_indexes.parent = self


        class PhysicalIndexes(object):
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
                self.parent = None
                self.physical_index = YList()
                self.physical_index.parent = self
                self.physical_index.name = 'physical_index'


            class PhysicalIndex(object):
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
                    self.parent = None
                    self.index = None
                    self.threshold_indexes = Snmp.SensorMib.PhysicalIndexes.PhysicalIndex.ThresholdIndexes()
                    self.threshold_indexes.parent = self


                class ThresholdIndexes(object):
                    """
                    List of threshold index
                    
                    .. attribute:: threshold_index
                    
                    	Threshold value for threshold index
                    	**type**\: list of    :py:class:`ThresholdIndex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.SensorMib.PhysicalIndexes.PhysicalIndex.ThresholdIndexes.ThresholdIndex>`
                    
                    

                    """

                    _prefix = 'snmp-sensormib-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.threshold_index = YList()
                        self.threshold_index.parent = self
                        self.threshold_index.name = 'threshold_index'


                    class ThresholdIndex(object):
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
                            self.parent = None
                            self.phy_index = None
                            self.thre_index = None
                            self.threshold_evaluation = None
                            self.threshold_notification_enabled = None
                            self.threshold_relation = None
                            self.threshold_severity = None
                            self.threshold_value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-snmp-sensormib-oper:threshold-index'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.phy_index is not None:
                                return True

                            if self.thre_index is not None:
                                return True

                            if self.threshold_evaluation is not None:
                                return True

                            if self.threshold_notification_enabled is not None:
                                return True

                            if self.threshold_relation is not None:
                                return True

                            if self.threshold_severity is not None:
                                return True

                            if self.threshold_value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                            return meta._meta_table['Snmp.SensorMib.PhysicalIndexes.PhysicalIndex.ThresholdIndexes.ThresholdIndex']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-snmp-sensormib-oper:threshold-indexes'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.threshold_index is not None:
                            for child_ref in self.threshold_index:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                        return meta._meta_table['Snmp.SensorMib.PhysicalIndexes.PhysicalIndex.ThresholdIndexes']['meta_info']

                @property
                def _common_path(self):
                    if self.index is None:
                        raise YPYModelError('Key property index is None')

                    return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-sensormib-oper:sensor-mib/Cisco-IOS-XR-snmp-sensormib-oper:physical-indexes/Cisco-IOS-XR-snmp-sensormib-oper:physical-index[Cisco-IOS-XR-snmp-sensormib-oper:index = ' + str(self.index) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.index is not None:
                        return True

                    if self.threshold_indexes is not None and self.threshold_indexes._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.SensorMib.PhysicalIndexes.PhysicalIndex']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-sensormib-oper:sensor-mib/Cisco-IOS-XR-snmp-sensormib-oper:physical-indexes'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.physical_index is not None:
                    for child_ref in self.physical_index:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.SensorMib.PhysicalIndexes']['meta_info']


        class EntPhyIndexes(object):
            """
            List of physical index 
            
            .. attribute:: ent_phy_index
            
            	Sensor value for physical index
            	**type**\: list of    :py:class:`EntPhyIndex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper.Snmp.SensorMib.EntPhyIndexes.EntPhyIndex>`
            
            

            """

            _prefix = 'snmp-sensormib-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.ent_phy_index = YList()
                self.ent_phy_index.parent = self
                self.ent_phy_index.name = 'ent_phy_index'


            class EntPhyIndex(object):
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
                    self.parent = None
                    self.index = None
                    self.age_time_stamp = None
                    self.alarm_type = None
                    self.data_type = None
                    self.device_description = None
                    self.device_id = None
                    self.field_validity_bitmap = None
                    self.measured_entity = None
                    self.precision = None
                    self.scale = None
                    self.status = None
                    self.units = None
                    self.update_rate = None
                    self.value = None

                @property
                def _common_path(self):
                    if self.index is None:
                        raise YPYModelError('Key property index is None')

                    return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-sensormib-oper:sensor-mib/Cisco-IOS-XR-snmp-sensormib-oper:ent-phy-indexes/Cisco-IOS-XR-snmp-sensormib-oper:ent-phy-index[Cisco-IOS-XR-snmp-sensormib-oper:index = ' + str(self.index) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.index is not None:
                        return True

                    if self.age_time_stamp is not None:
                        return True

                    if self.alarm_type is not None:
                        return True

                    if self.data_type is not None:
                        return True

                    if self.device_description is not None:
                        return True

                    if self.device_id is not None:
                        return True

                    if self.field_validity_bitmap is not None:
                        return True

                    if self.measured_entity is not None:
                        return True

                    if self.precision is not None:
                        return True

                    if self.scale is not None:
                        return True

                    if self.status is not None:
                        return True

                    if self.units is not None:
                        return True

                    if self.update_rate is not None:
                        return True

                    if self.value is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                    return meta._meta_table['Snmp.SensorMib.EntPhyIndexes.EntPhyIndex']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-sensormib-oper:sensor-mib/Cisco-IOS-XR-snmp-sensormib-oper:ent-phy-indexes'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ent_phy_index is not None:
                    for child_ref in self.ent_phy_index:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
                return meta._meta_table['Snmp.SensorMib.EntPhyIndexes']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-agent-oper:snmp/Cisco-IOS-XR-snmp-sensormib-oper:sensor-mib'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ent_phy_indexes is not None and self.ent_phy_indexes._has_data():
                return True

            if self.physical_indexes is not None and self.physical_indexes._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
            return meta._meta_table['Snmp.SensorMib']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-snmp-agent-oper:snmp'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.correlator is not None and self.correlator._has_data():
            return True

        if self.entity_mib is not None and self.entity_mib._has_data():
            return True

        if self.if_indexes is not None and self.if_indexes._has_data():
            return True

        if self.information is not None and self.information._has_data():
            return True

        if self.interface_indexes is not None and self.interface_indexes._has_data():
            return True

        if self.interface_mib is not None and self.interface_mib._has_data():
            return True

        if self.interfaces is not None and self.interfaces._has_data():
            return True

        if self.sensor_mib is not None and self.sensor_mib._has_data():
            return True

        if self.trap_servers is not None and self.trap_servers._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_oper as meta
        return meta._meta_table['Snmp']['meta_info']



""" Cisco_IOS_XR_infra_tc_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-tc package operational data.

This module contains definitions
for the following management objects\:
  traffic\-collector\: Global Traffic Collector configuration
    commands

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class TcOperAfNameEnum(Enum):
    """
    TcOperAfNameEnum

    Tc oper af name

    .. data:: ipv4 = 0

    	IPv4

    .. data:: ipv6 = 1

    	IPv6

    """

    ipv4 = 0

    ipv6 = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_oper as meta
        return meta._meta_table['TcOperAfNameEnum']



class TrafficCollector(object):
    """
    Global Traffic Collector configuration commands
    
    .. attribute:: afs
    
    	Address Family specific operational data
    	**type**\:   :py:class:`Afs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs>`
    
    .. attribute:: external_interfaces
    
    	External Interface
    	**type**\:   :py:class:`ExternalInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.ExternalInterfaces>`
    
    .. attribute:: summary
    
    	Traffic Collector summary
    	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Summary>`
    
    .. attribute:: vrf_table
    
    	VRF specific operational data
    	**type**\:   :py:class:`VrfTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable>`
    
    

    """

    _prefix = 'infra-tc-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.afs = TrafficCollector.Afs()
        self.afs.parent = self
        self.external_interfaces = TrafficCollector.ExternalInterfaces()
        self.external_interfaces.parent = self
        self.summary = TrafficCollector.Summary()
        self.summary.parent = self
        self.vrf_table = TrafficCollector.VrfTable()
        self.vrf_table.parent = self


    class ExternalInterfaces(object):
        """
        External Interface
        
        .. attribute:: external_interface
        
        	External Interface 
        	**type**\: list of    :py:class:`ExternalInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.ExternalInterfaces.ExternalInterface>`
        
        

        """

        _prefix = 'infra-tc-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.external_interface = YList()
            self.external_interface.parent = self
            self.external_interface.name = 'external_interface'


        class ExternalInterface(object):
            """
            External Interface 
            
            .. attribute:: interface_name  <key>
            
            	The Interface Name
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: interface_handle
            
            	Interface handle
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: interface_name_xr
            
            	Interface name in Display format
            	**type**\:  str
            
            .. attribute:: is_interface_enabled
            
            	Flag to indicate interface enabled or not
            	**type**\:  bool
            
            .. attribute:: vrfid
            
            	Interface VRF ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-tc-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.interface_name = None
                self.interface_handle = None
                self.interface_name_xr = None
                self.is_interface_enabled = None
                self.vrfid = None

            @property
            def _common_path(self):
                if self.interface_name is None:
                    raise YPYModelError('Key property interface_name is None')

                return '/Cisco-IOS-XR-infra-tc-oper:traffic-collector/Cisco-IOS-XR-infra-tc-oper:external-interfaces/Cisco-IOS-XR-infra-tc-oper:external-interface[Cisco-IOS-XR-infra-tc-oper:interface-name = ' + str(self.interface_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.interface_name is not None:
                    return True

                if self.interface_handle is not None:
                    return True

                if self.interface_name_xr is not None:
                    return True

                if self.is_interface_enabled is not None:
                    return True

                if self.vrfid is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_oper as meta
                return meta._meta_table['TrafficCollector.ExternalInterfaces.ExternalInterface']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-tc-oper:traffic-collector/Cisco-IOS-XR-infra-tc-oper:external-interfaces'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.external_interface is not None:
                for child_ref in self.external_interface:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_oper as meta
            return meta._meta_table['TrafficCollector.ExternalInterfaces']['meta_info']


    class Summary(object):
        """
        Traffic Collector summary
        
        .. attribute:: checkpoint_message_statistic
        
        	Statistics per message type for Chkpt
        	**type**\: list of    :py:class:`CheckpointMessageStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Summary.CheckpointMessageStatistic>`
        
        .. attribute:: collection_interval
        
        	Statistic collection interval in minutes
        	**type**\:  int
        
        	**range:** 0..255
        
        	**units**\: minute
        
        .. attribute:: collection_message_statistic
        
        	Statistics per message type for STAT collector
        	**type**\: list of    :py:class:`CollectionMessageStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Summary.CollectionMessageStatistic>`
        
        .. attribute:: collection_timer_is_running
        
        	TRUE if collection timer is running
        	**type**\:  bool
        
        .. attribute:: database_statistics_external_interface
        
        	Database statistics for External Interface
        	**type**\:   :py:class:`DatabaseStatisticsExternalInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Summary.DatabaseStatisticsExternalInterface>`
        
        .. attribute:: history_size
        
        	Statistics history size
        	**type**\:  int
        
        	**range:** 0..255
        
        .. attribute:: timeout_interval
        
        	Statistic history timeout interval in hours
        	**type**\:  int
        
        	**range:** 0..65535
        
        	**units**\: hour
        
        .. attribute:: timeout_timer_is_running
        
        	TRUE if history timeout timer is running
        	**type**\:  bool
        
        .. attribute:: vrf_statistic
        
        	VRF table statistics
        	**type**\: list of    :py:class:`VrfStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Summary.VrfStatistic>`
        
        

        """

        _prefix = 'infra-tc-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.checkpoint_message_statistic = YList()
            self.checkpoint_message_statistic.parent = self
            self.checkpoint_message_statistic.name = 'checkpoint_message_statistic'
            self.collection_interval = None
            self.collection_message_statistic = YList()
            self.collection_message_statistic.parent = self
            self.collection_message_statistic.name = 'collection_message_statistic'
            self.collection_timer_is_running = None
            self.database_statistics_external_interface = TrafficCollector.Summary.DatabaseStatisticsExternalInterface()
            self.database_statistics_external_interface.parent = self
            self.history_size = None
            self.timeout_interval = None
            self.timeout_timer_is_running = None
            self.vrf_statistic = YList()
            self.vrf_statistic.parent = self
            self.vrf_statistic.name = 'vrf_statistic'


        class DatabaseStatisticsExternalInterface(object):
            """
            Database statistics for External Interface
            
            .. attribute:: number_of_add_o_perations
            
            	Number of add operations
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: number_of_delete_o_perations
            
            	Number of delete operations
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: number_of_entries
            
            	Number of DB entries
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: number_of_stale_entries
            
            	Number of stale  entries
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-tc-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.number_of_add_o_perations = None
                self.number_of_delete_o_perations = None
                self.number_of_entries = None
                self.number_of_stale_entries = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-tc-oper:traffic-collector/Cisco-IOS-XR-infra-tc-oper:summary/Cisco-IOS-XR-infra-tc-oper:database-statistics-external-interface'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.number_of_add_o_perations is not None:
                    return True

                if self.number_of_delete_o_perations is not None:
                    return True

                if self.number_of_entries is not None:
                    return True

                if self.number_of_stale_entries is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_oper as meta
                return meta._meta_table['TrafficCollector.Summary.DatabaseStatisticsExternalInterface']['meta_info']


        class VrfStatistic(object):
            """
            VRF table statistics
            
            .. attribute:: database_statistics_ipv4
            
            	Database statistics for IPv4 table
            	**type**\:   :py:class:`DatabaseStatisticsIpv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsIpv4>`
            
            .. attribute:: database_statistics_tunnel
            
            	Database statistics for Tunnel table
            	**type**\:   :py:class:`DatabaseStatisticsTunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsTunnel>`
            
            .. attribute:: vrf_name
            
            	VRF name
            	**type**\:  str
            
            

            """

            _prefix = 'infra-tc-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.database_statistics_ipv4 = TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsIpv4()
                self.database_statistics_ipv4.parent = self
                self.database_statistics_tunnel = TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsTunnel()
                self.database_statistics_tunnel.parent = self
                self.vrf_name = None


            class DatabaseStatisticsIpv4(object):
                """
                Database statistics for IPv4 table
                
                .. attribute:: number_of_add_o_perations
                
                	Number of add operations
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: number_of_delete_o_perations
                
                	Number of delete operations
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: number_of_entries
                
                	Number of DB entries
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: number_of_stale_entries
                
                	Number of stale  entries
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'infra-tc-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.number_of_add_o_perations = None
                    self.number_of_delete_o_perations = None
                    self.number_of_entries = None
                    self.number_of_stale_entries = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-infra-tc-oper:traffic-collector/Cisco-IOS-XR-infra-tc-oper:summary/Cisco-IOS-XR-infra-tc-oper:vrf-statistic/Cisco-IOS-XR-infra-tc-oper:database-statistics-ipv4'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.number_of_add_o_perations is not None:
                        return True

                    if self.number_of_delete_o_perations is not None:
                        return True

                    if self.number_of_entries is not None:
                        return True

                    if self.number_of_stale_entries is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_oper as meta
                    return meta._meta_table['TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsIpv4']['meta_info']


            class DatabaseStatisticsTunnel(object):
                """
                Database statistics for Tunnel table
                
                .. attribute:: number_of_add_o_perations
                
                	Number of add operations
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: number_of_delete_o_perations
                
                	Number of delete operations
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: number_of_entries
                
                	Number of DB entries
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: number_of_stale_entries
                
                	Number of stale  entries
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'infra-tc-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.number_of_add_o_perations = None
                    self.number_of_delete_o_perations = None
                    self.number_of_entries = None
                    self.number_of_stale_entries = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-infra-tc-oper:traffic-collector/Cisco-IOS-XR-infra-tc-oper:summary/Cisco-IOS-XR-infra-tc-oper:vrf-statistic/Cisco-IOS-XR-infra-tc-oper:database-statistics-tunnel'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.number_of_add_o_perations is not None:
                        return True

                    if self.number_of_delete_o_perations is not None:
                        return True

                    if self.number_of_entries is not None:
                        return True

                    if self.number_of_stale_entries is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_oper as meta
                    return meta._meta_table['TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsTunnel']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-tc-oper:traffic-collector/Cisco-IOS-XR-infra-tc-oper:summary/Cisco-IOS-XR-infra-tc-oper:vrf-statistic'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.database_statistics_ipv4 is not None and self.database_statistics_ipv4._has_data():
                    return True

                if self.database_statistics_tunnel is not None and self.database_statistics_tunnel._has_data():
                    return True

                if self.vrf_name is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_oper as meta
                return meta._meta_table['TrafficCollector.Summary.VrfStatistic']['meta_info']


        class CollectionMessageStatistic(object):
            """
            Statistics per message type for STAT collector
            
            .. attribute:: byte_received
            
            	Number of bytes received
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: byte
            
            .. attribute:: byte_sent
            
            	Number of bytes sent
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: byte
            
            .. attribute:: maimum_latency_timestamp
            
            	Timestamp of maximum latency
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: maximum_roundtrip_latency
            
            	Maximum roundtrip latency in msec
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: packet_received
            
            	Number of packets received
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: packet_sent
            
            	Number of packets sent
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'infra-tc-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.byte_received = None
                self.byte_sent = None
                self.maimum_latency_timestamp = None
                self.maximum_roundtrip_latency = None
                self.packet_received = None
                self.packet_sent = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-tc-oper:traffic-collector/Cisco-IOS-XR-infra-tc-oper:summary/Cisco-IOS-XR-infra-tc-oper:collection-message-statistic'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.byte_received is not None:
                    return True

                if self.byte_sent is not None:
                    return True

                if self.maimum_latency_timestamp is not None:
                    return True

                if self.maximum_roundtrip_latency is not None:
                    return True

                if self.packet_received is not None:
                    return True

                if self.packet_sent is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_oper as meta
                return meta._meta_table['TrafficCollector.Summary.CollectionMessageStatistic']['meta_info']


        class CheckpointMessageStatistic(object):
            """
            Statistics per message type for Chkpt
            
            .. attribute:: byte_received
            
            	Number of bytes received
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: byte
            
            .. attribute:: byte_sent
            
            	Number of bytes sent
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: byte
            
            .. attribute:: maimum_latency_timestamp
            
            	Timestamp of maximum latency
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: maximum_roundtrip_latency
            
            	Maximum roundtrip latency in msec
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: packet_received
            
            	Number of packets received
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: packet_sent
            
            	Number of packets sent
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'infra-tc-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.byte_received = None
                self.byte_sent = None
                self.maimum_latency_timestamp = None
                self.maximum_roundtrip_latency = None
                self.packet_received = None
                self.packet_sent = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-tc-oper:traffic-collector/Cisco-IOS-XR-infra-tc-oper:summary/Cisco-IOS-XR-infra-tc-oper:checkpoint-message-statistic'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.byte_received is not None:
                    return True

                if self.byte_sent is not None:
                    return True

                if self.maimum_latency_timestamp is not None:
                    return True

                if self.maximum_roundtrip_latency is not None:
                    return True

                if self.packet_received is not None:
                    return True

                if self.packet_sent is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_oper as meta
                return meta._meta_table['TrafficCollector.Summary.CheckpointMessageStatistic']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-tc-oper:traffic-collector/Cisco-IOS-XR-infra-tc-oper:summary'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.checkpoint_message_statistic is not None:
                for child_ref in self.checkpoint_message_statistic:
                    if child_ref._has_data():
                        return True

            if self.collection_interval is not None:
                return True

            if self.collection_message_statistic is not None:
                for child_ref in self.collection_message_statistic:
                    if child_ref._has_data():
                        return True

            if self.collection_timer_is_running is not None:
                return True

            if self.database_statistics_external_interface is not None and self.database_statistics_external_interface._has_data():
                return True

            if self.history_size is not None:
                return True

            if self.timeout_interval is not None:
                return True

            if self.timeout_timer_is_running is not None:
                return True

            if self.vrf_statistic is not None:
                for child_ref in self.vrf_statistic:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_oper as meta
            return meta._meta_table['TrafficCollector.Summary']['meta_info']


    class VrfTable(object):
        """
        VRF specific operational data
        
        .. attribute:: default_vrf
        
        	DefaultVRF specific operational data
        	**type**\:   :py:class:`DefaultVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf>`
        
        

        """

        _prefix = 'infra-tc-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.default_vrf = TrafficCollector.VrfTable.DefaultVrf()
            self.default_vrf.parent = self


        class DefaultVrf(object):
            """
            DefaultVRF specific operational data
            
            .. attribute:: afs
            
            	Address Family specific operational data
            	**type**\:   :py:class:`Afs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs>`
            
            

            """

            _prefix = 'infra-tc-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.afs = TrafficCollector.VrfTable.DefaultVrf.Afs()
                self.afs.parent = self


            class Afs(object):
                """
                Address Family specific operational data
                
                .. attribute:: af
                
                	Operational data for given Address Family
                	**type**\: list of    :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af>`
                
                

                """

                _prefix = 'infra-tc-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.af = YList()
                    self.af.parent = self
                    self.af.name = 'af'


                class Af(object):
                    """
                    Operational data for given Address Family
                    
                    .. attribute:: af_name  <key>
                    
                    	Address Family name
                    	**type**\:   :py:class:`TcOperAfNameEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TcOperAfNameEnum>`
                    
                    .. attribute:: counters
                    
                    	Show Counters
                    	**type**\:   :py:class:`Counters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters>`
                    
                    

                    """

                    _prefix = 'infra-tc-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.af_name = None
                        self.counters = TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters()
                        self.counters.parent = self


                    class Counters(object):
                        """
                        Show Counters
                        
                        .. attribute:: prefixes
                        
                        	Prefix Database
                        	**type**\:   :py:class:`Prefixes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes>`
                        
                        .. attribute:: tunnels
                        
                        	Tunnels
                        	**type**\:   :py:class:`Tunnels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels>`
                        
                        

                        """

                        _prefix = 'infra-tc-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.prefixes = TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes()
                            self.prefixes.parent = self
                            self.tunnels = TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels()
                            self.tunnels.parent = self


                        class Prefixes(object):
                            """
                            Prefix Database
                            
                            .. attribute:: prefix
                            
                            	Show Prefix Counter
                            	**type**\: list of    :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix>`
                            
                            

                            """

                            _prefix = 'infra-tc-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.prefix = YList()
                                self.prefix.parent = self
                                self.prefix.name = 'prefix'


                            class Prefix(object):
                                """
                                Show Prefix Counter
                                
                                .. attribute:: base_counter_statistics
                                
                                	Base counter statistics
                                	**type**\:   :py:class:`BaseCounterStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics>`
                                
                                .. attribute:: ipaddr
                                
                                	IP Address
                                	**type**\:  str
                                
                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                
                                .. attribute:: is_active
                                
                                	Prefix is Active and collecting new Statistics
                                	**type**\:  bool
                                
                                .. attribute:: label
                                
                                	Local Label
                                	**type**\:  int
                                
                                	**range:** 16..1048575
                                
                                .. attribute:: label_xr
                                
                                	Label
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: mask
                                
                                	Prefix Mask
                                	**type**\:  str
                                
                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                
                                .. attribute:: prefix
                                
                                	Prefix Address (V4 or V6 Format)
                                	**type**\:  str
                                
                                .. attribute:: traffic_matrix_counter_statistics
                                
                                	Traffic Matrix (TM) counter statistics
                                	**type**\:   :py:class:`TrafficMatrixCounterStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics>`
                                
                                

                                """

                                _prefix = 'infra-tc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.base_counter_statistics = TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics()
                                    self.base_counter_statistics.parent = self
                                    self.ipaddr = None
                                    self.is_active = None
                                    self.label = None
                                    self.label_xr = None
                                    self.mask = None
                                    self.prefix = None
                                    self.traffic_matrix_counter_statistics = TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics()
                                    self.traffic_matrix_counter_statistics.parent = self


                                class BaseCounterStatistics(object):
                                    """
                                    Base counter statistics
                                    
                                    .. attribute:: count_history
                                    
                                    	Counter History
                                    	**type**\: list of    :py:class:`CountHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics.CountHistory>`
                                    
                                    .. attribute:: transmit_bytes_per_second_switched
                                    
                                    	Average Rate of Bytes/second switched
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte/s
                                    
                                    .. attribute:: transmit_packets_per_second_switched
                                    
                                    	Average Rate of Packets/second switched
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: packet/s
                                    
                                    

                                    """

                                    _prefix = 'infra-tc-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.count_history = YList()
                                        self.count_history.parent = self
                                        self.count_history.name = 'count_history'
                                        self.transmit_bytes_per_second_switched = None
                                        self.transmit_packets_per_second_switched = None


                                    class CountHistory(object):
                                        """
                                        Counter History
                                        
                                        .. attribute:: event_end_timestamp
                                        
                                        	Event End timestamp
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: event_start_timestamp
                                        
                                        	Event Start timestamp
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: is_valid
                                        
                                        	Flag to indicate if this history entry is valid
                                        	**type**\:  bool
                                        
                                        .. attribute:: transmit_number_of_bytes_switched
                                        
                                        	Number of Bytes switched in this interval
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: transmit_number_of_packets_switched
                                        
                                        	Number of packets switched in this interval
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'infra-tc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.event_end_timestamp = None
                                            self.event_start_timestamp = None
                                            self.is_valid = None
                                            self.transmit_number_of_bytes_switched = None
                                            self.transmit_number_of_packets_switched = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-infra-tc-oper:count-history'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.event_end_timestamp is not None:
                                                return True

                                            if self.event_start_timestamp is not None:
                                                return True

                                            if self.is_valid is not None:
                                                return True

                                            if self.transmit_number_of_bytes_switched is not None:
                                                return True

                                            if self.transmit_number_of_packets_switched is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_oper as meta
                                            return meta._meta_table['TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics.CountHistory']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-infra-tc-oper:base-counter-statistics'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.count_history is not None:
                                            for child_ref in self.count_history:
                                                if child_ref._has_data():
                                                    return True

                                        if self.transmit_bytes_per_second_switched is not None:
                                            return True

                                        if self.transmit_packets_per_second_switched is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_oper as meta
                                        return meta._meta_table['TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics']['meta_info']


                                class TrafficMatrixCounterStatistics(object):
                                    """
                                    Traffic Matrix (TM) counter statistics
                                    
                                    .. attribute:: count_history
                                    
                                    	Counter History
                                    	**type**\: list of    :py:class:`CountHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics.CountHistory>`
                                    
                                    .. attribute:: transmit_bytes_per_second_switched
                                    
                                    	Average Rate of Bytes/second switched
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte/s
                                    
                                    .. attribute:: transmit_packets_per_second_switched
                                    
                                    	Average Rate of Packets/second switched
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: packet/s
                                    
                                    

                                    """

                                    _prefix = 'infra-tc-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.count_history = YList()
                                        self.count_history.parent = self
                                        self.count_history.name = 'count_history'
                                        self.transmit_bytes_per_second_switched = None
                                        self.transmit_packets_per_second_switched = None


                                    class CountHistory(object):
                                        """
                                        Counter History
                                        
                                        .. attribute:: event_end_timestamp
                                        
                                        	Event End timestamp
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: event_start_timestamp
                                        
                                        	Event Start timestamp
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: is_valid
                                        
                                        	Flag to indicate if this history entry is valid
                                        	**type**\:  bool
                                        
                                        .. attribute:: transmit_number_of_bytes_switched
                                        
                                        	Number of Bytes switched in this interval
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: transmit_number_of_packets_switched
                                        
                                        	Number of packets switched in this interval
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'infra-tc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.event_end_timestamp = None
                                            self.event_start_timestamp = None
                                            self.is_valid = None
                                            self.transmit_number_of_bytes_switched = None
                                            self.transmit_number_of_packets_switched = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-infra-tc-oper:count-history'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.event_end_timestamp is not None:
                                                return True

                                            if self.event_start_timestamp is not None:
                                                return True

                                            if self.is_valid is not None:
                                                return True

                                            if self.transmit_number_of_bytes_switched is not None:
                                                return True

                                            if self.transmit_number_of_packets_switched is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_oper as meta
                                            return meta._meta_table['TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics.CountHistory']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-infra-tc-oper:traffic-matrix-counter-statistics'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.count_history is not None:
                                            for child_ref in self.count_history:
                                                if child_ref._has_data():
                                                    return True

                                        if self.transmit_bytes_per_second_switched is not None:
                                            return True

                                        if self.transmit_packets_per_second_switched is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_oper as meta
                                        return meta._meta_table['TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-infra-tc-oper:prefix'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.base_counter_statistics is not None and self.base_counter_statistics._has_data():
                                        return True

                                    if self.ipaddr is not None:
                                        return True

                                    if self.is_active is not None:
                                        return True

                                    if self.label is not None:
                                        return True

                                    if self.label_xr is not None:
                                        return True

                                    if self.mask is not None:
                                        return True

                                    if self.prefix is not None:
                                        return True

                                    if self.traffic_matrix_counter_statistics is not None and self.traffic_matrix_counter_statistics._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_oper as meta
                                    return meta._meta_table['TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-tc-oper:prefixes'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.prefix is not None:
                                    for child_ref in self.prefix:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_oper as meta
                                return meta._meta_table['TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes']['meta_info']


                        class Tunnels(object):
                            """
                            Tunnels
                            
                            .. attribute:: tunnel
                            
                            	Tunnel information
                            	**type**\: list of    :py:class:`Tunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel>`
                            
                            

                            """

                            _prefix = 'infra-tc-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.tunnel = YList()
                                self.tunnel.parent = self
                                self.tunnel.name = 'tunnel'


                            class Tunnel(object):
                                """
                                Tunnel information
                                
                                .. attribute:: interface_name  <key>
                                
                                	The Interface Name
                                	**type**\:  str
                                
                                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                
                                .. attribute:: base_counter_statistics
                                
                                	Base counter statistics
                                	**type**\:   :py:class:`BaseCounterStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics>`
                                
                                .. attribute:: interface_handle
                                
                                	Interface handle
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: interface_name_xr
                                
                                	Interface name in Display format
                                	**type**\:  str
                                
                                .. attribute:: is_active
                                
                                	Interface is Active and collecting new Statistics
                                	**type**\:  bool
                                
                                .. attribute:: vrfid
                                
                                	Interface VRF ID
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'infra-tc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.interface_name = None
                                    self.base_counter_statistics = TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics()
                                    self.base_counter_statistics.parent = self
                                    self.interface_handle = None
                                    self.interface_name_xr = None
                                    self.is_active = None
                                    self.vrfid = None


                                class BaseCounterStatistics(object):
                                    """
                                    Base counter statistics
                                    
                                    .. attribute:: count_history
                                    
                                    	Counter History
                                    	**type**\: list of    :py:class:`CountHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics.CountHistory>`
                                    
                                    .. attribute:: transmit_bytes_per_second_switched
                                    
                                    	Average Rate of Bytes/second switched
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte/s
                                    
                                    .. attribute:: transmit_packets_per_second_switched
                                    
                                    	Average Rate of Packets/second switched
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: packet/s
                                    
                                    

                                    """

                                    _prefix = 'infra-tc-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.count_history = YList()
                                        self.count_history.parent = self
                                        self.count_history.name = 'count_history'
                                        self.transmit_bytes_per_second_switched = None
                                        self.transmit_packets_per_second_switched = None


                                    class CountHistory(object):
                                        """
                                        Counter History
                                        
                                        .. attribute:: event_end_timestamp
                                        
                                        	Event End timestamp
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: event_start_timestamp
                                        
                                        	Event Start timestamp
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: is_valid
                                        
                                        	Flag to indicate if this history entry is valid
                                        	**type**\:  bool
                                        
                                        .. attribute:: transmit_number_of_bytes_switched
                                        
                                        	Number of Bytes switched in this interval
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: transmit_number_of_packets_switched
                                        
                                        	Number of packets switched in this interval
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'infra-tc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.event_end_timestamp = None
                                            self.event_start_timestamp = None
                                            self.is_valid = None
                                            self.transmit_number_of_bytes_switched = None
                                            self.transmit_number_of_packets_switched = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-infra-tc-oper:count-history'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.event_end_timestamp is not None:
                                                return True

                                            if self.event_start_timestamp is not None:
                                                return True

                                            if self.is_valid is not None:
                                                return True

                                            if self.transmit_number_of_bytes_switched is not None:
                                                return True

                                            if self.transmit_number_of_packets_switched is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_oper as meta
                                            return meta._meta_table['TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics.CountHistory']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-infra-tc-oper:base-counter-statistics'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.count_history is not None:
                                            for child_ref in self.count_history:
                                                if child_ref._has_data():
                                                    return True

                                        if self.transmit_bytes_per_second_switched is not None:
                                            return True

                                        if self.transmit_packets_per_second_switched is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_oper as meta
                                        return meta._meta_table['TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.interface_name is None:
                                        raise YPYModelError('Key property interface_name is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-infra-tc-oper:tunnel[Cisco-IOS-XR-infra-tc-oper:interface-name = ' + str(self.interface_name) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.interface_name is not None:
                                        return True

                                    if self.base_counter_statistics is not None and self.base_counter_statistics._has_data():
                                        return True

                                    if self.interface_handle is not None:
                                        return True

                                    if self.interface_name_xr is not None:
                                        return True

                                    if self.is_active is not None:
                                        return True

                                    if self.vrfid is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_oper as meta
                                    return meta._meta_table['TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-tc-oper:tunnels'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.tunnel is not None:
                                    for child_ref in self.tunnel:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_oper as meta
                                return meta._meta_table['TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-tc-oper:counters'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.prefixes is not None and self.prefixes._has_data():
                                return True

                            if self.tunnels is not None and self.tunnels._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_oper as meta
                            return meta._meta_table['TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters']['meta_info']

                    @property
                    def _common_path(self):
                        if self.af_name is None:
                            raise YPYModelError('Key property af_name is None')

                        return '/Cisco-IOS-XR-infra-tc-oper:traffic-collector/Cisco-IOS-XR-infra-tc-oper:vrf-table/Cisco-IOS-XR-infra-tc-oper:default-vrf/Cisco-IOS-XR-infra-tc-oper:afs/Cisco-IOS-XR-infra-tc-oper:af[Cisco-IOS-XR-infra-tc-oper:af-name = ' + str(self.af_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.af_name is not None:
                            return True

                        if self.counters is not None and self.counters._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_oper as meta
                        return meta._meta_table['TrafficCollector.VrfTable.DefaultVrf.Afs.Af']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-infra-tc-oper:traffic-collector/Cisco-IOS-XR-infra-tc-oper:vrf-table/Cisco-IOS-XR-infra-tc-oper:default-vrf/Cisco-IOS-XR-infra-tc-oper:afs'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.af is not None:
                        for child_ref in self.af:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_oper as meta
                    return meta._meta_table['TrafficCollector.VrfTable.DefaultVrf.Afs']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-tc-oper:traffic-collector/Cisco-IOS-XR-infra-tc-oper:vrf-table/Cisco-IOS-XR-infra-tc-oper:default-vrf'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.afs is not None and self.afs._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_oper as meta
                return meta._meta_table['TrafficCollector.VrfTable.DefaultVrf']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-tc-oper:traffic-collector/Cisco-IOS-XR-infra-tc-oper:vrf-table'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.default_vrf is not None and self.default_vrf._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_oper as meta
            return meta._meta_table['TrafficCollector.VrfTable']['meta_info']


    class Afs(object):
        """
        Address Family specific operational data
        
        .. attribute:: af
        
        	Operational data for given Address Family
        	**type**\: list of    :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af>`
        
        

        """

        _prefix = 'infra-tc-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.af = YList()
            self.af.parent = self
            self.af.name = 'af'


        class Af(object):
            """
            Operational data for given Address Family
            
            .. attribute:: af_name  <key>
            
            	Address Family name
            	**type**\:   :py:class:`TcOperAfNameEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TcOperAfNameEnum>`
            
            .. attribute:: counters
            
            	Show Counters
            	**type**\:   :py:class:`Counters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af.Counters>`
            
            

            """

            _prefix = 'infra-tc-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.af_name = None
                self.counters = TrafficCollector.Afs.Af.Counters()
                self.counters.parent = self


            class Counters(object):
                """
                Show Counters
                
                .. attribute:: prefixes
                
                	Prefix Database
                	**type**\:   :py:class:`Prefixes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af.Counters.Prefixes>`
                
                .. attribute:: tunnels
                
                	Tunnels
                	**type**\:   :py:class:`Tunnels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af.Counters.Tunnels>`
                
                

                """

                _prefix = 'infra-tc-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.prefixes = TrafficCollector.Afs.Af.Counters.Prefixes()
                    self.prefixes.parent = self
                    self.tunnels = TrafficCollector.Afs.Af.Counters.Tunnels()
                    self.tunnels.parent = self


                class Prefixes(object):
                    """
                    Prefix Database
                    
                    .. attribute:: prefix
                    
                    	Show Prefix Counter
                    	**type**\: list of    :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af.Counters.Prefixes.Prefix>`
                    
                    

                    """

                    _prefix = 'infra-tc-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.prefix = YList()
                        self.prefix.parent = self
                        self.prefix.name = 'prefix'


                    class Prefix(object):
                        """
                        Show Prefix Counter
                        
                        .. attribute:: base_counter_statistics
                        
                        	Base counter statistics
                        	**type**\:   :py:class:`BaseCounterStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics>`
                        
                        .. attribute:: ipaddr
                        
                        	IP Address
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: is_active
                        
                        	Prefix is Active and collecting new Statistics
                        	**type**\:  bool
                        
                        .. attribute:: label
                        
                        	Local Label
                        	**type**\:  int
                        
                        	**range:** 16..1048575
                        
                        .. attribute:: label_xr
                        
                        	Label
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mask
                        
                        	Prefix Mask
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: prefix
                        
                        	Prefix Address (V4 or V6 Format)
                        	**type**\:  str
                        
                        .. attribute:: traffic_matrix_counter_statistics
                        
                        	Traffic Matrix (TM) counter statistics
                        	**type**\:   :py:class:`TrafficMatrixCounterStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics>`
                        
                        

                        """

                        _prefix = 'infra-tc-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.base_counter_statistics = TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics()
                            self.base_counter_statistics.parent = self
                            self.ipaddr = None
                            self.is_active = None
                            self.label = None
                            self.label_xr = None
                            self.mask = None
                            self.prefix = None
                            self.traffic_matrix_counter_statistics = TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics()
                            self.traffic_matrix_counter_statistics.parent = self


                        class BaseCounterStatistics(object):
                            """
                            Base counter statistics
                            
                            .. attribute:: count_history
                            
                            	Counter History
                            	**type**\: list of    :py:class:`CountHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics.CountHistory>`
                            
                            .. attribute:: transmit_bytes_per_second_switched
                            
                            	Average Rate of Bytes/second switched
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte/s
                            
                            .. attribute:: transmit_packets_per_second_switched
                            
                            	Average Rate of Packets/second switched
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: packet/s
                            
                            

                            """

                            _prefix = 'infra-tc-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.count_history = YList()
                                self.count_history.parent = self
                                self.count_history.name = 'count_history'
                                self.transmit_bytes_per_second_switched = None
                                self.transmit_packets_per_second_switched = None


                            class CountHistory(object):
                                """
                                Counter History
                                
                                .. attribute:: event_end_timestamp
                                
                                	Event End timestamp
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: event_start_timestamp
                                
                                	Event Start timestamp
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: is_valid
                                
                                	Flag to indicate if this history entry is valid
                                	**type**\:  bool
                                
                                .. attribute:: transmit_number_of_bytes_switched
                                
                                	Number of Bytes switched in this interval
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: byte
                                
                                .. attribute:: transmit_number_of_packets_switched
                                
                                	Number of packets switched in this interval
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'infra-tc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.event_end_timestamp = None
                                    self.event_start_timestamp = None
                                    self.is_valid = None
                                    self.transmit_number_of_bytes_switched = None
                                    self.transmit_number_of_packets_switched = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-infra-tc-oper:count-history'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.event_end_timestamp is not None:
                                        return True

                                    if self.event_start_timestamp is not None:
                                        return True

                                    if self.is_valid is not None:
                                        return True

                                    if self.transmit_number_of_bytes_switched is not None:
                                        return True

                                    if self.transmit_number_of_packets_switched is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_oper as meta
                                    return meta._meta_table['TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics.CountHistory']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-tc-oper:base-counter-statistics'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.count_history is not None:
                                    for child_ref in self.count_history:
                                        if child_ref._has_data():
                                            return True

                                if self.transmit_bytes_per_second_switched is not None:
                                    return True

                                if self.transmit_packets_per_second_switched is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_oper as meta
                                return meta._meta_table['TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics']['meta_info']


                        class TrafficMatrixCounterStatistics(object):
                            """
                            Traffic Matrix (TM) counter statistics
                            
                            .. attribute:: count_history
                            
                            	Counter History
                            	**type**\: list of    :py:class:`CountHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics.CountHistory>`
                            
                            .. attribute:: transmit_bytes_per_second_switched
                            
                            	Average Rate of Bytes/second switched
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte/s
                            
                            .. attribute:: transmit_packets_per_second_switched
                            
                            	Average Rate of Packets/second switched
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: packet/s
                            
                            

                            """

                            _prefix = 'infra-tc-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.count_history = YList()
                                self.count_history.parent = self
                                self.count_history.name = 'count_history'
                                self.transmit_bytes_per_second_switched = None
                                self.transmit_packets_per_second_switched = None


                            class CountHistory(object):
                                """
                                Counter History
                                
                                .. attribute:: event_end_timestamp
                                
                                	Event End timestamp
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: event_start_timestamp
                                
                                	Event Start timestamp
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: is_valid
                                
                                	Flag to indicate if this history entry is valid
                                	**type**\:  bool
                                
                                .. attribute:: transmit_number_of_bytes_switched
                                
                                	Number of Bytes switched in this interval
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: byte
                                
                                .. attribute:: transmit_number_of_packets_switched
                                
                                	Number of packets switched in this interval
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'infra-tc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.event_end_timestamp = None
                                    self.event_start_timestamp = None
                                    self.is_valid = None
                                    self.transmit_number_of_bytes_switched = None
                                    self.transmit_number_of_packets_switched = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-infra-tc-oper:count-history'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.event_end_timestamp is not None:
                                        return True

                                    if self.event_start_timestamp is not None:
                                        return True

                                    if self.is_valid is not None:
                                        return True

                                    if self.transmit_number_of_bytes_switched is not None:
                                        return True

                                    if self.transmit_number_of_packets_switched is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_oper as meta
                                    return meta._meta_table['TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics.CountHistory']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-tc-oper:traffic-matrix-counter-statistics'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.count_history is not None:
                                    for child_ref in self.count_history:
                                        if child_ref._has_data():
                                            return True

                                if self.transmit_bytes_per_second_switched is not None:
                                    return True

                                if self.transmit_packets_per_second_switched is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_oper as meta
                                return meta._meta_table['TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-tc-oper:prefix'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.base_counter_statistics is not None and self.base_counter_statistics._has_data():
                                return True

                            if self.ipaddr is not None:
                                return True

                            if self.is_active is not None:
                                return True

                            if self.label is not None:
                                return True

                            if self.label_xr is not None:
                                return True

                            if self.mask is not None:
                                return True

                            if self.prefix is not None:
                                return True

                            if self.traffic_matrix_counter_statistics is not None and self.traffic_matrix_counter_statistics._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_oper as meta
                            return meta._meta_table['TrafficCollector.Afs.Af.Counters.Prefixes.Prefix']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-tc-oper:prefixes'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.prefix is not None:
                            for child_ref in self.prefix:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_oper as meta
                        return meta._meta_table['TrafficCollector.Afs.Af.Counters.Prefixes']['meta_info']


                class Tunnels(object):
                    """
                    Tunnels
                    
                    .. attribute:: tunnel
                    
                    	Tunnel information
                    	**type**\: list of    :py:class:`Tunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel>`
                    
                    

                    """

                    _prefix = 'infra-tc-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.tunnel = YList()
                        self.tunnel.parent = self
                        self.tunnel.name = 'tunnel'


                    class Tunnel(object):
                        """
                        Tunnel information
                        
                        .. attribute:: interface_name  <key>
                        
                        	The Interface Name
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: base_counter_statistics
                        
                        	Base counter statistics
                        	**type**\:   :py:class:`BaseCounterStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics>`
                        
                        .. attribute:: interface_handle
                        
                        	Interface handle
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: interface_name_xr
                        
                        	Interface name in Display format
                        	**type**\:  str
                        
                        .. attribute:: is_active
                        
                        	Interface is Active and collecting new Statistics
                        	**type**\:  bool
                        
                        .. attribute:: vrfid
                        
                        	Interface VRF ID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-tc-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.interface_name = None
                            self.base_counter_statistics = TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics()
                            self.base_counter_statistics.parent = self
                            self.interface_handle = None
                            self.interface_name_xr = None
                            self.is_active = None
                            self.vrfid = None


                        class BaseCounterStatistics(object):
                            """
                            Base counter statistics
                            
                            .. attribute:: count_history
                            
                            	Counter History
                            	**type**\: list of    :py:class:`CountHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics.CountHistory>`
                            
                            .. attribute:: transmit_bytes_per_second_switched
                            
                            	Average Rate of Bytes/second switched
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte/s
                            
                            .. attribute:: transmit_packets_per_second_switched
                            
                            	Average Rate of Packets/second switched
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: packet/s
                            
                            

                            """

                            _prefix = 'infra-tc-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.count_history = YList()
                                self.count_history.parent = self
                                self.count_history.name = 'count_history'
                                self.transmit_bytes_per_second_switched = None
                                self.transmit_packets_per_second_switched = None


                            class CountHistory(object):
                                """
                                Counter History
                                
                                .. attribute:: event_end_timestamp
                                
                                	Event End timestamp
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: event_start_timestamp
                                
                                	Event Start timestamp
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: is_valid
                                
                                	Flag to indicate if this history entry is valid
                                	**type**\:  bool
                                
                                .. attribute:: transmit_number_of_bytes_switched
                                
                                	Number of Bytes switched in this interval
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: byte
                                
                                .. attribute:: transmit_number_of_packets_switched
                                
                                	Number of packets switched in this interval
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'infra-tc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.event_end_timestamp = None
                                    self.event_start_timestamp = None
                                    self.is_valid = None
                                    self.transmit_number_of_bytes_switched = None
                                    self.transmit_number_of_packets_switched = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-infra-tc-oper:count-history'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.event_end_timestamp is not None:
                                        return True

                                    if self.event_start_timestamp is not None:
                                        return True

                                    if self.is_valid is not None:
                                        return True

                                    if self.transmit_number_of_bytes_switched is not None:
                                        return True

                                    if self.transmit_number_of_packets_switched is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_oper as meta
                                    return meta._meta_table['TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics.CountHistory']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-tc-oper:base-counter-statistics'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.count_history is not None:
                                    for child_ref in self.count_history:
                                        if child_ref._has_data():
                                            return True

                                if self.transmit_bytes_per_second_switched is not None:
                                    return True

                                if self.transmit_packets_per_second_switched is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_oper as meta
                                return meta._meta_table['TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.interface_name is None:
                                raise YPYModelError('Key property interface_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-tc-oper:tunnel[Cisco-IOS-XR-infra-tc-oper:interface-name = ' + str(self.interface_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.interface_name is not None:
                                return True

                            if self.base_counter_statistics is not None and self.base_counter_statistics._has_data():
                                return True

                            if self.interface_handle is not None:
                                return True

                            if self.interface_name_xr is not None:
                                return True

                            if self.is_active is not None:
                                return True

                            if self.vrfid is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_oper as meta
                            return meta._meta_table['TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-tc-oper:tunnels'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.tunnel is not None:
                            for child_ref in self.tunnel:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_oper as meta
                        return meta._meta_table['TrafficCollector.Afs.Af.Counters.Tunnels']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-tc-oper:counters'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.prefixes is not None and self.prefixes._has_data():
                        return True

                    if self.tunnels is not None and self.tunnels._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_oper as meta
                    return meta._meta_table['TrafficCollector.Afs.Af.Counters']['meta_info']

            @property
            def _common_path(self):
                if self.af_name is None:
                    raise YPYModelError('Key property af_name is None')

                return '/Cisco-IOS-XR-infra-tc-oper:traffic-collector/Cisco-IOS-XR-infra-tc-oper:afs/Cisco-IOS-XR-infra-tc-oper:af[Cisco-IOS-XR-infra-tc-oper:af-name = ' + str(self.af_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.af_name is not None:
                    return True

                if self.counters is not None and self.counters._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_oper as meta
                return meta._meta_table['TrafficCollector.Afs.Af']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-tc-oper:traffic-collector/Cisco-IOS-XR-infra-tc-oper:afs'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.af is not None:
                for child_ref in self.af:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_oper as meta
            return meta._meta_table['TrafficCollector.Afs']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-infra-tc-oper:traffic-collector'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.afs is not None and self.afs._has_data():
            return True

        if self.external_interfaces is not None and self.external_interfaces._has_data():
            return True

        if self.summary is not None and self.summary._has_data():
            return True

        if self.vrf_table is not None and self.vrf_table._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_tc_oper as meta
        return meta._meta_table['TrafficCollector']['meta_info']



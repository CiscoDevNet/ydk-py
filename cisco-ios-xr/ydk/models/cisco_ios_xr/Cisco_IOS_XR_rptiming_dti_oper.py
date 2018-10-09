""" Cisco_IOS_XR_rptiming_dti_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR rptiming\-dti package operational data.

This module contains definitions
for the following management objects\:
  dti\-controller\: DTI interface controller status and
    configuration

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class DtiController(Entity):
    """
    DTI interface controller status and configuration
    
    .. attribute:: nodes
    
    	List of nodes applicable to DTI controller
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rptiming_dti_oper.DtiController.Nodes>`
    
    

    """

    _prefix = 'rptiming-dti-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(DtiController, self).__init__()
        self._top_entity = None

        self.yang_name = "dti-controller"
        self.yang_parent_name = "Cisco-IOS-XR-rptiming-dti-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", DtiController.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = DtiController.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-rptiming-dti-oper:dti-controller"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(DtiController, [], name, value)


    class Nodes(Entity):
        """
        List of nodes applicable to DTI controller
        
        .. attribute:: node
        
        	DTI operational data for a single node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rptiming_dti_oper.DtiController.Nodes.Node>`
        
        

        """

        _prefix = 'rptiming-dti-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(DtiController.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "dti-controller"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", DtiController.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-rptiming-dti-oper:dti-controller/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DtiController.Nodes, [], name, value)


        class Node(Entity):
            """
            DTI operational data for a single node
            
            .. attribute:: node_name  (key)
            
            	Node Name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: client
            
            	Display DTI client status
            	**type**\:  :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rptiming_dti_oper.DtiController.Nodes.Node.Client>`
            
            .. attribute:: port
            
            	Display DTI input port status
            	**type**\:  :py:class:`Port <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rptiming_dti_oper.DtiController.Nodes.Node.Port>`
            
            .. attribute:: time_of_day
            
            	Display DTI time\-of\-day status
            	**type**\:  :py:class:`TimeOfDay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rptiming_dti_oper.DtiController.Nodes.Node.TimeOfDay>`
            
            

            """

            _prefix = 'rptiming-dti-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(DtiController.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("client", ("client", DtiController.Nodes.Node.Client)), ("port", ("port", DtiController.Nodes.Node.Port)), ("time-of-day", ("time_of_day", DtiController.Nodes.Node.TimeOfDay))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.client = DtiController.Nodes.Node.Client()
                self.client.parent = self
                self._children_name_map["client"] = "client"

                self.port = DtiController.Nodes.Node.Port()
                self.port.parent = self
                self._children_name_map["port"] = "port"

                self.time_of_day = DtiController.Nodes.Node.TimeOfDay()
                self.time_of_day.parent = self
                self._children_name_map["time_of_day"] = "time-of-day"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-rptiming-dti-oper:dti-controller/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DtiController.Nodes.Node, ['node_name'], name, value)


            class Client(Entity):
                """
                Display DTI client status
                
                .. attribute:: timestamp_comparator_enable
                
                	timestamp comparator enable
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: register_write_enable
                
                	register write enable
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: revertive_mode_enable
                
                	revertive mode enable
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: port_mode_select
                
                	port mode select
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: force_freerun
                
                	force freerun
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: reference_select_port
                
                	reference select port
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: timestamp_sync_detected
                
                	timestamp sync detected
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: reference10mhz_detected
                
                	10Mhz reference detected
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: active_input_port
                
                	active input port
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: client_state
                
                	client state
                	**type**\: str
                
                	**length:** 0..50
                
                

                """

                _prefix = 'rptiming-dti-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(DtiController.Nodes.Node.Client, self).__init__()

                    self.yang_name = "client"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('timestamp_comparator_enable', (YLeaf(YType.str, 'timestamp-comparator-enable'), ['str'])),
                        ('register_write_enable', (YLeaf(YType.str, 'register-write-enable'), ['str'])),
                        ('revertive_mode_enable', (YLeaf(YType.str, 'revertive-mode-enable'), ['str'])),
                        ('port_mode_select', (YLeaf(YType.str, 'port-mode-select'), ['str'])),
                        ('force_freerun', (YLeaf(YType.str, 'force-freerun'), ['str'])),
                        ('reference_select_port', (YLeaf(YType.str, 'reference-select-port'), ['str'])),
                        ('timestamp_sync_detected', (YLeaf(YType.str, 'timestamp-sync-detected'), ['str'])),
                        ('reference10mhz_detected', (YLeaf(YType.str, 'reference10mhz-detected'), ['str'])),
                        ('active_input_port', (YLeaf(YType.str, 'active-input-port'), ['str'])),
                        ('client_state', (YLeaf(YType.str, 'client-state'), ['str'])),
                    ])
                    self.timestamp_comparator_enable = None
                    self.register_write_enable = None
                    self.revertive_mode_enable = None
                    self.port_mode_select = None
                    self.force_freerun = None
                    self.reference_select_port = None
                    self.timestamp_sync_detected = None
                    self.reference10mhz_detected = None
                    self.active_input_port = None
                    self.client_state = None
                    self._segment_path = lambda: "client"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DtiController.Nodes.Node.Client, [u'timestamp_comparator_enable', u'register_write_enable', u'revertive_mode_enable', u'port_mode_select', u'force_freerun', u'reference_select_port', u'timestamp_sync_detected', u'reference10mhz_detected', u'active_input_port', u'client_state'], name, value)


            class Port(Entity):
                """
                Display DTI input port status
                
                .. attribute:: port1_fr_err_rate_greater5_per
                
                	port1 frame error rate greater than 5 percent
                	**type**\: str
                
                	**length:** 0..50
                
                	**units**\: percentage
                
                .. attribute:: port1_fr_err_rate_greater2_per
                
                	port1 frame error rate greater than 2 percent
                	**type**\: str
                
                	**length:** 0..50
                
                	**units**\: percentage
                
                .. attribute:: port1_dti_signal_detected
                
                	port1 DTI signal detected
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: port1_server_timing_source
                
                	port1 server timing source
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: port1_server_type
                
                	port1 server type
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: port1_server_clock_type
                
                	port1 server clock type
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: port1_server_state
                
                	port1 server state
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: port1_client_perf_stable
                
                	port1 client performance stable
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: port1_cable_advance_valid
                
                	port1 cable advance valid
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: port2_fr_err_rate_greater5_per
                
                	port2 frame error rate greater than 5 percent
                	**type**\: str
                
                	**length:** 0..50
                
                	**units**\: percentage
                
                .. attribute:: port2_fr_err_rate_greater2_per
                
                	port2 frame error rate greater than 2 percent
                	**type**\: str
                
                	**length:** 0..50
                
                	**units**\: percentage
                
                .. attribute:: port2_dti_signal_detected
                
                	port2 DTI signal detected
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: port2_server_timing_source
                
                	port2 server timing source
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: port2_server_type
                
                	port2 server type
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: port2_server_clock_type
                
                	port2 server clock type
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: port2_server_state
                
                	port2 server state
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: port2_client_perf_stable
                
                	port2 client performance stable
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: port2_cable_advance_valid
                
                	port2 cable advance valid
                	**type**\: str
                
                	**length:** 0..50
                
                

                """

                _prefix = 'rptiming-dti-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(DtiController.Nodes.Node.Port, self).__init__()

                    self.yang_name = "port"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('port1_fr_err_rate_greater5_per', (YLeaf(YType.str, 'port1-fr-err-rate-greater5-per'), ['str'])),
                        ('port1_fr_err_rate_greater2_per', (YLeaf(YType.str, 'port1-fr-err-rate-greater2-per'), ['str'])),
                        ('port1_dti_signal_detected', (YLeaf(YType.str, 'port1-dti-signal-detected'), ['str'])),
                        ('port1_server_timing_source', (YLeaf(YType.str, 'port1-server-timing-source'), ['str'])),
                        ('port1_server_type', (YLeaf(YType.str, 'port1-server-type'), ['str'])),
                        ('port1_server_clock_type', (YLeaf(YType.str, 'port1-server-clock-type'), ['str'])),
                        ('port1_server_state', (YLeaf(YType.str, 'port1-server-state'), ['str'])),
                        ('port1_client_perf_stable', (YLeaf(YType.str, 'port1-client-perf-stable'), ['str'])),
                        ('port1_cable_advance_valid', (YLeaf(YType.str, 'port1-cable-advance-valid'), ['str'])),
                        ('port2_fr_err_rate_greater5_per', (YLeaf(YType.str, 'port2-fr-err-rate-greater5-per'), ['str'])),
                        ('port2_fr_err_rate_greater2_per', (YLeaf(YType.str, 'port2-fr-err-rate-greater2-per'), ['str'])),
                        ('port2_dti_signal_detected', (YLeaf(YType.str, 'port2-dti-signal-detected'), ['str'])),
                        ('port2_server_timing_source', (YLeaf(YType.str, 'port2-server-timing-source'), ['str'])),
                        ('port2_server_type', (YLeaf(YType.str, 'port2-server-type'), ['str'])),
                        ('port2_server_clock_type', (YLeaf(YType.str, 'port2-server-clock-type'), ['str'])),
                        ('port2_server_state', (YLeaf(YType.str, 'port2-server-state'), ['str'])),
                        ('port2_client_perf_stable', (YLeaf(YType.str, 'port2-client-perf-stable'), ['str'])),
                        ('port2_cable_advance_valid', (YLeaf(YType.str, 'port2-cable-advance-valid'), ['str'])),
                    ])
                    self.port1_fr_err_rate_greater5_per = None
                    self.port1_fr_err_rate_greater2_per = None
                    self.port1_dti_signal_detected = None
                    self.port1_server_timing_source = None
                    self.port1_server_type = None
                    self.port1_server_clock_type = None
                    self.port1_server_state = None
                    self.port1_client_perf_stable = None
                    self.port1_cable_advance_valid = None
                    self.port2_fr_err_rate_greater5_per = None
                    self.port2_fr_err_rate_greater2_per = None
                    self.port2_dti_signal_detected = None
                    self.port2_server_timing_source = None
                    self.port2_server_type = None
                    self.port2_server_clock_type = None
                    self.port2_server_state = None
                    self.port2_client_perf_stable = None
                    self.port2_cable_advance_valid = None
                    self._segment_path = lambda: "port"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DtiController.Nodes.Node.Port, [u'port1_fr_err_rate_greater5_per', u'port1_fr_err_rate_greater2_per', u'port1_dti_signal_detected', u'port1_server_timing_source', u'port1_server_type', u'port1_server_clock_type', u'port1_server_state', u'port1_client_perf_stable', u'port1_cable_advance_valid', u'port2_fr_err_rate_greater5_per', u'port2_fr_err_rate_greater2_per', u'port2_dti_signal_detected', u'port2_server_timing_source', u'port2_server_type', u'port2_server_clock_type', u'port2_server_state', u'port2_client_perf_stable', u'port2_cable_advance_valid'], name, value)


            class TimeOfDay(Entity):
                """
                Display DTI time\-of\-day status
                
                .. attribute:: port1_tod_message_mode
                
                	port1 tod message mode
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: port1_tod_state
                
                	port1 tod state
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: port1_tod_time_setting_mode
                
                	port1 tod time setting mode
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: port1_gps_seconds
                
                	port1 gps seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: port1_leap_seconds
                
                	port1 leap seconds
                	**type**\: int
                
                	**range:** 0..255
                
                	**units**\: second
                
                .. attribute:: port1_calendar_time_valid
                
                	port1 calendar time valid
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: port1_modified_julian_date
                
                	port1 modified julian date
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: port1_date
                
                	port1 date
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: port1_time
                
                	port1 time
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: port1_time_zone_offset
                
                	port1 time zone offset
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: port1_leap_second_indicator
                
                	port1 leap second indicator
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: port2_tod_message_mode
                
                	port2 tod message mode
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: port2_tod_state
                
                	port2 tod state
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: port2_tod_time_setting_mode
                
                	port2 tod time setting mode
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: port2_gps_seconds
                
                	port2 gps seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: port2_leap_seconds
                
                	port2 leap seconds
                	**type**\: int
                
                	**range:** 0..255
                
                	**units**\: second
                
                .. attribute:: port2_calendar_time_valid
                
                	port2 calendar time valid
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: port2_modified_julian_date
                
                	port2 modified julian date
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: port2_date
                
                	port2 date
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: port2_time
                
                	port2 time
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: port2_time_zone_offset
                
                	port2 time zone offset
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: port2_leap_second_indicator
                
                	port2 leap second indicator
                	**type**\: int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'rptiming-dti-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(DtiController.Nodes.Node.TimeOfDay, self).__init__()

                    self.yang_name = "time-of-day"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('port1_tod_message_mode', (YLeaf(YType.str, 'port1-tod-message-mode'), ['str'])),
                        ('port1_tod_state', (YLeaf(YType.str, 'port1-tod-state'), ['str'])),
                        ('port1_tod_time_setting_mode', (YLeaf(YType.str, 'port1-tod-time-setting-mode'), ['str'])),
                        ('port1_gps_seconds', (YLeaf(YType.uint32, 'port1-gps-seconds'), ['int'])),
                        ('port1_leap_seconds', (YLeaf(YType.uint8, 'port1-leap-seconds'), ['int'])),
                        ('port1_calendar_time_valid', (YLeaf(YType.str, 'port1-calendar-time-valid'), ['str'])),
                        ('port1_modified_julian_date', (YLeaf(YType.str, 'port1-modified-julian-date'), ['str'])),
                        ('port1_date', (YLeaf(YType.str, 'port1-date'), ['str'])),
                        ('port1_time', (YLeaf(YType.str, 'port1-time'), ['str'])),
                        ('port1_time_zone_offset', (YLeaf(YType.str, 'port1-time-zone-offset'), ['str'])),
                        ('port1_leap_second_indicator', (YLeaf(YType.uint8, 'port1-leap-second-indicator'), ['int'])),
                        ('port2_tod_message_mode', (YLeaf(YType.str, 'port2-tod-message-mode'), ['str'])),
                        ('port2_tod_state', (YLeaf(YType.str, 'port2-tod-state'), ['str'])),
                        ('port2_tod_time_setting_mode', (YLeaf(YType.str, 'port2-tod-time-setting-mode'), ['str'])),
                        ('port2_gps_seconds', (YLeaf(YType.uint32, 'port2-gps-seconds'), ['int'])),
                        ('port2_leap_seconds', (YLeaf(YType.uint8, 'port2-leap-seconds'), ['int'])),
                        ('port2_calendar_time_valid', (YLeaf(YType.str, 'port2-calendar-time-valid'), ['str'])),
                        ('port2_modified_julian_date', (YLeaf(YType.str, 'port2-modified-julian-date'), ['str'])),
                        ('port2_date', (YLeaf(YType.str, 'port2-date'), ['str'])),
                        ('port2_time', (YLeaf(YType.str, 'port2-time'), ['str'])),
                        ('port2_time_zone_offset', (YLeaf(YType.str, 'port2-time-zone-offset'), ['str'])),
                        ('port2_leap_second_indicator', (YLeaf(YType.uint8, 'port2-leap-second-indicator'), ['int'])),
                    ])
                    self.port1_tod_message_mode = None
                    self.port1_tod_state = None
                    self.port1_tod_time_setting_mode = None
                    self.port1_gps_seconds = None
                    self.port1_leap_seconds = None
                    self.port1_calendar_time_valid = None
                    self.port1_modified_julian_date = None
                    self.port1_date = None
                    self.port1_time = None
                    self.port1_time_zone_offset = None
                    self.port1_leap_second_indicator = None
                    self.port2_tod_message_mode = None
                    self.port2_tod_state = None
                    self.port2_tod_time_setting_mode = None
                    self.port2_gps_seconds = None
                    self.port2_leap_seconds = None
                    self.port2_calendar_time_valid = None
                    self.port2_modified_julian_date = None
                    self.port2_date = None
                    self.port2_time = None
                    self.port2_time_zone_offset = None
                    self.port2_leap_second_indicator = None
                    self._segment_path = lambda: "time-of-day"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DtiController.Nodes.Node.TimeOfDay, [u'port1_tod_message_mode', u'port1_tod_state', u'port1_tod_time_setting_mode', u'port1_gps_seconds', u'port1_leap_seconds', u'port1_calendar_time_valid', u'port1_modified_julian_date', u'port1_date', u'port1_time', u'port1_time_zone_offset', u'port1_leap_second_indicator', u'port2_tod_message_mode', u'port2_tod_state', u'port2_tod_time_setting_mode', u'port2_gps_seconds', u'port2_leap_seconds', u'port2_calendar_time_valid', u'port2_modified_julian_date', u'port2_date', u'port2_time', u'port2_time_zone_offset', u'port2_leap_second_indicator'], name, value)

    def clone_ptr(self):
        self._top_entity = DtiController()
        return self._top_entity


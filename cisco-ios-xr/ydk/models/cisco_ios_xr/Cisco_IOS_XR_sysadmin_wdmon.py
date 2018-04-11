""" Cisco_IOS_XR_sysadmin_wdmon 


"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Wdmon(Entity):
    """
    
    
    .. attribute:: trace
    
    	show traceable processes
    	**type**\: list of  		 :py:class:`Trace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_wdmon.Wdmon.Trace>`
    
    

    """

    _prefix = 'wdmonh'
    _revision = '2017-05-01'

    def __init__(self):
        super(Wdmon, self).__init__()
        self._top_entity = None

        self.yang_name = "wdmon"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-wdmon"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([("trace", ("trace", Wdmon.Trace))])
        self._leafs = OrderedDict()

        self.trace = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-wdmon:wdmon"

    def __setattr__(self, name, value):
        self._perform_setattr(Wdmon, [], name, value)


    class Trace(Entity):
        """
        show traceable processes
        
        .. attribute:: buffer  (key)
        
        	
        	**type**\: str
        
        .. attribute:: location
        
        	
        	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_wdmon.Wdmon.Trace.Location>`
        
        

        """

        _prefix = 'wdmonh'
        _revision = '2017-05-01'

        def __init__(self):
            super(Wdmon.Trace, self).__init__()

            self.yang_name = "trace"
            self.yang_parent_name = "wdmon"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['buffer']
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("location", ("location", Wdmon.Trace.Location))])
            self._leafs = OrderedDict([
                ('buffer', YLeaf(YType.str, 'buffer')),
            ])
            self.buffer = None

            self.location = YList(self)
            self._segment_path = lambda: "trace" + "[buffer='" + str(self.buffer) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-wdmon:wdmon/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Wdmon.Trace, ['buffer'], name, value)


        class Location(Entity):
            """
            
            
            .. attribute:: location_name  (key)
            
            	
            	**type**\: str
            
            .. attribute:: all_options
            
            	
            	**type**\: list of  		 :py:class:`AllOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_wdmon.Wdmon.Trace.Location.AllOptions>`
            
            

            """

            _prefix = 'wdmonh'
            _revision = '2017-05-01'

            def __init__(self):
                super(Wdmon.Trace.Location, self).__init__()

                self.yang_name = "location"
                self.yang_parent_name = "trace"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['location_name']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("all-options", ("all_options", Wdmon.Trace.Location.AllOptions))])
                self._leafs = OrderedDict([
                    ('location_name', YLeaf(YType.str, 'location_name')),
                ])
                self.location_name = None

                self.all_options = YList(self)
                self._segment_path = lambda: "location" + "[location_name='" + str(self.location_name) + "']"

            def __setattr__(self, name, value):
                self._perform_setattr(Wdmon.Trace.Location, ['location_name'], name, value)


            class AllOptions(Entity):
                """
                
                
                .. attribute:: option  (key)
                
                	
                	**type**\: str
                
                .. attribute:: trace_blocks
                
                	
                	**type**\: list of  		 :py:class:`TraceBlocks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_wdmon.Wdmon.Trace.Location.AllOptions.TraceBlocks>`
                
                

                """

                _prefix = 'wdmonh'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Wdmon.Trace.Location.AllOptions, self).__init__()

                    self.yang_name = "all-options"
                    self.yang_parent_name = "location"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['option']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("trace-blocks", ("trace_blocks", Wdmon.Trace.Location.AllOptions.TraceBlocks))])
                    self._leafs = OrderedDict([
                        ('option', YLeaf(YType.str, 'option')),
                    ])
                    self.option = None

                    self.trace_blocks = YList(self)
                    self._segment_path = lambda: "all-options" + "[option='" + str(self.option) + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(Wdmon.Trace.Location.AllOptions, ['option'], name, value)


                class TraceBlocks(Entity):
                    """
                    
                    
                    .. attribute:: data
                    
                    	Trace output block
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'wdmonh'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Wdmon.Trace.Location.AllOptions.TraceBlocks, self).__init__()

                        self.yang_name = "trace-blocks"
                        self.yang_parent_name = "all-options"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('data', YLeaf(YType.str, 'data')),
                        ])
                        self.data = None
                        self._segment_path = lambda: "trace-blocks"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Wdmon.Trace.Location.AllOptions.TraceBlocks, ['data'], name, value)

    def clone_ptr(self):
        self._top_entity = Wdmon()
        return self._top_entity

class WdmonInfo(Entity):
    """
    
    
    .. attribute:: all_locations
    
    	
    	**type**\: list of  		 :py:class:`AllLocations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_wdmon.WdmonInfo.AllLocations>`
    
    

    """

    _prefix = 'wdmonh'
    _revision = '2017-05-01'

    def __init__(self):
        super(WdmonInfo, self).__init__()
        self._top_entity = None

        self.yang_name = "wdmon-info"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-wdmon"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([("all-locations", ("all_locations", WdmonInfo.AllLocations))])
        self._leafs = OrderedDict()

        self.all_locations = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-wdmon:wdmon-info"

    def __setattr__(self, name, value):
        self._perform_setattr(WdmonInfo, [], name, value)


    class AllLocations(Entity):
        """
        
        
        .. attribute:: location  (key)
        
        	
        	**type**\: str
        
        .. attribute:: start_timestamp
        
        	Last start date and time for wdmon
        	**type**\: str
        
        .. attribute:: hushd_timeout
        
        	wdmon/Calv/Hushd liveness timeout
        	**type**\: str
        
        .. attribute:: calv_restart_timeout
        
        	Calvados restart timeout
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: hushd_wd_action_disable
        
        	Hushd WD expire action disable or not
        	**type**\: bool
        
        .. attribute:: hushd_wd_action_timestamp
        
        	Last Hushd WD expire action date and time
        	**type**\: str
        
        .. attribute:: hushd_capi_up
        
        	Hushd CAPI up or not
        	**type**\: bool
        
        .. attribute:: hushd_pending_resp
        
        	Any pending response from Hushd
        	**type**\: bool
        
        .. attribute:: hushd_stop_punching
        
        	Hushd HB punching stopped
        	**type**\: bool
        
        .. attribute:: hushd_capi_up_timestamp
        
        	Last Hushd CAPI up date and time
        	**type**\: str
        
        .. attribute:: hushd_last_hb_resp
        
        	How long ago was last HB response from Hushd
        	**type**\: str
        
        .. attribute:: hushd_num_capi_connects
        
        	Num of Hushd CAPI connects
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: wds_action_disable
        
        	wdmon client timeout action disabled or not
        	**type**\: bool
        
        .. attribute:: wds_action_timestamp
        
        	Last wdmon client timeout action date and time
        	**type**\: str
        
        .. attribute:: wds_restart_timeout
        
        	wdmon client restart timeout
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: wds_liveness_timeout
        
        	wdmon client liveness timeout
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: wds_client_up
        
        	wdmon client is up or not
        	**type**\: bool
        
        .. attribute:: wds_client_pid
        
        	Process ID of the wdmon client
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: wds_client_up_timestamp
        
        	Last wdmon client connect date and time
        	**type**\: str
        
        .. attribute:: wds_client_last_hb
        
        	How long ago was last HB from wdmon client
        	**type**\: str
        
        .. attribute:: wds_client_num_connects
        
        	Total number of client connects
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: wds_num_liveness_timeout
        
        	Total number of client liveness timeouts
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: wds_num_restart_timeout
        
        	Total number of client restart timeouts
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: wds_client_reported_status
        
        	Status reported by wdmon client
        	**type**\: str
        
        

        """

        _prefix = 'wdmonh'
        _revision = '2017-05-01'

        def __init__(self):
            super(WdmonInfo.AllLocations, self).__init__()

            self.yang_name = "all-locations"
            self.yang_parent_name = "wdmon-info"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['location']
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('location', YLeaf(YType.str, 'location')),
                ('start_timestamp', YLeaf(YType.str, 'start-timestamp')),
                ('hushd_timeout', YLeaf(YType.str, 'hushd-timeout')),
                ('calv_restart_timeout', YLeaf(YType.uint32, 'calv-restart-timeout')),
                ('hushd_wd_action_disable', YLeaf(YType.boolean, 'hushd-wd-action-disable')),
                ('hushd_wd_action_timestamp', YLeaf(YType.str, 'hushd-wd-action-timestamp')),
                ('hushd_capi_up', YLeaf(YType.boolean, 'hushd-capi-up')),
                ('hushd_pending_resp', YLeaf(YType.boolean, 'hushd-pending-resp')),
                ('hushd_stop_punching', YLeaf(YType.boolean, 'hushd-stop-punching')),
                ('hushd_capi_up_timestamp', YLeaf(YType.str, 'hushd-capi-up-timestamp')),
                ('hushd_last_hb_resp', YLeaf(YType.str, 'hushd-last-hb-resp')),
                ('hushd_num_capi_connects', YLeaf(YType.uint32, 'hushd-num-capi-connects')),
                ('wds_action_disable', YLeaf(YType.boolean, 'wds-action-disable')),
                ('wds_action_timestamp', YLeaf(YType.str, 'wds-action-timestamp')),
                ('wds_restart_timeout', YLeaf(YType.uint32, 'wds-restart-timeout')),
                ('wds_liveness_timeout', YLeaf(YType.uint32, 'wds-liveness-timeout')),
                ('wds_client_up', YLeaf(YType.boolean, 'wds-client-up')),
                ('wds_client_pid', YLeaf(YType.uint32, 'wds-client-pid')),
                ('wds_client_up_timestamp', YLeaf(YType.str, 'wds-client-up-timestamp')),
                ('wds_client_last_hb', YLeaf(YType.str, 'wds-client-last-hb')),
                ('wds_client_num_connects', YLeaf(YType.uint32, 'wds-client-num-connects')),
                ('wds_num_liveness_timeout', YLeaf(YType.uint32, 'wds-num-liveness-timeout')),
                ('wds_num_restart_timeout', YLeaf(YType.uint32, 'wds-num-restart-timeout')),
                ('wds_client_reported_status', YLeaf(YType.str, 'wds-client-reported-status')),
            ])
            self.location = None
            self.start_timestamp = None
            self.hushd_timeout = None
            self.calv_restart_timeout = None
            self.hushd_wd_action_disable = None
            self.hushd_wd_action_timestamp = None
            self.hushd_capi_up = None
            self.hushd_pending_resp = None
            self.hushd_stop_punching = None
            self.hushd_capi_up_timestamp = None
            self.hushd_last_hb_resp = None
            self.hushd_num_capi_connects = None
            self.wds_action_disable = None
            self.wds_action_timestamp = None
            self.wds_restart_timeout = None
            self.wds_liveness_timeout = None
            self.wds_client_up = None
            self.wds_client_pid = None
            self.wds_client_up_timestamp = None
            self.wds_client_last_hb = None
            self.wds_client_num_connects = None
            self.wds_num_liveness_timeout = None
            self.wds_num_restart_timeout = None
            self.wds_client_reported_status = None
            self._segment_path = lambda: "all-locations" + "[location='" + str(self.location) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-wdmon:wdmon-info/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(WdmonInfo.AllLocations, ['location', 'start_timestamp', 'hushd_timeout', 'calv_restart_timeout', 'hushd_wd_action_disable', 'hushd_wd_action_timestamp', 'hushd_capi_up', 'hushd_pending_resp', 'hushd_stop_punching', 'hushd_capi_up_timestamp', 'hushd_last_hb_resp', 'hushd_num_capi_connects', 'wds_action_disable', 'wds_action_timestamp', 'wds_restart_timeout', 'wds_liveness_timeout', 'wds_client_up', 'wds_client_pid', 'wds_client_up_timestamp', 'wds_client_last_hb', 'wds_client_num_connects', 'wds_num_liveness_timeout', 'wds_num_restart_timeout', 'wds_client_reported_status'], name, value)

    def clone_ptr(self):
        self._top_entity = WdmonInfo()
        return self._top_entity


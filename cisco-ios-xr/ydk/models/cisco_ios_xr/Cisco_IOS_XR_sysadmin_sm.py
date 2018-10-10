""" Cisco_IOS_XR_sysadmin_sm 

This module contains definitions
for the Calvados model objects.

This module contains a collection of YANG
definitions for Cisco IOS\-XR SysAdmin configuration.

This module holds Shelf Management configuration data.

Copyright(c) 2011\-2017 by Cisco Systems, Inc.
All rights reserved.

Copyright (c) 2012\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Oper(Entity):
    """
    
    
    .. attribute:: shelf_mgr
    
    	
    	**type**\:  :py:class:`ShelfMgr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.ShelfMgr>`
    
    .. attribute:: platform
    
    	
    	**type**\:  :py:class:`Platform <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.Platform>`
    
    .. attribute:: chassis
    
    	
    	**type**\:  :py:class:`Chassis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.Chassis>`
    
    .. attribute:: reload
    
    	
    	**type**\:  :py:class:`Reload <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.Reload>`
    
    .. attribute:: reboot_history
    
    	
    	**type**\:  :py:class:`RebootHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.RebootHistory>`
    
    .. attribute:: interface
    
    	
    	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.Interface>`
    
    .. attribute:: reload_vm
    
    	
    	**type**\:  :py:class:`ReloadVm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.ReloadVm>`
    
    .. attribute:: macpool
    
    	
    	**type**\:  :py:class:`Macpool <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.Macpool>`
    
    

    """

    _prefix = 'shelf_sm'
    _revision = '2017-07-22'

    def __init__(self):
        super(Oper, self).__init__()
        self._top_entity = None

        self.yang_name = "oper"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-sm"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("shelf_mgr", ("shelf_mgr", Oper.ShelfMgr)), ("platform", ("platform", Oper.Platform)), ("chassis", ("chassis", Oper.Chassis)), ("reload", ("reload", Oper.Reload)), ("reboot-history", ("reboot_history", Oper.RebootHistory)), ("interface", ("interface", Oper.Interface)), ("reload_vm", ("reload_vm", Oper.ReloadVm)), ("macpool", ("macpool", Oper.Macpool))])
        self._leafs = OrderedDict()

        self.shelf_mgr = Oper.ShelfMgr()
        self.shelf_mgr.parent = self
        self._children_name_map["shelf_mgr"] = "shelf_mgr"

        self.platform = Oper.Platform()
        self.platform.parent = self
        self._children_name_map["platform"] = "platform"

        self.chassis = Oper.Chassis()
        self.chassis.parent = self
        self._children_name_map["chassis"] = "chassis"

        self.reload = Oper.Reload()
        self.reload.parent = self
        self._children_name_map["reload"] = "reload"

        self.reboot_history = Oper.RebootHistory()
        self.reboot_history.parent = self
        self._children_name_map["reboot_history"] = "reboot-history"

        self.reload_vm = Oper.ReloadVm()
        self.reload_vm.parent = self
        self._children_name_map["reload_vm"] = "reload_vm"

        self.macpool = Oper.Macpool()
        self.macpool.parent = self
        self._children_name_map["macpool"] = "macpool"

        self.interface = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-sm:oper"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Oper, [], name, value)


    class ShelfMgr(Entity):
        """
        
        
        .. attribute:: trace
        
        	show traceable processes
        	**type**\: list of  		 :py:class:`Trace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.ShelfMgr.Trace>`
        
        

        """

        _prefix = 'shelf_sm'
        _revision = '2017-07-22'

        def __init__(self):
            super(Oper.ShelfMgr, self).__init__()

            self.yang_name = "shelf_mgr"
            self.yang_parent_name = "oper"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("trace", ("trace", Oper.ShelfMgr.Trace))])
            self._leafs = OrderedDict()

            self.trace = YList(self)
            self._segment_path = lambda: "shelf_mgr"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sm:oper/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Oper.ShelfMgr, [], name, value)


        class Trace(Entity):
            """
            show traceable processes
            
            .. attribute:: buffer  (key)
            
            	
            	**type**\: str
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.ShelfMgr.Trace.Location>`
            
            

            """

            _prefix = 'shelf_sm'
            _revision = '2017-07-22'

            def __init__(self):
                super(Oper.ShelfMgr.Trace, self).__init__()

                self.yang_name = "trace"
                self.yang_parent_name = "shelf_mgr"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['buffer']
                self._child_classes = OrderedDict([("location", ("location", Oper.ShelfMgr.Trace.Location))])
                self._leafs = OrderedDict([
                    ('buffer', (YLeaf(YType.str, 'buffer'), ['str'])),
                ])
                self.buffer = None

                self.location = YList(self)
                self._segment_path = lambda: "trace" + "[buffer='" + str(self.buffer) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sm:oper/shelf_mgr/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Oper.ShelfMgr.Trace, [u'buffer'], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                .. attribute:: all_options
                
                	
                	**type**\: list of  		 :py:class:`AllOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.ShelfMgr.Trace.Location.AllOptions>`
                
                

                """

                _prefix = 'shelf_sm'
                _revision = '2017-07-22'

                def __init__(self):
                    super(Oper.ShelfMgr.Trace.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "trace"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("all-options", ("all_options", Oper.ShelfMgr.Trace.Location.AllOptions))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location_name'), ['str'])),
                    ])
                    self.location_name = None

                    self.all_options = YList(self)
                    self._segment_path = lambda: "location" + "[location_name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Oper.ShelfMgr.Trace.Location, [u'location_name'], name, value)


                class AllOptions(Entity):
                    """
                    
                    
                    .. attribute:: option  (key)
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: trace_blocks
                    
                    	
                    	**type**\: list of  		 :py:class:`TraceBlocks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.ShelfMgr.Trace.Location.AllOptions.TraceBlocks>`
                    
                    

                    """

                    _prefix = 'shelf_sm'
                    _revision = '2017-07-22'

                    def __init__(self):
                        super(Oper.ShelfMgr.Trace.Location.AllOptions, self).__init__()

                        self.yang_name = "all-options"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['option']
                        self._child_classes = OrderedDict([("trace-blocks", ("trace_blocks", Oper.ShelfMgr.Trace.Location.AllOptions.TraceBlocks))])
                        self._leafs = OrderedDict([
                            ('option', (YLeaf(YType.str, 'option'), ['str'])),
                        ])
                        self.option = None

                        self.trace_blocks = YList(self)
                        self._segment_path = lambda: "all-options" + "[option='" + str(self.option) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Oper.ShelfMgr.Trace.Location.AllOptions, [u'option'], name, value)


                    class TraceBlocks(Entity):
                        """
                        
                        
                        .. attribute:: data
                        
                        	Trace output block
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'shelf_sm'
                        _revision = '2017-07-22'

                        def __init__(self):
                            super(Oper.ShelfMgr.Trace.Location.AllOptions.TraceBlocks, self).__init__()

                            self.yang_name = "trace-blocks"
                            self.yang_parent_name = "all-options"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('data', (YLeaf(YType.str, 'data'), ['str'])),
                            ])
                            self.data = None
                            self._segment_path = lambda: "trace-blocks"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Oper.ShelfMgr.Trace.Location.AllOptions.TraceBlocks, [u'data'], name, value)


    class Platform(Entity):
        """
        
        
        .. attribute:: summary
        
        	
        	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.Platform.Summary>`
        
        .. attribute:: detail
        
        	
        	**type**\:  :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.Platform.Detail>`
        
        .. attribute:: slices
        
        	
        	**type**\:  :py:class:`Slices <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.Platform.Slices>`
        
        

        """

        _prefix = 'shelf_sm'
        _revision = '2017-07-22'

        def __init__(self):
            super(Oper.Platform, self).__init__()

            self.yang_name = "platform"
            self.yang_parent_name = "oper"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("summary", ("summary", Oper.Platform.Summary)), ("detail", ("detail", Oper.Platform.Detail)), ("slices", ("slices", Oper.Platform.Slices))])
            self._leafs = OrderedDict()

            self.summary = Oper.Platform.Summary()
            self.summary.parent = self
            self._children_name_map["summary"] = "summary"

            self.detail = Oper.Platform.Detail()
            self.detail.parent = self
            self._children_name_map["detail"] = "detail"

            self.slices = Oper.Platform.Slices()
            self.slices.parent = self
            self._children_name_map["slices"] = "slices"
            self._segment_path = lambda: "platform"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sm:oper/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Oper.Platform, [], name, value)


        class Summary(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.Platform.Summary.Location>`
            
            

            """

            _prefix = 'shelf_sm'
            _revision = '2017-07-22'

            def __init__(self):
                super(Oper.Platform.Summary, self).__init__()

                self.yang_name = "summary"
                self.yang_parent_name = "platform"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", Oper.Platform.Summary.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "summary"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sm:oper/platform/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Oper.Platform.Summary, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                .. attribute:: summary_data
                
                	
                	**type**\:  :py:class:`SummaryData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.Platform.Summary.Location.SummaryData>`
                
                

                """

                _prefix = 'shelf_sm'
                _revision = '2017-07-22'

                def __init__(self):
                    super(Oper.Platform.Summary.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "summary"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['location']
                    self._child_classes = OrderedDict([("summary-data", ("summary_data", Oper.Platform.Summary.Location.SummaryData))])
                    self._leafs = OrderedDict([
                        ('location', (YLeaf(YType.str, 'location'), ['str'])),
                    ])
                    self.location = None

                    self.summary_data = Oper.Platform.Summary.Location.SummaryData()
                    self.summary_data.parent = self
                    self._children_name_map["summary_data"] = "summary-data"
                    self._segment_path = lambda: "location" + "[location='" + str(self.location) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sm:oper/platform/summary/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Oper.Platform.Summary.Location, ['location'], name, value)


                class SummaryData(Entity):
                    """
                    
                    
                    .. attribute:: card_type
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: hw_state
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: sw_state
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: config_state
                    
                    	
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'shelf_sm'
                    _revision = '2017-07-22'

                    def __init__(self):
                        super(Oper.Platform.Summary.Location.SummaryData, self).__init__()

                        self.yang_name = "summary-data"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('card_type', (YLeaf(YType.str, 'card_type'), ['str'])),
                            ('hw_state', (YLeaf(YType.str, 'hw_state'), ['str'])),
                            ('sw_state', (YLeaf(YType.str, 'sw_state'), ['str'])),
                            ('config_state', (YLeaf(YType.str, 'config_state'), ['str'])),
                        ])
                        self.card_type = None
                        self.hw_state = None
                        self.sw_state = None
                        self.config_state = None
                        self._segment_path = lambda: "summary-data"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Oper.Platform.Summary.Location.SummaryData, ['card_type', 'hw_state', 'sw_state', 'config_state'], name, value)


        class Detail(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.Platform.Detail.Location>`
            
            

            """

            _prefix = 'shelf_sm'
            _revision = '2017-07-22'

            def __init__(self):
                super(Oper.Platform.Detail, self).__init__()

                self.yang_name = "detail"
                self.yang_parent_name = "platform"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", Oper.Platform.Detail.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "detail"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sm:oper/platform/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Oper.Platform.Detail, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                .. attribute:: detail_data
                
                	
                	**type**\:  :py:class:`DetailData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.Platform.Detail.Location.DetailData>`
                
                

                """

                _prefix = 'shelf_sm'
                _revision = '2017-07-22'

                def __init__(self):
                    super(Oper.Platform.Detail.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "detail"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['location']
                    self._child_classes = OrderedDict([("detail-data", ("detail_data", Oper.Platform.Detail.Location.DetailData))])
                    self._leafs = OrderedDict([
                        ('location', (YLeaf(YType.str, 'location'), ['str'])),
                    ])
                    self.location = None

                    self.detail_data = Oper.Platform.Detail.Location.DetailData()
                    self.detail_data.parent = self
                    self._children_name_map["detail_data"] = "detail-data"
                    self._segment_path = lambda: "location" + "[location='" + str(self.location) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sm:oper/platform/detail/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Oper.Platform.Detail.Location, ['location'], name, value)


                class DetailData(Entity):
                    """
                    
                    
                    .. attribute:: pid
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: description
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: vid_sn
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: hw_state
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: sw_state
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: config_wordy
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: hw_ver
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: last_event
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: last_ev_reason_str
                    
                    	
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'shelf_sm'
                    _revision = '2017-07-22'

                    def __init__(self):
                        super(Oper.Platform.Detail.Location.DetailData, self).__init__()

                        self.yang_name = "detail-data"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('pid', (YLeaf(YType.str, 'pid'), ['str'])),
                            ('description', (YLeaf(YType.str, 'description'), ['str'])),
                            ('vid_sn', (YLeaf(YType.str, 'vid_sn'), ['str'])),
                            ('hw_state', (YLeaf(YType.str, 'hw_state'), ['str'])),
                            ('sw_state', (YLeaf(YType.str, 'sw_state'), ['str'])),
                            ('config_wordy', (YLeaf(YType.str, 'config_wordy'), ['str'])),
                            ('hw_ver', (YLeaf(YType.str, 'hw_ver'), ['str'])),
                            ('last_event', (YLeaf(YType.str, 'last_event'), ['str'])),
                            ('last_ev_reason_str', (YLeaf(YType.str, 'last_ev_reason_str'), ['str'])),
                        ])
                        self.pid = None
                        self.description = None
                        self.vid_sn = None
                        self.hw_state = None
                        self.sw_state = None
                        self.config_wordy = None
                        self.hw_ver = None
                        self.last_event = None
                        self.last_ev_reason_str = None
                        self._segment_path = lambda: "detail-data"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Oper.Platform.Detail.Location.DetailData, ['pid', 'description', 'vid_sn', 'hw_state', 'sw_state', 'config_wordy', 'hw_ver', 'last_event', 'last_ev_reason_str'], name, value)


        class Slices(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.Platform.Slices.Location>`
            
            

            """

            _prefix = 'shelf_sm'
            _revision = '2017-07-22'

            def __init__(self):
                super(Oper.Platform.Slices, self).__init__()

                self.yang_name = "slices"
                self.yang_parent_name = "platform"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", Oper.Platform.Slices.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "slices"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sm:oper/platform/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Oper.Platform.Slices, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                .. attribute:: slice_values
                
                	
                	**type**\: list of  		 :py:class:`SliceValues <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.Platform.Slices.Location.SliceValues>`
                
                

                """

                _prefix = 'shelf_sm'
                _revision = '2017-07-22'

                def __init__(self):
                    super(Oper.Platform.Slices.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "slices"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['location']
                    self._child_classes = OrderedDict([("slice_values", ("slice_values", Oper.Platform.Slices.Location.SliceValues))])
                    self._leafs = OrderedDict([
                        ('location', (YLeaf(YType.str, 'location'), ['str'])),
                    ])
                    self.location = None

                    self.slice_values = YList(self)
                    self._segment_path = lambda: "location" + "[location='" + str(self.location) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sm:oper/platform/slices/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Oper.Platform.Slices.Location, ['location'], name, value)


                class SliceValues(Entity):
                    """
                    
                    
                    .. attribute:: slice_idx  (key)
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: slice
                    
                    	
                    	**type**\:  :py:class:`Slice <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.Platform.Slices.Location.SliceValues.Slice>`
                    
                    

                    """

                    _prefix = 'shelf_sm'
                    _revision = '2017-07-22'

                    def __init__(self):
                        super(Oper.Platform.Slices.Location.SliceValues, self).__init__()

                        self.yang_name = "slice_values"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['slice_idx']
                        self._child_classes = OrderedDict([("slice", ("slice", Oper.Platform.Slices.Location.SliceValues.Slice))])
                        self._leafs = OrderedDict([
                            ('slice_idx', (YLeaf(YType.uint32, 'slice_idx'), ['int'])),
                        ])
                        self.slice_idx = None

                        self.slice = Oper.Platform.Slices.Location.SliceValues.Slice()
                        self.slice.parent = self
                        self._children_name_map["slice"] = "slice"
                        self._segment_path = lambda: "slice_values" + "[slice_idx='" + str(self.slice_idx) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Oper.Platform.Slices.Location.SliceValues, ['slice_idx'], name, value)


                    class Slice(Entity):
                        """
                        
                        
                        .. attribute:: slice_num
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: admin_state
                        
                        	
                        	**type**\: str
                        
                        .. attribute:: oper_state
                        
                        	
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'shelf_sm'
                        _revision = '2017-07-22'

                        def __init__(self):
                            super(Oper.Platform.Slices.Location.SliceValues.Slice, self).__init__()

                            self.yang_name = "slice"
                            self.yang_parent_name = "slice_values"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('slice_num', (YLeaf(YType.uint32, 'slice_num'), ['int'])),
                                ('admin_state', (YLeaf(YType.str, 'admin_state'), ['str'])),
                                ('oper_state', (YLeaf(YType.str, 'oper_state'), ['str'])),
                            ])
                            self.slice_num = None
                            self.admin_state = None
                            self.oper_state = None
                            self._segment_path = lambda: "slice"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Oper.Platform.Slices.Location.SliceValues.Slice, ['slice_num', 'admin_state', 'oper_state'], name, value)


    class Chassis(Entity):
        """
        
        
        .. attribute:: brief
        
        	
        	**type**\:  :py:class:`Brief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.Chassis.Brief>`
        
        

        """

        _prefix = 'shelf_sm'
        _revision = '2017-07-22'

        def __init__(self):
            super(Oper.Chassis, self).__init__()

            self.yang_name = "chassis"
            self.yang_parent_name = "oper"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("brief", ("brief", Oper.Chassis.Brief))])
            self._leafs = OrderedDict()

            self.brief = Oper.Chassis.Brief()
            self.brief.parent = self
            self._children_name_map["brief"] = "brief"
            self._segment_path = lambda: "chassis"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sm:oper/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Oper.Chassis, [], name, value)


        class Brief(Entity):
            """
            
            
            .. attribute:: chassis_serial
            
            	
            	**type**\: list of  		 :py:class:`ChassisSerial <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.Chassis.Brief.ChassisSerial>`
            
            

            """

            _prefix = 'shelf_sm'
            _revision = '2017-07-22'

            def __init__(self):
                super(Oper.Chassis.Brief, self).__init__()

                self.yang_name = "brief"
                self.yang_parent_name = "chassis"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("chassis_serial", ("chassis_serial", Oper.Chassis.Brief.ChassisSerial))])
                self._leafs = OrderedDict()

                self.chassis_serial = YList(self)
                self._segment_path = lambda: "brief"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sm:oper/chassis/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Oper.Chassis.Brief, [], name, value)


            class ChassisSerial(Entity):
                """
                
                
                .. attribute:: serial_number  (key)
                
                	
                	**type**\: str
                
                .. attribute:: brief_data
                
                	
                	**type**\:  :py:class:`BriefData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.Chassis.Brief.ChassisSerial.BriefData>`
                
                

                """

                _prefix = 'shelf_sm'
                _revision = '2017-07-22'

                def __init__(self):
                    super(Oper.Chassis.Brief.ChassisSerial, self).__init__()

                    self.yang_name = "chassis_serial"
                    self.yang_parent_name = "brief"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['serial_number']
                    self._child_classes = OrderedDict([("brief-data", ("brief_data", Oper.Chassis.Brief.ChassisSerial.BriefData))])
                    self._leafs = OrderedDict([
                        ('serial_number', (YLeaf(YType.str, 'serial_number'), ['str'])),
                    ])
                    self.serial_number = None

                    self.brief_data = Oper.Chassis.Brief.ChassisSerial.BriefData()
                    self.brief_data.parent = self
                    self._children_name_map["brief_data"] = "brief-data"
                    self._segment_path = lambda: "chassis_serial" + "[serial_number='" + str(self.serial_number) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sm:oper/chassis/brief/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Oper.Chassis.Brief.ChassisSerial, ['serial_number'], name, value)


                class BriefData(Entity):
                    """
                    
                    
                    .. attribute:: racknum
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: rack_type
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: rack_state
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: data_plane
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: ctrl_plane
                    
                    	
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'shelf_sm'
                    _revision = '2017-07-22'

                    def __init__(self):
                        super(Oper.Chassis.Brief.ChassisSerial.BriefData, self).__init__()

                        self.yang_name = "brief-data"
                        self.yang_parent_name = "chassis_serial"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('racknum', (YLeaf(YType.str, 'racknum'), ['str'])),
                            ('rack_type', (YLeaf(YType.str, 'rack_type'), ['str'])),
                            ('rack_state', (YLeaf(YType.str, 'rack_state'), ['str'])),
                            ('data_plane', (YLeaf(YType.str, 'data_plane'), ['str'])),
                            ('ctrl_plane', (YLeaf(YType.str, 'ctrl_plane'), ['str'])),
                        ])
                        self.racknum = None
                        self.rack_type = None
                        self.rack_state = None
                        self.data_plane = None
                        self.ctrl_plane = None
                        self._segment_path = lambda: "brief-data"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Oper.Chassis.Brief.ChassisSerial.BriefData, ['racknum', 'rack_type', 'rack_state', 'data_plane', 'ctrl_plane'], name, value)


    class Reload(Entity):
        """
        
        
        .. attribute:: rack
        
        	
        	**type**\:  :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.Reload.Rack>`
        
        

        """

        _prefix = 'shelf_sm'
        _revision = '2017-07-22'

        def __init__(self):
            super(Oper.Reload, self).__init__()

            self.yang_name = "reload"
            self.yang_parent_name = "oper"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rack", ("rack", Oper.Reload.Rack))])
            self._leafs = OrderedDict()

            self.rack = Oper.Reload.Rack()
            self.rack.parent = self
            self._children_name_map["rack"] = "rack"
            self._segment_path = lambda: "reload"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sm:oper/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Oper.Reload, [], name, value)


        class Rack(Entity):
            """
            
            
            .. attribute:: racks
            
            	
            	**type**\: list of  		 :py:class:`Racks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.Reload.Rack.Racks>`
            
            

            """

            _prefix = 'shelf_sm'
            _revision = '2017-07-22'

            def __init__(self):
                super(Oper.Reload.Rack, self).__init__()

                self.yang_name = "rack"
                self.yang_parent_name = "reload"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("racks", ("racks", Oper.Reload.Rack.Racks))])
                self._leafs = OrderedDict()

                self.racks = YList(self)
                self._segment_path = lambda: "rack"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sm:oper/reload/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Oper.Reload.Rack, [], name, value)


            class Racks(Entity):
                """
                
                
                .. attribute:: rack  (key)
                
                	
                	**type**\: str
                
                

                """

                _prefix = 'shelf_sm'
                _revision = '2017-07-22'

                def __init__(self):
                    super(Oper.Reload.Rack.Racks, self).__init__()

                    self.yang_name = "racks"
                    self.yang_parent_name = "rack"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['rack']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('rack', (YLeaf(YType.str, 'rack'), ['str'])),
                    ])
                    self.rack = None
                    self._segment_path = lambda: "racks" + "[rack='" + str(self.rack) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sm:oper/reload/rack/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Oper.Reload.Rack.Racks, ['rack'], name, value)


    class RebootHistory(Entity):
        """
        
        
        .. attribute:: card
        
        	
        	**type**\:  :py:class:`Card <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.RebootHistory.Card>`
        
        .. attribute:: admin_vm
        
        	
        	**type**\:  :py:class:`AdminVm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.RebootHistory.AdminVm>`
        
        .. attribute:: reverse
        
        	
        	**type**\:  :py:class:`Reverse <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.RebootHistory.Reverse>`
        
        

        """

        _prefix = 'shelf_sm'
        _revision = '2017-07-22'

        def __init__(self):
            super(Oper.RebootHistory, self).__init__()

            self.yang_name = "reboot-history"
            self.yang_parent_name = "oper"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("card", ("card", Oper.RebootHistory.Card)), ("admin-vm", ("admin_vm", Oper.RebootHistory.AdminVm)), ("reverse", ("reverse", Oper.RebootHistory.Reverse))])
            self._leafs = OrderedDict()

            self.card = Oper.RebootHistory.Card()
            self.card.parent = self
            self._children_name_map["card"] = "card"

            self.admin_vm = Oper.RebootHistory.AdminVm()
            self.admin_vm.parent = self
            self._children_name_map["admin_vm"] = "admin-vm"

            self.reverse = Oper.RebootHistory.Reverse()
            self.reverse.parent = self
            self._children_name_map["reverse"] = "reverse"
            self._segment_path = lambda: "reboot-history"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sm:oper/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Oper.RebootHistory, [], name, value)


        class Card(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.RebootHistory.Card.Location>`
            
            

            """

            _prefix = 'shelf_sm'
            _revision = '2017-07-22'

            def __init__(self):
                super(Oper.RebootHistory.Card, self).__init__()

                self.yang_name = "card"
                self.yang_parent_name = "reboot-history"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", Oper.RebootHistory.Card.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "card"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sm:oper/reboot-history/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Oper.RebootHistory.Card, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                .. attribute:: events
                
                	
                	**type**\: list of  		 :py:class:`Events <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.RebootHistory.Card.Location.Events>`
                
                

                """

                _prefix = 'shelf_sm'
                _revision = '2017-07-22'

                def __init__(self):
                    super(Oper.RebootHistory.Card.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "card"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['location']
                    self._child_classes = OrderedDict([("events", ("events", Oper.RebootHistory.Card.Location.Events))])
                    self._leafs = OrderedDict([
                        ('location', (YLeaf(YType.str, 'location'), ['str'])),
                    ])
                    self.location = None

                    self.events = YList(self)
                    self._segment_path = lambda: "location" + "[location='" + str(self.location) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sm:oper/reboot-history/card/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Oper.RebootHistory.Card.Location, ['location'], name, value)


                class Events(Entity):
                    """
                    
                    
                    .. attribute:: event_idx  (key)
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: event
                    
                    	
                    	**type**\:  :py:class:`Event <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.RebootHistory.Card.Location.Events.Event>`
                    
                    

                    """

                    _prefix = 'shelf_sm'
                    _revision = '2017-07-22'

                    def __init__(self):
                        super(Oper.RebootHistory.Card.Location.Events, self).__init__()

                        self.yang_name = "events"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['event_idx']
                        self._child_classes = OrderedDict([("event", ("event", Oper.RebootHistory.Card.Location.Events.Event))])
                        self._leafs = OrderedDict([
                            ('event_idx', (YLeaf(YType.uint32, 'event_idx'), ['int'])),
                        ])
                        self.event_idx = None

                        self.event = Oper.RebootHistory.Card.Location.Events.Event()
                        self.event.parent = self
                        self._children_name_map["event"] = "event"
                        self._segment_path = lambda: "events" + "[event_idx='" + str(self.event_idx) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Oper.RebootHistory.Card.Location.Events, ['event_idx'], name, value)


                    class Event(Entity):
                        """
                        
                        
                        .. attribute:: timestamp
                        
                        	
                        	**type**\: str
                        
                        .. attribute:: reason_code
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: reason
                        
                        	
                        	**type**\: str
                        
                        .. attribute:: src_loc
                        
                        	
                        	**type**\: str
                        
                        .. attribute:: src_name
                        
                        	
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'shelf_sm'
                        _revision = '2017-07-22'

                        def __init__(self):
                            super(Oper.RebootHistory.Card.Location.Events.Event, self).__init__()

                            self.yang_name = "event"
                            self.yang_parent_name = "events"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('timestamp', (YLeaf(YType.str, 'timestamp'), ['str'])),
                                ('reason_code', (YLeaf(YType.uint32, 'reason_code'), ['int'])),
                                ('reason', (YLeaf(YType.str, 'reason'), ['str'])),
                                ('src_loc', (YLeaf(YType.str, 'src_loc'), ['str'])),
                                ('src_name', (YLeaf(YType.str, 'src_name'), ['str'])),
                            ])
                            self.timestamp = None
                            self.reason_code = None
                            self.reason = None
                            self.src_loc = None
                            self.src_name = None
                            self._segment_path = lambda: "event"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Oper.RebootHistory.Card.Location.Events.Event, ['timestamp', 'reason_code', 'reason', 'src_loc', 'src_name'], name, value)


        class AdminVm(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.RebootHistory.AdminVm.Location>`
            
            

            """

            _prefix = 'shelf_sm'
            _revision = '2017-07-22'

            def __init__(self):
                super(Oper.RebootHistory.AdminVm, self).__init__()

                self.yang_name = "admin-vm"
                self.yang_parent_name = "reboot-history"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", Oper.RebootHistory.AdminVm.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "admin-vm"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sm:oper/reboot-history/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Oper.RebootHistory.AdminVm, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                .. attribute:: events
                
                	
                	**type**\: list of  		 :py:class:`Events <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.RebootHistory.AdminVm.Location.Events>`
                
                

                """

                _prefix = 'shelf_sm'
                _revision = '2017-07-22'

                def __init__(self):
                    super(Oper.RebootHistory.AdminVm.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "admin-vm"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['location']
                    self._child_classes = OrderedDict([("events", ("events", Oper.RebootHistory.AdminVm.Location.Events))])
                    self._leafs = OrderedDict([
                        ('location', (YLeaf(YType.str, 'location'), ['str'])),
                    ])
                    self.location = None

                    self.events = YList(self)
                    self._segment_path = lambda: "location" + "[location='" + str(self.location) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sm:oper/reboot-history/admin-vm/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Oper.RebootHistory.AdminVm.Location, ['location'], name, value)


                class Events(Entity):
                    """
                    
                    
                    .. attribute:: event_idx  (key)
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: event
                    
                    	
                    	**type**\:  :py:class:`Event <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.RebootHistory.AdminVm.Location.Events.Event>`
                    
                    

                    """

                    _prefix = 'shelf_sm'
                    _revision = '2017-07-22'

                    def __init__(self):
                        super(Oper.RebootHistory.AdminVm.Location.Events, self).__init__()

                        self.yang_name = "events"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['event_idx']
                        self._child_classes = OrderedDict([("event", ("event", Oper.RebootHistory.AdminVm.Location.Events.Event))])
                        self._leafs = OrderedDict([
                            ('event_idx', (YLeaf(YType.uint32, 'event_idx'), ['int'])),
                        ])
                        self.event_idx = None

                        self.event = Oper.RebootHistory.AdminVm.Location.Events.Event()
                        self.event.parent = self
                        self._children_name_map["event"] = "event"
                        self._segment_path = lambda: "events" + "[event_idx='" + str(self.event_idx) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Oper.RebootHistory.AdminVm.Location.Events, ['event_idx'], name, value)


                    class Event(Entity):
                        """
                        
                        
                        .. attribute:: timestamp
                        
                        	
                        	**type**\: str
                        
                        .. attribute:: reason_code
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: reason
                        
                        	
                        	**type**\: str
                        
                        .. attribute:: src_loc
                        
                        	
                        	**type**\: str
                        
                        .. attribute:: src_name
                        
                        	
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'shelf_sm'
                        _revision = '2017-07-22'

                        def __init__(self):
                            super(Oper.RebootHistory.AdminVm.Location.Events.Event, self).__init__()

                            self.yang_name = "event"
                            self.yang_parent_name = "events"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('timestamp', (YLeaf(YType.str, 'timestamp'), ['str'])),
                                ('reason_code', (YLeaf(YType.uint32, 'reason_code'), ['int'])),
                                ('reason', (YLeaf(YType.str, 'reason'), ['str'])),
                                ('src_loc', (YLeaf(YType.str, 'src_loc'), ['str'])),
                                ('src_name', (YLeaf(YType.str, 'src_name'), ['str'])),
                            ])
                            self.timestamp = None
                            self.reason_code = None
                            self.reason = None
                            self.src_loc = None
                            self.src_name = None
                            self._segment_path = lambda: "event"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Oper.RebootHistory.AdminVm.Location.Events.Event, ['timestamp', 'reason_code', 'reason', 'src_loc', 'src_name'], name, value)


        class Reverse(Entity):
            """
            
            
            .. attribute:: card
            
            	
            	**type**\:  :py:class:`Card <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.RebootHistory.Reverse.Card>`
            
            .. attribute:: admin_vm
            
            	
            	**type**\:  :py:class:`AdminVm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.RebootHistory.Reverse.AdminVm>`
            
            

            """

            _prefix = 'shelf_sm'
            _revision = '2017-07-22'

            def __init__(self):
                super(Oper.RebootHistory.Reverse, self).__init__()

                self.yang_name = "reverse"
                self.yang_parent_name = "reboot-history"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("card", ("card", Oper.RebootHistory.Reverse.Card)), ("admin-vm", ("admin_vm", Oper.RebootHistory.Reverse.AdminVm))])
                self._leafs = OrderedDict()

                self.card = Oper.RebootHistory.Reverse.Card()
                self.card.parent = self
                self._children_name_map["card"] = "card"

                self.admin_vm = Oper.RebootHistory.Reverse.AdminVm()
                self.admin_vm.parent = self
                self._children_name_map["admin_vm"] = "admin-vm"
                self._segment_path = lambda: "reverse"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sm:oper/reboot-history/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Oper.RebootHistory.Reverse, [], name, value)


            class Card(Entity):
                """
                
                
                .. attribute:: location
                
                	
                	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.RebootHistory.Reverse.Card.Location>`
                
                

                """

                _prefix = 'shelf_sm'
                _revision = '2017-07-22'

                def __init__(self):
                    super(Oper.RebootHistory.Reverse.Card, self).__init__()

                    self.yang_name = "card"
                    self.yang_parent_name = "reverse"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("location", ("location", Oper.RebootHistory.Reverse.Card.Location))])
                    self._leafs = OrderedDict()

                    self.location = YList(self)
                    self._segment_path = lambda: "card"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sm:oper/reboot-history/reverse/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Oper.RebootHistory.Reverse.Card, [], name, value)


                class Location(Entity):
                    """
                    
                    
                    .. attribute:: location  (key)
                    
                    	
                    	**type**\: str
                    
                    	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                    
                    .. attribute:: events
                    
                    	
                    	**type**\: list of  		 :py:class:`Events <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.RebootHistory.Reverse.Card.Location.Events>`
                    
                    

                    """

                    _prefix = 'shelf_sm'
                    _revision = '2017-07-22'

                    def __init__(self):
                        super(Oper.RebootHistory.Reverse.Card.Location, self).__init__()

                        self.yang_name = "location"
                        self.yang_parent_name = "card"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['location']
                        self._child_classes = OrderedDict([("events", ("events", Oper.RebootHistory.Reverse.Card.Location.Events))])
                        self._leafs = OrderedDict([
                            ('location', (YLeaf(YType.str, 'location'), ['str'])),
                        ])
                        self.location = None

                        self.events = YList(self)
                        self._segment_path = lambda: "location" + "[location='" + str(self.location) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sm:oper/reboot-history/reverse/card/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Oper.RebootHistory.Reverse.Card.Location, ['location'], name, value)


                    class Events(Entity):
                        """
                        
                        
                        .. attribute:: event_idx  (key)
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: event
                        
                        	
                        	**type**\:  :py:class:`Event <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.RebootHistory.Reverse.Card.Location.Events.Event>`
                        
                        

                        """

                        _prefix = 'shelf_sm'
                        _revision = '2017-07-22'

                        def __init__(self):
                            super(Oper.RebootHistory.Reverse.Card.Location.Events, self).__init__()

                            self.yang_name = "events"
                            self.yang_parent_name = "location"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['event_idx']
                            self._child_classes = OrderedDict([("event", ("event", Oper.RebootHistory.Reverse.Card.Location.Events.Event))])
                            self._leafs = OrderedDict([
                                ('event_idx', (YLeaf(YType.uint32, 'event_idx'), ['int'])),
                            ])
                            self.event_idx = None

                            self.event = Oper.RebootHistory.Reverse.Card.Location.Events.Event()
                            self.event.parent = self
                            self._children_name_map["event"] = "event"
                            self._segment_path = lambda: "events" + "[event_idx='" + str(self.event_idx) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Oper.RebootHistory.Reverse.Card.Location.Events, ['event_idx'], name, value)


                        class Event(Entity):
                            """
                            
                            
                            .. attribute:: timestamp
                            
                            	
                            	**type**\: str
                            
                            .. attribute:: reason_code
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: reason
                            
                            	
                            	**type**\: str
                            
                            .. attribute:: src_loc
                            
                            	
                            	**type**\: str
                            
                            .. attribute:: src_name
                            
                            	
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'shelf_sm'
                            _revision = '2017-07-22'

                            def __init__(self):
                                super(Oper.RebootHistory.Reverse.Card.Location.Events.Event, self).__init__()

                                self.yang_name = "event"
                                self.yang_parent_name = "events"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('timestamp', (YLeaf(YType.str, 'timestamp'), ['str'])),
                                    ('reason_code', (YLeaf(YType.uint32, 'reason_code'), ['int'])),
                                    ('reason', (YLeaf(YType.str, 'reason'), ['str'])),
                                    ('src_loc', (YLeaf(YType.str, 'src_loc'), ['str'])),
                                    ('src_name', (YLeaf(YType.str, 'src_name'), ['str'])),
                                ])
                                self.timestamp = None
                                self.reason_code = None
                                self.reason = None
                                self.src_loc = None
                                self.src_name = None
                                self._segment_path = lambda: "event"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Oper.RebootHistory.Reverse.Card.Location.Events.Event, ['timestamp', 'reason_code', 'reason', 'src_loc', 'src_name'], name, value)


            class AdminVm(Entity):
                """
                
                
                .. attribute:: location
                
                	
                	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.RebootHistory.Reverse.AdminVm.Location>`
                
                

                """

                _prefix = 'shelf_sm'
                _revision = '2017-07-22'

                def __init__(self):
                    super(Oper.RebootHistory.Reverse.AdminVm, self).__init__()

                    self.yang_name = "admin-vm"
                    self.yang_parent_name = "reverse"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("location", ("location", Oper.RebootHistory.Reverse.AdminVm.Location))])
                    self._leafs = OrderedDict()

                    self.location = YList(self)
                    self._segment_path = lambda: "admin-vm"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sm:oper/reboot-history/reverse/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Oper.RebootHistory.Reverse.AdminVm, [], name, value)


                class Location(Entity):
                    """
                    
                    
                    .. attribute:: location  (key)
                    
                    	
                    	**type**\: str
                    
                    	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                    
                    .. attribute:: events
                    
                    	
                    	**type**\: list of  		 :py:class:`Events <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.RebootHistory.Reverse.AdminVm.Location.Events>`
                    
                    

                    """

                    _prefix = 'shelf_sm'
                    _revision = '2017-07-22'

                    def __init__(self):
                        super(Oper.RebootHistory.Reverse.AdminVm.Location, self).__init__()

                        self.yang_name = "location"
                        self.yang_parent_name = "admin-vm"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['location']
                        self._child_classes = OrderedDict([("events", ("events", Oper.RebootHistory.Reverse.AdminVm.Location.Events))])
                        self._leafs = OrderedDict([
                            ('location', (YLeaf(YType.str, 'location'), ['str'])),
                        ])
                        self.location = None

                        self.events = YList(self)
                        self._segment_path = lambda: "location" + "[location='" + str(self.location) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sm:oper/reboot-history/reverse/admin-vm/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Oper.RebootHistory.Reverse.AdminVm.Location, ['location'], name, value)


                    class Events(Entity):
                        """
                        
                        
                        .. attribute:: event_idx  (key)
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: event
                        
                        	
                        	**type**\:  :py:class:`Event <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.RebootHistory.Reverse.AdminVm.Location.Events.Event>`
                        
                        

                        """

                        _prefix = 'shelf_sm'
                        _revision = '2017-07-22'

                        def __init__(self):
                            super(Oper.RebootHistory.Reverse.AdminVm.Location.Events, self).__init__()

                            self.yang_name = "events"
                            self.yang_parent_name = "location"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['event_idx']
                            self._child_classes = OrderedDict([("event", ("event", Oper.RebootHistory.Reverse.AdminVm.Location.Events.Event))])
                            self._leafs = OrderedDict([
                                ('event_idx', (YLeaf(YType.uint32, 'event_idx'), ['int'])),
                            ])
                            self.event_idx = None

                            self.event = Oper.RebootHistory.Reverse.AdminVm.Location.Events.Event()
                            self.event.parent = self
                            self._children_name_map["event"] = "event"
                            self._segment_path = lambda: "events" + "[event_idx='" + str(self.event_idx) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Oper.RebootHistory.Reverse.AdminVm.Location.Events, ['event_idx'], name, value)


                        class Event(Entity):
                            """
                            
                            
                            .. attribute:: timestamp
                            
                            	
                            	**type**\: str
                            
                            .. attribute:: reason_code
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: reason
                            
                            	
                            	**type**\: str
                            
                            .. attribute:: src_loc
                            
                            	
                            	**type**\: str
                            
                            .. attribute:: src_name
                            
                            	
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'shelf_sm'
                            _revision = '2017-07-22'

                            def __init__(self):
                                super(Oper.RebootHistory.Reverse.AdminVm.Location.Events.Event, self).__init__()

                                self.yang_name = "event"
                                self.yang_parent_name = "events"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('timestamp', (YLeaf(YType.str, 'timestamp'), ['str'])),
                                    ('reason_code', (YLeaf(YType.uint32, 'reason_code'), ['int'])),
                                    ('reason', (YLeaf(YType.str, 'reason'), ['str'])),
                                    ('src_loc', (YLeaf(YType.str, 'src_loc'), ['str'])),
                                    ('src_name', (YLeaf(YType.str, 'src_name'), ['str'])),
                                ])
                                self.timestamp = None
                                self.reason_code = None
                                self.reason = None
                                self.src_loc = None
                                self.src_name = None
                                self._segment_path = lambda: "event"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Oper.RebootHistory.Reverse.AdminVm.Location.Events.Event, ['timestamp', 'reason_code', 'reason', 'src_loc', 'src_name'], name, value)


    class Interface(Entity):
        """
        
        
        .. attribute:: ifname  (key)
        
        	
        	**type**\: str
        
        .. attribute:: interface_data
        
        	
        	**type**\:  :py:class:`InterfaceData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.Interface.InterfaceData>`
        
        

        """

        _prefix = 'shelf_sm'
        _revision = '2017-07-22'

        def __init__(self):
            super(Oper.Interface, self).__init__()

            self.yang_name = "interface"
            self.yang_parent_name = "oper"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['ifname']
            self._child_classes = OrderedDict([("interface-data", ("interface_data", Oper.Interface.InterfaceData))])
            self._leafs = OrderedDict([
                ('ifname', (YLeaf(YType.str, 'ifname'), ['str'])),
            ])
            self.ifname = None

            self.interface_data = Oper.Interface.InterfaceData()
            self.interface_data.parent = self
            self._children_name_map["interface_data"] = "interface-data"
            self._segment_path = lambda: "interface" + "[ifname='" + str(self.ifname) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sm:oper/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Oper.Interface, ['ifname'], name, value)


        class InterfaceData(Entity):
            """
            
            
            .. attribute:: mac
            
            	
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: ipv4
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: flagstr
            
            	
            	**type**\: str
            
            .. attribute:: port_status
            
            	
            	**type**\: str
            
            .. attribute:: mtu
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: metric
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rx_pak
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rx_errors
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rx_dropped
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rx_overruns
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rx_frame
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tx_pak
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tx_errors
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tx_dropped
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tx_overruns
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tx_carrier
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: collisions
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tx_queuelen
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rx_bytes
            
            	
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: tx_bytes
            
            	
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: intf_num
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'shelf_sm'
            _revision = '2017-07-22'

            def __init__(self):
                super(Oper.Interface.InterfaceData, self).__init__()

                self.yang_name = "interface-data"
                self.yang_parent_name = "interface"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mac', (YLeaf(YType.str, 'mac'), ['str'])),
                    ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                    ('flagstr', (YLeaf(YType.str, 'flagstr'), ['str'])),
                    ('port_status', (YLeaf(YType.str, 'port_status'), ['str'])),
                    ('mtu', (YLeaf(YType.uint32, 'mtu'), ['int'])),
                    ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                    ('rx_pak', (YLeaf(YType.uint32, 'rx_pak'), ['int'])),
                    ('rx_errors', (YLeaf(YType.uint32, 'rx_errors'), ['int'])),
                    ('rx_dropped', (YLeaf(YType.uint32, 'rx_dropped'), ['int'])),
                    ('rx_overruns', (YLeaf(YType.uint32, 'rx_overruns'), ['int'])),
                    ('rx_frame', (YLeaf(YType.uint32, 'rx_frame'), ['int'])),
                    ('tx_pak', (YLeaf(YType.uint32, 'tx_pak'), ['int'])),
                    ('tx_errors', (YLeaf(YType.uint32, 'tx_errors'), ['int'])),
                    ('tx_dropped', (YLeaf(YType.uint32, 'tx_dropped'), ['int'])),
                    ('tx_overruns', (YLeaf(YType.uint32, 'tx_overruns'), ['int'])),
                    ('tx_carrier', (YLeaf(YType.uint32, 'tx_carrier'), ['int'])),
                    ('collisions', (YLeaf(YType.uint32, 'collisions'), ['int'])),
                    ('tx_queuelen', (YLeaf(YType.uint32, 'tx_queuelen'), ['int'])),
                    ('rx_bytes', (YLeaf(YType.uint64, 'rx_bytes'), ['int'])),
                    ('tx_bytes', (YLeaf(YType.uint64, 'tx_bytes'), ['int'])),
                    ('intf_num', (YLeaf(YType.uint32, 'intf_num'), ['int'])),
                ])
                self.mac = None
                self.ipv4 = None
                self.flagstr = None
                self.port_status = None
                self.mtu = None
                self.metric = None
                self.rx_pak = None
                self.rx_errors = None
                self.rx_dropped = None
                self.rx_overruns = None
                self.rx_frame = None
                self.tx_pak = None
                self.tx_errors = None
                self.tx_dropped = None
                self.tx_overruns = None
                self.tx_carrier = None
                self.collisions = None
                self.tx_queuelen = None
                self.rx_bytes = None
                self.tx_bytes = None
                self.intf_num = None
                self._segment_path = lambda: "interface-data"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Oper.Interface.InterfaceData, ['mac', 'ipv4', 'flagstr', 'port_status', 'mtu', 'metric', 'rx_pak', 'rx_errors', 'rx_dropped', 'rx_overruns', 'rx_frame', 'tx_pak', 'tx_errors', 'tx_dropped', 'tx_overruns', 'tx_carrier', 'collisions', 'tx_queuelen', 'rx_bytes', 'tx_bytes', 'intf_num'], name, value)


    class ReloadVm(Entity):
        """
        
        
        .. attribute:: location
        
        	
        	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.ReloadVm.Location>`
        
        

        """

        _prefix = 'shelf_sm'
        _revision = '2017-07-22'

        def __init__(self):
            super(Oper.ReloadVm, self).__init__()

            self.yang_name = "reload_vm"
            self.yang_parent_name = "oper"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("location", ("location", Oper.ReloadVm.Location))])
            self._leafs = OrderedDict()

            self.location = YList(self)
            self._segment_path = lambda: "reload_vm"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sm:oper/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Oper.ReloadVm, [], name, value)


        class Location(Entity):
            """
            
            
            .. attribute:: location  (key)
            
            	
            	**type**\: str
            
            

            """

            _prefix = 'shelf_sm'
            _revision = '2017-07-22'

            def __init__(self):
                super(Oper.ReloadVm.Location, self).__init__()

                self.yang_name = "location"
                self.yang_parent_name = "reload_vm"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['location']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('location', (YLeaf(YType.str, 'location'), ['str'])),
                ])
                self.location = None
                self._segment_path = lambda: "location" + "[location='" + str(self.location) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sm:oper/reload_vm/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Oper.ReloadVm.Location, ['location'], name, value)


    class Macpool(Entity):
        """
        
        
        .. attribute:: brief
        
        	
        	**type**\:  :py:class:`Brief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.Macpool.Brief>`
        
        

        """

        _prefix = 'shelf_sm'
        _revision = '2017-07-22'

        def __init__(self):
            super(Oper.Macpool, self).__init__()

            self.yang_name = "macpool"
            self.yang_parent_name = "oper"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("brief", ("brief", Oper.Macpool.Brief))])
            self._leafs = OrderedDict()

            self.brief = Oper.Macpool.Brief()
            self.brief.parent = self
            self._children_name_map["brief"] = "brief"
            self._segment_path = lambda: "macpool"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sm:oper/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Oper.Macpool, [], name, value)


        class Brief(Entity):
            """
            
            
            .. attribute:: rack
            
            	
            	**type**\: list of  		 :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.Macpool.Brief.Rack>`
            
            

            """

            _prefix = 'shelf_sm'
            _revision = '2017-07-22'

            def __init__(self):
                super(Oper.Macpool.Brief, self).__init__()

                self.yang_name = "brief"
                self.yang_parent_name = "macpool"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("rack", ("rack", Oper.Macpool.Brief.Rack))])
                self._leafs = OrderedDict()

                self.rack = YList(self)
                self._segment_path = lambda: "brief"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sm:oper/macpool/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Oper.Macpool.Brief, [], name, value)


            class Rack(Entity):
                """
                
                
                .. attribute:: serial_number  (key)
                
                	
                	**type**\: str
                
                .. attribute:: brief_data
                
                	
                	**type**\:  :py:class:`BriefData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Oper.Macpool.Brief.Rack.BriefData>`
                
                

                """

                _prefix = 'shelf_sm'
                _revision = '2017-07-22'

                def __init__(self):
                    super(Oper.Macpool.Brief.Rack, self).__init__()

                    self.yang_name = "rack"
                    self.yang_parent_name = "brief"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['serial_number']
                    self._child_classes = OrderedDict([("brief-data", ("brief_data", Oper.Macpool.Brief.Rack.BriefData))])
                    self._leafs = OrderedDict([
                        ('serial_number', (YLeaf(YType.str, 'serial_number'), ['str'])),
                    ])
                    self.serial_number = None

                    self.brief_data = Oper.Macpool.Brief.Rack.BriefData()
                    self.brief_data.parent = self
                    self._children_name_map["brief_data"] = "brief-data"
                    self._segment_path = lambda: "rack" + "[serial_number='" + str(self.serial_number) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sm:oper/macpool/brief/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Oper.Macpool.Brief.Rack, ['serial_number'], name, value)


                class BriefData(Entity):
                    """
                    
                    
                    .. attribute:: racknum
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: mac_base
                    
                    	
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: mac_count
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: is_selected
                    
                    	
                    	**type**\: bool
                    
                    .. attribute:: allocated_count
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'shelf_sm'
                    _revision = '2017-07-22'

                    def __init__(self):
                        super(Oper.Macpool.Brief.Rack.BriefData, self).__init__()

                        self.yang_name = "brief-data"
                        self.yang_parent_name = "rack"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('racknum', (YLeaf(YType.str, 'racknum'), ['str'])),
                            ('mac_base', (YLeaf(YType.str, 'mac_base'), ['str'])),
                            ('mac_count', (YLeaf(YType.uint32, 'mac_count'), ['int'])),
                            ('is_selected', (YLeaf(YType.boolean, 'is_selected'), ['bool'])),
                            ('allocated_count', (YLeaf(YType.uint32, 'allocated_count'), ['int'])),
                        ])
                        self.racknum = None
                        self.mac_base = None
                        self.mac_count = None
                        self.is_selected = None
                        self.allocated_count = None
                        self._segment_path = lambda: "brief-data"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Oper.Macpool.Brief.Rack.BriefData, ['racknum', 'mac_base', 'mac_count', 'is_selected', 'allocated_count'], name, value)

    def clone_ptr(self):
        self._top_entity = Oper()
        return self._top_entity

class Config(Entity):
    """
    
    
    .. attribute:: chassis
    
    	
    	**type**\:  :py:class:`Chassis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Config.Chassis>`
    
    .. attribute:: interface
    
    	
    	**type**\:  :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Config.Interface>`
    
    .. attribute:: domain
    
    	
    	**type**\:  :py:class:`Domain <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Config.Domain>`
    
    .. attribute:: virtual_macaddr_range
    
    	
    	**type**\:  :py:class:`VirtualMacaddrRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Config.VirtualMacaddrRange>`
    
    

    """

    _prefix = 'shelf_sm'
    _revision = '2017-07-22'

    def __init__(self):
        super(Config, self).__init__()
        self._top_entity = None

        self.yang_name = "config"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-sm"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("chassis", ("chassis", Config.Chassis)), ("interface", ("interface", Config.Interface)), ("domain", ("domain", Config.Domain)), ("virtual-macaddr-range", ("virtual_macaddr_range", Config.VirtualMacaddrRange))])
        self._leafs = OrderedDict()

        self.chassis = Config.Chassis()
        self.chassis.parent = self
        self._children_name_map["chassis"] = "chassis"

        self.interface = Config.Interface()
        self.interface.parent = self
        self._children_name_map["interface"] = "interface"

        self.domain = Config.Domain()
        self.domain.parent = self
        self._children_name_map["domain"] = "domain"

        self.virtual_macaddr_range = Config.VirtualMacaddrRange()
        self.virtual_macaddr_range.parent = self
        self._children_name_map["virtual_macaddr_range"] = "virtual-macaddr-range"
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-sm:config"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Config, [], name, value)


    class Chassis(Entity):
        """
        
        
        .. attribute:: serial
        
        	
        	**type**\: list of  		 :py:class:`Serial <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Config.Chassis.Serial>`
        
        

        """

        _prefix = 'shelf_sm'
        _revision = '2017-07-22'

        def __init__(self):
            super(Config.Chassis, self).__init__()

            self.yang_name = "chassis"
            self.yang_parent_name = "config"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("serial", ("serial", Config.Chassis.Serial))])
            self._leafs = OrderedDict()

            self.serial = YList(self)
            self._segment_path = lambda: "chassis"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sm:config/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Config.Chassis, [], name, value)


        class Serial(Entity):
            """
            
            
            .. attribute:: serial  (key)
            
            	
            	**type**\: str
            
            	**mandatory**\: True
            
            .. attribute:: rack
            
            	
            	**type**\: str
            
            	**pattern:** [bB][0\-9]\|[fF][0\-7]\|[0\-9]\|[1][0\-5]\|[2][4][0\-7]
            
            	**mandatory**\: True
            
            

            """

            _prefix = 'shelf_sm'
            _revision = '2017-07-22'

            def __init__(self):
                super(Config.Chassis.Serial, self).__init__()

                self.yang_name = "serial"
                self.yang_parent_name = "chassis"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['serial']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('serial', (YLeaf(YType.str, 'serial'), ['str'])),
                    ('rack', (YLeaf(YType.str, 'rack'), ['str'])),
                ])
                self.serial = None
                self.rack = None
                self._segment_path = lambda: "serial" + "[serial='" + str(self.serial) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sm:config/chassis/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Config.Chassis.Serial, ['serial', 'rack'], name, value)


    class Interface(Entity):
        """
        
        
        .. attribute:: mgmteth
        
        	
        	**type**\:  :py:class:`MgmtEth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Config.Interface.MgmtEth>`
        
        

        """

        _prefix = 'shelf_sm'
        _revision = '2017-07-22'

        def __init__(self):
            super(Config.Interface, self).__init__()

            self.yang_name = "interface"
            self.yang_parent_name = "config"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("MgmtEth", ("mgmteth", Config.Interface.MgmtEth))])
            self._leafs = OrderedDict()

            self.mgmteth = Config.Interface.MgmtEth()
            self.mgmteth.parent = self
            self._children_name_map["mgmteth"] = "MgmtEth"
            self._segment_path = lambda: "interface"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sm:config/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Config.Interface, [], name, value)


        class MgmtEth(Entity):
            """
            
            
            .. attribute:: locport
            
            	
            	**type**\: list of  		 :py:class:`Locport <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Config.Interface.MgmtEth.Locport>`
            
            

            """

            _prefix = 'shelf_sm'
            _revision = '2017-07-22'

            def __init__(self):
                super(Config.Interface.MgmtEth, self).__init__()

                self.yang_name = "MgmtEth"
                self.yang_parent_name = "interface"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("locport", ("locport", Config.Interface.MgmtEth.Locport))])
                self._leafs = OrderedDict()

                self.locport = YList(self)
                self._segment_path = lambda: "MgmtEth"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sm:config/interface/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Config.Interface.MgmtEth, [], name, value)


            class Locport(Entity):
                """
                
                
                .. attribute:: rack  (key)
                
                	
                	**type**\: str
                
                	**pattern:** [fF][0\-7]\|[0\-9]\|[1][0\-5]\|[bB][0\-9]
                
                .. attribute:: slot  (key)
                
                	
                	**type**\: str
                
                	**pattern:** [Rr][Pp][0\-1]\|[Rr][Ss][Pp][0\-1]\|[Ss][Cc][0\-1]\|[cC][bB][0\-9]
                
                .. attribute:: intf  (key)
                
                	
                	**type**\: int
                
                	**range:** 0..None
                
                .. attribute:: port  (key)
                
                	
                	**type**\: int
                
                	**range:** 0..None
                
                .. attribute:: ipv4
                
                	
                	**type**\:  :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Config.Interface.MgmtEth.Locport.Ipv4>`
                
                .. attribute:: shutdown
                
                	
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: mtu
                
                	
                	**type**\: int
                
                	**range:** 48..9000
                
                .. attribute:: default_gw
                
                	
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: arp
                
                	
                	**type**\:  :py:class:`Arp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Config.Interface.MgmtEth.Locport.Arp>`
                
                

                """

                _prefix = 'shelf_sm'
                _revision = '2017-07-22'

                def __init__(self):
                    super(Config.Interface.MgmtEth.Locport, self).__init__()

                    self.yang_name = "locport"
                    self.yang_parent_name = "MgmtEth"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['rack','slot','intf','port']
                    self._child_classes = OrderedDict([("ipv4", ("ipv4", Config.Interface.MgmtEth.Locport.Ipv4)), ("arp", ("arp", Config.Interface.MgmtEth.Locport.Arp))])
                    self._leafs = OrderedDict([
                        ('rack', (YLeaf(YType.str, 'rack'), ['str'])),
                        ('slot', (YLeaf(YType.str, 'slot'), ['str'])),
                        ('intf', (YLeaf(YType.uint32, 'intf'), ['int'])),
                        ('port', (YLeaf(YType.uint32, 'port'), ['int'])),
                        ('shutdown', (YLeaf(YType.empty, 'shutdown'), ['Empty'])),
                        ('mtu', (YLeaf(YType.uint32, 'mtu'), ['int'])),
                        ('default_gw', (YLeaf(YType.str, 'default-gw'), ['str'])),
                    ])
                    self.rack = None
                    self.slot = None
                    self.intf = None
                    self.port = None
                    self.shutdown = None
                    self.mtu = None
                    self.default_gw = None

                    self.ipv4 = Config.Interface.MgmtEth.Locport.Ipv4()
                    self.ipv4.parent = self
                    self._children_name_map["ipv4"] = "ipv4"

                    self.arp = Config.Interface.MgmtEth.Locport.Arp()
                    self.arp.parent = self
                    self._children_name_map["arp"] = "arp"
                    self._segment_path = lambda: "locport" + "[rack='" + str(self.rack) + "']" + "[slot='" + str(self.slot) + "']" + "[intf='" + str(self.intf) + "']" + "[port='" + str(self.port) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sm:config/interface/MgmtEth/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Config.Interface.MgmtEth.Locport, ['rack', 'slot', 'intf', 'port', 'shutdown', 'mtu', 'default_gw'], name, value)


                class Ipv4(Entity):
                    """
                    
                    
                    .. attribute:: address
                    
                    	
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(( (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5]))\|(/([0\-9]+)))
                    
                    

                    """

                    _prefix = 'shelf_sm'
                    _revision = '2017-07-22'

                    def __init__(self):
                        super(Config.Interface.MgmtEth.Locport.Ipv4, self).__init__()

                        self.yang_name = "ipv4"
                        self.yang_parent_name = "locport"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                        ])
                        self.address = None
                        self._segment_path = lambda: "ipv4"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Config.Interface.MgmtEth.Locport.Ipv4, ['address'], name, value)


                class Arp(Entity):
                    """
                    
                    
                    .. attribute:: ip
                    
                    	
                    	**type**\: list of  		 :py:class:`Ip <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Config.Interface.MgmtEth.Locport.Arp.Ip>`
                    
                    

                    """

                    _prefix = 'shelf_sm'
                    _revision = '2017-07-22'

                    def __init__(self):
                        super(Config.Interface.MgmtEth.Locport.Arp, self).__init__()

                        self.yang_name = "arp"
                        self.yang_parent_name = "locport"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("ip", ("ip", Config.Interface.MgmtEth.Locport.Arp.Ip))])
                        self._leafs = OrderedDict()

                        self.ip = YList(self)
                        self._segment_path = lambda: "arp"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Config.Interface.MgmtEth.Locport.Arp, [], name, value)


                    class Ip(Entity):
                        """
                        
                        
                        .. attribute:: ip  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**mandatory**\: True
                        
                        .. attribute:: mac
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'shelf_sm'
                        _revision = '2017-07-22'

                        def __init__(self):
                            super(Config.Interface.MgmtEth.Locport.Arp.Ip, self).__init__()

                            self.yang_name = "ip"
                            self.yang_parent_name = "arp"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['ip']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ip', (YLeaf(YType.str, 'ip'), ['str'])),
                                ('mac', (YLeaf(YType.str, 'mac'), ['str'])),
                            ])
                            self.ip = None
                            self.mac = None
                            self._segment_path = lambda: "ip" + "[ip='" + str(self.ip) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Config.Interface.MgmtEth.Locport.Arp.Ip, ['ip', 'mac'], name, value)


    class Domain(Entity):
        """
        
        
        .. attribute:: name
        
        	
        	**type**\: list of  		 :py:class:`Name <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Config.Domain.Name>`
        
        .. attribute:: name_server
        
        	
        	**type**\: list of  		 :py:class:`NameServer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sm.Config.Domain.NameServer>`
        
        

        """

        _prefix = 'shelf_sm'
        _revision = '2017-07-22'

        def __init__(self):
            super(Config.Domain, self).__init__()

            self.yang_name = "domain"
            self.yang_parent_name = "config"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("name", ("name", Config.Domain.Name)), ("name-server", ("name_server", Config.Domain.NameServer))])
            self._leafs = OrderedDict()

            self.name = YList(self)
            self.name_server = YList(self)
            self._segment_path = lambda: "domain"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sm:config/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Config.Domain, [], name, value)


        class Name(Entity):
            """
            
            
            .. attribute:: name  (key)
            
            	
            	**type**\: str
            
            

            """

            _prefix = 'shelf_sm'
            _revision = '2017-07-22'

            def __init__(self):
                super(Config.Domain.Name, self).__init__()

                self.yang_name = "name"
                self.yang_parent_name = "domain"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                ])
                self.name = None
                self._segment_path = lambda: "name" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sm:config/domain/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Config.Domain.Name, ['name'], name, value)


        class NameServer(Entity):
            """
            
            
            .. attribute:: name_server  (key)
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            

            """

            _prefix = 'shelf_sm'
            _revision = '2017-07-22'

            def __init__(self):
                super(Config.Domain.NameServer, self).__init__()

                self.yang_name = "name-server"
                self.yang_parent_name = "domain"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name_server']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('name_server', (YLeaf(YType.str, 'name-server'), ['str'])),
                ])
                self.name_server = None
                self._segment_path = lambda: "name-server" + "[name-server='" + str(self.name_server) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sm:config/domain/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Config.Domain.NameServer, ['name_server'], name, value)


    class VirtualMacaddrRange(Entity):
        """
        
        
        .. attribute:: base
        
        	
        	**type**\: str
        
        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
        
        .. attribute:: count
        
        	
        	**type**\: int
        
        	**range:** 1..65535
        
        

        """

        _prefix = 'shelf_sm'
        _revision = '2017-07-22'

        def __init__(self):
            super(Config.VirtualMacaddrRange, self).__init__()

            self.yang_name = "virtual-macaddr-range"
            self.yang_parent_name = "config"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('base', (YLeaf(YType.str, 'base'), ['str'])),
                ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
            ])
            self.base = None
            self.count = None
            self._segment_path = lambda: "virtual-macaddr-range"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sm:config/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Config.VirtualMacaddrRange, ['base', 'count'], name, value)

    def clone_ptr(self):
        self._top_entity = Config()
        return self._top_entity

class Actions(Entity):
    """
    
    
    

    """

    _prefix = 'shelf_sm'
    _revision = '2017-07-22'

    def __init__(self):
        super(Actions, self).__init__()
        self._top_entity = None

        self.yang_name = "actions"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-sm"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-sm:actions"
        self._is_frozen = True

    def clone_ptr(self):
        self._top_entity = Actions()
        return self._top_entity


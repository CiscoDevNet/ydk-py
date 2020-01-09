""" Cisco_IOS_XR_sysadmin_time_of_day_timezone 

This module contains definitions
for the Calvados model objects.

This module contains a collection of YANG definitions
for Cisco IOS\-XR syadmin TOD configuration and cli.

This module contains definitions
for the following management objects\:
Time of the Day(TOD) Cli and configuration data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

Copyright (c) 2012\-2018 by Cisco Systems, Inc.
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




class Clock(_Entity_):
    """
    
    
    .. attribute:: timezone
    
    	
    	**type**\:  :py:class:`Timezone <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_time_of_day_timezone.Clock.Timezone>`
    
    

    """

    _prefix = 'timezone'
    _revision = '2016-07-04'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Clock, self).__init__()
        self._top_entity = None

        self.yang_name = "clock"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-time-of-day-timezone"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("timezone", ("timezone", Clock.Timezone))])
        self._leafs = OrderedDict()

        self.timezone = Clock.Timezone()
        self.timezone.parent = self
        self._children_name_map["timezone"] = "timezone"
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-time-of-day-timezone:clock"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Clock, [], name, value)


    class Timezone(_Entity_):
        """
        
        
        .. attribute:: tzname
        
        	
        	**type**\: str
        
        .. attribute:: area
        
        	
        	**type**\: str
        
        

        """

        _prefix = 'timezone'
        _revision = '2016-07-04'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Clock.Timezone, self).__init__()

            self.yang_name = "timezone"
            self.yang_parent_name = "clock"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('tzname', (YLeaf(YType.str, 'tzname'), ['str'])),
                ('area', (YLeaf(YType.str, 'area'), ['str'])),
            ])
            self.tzname = None
            self.area = None
            self._segment_path = lambda: "timezone"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-time-of-day-timezone:clock/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Clock.Timezone, ['tzname', 'area'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_time_of_day_timezone as meta
            return meta._meta_table['Clock.Timezone']['meta_info']

    def clone_ptr(self):
        self._top_entity = Clock()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_time_of_day_timezone as meta
        return meta._meta_table['Clock']['meta_info']


class Trace(_Entity_):
    """
    
    
    .. attribute:: timezone_config
    
    	
    	**type**\:  :py:class:`TimezoneConfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_time_of_day_timezone.Trace.TimezoneConfig>`
    
    	**config**\: False
    
    .. attribute:: timezone_notify
    
    	
    	**type**\:  :py:class:`TimezoneNotify <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_time_of_day_timezone.Trace.TimezoneNotify>`
    
    	**config**\: False
    
    

    """

    _prefix = 'timezone'
    _revision = '2016-07-04'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Trace, self).__init__()
        self._top_entity = None

        self.yang_name = "trace"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-time-of-day-timezone"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("timezone_config", ("timezone_config", Trace.TimezoneConfig)), ("timezone_notify", ("timezone_notify", Trace.TimezoneNotify))])
        self._leafs = OrderedDict()

        self.timezone_config = Trace.TimezoneConfig()
        self.timezone_config.parent = self
        self._children_name_map["timezone_config"] = "timezone_config"

        self.timezone_notify = Trace.TimezoneNotify()
        self.timezone_notify.parent = self
        self._children_name_map["timezone_notify"] = "timezone_notify"
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-time-of-day-timezone:trace"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Trace, [], name, value)


    class TimezoneConfig(_Entity_):
        """
        
        
        .. attribute:: trace
        
        	show traceable processes
        	**type**\: list of  		 :py:class:`Trace_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_time_of_day_timezone.Trace.TimezoneConfig.Trace_>`
        
        	**config**\: False
        
        

        """

        _prefix = 'timezone'
        _revision = '2016-07-04'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Trace.TimezoneConfig, self).__init__()

            self.yang_name = "timezone_config"
            self.yang_parent_name = "trace"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("trace", ("trace", Trace.TimezoneConfig.Trace_))])
            self._leafs = OrderedDict()

            self.trace = YList(self)
            self._segment_path = lambda: "timezone_config"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-time-of-day-timezone:trace/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Trace.TimezoneConfig, [], name, value)


        class Trace_(_Entity_):
            """
            show traceable processes
            
            .. attribute:: buffer  (key)
            
            	
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_time_of_day_timezone.Trace.TimezoneConfig.Trace_.Location>`
            
            	**config**\: False
            
            

            """

            _prefix = 'timezone'
            _revision = '2016-07-04'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Trace.TimezoneConfig.Trace_, self).__init__()

                self.yang_name = "trace"
                self.yang_parent_name = "timezone_config"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['buffer']
                self._child_classes = OrderedDict([("location", ("location", Trace.TimezoneConfig.Trace_.Location))])
                self._leafs = OrderedDict([
                    ('buffer', (YLeaf(YType.str, 'buffer'), ['str'])),
                ])
                self.buffer = None

                self.location = YList(self)
                self._segment_path = lambda: "trace" + "[buffer='" + str(self.buffer) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-time-of-day-timezone:trace/timezone_config/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Trace.TimezoneConfig.Trace_, ['buffer'], name, value)


            class Location(_Entity_):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: all_options
                
                	
                	**type**\: list of  		 :py:class:`AllOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_time_of_day_timezone.Trace.TimezoneConfig.Trace_.Location.AllOptions>`
                
                	**config**\: False
                
                

                """

                _prefix = 'timezone'
                _revision = '2016-07-04'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Trace.TimezoneConfig.Trace_.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "trace"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("all-options", ("all_options", Trace.TimezoneConfig.Trace_.Location.AllOptions))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location_name'), ['str'])),
                    ])
                    self.location_name = None

                    self.all_options = YList(self)
                    self._segment_path = lambda: "location" + "[location_name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Trace.TimezoneConfig.Trace_.Location, ['location_name'], name, value)


                class AllOptions(_Entity_):
                    """
                    
                    
                    .. attribute:: option  (key)
                    
                    	
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: trace_blocks
                    
                    	
                    	**type**\: list of  		 :py:class:`TraceBlocks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_time_of_day_timezone.Trace.TimezoneConfig.Trace_.Location.AllOptions.TraceBlocks>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'timezone'
                    _revision = '2016-07-04'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Trace.TimezoneConfig.Trace_.Location.AllOptions, self).__init__()

                        self.yang_name = "all-options"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['option']
                        self._child_classes = OrderedDict([("trace-blocks", ("trace_blocks", Trace.TimezoneConfig.Trace_.Location.AllOptions.TraceBlocks))])
                        self._leafs = OrderedDict([
                            ('option', (YLeaf(YType.str, 'option'), ['str'])),
                        ])
                        self.option = None

                        self.trace_blocks = YList(self)
                        self._segment_path = lambda: "all-options" + "[option='" + str(self.option) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Trace.TimezoneConfig.Trace_.Location.AllOptions, ['option'], name, value)


                    class TraceBlocks(_Entity_):
                        """
                        
                        
                        .. attribute:: data
                        
                        	Trace output block
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'timezone'
                        _revision = '2016-07-04'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Trace.TimezoneConfig.Trace_.Location.AllOptions.TraceBlocks, self).__init__()

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
                            self._perform_setattr(Trace.TimezoneConfig.Trace_.Location.AllOptions.TraceBlocks, ['data'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_time_of_day_timezone as meta
                            return meta._meta_table['Trace.TimezoneConfig.Trace_.Location.AllOptions.TraceBlocks']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_time_of_day_timezone as meta
                        return meta._meta_table['Trace.TimezoneConfig.Trace_.Location.AllOptions']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_time_of_day_timezone as meta
                    return meta._meta_table['Trace.TimezoneConfig.Trace_.Location']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_time_of_day_timezone as meta
                return meta._meta_table['Trace.TimezoneConfig.Trace_']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_time_of_day_timezone as meta
            return meta._meta_table['Trace.TimezoneConfig']['meta_info']


    class TimezoneNotify(_Entity_):
        """
        
        
        .. attribute:: trace
        
        	show traceable processes
        	**type**\: list of  		 :py:class:`Trace_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_time_of_day_timezone.Trace.TimezoneNotify.Trace_>`
        
        	**config**\: False
        
        

        """

        _prefix = 'timezone'
        _revision = '2016-07-04'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Trace.TimezoneNotify, self).__init__()

            self.yang_name = "timezone_notify"
            self.yang_parent_name = "trace"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("trace", ("trace", Trace.TimezoneNotify.Trace_))])
            self._leafs = OrderedDict()

            self.trace = YList(self)
            self._segment_path = lambda: "timezone_notify"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-time-of-day-timezone:trace/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Trace.TimezoneNotify, [], name, value)


        class Trace_(_Entity_):
            """
            show traceable processes
            
            .. attribute:: buffer  (key)
            
            	
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_time_of_day_timezone.Trace.TimezoneNotify.Trace_.Location>`
            
            	**config**\: False
            
            

            """

            _prefix = 'timezone'
            _revision = '2016-07-04'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Trace.TimezoneNotify.Trace_, self).__init__()

                self.yang_name = "trace"
                self.yang_parent_name = "timezone_notify"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['buffer']
                self._child_classes = OrderedDict([("location", ("location", Trace.TimezoneNotify.Trace_.Location))])
                self._leafs = OrderedDict([
                    ('buffer', (YLeaf(YType.str, 'buffer'), ['str'])),
                ])
                self.buffer = None

                self.location = YList(self)
                self._segment_path = lambda: "trace" + "[buffer='" + str(self.buffer) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-time-of-day-timezone:trace/timezone_notify/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Trace.TimezoneNotify.Trace_, ['buffer'], name, value)


            class Location(_Entity_):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: all_options
                
                	
                	**type**\: list of  		 :py:class:`AllOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_time_of_day_timezone.Trace.TimezoneNotify.Trace_.Location.AllOptions>`
                
                	**config**\: False
                
                

                """

                _prefix = 'timezone'
                _revision = '2016-07-04'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Trace.TimezoneNotify.Trace_.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "trace"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("all-options", ("all_options", Trace.TimezoneNotify.Trace_.Location.AllOptions))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location_name'), ['str'])),
                    ])
                    self.location_name = None

                    self.all_options = YList(self)
                    self._segment_path = lambda: "location" + "[location_name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Trace.TimezoneNotify.Trace_.Location, ['location_name'], name, value)


                class AllOptions(_Entity_):
                    """
                    
                    
                    .. attribute:: option  (key)
                    
                    	
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: trace_blocks
                    
                    	
                    	**type**\: list of  		 :py:class:`TraceBlocks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_time_of_day_timezone.Trace.TimezoneNotify.Trace_.Location.AllOptions.TraceBlocks>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'timezone'
                    _revision = '2016-07-04'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Trace.TimezoneNotify.Trace_.Location.AllOptions, self).__init__()

                        self.yang_name = "all-options"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['option']
                        self._child_classes = OrderedDict([("trace-blocks", ("trace_blocks", Trace.TimezoneNotify.Trace_.Location.AllOptions.TraceBlocks))])
                        self._leafs = OrderedDict([
                            ('option', (YLeaf(YType.str, 'option'), ['str'])),
                        ])
                        self.option = None

                        self.trace_blocks = YList(self)
                        self._segment_path = lambda: "all-options" + "[option='" + str(self.option) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Trace.TimezoneNotify.Trace_.Location.AllOptions, ['option'], name, value)


                    class TraceBlocks(_Entity_):
                        """
                        
                        
                        .. attribute:: data
                        
                        	Trace output block
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'timezone'
                        _revision = '2016-07-04'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Trace.TimezoneNotify.Trace_.Location.AllOptions.TraceBlocks, self).__init__()

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
                            self._perform_setattr(Trace.TimezoneNotify.Trace_.Location.AllOptions.TraceBlocks, ['data'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_time_of_day_timezone as meta
                            return meta._meta_table['Trace.TimezoneNotify.Trace_.Location.AllOptions.TraceBlocks']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_time_of_day_timezone as meta
                        return meta._meta_table['Trace.TimezoneNotify.Trace_.Location.AllOptions']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_time_of_day_timezone as meta
                    return meta._meta_table['Trace.TimezoneNotify.Trace_.Location']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_time_of_day_timezone as meta
                return meta._meta_table['Trace.TimezoneNotify.Trace_']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_time_of_day_timezone as meta
            return meta._meta_table['Trace.TimezoneNotify']['meta_info']

    def clone_ptr(self):
        self._top_entity = Trace()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_time_of_day_timezone as meta
        return meta._meta_table['Trace']['meta_info']



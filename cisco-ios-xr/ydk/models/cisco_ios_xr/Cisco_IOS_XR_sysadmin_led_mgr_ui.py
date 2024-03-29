""" Cisco_IOS_XR_sysadmin_led_mgr_ui 

This module contains definitions
for the Calvados model objects.

This module provides CLI for Status, ATTN, ALARM LED's.

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




class Led(_Entity_):
    """
    Calvados Led Manager Status, Attn, Alarm inventory
    
    .. attribute:: location
    
    	
    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_led_mgr_ui.Led.Location>`
    
    	**config**\: False
    
    .. attribute:: trace
    
    	show traceable processes
    	**type**\: list of  		 :py:class:`Trace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_led_mgr_ui.Led.Trace>`
    
    	**config**\: False
    
    

    """

    _prefix = 'led_mgr'
    _revision = '2017-05-01'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Led, self).__init__()
        self._top_entity = None

        self.yang_name = "led"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-led-mgr-ui"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("location", ("location", Led.Location)), ("trace", ("trace", Led.Trace))])
        self._leafs = OrderedDict()

        self.location = YList(self)
        self.trace = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-led-mgr-ui:led"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Led, [], name, value)


    class Location(_Entity_):
        """
        
        
        .. attribute:: location  (key)
        
        	
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: led_attributes
        
        	
        	**type**\: list of  		 :py:class:`LedAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_led_mgr_ui.Led.Location.LedAttributes>`
        
        	**config**\: False
        
        

        """

        _prefix = 'led_mgr'
        _revision = '2017-05-01'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Led.Location, self).__init__()

            self.yang_name = "location"
            self.yang_parent_name = "led"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['location']
            self._child_classes = OrderedDict([("led_attributes", ("led_attributes", Led.Location.LedAttributes))])
            self._leafs = OrderedDict([
                ('location', (YLeaf(YType.str, 'location'), ['str'])),
            ])
            self.location = None

            self.led_attributes = YList(self)
            self._segment_path = lambda: "location" + "[location='" + str(self.location) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-led-mgr-ui:led/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Led.Location, ['location'], name, value)


        class LedAttributes(_Entity_):
            """
            
            
            .. attribute:: led_name  (key)
            
            	
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: location
            
            	
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: print_header
            
            	
            	**type**\: bool
            
            	**config**\: False
            
            	**default value**\: false
            
            .. attribute:: loc_header
            
            	
            	**type**\: bool
            
            	**config**\: False
            
            	**default value**\: false
            
            .. attribute:: led_mode
            
            	
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: led_color
            
            	
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'led_mgr'
            _revision = '2017-05-01'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Led.Location.LedAttributes, self).__init__()

                self.yang_name = "led_attributes"
                self.yang_parent_name = "location"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['led_name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('led_name', (YLeaf(YType.str, 'led_name'), ['str'])),
                    ('location', (YLeaf(YType.str, 'location'), ['str'])),
                    ('print_header', (YLeaf(YType.boolean, 'print_header'), ['bool'])),
                    ('loc_header', (YLeaf(YType.boolean, 'loc_header'), ['bool'])),
                    ('led_mode', (YLeaf(YType.str, 'led_mode'), ['str'])),
                    ('led_color', (YLeaf(YType.str, 'led_color'), ['str'])),
                ])
                self.led_name = None
                self.location = None
                self.print_header = None
                self.loc_header = None
                self.led_mode = None
                self.led_color = None
                self._segment_path = lambda: "led_attributes" + "[led_name='" + str(self.led_name) + "']"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Led.Location.LedAttributes, ['led_name', 'location', 'print_header', 'loc_header', 'led_mode', 'led_color'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_led_mgr_ui as meta
                return meta._meta_table['Led.Location.LedAttributes']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_led_mgr_ui as meta
            return meta._meta_table['Led.Location']['meta_info']


    class Trace(_Entity_):
        """
        show traceable processes
        
        .. attribute:: buffer  (key)
        
        	
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: location
        
        	
        	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_led_mgr_ui.Led.Trace.Location>`
        
        	**config**\: False
        
        

        """

        _prefix = 'led_mgr'
        _revision = '2017-05-01'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Led.Trace, self).__init__()

            self.yang_name = "trace"
            self.yang_parent_name = "led"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['buffer']
            self._child_classes = OrderedDict([("location", ("location", Led.Trace.Location))])
            self._leafs = OrderedDict([
                ('buffer', (YLeaf(YType.str, 'buffer'), ['str'])),
            ])
            self.buffer = None

            self.location = YList(self)
            self._segment_path = lambda: "trace" + "[buffer='" + str(self.buffer) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-led-mgr-ui:led/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Led.Trace, ['buffer'], name, value)


        class Location(_Entity_):
            """
            
            
            .. attribute:: location_name  (key)
            
            	
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: all_options
            
            	
            	**type**\: list of  		 :py:class:`AllOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_led_mgr_ui.Led.Trace.Location.AllOptions>`
            
            	**config**\: False
            
            

            """

            _prefix = 'led_mgr'
            _revision = '2017-05-01'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Led.Trace.Location, self).__init__()

                self.yang_name = "location"
                self.yang_parent_name = "trace"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['location_name']
                self._child_classes = OrderedDict([("all-options", ("all_options", Led.Trace.Location.AllOptions))])
                self._leafs = OrderedDict([
                    ('location_name', (YLeaf(YType.str, 'location_name'), ['str'])),
                ])
                self.location_name = None

                self.all_options = YList(self)
                self._segment_path = lambda: "location" + "[location_name='" + str(self.location_name) + "']"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Led.Trace.Location, ['location_name'], name, value)


            class AllOptions(_Entity_):
                """
                
                
                .. attribute:: option  (key)
                
                	
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: trace_blocks
                
                	
                	**type**\: list of  		 :py:class:`TraceBlocks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_led_mgr_ui.Led.Trace.Location.AllOptions.TraceBlocks>`
                
                	**config**\: False
                
                

                """

                _prefix = 'led_mgr'
                _revision = '2017-05-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Led.Trace.Location.AllOptions, self).__init__()

                    self.yang_name = "all-options"
                    self.yang_parent_name = "location"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['option']
                    self._child_classes = OrderedDict([("trace-blocks", ("trace_blocks", Led.Trace.Location.AllOptions.TraceBlocks))])
                    self._leafs = OrderedDict([
                        ('option', (YLeaf(YType.str, 'option'), ['str'])),
                    ])
                    self.option = None

                    self.trace_blocks = YList(self)
                    self._segment_path = lambda: "all-options" + "[option='" + str(self.option) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Led.Trace.Location.AllOptions, ['option'], name, value)


                class TraceBlocks(_Entity_):
                    """
                    
                    
                    .. attribute:: data
                    
                    	Trace output block
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'led_mgr'
                    _revision = '2017-05-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Led.Trace.Location.AllOptions.TraceBlocks, self).__init__()

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
                        self._perform_setattr(Led.Trace.Location.AllOptions.TraceBlocks, ['data'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_led_mgr_ui as meta
                        return meta._meta_table['Led.Trace.Location.AllOptions.TraceBlocks']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_led_mgr_ui as meta
                    return meta._meta_table['Led.Trace.Location.AllOptions']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_led_mgr_ui as meta
                return meta._meta_table['Led.Trace.Location']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_led_mgr_ui as meta
            return meta._meta_table['Led.Trace']['meta_info']

    def clone_ptr(self):
        self._top_entity = Led()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_led_mgr_ui as meta
        return meta._meta_table['Led']['meta_info']



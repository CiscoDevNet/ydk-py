""" Cisco_IOS_XR_sysadmin_debug_trace 

This module contains a collection of YANG
definitions for Cisco IOS\-XR SysAdmin configuration.
This module contains definitions
for the following management objects\:
debug\_trace\: Calvados debug trace.

Copyright (c) 2015\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Config(Entity):
    """
    
    
    .. attribute:: debug
    
    	
    	**type**\:  :py:class:`Debug <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_debug_trace.Config.Debug>`
    
    

    """

    _prefix = 'debug_trace'
    _revision = '2017-04-12'

    def __init__(self):
        super(Config, self).__init__()
        self._top_entity = None

        self.yang_name = "config"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-debug-trace"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("debug", ("debug", Config.Debug))])
        self._leafs = OrderedDict()

        self.debug = Config.Debug()
        self.debug.parent = self
        self._children_name_map["debug"] = "debug"
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-debug-trace:config"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Config, [], name, value)


    class Debug(Entity):
        """
        
        
        .. attribute:: trace
        
        	
        	**type**\: list of  		 :py:class:`Trace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_debug_trace.Config.Debug.Trace>`
        
        

        """

        _prefix = 'debug_trace'
        _revision = '2017-04-12'

        def __init__(self):
            super(Config.Debug, self).__init__()

            self.yang_name = "debug"
            self.yang_parent_name = "config"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("trace", ("trace", Config.Debug.Trace))])
            self._leafs = OrderedDict()

            self.trace = YList(self)
            self._segment_path = lambda: "debug"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-debug-trace:config/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Config.Debug, [], name, value)


        class Trace(Entity):
            """
            
            
            .. attribute:: connection_type  (key)
            
            	
            	**type**\: str
            
            .. attribute:: enable
            
            	
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: disable
            
            	
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'debug_trace'
            _revision = '2017-04-12'

            def __init__(self):
                super(Config.Debug.Trace, self).__init__()

                self.yang_name = "trace"
                self.yang_parent_name = "debug"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['connection_type']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('connection_type', (YLeaf(YType.str, 'connection_type'), ['str'])),
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                    ('disable', (YLeaf(YType.empty, 'disable'), ['Empty'])),
                ])
                self.connection_type = None
                self.enable = None
                self.disable = None
                self._segment_path = lambda: "trace" + "[connection_type='" + str(self.connection_type) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-debug-trace:config/debug/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Config.Debug.Trace, ['connection_type', 'enable', 'disable'], name, value)

    def clone_ptr(self):
        self._top_entity = Config()
        return self._top_entity


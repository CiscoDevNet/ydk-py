""" Cisco_IOS_XR_syslog_act 

This module contains a collection of YANG definitions
for Cisco IOS\-XR action package configuration.

This module contains definitions
for the following management objects\:
syslog\: Global Syslog messaging data

Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Logmsg(Entity):
    """
    
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syslog_act.Logmsg.Input>`
    
    

    """

    _prefix = 'syslog-act'
    _revision = '2016-04-17'

    def __init__(self):
        super(Logmsg, self).__init__()
        self._top_entity = None

        self.yang_name = "logmsg"
        self.yang_parent_name = "Cisco-IOS-XR-syslog-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {}

        self.input = Logmsg.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")
        self._segment_path = lambda: "Cisco-IOS-XR-syslog-act:logmsg"


    class Input(Entity):
        """
        
        
        .. attribute:: message
        
        	Message body
        	**type**\:  str
        
        	**mandatory**\: True
        
        .. attribute:: severity
        
        	Set serverity level
        	**type**\:   :py:class:`Severity <ydk.models.ietf.ietf_syslog_types.Severity>`
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'syslog-act'
        _revision = '2016-04-17'

        def __init__(self):
            super(Logmsg.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "logmsg"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.message = YLeaf(YType.str, "message")

            self.severity = YLeaf(YType.enumeration, "severity")
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-syslog-act:logmsg/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Logmsg.Input, ['message', 'severity'], name, value)

    def clone_ptr(self):
        self._top_entity = Logmsg()
        return self._top_entity


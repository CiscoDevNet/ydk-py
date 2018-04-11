""" Cisco_IOS_XR_sysadmin_zapdisk 

This module contains a collection of YANG
definitions for Cisco IOS\-XR Zapdisk module.

This module zapdisk is for factory card reset feature.

Copyright(c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Zapdisk(Entity):
    """
    
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_zapdisk.Zapdisk.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_zapdisk.Zapdisk.Output>`
    
    

    """

    _prefix = 'zapdisk'
    _revision = '2017-05-23'

    def __init__(self):
        super(Zapdisk, self).__init__()
        self._top_entity = None

        self.yang_name = "zapdisk"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-zapdisk"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = Zapdisk.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = Zapdisk.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-zapdisk:zapdisk"


    class Input(Entity):
        """
        
        
        .. attribute:: set
        
        	
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: czapdisk_unset
        
        	
        	**type**\:  :py:class:`CzapdiskUnset <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_zapdisk.Zapdisk.Input.CzapdiskUnset>`
        
        

        """

        _prefix = 'zapdisk'
        _revision = '2017-05-23'

        def __init__(self):
            super(Zapdisk.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "zapdisk"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("czapdisk-unset", ("czapdisk_unset", Zapdisk.Input.CzapdiskUnset))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('set', YLeaf(YType.empty, 'set')),
            ])
            self.set = None

            self.czapdisk_unset = Zapdisk.Input.CzapdiskUnset()
            self.czapdisk_unset.parent = self
            self._children_name_map["czapdisk_unset"] = "czapdisk-unset"
            self._children_yang_names.add("czapdisk-unset")
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-zapdisk:zapdisk/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Zapdisk.Input, ['set'], name, value)


        class CzapdiskUnset(Entity):
            """
            
            
            .. attribute:: unset
            
            	
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'zapdisk'
            _revision = '2017-05-23'

            def __init__(self):
                super(Zapdisk.Input.CzapdiskUnset, self).__init__()

                self.yang_name = "czapdisk-unset"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('unset', YLeaf(YType.empty, 'unset')),
                ])
                self.unset = None
                self._segment_path = lambda: "czapdisk-unset"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-zapdisk:zapdisk/input/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Zapdisk.Input.CzapdiskUnset, ['unset'], name, value)


    class Output(Entity):
        """
        
        
        .. attribute:: result
        
        	
        	**type**\: str
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'zapdisk'
        _revision = '2017-05-23'

        def __init__(self):
            super(Zapdisk.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "zapdisk"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('result', YLeaf(YType.str, 'result')),
            ])
            self.result = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-zapdisk:zapdisk/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Zapdisk.Output, ['result'], name, value)

    def clone_ptr(self):
        self._top_entity = Zapdisk()
        return self._top_entity


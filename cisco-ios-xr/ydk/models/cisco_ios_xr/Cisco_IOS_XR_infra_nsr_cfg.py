""" Cisco_IOS_XR_infra_nsr_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-nsr package configuration.

This module contains definitions
for the following management objects\:
  nsr\: NSR global configuration

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Nsr(Entity):
    """
    NSR global configuration
    
    .. attribute:: process_failure
    
    	Recovery action for process failures on active RP/DRP
    	**type**\:  :py:class:`ProcessFailure <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_nsr_cfg.Nsr.ProcessFailure>`
    
    

    """

    _prefix = 'infra-nsr-cfg'
    _revision = '2017-06-27'

    def __init__(self):
        super(Nsr, self).__init__()
        self._top_entity = None

        self.yang_name = "nsr"
        self.yang_parent_name = "Cisco-IOS-XR-infra-nsr-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("process-failure", ("process_failure", Nsr.ProcessFailure))])
        self._leafs = OrderedDict()

        self.process_failure = Nsr.ProcessFailure()
        self.process_failure.parent = self
        self._children_name_map["process_failure"] = "process-failure"
        self._segment_path = lambda: "Cisco-IOS-XR-infra-nsr-cfg:nsr"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Nsr, [], name, value)


    class ProcessFailure(Entity):
        """
        Recovery action for process failures on active
        RP/DRP
        
        .. attribute:: switchover
        
        	Enable RP/DRP switchover on process failures
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'infra-nsr-cfg'
        _revision = '2017-06-27'

        def __init__(self):
            super(Nsr.ProcessFailure, self).__init__()

            self.yang_name = "process-failure"
            self.yang_parent_name = "nsr"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('switchover', (YLeaf(YType.empty, 'switchover'), ['Empty'])),
            ])
            self.switchover = None
            self._segment_path = lambda: "process-failure"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-nsr-cfg:nsr/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Nsr.ProcessFailure, ['switchover'], name, value)

    def clone_ptr(self):
        self._top_entity = Nsr()
        return self._top_entity


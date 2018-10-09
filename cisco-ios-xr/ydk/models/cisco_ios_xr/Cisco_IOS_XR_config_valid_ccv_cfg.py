""" Cisco_IOS_XR_config_valid_ccv_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR config\-valid\-ccv package configuration.

This module contains definitions
for the following management objects\:
  configurationvalidation\: Configuration for the Configuration
    Validation feature

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Failure(Enum):
    """
    Failure (Enum Class)

    Failure

    .. data:: unsupported = 0

    	Unsupported failure type

    """

    unsupported = Enum.YLeaf(0, "unsupported")


class FailureAction(Enum):
    """
    FailureAction (Enum Class)

    Failure action

    .. data:: report = 1

    	Report this failure type

    """

    report = Enum.YLeaf(1, "report")



class Configurationvalidation(Entity):
    """
    Configuration for the Configuration Validation
    feature
    
    .. attribute:: failure_type_actions
    
    	Table for failure type actions
    	**type**\:  :py:class:`FailureTypeActions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_valid_ccv_cfg.Configurationvalidation.FailureTypeActions>`
    
    .. attribute:: enable
    
    	Enable configuration validation
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    

    """

    _prefix = 'config-valid-ccv-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Configurationvalidation, self).__init__()
        self._top_entity = None

        self.yang_name = "configurationvalidation"
        self.yang_parent_name = "Cisco-IOS-XR-config-valid-ccv-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("failure-type-actions", ("failure_type_actions", Configurationvalidation.FailureTypeActions))])
        self._leafs = OrderedDict([
            ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
        ])
        self.enable = None

        self.failure_type_actions = Configurationvalidation.FailureTypeActions()
        self.failure_type_actions.parent = self
        self._children_name_map["failure_type_actions"] = "failure-type-actions"
        self._segment_path = lambda: "Cisco-IOS-XR-config-valid-ccv-cfg:configurationvalidation"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Configurationvalidation, ['enable'], name, value)


    class FailureTypeActions(Entity):
        """
        Table for failure type actions
        
        .. attribute:: failure_type_action
        
        	Failure type action configuration
        	**type**\: list of  		 :py:class:`FailureTypeAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_valid_ccv_cfg.Configurationvalidation.FailureTypeActions.FailureTypeAction>`
        
        

        """

        _prefix = 'config-valid-ccv-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Configurationvalidation.FailureTypeActions, self).__init__()

            self.yang_name = "failure-type-actions"
            self.yang_parent_name = "configurationvalidation"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("failure-type-action", ("failure_type_action", Configurationvalidation.FailureTypeActions.FailureTypeAction))])
            self._leafs = OrderedDict()

            self.failure_type_action = YList(self)
            self._segment_path = lambda: "failure-type-actions"
            self._absolute_path = lambda: "Cisco-IOS-XR-config-valid-ccv-cfg:configurationvalidation/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Configurationvalidation.FailureTypeActions, [], name, value)


        class FailureTypeAction(Entity):
            """
            Failure type action configuration
            
            .. attribute:: failure  (key)
            
            	Failure type
            	**type**\:  :py:class:`Failure <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_valid_ccv_cfg.Failure>`
            
            .. attribute:: action
            
            	Action configuration for this failure type
            	**type**\:  :py:class:`FailureAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_valid_ccv_cfg.FailureAction>`
            
            

            """

            _prefix = 'config-valid-ccv-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Configurationvalidation.FailureTypeActions.FailureTypeAction, self).__init__()

                self.yang_name = "failure-type-action"
                self.yang_parent_name = "failure-type-actions"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['failure']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('failure', (YLeaf(YType.enumeration, 'failure'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_valid_ccv_cfg', 'Failure', '')])),
                    ('action', (YLeaf(YType.enumeration, 'action'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_valid_ccv_cfg', 'FailureAction', '')])),
                ])
                self.failure = None
                self.action = None
                self._segment_path = lambda: "failure-type-action" + "[failure='" + str(self.failure) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-config-valid-ccv-cfg:configurationvalidation/failure-type-actions/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Configurationvalidation.FailureTypeActions.FailureTypeAction, ['failure', 'action'], name, value)

    def clone_ptr(self):
        self._top_entity = Configurationvalidation()
        return self._top_entity


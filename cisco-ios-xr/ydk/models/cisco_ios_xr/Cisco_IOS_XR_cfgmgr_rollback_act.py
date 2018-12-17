""" Cisco_IOS_XR_cfgmgr_rollback_act 

This module contains a collection of YANG definitions
for Cisco IOS\-XR action package configuration.

Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class RollBackConfigurationLast(Entity):
    """
    Rollback last <n> commits made
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cfgmgr_rollback_act.RollBackConfigurationLast.Input>`
    
    

    """

    _prefix = 'rollback-act'
    _revision = '2016-04-17'

    def __init__(self):
        super(RollBackConfigurationLast, self).__init__()
        self._top_entity = None

        self.yang_name = "roll-back-configuration-last"
        self.yang_parent_name = "Cisco-IOS-XR-cfgmgr-rollback-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = RollBackConfigurationLast.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-cfgmgr-rollback-act:roll-back-configuration-last"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: count
        
        	Number of commits to rollback
        	**type**\: int
        
        	**range:** 1..100
        
        	**mandatory**\: True
        
        .. attribute:: force
        
        	Override commit blocks
        	**type**\: bool
        
        	**default value**\: false
        
        .. attribute:: best_effort
        
        	Rollback via best\-effort operation
        	**type**\: bool
        
        	**default value**\: false
        
        .. attribute:: label
        
        	Assign a label to this rollback
        	**type**\: str
        
        .. attribute:: comment
        
        	Assign a comment to this rollback
        	**type**\: str
        
        

        """

        _prefix = 'rollback-act'
        _revision = '2016-04-17'

        def __init__(self):
            super(RollBackConfigurationLast.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "roll-back-configuration-last"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('count', (YLeaf(YType.int32, 'count'), ['int'])),
                ('force', (YLeaf(YType.boolean, 'force'), ['bool'])),
                ('best_effort', (YLeaf(YType.boolean, 'best-effort'), ['bool'])),
                ('label', (YLeaf(YType.str, 'label'), ['str'])),
                ('comment', (YLeaf(YType.str, 'comment'), ['str'])),
            ])
            self.count = None
            self.force = None
            self.best_effort = None
            self.label = None
            self.comment = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-cfgmgr-rollback-act:roll-back-configuration-last/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RollBackConfigurationLast.Input, ['count', 'force', 'best_effort', 'label', 'comment'], name, value)

    def clone_ptr(self):
        self._top_entity = RollBackConfigurationLast()
        return self._top_entity

class RollBackConfigurationTo(Entity):
    """
    Rollback up to (and including) a specific commit
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cfgmgr_rollback_act.RollBackConfigurationTo.Input>`
    
    

    """

    _prefix = 'rollback-act'
    _revision = '2016-04-17'

    def __init__(self):
        super(RollBackConfigurationTo, self).__init__()
        self._top_entity = None

        self.yang_name = "roll-back-configuration-to"
        self.yang_parent_name = "Cisco-IOS-XR-cfgmgr-rollback-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = RollBackConfigurationTo.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-cfgmgr-rollback-act:roll-back-configuration-to"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: commit_id
        
        	Commit ID
        	**type**\: str
        
        	**mandatory**\: True
        
        .. attribute:: force
        
        	Override commit blocks
        	**type**\: bool
        
        	**default value**\: false
        
        .. attribute:: best_effort
        
        	Rollback via best\-effort operation
        	**type**\: bool
        
        	**default value**\: false
        
        .. attribute:: label
        
        	Assign a label to this rollback
        	**type**\: str
        
        .. attribute:: comment
        
        	Assign a comment to this rollback
        	**type**\: str
        
        

        """

        _prefix = 'rollback-act'
        _revision = '2016-04-17'

        def __init__(self):
            super(RollBackConfigurationTo.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "roll-back-configuration-to"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('commit_id', (YLeaf(YType.str, 'commit-id'), ['str'])),
                ('force', (YLeaf(YType.boolean, 'force'), ['bool'])),
                ('best_effort', (YLeaf(YType.boolean, 'best-effort'), ['bool'])),
                ('label', (YLeaf(YType.str, 'label'), ['str'])),
                ('comment', (YLeaf(YType.str, 'comment'), ['str'])),
            ])
            self.commit_id = None
            self.force = None
            self.best_effort = None
            self.label = None
            self.comment = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-cfgmgr-rollback-act:roll-back-configuration-to/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RollBackConfigurationTo.Input, ['commit_id', 'force', 'best_effort', 'label', 'comment'], name, value)

    def clone_ptr(self):
        self._top_entity = RollBackConfigurationTo()
        return self._top_entity

class RollBackConfigurationToExclude(Entity):
    """
    Rollback up to (and excluding) a specific commit
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cfgmgr_rollback_act.RollBackConfigurationToExclude.Input>`
    
    

    """

    _prefix = 'rollback-act'
    _revision = '2016-04-17'

    def __init__(self):
        super(RollBackConfigurationToExclude, self).__init__()
        self._top_entity = None

        self.yang_name = "roll-back-configuration-to-exclude"
        self.yang_parent_name = "Cisco-IOS-XR-cfgmgr-rollback-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = RollBackConfigurationToExclude.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-cfgmgr-rollback-act:roll-back-configuration-to-exclude"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: commit_id
        
        	Commit ID
        	**type**\: str
        
        	**mandatory**\: True
        
        .. attribute:: force
        
        	Override commit blocks
        	**type**\: bool
        
        	**default value**\: false
        
        .. attribute:: best_effort
        
        	Rollback via best\-effort operation
        	**type**\: bool
        
        	**default value**\: false
        
        .. attribute:: label
        
        	Assign a label to this rollback
        	**type**\: str
        
        .. attribute:: comment
        
        	Assign a comment to this rollback
        	**type**\: str
        
        

        """

        _prefix = 'rollback-act'
        _revision = '2016-04-17'

        def __init__(self):
            super(RollBackConfigurationToExclude.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "roll-back-configuration-to-exclude"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('commit_id', (YLeaf(YType.str, 'commit-id'), ['str'])),
                ('force', (YLeaf(YType.boolean, 'force'), ['bool'])),
                ('best_effort', (YLeaf(YType.boolean, 'best-effort'), ['bool'])),
                ('label', (YLeaf(YType.str, 'label'), ['str'])),
                ('comment', (YLeaf(YType.str, 'comment'), ['str'])),
            ])
            self.commit_id = None
            self.force = None
            self.best_effort = None
            self.label = None
            self.comment = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-cfgmgr-rollback-act:roll-back-configuration-to-exclude/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RollBackConfigurationToExclude.Input, ['commit_id', 'force', 'best_effort', 'label', 'comment'], name, value)

    def clone_ptr(self):
        self._top_entity = RollBackConfigurationToExclude()
        return self._top_entity

class RollBackConfiguration(Entity):
    """
    Rollback a specific commit
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cfgmgr_rollback_act.RollBackConfiguration.Input>`
    
    

    """

    _prefix = 'rollback-act'
    _revision = '2016-04-17'

    def __init__(self):
        super(RollBackConfiguration, self).__init__()
        self._top_entity = None

        self.yang_name = "roll-back-configuration"
        self.yang_parent_name = "Cisco-IOS-XR-cfgmgr-rollback-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = RollBackConfiguration.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-cfgmgr-rollback-act:roll-back-configuration"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: commit_id
        
        	Commit ID
        	**type**\: str
        
        	**mandatory**\: True
        
        .. attribute:: force
        
        	Override commit blocks
        	**type**\: bool
        
        	**default value**\: false
        
        .. attribute:: best_effort
        
        	Rollback via best\-effort operation
        	**type**\: bool
        
        	**default value**\: false
        
        .. attribute:: label
        
        	Assign a label to this rollback
        	**type**\: str
        
        .. attribute:: comment
        
        	Assign a comment to this rollback
        	**type**\: str
        
        

        """

        _prefix = 'rollback-act'
        _revision = '2016-04-17'

        def __init__(self):
            super(RollBackConfiguration.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "roll-back-configuration"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('commit_id', (YLeaf(YType.str, 'commit-id'), ['str'])),
                ('force', (YLeaf(YType.boolean, 'force'), ['bool'])),
                ('best_effort', (YLeaf(YType.boolean, 'best-effort'), ['bool'])),
                ('label', (YLeaf(YType.str, 'label'), ['str'])),
                ('comment', (YLeaf(YType.str, 'comment'), ['str'])),
            ])
            self.commit_id = None
            self.force = None
            self.best_effort = None
            self.label = None
            self.comment = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-cfgmgr-rollback-act:roll-back-configuration/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RollBackConfiguration.Input, ['commit_id', 'force', 'best_effort', 'label', 'comment'], name, value)

    def clone_ptr(self):
        self._top_entity = RollBackConfiguration()
        return self._top_entity


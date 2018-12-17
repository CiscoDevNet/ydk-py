""" Cisco_IOS_XR_lib_keychain_act 

This module contains a collection of YANG definitions
for Cisco IOS\-XR action package configuration.

Copyright (c) 2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class MasterKeyAdd(Entity):
    """
    To add a new master key
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_act.MasterKeyAdd.Input>`
    
    

    """

    _prefix = 'lib-keychain-act'
    _revision = '2017-04-17'

    def __init__(self):
        super(MasterKeyAdd, self).__init__()
        self._top_entity = None

        self.yang_name = "master-key-add"
        self.yang_parent_name = "Cisco-IOS-XR-lib-keychain-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = MasterKeyAdd.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-lib-keychain-act:master-key-add"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: new_key
        
        	New master key to be added
        	**type**\: str
        
        

        """

        _prefix = 'lib-keychain-act'
        _revision = '2017-04-17'

        def __init__(self):
            super(MasterKeyAdd.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "master-key-add"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('new_key', (YLeaf(YType.str, 'new-key'), ['str'])),
            ])
            self.new_key = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-lib-keychain-act:master-key-add/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MasterKeyAdd.Input, ['new_key'], name, value)

    def clone_ptr(self):
        self._top_entity = MasterKeyAdd()
        return self._top_entity

class MasterKeyDelete(Entity):
    """
    Remove Master key
    
    

    """

    _prefix = 'lib-keychain-act'
    _revision = '2017-04-17'

    def __init__(self):
        super(MasterKeyDelete, self).__init__()
        self._top_entity = None

        self.yang_name = "master-key-delete"
        self.yang_parent_name = "Cisco-IOS-XR-lib-keychain-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()
        self._segment_path = lambda: "Cisco-IOS-XR-lib-keychain-act:master-key-delete"
        self._is_frozen = True

    def clone_ptr(self):
        self._top_entity = MasterKeyDelete()
        return self._top_entity

class MasterKeyUpdate(Entity):
    """
    To update master key
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_act.MasterKeyUpdate.Input>`
    
    

    """

    _prefix = 'lib-keychain-act'
    _revision = '2017-04-17'

    def __init__(self):
        super(MasterKeyUpdate, self).__init__()
        self._top_entity = None

        self.yang_name = "master-key-update"
        self.yang_parent_name = "Cisco-IOS-XR-lib-keychain-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = MasterKeyUpdate.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-lib-keychain-act:master-key-update"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: old_key
        
        	key already added/key to be replaced
        	**type**\: str
        
        	**mandatory**\: True
        
        .. attribute:: new_key
        
        	New master key to be added 
        	**type**\: str
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'lib-keychain-act'
        _revision = '2017-04-17'

        def __init__(self):
            super(MasterKeyUpdate.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "master-key-update"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('old_key', (YLeaf(YType.str, 'old-key'), ['str'])),
                ('new_key', (YLeaf(YType.str, 'new-key'), ['str'])),
            ])
            self.old_key = None
            self.new_key = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-lib-keychain-act:master-key-update/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MasterKeyUpdate.Input, ['old_key', 'new_key'], name, value)

    def clone_ptr(self):
        self._top_entity = MasterKeyUpdate()
        return self._top_entity


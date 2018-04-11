""" Cisco_IOS_XR_lib_keychain_masterkey_aes_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR lib\-keychain\-masterkey\-aes package configuration.

This module contains definitions
for the following management objects\:
  password\: Configure masterkey

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Password(Entity):
    """
    Configure masterkey
    
    .. attribute:: encryption
    
    	Enable password encryption
    	**type**\:  :py:class:`Encryption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_masterkey_aes_cfg.Password.Encryption>`
    
    

    """

    _prefix = 'lib-keychain-masterkey-aes-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Password, self).__init__()
        self._top_entity = None

        self.yang_name = "password"
        self.yang_parent_name = "Cisco-IOS-XR-lib-keychain-masterkey-aes-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("encryption", ("encryption", Password.Encryption))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.encryption = Password.Encryption()
        self.encryption.parent = self
        self._children_name_map["encryption"] = "encryption"
        self._children_yang_names.add("encryption")
        self._segment_path = lambda: "Cisco-IOS-XR-lib-keychain-masterkey-aes-cfg:password"


    class Encryption(Entity):
        """
        Enable password encryption
        
        .. attribute:: aes
        
        	encryption type used to store key
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        	**default value**\: 0
        
        

        """

        _prefix = 'lib-keychain-masterkey-aes-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Password.Encryption, self).__init__()

            self.yang_name = "encryption"
            self.yang_parent_name = "password"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('aes', YLeaf(YType.int32, 'aes')),
            ])
            self.aes = None
            self._segment_path = lambda: "encryption"
            self._absolute_path = lambda: "Cisco-IOS-XR-lib-keychain-masterkey-aes-cfg:password/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Password.Encryption, ['aes'], name, value)

    def clone_ptr(self):
        self._top_entity = Password()
        return self._top_entity


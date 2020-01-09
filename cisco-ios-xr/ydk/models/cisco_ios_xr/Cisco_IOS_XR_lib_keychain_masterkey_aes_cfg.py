""" Cisco_IOS_XR_lib_keychain_masterkey_aes_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR lib\-keychain\-masterkey\-aes package configuration.

This module contains definitions
for the following management objects\:
  password\: Configure masterkey

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
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



class KeyEncryption(Enum):
    """
    KeyEncryption (Enum Class)

    Key encryption

    .. data:: type6 = 2

    	Type6

    """

    type6 = Enum.YLeaf(2, "type6")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lib_keychain_masterkey_aes_cfg as meta
        return meta._meta_table['KeyEncryption']



class Password(_Entity_):
    """
    Configure masterkey
    
    .. attribute:: encryption
    
    	Enable password encryption
    	**type**\:  :py:class:`Encryption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_masterkey_aes_cfg.Password.Encryption>`
    
    

    """

    _prefix = 'lib-keychain-masterkey-aes-cfg'
    _revision = '2017-09-07'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Password, self).__init__()
        self._top_entity = None

        self.yang_name = "password"
        self.yang_parent_name = "Cisco-IOS-XR-lib-keychain-masterkey-aes-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("encryption", ("encryption", Password.Encryption))])
        self._leafs = OrderedDict()

        self.encryption = Password.Encryption()
        self.encryption.parent = self
        self._children_name_map["encryption"] = "encryption"
        self._segment_path = lambda: "Cisco-IOS-XR-lib-keychain-masterkey-aes-cfg:password"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Password, [], name, value)


    class Encryption(_Entity_):
        """
        Enable password encryption
        
        .. attribute:: aes
        
        	encryption type used to store key
        	**type**\:  :py:class:`KeyEncryption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_masterkey_aes_cfg.KeyEncryption>`
        
        

        """

        _prefix = 'lib-keychain-masterkey-aes-cfg'
        _revision = '2017-09-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Password.Encryption, self).__init__()

            self.yang_name = "encryption"
            self.yang_parent_name = "password"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('aes', (YLeaf(YType.enumeration, 'aes'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_masterkey_aes_cfg', 'KeyEncryption', '')])),
            ])
            self.aes = None
            self._segment_path = lambda: "encryption"
            self._absolute_path = lambda: "Cisco-IOS-XR-lib-keychain-masterkey-aes-cfg:password/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Password.Encryption, ['aes'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lib_keychain_masterkey_aes_cfg as meta
            return meta._meta_table['Password.Encryption']['meta_info']

    def clone_ptr(self):
        self._top_entity = Password()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lib_keychain_masterkey_aes_cfg as meta
        return meta._meta_table['Password']['meta_info']



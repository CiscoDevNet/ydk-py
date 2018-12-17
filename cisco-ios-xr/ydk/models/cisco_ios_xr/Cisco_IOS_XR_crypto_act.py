""" Cisco_IOS_XR_crypto_act 

This module contains a collection of YANG definitions
for Cisco IOS\-XR action package configuration.

Copyright (c) 2016\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class KeyGenerateRsaGeneralKeys(Entity):
    """
    Generate a general purpose RSA key pair for signing and encryption
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.KeyGenerateRsaGeneralKeys.Input>`
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):
        super(KeyGenerateRsaGeneralKeys, self).__init__()
        self._top_entity = None

        self.yang_name = "key-generate-rsa-general-keys"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = KeyGenerateRsaGeneralKeys.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-crypto-act:key-generate-rsa-general-keys"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: key_label
        
        	RSA keypair label
        	**type**\: str
        
        .. attribute:: key_modulus
        
        	Key modulus in the range of 512 to 4096 for your General Purpose Keypair. Choosing a key modulus greater than 512 may take a few minutes
        	**type**\: int
        
        	**range:** 512..4096
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'crypto-act'
        _revision = '2016-04-17'

        def __init__(self):
            super(KeyGenerateRsaGeneralKeys.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "key-generate-rsa-general-keys"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('key_label', (YLeaf(YType.str, 'key-label'), ['str'])),
                ('key_modulus', (YLeaf(YType.int32, 'key-modulus'), ['int'])),
            ])
            self.key_label = None
            self.key_modulus = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-act:key-generate-rsa-general-keys/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(KeyGenerateRsaGeneralKeys.Input, ['key_label', 'key_modulus'], name, value)

    def clone_ptr(self):
        self._top_entity = KeyGenerateRsaGeneralKeys()
        return self._top_entity

class KeyGenerateRsaUsageKeys(Entity):
    """
    Generate seperate RSA key pairs for signing and encryption
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.KeyGenerateRsaUsageKeys.Input>`
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):
        super(KeyGenerateRsaUsageKeys, self).__init__()
        self._top_entity = None

        self.yang_name = "key-generate-rsa-usage-keys"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = KeyGenerateRsaUsageKeys.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-crypto-act:key-generate-rsa-usage-keys"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: key_label
        
        	RSA keypair label
        	**type**\: str
        
        .. attribute:: key_modulus
        
        	Key modulus in the range of 512 to 4096 for your General Purpose Keypair. Choosing a key modulus greater than 512 may take a few minutes
        	**type**\: int
        
        	**range:** 512..4096
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'crypto-act'
        _revision = '2016-04-17'

        def __init__(self):
            super(KeyGenerateRsaUsageKeys.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "key-generate-rsa-usage-keys"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('key_label', (YLeaf(YType.str, 'key-label'), ['str'])),
                ('key_modulus', (YLeaf(YType.int32, 'key-modulus'), ['int'])),
            ])
            self.key_label = None
            self.key_modulus = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-act:key-generate-rsa-usage-keys/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(KeyGenerateRsaUsageKeys.Input, ['key_label', 'key_modulus'], name, value)

    def clone_ptr(self):
        self._top_entity = KeyGenerateRsaUsageKeys()
        return self._top_entity

class KeyGenerateRsa(Entity):
    """
    Generate seperate RSA key pairs for signing and encryption
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.KeyGenerateRsa.Input>`
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):
        super(KeyGenerateRsa, self).__init__()
        self._top_entity = None

        self.yang_name = "key-generate-rsa"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = KeyGenerateRsa.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-crypto-act:key-generate-rsa"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: key_label
        
        	RSA keypair label
        	**type**\: str
        
        .. attribute:: key_modulus
        
        	Key modulus in the range of 512 to 4096 for your General Purpose Keypair. Choosing a key modulus greater than 512 may take a few minutes
        	**type**\: int
        
        	**range:** 512..4096
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'crypto-act'
        _revision = '2016-04-17'

        def __init__(self):
            super(KeyGenerateRsa.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "key-generate-rsa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('key_label', (YLeaf(YType.str, 'key-label'), ['str'])),
                ('key_modulus', (YLeaf(YType.int32, 'key-modulus'), ['int'])),
            ])
            self.key_label = None
            self.key_modulus = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-act:key-generate-rsa/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(KeyGenerateRsa.Input, ['key_label', 'key_modulus'], name, value)

    def clone_ptr(self):
        self._top_entity = KeyGenerateRsa()
        return self._top_entity

class KeyGenerateDsa(Entity):
    """
    Generate DSA keys
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.KeyGenerateDsa.Input>`
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):
        super(KeyGenerateDsa, self).__init__()
        self._top_entity = None

        self.yang_name = "key-generate-dsa"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = KeyGenerateDsa.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-crypto-act:key-generate-dsa"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: key_modulus
        
        	Key modulus size can be 512, 768 or 1024 bits
        	**type**\: int
        
        	**range:** 512..None \| 768..None \| 1024..None
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'crypto-act'
        _revision = '2016-04-17'

        def __init__(self):
            super(KeyGenerateDsa.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "key-generate-dsa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('key_modulus', (YLeaf(YType.int32, 'key-modulus'), ['int'])),
            ])
            self.key_modulus = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-act:key-generate-dsa/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(KeyGenerateDsa.Input, ['key_modulus'], name, value)

    def clone_ptr(self):
        self._top_entity = KeyGenerateDsa()
        return self._top_entity

class KeyGenerateEcdsa(Entity):
    """
    Generate a ECDSA key of curve type nistp256 \| nistp384 \| nistp521
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.KeyGenerateEcdsa.Input>`
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):
        super(KeyGenerateEcdsa, self).__init__()
        self._top_entity = None

        self.yang_name = "key-generate-ecdsa"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = KeyGenerateEcdsa.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-crypto-act:key-generate-ecdsa"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: key_modulus
        
        	
        	**type**\:  :py:class:`KeyModulus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.KeyGenerateEcdsa.Input.KeyModulus>`
        
        	**mandatory**\: True
        
        .. attribute:: key_label
        
        	ECDSA key label
        	**type**\: str
        
        

        """

        _prefix = 'crypto-act'
        _revision = '2016-04-17'

        def __init__(self):
            super(KeyGenerateEcdsa.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "key-generate-ecdsa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('key_modulus', (YLeaf(YType.enumeration, 'key-modulus'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act', 'KeyGenerateEcdsa', 'Input.KeyModulus')])),
                ('key_label', (YLeaf(YType.str, 'key-label'), ['str'])),
            ])
            self.key_modulus = None
            self.key_label = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-act:key-generate-ecdsa/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(KeyGenerateEcdsa.Input, ['key_modulus', 'key_label'], name, value)

        class KeyModulus(Enum):
            """
            KeyModulus (Enum Class)

            .. data:: nistp256 = 0

            .. data:: nistp384 = 1

            .. data:: nistp521 = 2

            """

            nistp256 = Enum.YLeaf(0, "nistp256")

            nistp384 = Enum.YLeaf(1, "nistp384")

            nistp521 = Enum.YLeaf(2, "nistp521")


    def clone_ptr(self):
        self._top_entity = KeyGenerateEcdsa()
        return self._top_entity

class KeyZeroizeRsa(Entity):
    """
    Remove RSA keys
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.KeyZeroizeRsa.Input>`
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):
        super(KeyZeroizeRsa, self).__init__()
        self._top_entity = None

        self.yang_name = "key-zeroize-rsa"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = KeyZeroizeRsa.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-crypto-act:key-zeroize-rsa"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: key_label
        
        	RSA key label
        	**type**\: str
        
        

        """

        _prefix = 'crypto-act'
        _revision = '2016-04-17'

        def __init__(self):
            super(KeyZeroizeRsa.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "key-zeroize-rsa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('key_label', (YLeaf(YType.str, 'key-label'), ['str'])),
            ])
            self.key_label = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-act:key-zeroize-rsa/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(KeyZeroizeRsa.Input, ['key_label'], name, value)

    def clone_ptr(self):
        self._top_entity = KeyZeroizeRsa()
        return self._top_entity

class KeyZeroizeDsa(Entity):
    """
    Remove DSA keys
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):
        super(KeyZeroizeDsa, self).__init__()
        self._top_entity = None

        self.yang_name = "key-zeroize-dsa"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()
        self._segment_path = lambda: "Cisco-IOS-XR-crypto-act:key-zeroize-dsa"
        self._is_frozen = True

    def clone_ptr(self):
        self._top_entity = KeyZeroizeDsa()
        return self._top_entity

class KeyZeroizeEcdsa(Entity):
    """
    Remove ECDSA key of curve type nistp256 \| nistp384 \| nistp521
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.KeyZeroizeEcdsa.Input>`
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):
        super(KeyZeroizeEcdsa, self).__init__()
        self._top_entity = None

        self.yang_name = "key-zeroize-ecdsa"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = KeyZeroizeEcdsa.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-crypto-act:key-zeroize-ecdsa"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: key_modulus
        
        	
        	**type**\:  :py:class:`KeyModulus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.KeyZeroizeEcdsa.Input.KeyModulus>`
        
        	**mandatory**\: True
        
        .. attribute:: key_label
        
        	ECDSA key label
        	**type**\: str
        
        

        """

        _prefix = 'crypto-act'
        _revision = '2016-04-17'

        def __init__(self):
            super(KeyZeroizeEcdsa.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "key-zeroize-ecdsa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('key_modulus', (YLeaf(YType.enumeration, 'key-modulus'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act', 'KeyZeroizeEcdsa', 'Input.KeyModulus')])),
                ('key_label', (YLeaf(YType.str, 'key-label'), ['str'])),
            ])
            self.key_modulus = None
            self.key_label = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-act:key-zeroize-ecdsa/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(KeyZeroizeEcdsa.Input, ['key_modulus', 'key_label'], name, value)

        class KeyModulus(Enum):
            """
            KeyModulus (Enum Class)

            .. data:: nistp256 = 0

            .. data:: nistp384 = 1

            .. data:: nistp521 = 2

            """

            nistp256 = Enum.YLeaf(0, "nistp256")

            nistp384 = Enum.YLeaf(1, "nistp384")

            nistp521 = Enum.YLeaf(2, "nistp521")


    def clone_ptr(self):
        self._top_entity = KeyZeroizeEcdsa()
        return self._top_entity

class KeyZeroizeAuthenticationRsa(Entity):
    """
    Remove RSA authentication key
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):
        super(KeyZeroizeAuthenticationRsa, self).__init__()
        self._top_entity = None

        self.yang_name = "key-zeroize-authentication-rsa"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()
        self._segment_path = lambda: "Cisco-IOS-XR-crypto-act:key-zeroize-authentication-rsa"
        self._is_frozen = True

    def clone_ptr(self):
        self._top_entity = KeyZeroizeAuthenticationRsa()
        return self._top_entity

class KeyImportAuthenticationRsa(Entity):
    """
    Remove RSA authentication key
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.KeyImportAuthenticationRsa.Input>`
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):
        super(KeyImportAuthenticationRsa, self).__init__()
        self._top_entity = None

        self.yang_name = "key-import-authentication-rsa"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = KeyImportAuthenticationRsa.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-crypto-act:key-import-authentication-rsa"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: path
        
        	Path to RSA pubkey file
        	**type**\: str
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'crypto-act'
        _revision = '2016-04-17'

        def __init__(self):
            super(KeyImportAuthenticationRsa.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "key-import-authentication-rsa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('path', (YLeaf(YType.str, 'path'), ['str'])),
            ])
            self.path = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-act:key-import-authentication-rsa/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(KeyImportAuthenticationRsa.Input, ['path'], name, value)

    def clone_ptr(self):
        self._top_entity = KeyImportAuthenticationRsa()
        return self._top_entity

class CaAuthenticate(Entity):
    """
    Get the certification authority certificate
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.CaAuthenticate.Input>`
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):
        super(CaAuthenticate, self).__init__()
        self._top_entity = None

        self.yang_name = "ca-authenticate"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = CaAuthenticate.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-crypto-act:ca-authenticate"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: server_name
        
        	CA Server Name
        	**type**\: str
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'crypto-act'
        _revision = '2016-04-17'

        def __init__(self):
            super(CaAuthenticate.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "ca-authenticate"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('server_name', (YLeaf(YType.str, 'server-name'), ['str'])),
            ])
            self.server_name = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-act:ca-authenticate/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CaAuthenticate.Input, ['server_name'], name, value)

    def clone_ptr(self):
        self._top_entity = CaAuthenticate()
        return self._top_entity

class CaEnroll(Entity):
    """
    Request a certificate from a CA
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.CaEnroll.Input>`
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):
        super(CaEnroll, self).__init__()
        self._top_entity = None

        self.yang_name = "ca-enroll"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = CaEnroll.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-crypto-act:ca-enroll"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: server_name
        
        	CA Server Name
        	**type**\: str
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'crypto-act'
        _revision = '2016-04-17'

        def __init__(self):
            super(CaEnroll.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "ca-enroll"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('server_name', (YLeaf(YType.str, 'server-name'), ['str'])),
            ])
            self.server_name = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-act:ca-enroll/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CaEnroll.Input, ['server_name'], name, value)

    def clone_ptr(self):
        self._top_entity = CaEnroll()
        return self._top_entity

class CaImportCertificate(Entity):
    """
    Import a certificate from a s/tftp server or the terminal
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.CaImportCertificate.Input>`
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):
        super(CaImportCertificate, self).__init__()
        self._top_entity = None

        self.yang_name = "ca-import-certificate"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = CaImportCertificate.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-crypto-act:ca-import-certificate"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: server_name
        
        	CA Server Name
        	**type**\: str
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'crypto-act'
        _revision = '2016-04-17'

        def __init__(self):
            super(CaImportCertificate.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "ca-import-certificate"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('server_name', (YLeaf(YType.str, 'server-name'), ['str'])),
            ])
            self.server_name = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-act:ca-import-certificate/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CaImportCertificate.Input, ['server_name'], name, value)

    def clone_ptr(self):
        self._top_entity = CaImportCertificate()
        return self._top_entity

class CaCancelEnroll(Entity):
    """
    Cancel enrollment from a CA
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.CaCancelEnroll.Input>`
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):
        super(CaCancelEnroll, self).__init__()
        self._top_entity = None

        self.yang_name = "ca-cancel-enroll"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = CaCancelEnroll.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-crypto-act:ca-cancel-enroll"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: server_name
        
        	CA Server Name
        	**type**\: str
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'crypto-act'
        _revision = '2016-04-17'

        def __init__(self):
            super(CaCancelEnroll.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "ca-cancel-enroll"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('server_name', (YLeaf(YType.str, 'server-name'), ['str'])),
            ])
            self.server_name = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-act:ca-cancel-enroll/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CaCancelEnroll.Input, ['server_name'], name, value)

    def clone_ptr(self):
        self._top_entity = CaCancelEnroll()
        return self._top_entity

class CaCrlRequest(Entity):
    """
    Actions on certificate revocation lists
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.CaCrlRequest.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.CaCrlRequest.Output>`
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):
        super(CaCrlRequest, self).__init__()
        self._top_entity = None

        self.yang_name = "ca-crl-request"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = CaCrlRequest.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"

        self.output = CaCrlRequest.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._segment_path = lambda: "Cisco-IOS-XR-crypto-act:ca-crl-request"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: uri
        
        	CRL Distribution Point in URI format
        	**type**\: str
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'crypto-act'
        _revision = '2016-04-17'

        def __init__(self):
            super(CaCrlRequest.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "ca-crl-request"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('uri', (YLeaf(YType.str, 'uri'), ['str'])),
            ])
            self.uri = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-act:ca-crl-request/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CaCrlRequest.Input, ['uri'], name, value)


    class Output(Entity):
        """
        
        
        .. attribute:: certificate
        
        	Certificate returned
        	**type**\: str
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'crypto-act'
        _revision = '2016-04-17'

        def __init__(self):
            super(CaCrlRequest.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "ca-crl-request"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('certificate', (YLeaf(YType.str, 'certificate'), ['str'])),
            ])
            self.certificate = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-act:ca-crl-request/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CaCrlRequest.Output, ['certificate'], name, value)

    def clone_ptr(self):
        self._top_entity = CaCrlRequest()
        return self._top_entity

class CaTrustpoolImportUrl(Entity):
    """
    Manual import trustpool certificates from URL
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.CaTrustpoolImportUrl.Input>`
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):
        super(CaTrustpoolImportUrl, self).__init__()
        self._top_entity = None

        self.yang_name = "ca-trustpool-import-url"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = CaTrustpoolImportUrl.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-crypto-act:ca-trustpool-import-url"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: url
        
        	in URL format
        	**type**\: str
        
        

        """

        _prefix = 'crypto-act'
        _revision = '2016-04-17'

        def __init__(self):
            super(CaTrustpoolImportUrl.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "ca-trustpool-import-url"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('url', (YLeaf(YType.str, 'url'), ['str'])),
            ])
            self.url = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-act:ca-trustpool-import-url/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CaTrustpoolImportUrl.Input, ['url'], name, value)

    def clone_ptr(self):
        self._top_entity = CaTrustpoolImportUrl()
        return self._top_entity

class CaTrustpoolImportUrlClean(Entity):
    """
    Remove downloaded certificates in trustpool
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.CaTrustpoolImportUrlClean.Input>`
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):
        super(CaTrustpoolImportUrlClean, self).__init__()
        self._top_entity = None

        self.yang_name = "ca-trustpool-import-url-clean"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = CaTrustpoolImportUrlClean.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-crypto-act:ca-trustpool-import-url-clean"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: url
        
        	in URL format
        	**type**\: str
        
        

        """

        _prefix = 'crypto-act'
        _revision = '2016-04-17'

        def __init__(self):
            super(CaTrustpoolImportUrlClean.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "ca-trustpool-import-url-clean"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('url', (YLeaf(YType.str, 'url'), ['str'])),
            ])
            self.url = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-act:ca-trustpool-import-url-clean/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CaTrustpoolImportUrlClean.Input, ['url'], name, value)

    def clone_ptr(self):
        self._top_entity = CaTrustpoolImportUrlClean()
        return self._top_entity


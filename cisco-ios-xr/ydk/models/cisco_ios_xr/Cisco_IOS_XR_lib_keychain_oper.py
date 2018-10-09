""" Cisco_IOS_XR_lib_keychain_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR lib\-keychain package operational data.

This module contains definitions
for the following management objects\:
  keychain\: Keychain operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CrytoAlgo(Enum):
    """
    CrytoAlgo (Enum Class)

    Cryptographic algorithm type

    .. data:: not_configured = 0

    	Not configured

    .. data:: aes_128_cmac_96 = 1

    	CMAC AES 12 bytes

    .. data:: hmac_sha1_12 = 2

    	HMAC SHA1 12 bytes

    .. data:: md5 = 3

    	MD5 16 bytes

    .. data:: sha1 = 4

    	SHA1 20 bytes

    .. data:: hmac_md5 = 5

    	HMAC MD5 16 bytes

    .. data:: hmac_sha1_20 = 6

    	HMAC SHA1 20 bytes

    .. data:: aes_128_cmac = 7

    	CMAC AES 32 bytes

    .. data:: aes_256_cmac = 8

    	CMAC AES 64 bytes

    .. data:: hmac_sha1_96 = 9

    	HMAC SHA1 12 bytes

    .. data:: hmac_sha_256 = 10

    	HMAC SHA256 32 bytes

    """

    not_configured = Enum.YLeaf(0, "not-configured")

    aes_128_cmac_96 = Enum.YLeaf(1, "aes-128-cmac-96")

    hmac_sha1_12 = Enum.YLeaf(2, "hmac-sha1-12")

    md5 = Enum.YLeaf(3, "md5")

    sha1 = Enum.YLeaf(4, "sha1")

    hmac_md5 = Enum.YLeaf(5, "hmac-md5")

    hmac_sha1_20 = Enum.YLeaf(6, "hmac-sha1-20")

    aes_128_cmac = Enum.YLeaf(7, "aes-128-cmac")

    aes_256_cmac = Enum.YLeaf(8, "aes-256-cmac")

    hmac_sha1_96 = Enum.YLeaf(9, "hmac-sha1-96")

    hmac_sha_256 = Enum.YLeaf(10, "hmac-sha-256")


class Enc(Enum):
    """
    Enc (Enum Class)

    Type of password encryption

    .. data:: password_type7 = 0

    	Type 7 password type

    .. data:: password_type6 = 2

    	Type 6 Encryption

    """

    password_type7 = Enum.YLeaf(0, "password-type7")

    password_type6 = Enum.YLeaf(2, "password-type6")



class Keychain(Entity):
    """
    Keychain operational data
    
    .. attribute:: keys
    
    	List of configured key names
    	**type**\:  :py:class:`Keys <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper.Keychain.Keys>`
    
    

    """

    _prefix = 'lib-keychain-oper'
    _revision = '2018-01-31'

    def __init__(self):
        super(Keychain, self).__init__()
        self._top_entity = None

        self.yang_name = "keychain"
        self.yang_parent_name = "Cisco-IOS-XR-lib-keychain-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("keys", ("keys", Keychain.Keys))])
        self._leafs = OrderedDict()

        self.keys = Keychain.Keys()
        self.keys.parent = self
        self._children_name_map["keys"] = "keys"
        self._segment_path = lambda: "Cisco-IOS-XR-lib-keychain-oper:keychain"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Keychain, [], name, value)


    class Keys(Entity):
        """
        List of configured key names
        
        .. attribute:: key
        
        	Configured key name
        	**type**\: list of  		 :py:class:`Key <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper.Keychain.Keys.Key>`
        
        

        """

        _prefix = 'lib-keychain-oper'
        _revision = '2018-01-31'

        def __init__(self):
            super(Keychain.Keys, self).__init__()

            self.yang_name = "keys"
            self.yang_parent_name = "keychain"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("key", ("key", Keychain.Keys.Key))])
            self._leafs = OrderedDict()

            self.key = YList(self)
            self._segment_path = lambda: "keys"
            self._absolute_path = lambda: "Cisco-IOS-XR-lib-keychain-oper:keychain/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Keychain.Keys, [], name, value)


        class Key(Entity):
            """
            Configured key name
            
            .. attribute:: key_name  (key)
            
            	Key name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: key
            
            	Key properties
            	**type**\:  :py:class:`Key_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper.Keychain.Keys.Key.Key_>`
            
            .. attribute:: accept_tolerance
            
            	Accept tolerance is infinite if value is 0xffffffff
            	**type**\: str
            
            

            """

            _prefix = 'lib-keychain-oper'
            _revision = '2018-01-31'

            def __init__(self):
                super(Keychain.Keys.Key, self).__init__()

                self.yang_name = "key"
                self.yang_parent_name = "keys"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['key_name']
                self._child_classes = OrderedDict([("key", ("key", Keychain.Keys.Key.Key_))])
                self._leafs = OrderedDict([
                    ('key_name', (YLeaf(YType.str, 'key-name'), ['str'])),
                    ('accept_tolerance', (YLeaf(YType.str, 'accept-tolerance'), ['str'])),
                ])
                self.key_name = None
                self.accept_tolerance = None

                self.key = Keychain.Keys.Key.Key_()
                self.key.parent = self
                self._children_name_map["key"] = "key"
                self._segment_path = lambda: "key" + "[key-name='" + str(self.key_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-lib-keychain-oper:keychain/keys/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Keychain.Keys.Key, ['key_name', u'accept_tolerance'], name, value)


            class Key_(Entity):
                """
                Key properties
                
                .. attribute:: key_id
                
                	key id
                	**type**\: list of  		 :py:class:`KeyId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper.Keychain.Keys.Key.Key_.KeyId>`
                
                

                """

                _prefix = 'lib-keychain-oper'
                _revision = '2018-01-31'

                def __init__(self):
                    super(Keychain.Keys.Key.Key_, self).__init__()

                    self.yang_name = "key"
                    self.yang_parent_name = "key"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("key-id", ("key_id", Keychain.Keys.Key.Key_.KeyId))])
                    self._leafs = OrderedDict()

                    self.key_id = YList(self)
                    self._segment_path = lambda: "key"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Keychain.Keys.Key.Key_, [], name, value)


                class KeyId(Entity):
                    """
                    key id
                    
                    .. attribute:: macsec
                    
                    	To check if it's a macsec key
                    	**type**\:  :py:class:`Macsec <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper.Keychain.Keys.Key.Key_.KeyId.Macsec>`
                    
                    .. attribute:: send_lifetime
                    
                    	Lifetime of the key
                    	**type**\:  :py:class:`SendLifetime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper.Keychain.Keys.Key.Key_.KeyId.SendLifetime>`
                    
                    .. attribute:: accept_lifetime
                    
                    	Accept Lifetime of the key
                    	**type**\:  :py:class:`AcceptLifetime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper.Keychain.Keys.Key.Key_.KeyId.AcceptLifetime>`
                    
                    .. attribute:: key_string
                    
                    	Key string
                    	**type**\: str
                    
                    .. attribute:: type
                    
                    	Type of key encryption
                    	**type**\:  :py:class:`Enc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper.Enc>`
                    
                    .. attribute:: key_id
                    
                    	Key ID
                    	**type**\: str
                    
                    .. attribute:: cryptographic_algorithm
                    
                    	Cryptographic algorithm
                    	**type**\:  :py:class:`CrytoAlgo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper.CrytoAlgo>`
                    
                    

                    """

                    _prefix = 'lib-keychain-oper'
                    _revision = '2018-01-31'

                    def __init__(self):
                        super(Keychain.Keys.Key.Key_.KeyId, self).__init__()

                        self.yang_name = "key-id"
                        self.yang_parent_name = "key"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("macsec", ("macsec", Keychain.Keys.Key.Key_.KeyId.Macsec)), ("send-lifetime", ("send_lifetime", Keychain.Keys.Key.Key_.KeyId.SendLifetime)), ("accept-lifetime", ("accept_lifetime", Keychain.Keys.Key.Key_.KeyId.AcceptLifetime))])
                        self._leafs = OrderedDict([
                            ('key_string', (YLeaf(YType.str, 'key-string'), ['str'])),
                            ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper', 'Enc', '')])),
                            ('key_id', (YLeaf(YType.str, 'key-id'), ['str'])),
                            ('cryptographic_algorithm', (YLeaf(YType.enumeration, 'cryptographic-algorithm'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper', 'CrytoAlgo', '')])),
                        ])
                        self.key_string = None
                        self.type = None
                        self.key_id = None
                        self.cryptographic_algorithm = None

                        self.macsec = Keychain.Keys.Key.Key_.KeyId.Macsec()
                        self.macsec.parent = self
                        self._children_name_map["macsec"] = "macsec"

                        self.send_lifetime = Keychain.Keys.Key.Key_.KeyId.SendLifetime()
                        self.send_lifetime.parent = self
                        self._children_name_map["send_lifetime"] = "send-lifetime"

                        self.accept_lifetime = Keychain.Keys.Key.Key_.KeyId.AcceptLifetime()
                        self.accept_lifetime.parent = self
                        self._children_name_map["accept_lifetime"] = "accept-lifetime"
                        self._segment_path = lambda: "key-id"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Keychain.Keys.Key.Key_.KeyId, [u'key_string', u'type', u'key_id', u'cryptographic_algorithm'], name, value)


                    class Macsec(Entity):
                        """
                        To check if it's a macsec key
                        
                        .. attribute:: is_macsec_key
                        
                        	To check if it's a macsec key
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'lib-keychain-oper'
                        _revision = '2018-01-31'

                        def __init__(self):
                            super(Keychain.Keys.Key.Key_.KeyId.Macsec, self).__init__()

                            self.yang_name = "macsec"
                            self.yang_parent_name = "key-id"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_macsec_key', (YLeaf(YType.boolean, 'is-macsec-key'), ['bool'])),
                            ])
                            self.is_macsec_key = None
                            self._segment_path = lambda: "macsec"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Keychain.Keys.Key.Key_.KeyId.Macsec, [u'is_macsec_key'], name, value)


                    class SendLifetime(Entity):
                        """
                        Lifetime of the key
                        
                        .. attribute:: start
                        
                        	Key life start time in format \: day\-of\-week month date\-of\-month HH\:MM\:SS year eg\: Thu Feb 1 18\:32\:14 2011
                        	**type**\: str
                        
                        .. attribute:: end
                        
                        	Key life end time in format \: day\-of\-week month date\-of\-month HH\:MM\:SS year eg\: Thu Feb 1 18\:32 \:14 2011
                        	**type**\: str
                        
                        .. attribute:: duration
                        
                        	Duration of the key in seconds. value 0xffffffff reflects infinite, never expires, is configured 
                        	**type**\: str
                        
                        	**units**\: second
                        
                        .. attribute:: is_always_valid
                        
                        	Is TRUE if duration is 0xffffffff 
                        	**type**\: bool
                        
                        .. attribute:: is_valid_now
                        
                        	Is TRUE if current time is betweenstart and end lifetime , else FALSE
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'lib-keychain-oper'
                        _revision = '2018-01-31'

                        def __init__(self):
                            super(Keychain.Keys.Key.Key_.KeyId.SendLifetime, self).__init__()

                            self.yang_name = "send-lifetime"
                            self.yang_parent_name = "key-id"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('start', (YLeaf(YType.str, 'start'), ['str'])),
                                ('end', (YLeaf(YType.str, 'end'), ['str'])),
                                ('duration', (YLeaf(YType.str, 'duration'), ['str'])),
                                ('is_always_valid', (YLeaf(YType.boolean, 'is-always-valid'), ['bool'])),
                                ('is_valid_now', (YLeaf(YType.boolean, 'is-valid-now'), ['bool'])),
                            ])
                            self.start = None
                            self.end = None
                            self.duration = None
                            self.is_always_valid = None
                            self.is_valid_now = None
                            self._segment_path = lambda: "send-lifetime"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Keychain.Keys.Key.Key_.KeyId.SendLifetime, [u'start', u'end', u'duration', u'is_always_valid', u'is_valid_now'], name, value)


                    class AcceptLifetime(Entity):
                        """
                        Accept Lifetime of the key
                        
                        .. attribute:: start
                        
                        	Key life start time in format \: day\-of\-week month date\-of\-month HH\:MM\:SS year eg\: Thu Feb 1 18\:32\:14 2011
                        	**type**\: str
                        
                        .. attribute:: end
                        
                        	Key life end time in format \: day\-of\-week month date\-of\-month HH\:MM\:SS year eg\: Thu Feb 1 18\:32 \:14 2011
                        	**type**\: str
                        
                        .. attribute:: duration
                        
                        	Duration of the key in seconds. value 0xffffffff reflects infinite, never expires, is configured 
                        	**type**\: str
                        
                        	**units**\: second
                        
                        .. attribute:: is_always_valid
                        
                        	Is TRUE if duration is 0xffffffff 
                        	**type**\: bool
                        
                        .. attribute:: is_valid_now
                        
                        	Is TRUE if current time is betweenstart and end lifetime , else FALSE
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'lib-keychain-oper'
                        _revision = '2018-01-31'

                        def __init__(self):
                            super(Keychain.Keys.Key.Key_.KeyId.AcceptLifetime, self).__init__()

                            self.yang_name = "accept-lifetime"
                            self.yang_parent_name = "key-id"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('start', (YLeaf(YType.str, 'start'), ['str'])),
                                ('end', (YLeaf(YType.str, 'end'), ['str'])),
                                ('duration', (YLeaf(YType.str, 'duration'), ['str'])),
                                ('is_always_valid', (YLeaf(YType.boolean, 'is-always-valid'), ['bool'])),
                                ('is_valid_now', (YLeaf(YType.boolean, 'is-valid-now'), ['bool'])),
                            ])
                            self.start = None
                            self.end = None
                            self.duration = None
                            self.is_always_valid = None
                            self.is_valid_now = None
                            self._segment_path = lambda: "accept-lifetime"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Keychain.Keys.Key.Key_.KeyId.AcceptLifetime, [u'start', u'end', u'duration', u'is_always_valid', u'is_valid_now'], name, value)

    def clone_ptr(self):
        self._top_entity = Keychain()
        return self._top_entity


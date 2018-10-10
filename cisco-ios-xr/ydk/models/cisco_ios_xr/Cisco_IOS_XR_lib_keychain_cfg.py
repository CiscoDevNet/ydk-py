""" Cisco_IOS_XR_lib_keychain_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR lib\-keychain package configuration.

This module contains definitions
for the following management objects\:
  keychains\: Configure a Key Chain

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CryptoAlg(Enum):
    """
    CryptoAlg (Enum Class)

    Crypto alg

    .. data:: alg_aes_128_cmac_96 = 1

    	AES 128 CMAC 96

    .. data:: alg_hmac_sha1_12 = 2

    	HMAC SHA 1 12

    .. data:: alg_md5_16 = 3

    	MD5 16

    .. data:: alg_sha1_20 = 4

    	SHA 1 20

    .. data:: alg_hmac_md5_16 = 5

    	HMAC MD5 16

    .. data:: alg_hmac_sha1_20 = 6

    	HMAC SHA 1 20

    .. data:: alg_hmac_sha1_96 = 9

    	HMAC SHA 1 96

    .. data:: alg_hmac_sha_256 = 10

    	HMAC SHA 256

    """

    alg_aes_128_cmac_96 = Enum.YLeaf(1, "alg-aes-128-cmac-96")

    alg_hmac_sha1_12 = Enum.YLeaf(2, "alg-hmac-sha1-12")

    alg_md5_16 = Enum.YLeaf(3, "alg-md5-16")

    alg_sha1_20 = Enum.YLeaf(4, "alg-sha1-20")

    alg_hmac_md5_16 = Enum.YLeaf(5, "alg-hmac-md5-16")

    alg_hmac_sha1_20 = Enum.YLeaf(6, "alg-hmac-sha1-20")

    alg_hmac_sha1_96 = Enum.YLeaf(9, "alg-hmac-sha1-96")

    alg_hmac_sha_256 = Enum.YLeaf(10, "alg-hmac-sha-256")


class KeyChainMonth(Enum):
    """
    KeyChainMonth (Enum Class)

    Key chain month

    .. data:: jan = 0

    	January

    .. data:: feb = 1

    	February

    .. data:: mar = 2

    	March

    .. data:: apr = 3

    	April

    .. data:: may = 4

    	May

    .. data:: jun = 5

    	June

    .. data:: jul = 6

    	July

    .. data:: aug = 7

    	August

    .. data:: sep = 8

    	September

    .. data:: oct = 9

    	October

    .. data:: nov = 10

    	November

    .. data:: dec = 11

    	December

    """

    jan = Enum.YLeaf(0, "jan")

    feb = Enum.YLeaf(1, "feb")

    mar = Enum.YLeaf(2, "mar")

    apr = Enum.YLeaf(3, "apr")

    may = Enum.YLeaf(4, "may")

    jun = Enum.YLeaf(5, "jun")

    jul = Enum.YLeaf(6, "jul")

    aug = Enum.YLeaf(7, "aug")

    sep = Enum.YLeaf(8, "sep")

    oct = Enum.YLeaf(9, "oct")

    nov = Enum.YLeaf(10, "nov")

    dec = Enum.YLeaf(11, "dec")


class MacsecCryptoAlg(Enum):
    """
    MacsecCryptoAlg (Enum Class)

    Macsec crypto alg

    .. data:: aes_128_cmac = 7

    	aes 128 cmac

    .. data:: aes_256_cmac = 8

    	aes 256 cmac

    """

    aes_128_cmac = Enum.YLeaf(7, "aes-128-cmac")

    aes_256_cmac = Enum.YLeaf(8, "aes-256-cmac")


class MacsecEncryption(Enum):
    """
    MacsecEncryption (Enum Class)

    Macsec encryption

    .. data:: type7 = 0

    	Type7

    .. data:: type6 = 2

    	Type6

    """

    type7 = Enum.YLeaf(0, "type7")

    type6 = Enum.YLeaf(2, "type6")



class Keychains(Entity):
    """
    Configure a Key Chain
    
    .. attribute:: keychain
    
    	Name of the key chain
    	**type**\: list of  		 :py:class:`Keychain <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg.Keychains.Keychain>`
    
    

    """

    _prefix = 'lib-keychain-cfg'
    _revision = '2018-01-31'

    def __init__(self):
        super(Keychains, self).__init__()
        self._top_entity = None

        self.yang_name = "keychains"
        self.yang_parent_name = "Cisco-IOS-XR-lib-keychain-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("keychain", ("keychain", Keychains.Keychain))])
        self._leafs = OrderedDict()

        self.keychain = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-lib-keychain-cfg:keychains"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Keychains, [], name, value)


    class Keychain(Entity):
        """
        Name of the key chain
        
        .. attribute:: chain_name  (key)
        
        	Name of the key chain
        	**type**\: str
        
        	**length:** 1..32
        
        .. attribute:: accept_tolerance
        
        	Accept Tolerance in seconds or infinite
        	**type**\:  :py:class:`AcceptTolerance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg.Keychains.Keychain.AcceptTolerance>`
        
        .. attribute:: macsec_keychain
        
        	Name of the key chain for MACSec
        	**type**\:  :py:class:`MacsecKeychain <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg.Keychains.Keychain.MacsecKeychain>`
        
        .. attribute:: keys
        
        	Configure a Key
        	**type**\:  :py:class:`Keys <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg.Keychains.Keychain.Keys>`
        
        

        """

        _prefix = 'lib-keychain-cfg'
        _revision = '2018-01-31'

        def __init__(self):
            super(Keychains.Keychain, self).__init__()

            self.yang_name = "keychain"
            self.yang_parent_name = "keychains"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['chain_name']
            self._child_classes = OrderedDict([("accept-tolerance", ("accept_tolerance", Keychains.Keychain.AcceptTolerance)), ("macsec-keychain", ("macsec_keychain", Keychains.Keychain.MacsecKeychain)), ("keys", ("keys", Keychains.Keychain.Keys))])
            self._leafs = OrderedDict([
                ('chain_name', (YLeaf(YType.str, 'chain-name'), ['str'])),
            ])
            self.chain_name = None

            self.accept_tolerance = Keychains.Keychain.AcceptTolerance()
            self.accept_tolerance.parent = self
            self._children_name_map["accept_tolerance"] = "accept-tolerance"

            self.macsec_keychain = Keychains.Keychain.MacsecKeychain()
            self.macsec_keychain.parent = self
            self._children_name_map["macsec_keychain"] = "macsec-keychain"

            self.keys = Keychains.Keychain.Keys()
            self.keys.parent = self
            self._children_name_map["keys"] = "keys"
            self._segment_path = lambda: "keychain" + "[chain-name='" + str(self.chain_name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-lib-keychain-cfg:keychains/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Keychains.Keychain, ['chain_name'], name, value)


        class AcceptTolerance(Entity):
            """
            Accept Tolerance in seconds or infinite
            
            .. attribute:: value
            
            	Value in seconds
            	**type**\: int
            
            	**range:** 1..8640000
            
            	**units**\: second
            
            .. attribute:: infinite
            
            	Infinite tolerance
            	**type**\: bool
            
            

            """

            _prefix = 'lib-keychain-cfg'
            _revision = '2018-01-31'

            def __init__(self):
                super(Keychains.Keychain.AcceptTolerance, self).__init__()

                self.yang_name = "accept-tolerance"
                self.yang_parent_name = "keychain"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                    ('infinite', (YLeaf(YType.boolean, 'infinite'), ['bool'])),
                ])
                self.value = None
                self.infinite = None
                self._segment_path = lambda: "accept-tolerance"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Keychains.Keychain.AcceptTolerance, ['value', 'infinite'], name, value)


        class MacsecKeychain(Entity):
            """
            Name of the key chain for MACSec
            
            .. attribute:: macsec_keys
            
            	Configure a Key
            	**type**\:  :py:class:`MacsecKeys <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg.Keychains.Keychain.MacsecKeychain.MacsecKeys>`
            
            

            """

            _prefix = 'lib-keychain-cfg'
            _revision = '2018-01-31'

            def __init__(self):
                super(Keychains.Keychain.MacsecKeychain, self).__init__()

                self.yang_name = "macsec-keychain"
                self.yang_parent_name = "keychain"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("macsec-keys", ("macsec_keys", Keychains.Keychain.MacsecKeychain.MacsecKeys))])
                self._leafs = OrderedDict()

                self.macsec_keys = Keychains.Keychain.MacsecKeychain.MacsecKeys()
                self.macsec_keys.parent = self
                self._children_name_map["macsec_keys"] = "macsec-keys"
                self._segment_path = lambda: "macsec-keychain"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Keychains.Keychain.MacsecKeychain, [], name, value)


            class MacsecKeys(Entity):
                """
                Configure a Key
                
                .. attribute:: macsec_key
                
                	Key Identifier
                	**type**\: list of  		 :py:class:`MacsecKey <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg.Keychains.Keychain.MacsecKeychain.MacsecKeys.MacsecKey>`
                
                

                """

                _prefix = 'lib-keychain-cfg'
                _revision = '2018-01-31'

                def __init__(self):
                    super(Keychains.Keychain.MacsecKeychain.MacsecKeys, self).__init__()

                    self.yang_name = "macsec-keys"
                    self.yang_parent_name = "macsec-keychain"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("macsec-key", ("macsec_key", Keychains.Keychain.MacsecKeychain.MacsecKeys.MacsecKey))])
                    self._leafs = OrderedDict()

                    self.macsec_key = YList(self)
                    self._segment_path = lambda: "macsec-keys"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Keychains.Keychain.MacsecKeychain.MacsecKeys, [], name, value)


                class MacsecKey(Entity):
                    """
                    Key Identifier
                    
                    .. attribute:: key_id  (key)
                    
                    	Enter CKN as non\-zero hex string of even length, length range\: <02\-64>, i.e 1\-32 bytes of MACsec CKN
                    	**type**\: str
                    
                    	**length:** 2..64
                    
                    .. attribute:: macsec_lifetime
                    
                    	Configure a key Lifetime
                    	**type**\:  :py:class:`MacsecLifetime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg.Keychains.Keychain.MacsecKeychain.MacsecKeys.MacsecKey.MacsecLifetime>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: macsec_key_string
                    
                    	Configure a clear text/encrypted Key string along with cryptographic algorithm
                    	**type**\:  :py:class:`MacsecKeyString <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg.Keychains.Keychain.MacsecKeychain.MacsecKeys.MacsecKey.MacsecKeyString>`
                    
                    	**presence node**\: True
                    
                    

                    """

                    _prefix = 'lib-keychain-cfg'
                    _revision = '2018-01-31'

                    def __init__(self):
                        super(Keychains.Keychain.MacsecKeychain.MacsecKeys.MacsecKey, self).__init__()

                        self.yang_name = "macsec-key"
                        self.yang_parent_name = "macsec-keys"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['key_id']
                        self._child_classes = OrderedDict([("macsec-lifetime", ("macsec_lifetime", Keychains.Keychain.MacsecKeychain.MacsecKeys.MacsecKey.MacsecLifetime)), ("macsec-key-string", ("macsec_key_string", Keychains.Keychain.MacsecKeychain.MacsecKeys.MacsecKey.MacsecKeyString))])
                        self._leafs = OrderedDict([
                            ('key_id', (YLeaf(YType.str, 'key-id'), ['str'])),
                        ])
                        self.key_id = None

                        self.macsec_lifetime = None
                        self._children_name_map["macsec_lifetime"] = "macsec-lifetime"

                        self.macsec_key_string = None
                        self._children_name_map["macsec_key_string"] = "macsec-key-string"
                        self._segment_path = lambda: "macsec-key" + "[key-id='" + str(self.key_id) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Keychains.Keychain.MacsecKeychain.MacsecKeys.MacsecKey, ['key_id'], name, value)


                    class MacsecLifetime(Entity):
                        """
                        Configure a key Lifetime
                        
                        .. attribute:: start_hour
                        
                        	Start Hour
                        	**type**\: int
                        
                        	**range:** 0..23
                        
                        	**mandatory**\: True
                        
                        .. attribute:: start_minutes
                        
                        	Start Minutes
                        	**type**\: int
                        
                        	**range:** 0..59
                        
                        	**mandatory**\: True
                        
                        	**units**\: minute
                        
                        .. attribute:: start_seconds
                        
                        	Start Seconds
                        	**type**\: int
                        
                        	**range:** 0..59
                        
                        	**mandatory**\: True
                        
                        	**units**\: second
                        
                        .. attribute:: start_date
                        
                        	Start Date
                        	**type**\: int
                        
                        	**range:** 1..31
                        
                        	**mandatory**\: True
                        
                        .. attribute:: start_month
                        
                        	Start Month
                        	**type**\:  :py:class:`KeyChainMonth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg.KeyChainMonth>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: start_year
                        
                        	Start Year
                        	**type**\: int
                        
                        	**range:** 1993..2035
                        
                        	**mandatory**\: True
                        
                        .. attribute:: life_time
                        
                        	Lifetime duration in seconds
                        	**type**\: int
                        
                        	**range:** 1..2147483647
                        
                        	**units**\: second
                        
                        .. attribute:: infinite_flag
                        
                        	Infinite Lifetime flag
                        	**type**\: bool
                        
                        .. attribute:: end_hour
                        
                        	End Hour
                        	**type**\: int
                        
                        	**range:** 0..23
                        
                        .. attribute:: end_minutes
                        
                        	End Minutes
                        	**type**\: int
                        
                        	**range:** 0..59
                        
                        	**units**\: minute
                        
                        .. attribute:: end_seconds
                        
                        	End Seconds
                        	**type**\: int
                        
                        	**range:** 0..59
                        
                        	**units**\: second
                        
                        .. attribute:: end_date
                        
                        	End Date
                        	**type**\: int
                        
                        	**range:** 1..31
                        
                        .. attribute:: end_month
                        
                        	End Month
                        	**type**\:  :py:class:`KeyChainMonth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg.KeyChainMonth>`
                        
                        .. attribute:: end_year
                        
                        	End Year
                        	**type**\: int
                        
                        	**range:** 1993..2035
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'lib-keychain-cfg'
                        _revision = '2018-01-31'

                        def __init__(self):
                            super(Keychains.Keychain.MacsecKeychain.MacsecKeys.MacsecKey.MacsecLifetime, self).__init__()

                            self.yang_name = "macsec-lifetime"
                            self.yang_parent_name = "macsec-key"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('start_hour', (YLeaf(YType.uint32, 'start-hour'), ['int'])),
                                ('start_minutes', (YLeaf(YType.uint32, 'start-minutes'), ['int'])),
                                ('start_seconds', (YLeaf(YType.uint32, 'start-seconds'), ['int'])),
                                ('start_date', (YLeaf(YType.uint32, 'start-date'), ['int'])),
                                ('start_month', (YLeaf(YType.enumeration, 'start-month'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg', 'KeyChainMonth', '')])),
                                ('start_year', (YLeaf(YType.uint32, 'start-year'), ['int'])),
                                ('life_time', (YLeaf(YType.uint32, 'life-time'), ['int'])),
                                ('infinite_flag', (YLeaf(YType.boolean, 'infinite-flag'), ['bool'])),
                                ('end_hour', (YLeaf(YType.uint32, 'end-hour'), ['int'])),
                                ('end_minutes', (YLeaf(YType.uint32, 'end-minutes'), ['int'])),
                                ('end_seconds', (YLeaf(YType.uint32, 'end-seconds'), ['int'])),
                                ('end_date', (YLeaf(YType.uint32, 'end-date'), ['int'])),
                                ('end_month', (YLeaf(YType.enumeration, 'end-month'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg', 'KeyChainMonth', '')])),
                                ('end_year', (YLeaf(YType.uint32, 'end-year'), ['int'])),
                            ])
                            self.start_hour = None
                            self.start_minutes = None
                            self.start_seconds = None
                            self.start_date = None
                            self.start_month = None
                            self.start_year = None
                            self.life_time = None
                            self.infinite_flag = None
                            self.end_hour = None
                            self.end_minutes = None
                            self.end_seconds = None
                            self.end_date = None
                            self.end_month = None
                            self.end_year = None
                            self._segment_path = lambda: "macsec-lifetime"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Keychains.Keychain.MacsecKeychain.MacsecKeys.MacsecKey.MacsecLifetime, ['start_hour', 'start_minutes', 'start_seconds', 'start_date', 'start_month', 'start_year', 'life_time', 'infinite_flag', 'end_hour', 'end_minutes', 'end_seconds', 'end_date', 'end_month', 'end_year'], name, value)


                    class MacsecKeyString(Entity):
                        """
                        Configure a clear text/encrypted Key string
                        along with cryptographic algorithm
                        
                        .. attribute:: string
                        
                        	Key String
                        	**type**\: str
                        
                        	**pattern:** (!.+)\|([^!].+)
                        
                        	**mandatory**\: True
                        
                        .. attribute:: cryptographic_algorithm
                        
                        	Cryptographic Algorithm
                        	**type**\:  :py:class:`MacsecCryptoAlg <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg.MacsecCryptoAlg>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: encryption_type
                        
                        	encryption type used to store key
                        	**type**\:  :py:class:`MacsecEncryption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg.MacsecEncryption>`
                        
                        	**default value**\: type7
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'lib-keychain-cfg'
                        _revision = '2018-01-31'

                        def __init__(self):
                            super(Keychains.Keychain.MacsecKeychain.MacsecKeys.MacsecKey.MacsecKeyString, self).__init__()

                            self.yang_name = "macsec-key-string"
                            self.yang_parent_name = "macsec-key"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('string', (YLeaf(YType.str, 'string'), ['str'])),
                                ('cryptographic_algorithm', (YLeaf(YType.enumeration, 'cryptographic-algorithm'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg', 'MacsecCryptoAlg', '')])),
                                ('encryption_type', (YLeaf(YType.enumeration, 'encryption-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg', 'MacsecEncryption', '')])),
                            ])
                            self.string = None
                            self.cryptographic_algorithm = None
                            self.encryption_type = None
                            self._segment_path = lambda: "macsec-key-string"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Keychains.Keychain.MacsecKeychain.MacsecKeys.MacsecKey.MacsecKeyString, ['string', 'cryptographic_algorithm', 'encryption_type'], name, value)


        class Keys(Entity):
            """
            Configure a Key
            
            .. attribute:: key
            
            	Key Identifier
            	**type**\: list of  		 :py:class:`Key <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg.Keychains.Keychain.Keys.Key>`
            
            

            """

            _prefix = 'lib-keychain-cfg'
            _revision = '2018-01-31'

            def __init__(self):
                super(Keychains.Keychain.Keys, self).__init__()

                self.yang_name = "keys"
                self.yang_parent_name = "keychain"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("key", ("key", Keychains.Keychain.Keys.Key))])
                self._leafs = OrderedDict()

                self.key = YList(self)
                self._segment_path = lambda: "keys"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Keychains.Keychain.Keys, [], name, value)


            class Key(Entity):
                """
                Key Identifier
                
                .. attribute:: key_id  (key)
                
                	48\-bit Key identifier
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: accept_lifetime
                
                	Configure a key Acceptance Lifetime
                	**type**\:  :py:class:`AcceptLifetime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg.Keychains.Keychain.Keys.Key.AcceptLifetime>`
                
                	**presence node**\: True
                
                .. attribute:: send_lifetime
                
                	Configure a Send Lifetime
                	**type**\:  :py:class:`SendLifetime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg.Keychains.Keychain.Keys.Key.SendLifetime>`
                
                	**presence node**\: True
                
                .. attribute:: key_string
                
                	Configure a clear text/encrypted Key string 
                	**type**\: str
                
                	**pattern:** (!.+)\|([^!].+)
                
                .. attribute:: cryptographic_algorithm
                
                	Configure the cryptographic algorithm
                	**type**\:  :py:class:`CryptoAlg <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg.CryptoAlg>`
                
                

                """

                _prefix = 'lib-keychain-cfg'
                _revision = '2018-01-31'

                def __init__(self):
                    super(Keychains.Keychain.Keys.Key, self).__init__()

                    self.yang_name = "key"
                    self.yang_parent_name = "keys"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['key_id']
                    self._child_classes = OrderedDict([("accept-lifetime", ("accept_lifetime", Keychains.Keychain.Keys.Key.AcceptLifetime)), ("send-lifetime", ("send_lifetime", Keychains.Keychain.Keys.Key.SendLifetime))])
                    self._leafs = OrderedDict([
                        ('key_id', (YLeaf(YType.str, 'key-id'), ['str'])),
                        ('key_string', (YLeaf(YType.str, 'key-string'), ['str'])),
                        ('cryptographic_algorithm', (YLeaf(YType.enumeration, 'cryptographic-algorithm'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg', 'CryptoAlg', '')])),
                    ])
                    self.key_id = None
                    self.key_string = None
                    self.cryptographic_algorithm = None

                    self.accept_lifetime = None
                    self._children_name_map["accept_lifetime"] = "accept-lifetime"

                    self.send_lifetime = None
                    self._children_name_map["send_lifetime"] = "send-lifetime"
                    self._segment_path = lambda: "key" + "[key-id='" + str(self.key_id) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Keychains.Keychain.Keys.Key, ['key_id', 'key_string', 'cryptographic_algorithm'], name, value)


                class AcceptLifetime(Entity):
                    """
                    Configure a key Acceptance Lifetime
                    
                    .. attribute:: start_hour
                    
                    	Start Hour
                    	**type**\: int
                    
                    	**range:** 0..23
                    
                    	**mandatory**\: True
                    
                    .. attribute:: start_minutes
                    
                    	Start Minutes
                    	**type**\: int
                    
                    	**range:** 0..59
                    
                    	**mandatory**\: True
                    
                    	**units**\: minute
                    
                    .. attribute:: start_seconds
                    
                    	Start Seconds
                    	**type**\: int
                    
                    	**range:** 0..59
                    
                    	**mandatory**\: True
                    
                    	**units**\: second
                    
                    .. attribute:: start_date
                    
                    	Start Date
                    	**type**\: int
                    
                    	**range:** 1..31
                    
                    	**mandatory**\: True
                    
                    .. attribute:: start_month
                    
                    	Start Month
                    	**type**\:  :py:class:`KeyChainMonth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg.KeyChainMonth>`
                    
                    	**mandatory**\: True
                    
                    .. attribute:: start_year
                    
                    	Start Year
                    	**type**\: int
                    
                    	**range:** 1993..2035
                    
                    	**mandatory**\: True
                    
                    .. attribute:: life_time
                    
                    	Lifetime duration in seconds
                    	**type**\: int
                    
                    	**range:** 1..2147483647
                    
                    	**units**\: second
                    
                    .. attribute:: infinite_flag
                    
                    	Infinite Lifetime flag
                    	**type**\: bool
                    
                    .. attribute:: end_hour
                    
                    	End Hour
                    	**type**\: int
                    
                    	**range:** 0..23
                    
                    .. attribute:: end_minutes
                    
                    	End Minutes
                    	**type**\: int
                    
                    	**range:** 0..59
                    
                    	**units**\: minute
                    
                    .. attribute:: end_seconds
                    
                    	End Seconds
                    	**type**\: int
                    
                    	**range:** 0..59
                    
                    	**units**\: second
                    
                    .. attribute:: end_date
                    
                    	End Date
                    	**type**\: int
                    
                    	**range:** 1..31
                    
                    .. attribute:: end_month
                    
                    	End Month
                    	**type**\:  :py:class:`KeyChainMonth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg.KeyChainMonth>`
                    
                    .. attribute:: end_year
                    
                    	End Year
                    	**type**\: int
                    
                    	**range:** 1993..2035
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'lib-keychain-cfg'
                    _revision = '2018-01-31'

                    def __init__(self):
                        super(Keychains.Keychain.Keys.Key.AcceptLifetime, self).__init__()

                        self.yang_name = "accept-lifetime"
                        self.yang_parent_name = "key"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('start_hour', (YLeaf(YType.uint32, 'start-hour'), ['int'])),
                            ('start_minutes', (YLeaf(YType.uint32, 'start-minutes'), ['int'])),
                            ('start_seconds', (YLeaf(YType.uint32, 'start-seconds'), ['int'])),
                            ('start_date', (YLeaf(YType.uint32, 'start-date'), ['int'])),
                            ('start_month', (YLeaf(YType.enumeration, 'start-month'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg', 'KeyChainMonth', '')])),
                            ('start_year', (YLeaf(YType.uint32, 'start-year'), ['int'])),
                            ('life_time', (YLeaf(YType.uint32, 'life-time'), ['int'])),
                            ('infinite_flag', (YLeaf(YType.boolean, 'infinite-flag'), ['bool'])),
                            ('end_hour', (YLeaf(YType.uint32, 'end-hour'), ['int'])),
                            ('end_minutes', (YLeaf(YType.uint32, 'end-minutes'), ['int'])),
                            ('end_seconds', (YLeaf(YType.uint32, 'end-seconds'), ['int'])),
                            ('end_date', (YLeaf(YType.uint32, 'end-date'), ['int'])),
                            ('end_month', (YLeaf(YType.enumeration, 'end-month'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg', 'KeyChainMonth', '')])),
                            ('end_year', (YLeaf(YType.uint32, 'end-year'), ['int'])),
                        ])
                        self.start_hour = None
                        self.start_minutes = None
                        self.start_seconds = None
                        self.start_date = None
                        self.start_month = None
                        self.start_year = None
                        self.life_time = None
                        self.infinite_flag = None
                        self.end_hour = None
                        self.end_minutes = None
                        self.end_seconds = None
                        self.end_date = None
                        self.end_month = None
                        self.end_year = None
                        self._segment_path = lambda: "accept-lifetime"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Keychains.Keychain.Keys.Key.AcceptLifetime, ['start_hour', 'start_minutes', 'start_seconds', 'start_date', 'start_month', 'start_year', 'life_time', 'infinite_flag', 'end_hour', 'end_minutes', 'end_seconds', 'end_date', 'end_month', 'end_year'], name, value)


                class SendLifetime(Entity):
                    """
                    Configure a Send Lifetime
                    
                    .. attribute:: start_hour
                    
                    	Start Hour
                    	**type**\: int
                    
                    	**range:** 0..23
                    
                    	**mandatory**\: True
                    
                    .. attribute:: start_minutes
                    
                    	Start Minutes
                    	**type**\: int
                    
                    	**range:** 0..59
                    
                    	**mandatory**\: True
                    
                    	**units**\: minute
                    
                    .. attribute:: start_seconds
                    
                    	Start Seconds
                    	**type**\: int
                    
                    	**range:** 0..59
                    
                    	**mandatory**\: True
                    
                    	**units**\: second
                    
                    .. attribute:: start_date
                    
                    	Start Date
                    	**type**\: int
                    
                    	**range:** 1..31
                    
                    	**mandatory**\: True
                    
                    .. attribute:: start_month
                    
                    	Start Month
                    	**type**\:  :py:class:`KeyChainMonth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg.KeyChainMonth>`
                    
                    	**mandatory**\: True
                    
                    .. attribute:: start_year
                    
                    	Start Year
                    	**type**\: int
                    
                    	**range:** 1993..2035
                    
                    	**mandatory**\: True
                    
                    .. attribute:: life_time
                    
                    	Lifetime duration in seconds
                    	**type**\: int
                    
                    	**range:** 1..2147483647
                    
                    	**units**\: second
                    
                    .. attribute:: infinite_flag
                    
                    	Infinite Lifetime flag
                    	**type**\: bool
                    
                    .. attribute:: end_hour
                    
                    	End Hour
                    	**type**\: int
                    
                    	**range:** 0..23
                    
                    .. attribute:: end_minutes
                    
                    	End Minutes
                    	**type**\: int
                    
                    	**range:** 0..59
                    
                    	**units**\: minute
                    
                    .. attribute:: end_seconds
                    
                    	End Seconds
                    	**type**\: int
                    
                    	**range:** 0..59
                    
                    	**units**\: second
                    
                    .. attribute:: end_date
                    
                    	End Date
                    	**type**\: int
                    
                    	**range:** 1..31
                    
                    .. attribute:: end_month
                    
                    	End Month
                    	**type**\:  :py:class:`KeyChainMonth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg.KeyChainMonth>`
                    
                    .. attribute:: end_year
                    
                    	End Year
                    	**type**\: int
                    
                    	**range:** 1993..2035
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'lib-keychain-cfg'
                    _revision = '2018-01-31'

                    def __init__(self):
                        super(Keychains.Keychain.Keys.Key.SendLifetime, self).__init__()

                        self.yang_name = "send-lifetime"
                        self.yang_parent_name = "key"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('start_hour', (YLeaf(YType.uint32, 'start-hour'), ['int'])),
                            ('start_minutes', (YLeaf(YType.uint32, 'start-minutes'), ['int'])),
                            ('start_seconds', (YLeaf(YType.uint32, 'start-seconds'), ['int'])),
                            ('start_date', (YLeaf(YType.uint32, 'start-date'), ['int'])),
                            ('start_month', (YLeaf(YType.enumeration, 'start-month'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg', 'KeyChainMonth', '')])),
                            ('start_year', (YLeaf(YType.uint32, 'start-year'), ['int'])),
                            ('life_time', (YLeaf(YType.uint32, 'life-time'), ['int'])),
                            ('infinite_flag', (YLeaf(YType.boolean, 'infinite-flag'), ['bool'])),
                            ('end_hour', (YLeaf(YType.uint32, 'end-hour'), ['int'])),
                            ('end_minutes', (YLeaf(YType.uint32, 'end-minutes'), ['int'])),
                            ('end_seconds', (YLeaf(YType.uint32, 'end-seconds'), ['int'])),
                            ('end_date', (YLeaf(YType.uint32, 'end-date'), ['int'])),
                            ('end_month', (YLeaf(YType.enumeration, 'end-month'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg', 'KeyChainMonth', '')])),
                            ('end_year', (YLeaf(YType.uint32, 'end-year'), ['int'])),
                        ])
                        self.start_hour = None
                        self.start_minutes = None
                        self.start_seconds = None
                        self.start_date = None
                        self.start_month = None
                        self.start_year = None
                        self.life_time = None
                        self.infinite_flag = None
                        self.end_hour = None
                        self.end_minutes = None
                        self.end_seconds = None
                        self.end_date = None
                        self.end_month = None
                        self.end_year = None
                        self._segment_path = lambda: "send-lifetime"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Keychains.Keychain.Keys.Key.SendLifetime, ['start_hour', 'start_minutes', 'start_seconds', 'start_date', 'start_month', 'start_year', 'life_time', 'infinite_flag', 'end_hour', 'end_minutes', 'end_seconds', 'end_date', 'end_month', 'end_year'], name, value)

    def clone_ptr(self):
        self._top_entity = Keychains()
        return self._top_entity


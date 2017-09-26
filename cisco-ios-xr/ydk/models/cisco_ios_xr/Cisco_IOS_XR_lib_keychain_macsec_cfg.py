""" Cisco_IOS_XR_lib_keychain_macsec_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR lib\-keychain\-macsec package configuration.

This module contains definitions
for the following management objects\:
  mac\-sec\-keychains\: Configure a Key Chain

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class MacSecCryptoAlg(Enum):
    """
    MacSecCryptoAlg

    Mac sec crypto alg

    .. data:: aes_128_cmac = 7

    	aes 128 cmac

    .. data:: aes_256_cmac = 8

    	aes 256 cmac

    """

    aes_128_cmac = Enum.YLeaf(7, "aes-128-cmac")

    aes_256_cmac = Enum.YLeaf(8, "aes-256-cmac")


class MacSecEncryption(Enum):
    """
    MacSecEncryption

    Mac sec encryption

    .. data:: type7 = 0

    	Type7

    .. data:: type6 = 2

    	Type6

    """

    type7 = Enum.YLeaf(0, "type7")

    type6 = Enum.YLeaf(2, "type6")


class MacSecKeyChainMonth(Enum):
    """
    MacSecKeyChainMonth

    Mac sec key chain month

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



class MacSecKeychains(Entity):
    """
    Configure a Key Chain
    
    .. attribute:: mac_sec_keychain
    
    	Name of the key chain for MACSec
    	**type**\: list of    :py:class:`MacSecKeychain <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_macsec_cfg.MacSecKeychains.MacSecKeychain>`
    
    

    """

    _prefix = 'lib-keychain-macsec-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(MacSecKeychains, self).__init__()
        self._top_entity = None

        self.yang_name = "mac-sec-keychains"
        self.yang_parent_name = "Cisco-IOS-XR-lib-keychain-macsec-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {"mac-sec-keychain" : ("mac_sec_keychain", MacSecKeychains.MacSecKeychain)}

        self.mac_sec_keychain = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-lib-keychain-macsec-cfg:mac-sec-keychains"

    def __setattr__(self, name, value):
        self._perform_setattr(MacSecKeychains, [], name, value)


    class MacSecKeychain(Entity):
        """
        Name of the key chain for MACSec
        
        .. attribute:: chain_name  <key>
        
        	Name of the key chain
        	**type**\:  str
        
        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
        
        .. attribute:: keies
        
        	Configure a Key
        	**type**\:   :py:class:`Keies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_macsec_cfg.MacSecKeychains.MacSecKeychain.Keies>`
        
        

        """

        _prefix = 'lib-keychain-macsec-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(MacSecKeychains.MacSecKeychain, self).__init__()

            self.yang_name = "mac-sec-keychain"
            self.yang_parent_name = "mac-sec-keychains"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"keies" : ("keies", MacSecKeychains.MacSecKeychain.Keies)}
            self._child_list_classes = {}

            self.chain_name = YLeaf(YType.str, "chain-name")

            self.keies = MacSecKeychains.MacSecKeychain.Keies()
            self.keies.parent = self
            self._children_name_map["keies"] = "keies"
            self._children_yang_names.add("keies")
            self._segment_path = lambda: "mac-sec-keychain" + "[chain-name='" + self.chain_name.get() + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-lib-keychain-macsec-cfg:mac-sec-keychains/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(MacSecKeychains.MacSecKeychain, ['chain_name'], name, value)


        class Keies(Entity):
            """
            Configure a Key
            
            .. attribute:: key
            
            	Key Identifier
            	**type**\: list of    :py:class:`Key <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_macsec_cfg.MacSecKeychains.MacSecKeychain.Keies.Key>`
            
            

            """

            _prefix = 'lib-keychain-macsec-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(MacSecKeychains.MacSecKeychain.Keies, self).__init__()

                self.yang_name = "keies"
                self.yang_parent_name = "mac-sec-keychain"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {"key" : ("key", MacSecKeychains.MacSecKeychain.Keies.Key)}

                self.key = YList(self)
                self._segment_path = lambda: "keies"

            def __setattr__(self, name, value):
                self._perform_setattr(MacSecKeychains.MacSecKeychain.Keies, [], name, value)


            class Key(Entity):
                """
                Key Identifier
                
                .. attribute:: key_id  <key>
                
                	48\-bit Key identifier
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: key_string
                
                	Configure a clear text/encrypted Key string along with cryptographic algorithm
                	**type**\:   :py:class:`KeyString <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_macsec_cfg.MacSecKeychains.MacSecKeychain.Keies.Key.KeyString>`
                
                	**presence node**\: True
                
                .. attribute:: lifetime
                
                	Configure a key Lifetime
                	**type**\:   :py:class:`Lifetime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_macsec_cfg.MacSecKeychains.MacSecKeychain.Keies.Key.Lifetime>`
                
                

                """

                _prefix = 'lib-keychain-macsec-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MacSecKeychains.MacSecKeychain.Keies.Key, self).__init__()

                    self.yang_name = "key"
                    self.yang_parent_name = "keies"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"key-string" : ("key_string", MacSecKeychains.MacSecKeychain.Keies.Key.KeyString), "lifetime" : ("lifetime", MacSecKeychains.MacSecKeychain.Keies.Key.Lifetime)}
                    self._child_list_classes = {}

                    self.key_id = YLeaf(YType.str, "key-id")

                    self.key_string = None
                    self._children_name_map["key_string"] = "key-string"
                    self._children_yang_names.add("key-string")

                    self.lifetime = MacSecKeychains.MacSecKeychain.Keies.Key.Lifetime()
                    self.lifetime.parent = self
                    self._children_name_map["lifetime"] = "lifetime"
                    self._children_yang_names.add("lifetime")
                    self._segment_path = lambda: "key" + "[key-id='" + self.key_id.get() + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(MacSecKeychains.MacSecKeychain.Keies.Key, ['key_id'], name, value)


                class KeyString(Entity):
                    """
                    Configure a clear text/encrypted Key string
                    along with cryptographic algorithm
                    
                    .. attribute:: cryptographic_algorithm
                    
                    	Cryptographic Algorithm
                    	**type**\:   :py:class:`MacSecCryptoAlg <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_macsec_cfg.MacSecCryptoAlg>`
                    
                    	**mandatory**\: True
                    
                    .. attribute:: encryption_type
                    
                    	encryption type used to store key
                    	**type**\:   :py:class:`MacSecEncryption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_macsec_cfg.MacSecEncryption>`
                    
                    	**default value**\: type7
                    
                    .. attribute:: string
                    
                    	Key String
                    	**type**\:  str
                    
                    	**pattern:** (!.+)\|([^!].+)
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'lib-keychain-macsec-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MacSecKeychains.MacSecKeychain.Keies.Key.KeyString, self).__init__()

                        self.yang_name = "key-string"
                        self.yang_parent_name = "key"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.cryptographic_algorithm = YLeaf(YType.enumeration, "cryptographic-algorithm")

                        self.encryption_type = YLeaf(YType.enumeration, "encryption-type")

                        self.string = YLeaf(YType.str, "string")
                        self._segment_path = lambda: "key-string"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MacSecKeychains.MacSecKeychain.Keies.Key.KeyString, ['cryptographic_algorithm', 'encryption_type', 'string'], name, value)


                class Lifetime(Entity):
                    """
                    Configure a key Lifetime
                    
                    .. attribute:: end_date
                    
                    	End Date
                    	**type**\:  int
                    
                    	**range:** 1..31
                    
                    .. attribute:: end_hour
                    
                    	End Hour
                    	**type**\:  int
                    
                    	**range:** 0..23
                    
                    .. attribute:: end_minutes
                    
                    	End Minutes
                    	**type**\:  int
                    
                    	**range:** 0..59
                    
                    	**units**\: minute
                    
                    .. attribute:: end_month
                    
                    	End Month
                    	**type**\:   :py:class:`MacSecKeyChainMonth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_macsec_cfg.MacSecKeyChainMonth>`
                    
                    .. attribute:: end_seconds
                    
                    	End Seconds
                    	**type**\:  int
                    
                    	**range:** 0..59
                    
                    	**units**\: second
                    
                    .. attribute:: end_year
                    
                    	End Year
                    	**type**\:  int
                    
                    	**range:** 1993..2035
                    
                    .. attribute:: infinite_flag
                    
                    	Infinite Lifetime flag
                    	**type**\:  bool
                    
                    .. attribute:: life_time
                    
                    	Lifetime duration in seconds
                    	**type**\:  int
                    
                    	**range:** 1..2147483647
                    
                    	**units**\: second
                    
                    .. attribute:: start_date
                    
                    	Start Date
                    	**type**\:  int
                    
                    	**range:** 1..31
                    
                    .. attribute:: start_hour
                    
                    	Start Hour
                    	**type**\:  int
                    
                    	**range:** 0..23
                    
                    .. attribute:: start_minutes
                    
                    	Start Minutes
                    	**type**\:  int
                    
                    	**range:** 0..59
                    
                    	**units**\: minute
                    
                    .. attribute:: start_month
                    
                    	Start Month
                    	**type**\:   :py:class:`MacSecKeyChainMonth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_macsec_cfg.MacSecKeyChainMonth>`
                    
                    .. attribute:: start_seconds
                    
                    	Start Seconds
                    	**type**\:  int
                    
                    	**range:** 0..59
                    
                    	**units**\: second
                    
                    .. attribute:: start_year
                    
                    	Start Year
                    	**type**\:  int
                    
                    	**range:** 1993..2035
                    
                    

                    """

                    _prefix = 'lib-keychain-macsec-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MacSecKeychains.MacSecKeychain.Keies.Key.Lifetime, self).__init__()

                        self.yang_name = "lifetime"
                        self.yang_parent_name = "key"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.end_date = YLeaf(YType.uint32, "end-date")

                        self.end_hour = YLeaf(YType.uint32, "end-hour")

                        self.end_minutes = YLeaf(YType.uint32, "end-minutes")

                        self.end_month = YLeaf(YType.enumeration, "end-month")

                        self.end_seconds = YLeaf(YType.uint32, "end-seconds")

                        self.end_year = YLeaf(YType.uint32, "end-year")

                        self.infinite_flag = YLeaf(YType.boolean, "infinite-flag")

                        self.life_time = YLeaf(YType.uint32, "life-time")

                        self.start_date = YLeaf(YType.uint32, "start-date")

                        self.start_hour = YLeaf(YType.uint32, "start-hour")

                        self.start_minutes = YLeaf(YType.uint32, "start-minutes")

                        self.start_month = YLeaf(YType.enumeration, "start-month")

                        self.start_seconds = YLeaf(YType.uint32, "start-seconds")

                        self.start_year = YLeaf(YType.uint32, "start-year")
                        self._segment_path = lambda: "lifetime"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MacSecKeychains.MacSecKeychain.Keies.Key.Lifetime, ['end_date', 'end_hour', 'end_minutes', 'end_month', 'end_seconds', 'end_year', 'infinite_flag', 'life_time', 'start_date', 'start_hour', 'start_minutes', 'start_month', 'start_seconds', 'start_year'], name, value)

    def clone_ptr(self):
        self._top_entity = MacSecKeychains()
        return self._top_entity


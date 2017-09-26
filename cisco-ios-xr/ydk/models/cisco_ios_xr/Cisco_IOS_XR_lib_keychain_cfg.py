""" Cisco_IOS_XR_lib_keychain_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR lib\-keychain package configuration.

This module contains definitions
for the following management objects\:
  keychains\: Configure a Key Chain

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class CryptoAlg(Enum):
    """
    CryptoAlg

    Crypto alg

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

    """

    alg_hmac_sha1_12 = Enum.YLeaf(2, "alg-hmac-sha1-12")

    alg_md5_16 = Enum.YLeaf(3, "alg-md5-16")

    alg_sha1_20 = Enum.YLeaf(4, "alg-sha1-20")

    alg_hmac_md5_16 = Enum.YLeaf(5, "alg-hmac-md5-16")

    alg_hmac_sha1_20 = Enum.YLeaf(6, "alg-hmac-sha1-20")


class KeyChainMonth(Enum):
    """
    KeyChainMonth

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



class Keychains(Entity):
    """
    Configure a Key Chain
    
    .. attribute:: keychain
    
    	Name of the key chain
    	**type**\: list of    :py:class:`Keychain <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg.Keychains.Keychain>`
    
    

    """

    _prefix = 'lib-keychain-cfg'
    _revision = '2017-05-01'

    def __init__(self):
        super(Keychains, self).__init__()
        self._top_entity = None

        self.yang_name = "keychains"
        self.yang_parent_name = "Cisco-IOS-XR-lib-keychain-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {"keychain" : ("keychain", Keychains.Keychain)}

        self.keychain = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-lib-keychain-cfg:keychains"

    def __setattr__(self, name, value):
        self._perform_setattr(Keychains, [], name, value)


    class Keychain(Entity):
        """
        Name of the key chain
        
        .. attribute:: chain_name  <key>
        
        	Name of the key chain
        	**type**\:  str
        
        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
        
        .. attribute:: accept_tolerance
        
        	Accept Tolerance in seconds or infinite
        	**type**\:   :py:class:`AcceptTolerance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg.Keychains.Keychain.AcceptTolerance>`
        
        .. attribute:: keies
        
        	Configure a Key
        	**type**\:   :py:class:`Keies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg.Keychains.Keychain.Keies>`
        
        

        """

        _prefix = 'lib-keychain-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Keychains.Keychain, self).__init__()

            self.yang_name = "keychain"
            self.yang_parent_name = "keychains"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"accept-tolerance" : ("accept_tolerance", Keychains.Keychain.AcceptTolerance), "keies" : ("keies", Keychains.Keychain.Keies)}
            self._child_list_classes = {}

            self.chain_name = YLeaf(YType.str, "chain-name")

            self.accept_tolerance = Keychains.Keychain.AcceptTolerance()
            self.accept_tolerance.parent = self
            self._children_name_map["accept_tolerance"] = "accept-tolerance"
            self._children_yang_names.add("accept-tolerance")

            self.keies = Keychains.Keychain.Keies()
            self.keies.parent = self
            self._children_name_map["keies"] = "keies"
            self._children_yang_names.add("keies")
            self._segment_path = lambda: "keychain" + "[chain-name='" + self.chain_name.get() + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-lib-keychain-cfg:keychains/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Keychains.Keychain, ['chain_name'], name, value)


        class AcceptTolerance(Entity):
            """
            Accept Tolerance in seconds or infinite
            
            .. attribute:: infinite
            
            	Infinite tolerance
            	**type**\:  bool
            
            .. attribute:: value
            
            	Value in seconds
            	**type**\:  int
            
            	**range:** 1..8640000
            
            	**units**\: second
            
            

            """

            _prefix = 'lib-keychain-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Keychains.Keychain.AcceptTolerance, self).__init__()

                self.yang_name = "accept-tolerance"
                self.yang_parent_name = "keychain"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.infinite = YLeaf(YType.boolean, "infinite")

                self.value = YLeaf(YType.uint32, "value")
                self._segment_path = lambda: "accept-tolerance"

            def __setattr__(self, name, value):
                self._perform_setattr(Keychains.Keychain.AcceptTolerance, ['infinite', 'value'], name, value)


        class Keies(Entity):
            """
            Configure a Key
            
            .. attribute:: key
            
            	Key Identifier
            	**type**\: list of    :py:class:`Key <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg.Keychains.Keychain.Keies.Key>`
            
            

            """

            _prefix = 'lib-keychain-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Keychains.Keychain.Keies, self).__init__()

                self.yang_name = "keies"
                self.yang_parent_name = "keychain"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {"key" : ("key", Keychains.Keychain.Keies.Key)}

                self.key = YList(self)
                self._segment_path = lambda: "keies"

            def __setattr__(self, name, value):
                self._perform_setattr(Keychains.Keychain.Keies, [], name, value)


            class Key(Entity):
                """
                Key Identifier
                
                .. attribute:: key_id  <key>
                
                	48\-bit Key identifier
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: accept_lifetime
                
                	Configure a key Acceptance Lifetime
                	**type**\:   :py:class:`AcceptLifetime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg.Keychains.Keychain.Keies.Key.AcceptLifetime>`
                
                .. attribute:: cryptographic_algorithm
                
                	Configure the cryptographic algorithm
                	**type**\:   :py:class:`CryptoAlg <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg.CryptoAlg>`
                
                .. attribute:: key_string
                
                	Configure a clear text/encrypted Key string 
                	**type**\:  str
                
                	**pattern:** (!.+)\|([^!].+)
                
                .. attribute:: send_lifetime
                
                	Configure a Send Lifetime
                	**type**\:   :py:class:`SendLifetime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg.Keychains.Keychain.Keies.Key.SendLifetime>`
                
                

                """

                _prefix = 'lib-keychain-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Keychains.Keychain.Keies.Key, self).__init__()

                    self.yang_name = "key"
                    self.yang_parent_name = "keies"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"accept-lifetime" : ("accept_lifetime", Keychains.Keychain.Keies.Key.AcceptLifetime), "send-lifetime" : ("send_lifetime", Keychains.Keychain.Keies.Key.SendLifetime)}
                    self._child_list_classes = {}

                    self.key_id = YLeaf(YType.str, "key-id")

                    self.cryptographic_algorithm = YLeaf(YType.enumeration, "cryptographic-algorithm")

                    self.key_string = YLeaf(YType.str, "key-string")

                    self.accept_lifetime = Keychains.Keychain.Keies.Key.AcceptLifetime()
                    self.accept_lifetime.parent = self
                    self._children_name_map["accept_lifetime"] = "accept-lifetime"
                    self._children_yang_names.add("accept-lifetime")

                    self.send_lifetime = Keychains.Keychain.Keies.Key.SendLifetime()
                    self.send_lifetime.parent = self
                    self._children_name_map["send_lifetime"] = "send-lifetime"
                    self._children_yang_names.add("send-lifetime")
                    self._segment_path = lambda: "key" + "[key-id='" + self.key_id.get() + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(Keychains.Keychain.Keies.Key, ['key_id', 'cryptographic_algorithm', 'key_string'], name, value)


                class AcceptLifetime(Entity):
                    """
                    Configure a key Acceptance Lifetime
                    
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
                    	**type**\:   :py:class:`KeyChainMonth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg.KeyChainMonth>`
                    
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
                    	**type**\:   :py:class:`KeyChainMonth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg.KeyChainMonth>`
                    
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

                    _prefix = 'lib-keychain-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Keychains.Keychain.Keies.Key.AcceptLifetime, self).__init__()

                        self.yang_name = "accept-lifetime"
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
                        self._segment_path = lambda: "accept-lifetime"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Keychains.Keychain.Keies.Key.AcceptLifetime, ['end_date', 'end_hour', 'end_minutes', 'end_month', 'end_seconds', 'end_year', 'infinite_flag', 'life_time', 'start_date', 'start_hour', 'start_minutes', 'start_month', 'start_seconds', 'start_year'], name, value)


                class SendLifetime(Entity):
                    """
                    Configure a Send Lifetime
                    
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
                    	**type**\:   :py:class:`KeyChainMonth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg.KeyChainMonth>`
                    
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
                    	**type**\:   :py:class:`KeyChainMonth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg.KeyChainMonth>`
                    
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

                    _prefix = 'lib-keychain-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Keychains.Keychain.Keies.Key.SendLifetime, self).__init__()

                        self.yang_name = "send-lifetime"
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
                        self._segment_path = lambda: "send-lifetime"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Keychains.Keychain.Keies.Key.SendLifetime, ['end_date', 'end_hour', 'end_minutes', 'end_month', 'end_seconds', 'end_year', 'infinite_flag', 'life_time', 'start_date', 'start_hour', 'start_minutes', 'start_month', 'start_seconds', 'start_year'], name, value)

    def clone_ptr(self):
        self._top_entity = Keychains()
        return self._top_entity


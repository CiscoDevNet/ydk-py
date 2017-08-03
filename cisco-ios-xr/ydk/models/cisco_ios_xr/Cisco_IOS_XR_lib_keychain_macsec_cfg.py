""" Cisco_IOS_XR_lib_keychain_macsec_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR lib\-keychain\-macsec package configuration.

This module contains definitions
for the following management objects\:
  mac\-sec\-keychains\: Configure a Key Chain

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
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

        self.mac_sec_keychain = YList(self)

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in () and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(MacSecKeychains, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(MacSecKeychains, self).__setattr__(name, value)


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

            self.chain_name = YLeaf(YType.str, "chain-name")

            self.keies = MacSecKeychains.MacSecKeychain.Keies()
            self.keies.parent = self
            self._children_name_map["keies"] = "keies"
            self._children_yang_names.add("keies")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("chain_name") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(MacSecKeychains.MacSecKeychain, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MacSecKeychains.MacSecKeychain, self).__setattr__(name, value)


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

                self.key = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MacSecKeychains.MacSecKeychain.Keies, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MacSecKeychains.MacSecKeychain.Keies, self).__setattr__(name, value)


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

                    self.key_id = YLeaf(YType.str, "key-id")

                    self.key_string = None
                    self._children_name_map["key_string"] = "key-string"
                    self._children_yang_names.add("key-string")

                    self.lifetime = MacSecKeychains.MacSecKeychain.Keies.Key.Lifetime()
                    self.lifetime.parent = self
                    self._children_name_map["lifetime"] = "lifetime"
                    self._children_yang_names.add("lifetime")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("key_id") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MacSecKeychains.MacSecKeychain.Keies.Key, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MacSecKeychains.MacSecKeychain.Keies.Key, self).__setattr__(name, value)


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

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("end_date",
                                        "end_hour",
                                        "end_minutes",
                                        "end_month",
                                        "end_seconds",
                                        "end_year",
                                        "infinite_flag",
                                        "life_time",
                                        "start_date",
                                        "start_hour",
                                        "start_minutes",
                                        "start_month",
                                        "start_seconds",
                                        "start_year") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MacSecKeychains.MacSecKeychain.Keies.Key.Lifetime, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MacSecKeychains.MacSecKeychain.Keies.Key.Lifetime, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.end_date.is_set or
                            self.end_hour.is_set or
                            self.end_minutes.is_set or
                            self.end_month.is_set or
                            self.end_seconds.is_set or
                            self.end_year.is_set or
                            self.infinite_flag.is_set or
                            self.life_time.is_set or
                            self.start_date.is_set or
                            self.start_hour.is_set or
                            self.start_minutes.is_set or
                            self.start_month.is_set or
                            self.start_seconds.is_set or
                            self.start_year.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.end_date.yfilter != YFilter.not_set or
                            self.end_hour.yfilter != YFilter.not_set or
                            self.end_minutes.yfilter != YFilter.not_set or
                            self.end_month.yfilter != YFilter.not_set or
                            self.end_seconds.yfilter != YFilter.not_set or
                            self.end_year.yfilter != YFilter.not_set or
                            self.infinite_flag.yfilter != YFilter.not_set or
                            self.life_time.yfilter != YFilter.not_set or
                            self.start_date.yfilter != YFilter.not_set or
                            self.start_hour.yfilter != YFilter.not_set or
                            self.start_minutes.yfilter != YFilter.not_set or
                            self.start_month.yfilter != YFilter.not_set or
                            self.start_seconds.yfilter != YFilter.not_set or
                            self.start_year.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "lifetime" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.end_date.is_set or self.end_date.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.end_date.get_name_leafdata())
                        if (self.end_hour.is_set or self.end_hour.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.end_hour.get_name_leafdata())
                        if (self.end_minutes.is_set or self.end_minutes.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.end_minutes.get_name_leafdata())
                        if (self.end_month.is_set or self.end_month.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.end_month.get_name_leafdata())
                        if (self.end_seconds.is_set or self.end_seconds.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.end_seconds.get_name_leafdata())
                        if (self.end_year.is_set or self.end_year.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.end_year.get_name_leafdata())
                        if (self.infinite_flag.is_set or self.infinite_flag.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.infinite_flag.get_name_leafdata())
                        if (self.life_time.is_set or self.life_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.life_time.get_name_leafdata())
                        if (self.start_date.is_set or self.start_date.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.start_date.get_name_leafdata())
                        if (self.start_hour.is_set or self.start_hour.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.start_hour.get_name_leafdata())
                        if (self.start_minutes.is_set or self.start_minutes.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.start_minutes.get_name_leafdata())
                        if (self.start_month.is_set or self.start_month.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.start_month.get_name_leafdata())
                        if (self.start_seconds.is_set or self.start_seconds.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.start_seconds.get_name_leafdata())
                        if (self.start_year.is_set or self.start_year.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.start_year.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "end-date" or name == "end-hour" or name == "end-minutes" or name == "end-month" or name == "end-seconds" or name == "end-year" or name == "infinite-flag" or name == "life-time" or name == "start-date" or name == "start-hour" or name == "start-minutes" or name == "start-month" or name == "start-seconds" or name == "start-year"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "end-date"):
                            self.end_date = value
                            self.end_date.value_namespace = name_space
                            self.end_date.value_namespace_prefix = name_space_prefix
                        if(value_path == "end-hour"):
                            self.end_hour = value
                            self.end_hour.value_namespace = name_space
                            self.end_hour.value_namespace_prefix = name_space_prefix
                        if(value_path == "end-minutes"):
                            self.end_minutes = value
                            self.end_minutes.value_namespace = name_space
                            self.end_minutes.value_namespace_prefix = name_space_prefix
                        if(value_path == "end-month"):
                            self.end_month = value
                            self.end_month.value_namespace = name_space
                            self.end_month.value_namespace_prefix = name_space_prefix
                        if(value_path == "end-seconds"):
                            self.end_seconds = value
                            self.end_seconds.value_namespace = name_space
                            self.end_seconds.value_namespace_prefix = name_space_prefix
                        if(value_path == "end-year"):
                            self.end_year = value
                            self.end_year.value_namespace = name_space
                            self.end_year.value_namespace_prefix = name_space_prefix
                        if(value_path == "infinite-flag"):
                            self.infinite_flag = value
                            self.infinite_flag.value_namespace = name_space
                            self.infinite_flag.value_namespace_prefix = name_space_prefix
                        if(value_path == "life-time"):
                            self.life_time = value
                            self.life_time.value_namespace = name_space
                            self.life_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "start-date"):
                            self.start_date = value
                            self.start_date.value_namespace = name_space
                            self.start_date.value_namespace_prefix = name_space_prefix
                        if(value_path == "start-hour"):
                            self.start_hour = value
                            self.start_hour.value_namespace = name_space
                            self.start_hour.value_namespace_prefix = name_space_prefix
                        if(value_path == "start-minutes"):
                            self.start_minutes = value
                            self.start_minutes.value_namespace = name_space
                            self.start_minutes.value_namespace_prefix = name_space_prefix
                        if(value_path == "start-month"):
                            self.start_month = value
                            self.start_month.value_namespace = name_space
                            self.start_month.value_namespace_prefix = name_space_prefix
                        if(value_path == "start-seconds"):
                            self.start_seconds = value
                            self.start_seconds.value_namespace = name_space
                            self.start_seconds.value_namespace_prefix = name_space_prefix
                        if(value_path == "start-year"):
                            self.start_year = value
                            self.start_year.value_namespace = name_space
                            self.start_year.value_namespace_prefix = name_space_prefix


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
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**default value**\: 0
                    
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
                        self.is_presence_container = True

                        self.cryptographic_algorithm = YLeaf(YType.enumeration, "cryptographic-algorithm")

                        self.encryption_type = YLeaf(YType.int32, "encryption-type")

                        self.string = YLeaf(YType.str, "string")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("cryptographic_algorithm",
                                        "encryption_type",
                                        "string") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MacSecKeychains.MacSecKeychain.Keies.Key.KeyString, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MacSecKeychains.MacSecKeychain.Keies.Key.KeyString, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.cryptographic_algorithm.is_set or
                            self.encryption_type.is_set or
                            self.string.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.cryptographic_algorithm.yfilter != YFilter.not_set or
                            self.encryption_type.yfilter != YFilter.not_set or
                            self.string.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "key-string" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.cryptographic_algorithm.is_set or self.cryptographic_algorithm.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.cryptographic_algorithm.get_name_leafdata())
                        if (self.encryption_type.is_set or self.encryption_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.encryption_type.get_name_leafdata())
                        if (self.string.is_set or self.string.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.string.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "cryptographic-algorithm" or name == "encryption-type" or name == "string"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "cryptographic-algorithm"):
                            self.cryptographic_algorithm = value
                            self.cryptographic_algorithm.value_namespace = name_space
                            self.cryptographic_algorithm.value_namespace_prefix = name_space_prefix
                        if(value_path == "encryption-type"):
                            self.encryption_type = value
                            self.encryption_type.value_namespace = name_space
                            self.encryption_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "string"):
                            self.string = value
                            self.string.value_namespace = name_space
                            self.string.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.key_id.is_set or
                        (self.lifetime is not None and self.lifetime.has_data()) or
                        (self.key_string is not None))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.key_id.yfilter != YFilter.not_set or
                        (self.key_string is not None and self.key_string.has_operation()) or
                        (self.lifetime is not None and self.lifetime.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "key" + "[key-id='" + self.key_id.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.key_id.is_set or self.key_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.key_id.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "key-string"):
                        if (self.key_string is None):
                            self.key_string = MacSecKeychains.MacSecKeychain.Keies.Key.KeyString()
                            self.key_string.parent = self
                            self._children_name_map["key_string"] = "key-string"
                        return self.key_string

                    if (child_yang_name == "lifetime"):
                        if (self.lifetime is None):
                            self.lifetime = MacSecKeychains.MacSecKeychain.Keies.Key.Lifetime()
                            self.lifetime.parent = self
                            self._children_name_map["lifetime"] = "lifetime"
                        return self.lifetime

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "key-string" or name == "lifetime" or name == "key-id"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "key-id"):
                        self.key_id = value
                        self.key_id.value_namespace = name_space
                        self.key_id.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.key:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.key:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "keies" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "key"):
                    for c in self.key:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = MacSecKeychains.MacSecKeychain.Keies.Key()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.key.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "key"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                self.chain_name.is_set or
                (self.keies is not None and self.keies.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.chain_name.yfilter != YFilter.not_set or
                (self.keies is not None and self.keies.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mac-sec-keychain" + "[chain-name='" + self.chain_name.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-lib-keychain-macsec-cfg:mac-sec-keychains/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.chain_name.is_set or self.chain_name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.chain_name.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "keies"):
                if (self.keies is None):
                    self.keies = MacSecKeychains.MacSecKeychain.Keies()
                    self.keies.parent = self
                    self._children_name_map["keies"] = "keies"
                return self.keies

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "keies" or name == "chain-name"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "chain-name"):
                self.chain_name = value
                self.chain_name.value_namespace = name_space
                self.chain_name.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.mac_sec_keychain:
            if (c.has_data()):
                return True
        return False

    def has_operation(self):
        for c in self.mac_sec_keychain:
            if (c.has_operation()):
                return True
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-lib-keychain-macsec-cfg:mac-sec-keychains" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "mac-sec-keychain"):
            for c in self.mac_sec_keychain:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = MacSecKeychains.MacSecKeychain()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.mac_sec_keychain.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "mac-sec-keychain"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = MacSecKeychains()
        return self._top_entity


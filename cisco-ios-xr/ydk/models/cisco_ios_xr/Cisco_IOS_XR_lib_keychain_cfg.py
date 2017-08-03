""" Cisco_IOS_XR_lib_keychain_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR lib\-keychain package configuration.

This module contains definitions
for the following management objects\:
  keychains\: Configure a Key Chain

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
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
    _revision = '2015-07-30'

    def __init__(self):
        super(Keychains, self).__init__()
        self._top_entity = None

        self.yang_name = "keychains"
        self.yang_parent_name = "Cisco-IOS-XR-lib-keychain-cfg"

        self.keychain = YList(self)

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
                    super(Keychains, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Keychains, self).__setattr__(name, value)


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
        _revision = '2015-07-30'

        def __init__(self):
            super(Keychains.Keychain, self).__init__()

            self.yang_name = "keychain"
            self.yang_parent_name = "keychains"

            self.chain_name = YLeaf(YType.str, "chain-name")

            self.accept_tolerance = Keychains.Keychain.AcceptTolerance()
            self.accept_tolerance.parent = self
            self._children_name_map["accept_tolerance"] = "accept-tolerance"
            self._children_yang_names.add("accept-tolerance")

            self.keies = Keychains.Keychain.Keies()
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
                        super(Keychains.Keychain, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Keychains.Keychain, self).__setattr__(name, value)


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
            _revision = '2015-07-30'

            def __init__(self):
                super(Keychains.Keychain.AcceptTolerance, self).__init__()

                self.yang_name = "accept-tolerance"
                self.yang_parent_name = "keychain"

                self.infinite = YLeaf(YType.boolean, "infinite")

                self.value = YLeaf(YType.uint32, "value")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("infinite",
                                "value") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Keychains.Keychain.AcceptTolerance, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Keychains.Keychain.AcceptTolerance, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.infinite.is_set or
                    self.value.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.infinite.yfilter != YFilter.not_set or
                    self.value.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "accept-tolerance" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.infinite.is_set or self.infinite.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.infinite.get_name_leafdata())
                if (self.value.is_set or self.value.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.value.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "infinite" or name == "value"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "infinite"):
                    self.infinite = value
                    self.infinite.value_namespace = name_space
                    self.infinite.value_namespace_prefix = name_space_prefix
                if(value_path == "value"):
                    self.value = value
                    self.value.value_namespace = name_space
                    self.value.value_namespace_prefix = name_space_prefix


        class Keies(Entity):
            """
            Configure a Key
            
            .. attribute:: key
            
            	Key Identifier
            	**type**\: list of    :py:class:`Key <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg.Keychains.Keychain.Keies.Key>`
            
            

            """

            _prefix = 'lib-keychain-cfg'
            _revision = '2015-07-30'

            def __init__(self):
                super(Keychains.Keychain.Keies, self).__init__()

                self.yang_name = "keies"
                self.yang_parent_name = "keychain"

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
                            super(Keychains.Keychain.Keies, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Keychains.Keychain.Keies, self).__setattr__(name, value)


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
                _revision = '2015-07-30'

                def __init__(self):
                    super(Keychains.Keychain.Keies.Key, self).__init__()

                    self.yang_name = "key"
                    self.yang_parent_name = "keies"

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

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("key_id",
                                    "cryptographic_algorithm",
                                    "key_string") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Keychains.Keychain.Keies.Key, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Keychains.Keychain.Keies.Key, self).__setattr__(name, value)


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
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(Keychains.Keychain.Keies.Key.AcceptLifetime, self).__init__()

                        self.yang_name = "accept-lifetime"
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
                                    super(Keychains.Keychain.Keies.Key.AcceptLifetime, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Keychains.Keychain.Keies.Key.AcceptLifetime, self).__setattr__(name, value)

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
                        path_buffer = "accept-lifetime" + path_buffer

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
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(Keychains.Keychain.Keies.Key.SendLifetime, self).__init__()

                        self.yang_name = "send-lifetime"
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
                                    super(Keychains.Keychain.Keies.Key.SendLifetime, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Keychains.Keychain.Keies.Key.SendLifetime, self).__setattr__(name, value)

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
                        path_buffer = "send-lifetime" + path_buffer

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

                def has_data(self):
                    return (
                        self.key_id.is_set or
                        self.cryptographic_algorithm.is_set or
                        self.key_string.is_set or
                        (self.accept_lifetime is not None and self.accept_lifetime.has_data()) or
                        (self.send_lifetime is not None and self.send_lifetime.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.key_id.yfilter != YFilter.not_set or
                        self.cryptographic_algorithm.yfilter != YFilter.not_set or
                        self.key_string.yfilter != YFilter.not_set or
                        (self.accept_lifetime is not None and self.accept_lifetime.has_operation()) or
                        (self.send_lifetime is not None and self.send_lifetime.has_operation()))

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
                    if (self.cryptographic_algorithm.is_set or self.cryptographic_algorithm.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.cryptographic_algorithm.get_name_leafdata())
                    if (self.key_string.is_set or self.key_string.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.key_string.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "accept-lifetime"):
                        if (self.accept_lifetime is None):
                            self.accept_lifetime = Keychains.Keychain.Keies.Key.AcceptLifetime()
                            self.accept_lifetime.parent = self
                            self._children_name_map["accept_lifetime"] = "accept-lifetime"
                        return self.accept_lifetime

                    if (child_yang_name == "send-lifetime"):
                        if (self.send_lifetime is None):
                            self.send_lifetime = Keychains.Keychain.Keies.Key.SendLifetime()
                            self.send_lifetime.parent = self
                            self._children_name_map["send_lifetime"] = "send-lifetime"
                        return self.send_lifetime

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "accept-lifetime" or name == "send-lifetime" or name == "key-id" or name == "cryptographic-algorithm" or name == "key-string"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "key-id"):
                        self.key_id = value
                        self.key_id.value_namespace = name_space
                        self.key_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "cryptographic-algorithm"):
                        self.cryptographic_algorithm = value
                        self.cryptographic_algorithm.value_namespace = name_space
                        self.cryptographic_algorithm.value_namespace_prefix = name_space_prefix
                    if(value_path == "key-string"):
                        self.key_string = value
                        self.key_string.value_namespace = name_space
                        self.key_string.value_namespace_prefix = name_space_prefix

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
                    c = Keychains.Keychain.Keies.Key()
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
                (self.accept_tolerance is not None and self.accept_tolerance.has_data()) or
                (self.keies is not None and self.keies.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.chain_name.yfilter != YFilter.not_set or
                (self.accept_tolerance is not None and self.accept_tolerance.has_operation()) or
                (self.keies is not None and self.keies.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "keychain" + "[chain-name='" + self.chain_name.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-lib-keychain-cfg:keychains/%s" % self.get_segment_path()
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

            if (child_yang_name == "accept-tolerance"):
                if (self.accept_tolerance is None):
                    self.accept_tolerance = Keychains.Keychain.AcceptTolerance()
                    self.accept_tolerance.parent = self
                    self._children_name_map["accept_tolerance"] = "accept-tolerance"
                return self.accept_tolerance

            if (child_yang_name == "keies"):
                if (self.keies is None):
                    self.keies = Keychains.Keychain.Keies()
                    self.keies.parent = self
                    self._children_name_map["keies"] = "keies"
                return self.keies

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "accept-tolerance" or name == "keies" or name == "chain-name"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "chain-name"):
                self.chain_name = value
                self.chain_name.value_namespace = name_space
                self.chain_name.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.keychain:
            if (c.has_data()):
                return True
        return False

    def has_operation(self):
        for c in self.keychain:
            if (c.has_operation()):
                return True
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-lib-keychain-cfg:keychains" + path_buffer

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

        if (child_yang_name == "keychain"):
            for c in self.keychain:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = Keychains.Keychain()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.keychain.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "keychain"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Keychains()
        return self._top_entity


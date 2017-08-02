""" Cisco_IOS_XR_lib_keychain_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR lib\-keychain package operational data.

This module contains definitions
for the following management objects\:
  keychain\: Keychain operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class CrytoAlgo(Enum):
    """
    CrytoAlgo

    Cryptographic algorithm type

    .. data:: not_configured = 0

    	Not configured

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

    """

    not_configured = Enum.YLeaf(0, "not-configured")

    hmac_sha1_12 = Enum.YLeaf(2, "hmac-sha1-12")

    md5 = Enum.YLeaf(3, "md5")

    sha1 = Enum.YLeaf(4, "sha1")

    hmac_md5 = Enum.YLeaf(5, "hmac-md5")

    hmac_sha1_20 = Enum.YLeaf(6, "hmac-sha1-20")

    aes_128_cmac = Enum.YLeaf(7, "aes-128-cmac")

    aes_256_cmac = Enum.YLeaf(8, "aes-256-cmac")


class Enc(Enum):
    """
    Enc

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
    
    .. attribute:: keies
    
    	List of configured key names
    	**type**\:   :py:class:`Keies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper.Keychain.Keies>`
    
    

    """

    _prefix = 'lib-keychain-oper'
    _revision = '2015-01-07'

    def __init__(self):
        super(Keychain, self).__init__()
        self._top_entity = None

        self.yang_name = "keychain"
        self.yang_parent_name = "Cisco-IOS-XR-lib-keychain-oper"

        self.keies = Keychain.Keies()
        self.keies.parent = self
        self._children_name_map["keies"] = "keies"
        self._children_yang_names.add("keies")


    class Keies(Entity):
        """
        List of configured key names
        
        .. attribute:: key
        
        	Configured key name
        	**type**\: list of    :py:class:`Key <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper.Keychain.Keies.Key>`
        
        

        """

        _prefix = 'lib-keychain-oper'
        _revision = '2015-01-07'

        def __init__(self):
            super(Keychain.Keies, self).__init__()

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
                        super(Keychain.Keies, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Keychain.Keies, self).__setattr__(name, value)


        class Key(Entity):
            """
            Configured key name
            
            .. attribute:: key_name  <key>
            
            	Key name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: accept_tolerance
            
            	Accept tolerance is infinite if value is 0xffffffff
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: key
            
            	Key properties
            	**type**\:   :py:class:`Key <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper.Keychain.Keies.Key.Key>`
            
            

            """

            _prefix = 'lib-keychain-oper'
            _revision = '2015-01-07'

            def __init__(self):
                super(Keychain.Keies.Key, self).__init__()

                self.yang_name = "key"
                self.yang_parent_name = "keies"

                self.key_name = YLeaf(YType.str, "key-name")

                self.accept_tolerance = YLeaf(YType.int32, "accept-tolerance")

                self.key = Keychain.Keies.Key.Key()
                self.key.parent = self
                self._children_name_map["key"] = "key"
                self._children_yang_names.add("key")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("key_name",
                                "accept_tolerance") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Keychain.Keies.Key, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Keychain.Keies.Key, self).__setattr__(name, value)


            class Key(Entity):
                """
                Key properties
                
                .. attribute:: key_id
                
                	key id
                	**type**\: list of    :py:class:`KeyId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper.Keychain.Keies.Key.Key.KeyId>`
                
                

                """

                _prefix = 'lib-keychain-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    super(Keychain.Keies.Key.Key, self).__init__()

                    self.yang_name = "key"
                    self.yang_parent_name = "key"

                    self.key_id = YList(self)

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
                                super(Keychain.Keies.Key.Key, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Keychain.Keies.Key.Key, self).__setattr__(name, value)


                class KeyId(Entity):
                    """
                    key id
                    
                    .. attribute:: accept_lifetime
                    
                    	Accept Lifetime of the key
                    	**type**\:   :py:class:`AcceptLifetime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper.Keychain.Keies.Key.Key.KeyId.AcceptLifetime>`
                    
                    .. attribute:: cryptographic_algorithm
                    
                    	Cryptographic algorithm
                    	**type**\:   :py:class:`CrytoAlgo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper.CrytoAlgo>`
                    
                    .. attribute:: key_id
                    
                    	Key ID
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: key_string
                    
                    	Key string
                    	**type**\:  str
                    
                    .. attribute:: macsec
                    
                    	To check if it's a macsec key
                    	**type**\:   :py:class:`Macsec <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper.Keychain.Keies.Key.Key.KeyId.Macsec>`
                    
                    .. attribute:: send_lifetime
                    
                    	Lifetime of the key
                    	**type**\:   :py:class:`SendLifetime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper.Keychain.Keies.Key.Key.KeyId.SendLifetime>`
                    
                    .. attribute:: type
                    
                    	Type of key encryption
                    	**type**\:   :py:class:`Enc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper.Enc>`
                    
                    

                    """

                    _prefix = 'lib-keychain-oper'
                    _revision = '2015-01-07'

                    def __init__(self):
                        super(Keychain.Keies.Key.Key.KeyId, self).__init__()

                        self.yang_name = "key-id"
                        self.yang_parent_name = "key"

                        self.cryptographic_algorithm = YLeaf(YType.enumeration, "cryptographic-algorithm")

                        self.key_id = YLeaf(YType.uint64, "key-id")

                        self.key_string = YLeaf(YType.str, "key-string")

                        self.type = YLeaf(YType.enumeration, "type")

                        self.accept_lifetime = Keychain.Keies.Key.Key.KeyId.AcceptLifetime()
                        self.accept_lifetime.parent = self
                        self._children_name_map["accept_lifetime"] = "accept-lifetime"
                        self._children_yang_names.add("accept-lifetime")

                        self.macsec = Keychain.Keies.Key.Key.KeyId.Macsec()
                        self.macsec.parent = self
                        self._children_name_map["macsec"] = "macsec"
                        self._children_yang_names.add("macsec")

                        self.send_lifetime = Keychain.Keies.Key.Key.KeyId.SendLifetime()
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
                            if name in ("cryptographic_algorithm",
                                        "key_id",
                                        "key_string",
                                        "type") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Keychain.Keies.Key.Key.KeyId, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Keychain.Keies.Key.Key.KeyId, self).__setattr__(name, value)


                    class Macsec(Entity):
                        """
                        To check if it's a macsec key
                        
                        .. attribute:: is_macsec_key
                        
                        	To check if it's a macsec key
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'lib-keychain-oper'
                        _revision = '2015-01-07'

                        def __init__(self):
                            super(Keychain.Keies.Key.Key.KeyId.Macsec, self).__init__()

                            self.yang_name = "macsec"
                            self.yang_parent_name = "key-id"

                            self.is_macsec_key = YLeaf(YType.boolean, "is-macsec-key")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("is_macsec_key") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Keychain.Keies.Key.Key.KeyId.Macsec, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Keychain.Keies.Key.Key.KeyId.Macsec, self).__setattr__(name, value)

                        def has_data(self):
                            return self.is_macsec_key.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.is_macsec_key.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "macsec" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.is_macsec_key.is_set or self.is_macsec_key.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_macsec_key.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "is-macsec-key"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "is-macsec-key"):
                                self.is_macsec_key = value
                                self.is_macsec_key.value_namespace = name_space
                                self.is_macsec_key.value_namespace_prefix = name_space_prefix


                    class SendLifetime(Entity):
                        """
                        Lifetime of the key
                        
                        .. attribute:: duration
                        
                        	Duration of the key in seconds. value 0xffffffff reflects infinite, never expires, is configured 
                        	**type**\:  str
                        
                        	**units**\: second
                        
                        .. attribute:: end
                        
                        	Key life end time in format \: day\-of\-week month date\-of\-month HH\:MM\:SS year eg\: Thu Feb 1 18\:32 \:14 2011
                        	**type**\:  str
                        
                        .. attribute:: is_always_valid
                        
                        	Is TRUE if duration is 0xffffffff 
                        	**type**\:  bool
                        
                        .. attribute:: is_valid_now
                        
                        	Is TRUE if current time is betweenstart and end lifetime , else FALSE
                        	**type**\:  bool
                        
                        .. attribute:: start
                        
                        	Key life start time in format \: day\-of\-week month date\-of\-month HH\:MM\:SS year eg\: Thu Feb 1 18\:32\:14 2011
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'lib-keychain-oper'
                        _revision = '2015-01-07'

                        def __init__(self):
                            super(Keychain.Keies.Key.Key.KeyId.SendLifetime, self).__init__()

                            self.yang_name = "send-lifetime"
                            self.yang_parent_name = "key-id"

                            self.duration = YLeaf(YType.str, "duration")

                            self.end = YLeaf(YType.str, "end")

                            self.is_always_valid = YLeaf(YType.boolean, "is-always-valid")

                            self.is_valid_now = YLeaf(YType.boolean, "is-valid-now")

                            self.start = YLeaf(YType.str, "start")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("duration",
                                            "end",
                                            "is_always_valid",
                                            "is_valid_now",
                                            "start") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Keychain.Keies.Key.Key.KeyId.SendLifetime, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Keychain.Keies.Key.Key.KeyId.SendLifetime, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.duration.is_set or
                                self.end.is_set or
                                self.is_always_valid.is_set or
                                self.is_valid_now.is_set or
                                self.start.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.duration.yfilter != YFilter.not_set or
                                self.end.yfilter != YFilter.not_set or
                                self.is_always_valid.yfilter != YFilter.not_set or
                                self.is_valid_now.yfilter != YFilter.not_set or
                                self.start.yfilter != YFilter.not_set)

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
                            if (self.duration.is_set or self.duration.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.duration.get_name_leafdata())
                            if (self.end.is_set or self.end.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.end.get_name_leafdata())
                            if (self.is_always_valid.is_set or self.is_always_valid.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_always_valid.get_name_leafdata())
                            if (self.is_valid_now.is_set or self.is_valid_now.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_valid_now.get_name_leafdata())
                            if (self.start.is_set or self.start.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.start.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "duration" or name == "end" or name == "is-always-valid" or name == "is-valid-now" or name == "start"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "duration"):
                                self.duration = value
                                self.duration.value_namespace = name_space
                                self.duration.value_namespace_prefix = name_space_prefix
                            if(value_path == "end"):
                                self.end = value
                                self.end.value_namespace = name_space
                                self.end.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-always-valid"):
                                self.is_always_valid = value
                                self.is_always_valid.value_namespace = name_space
                                self.is_always_valid.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-valid-now"):
                                self.is_valid_now = value
                                self.is_valid_now.value_namespace = name_space
                                self.is_valid_now.value_namespace_prefix = name_space_prefix
                            if(value_path == "start"):
                                self.start = value
                                self.start.value_namespace = name_space
                                self.start.value_namespace_prefix = name_space_prefix


                    class AcceptLifetime(Entity):
                        """
                        Accept Lifetime of the key
                        
                        .. attribute:: duration
                        
                        	Duration of the key in seconds. value 0xffffffff reflects infinite, never expires, is configured 
                        	**type**\:  str
                        
                        	**units**\: second
                        
                        .. attribute:: end
                        
                        	Key life end time in format \: day\-of\-week month date\-of\-month HH\:MM\:SS year eg\: Thu Feb 1 18\:32 \:14 2011
                        	**type**\:  str
                        
                        .. attribute:: is_always_valid
                        
                        	Is TRUE if duration is 0xffffffff 
                        	**type**\:  bool
                        
                        .. attribute:: is_valid_now
                        
                        	Is TRUE if current time is betweenstart and end lifetime , else FALSE
                        	**type**\:  bool
                        
                        .. attribute:: start
                        
                        	Key life start time in format \: day\-of\-week month date\-of\-month HH\:MM\:SS year eg\: Thu Feb 1 18\:32\:14 2011
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'lib-keychain-oper'
                        _revision = '2015-01-07'

                        def __init__(self):
                            super(Keychain.Keies.Key.Key.KeyId.AcceptLifetime, self).__init__()

                            self.yang_name = "accept-lifetime"
                            self.yang_parent_name = "key-id"

                            self.duration = YLeaf(YType.str, "duration")

                            self.end = YLeaf(YType.str, "end")

                            self.is_always_valid = YLeaf(YType.boolean, "is-always-valid")

                            self.is_valid_now = YLeaf(YType.boolean, "is-valid-now")

                            self.start = YLeaf(YType.str, "start")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("duration",
                                            "end",
                                            "is_always_valid",
                                            "is_valid_now",
                                            "start") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Keychain.Keies.Key.Key.KeyId.AcceptLifetime, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Keychain.Keies.Key.Key.KeyId.AcceptLifetime, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.duration.is_set or
                                self.end.is_set or
                                self.is_always_valid.is_set or
                                self.is_valid_now.is_set or
                                self.start.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.duration.yfilter != YFilter.not_set or
                                self.end.yfilter != YFilter.not_set or
                                self.is_always_valid.yfilter != YFilter.not_set or
                                self.is_valid_now.yfilter != YFilter.not_set or
                                self.start.yfilter != YFilter.not_set)

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
                            if (self.duration.is_set or self.duration.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.duration.get_name_leafdata())
                            if (self.end.is_set or self.end.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.end.get_name_leafdata())
                            if (self.is_always_valid.is_set or self.is_always_valid.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_always_valid.get_name_leafdata())
                            if (self.is_valid_now.is_set or self.is_valid_now.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_valid_now.get_name_leafdata())
                            if (self.start.is_set or self.start.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.start.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "duration" or name == "end" or name == "is-always-valid" or name == "is-valid-now" or name == "start"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "duration"):
                                self.duration = value
                                self.duration.value_namespace = name_space
                                self.duration.value_namespace_prefix = name_space_prefix
                            if(value_path == "end"):
                                self.end = value
                                self.end.value_namespace = name_space
                                self.end.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-always-valid"):
                                self.is_always_valid = value
                                self.is_always_valid.value_namespace = name_space
                                self.is_always_valid.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-valid-now"):
                                self.is_valid_now = value
                                self.is_valid_now.value_namespace = name_space
                                self.is_valid_now.value_namespace_prefix = name_space_prefix
                            if(value_path == "start"):
                                self.start = value
                                self.start.value_namespace = name_space
                                self.start.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.cryptographic_algorithm.is_set or
                            self.key_id.is_set or
                            self.key_string.is_set or
                            self.type.is_set or
                            (self.accept_lifetime is not None and self.accept_lifetime.has_data()) or
                            (self.macsec is not None and self.macsec.has_data()) or
                            (self.send_lifetime is not None and self.send_lifetime.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.cryptographic_algorithm.yfilter != YFilter.not_set or
                            self.key_id.yfilter != YFilter.not_set or
                            self.key_string.yfilter != YFilter.not_set or
                            self.type.yfilter != YFilter.not_set or
                            (self.accept_lifetime is not None and self.accept_lifetime.has_operation()) or
                            (self.macsec is not None and self.macsec.has_operation()) or
                            (self.send_lifetime is not None and self.send_lifetime.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "key-id" + path_buffer

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
                        if (self.key_id.is_set or self.key_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.key_id.get_name_leafdata())
                        if (self.key_string.is_set or self.key_string.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.key_string.get_name_leafdata())
                        if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.type.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "accept-lifetime"):
                            if (self.accept_lifetime is None):
                                self.accept_lifetime = Keychain.Keies.Key.Key.KeyId.AcceptLifetime()
                                self.accept_lifetime.parent = self
                                self._children_name_map["accept_lifetime"] = "accept-lifetime"
                            return self.accept_lifetime

                        if (child_yang_name == "macsec"):
                            if (self.macsec is None):
                                self.macsec = Keychain.Keies.Key.Key.KeyId.Macsec()
                                self.macsec.parent = self
                                self._children_name_map["macsec"] = "macsec"
                            return self.macsec

                        if (child_yang_name == "send-lifetime"):
                            if (self.send_lifetime is None):
                                self.send_lifetime = Keychain.Keies.Key.Key.KeyId.SendLifetime()
                                self.send_lifetime.parent = self
                                self._children_name_map["send_lifetime"] = "send-lifetime"
                            return self.send_lifetime

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "accept-lifetime" or name == "macsec" or name == "send-lifetime" or name == "cryptographic-algorithm" or name == "key-id" or name == "key-string" or name == "type"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "cryptographic-algorithm"):
                            self.cryptographic_algorithm = value
                            self.cryptographic_algorithm.value_namespace = name_space
                            self.cryptographic_algorithm.value_namespace_prefix = name_space_prefix
                        if(value_path == "key-id"):
                            self.key_id = value
                            self.key_id.value_namespace = name_space
                            self.key_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "key-string"):
                            self.key_string = value
                            self.key_string.value_namespace = name_space
                            self.key_string.value_namespace_prefix = name_space_prefix
                        if(value_path == "type"):
                            self.type = value
                            self.type.value_namespace = name_space
                            self.type.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.key_id:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.key_id:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "key" + path_buffer

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

                    if (child_yang_name == "key-id"):
                        for c in self.key_id:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Keychain.Keies.Key.Key.KeyId()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.key_id.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "key-id"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.key_name.is_set or
                    self.accept_tolerance.is_set or
                    (self.key is not None and self.key.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.key_name.yfilter != YFilter.not_set or
                    self.accept_tolerance.yfilter != YFilter.not_set or
                    (self.key is not None and self.key.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "key" + "[key-name='" + self.key_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-lib-keychain-oper:keychain/keies/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.key_name.is_set or self.key_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.key_name.get_name_leafdata())
                if (self.accept_tolerance.is_set or self.accept_tolerance.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.accept_tolerance.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "key"):
                    if (self.key is None):
                        self.key = Keychain.Keies.Key.Key()
                        self.key.parent = self
                        self._children_name_map["key"] = "key"
                    return self.key

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "key" or name == "key-name" or name == "accept-tolerance"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "key-name"):
                    self.key_name = value
                    self.key_name.value_namespace = name_space
                    self.key_name.value_namespace_prefix = name_space_prefix
                if(value_path == "accept-tolerance"):
                    self.accept_tolerance = value
                    self.accept_tolerance.value_namespace = name_space
                    self.accept_tolerance.value_namespace_prefix = name_space_prefix

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
                path_buffer = "Cisco-IOS-XR-lib-keychain-oper:keychain/%s" % self.get_segment_path()
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
                c = Keychain.Keies.Key()
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
        return (self.keies is not None and self.keies.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.keies is not None and self.keies.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-lib-keychain-oper:keychain" + path_buffer

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

        if (child_yang_name == "keies"):
            if (self.keies is None):
                self.keies = Keychain.Keies()
                self.keies.parent = self
                self._children_name_map["keies"] = "keies"
            return self.keies

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "keies"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Keychain()
        return self._top_entity


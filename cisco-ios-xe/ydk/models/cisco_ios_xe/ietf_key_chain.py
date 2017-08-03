""" ietf_key_chain 

This YANG module defines the generic configuration
data for key\-chain. It is intended that the module
will be extended by vendors to define vendor\-specific
key\-chain configuration parameters.


"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class KeyChains(Entity):
    """
    A key\-chain is a sequence of keys that are collectively
    managed for authentication.
    
    .. attribute:: name  <key>
    
    	Name of the key\-chain
    	**type**\:  str
    
    .. attribute:: accept_tolerance
    
    	Tolerance for key lifetime acceptance (seconds)
    	**type**\:   :py:class:`AcceptTolerance <ydk.models.ietf.ietf_key_chain.KeyChains.AcceptTolerance>`
    
    .. attribute:: key
    
    	One key
    	**type**\: list of    :py:class:`Key <ydk.models.ietf.ietf_key_chain.KeyChains.Key>`
    
    

    """

    _prefix = 'key-chain'
    _revision = '2015-02-24'

    def __init__(self):
        super(KeyChains, self).__init__()
        self._top_entity = None

        self.yang_name = "key-chains"
        self.yang_parent_name = "ietf-key-chain"

        self.name = YLeaf(YType.str, "name")

        self.accept_tolerance = KeyChains.AcceptTolerance()
        self.accept_tolerance.parent = self
        self._children_name_map["accept_tolerance"] = "accept-tolerance"
        self._children_yang_names.add("accept-tolerance")

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
            if name in ("name") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(KeyChains, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(KeyChains, self).__setattr__(name, value)


    class AcceptTolerance(Entity):
        """
        Tolerance for key lifetime acceptance (seconds).
        
        .. attribute:: duration
        
        	Tolerance range, in seconds
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: seconds
        
        	**default value**\: 0
        
        

        """

        _prefix = 'key-chain'
        _revision = '2015-02-24'

        def __init__(self):
            super(KeyChains.AcceptTolerance, self).__init__()

            self.yang_name = "accept-tolerance"
            self.yang_parent_name = "key-chains"

            self.duration = YLeaf(YType.uint32, "duration")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("duration") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(KeyChains.AcceptTolerance, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(KeyChains.AcceptTolerance, self).__setattr__(name, value)

        def has_data(self):
            return self.duration.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.duration.yfilter != YFilter.not_set)

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
            if (self.duration.is_set or self.duration.yfilter != YFilter.not_set):
                leaf_name_data.append(self.duration.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "duration"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "duration"):
                self.duration = value
                self.duration.value_namespace = name_space
                self.duration.value_namespace_prefix = name_space_prefix


    class Key(Entity):
        """
        One key.
        
        .. attribute:: key_id  <key>
        
        	Key id
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: crypto_algorithm
        
        	Cryptographic algorithm associated with key
        	**type**\:   :py:class:`CryptoAlgorithm <ydk.models.ietf.ietf_key_chain.KeyChains.Key.CryptoAlgorithm>`
        
        .. attribute:: key_string
        
        	The key string
        	**type**\:   :py:class:`KeyString <ydk.models.ietf.ietf_key_chain.KeyChains.Key.KeyString>`
        
        .. attribute:: lifetime
        
        	Specify a key's lifetime
        	**type**\:   :py:class:`Lifetime <ydk.models.ietf.ietf_key_chain.KeyChains.Key.Lifetime>`
        
        

        """

        _prefix = 'key-chain'
        _revision = '2015-02-24'

        def __init__(self):
            super(KeyChains.Key, self).__init__()

            self.yang_name = "key"
            self.yang_parent_name = "key-chains"

            self.key_id = YLeaf(YType.uint64, "key-id")

            self.crypto_algorithm = KeyChains.Key.CryptoAlgorithm()
            self.crypto_algorithm.parent = self
            self._children_name_map["crypto_algorithm"] = "crypto-algorithm"
            self._children_yang_names.add("crypto-algorithm")

            self.key_string = KeyChains.Key.KeyString()
            self.key_string.parent = self
            self._children_name_map["key_string"] = "key-string"
            self._children_yang_names.add("key-string")

            self.lifetime = KeyChains.Key.Lifetime()
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
                        super(KeyChains.Key, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(KeyChains.Key, self).__setattr__(name, value)


        class KeyString(Entity):
            """
            The key string.
            
            .. attribute:: hexadecimal_string
            
            	Key in hexadecimal string format
            	**type**\:  str
            
            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
            
            .. attribute:: keystring
            
            	Key string in ASCII format
            	**type**\:  str
            
            

            """

            _prefix = 'key-chain'
            _revision = '2015-02-24'

            def __init__(self):
                super(KeyChains.Key.KeyString, self).__init__()

                self.yang_name = "key-string"
                self.yang_parent_name = "key"

                self.hexadecimal_string = YLeaf(YType.str, "hexadecimal-string")

                self.keystring = YLeaf(YType.str, "keystring")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("hexadecimal_string",
                                "keystring") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(KeyChains.Key.KeyString, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(KeyChains.Key.KeyString, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.hexadecimal_string.is_set or
                    self.keystring.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.hexadecimal_string.yfilter != YFilter.not_set or
                    self.keystring.yfilter != YFilter.not_set)

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
                if (self.hexadecimal_string.is_set or self.hexadecimal_string.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hexadecimal_string.get_name_leafdata())
                if (self.keystring.is_set or self.keystring.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.keystring.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "hexadecimal-string" or name == "keystring"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "hexadecimal-string"):
                    self.hexadecimal_string = value
                    self.hexadecimal_string.value_namespace = name_space
                    self.hexadecimal_string.value_namespace_prefix = name_space_prefix
                if(value_path == "keystring"):
                    self.keystring = value
                    self.keystring.value_namespace = name_space
                    self.keystring.value_namespace_prefix = name_space_prefix


        class Lifetime(Entity):
            """
            Specify a key's lifetime.
            
            .. attribute:: accept_lifetime
            
            	Separate lifetime specification for accept lifetime
            	**type**\:   :py:class:`AcceptLifetime <ydk.models.ietf.ietf_key_chain.KeyChains.Key.Lifetime.AcceptLifetime>`
            
            .. attribute:: send_accept_lifetime
            
            	Single lifetime specification for both send and accept lifetimes
            	**type**\:   :py:class:`SendAcceptLifetime <ydk.models.ietf.ietf_key_chain.KeyChains.Key.Lifetime.SendAcceptLifetime>`
            
            .. attribute:: send_lifetime
            
            	Separate lifetime specification for send lifetime
            	**type**\:   :py:class:`SendLifetime <ydk.models.ietf.ietf_key_chain.KeyChains.Key.Lifetime.SendLifetime>`
            
            

            """

            _prefix = 'key-chain'
            _revision = '2015-02-24'

            def __init__(self):
                super(KeyChains.Key.Lifetime, self).__init__()

                self.yang_name = "lifetime"
                self.yang_parent_name = "key"

                self.accept_lifetime = KeyChains.Key.Lifetime.AcceptLifetime()
                self.accept_lifetime.parent = self
                self._children_name_map["accept_lifetime"] = "accept-lifetime"
                self._children_yang_names.add("accept-lifetime")

                self.send_accept_lifetime = KeyChains.Key.Lifetime.SendAcceptLifetime()
                self.send_accept_lifetime.parent = self
                self._children_name_map["send_accept_lifetime"] = "send-accept-lifetime"
                self._children_yang_names.add("send-accept-lifetime")

                self.send_lifetime = KeyChains.Key.Lifetime.SendLifetime()
                self.send_lifetime.parent = self
                self._children_name_map["send_lifetime"] = "send-lifetime"
                self._children_yang_names.add("send-lifetime")


            class SendAcceptLifetime(Entity):
                """
                Single lifetime specification for both send and
                accept lifetimes.
                
                .. attribute:: always
                
                	Indicates key lifetime is always valid
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: duration
                
                	Key lifetime duration, in seconds
                	**type**\:  int
                
                	**range:** 1..2147483646
                
                	**units**\: seconds
                
                .. attribute:: end_date_time
                
                	End time
                	**type**\:  str
                
                	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                
                .. attribute:: no_end_time
                
                	Indicates key lifetime end\-time in infinite
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: start_date_time
                
                	Start time
                	**type**\:  str
                
                	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                
                

                """

                _prefix = 'key-chain'
                _revision = '2015-02-24'

                def __init__(self):
                    super(KeyChains.Key.Lifetime.SendAcceptLifetime, self).__init__()

                    self.yang_name = "send-accept-lifetime"
                    self.yang_parent_name = "lifetime"

                    self.always = YLeaf(YType.empty, "always")

                    self.duration = YLeaf(YType.uint32, "duration")

                    self.end_date_time = YLeaf(YType.str, "end-date-time")

                    self.no_end_time = YLeaf(YType.empty, "no-end-time")

                    self.start_date_time = YLeaf(YType.str, "start-date-time")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("always",
                                    "duration",
                                    "end_date_time",
                                    "no_end_time",
                                    "start_date_time") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(KeyChains.Key.Lifetime.SendAcceptLifetime, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(KeyChains.Key.Lifetime.SendAcceptLifetime, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.always.is_set or
                        self.duration.is_set or
                        self.end_date_time.is_set or
                        self.no_end_time.is_set or
                        self.start_date_time.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.always.yfilter != YFilter.not_set or
                        self.duration.yfilter != YFilter.not_set or
                        self.end_date_time.yfilter != YFilter.not_set or
                        self.no_end_time.yfilter != YFilter.not_set or
                        self.start_date_time.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "send-accept-lifetime" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.always.is_set or self.always.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.always.get_name_leafdata())
                    if (self.duration.is_set or self.duration.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.duration.get_name_leafdata())
                    if (self.end_date_time.is_set or self.end_date_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.end_date_time.get_name_leafdata())
                    if (self.no_end_time.is_set or self.no_end_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.no_end_time.get_name_leafdata())
                    if (self.start_date_time.is_set or self.start_date_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.start_date_time.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "always" or name == "duration" or name == "end-date-time" or name == "no-end-time" or name == "start-date-time"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "always"):
                        self.always = value
                        self.always.value_namespace = name_space
                        self.always.value_namespace_prefix = name_space_prefix
                    if(value_path == "duration"):
                        self.duration = value
                        self.duration.value_namespace = name_space
                        self.duration.value_namespace_prefix = name_space_prefix
                    if(value_path == "end-date-time"):
                        self.end_date_time = value
                        self.end_date_time.value_namespace = name_space
                        self.end_date_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "no-end-time"):
                        self.no_end_time = value
                        self.no_end_time.value_namespace = name_space
                        self.no_end_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "start-date-time"):
                        self.start_date_time = value
                        self.start_date_time.value_namespace = name_space
                        self.start_date_time.value_namespace_prefix = name_space_prefix


            class SendLifetime(Entity):
                """
                Separate lifetime specification for send
                lifetime.
                
                .. attribute:: always
                
                	Indicates key lifetime is always valid
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: duration
                
                	Key lifetime duration, in seconds
                	**type**\:  int
                
                	**range:** 1..2147483646
                
                	**units**\: seconds
                
                .. attribute:: end_date_time
                
                	End time
                	**type**\:  str
                
                	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                
                .. attribute:: no_end_time
                
                	Indicates key lifetime end\-time in infinite
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: start_date_time
                
                	Start time
                	**type**\:  str
                
                	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                
                

                """

                _prefix = 'key-chain'
                _revision = '2015-02-24'

                def __init__(self):
                    super(KeyChains.Key.Lifetime.SendLifetime, self).__init__()

                    self.yang_name = "send-lifetime"
                    self.yang_parent_name = "lifetime"

                    self.always = YLeaf(YType.empty, "always")

                    self.duration = YLeaf(YType.uint32, "duration")

                    self.end_date_time = YLeaf(YType.str, "end-date-time")

                    self.no_end_time = YLeaf(YType.empty, "no-end-time")

                    self.start_date_time = YLeaf(YType.str, "start-date-time")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("always",
                                    "duration",
                                    "end_date_time",
                                    "no_end_time",
                                    "start_date_time") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(KeyChains.Key.Lifetime.SendLifetime, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(KeyChains.Key.Lifetime.SendLifetime, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.always.is_set or
                        self.duration.is_set or
                        self.end_date_time.is_set or
                        self.no_end_time.is_set or
                        self.start_date_time.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.always.yfilter != YFilter.not_set or
                        self.duration.yfilter != YFilter.not_set or
                        self.end_date_time.yfilter != YFilter.not_set or
                        self.no_end_time.yfilter != YFilter.not_set or
                        self.start_date_time.yfilter != YFilter.not_set)

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
                    if (self.always.is_set or self.always.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.always.get_name_leafdata())
                    if (self.duration.is_set or self.duration.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.duration.get_name_leafdata())
                    if (self.end_date_time.is_set or self.end_date_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.end_date_time.get_name_leafdata())
                    if (self.no_end_time.is_set or self.no_end_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.no_end_time.get_name_leafdata())
                    if (self.start_date_time.is_set or self.start_date_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.start_date_time.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "always" or name == "duration" or name == "end-date-time" or name == "no-end-time" or name == "start-date-time"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "always"):
                        self.always = value
                        self.always.value_namespace = name_space
                        self.always.value_namespace_prefix = name_space_prefix
                    if(value_path == "duration"):
                        self.duration = value
                        self.duration.value_namespace = name_space
                        self.duration.value_namespace_prefix = name_space_prefix
                    if(value_path == "end-date-time"):
                        self.end_date_time = value
                        self.end_date_time.value_namespace = name_space
                        self.end_date_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "no-end-time"):
                        self.no_end_time = value
                        self.no_end_time.value_namespace = name_space
                        self.no_end_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "start-date-time"):
                        self.start_date_time = value
                        self.start_date_time.value_namespace = name_space
                        self.start_date_time.value_namespace_prefix = name_space_prefix


            class AcceptLifetime(Entity):
                """
                Separate lifetime specification for accept
                lifetime.
                
                .. attribute:: always
                
                	Indicates key lifetime is always valid
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: duration
                
                	Key lifetime duration, in seconds
                	**type**\:  int
                
                	**range:** 1..2147483646
                
                	**units**\: seconds
                
                .. attribute:: end_date_time
                
                	End time
                	**type**\:  str
                
                	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                
                .. attribute:: no_end_time
                
                	Indicates key lifetime end\-time in infinite
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: start_date_time
                
                	Start time
                	**type**\:  str
                
                	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                
                

                """

                _prefix = 'key-chain'
                _revision = '2015-02-24'

                def __init__(self):
                    super(KeyChains.Key.Lifetime.AcceptLifetime, self).__init__()

                    self.yang_name = "accept-lifetime"
                    self.yang_parent_name = "lifetime"

                    self.always = YLeaf(YType.empty, "always")

                    self.duration = YLeaf(YType.uint32, "duration")

                    self.end_date_time = YLeaf(YType.str, "end-date-time")

                    self.no_end_time = YLeaf(YType.empty, "no-end-time")

                    self.start_date_time = YLeaf(YType.str, "start-date-time")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("always",
                                    "duration",
                                    "end_date_time",
                                    "no_end_time",
                                    "start_date_time") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(KeyChains.Key.Lifetime.AcceptLifetime, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(KeyChains.Key.Lifetime.AcceptLifetime, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.always.is_set or
                        self.duration.is_set or
                        self.end_date_time.is_set or
                        self.no_end_time.is_set or
                        self.start_date_time.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.always.yfilter != YFilter.not_set or
                        self.duration.yfilter != YFilter.not_set or
                        self.end_date_time.yfilter != YFilter.not_set or
                        self.no_end_time.yfilter != YFilter.not_set or
                        self.start_date_time.yfilter != YFilter.not_set)

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
                    if (self.always.is_set or self.always.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.always.get_name_leafdata())
                    if (self.duration.is_set or self.duration.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.duration.get_name_leafdata())
                    if (self.end_date_time.is_set or self.end_date_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.end_date_time.get_name_leafdata())
                    if (self.no_end_time.is_set or self.no_end_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.no_end_time.get_name_leafdata())
                    if (self.start_date_time.is_set or self.start_date_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.start_date_time.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "always" or name == "duration" or name == "end-date-time" or name == "no-end-time" or name == "start-date-time"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "always"):
                        self.always = value
                        self.always.value_namespace = name_space
                        self.always.value_namespace_prefix = name_space_prefix
                    if(value_path == "duration"):
                        self.duration = value
                        self.duration.value_namespace = name_space
                        self.duration.value_namespace_prefix = name_space_prefix
                    if(value_path == "end-date-time"):
                        self.end_date_time = value
                        self.end_date_time.value_namespace = name_space
                        self.end_date_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "no-end-time"):
                        self.no_end_time = value
                        self.no_end_time.value_namespace = name_space
                        self.no_end_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "start-date-time"):
                        self.start_date_time = value
                        self.start_date_time.value_namespace = name_space
                        self.start_date_time.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    (self.accept_lifetime is not None and self.accept_lifetime.has_data()) or
                    (self.send_accept_lifetime is not None and self.send_accept_lifetime.has_data()) or
                    (self.send_lifetime is not None and self.send_lifetime.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.accept_lifetime is not None and self.accept_lifetime.has_operation()) or
                    (self.send_accept_lifetime is not None and self.send_accept_lifetime.has_operation()) or
                    (self.send_lifetime is not None and self.send_lifetime.has_operation()))

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

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "accept-lifetime"):
                    if (self.accept_lifetime is None):
                        self.accept_lifetime = KeyChains.Key.Lifetime.AcceptLifetime()
                        self.accept_lifetime.parent = self
                        self._children_name_map["accept_lifetime"] = "accept-lifetime"
                    return self.accept_lifetime

                if (child_yang_name == "send-accept-lifetime"):
                    if (self.send_accept_lifetime is None):
                        self.send_accept_lifetime = KeyChains.Key.Lifetime.SendAcceptLifetime()
                        self.send_accept_lifetime.parent = self
                        self._children_name_map["send_accept_lifetime"] = "send-accept-lifetime"
                    return self.send_accept_lifetime

                if (child_yang_name == "send-lifetime"):
                    if (self.send_lifetime is None):
                        self.send_lifetime = KeyChains.Key.Lifetime.SendLifetime()
                        self.send_lifetime.parent = self
                        self._children_name_map["send_lifetime"] = "send-lifetime"
                    return self.send_lifetime

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "accept-lifetime" or name == "send-accept-lifetime" or name == "send-lifetime"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class CryptoAlgorithm(Entity):
            """
            Cryptographic algorithm associated with key.
            
            .. attribute:: hmac_sha1_12
            
            	The HMAC\-SHA1\-12 algorithm
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: hmac_sha1_20
            
            	The HMAC\-SHA1\-20 algorithm
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: hmac_sha_1
            
            	HMAC\-SHA\-1 authentication algorithm
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: hmac_sha_256
            
            	HMAC\-SHA\-256 authentication algorithm
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: hmac_sha_384
            
            	HMAC\-SHA\-384 authentication algorithm
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: hmac_sha_512
            
            	HMAC\-SHA\-512 authentication algorithm
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: md5
            
            	The MD5 algorithm
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: sha_1
            
            	The SHA\-1 algorithm
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'key-chain'
            _revision = '2015-02-24'

            def __init__(self):
                super(KeyChains.Key.CryptoAlgorithm, self).__init__()

                self.yang_name = "crypto-algorithm"
                self.yang_parent_name = "key"

                self.hmac_sha1_12 = YLeaf(YType.empty, "hmac-sha1-12")

                self.hmac_sha1_20 = YLeaf(YType.empty, "hmac-sha1-20")

                self.hmac_sha_1 = YLeaf(YType.empty, "hmac-sha-1")

                self.hmac_sha_256 = YLeaf(YType.empty, "hmac-sha-256")

                self.hmac_sha_384 = YLeaf(YType.empty, "hmac-sha-384")

                self.hmac_sha_512 = YLeaf(YType.empty, "hmac-sha-512")

                self.md5 = YLeaf(YType.empty, "md5")

                self.sha_1 = YLeaf(YType.empty, "sha-1")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("hmac_sha1_12",
                                "hmac_sha1_20",
                                "hmac_sha_1",
                                "hmac_sha_256",
                                "hmac_sha_384",
                                "hmac_sha_512",
                                "md5",
                                "sha_1") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(KeyChains.Key.CryptoAlgorithm, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(KeyChains.Key.CryptoAlgorithm, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.hmac_sha1_12.is_set or
                    self.hmac_sha1_20.is_set or
                    self.hmac_sha_1.is_set or
                    self.hmac_sha_256.is_set or
                    self.hmac_sha_384.is_set or
                    self.hmac_sha_512.is_set or
                    self.md5.is_set or
                    self.sha_1.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.hmac_sha1_12.yfilter != YFilter.not_set or
                    self.hmac_sha1_20.yfilter != YFilter.not_set or
                    self.hmac_sha_1.yfilter != YFilter.not_set or
                    self.hmac_sha_256.yfilter != YFilter.not_set or
                    self.hmac_sha_384.yfilter != YFilter.not_set or
                    self.hmac_sha_512.yfilter != YFilter.not_set or
                    self.md5.yfilter != YFilter.not_set or
                    self.sha_1.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "crypto-algorithm" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.hmac_sha1_12.is_set or self.hmac_sha1_12.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hmac_sha1_12.get_name_leafdata())
                if (self.hmac_sha1_20.is_set or self.hmac_sha1_20.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hmac_sha1_20.get_name_leafdata())
                if (self.hmac_sha_1.is_set or self.hmac_sha_1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hmac_sha_1.get_name_leafdata())
                if (self.hmac_sha_256.is_set or self.hmac_sha_256.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hmac_sha_256.get_name_leafdata())
                if (self.hmac_sha_384.is_set or self.hmac_sha_384.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hmac_sha_384.get_name_leafdata())
                if (self.hmac_sha_512.is_set or self.hmac_sha_512.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hmac_sha_512.get_name_leafdata())
                if (self.md5.is_set or self.md5.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.md5.get_name_leafdata())
                if (self.sha_1.is_set or self.sha_1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sha_1.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "hmac-sha1-12" or name == "hmac-sha1-20" or name == "hmac-sha-1" or name == "hmac-sha-256" or name == "hmac-sha-384" or name == "hmac-sha-512" or name == "md5" or name == "sha-1"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "hmac-sha1-12"):
                    self.hmac_sha1_12 = value
                    self.hmac_sha1_12.value_namespace = name_space
                    self.hmac_sha1_12.value_namespace_prefix = name_space_prefix
                if(value_path == "hmac-sha1-20"):
                    self.hmac_sha1_20 = value
                    self.hmac_sha1_20.value_namespace = name_space
                    self.hmac_sha1_20.value_namespace_prefix = name_space_prefix
                if(value_path == "hmac-sha-1"):
                    self.hmac_sha_1 = value
                    self.hmac_sha_1.value_namespace = name_space
                    self.hmac_sha_1.value_namespace_prefix = name_space_prefix
                if(value_path == "hmac-sha-256"):
                    self.hmac_sha_256 = value
                    self.hmac_sha_256.value_namespace = name_space
                    self.hmac_sha_256.value_namespace_prefix = name_space_prefix
                if(value_path == "hmac-sha-384"):
                    self.hmac_sha_384 = value
                    self.hmac_sha_384.value_namespace = name_space
                    self.hmac_sha_384.value_namespace_prefix = name_space_prefix
                if(value_path == "hmac-sha-512"):
                    self.hmac_sha_512 = value
                    self.hmac_sha_512.value_namespace = name_space
                    self.hmac_sha_512.value_namespace_prefix = name_space_prefix
                if(value_path == "md5"):
                    self.md5 = value
                    self.md5.value_namespace = name_space
                    self.md5.value_namespace_prefix = name_space_prefix
                if(value_path == "sha-1"):
                    self.sha_1 = value
                    self.sha_1.value_namespace = name_space
                    self.sha_1.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                self.key_id.is_set or
                (self.crypto_algorithm is not None and self.crypto_algorithm.has_data()) or
                (self.key_string is not None and self.key_string.has_data()) or
                (self.lifetime is not None and self.lifetime.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.key_id.yfilter != YFilter.not_set or
                (self.crypto_algorithm is not None and self.crypto_algorithm.has_operation()) or
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

            if (child_yang_name == "crypto-algorithm"):
                if (self.crypto_algorithm is None):
                    self.crypto_algorithm = KeyChains.Key.CryptoAlgorithm()
                    self.crypto_algorithm.parent = self
                    self._children_name_map["crypto_algorithm"] = "crypto-algorithm"
                return self.crypto_algorithm

            if (child_yang_name == "key-string"):
                if (self.key_string is None):
                    self.key_string = KeyChains.Key.KeyString()
                    self.key_string.parent = self
                    self._children_name_map["key_string"] = "key-string"
                return self.key_string

            if (child_yang_name == "lifetime"):
                if (self.lifetime is None):
                    self.lifetime = KeyChains.Key.Lifetime()
                    self.lifetime.parent = self
                    self._children_name_map["lifetime"] = "lifetime"
                return self.lifetime

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "crypto-algorithm" or name == "key-string" or name == "lifetime" or name == "key-id"):
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
        return (
            self.name.is_set or
            (self.accept_tolerance is not None and self.accept_tolerance.has_data()))

    def has_operation(self):
        for c in self.key:
            if (c.has_operation()):
                return True
        return (
            self.yfilter != YFilter.not_set or
            self.name.yfilter != YFilter.not_set or
            (self.accept_tolerance is not None and self.accept_tolerance.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "ietf-key-chain:key-chains" + "[name='" + self.name.get() + "']" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
            leaf_name_data.append(self.name.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "accept-tolerance"):
            if (self.accept_tolerance is None):
                self.accept_tolerance = KeyChains.AcceptTolerance()
                self.accept_tolerance.parent = self
                self._children_name_map["accept_tolerance"] = "accept-tolerance"
            return self.accept_tolerance

        if (child_yang_name == "key"):
            for c in self.key:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = KeyChains.Key()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.key.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "accept-tolerance" or name == "key" or name == "name"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "name"):
            self.name = value
            self.name.value_namespace = name_space
            self.name.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = KeyChains()
        return self._top_entity


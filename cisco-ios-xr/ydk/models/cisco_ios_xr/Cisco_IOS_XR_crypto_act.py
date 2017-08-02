""" Cisco_IOS_XR_crypto_act 

This module contains a collection of YANG definitions
for Cisco IOS\-XR action package configuration.

Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class KeyGenerateRsaGeneralKeys(Entity):
    """
    Generate a general purpose RSA key pair for signing and encryption
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.KeyGenerateRsaGeneralKeys.Input>`
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):
        super(KeyGenerateRsaGeneralKeys, self).__init__()
        self._top_entity = None

        self.yang_name = "key-generate-rsa-general-keys"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-act"

        self.input = KeyGenerateRsaGeneralKeys.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: key_label
        
        	RSA keypair label
        	**type**\:  str
        
        .. attribute:: key_modulus
        
        	Key modulus in the range of 512 to 4096 for your General Purpose Keypair. Choosing a key modulus greater than 512 may take a few minutes
        	**type**\:  int
        
        	**range:** 512..4096
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'crypto-act'
        _revision = '2016-04-17'

        def __init__(self):
            super(KeyGenerateRsaGeneralKeys.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "key-generate-rsa-general-keys"

            self.key_label = YLeaf(YType.str, "key-label")

            self.key_modulus = YLeaf(YType.int32, "key-modulus")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("key_label",
                            "key_modulus") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(KeyGenerateRsaGeneralKeys.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(KeyGenerateRsaGeneralKeys.Input, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.key_label.is_set or
                self.key_modulus.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.key_label.yfilter != YFilter.not_set or
                self.key_modulus.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-crypto-act:key-generate-rsa-general-keys/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.key_label.is_set or self.key_label.yfilter != YFilter.not_set):
                leaf_name_data.append(self.key_label.get_name_leafdata())
            if (self.key_modulus.is_set or self.key_modulus.yfilter != YFilter.not_set):
                leaf_name_data.append(self.key_modulus.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "key-label" or name == "key-modulus"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "key-label"):
                self.key_label = value
                self.key_label.value_namespace = name_space
                self.key_label.value_namespace_prefix = name_space_prefix
            if(value_path == "key-modulus"):
                self.key_modulus = value
                self.key_modulus.value_namespace = name_space
                self.key_modulus.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-crypto-act:key-generate-rsa-general-keys" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = KeyGenerateRsaGeneralKeys.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = KeyGenerateRsaGeneralKeys()
        return self._top_entity

class KeyGenerateRsaUsageKeys(Entity):
    """
    Generate seperate RSA key pairs for signing and encryption
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.KeyGenerateRsaUsageKeys.Input>`
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):
        super(KeyGenerateRsaUsageKeys, self).__init__()
        self._top_entity = None

        self.yang_name = "key-generate-rsa-usage-keys"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-act"

        self.input = KeyGenerateRsaUsageKeys.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: key_label
        
        	RSA keypair label
        	**type**\:  str
        
        .. attribute:: key_modulus
        
        	Key modulus in the range of 512 to 4096 for your General Purpose Keypair. Choosing a key modulus greater than 512 may take a few minutes
        	**type**\:  int
        
        	**range:** 512..4096
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'crypto-act'
        _revision = '2016-04-17'

        def __init__(self):
            super(KeyGenerateRsaUsageKeys.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "key-generate-rsa-usage-keys"

            self.key_label = YLeaf(YType.str, "key-label")

            self.key_modulus = YLeaf(YType.int32, "key-modulus")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("key_label",
                            "key_modulus") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(KeyGenerateRsaUsageKeys.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(KeyGenerateRsaUsageKeys.Input, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.key_label.is_set or
                self.key_modulus.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.key_label.yfilter != YFilter.not_set or
                self.key_modulus.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-crypto-act:key-generate-rsa-usage-keys/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.key_label.is_set or self.key_label.yfilter != YFilter.not_set):
                leaf_name_data.append(self.key_label.get_name_leafdata())
            if (self.key_modulus.is_set or self.key_modulus.yfilter != YFilter.not_set):
                leaf_name_data.append(self.key_modulus.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "key-label" or name == "key-modulus"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "key-label"):
                self.key_label = value
                self.key_label.value_namespace = name_space
                self.key_label.value_namespace_prefix = name_space_prefix
            if(value_path == "key-modulus"):
                self.key_modulus = value
                self.key_modulus.value_namespace = name_space
                self.key_modulus.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-crypto-act:key-generate-rsa-usage-keys" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = KeyGenerateRsaUsageKeys.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = KeyGenerateRsaUsageKeys()
        return self._top_entity

class KeyGenerateRsa(Entity):
    """
    Generate seperate RSA key pairs for signing and encryption
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.KeyGenerateRsa.Input>`
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):
        super(KeyGenerateRsa, self).__init__()
        self._top_entity = None

        self.yang_name = "key-generate-rsa"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-act"

        self.input = KeyGenerateRsa.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: key_label
        
        	RSA keypair label
        	**type**\:  str
        
        .. attribute:: key_modulus
        
        	Key modulus in the range of 512 to 4096 for your General Purpose Keypair. Choosing a key modulus greater than 512 may take a few minutes
        	**type**\:  int
        
        	**range:** 512..4096
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'crypto-act'
        _revision = '2016-04-17'

        def __init__(self):
            super(KeyGenerateRsa.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "key-generate-rsa"

            self.key_label = YLeaf(YType.str, "key-label")

            self.key_modulus = YLeaf(YType.int32, "key-modulus")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("key_label",
                            "key_modulus") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(KeyGenerateRsa.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(KeyGenerateRsa.Input, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.key_label.is_set or
                self.key_modulus.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.key_label.yfilter != YFilter.not_set or
                self.key_modulus.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-crypto-act:key-generate-rsa/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.key_label.is_set or self.key_label.yfilter != YFilter.not_set):
                leaf_name_data.append(self.key_label.get_name_leafdata())
            if (self.key_modulus.is_set or self.key_modulus.yfilter != YFilter.not_set):
                leaf_name_data.append(self.key_modulus.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "key-label" or name == "key-modulus"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "key-label"):
                self.key_label = value
                self.key_label.value_namespace = name_space
                self.key_label.value_namespace_prefix = name_space_prefix
            if(value_path == "key-modulus"):
                self.key_modulus = value
                self.key_modulus.value_namespace = name_space
                self.key_modulus.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-crypto-act:key-generate-rsa" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = KeyGenerateRsa.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = KeyGenerateRsa()
        return self._top_entity

class KeyGenerateDsa(Entity):
    """
    Generate DSA keys
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.KeyGenerateDsa.Input>`
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):
        super(KeyGenerateDsa, self).__init__()
        self._top_entity = None

        self.yang_name = "key-generate-dsa"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-act"

        self.input = KeyGenerateDsa.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: key_modulus
        
        	Key modulus size can be 512, 768, or 1024 bits
        	**type**\:  int
        
        	**range:** 512..None \| 768..None \| 1024..None
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'crypto-act'
        _revision = '2016-04-17'

        def __init__(self):
            super(KeyGenerateDsa.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "key-generate-dsa"

            self.key_modulus = YLeaf(YType.int32, "key-modulus")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("key_modulus") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(KeyGenerateDsa.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(KeyGenerateDsa.Input, self).__setattr__(name, value)

        def has_data(self):
            return self.key_modulus.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.key_modulus.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-crypto-act:key-generate-dsa/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.key_modulus.is_set or self.key_modulus.yfilter != YFilter.not_set):
                leaf_name_data.append(self.key_modulus.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "key-modulus"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "key-modulus"):
                self.key_modulus = value
                self.key_modulus.value_namespace = name_space
                self.key_modulus.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-crypto-act:key-generate-dsa" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = KeyGenerateDsa.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = KeyGenerateDsa()
        return self._top_entity

class KeyZeroizeRsa(Entity):
    """
    Remove RSA keys
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.KeyZeroizeRsa.Input>`
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):
        super(KeyZeroizeRsa, self).__init__()
        self._top_entity = None

        self.yang_name = "key-zeroize-rsa"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-act"

        self.input = KeyZeroizeRsa.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: key_label
        
        	RSA key label
        	**type**\:  str
        
        

        """

        _prefix = 'crypto-act'
        _revision = '2016-04-17'

        def __init__(self):
            super(KeyZeroizeRsa.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "key-zeroize-rsa"

            self.key_label = YLeaf(YType.str, "key-label")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("key_label") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(KeyZeroizeRsa.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(KeyZeroizeRsa.Input, self).__setattr__(name, value)

        def has_data(self):
            return self.key_label.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.key_label.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-crypto-act:key-zeroize-rsa/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.key_label.is_set or self.key_label.yfilter != YFilter.not_set):
                leaf_name_data.append(self.key_label.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "key-label"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "key-label"):
                self.key_label = value
                self.key_label.value_namespace = name_space
                self.key_label.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-crypto-act:key-zeroize-rsa" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = KeyZeroizeRsa.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

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

    def has_data(self):
        return False

    def has_operation(self):
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-crypto-act:key-zeroize-dsa" + path_buffer

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

        return None

    def has_leaf_or_child_of_name(self, name):
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = KeyZeroizeDsa()
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

    def has_data(self):
        return False

    def has_operation(self):
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-crypto-act:key-zeroize-authentication-rsa" + path_buffer

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

        return None

    def has_leaf_or_child_of_name(self, name):
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = KeyZeroizeAuthenticationRsa()
        return self._top_entity

class KeyImportAuthenticationRsa(Entity):
    """
    Remove RSA authentication key
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.KeyImportAuthenticationRsa.Input>`
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):
        super(KeyImportAuthenticationRsa, self).__init__()
        self._top_entity = None

        self.yang_name = "key-import-authentication-rsa"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-act"

        self.input = KeyImportAuthenticationRsa.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: path
        
        	Path to RSA pubkey file
        	**type**\:  str
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'crypto-act'
        _revision = '2016-04-17'

        def __init__(self):
            super(KeyImportAuthenticationRsa.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "key-import-authentication-rsa"

            self.path = YLeaf(YType.str, "path")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("path") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(KeyImportAuthenticationRsa.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(KeyImportAuthenticationRsa.Input, self).__setattr__(name, value)

        def has_data(self):
            return self.path.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.path.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-crypto-act:key-import-authentication-rsa/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.path.is_set or self.path.yfilter != YFilter.not_set):
                leaf_name_data.append(self.path.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "path"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "path"):
                self.path = value
                self.path.value_namespace = name_space
                self.path.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-crypto-act:key-import-authentication-rsa" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = KeyImportAuthenticationRsa.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = KeyImportAuthenticationRsa()
        return self._top_entity

class CaAuthenticate(Entity):
    """
    Get the certification authority certificate
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.CaAuthenticate.Input>`
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):
        super(CaAuthenticate, self).__init__()
        self._top_entity = None

        self.yang_name = "ca-authenticate"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-act"

        self.input = CaAuthenticate.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: server_name
        
        	CA Server Name
        	**type**\:  str
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'crypto-act'
        _revision = '2016-04-17'

        def __init__(self):
            super(CaAuthenticate.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "ca-authenticate"

            self.server_name = YLeaf(YType.str, "server-name")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("server_name") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CaAuthenticate.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CaAuthenticate.Input, self).__setattr__(name, value)

        def has_data(self):
            return self.server_name.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.server_name.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-crypto-act:ca-authenticate/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.server_name.is_set or self.server_name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.server_name.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "server-name"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "server-name"):
                self.server_name = value
                self.server_name.value_namespace = name_space
                self.server_name.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-crypto-act:ca-authenticate" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = CaAuthenticate.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CaAuthenticate()
        return self._top_entity

class CaEnroll(Entity):
    """
    Request a certificate from a CA
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.CaEnroll.Input>`
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):
        super(CaEnroll, self).__init__()
        self._top_entity = None

        self.yang_name = "ca-enroll"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-act"

        self.input = CaEnroll.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: server_name
        
        	CA Server Name
        	**type**\:  str
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'crypto-act'
        _revision = '2016-04-17'

        def __init__(self):
            super(CaEnroll.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "ca-enroll"

            self.server_name = YLeaf(YType.str, "server-name")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("server_name") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CaEnroll.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CaEnroll.Input, self).__setattr__(name, value)

        def has_data(self):
            return self.server_name.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.server_name.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-crypto-act:ca-enroll/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.server_name.is_set or self.server_name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.server_name.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "server-name"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "server-name"):
                self.server_name = value
                self.server_name.value_namespace = name_space
                self.server_name.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-crypto-act:ca-enroll" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = CaEnroll.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CaEnroll()
        return self._top_entity

class CaImportCertificate(Entity):
    """
    Import a certificate from a s/tftp server or the terminal
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.CaImportCertificate.Input>`
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):
        super(CaImportCertificate, self).__init__()
        self._top_entity = None

        self.yang_name = "ca-import-certificate"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-act"

        self.input = CaImportCertificate.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: server_name
        
        	CA Server Name
        	**type**\:  str
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'crypto-act'
        _revision = '2016-04-17'

        def __init__(self):
            super(CaImportCertificate.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "ca-import-certificate"

            self.server_name = YLeaf(YType.str, "server-name")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("server_name") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CaImportCertificate.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CaImportCertificate.Input, self).__setattr__(name, value)

        def has_data(self):
            return self.server_name.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.server_name.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-crypto-act:ca-import-certificate/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.server_name.is_set or self.server_name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.server_name.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "server-name"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "server-name"):
                self.server_name = value
                self.server_name.value_namespace = name_space
                self.server_name.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-crypto-act:ca-import-certificate" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = CaImportCertificate.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CaImportCertificate()
        return self._top_entity

class CaCancelEnroll(Entity):
    """
    Cancel enrollment from a CA
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.CaCancelEnroll.Input>`
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):
        super(CaCancelEnroll, self).__init__()
        self._top_entity = None

        self.yang_name = "ca-cancel-enroll"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-act"

        self.input = CaCancelEnroll.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: server_name
        
        	CA Server Name
        	**type**\:  str
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'crypto-act'
        _revision = '2016-04-17'

        def __init__(self):
            super(CaCancelEnroll.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "ca-cancel-enroll"

            self.server_name = YLeaf(YType.str, "server-name")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("server_name") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CaCancelEnroll.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CaCancelEnroll.Input, self).__setattr__(name, value)

        def has_data(self):
            return self.server_name.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.server_name.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-crypto-act:ca-cancel-enroll/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.server_name.is_set or self.server_name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.server_name.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "server-name"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "server-name"):
                self.server_name = value
                self.server_name.value_namespace = name_space
                self.server_name.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-crypto-act:ca-cancel-enroll" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = CaCancelEnroll.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CaCancelEnroll()
        return self._top_entity

class CaCrlRequest(Entity):
    """
    Actions on certificate revocation lists
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.CaCrlRequest.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.CaCrlRequest.Output>`
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):
        super(CaCrlRequest, self).__init__()
        self._top_entity = None

        self.yang_name = "ca-crl-request"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-act"

        self.input = CaCrlRequest.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = CaCrlRequest.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")


    class Input(Entity):
        """
        
        
        .. attribute:: uri
        
        	CRL Distribution Point in URI format
        	**type**\:  str
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'crypto-act'
        _revision = '2016-04-17'

        def __init__(self):
            super(CaCrlRequest.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "ca-crl-request"

            self.uri = YLeaf(YType.str, "uri")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("uri") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CaCrlRequest.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CaCrlRequest.Input, self).__setattr__(name, value)

        def has_data(self):
            return self.uri.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.uri.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-crypto-act:ca-crl-request/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.uri.is_set or self.uri.yfilter != YFilter.not_set):
                leaf_name_data.append(self.uri.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "uri"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "uri"):
                self.uri = value
                self.uri.value_namespace = name_space
                self.uri.value_namespace_prefix = name_space_prefix


    class Output(Entity):
        """
        
        
        .. attribute:: certificate
        
        	Certificate returned
        	**type**\:  str
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'crypto-act'
        _revision = '2016-04-17'

        def __init__(self):
            super(CaCrlRequest.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "ca-crl-request"

            self.certificate = YLeaf(YType.str, "certificate")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("certificate") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CaCrlRequest.Output, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CaCrlRequest.Output, self).__setattr__(name, value)

        def has_data(self):
            return self.certificate.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.certificate.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "output" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-crypto-act:ca-crl-request/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.certificate.is_set or self.certificate.yfilter != YFilter.not_set):
                leaf_name_data.append(self.certificate.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "certificate"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "certificate"):
                self.certificate = value
                self.certificate.value_namespace = name_space
                self.certificate.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            (self.input is not None and self.input.has_data()) or
            (self.output is not None and self.output.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()) or
            (self.output is not None and self.output.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-crypto-act:ca-crl-request" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = CaCrlRequest.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        if (child_yang_name == "output"):
            if (self.output is None):
                self.output = CaCrlRequest.Output()
                self.output.parent = self
                self._children_name_map["output"] = "output"
            return self.output

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input" or name == "output"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CaCrlRequest()
        return self._top_entity

class CaTrustpoolImportUrl(Entity):
    """
    Manual import trustpool certificates from URL
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.CaTrustpoolImportUrl.Input>`
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):
        super(CaTrustpoolImportUrl, self).__init__()
        self._top_entity = None

        self.yang_name = "ca-trustpool-import-url"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-act"

        self.input = CaTrustpoolImportUrl.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: url
        
        	in URL format
        	**type**\:  str
        
        

        """

        _prefix = 'crypto-act'
        _revision = '2016-04-17'

        def __init__(self):
            super(CaTrustpoolImportUrl.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "ca-trustpool-import-url"

            self.url = YLeaf(YType.str, "url")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("url") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CaTrustpoolImportUrl.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CaTrustpoolImportUrl.Input, self).__setattr__(name, value)

        def has_data(self):
            return self.url.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.url.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-crypto-act:ca-trustpool-import-url/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.url.is_set or self.url.yfilter != YFilter.not_set):
                leaf_name_data.append(self.url.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "url"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "url"):
                self.url = value
                self.url.value_namespace = name_space
                self.url.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-crypto-act:ca-trustpool-import-url" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = CaTrustpoolImportUrl.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CaTrustpoolImportUrl()
        return self._top_entity

class CaTrustpoolImportUrlClean(Entity):
    """
    Remove downloaded certificates in trustpool
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.CaTrustpoolImportUrlClean.Input>`
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):
        super(CaTrustpoolImportUrlClean, self).__init__()
        self._top_entity = None

        self.yang_name = "ca-trustpool-import-url-clean"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-act"

        self.input = CaTrustpoolImportUrlClean.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: url
        
        	in URL format
        	**type**\:  str
        
        

        """

        _prefix = 'crypto-act'
        _revision = '2016-04-17'

        def __init__(self):
            super(CaTrustpoolImportUrlClean.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "ca-trustpool-import-url-clean"

            self.url = YLeaf(YType.str, "url")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("url") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CaTrustpoolImportUrlClean.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CaTrustpoolImportUrlClean.Input, self).__setattr__(name, value)

        def has_data(self):
            return self.url.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.url.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-crypto-act:ca-trustpool-import-url-clean/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.url.is_set or self.url.yfilter != YFilter.not_set):
                leaf_name_data.append(self.url.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "url"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "url"):
                self.url = value
                self.url.value_namespace = name_space
                self.url.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-crypto-act:ca-trustpool-import-url-clean" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = CaTrustpoolImportUrlClean.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CaTrustpoolImportUrlClean()
        return self._top_entity


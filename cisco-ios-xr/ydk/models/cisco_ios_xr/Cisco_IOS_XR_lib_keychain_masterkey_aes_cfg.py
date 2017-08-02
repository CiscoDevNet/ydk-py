""" Cisco_IOS_XR_lib_keychain_masterkey_aes_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR lib\-keychain\-masterkey\-aes package configuration.

This module contains definitions
for the following management objects\:
  password\: Configure masterkey

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Password(Entity):
    """
    Configure masterkey
    
    .. attribute:: encryption
    
    	Enable password encryption
    	**type**\:   :py:class:`Encryption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_masterkey_aes_cfg.Password.Encryption>`
    
    

    """

    _prefix = 'lib-keychain-masterkey-aes-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Password, self).__init__()
        self._top_entity = None

        self.yang_name = "password"
        self.yang_parent_name = "Cisco-IOS-XR-lib-keychain-masterkey-aes-cfg"

        self.encryption = Password.Encryption()
        self.encryption.parent = self
        self._children_name_map["encryption"] = "encryption"
        self._children_yang_names.add("encryption")


    class Encryption(Entity):
        """
        Enable password encryption
        
        .. attribute:: aes
        
        	encryption type used to store key
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        	**default value**\: 0
        
        

        """

        _prefix = 'lib-keychain-masterkey-aes-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Password.Encryption, self).__init__()

            self.yang_name = "encryption"
            self.yang_parent_name = "password"

            self.aes = YLeaf(YType.int32, "aes")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("aes") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Password.Encryption, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Password.Encryption, self).__setattr__(name, value)

        def has_data(self):
            return self.aes.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.aes.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "encryption" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-lib-keychain-masterkey-aes-cfg:password/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.aes.is_set or self.aes.yfilter != YFilter.not_set):
                leaf_name_data.append(self.aes.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "aes"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "aes"):
                self.aes = value
                self.aes.value_namespace = name_space
                self.aes.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.encryption is not None and self.encryption.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.encryption is not None and self.encryption.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-lib-keychain-masterkey-aes-cfg:password" + path_buffer

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

        if (child_yang_name == "encryption"):
            if (self.encryption is None):
                self.encryption = Password.Encryption()
                self.encryption.parent = self
                self._children_name_map["encryption"] = "encryption"
            return self.encryption

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "encryption"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Password()
        return self._top_entity


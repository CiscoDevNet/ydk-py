""" Cisco_IOS_XR_aaa_locald_admin_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR aaa\-locald package admin\-plane configuration.

This module contains definitions
for the following management objects\:
  aaa\: Admin plane AAA configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Aaa(Entity):
    """
    Admin plane AAA configuration
    
    .. attribute:: usernames
    
    	Configure local username
    	**type**\:   :py:class:`Usernames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_admin_cfg.Aaa.Usernames>`
    
    

    """

    _prefix = 'aaa-locald-admin-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Aaa, self).__init__()
        self._top_entity = None

        self.yang_name = "aaa"
        self.yang_parent_name = "Cisco-IOS-XR-aaa-locald-admin-cfg"

        self.usernames = Aaa.Usernames()
        self.usernames.parent = self
        self._children_name_map["usernames"] = "usernames"
        self._children_yang_names.add("usernames")


    class Usernames(Entity):
        """
        Configure local username
        
        .. attribute:: username
        
        	Admin Username
        	**type**\: list of    :py:class:`Username <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_admin_cfg.Aaa.Usernames.Username>`
        
        

        """

        _prefix = 'aaa-locald-admin-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.Usernames, self).__init__()

            self.yang_name = "usernames"
            self.yang_parent_name = "aaa"

            self.username = YList(self)

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
                        super(Aaa.Usernames, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Aaa.Usernames, self).__setattr__(name, value)


        class Username(Entity):
            """
            Admin Username
            
            .. attribute:: name  <key>
            
            	Username
            	**type**\:  str
            
            .. attribute:: secret
            
            	Specify the secret for the admin user
            	**type**\:  str
            
            	**pattern:** (!.+)\|([^!].+)
            
            .. attribute:: usergroup_under_usernames
            
            	Specify the usergroup to which this admin user belongs
            	**type**\:   :py:class:`UsergroupUnderUsernames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_admin_cfg.Aaa.Usernames.Username.UsergroupUnderUsernames>`
            
            

            """

            _prefix = 'aaa-locald-admin-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Usernames.Username, self).__init__()

                self.yang_name = "username"
                self.yang_parent_name = "usernames"

                self.name = YLeaf(YType.str, "name")

                self.secret = YLeaf(YType.str, "secret")

                self.usergroup_under_usernames = Aaa.Usernames.Username.UsergroupUnderUsernames()
                self.usergroup_under_usernames.parent = self
                self._children_name_map["usergroup_under_usernames"] = "usergroup-under-usernames"
                self._children_yang_names.add("usergroup-under-usernames")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("name",
                                "secret") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Aaa.Usernames.Username, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Usernames.Username, self).__setattr__(name, value)


            class UsergroupUnderUsernames(Entity):
                """
                Specify the usergroup to which this admin user
                belongs
                
                .. attribute:: usergroup_under_username
                
                	Name of the usergroup
                	**type**\: list of    :py:class:`UsergroupUnderUsername <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_admin_cfg.Aaa.Usernames.Username.UsergroupUnderUsernames.UsergroupUnderUsername>`
                
                

                """

                _prefix = 'aaa-locald-admin-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Usernames.Username.UsergroupUnderUsernames, self).__init__()

                    self.yang_name = "usergroup-under-usernames"
                    self.yang_parent_name = "username"

                    self.usergroup_under_username = YList(self)

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
                                super(Aaa.Usernames.Username.UsergroupUnderUsernames, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.Usernames.Username.UsergroupUnderUsernames, self).__setattr__(name, value)


                class UsergroupUnderUsername(Entity):
                    """
                    Name of the usergroup
                    
                    .. attribute:: name  <key>
                    
                    	Name of the usergroup
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    

                    """

                    _prefix = 'aaa-locald-admin-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.Usernames.Username.UsergroupUnderUsernames.UsergroupUnderUsername, self).__init__()

                        self.yang_name = "usergroup-under-username"
                        self.yang_parent_name = "usergroup-under-usernames"

                        self.name = YLeaf(YType.str, "name")

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
                                    super(Aaa.Usernames.Username.UsergroupUnderUsernames.UsergroupUnderUsername, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Aaa.Usernames.Username.UsergroupUnderUsernames.UsergroupUnderUsername, self).__setattr__(name, value)

                    def has_data(self):
                        return self.name.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "usergroup-under-username" + "[name='" + self.name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.usergroup_under_username:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.usergroup_under_username:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "usergroup-under-usernames" + path_buffer

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

                    if (child_yang_name == "usergroup-under-username"):
                        for c in self.usergroup_under_username:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Aaa.Usernames.Username.UsergroupUnderUsernames.UsergroupUnderUsername()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.usergroup_under_username.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "usergroup-under-username"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.name.is_set or
                    self.secret.is_set or
                    (self.usergroup_under_usernames is not None and self.usergroup_under_usernames.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    self.secret.yfilter != YFilter.not_set or
                    (self.usergroup_under_usernames is not None and self.usergroup_under_usernames.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "username" + "[name='" + self.name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-locald-admin-cfg:aaa/usernames/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())
                if (self.secret.is_set or self.secret.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.secret.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "usergroup-under-usernames"):
                    if (self.usergroup_under_usernames is None):
                        self.usergroup_under_usernames = Aaa.Usernames.Username.UsergroupUnderUsernames()
                        self.usergroup_under_usernames.parent = self
                        self._children_name_map["usergroup_under_usernames"] = "usergroup-under-usernames"
                    return self.usergroup_under_usernames

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "usergroup-under-usernames" or name == "name" or name == "secret"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix
                if(value_path == "secret"):
                    self.secret = value
                    self.secret.value_namespace = name_space
                    self.secret.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.username:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.username:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "usernames" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-aaa-locald-admin-cfg:aaa/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "username"):
                for c in self.username:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Aaa.Usernames.Username()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.username.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "username"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.usernames is not None and self.usernames.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.usernames is not None and self.usernames.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-aaa-locald-admin-cfg:aaa" + path_buffer

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

        if (child_yang_name == "usernames"):
            if (self.usernames is None):
                self.usernames = Aaa.Usernames()
                self.usernames.parent = self
                self._children_name_map["usernames"] = "usernames"
            return self.usernames

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "usernames"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Aaa()
        return self._top_entity


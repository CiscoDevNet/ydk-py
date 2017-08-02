""" Cisco_IOS_XR_ppp_ma_ssrp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ppp\-ma\-ssrp package configuration.

This module contains definitions
for the following management objects\:
  ssrp\: Shared plane SSRP configuration data

This YANG module augments the
  Cisco\-IOS\-XR\-config\-mda\-cfg,
  Cisco\-IOS\-XR\-ifmgr\-cfg
modules with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Ssrp(Entity):
    """
    Shared plane SSRP configuration data
    
    .. attribute:: profiles
    
    	Table of SSRP Profiles
    	**type**\:   :py:class:`Profiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_ssrp_cfg.Ssrp.Profiles>`
    
    

    """

    _prefix = 'ppp-ma-ssrp-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Ssrp, self).__init__()
        self._top_entity = None

        self.yang_name = "ssrp"
        self.yang_parent_name = "Cisco-IOS-XR-ppp-ma-ssrp-cfg"

        self.profiles = Ssrp.Profiles()
        self.profiles.parent = self
        self._children_name_map["profiles"] = "profiles"
        self._children_yang_names.add("profiles")


    class Profiles(Entity):
        """
        Table of SSRP Profiles
        
        .. attribute:: profile
        
        	SSRP Profile configuration
        	**type**\: list of    :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_ssrp_cfg.Ssrp.Profiles.Profile>`
        
        

        """

        _prefix = 'ppp-ma-ssrp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ssrp.Profiles, self).__init__()

            self.yang_name = "profiles"
            self.yang_parent_name = "ssrp"

            self.profile = YList(self)

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
                        super(Ssrp.Profiles, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ssrp.Profiles, self).__setattr__(name, value)


        class Profile(Entity):
            """
            SSRP Profile configuration
            
            .. attribute:: name  <key>
            
            	The name of the profile
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: max_hops
            
            	This specifies the maximum number of hops for packets on the SSO channel
            	**type**\:  int
            
            	**range:** 1..255
            
            .. attribute:: peer_ipv4_address
            
            	This specifies the remote end's IPv4\-address for the SSO channel
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            

            """

            _prefix = 'ppp-ma-ssrp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ssrp.Profiles.Profile, self).__init__()

                self.yang_name = "profile"
                self.yang_parent_name = "profiles"

                self.name = YLeaf(YType.str, "name")

                self.max_hops = YLeaf(YType.uint32, "max-hops")

                self.peer_ipv4_address = YLeaf(YType.str, "peer-ipv4-address")

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
                                "max_hops",
                                "peer_ipv4_address") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Ssrp.Profiles.Profile, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ssrp.Profiles.Profile, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.name.is_set or
                    self.max_hops.is_set or
                    self.peer_ipv4_address.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    self.max_hops.yfilter != YFilter.not_set or
                    self.peer_ipv4_address.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "profile" + "[name='" + self.name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ppp-ma-ssrp-cfg:ssrp/profiles/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())
                if (self.max_hops.is_set or self.max_hops.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.max_hops.get_name_leafdata())
                if (self.peer_ipv4_address.is_set or self.peer_ipv4_address.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.peer_ipv4_address.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "name" or name == "max-hops" or name == "peer-ipv4-address"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix
                if(value_path == "max-hops"):
                    self.max_hops = value
                    self.max_hops.value_namespace = name_space
                    self.max_hops.value_namespace_prefix = name_space_prefix
                if(value_path == "peer-ipv4-address"):
                    self.peer_ipv4_address = value
                    self.peer_ipv4_address.value_namespace = name_space
                    self.peer_ipv4_address.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.profile:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.profile:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "profiles" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ppp-ma-ssrp-cfg:ssrp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "profile"):
                for c in self.profile:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Ssrp.Profiles.Profile()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.profile.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "profile"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.profiles is not None and self.profiles.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.profiles is not None and self.profiles.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ppp-ma-ssrp-cfg:ssrp" + path_buffer

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

        if (child_yang_name == "profiles"):
            if (self.profiles is None):
                self.profiles = Ssrp.Profiles()
                self.profiles.parent = self
                self._children_name_map["profiles"] = "profiles"
            return self.profiles

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "profiles"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Ssrp()
        return self._top_entity


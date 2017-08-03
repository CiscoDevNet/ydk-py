""" Cisco_IOS_XR_lpts_lib_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR lpts\-lib package configuration.

This module contains definitions
for the following management objects\:
  lpts\: lpts configuration commands

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Lpts(Entity):
    """
    lpts configuration commands
    
    .. attribute:: ipolicer
    
    	Pre IFiB Configuration 
    	**type**\:   :py:class:`Ipolicer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer>`
    
    	**presence node**\: True
    
    .. attribute:: punt
    
    	Configure penalty timeout value
    	**type**\:   :py:class:`Punt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Punt>`
    
    

    """

    _prefix = 'lpts-lib-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Lpts, self).__init__()
        self._top_entity = None

        self.yang_name = "lpts"
        self.yang_parent_name = "Cisco-IOS-XR-lpts-lib-cfg"

        self.ipolicer = None
        self._children_name_map["ipolicer"] = "ipolicer"
        self._children_yang_names.add("ipolicer")

        self.punt = Lpts.Punt()
        self.punt.parent = self
        self._children_name_map["punt"] = "punt"
        self._children_yang_names.add("punt")


    class Ipolicer(Entity):
        """
        Pre IFiB Configuration 
        
        .. attribute:: enable
        
        	Enabled
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        	**mandatory**\: True
        
        .. attribute:: flows
        
        	Table for Flows
        	**type**\:   :py:class:`Flows <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer.Flows>`
        
        .. attribute:: ipv4acls
        
        	Table for ACLs
        	**type**\:   :py:class:`Ipv4Acls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer.Ipv4Acls>`
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'lpts-pre-ifib-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Lpts.Ipolicer, self).__init__()

            self.yang_name = "ipolicer"
            self.yang_parent_name = "lpts"
            self.is_presence_container = True

            self.enable = YLeaf(YType.empty, "enable")

            self.flows = Lpts.Ipolicer.Flows()
            self.flows.parent = self
            self._children_name_map["flows"] = "flows"
            self._children_yang_names.add("flows")

            self.ipv4acls = Lpts.Ipolicer.Ipv4Acls()
            self.ipv4acls.parent = self
            self._children_name_map["ipv4acls"] = "ipv4acls"
            self._children_yang_names.add("ipv4acls")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("enable") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Lpts.Ipolicer, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Lpts.Ipolicer, self).__setattr__(name, value)


        class Ipv4Acls(Entity):
            """
            Table for ACLs
            
            .. attribute:: ipv4acl
            
            	ACL name
            	**type**\: list of    :py:class:`Ipv4Acl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer.Ipv4Acls.Ipv4Acl>`
            
            

            """

            _prefix = 'lpts-pre-ifib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Lpts.Ipolicer.Ipv4Acls, self).__init__()

                self.yang_name = "ipv4acls"
                self.yang_parent_name = "ipolicer"

                self.ipv4acl = YList(self)

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
                            super(Lpts.Ipolicer.Ipv4Acls, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Lpts.Ipolicer.Ipv4Acls, self).__setattr__(name, value)


            class Ipv4Acl(Entity):
                """
                ACL name
                
                .. attribute:: acl_name  <key>
                
                	ACL name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: ipv4vrf_names
                
                	VRF list
                	**type**\:   :py:class:`Ipv4VrfNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer.Ipv4Acls.Ipv4Acl.Ipv4VrfNames>`
                
                

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Lpts.Ipolicer.Ipv4Acls.Ipv4Acl, self).__init__()

                    self.yang_name = "ipv4acl"
                    self.yang_parent_name = "ipv4acls"

                    self.acl_name = YLeaf(YType.str, "acl-name")

                    self.ipv4vrf_names = Lpts.Ipolicer.Ipv4Acls.Ipv4Acl.Ipv4VrfNames()
                    self.ipv4vrf_names.parent = self
                    self._children_name_map["ipv4vrf_names"] = "ipv4vrf-names"
                    self._children_yang_names.add("ipv4vrf-names")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("acl_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Lpts.Ipolicer.Ipv4Acls.Ipv4Acl, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Lpts.Ipolicer.Ipv4Acls.Ipv4Acl, self).__setattr__(name, value)


                class Ipv4VrfNames(Entity):
                    """
                    VRF list
                    
                    .. attribute:: ipv4vrf_name
                    
                    	VRF name
                    	**type**\: list of    :py:class:`Ipv4VrfName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer.Ipv4Acls.Ipv4Acl.Ipv4VrfNames.Ipv4VrfName>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Lpts.Ipolicer.Ipv4Acls.Ipv4Acl.Ipv4VrfNames, self).__init__()

                        self.yang_name = "ipv4vrf-names"
                        self.yang_parent_name = "ipv4acl"

                        self.ipv4vrf_name = YList(self)

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
                                    super(Lpts.Ipolicer.Ipv4Acls.Ipv4Acl.Ipv4VrfNames, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Lpts.Ipolicer.Ipv4Acls.Ipv4Acl.Ipv4VrfNames, self).__setattr__(name, value)


                    class Ipv4VrfName(Entity):
                        """
                        VRF name
                        
                        .. attribute:: vrf_name  <key>
                        
                        	VRF name
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: acl_rate
                        
                        	pre\-ifib policer rate config commands
                        	**type**\:  int
                        
                        	**range:** 0..100000
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Lpts.Ipolicer.Ipv4Acls.Ipv4Acl.Ipv4VrfNames.Ipv4VrfName, self).__init__()

                            self.yang_name = "ipv4vrf-name"
                            self.yang_parent_name = "ipv4vrf-names"

                            self.vrf_name = YLeaf(YType.str, "vrf-name")

                            self.acl_rate = YLeaf(YType.uint32, "acl-rate")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("vrf_name",
                                            "acl_rate") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Lpts.Ipolicer.Ipv4Acls.Ipv4Acl.Ipv4VrfNames.Ipv4VrfName, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Lpts.Ipolicer.Ipv4Acls.Ipv4Acl.Ipv4VrfNames.Ipv4VrfName, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.vrf_name.is_set or
                                self.acl_rate.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.vrf_name.yfilter != YFilter.not_set or
                                self.acl_rate.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "ipv4vrf-name" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.vrf_name.get_name_leafdata())
                            if (self.acl_rate.is_set or self.acl_rate.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.acl_rate.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "vrf-name" or name == "acl-rate"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "vrf-name"):
                                self.vrf_name = value
                                self.vrf_name.value_namespace = name_space
                                self.vrf_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "acl-rate"):
                                self.acl_rate = value
                                self.acl_rate.value_namespace = name_space
                                self.acl_rate.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.ipv4vrf_name:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.ipv4vrf_name:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ipv4vrf-names" + path_buffer

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

                        if (child_yang_name == "ipv4vrf-name"):
                            for c in self.ipv4vrf_name:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Lpts.Ipolicer.Ipv4Acls.Ipv4Acl.Ipv4VrfNames.Ipv4VrfName()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.ipv4vrf_name.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "ipv4vrf-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.acl_name.is_set or
                        (self.ipv4vrf_names is not None and self.ipv4vrf_names.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.acl_name.yfilter != YFilter.not_set or
                        (self.ipv4vrf_names is not None and self.ipv4vrf_names.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ipv4acl" + "[acl-name='" + self.acl_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipolicer/ipv4acls/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.acl_name.is_set or self.acl_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.acl_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "ipv4vrf-names"):
                        if (self.ipv4vrf_names is None):
                            self.ipv4vrf_names = Lpts.Ipolicer.Ipv4Acls.Ipv4Acl.Ipv4VrfNames()
                            self.ipv4vrf_names.parent = self
                            self._children_name_map["ipv4vrf_names"] = "ipv4vrf-names"
                        return self.ipv4vrf_names

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ipv4vrf-names" or name == "acl-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "acl-name"):
                        self.acl_name = value
                        self.acl_name.value_namespace = name_space
                        self.acl_name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.ipv4acl:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.ipv4acl:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ipv4acls" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipolicer/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "ipv4acl"):
                    for c in self.ipv4acl:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Lpts.Ipolicer.Ipv4Acls.Ipv4Acl()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.ipv4acl.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ipv4acl"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Flows(Entity):
            """
            Table for Flows
            
            .. attribute:: flow
            
            	selected flow type
            	**type**\: list of    :py:class:`Flow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer.Flows.Flow>`
            
            

            """

            _prefix = 'lpts-pre-ifib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Lpts.Ipolicer.Flows, self).__init__()

                self.yang_name = "flows"
                self.yang_parent_name = "ipolicer"

                self.flow = YList(self)

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
                            super(Lpts.Ipolicer.Flows, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Lpts.Ipolicer.Flows, self).__setattr__(name, value)


            class Flow(Entity):
                """
                selected flow type
                
                .. attribute:: flow_type  <key>
                
                	LPTS Flow Type
                	**type**\:   :py:class:`LptsFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsFlow>`
                
                .. attribute:: precedences
                
                	TOS Precedence value(s)
                	**type**\:   :py:class:`Precedences <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer.Flows.Flow.Precedences>`
                
                .. attribute:: rate
                
                	Configured rate value
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Lpts.Ipolicer.Flows.Flow, self).__init__()

                    self.yang_name = "flow"
                    self.yang_parent_name = "flows"

                    self.flow_type = YLeaf(YType.enumeration, "flow-type")

                    self.rate = YLeaf(YType.int32, "rate")

                    self.precedences = Lpts.Ipolicer.Flows.Flow.Precedences()
                    self.precedences.parent = self
                    self._children_name_map["precedences"] = "precedences"
                    self._children_yang_names.add("precedences")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("flow_type",
                                    "rate") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Lpts.Ipolicer.Flows.Flow, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Lpts.Ipolicer.Flows.Flow, self).__setattr__(name, value)


                class Precedences(Entity):
                    """
                    TOS Precedence value(s)
                    
                    .. attribute:: precedence
                    
                    	Precedence values
                    	**type**\: one of the below types:
                    
                    	**type**\:  list of   :py:class:`LptsPreIFibPrecedenceNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsPreIFibPrecedenceNumber>`
                    
                    
                    ----
                    	**type**\:  list of int
                    
                    	**range:** 0..7
                    
                    
                    ----
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Lpts.Ipolicer.Flows.Flow.Precedences, self).__init__()

                        self.yang_name = "precedences"
                        self.yang_parent_name = "flow"

                        self.precedence = YLeafList(YType.str, "precedence")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("precedence") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Lpts.Ipolicer.Flows.Flow.Precedences, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Lpts.Ipolicer.Flows.Flow.Precedences, self).__setattr__(name, value)

                    def has_data(self):
                        for leaf in self.precedence.getYLeafs():
                            if (leaf.yfilter != YFilter.not_set):
                                return True
                        return False

                    def has_operation(self):
                        for leaf in self.precedence.getYLeafs():
                            if (leaf.is_set):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.precedence.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "precedences" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        leaf_name_data.extend(self.precedence.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "precedence"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "precedence"):
                            self.precedence.append(value)

                def has_data(self):
                    return (
                        self.flow_type.is_set or
                        self.rate.is_set or
                        (self.precedences is not None and self.precedences.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.flow_type.yfilter != YFilter.not_set or
                        self.rate.yfilter != YFilter.not_set or
                        (self.precedences is not None and self.precedences.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "flow" + "[flow-type='" + self.flow_type.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipolicer/flows/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.flow_type.is_set or self.flow_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.flow_type.get_name_leafdata())
                    if (self.rate.is_set or self.rate.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rate.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "precedences"):
                        if (self.precedences is None):
                            self.precedences = Lpts.Ipolicer.Flows.Flow.Precedences()
                            self.precedences.parent = self
                            self._children_name_map["precedences"] = "precedences"
                        return self.precedences

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "precedences" or name == "flow-type" or name == "rate"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "flow-type"):
                        self.flow_type = value
                        self.flow_type.value_namespace = name_space
                        self.flow_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "rate"):
                        self.rate = value
                        self.rate.value_namespace = name_space
                        self.rate.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.flow:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.flow:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "flows" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipolicer/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "flow"):
                    for c in self.flow:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Lpts.Ipolicer.Flows.Flow()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.flow.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "flow"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                self.enable.is_set or
                (self.flows is not None and self.flows.has_data()) or
                (self.ipv4acls is not None and self.ipv4acls.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.enable.yfilter != YFilter.not_set or
                (self.flows is not None and self.flows.has_operation()) or
                (self.ipv4acls is not None and self.ipv4acls.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "Cisco-IOS-XR-lpts-pre-ifib-cfg:ipolicer" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-lpts-lib-cfg:lpts/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.enable.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "flows"):
                if (self.flows is None):
                    self.flows = Lpts.Ipolicer.Flows()
                    self.flows.parent = self
                    self._children_name_map["flows"] = "flows"
                return self.flows

            if (child_yang_name == "ipv4acls"):
                if (self.ipv4acls is None):
                    self.ipv4acls = Lpts.Ipolicer.Ipv4Acls()
                    self.ipv4acls.parent = self
                    self._children_name_map["ipv4acls"] = "ipv4acls"
                return self.ipv4acls

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "flows" or name == "ipv4acls" or name == "enable"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "enable"):
                self.enable = value
                self.enable.value_namespace = name_space
                self.enable.value_namespace_prefix = name_space_prefix


    class Punt(Entity):
        """
        Configure penalty timeout value
        
        .. attribute:: flowtrap
        
        	excessive punt flow trap configuration commands
        	**type**\:   :py:class:`Flowtrap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Punt.Flowtrap>`
        
        

        """

        _prefix = 'lpts-punt-flowtrap-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Lpts.Punt, self).__init__()

            self.yang_name = "punt"
            self.yang_parent_name = "lpts"

            self.flowtrap = Lpts.Punt.Flowtrap()
            self.flowtrap.parent = self
            self._children_name_map["flowtrap"] = "flowtrap"
            self._children_yang_names.add("flowtrap")


        class Flowtrap(Entity):
            """
            excessive punt flow trap configuration commands
            
            .. attribute:: dampening
            
            	Dampening period for a bad actor flow in milliseconds
            	**type**\:  int
            
            	**range:** 5000..60000
            
            .. attribute:: et_size
            
            	Should be power of 2. Any one of 1,2,4,8,16,32 ,64,128
            	**type**\:  int
            
            	**range:** 1..128
            
            .. attribute:: eviction_search_limit
            
            	Eviction search limit, should be less than trap\-size
            	**type**\:  int
            
            	**range:** 1..128
            
            .. attribute:: eviction_threshold
            
            	Eviction threshold, should be less than report\-threshold
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: exclude
            
            	Exclude an item from all traps
            	**type**\:   :py:class:`Exclude <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Punt.Flowtrap.Exclude>`
            
            .. attribute:: interface_based_flow
            
            	Identify flow based on interface and flowtype
            	**type**\:  bool
            
            .. attribute:: max_flow_gap
            
            	Maximum flow gap in milliseconds
            	**type**\:  int
            
            	**range:** 1..60000
            
            .. attribute:: non_subscriber_interfaces
            
            	Enable trap based on source mac on non\-subscriber interface
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: penalty_rates
            
            	Configure penalty policing rate
            	**type**\:   :py:class:`PenaltyRates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Punt.Flowtrap.PenaltyRates>`
            
            .. attribute:: penalty_timeouts
            
            	Configure penalty timeout value
            	**type**\:   :py:class:`PenaltyTimeouts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Punt.Flowtrap.PenaltyTimeouts>`
            
            .. attribute:: report_threshold
            
            	Threshold to cross for a flow to be considered as bad actor flow
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: routing_protocols_enable
            
            	Allow routing protocols to pass through copp sampler
            	**type**\:  bool
            
            .. attribute:: sample_prob
            
            	Probability of packets to be sampled
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: subscriber_interfaces
            
            	Enable the trap on subscriber interfaces
            	**type**\:  bool
            
            

            """

            _prefix = 'lpts-punt-flowtrap-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Lpts.Punt.Flowtrap, self).__init__()

                self.yang_name = "flowtrap"
                self.yang_parent_name = "punt"

                self.dampening = YLeaf(YType.uint32, "dampening")

                self.et_size = YLeaf(YType.uint32, "et-size")

                self.eviction_search_limit = YLeaf(YType.uint32, "eviction-search-limit")

                self.eviction_threshold = YLeaf(YType.uint32, "eviction-threshold")

                self.interface_based_flow = YLeaf(YType.boolean, "interface-based-flow")

                self.max_flow_gap = YLeaf(YType.uint32, "max-flow-gap")

                self.non_subscriber_interfaces = YLeaf(YType.int32, "non-subscriber-interfaces")

                self.report_threshold = YLeaf(YType.uint16, "report-threshold")

                self.routing_protocols_enable = YLeaf(YType.boolean, "routing-protocols-enable")

                self.sample_prob = YLeaf(YType.str, "sample-prob")

                self.subscriber_interfaces = YLeaf(YType.boolean, "subscriber-interfaces")

                self.exclude = Lpts.Punt.Flowtrap.Exclude()
                self.exclude.parent = self
                self._children_name_map["exclude"] = "exclude"
                self._children_yang_names.add("exclude")

                self.penalty_rates = Lpts.Punt.Flowtrap.PenaltyRates()
                self.penalty_rates.parent = self
                self._children_name_map["penalty_rates"] = "penalty-rates"
                self._children_yang_names.add("penalty-rates")

                self.penalty_timeouts = Lpts.Punt.Flowtrap.PenaltyTimeouts()
                self.penalty_timeouts.parent = self
                self._children_name_map["penalty_timeouts"] = "penalty-timeouts"
                self._children_yang_names.add("penalty-timeouts")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dampening",
                                "et_size",
                                "eviction_search_limit",
                                "eviction_threshold",
                                "interface_based_flow",
                                "max_flow_gap",
                                "non_subscriber_interfaces",
                                "report_threshold",
                                "routing_protocols_enable",
                                "sample_prob",
                                "subscriber_interfaces") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Lpts.Punt.Flowtrap, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Lpts.Punt.Flowtrap, self).__setattr__(name, value)


            class PenaltyRates(Entity):
                """
                Configure penalty policing rate
                
                .. attribute:: penalty_rate
                
                	none
                	**type**\: list of    :py:class:`PenaltyRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Punt.Flowtrap.PenaltyRates.PenaltyRate>`
                
                

                """

                _prefix = 'lpts-punt-flowtrap-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Lpts.Punt.Flowtrap.PenaltyRates, self).__init__()

                    self.yang_name = "penalty-rates"
                    self.yang_parent_name = "flowtrap"

                    self.penalty_rate = YList(self)

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
                                super(Lpts.Punt.Flowtrap.PenaltyRates, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Lpts.Punt.Flowtrap.PenaltyRates, self).__setattr__(name, value)


                class PenaltyRate(Entity):
                    """
                    none
                    
                    .. attribute:: protocol_name  <key>
                    
                    	none
                    	**type**\:   :py:class:`LptsPuntFlowtrapProtoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_punt_flowtrap_cfg.LptsPuntFlowtrapProtoId>`
                    
                    .. attribute:: rate
                    
                    	Penalty policer rate in packets\-per\-second
                    	**type**\:  int
                    
                    	**range:** 2..100
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'lpts-punt-flowtrap-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Lpts.Punt.Flowtrap.PenaltyRates.PenaltyRate, self).__init__()

                        self.yang_name = "penalty-rate"
                        self.yang_parent_name = "penalty-rates"

                        self.protocol_name = YLeaf(YType.enumeration, "protocol-name")

                        self.rate = YLeaf(YType.uint32, "rate")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("protocol_name",
                                        "rate") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Lpts.Punt.Flowtrap.PenaltyRates.PenaltyRate, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Lpts.Punt.Flowtrap.PenaltyRates.PenaltyRate, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.protocol_name.is_set or
                            self.rate.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.protocol_name.yfilter != YFilter.not_set or
                            self.rate.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "penalty-rate" + "[protocol-name='" + self.protocol_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:punt/flowtrap/penalty-rates/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.protocol_name.is_set or self.protocol_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.protocol_name.get_name_leafdata())
                        if (self.rate.is_set or self.rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rate.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "protocol-name" or name == "rate"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "protocol-name"):
                            self.protocol_name = value
                            self.protocol_name.value_namespace = name_space
                            self.protocol_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "rate"):
                            self.rate = value
                            self.rate.value_namespace = name_space
                            self.rate.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.penalty_rate:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.penalty_rate:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "penalty-rates" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:punt/flowtrap/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "penalty-rate"):
                        for c in self.penalty_rate:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Lpts.Punt.Flowtrap.PenaltyRates.PenaltyRate()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.penalty_rate.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "penalty-rate"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class PenaltyTimeouts(Entity):
                """
                Configure penalty timeout value
                
                .. attribute:: penalty_timeout
                
                	none
                	**type**\: list of    :py:class:`PenaltyTimeout <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Punt.Flowtrap.PenaltyTimeouts.PenaltyTimeout>`
                
                

                """

                _prefix = 'lpts-punt-flowtrap-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Lpts.Punt.Flowtrap.PenaltyTimeouts, self).__init__()

                    self.yang_name = "penalty-timeouts"
                    self.yang_parent_name = "flowtrap"

                    self.penalty_timeout = YList(self)

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
                                super(Lpts.Punt.Flowtrap.PenaltyTimeouts, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Lpts.Punt.Flowtrap.PenaltyTimeouts, self).__setattr__(name, value)


                class PenaltyTimeout(Entity):
                    """
                    none
                    
                    .. attribute:: protocol_name  <key>
                    
                    	none
                    	**type**\:   :py:class:`LptsPuntFlowtrapProtoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_punt_flowtrap_cfg.LptsPuntFlowtrapProtoId>`
                    
                    .. attribute:: timeout
                    
                    	Timeout value in minutes
                    	**type**\:  int
                    
                    	**range:** 1..1000
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'lpts-punt-flowtrap-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Lpts.Punt.Flowtrap.PenaltyTimeouts.PenaltyTimeout, self).__init__()

                        self.yang_name = "penalty-timeout"
                        self.yang_parent_name = "penalty-timeouts"

                        self.protocol_name = YLeaf(YType.enumeration, "protocol-name")

                        self.timeout = YLeaf(YType.uint32, "timeout")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("protocol_name",
                                        "timeout") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Lpts.Punt.Flowtrap.PenaltyTimeouts.PenaltyTimeout, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Lpts.Punt.Flowtrap.PenaltyTimeouts.PenaltyTimeout, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.protocol_name.is_set or
                            self.timeout.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.protocol_name.yfilter != YFilter.not_set or
                            self.timeout.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "penalty-timeout" + "[protocol-name='" + self.protocol_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:punt/flowtrap/penalty-timeouts/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.protocol_name.is_set or self.protocol_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.protocol_name.get_name_leafdata())
                        if (self.timeout.is_set or self.timeout.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.timeout.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "protocol-name" or name == "timeout"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "protocol-name"):
                            self.protocol_name = value
                            self.protocol_name.value_namespace = name_space
                            self.protocol_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "timeout"):
                            self.timeout = value
                            self.timeout.value_namespace = name_space
                            self.timeout.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.penalty_timeout:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.penalty_timeout:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "penalty-timeouts" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:punt/flowtrap/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "penalty-timeout"):
                        for c in self.penalty_timeout:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Lpts.Punt.Flowtrap.PenaltyTimeouts.PenaltyTimeout()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.penalty_timeout.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "penalty-timeout"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Exclude(Entity):
                """
                Exclude an item from all traps
                
                .. attribute:: interface_names
                
                	none
                	**type**\:   :py:class:`InterfaceNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Punt.Flowtrap.Exclude.InterfaceNames>`
                
                

                """

                _prefix = 'lpts-punt-flowtrap-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Lpts.Punt.Flowtrap.Exclude, self).__init__()

                    self.yang_name = "exclude"
                    self.yang_parent_name = "flowtrap"

                    self.interface_names = Lpts.Punt.Flowtrap.Exclude.InterfaceNames()
                    self.interface_names.parent = self
                    self._children_name_map["interface_names"] = "interface-names"
                    self._children_yang_names.add("interface-names")


                class InterfaceNames(Entity):
                    """
                    none
                    
                    .. attribute:: interface_name
                    
                    	Name of interface to exclude from all traps
                    	**type**\: list of    :py:class:`InterfaceName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Punt.Flowtrap.Exclude.InterfaceNames.InterfaceName>`
                    
                    

                    """

                    _prefix = 'lpts-punt-flowtrap-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Lpts.Punt.Flowtrap.Exclude.InterfaceNames, self).__init__()

                        self.yang_name = "interface-names"
                        self.yang_parent_name = "exclude"

                        self.interface_name = YList(self)

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
                                    super(Lpts.Punt.Flowtrap.Exclude.InterfaceNames, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Lpts.Punt.Flowtrap.Exclude.InterfaceNames, self).__setattr__(name, value)


                    class InterfaceName(Entity):
                        """
                        Name of interface to exclude from all traps
                        
                        .. attribute:: ifname  <key>
                        
                        	Name of interface to exclude from all traps
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: id1
                        
                        	Enabled or disabled
                        	**type**\:  bool
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'lpts-punt-flowtrap-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Lpts.Punt.Flowtrap.Exclude.InterfaceNames.InterfaceName, self).__init__()

                            self.yang_name = "interface-name"
                            self.yang_parent_name = "interface-names"

                            self.ifname = YLeaf(YType.str, "ifname")

                            self.id1 = YLeaf(YType.boolean, "id1")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("ifname",
                                            "id1") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Lpts.Punt.Flowtrap.Exclude.InterfaceNames.InterfaceName, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Lpts.Punt.Flowtrap.Exclude.InterfaceNames.InterfaceName, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.ifname.is_set or
                                self.id1.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.ifname.yfilter != YFilter.not_set or
                                self.id1.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "interface-name" + "[ifname='" + self.ifname.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:punt/flowtrap/exclude/interface-names/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.ifname.is_set or self.ifname.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ifname.get_name_leafdata())
                            if (self.id1.is_set or self.id1.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.id1.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ifname" or name == "id1"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "ifname"):
                                self.ifname = value
                                self.ifname.value_namespace = name_space
                                self.ifname.value_namespace_prefix = name_space_prefix
                            if(value_path == "id1"):
                                self.id1 = value
                                self.id1.value_namespace = name_space
                                self.id1.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.interface_name:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.interface_name:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface-names" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:punt/flowtrap/exclude/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "interface-name"):
                            for c in self.interface_name:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Lpts.Punt.Flowtrap.Exclude.InterfaceNames.InterfaceName()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.interface_name.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "interface-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (self.interface_names is not None and self.interface_names.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.interface_names is not None and self.interface_names.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "exclude" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:punt/flowtrap/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "interface-names"):
                        if (self.interface_names is None):
                            self.interface_names = Lpts.Punt.Flowtrap.Exclude.InterfaceNames()
                            self.interface_names.parent = self
                            self._children_name_map["interface_names"] = "interface-names"
                        return self.interface_names

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface-names"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.dampening.is_set or
                    self.et_size.is_set or
                    self.eviction_search_limit.is_set or
                    self.eviction_threshold.is_set or
                    self.interface_based_flow.is_set or
                    self.max_flow_gap.is_set or
                    self.non_subscriber_interfaces.is_set or
                    self.report_threshold.is_set or
                    self.routing_protocols_enable.is_set or
                    self.sample_prob.is_set or
                    self.subscriber_interfaces.is_set or
                    (self.exclude is not None and self.exclude.has_data()) or
                    (self.penalty_rates is not None and self.penalty_rates.has_data()) or
                    (self.penalty_timeouts is not None and self.penalty_timeouts.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dampening.yfilter != YFilter.not_set or
                    self.et_size.yfilter != YFilter.not_set or
                    self.eviction_search_limit.yfilter != YFilter.not_set or
                    self.eviction_threshold.yfilter != YFilter.not_set or
                    self.interface_based_flow.yfilter != YFilter.not_set or
                    self.max_flow_gap.yfilter != YFilter.not_set or
                    self.non_subscriber_interfaces.yfilter != YFilter.not_set or
                    self.report_threshold.yfilter != YFilter.not_set or
                    self.routing_protocols_enable.yfilter != YFilter.not_set or
                    self.sample_prob.yfilter != YFilter.not_set or
                    self.subscriber_interfaces.yfilter != YFilter.not_set or
                    (self.exclude is not None and self.exclude.has_operation()) or
                    (self.penalty_rates is not None and self.penalty_rates.has_operation()) or
                    (self.penalty_timeouts is not None and self.penalty_timeouts.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "flowtrap" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:punt/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dampening.is_set or self.dampening.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dampening.get_name_leafdata())
                if (self.et_size.is_set or self.et_size.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.et_size.get_name_leafdata())
                if (self.eviction_search_limit.is_set or self.eviction_search_limit.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.eviction_search_limit.get_name_leafdata())
                if (self.eviction_threshold.is_set or self.eviction_threshold.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.eviction_threshold.get_name_leafdata())
                if (self.interface_based_flow.is_set or self.interface_based_flow.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface_based_flow.get_name_leafdata())
                if (self.max_flow_gap.is_set or self.max_flow_gap.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.max_flow_gap.get_name_leafdata())
                if (self.non_subscriber_interfaces.is_set or self.non_subscriber_interfaces.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.non_subscriber_interfaces.get_name_leafdata())
                if (self.report_threshold.is_set or self.report_threshold.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.report_threshold.get_name_leafdata())
                if (self.routing_protocols_enable.is_set or self.routing_protocols_enable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.routing_protocols_enable.get_name_leafdata())
                if (self.sample_prob.is_set or self.sample_prob.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sample_prob.get_name_leafdata())
                if (self.subscriber_interfaces.is_set or self.subscriber_interfaces.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.subscriber_interfaces.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "exclude"):
                    if (self.exclude is None):
                        self.exclude = Lpts.Punt.Flowtrap.Exclude()
                        self.exclude.parent = self
                        self._children_name_map["exclude"] = "exclude"
                    return self.exclude

                if (child_yang_name == "penalty-rates"):
                    if (self.penalty_rates is None):
                        self.penalty_rates = Lpts.Punt.Flowtrap.PenaltyRates()
                        self.penalty_rates.parent = self
                        self._children_name_map["penalty_rates"] = "penalty-rates"
                    return self.penalty_rates

                if (child_yang_name == "penalty-timeouts"):
                    if (self.penalty_timeouts is None):
                        self.penalty_timeouts = Lpts.Punt.Flowtrap.PenaltyTimeouts()
                        self.penalty_timeouts.parent = self
                        self._children_name_map["penalty_timeouts"] = "penalty-timeouts"
                    return self.penalty_timeouts

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "exclude" or name == "penalty-rates" or name == "penalty-timeouts" or name == "dampening" or name == "et-size" or name == "eviction-search-limit" or name == "eviction-threshold" or name == "interface-based-flow" or name == "max-flow-gap" or name == "non-subscriber-interfaces" or name == "report-threshold" or name == "routing-protocols-enable" or name == "sample-prob" or name == "subscriber-interfaces"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dampening"):
                    self.dampening = value
                    self.dampening.value_namespace = name_space
                    self.dampening.value_namespace_prefix = name_space_prefix
                if(value_path == "et-size"):
                    self.et_size = value
                    self.et_size.value_namespace = name_space
                    self.et_size.value_namespace_prefix = name_space_prefix
                if(value_path == "eviction-search-limit"):
                    self.eviction_search_limit = value
                    self.eviction_search_limit.value_namespace = name_space
                    self.eviction_search_limit.value_namespace_prefix = name_space_prefix
                if(value_path == "eviction-threshold"):
                    self.eviction_threshold = value
                    self.eviction_threshold.value_namespace = name_space
                    self.eviction_threshold.value_namespace_prefix = name_space_prefix
                if(value_path == "interface-based-flow"):
                    self.interface_based_flow = value
                    self.interface_based_flow.value_namespace = name_space
                    self.interface_based_flow.value_namespace_prefix = name_space_prefix
                if(value_path == "max-flow-gap"):
                    self.max_flow_gap = value
                    self.max_flow_gap.value_namespace = name_space
                    self.max_flow_gap.value_namespace_prefix = name_space_prefix
                if(value_path == "non-subscriber-interfaces"):
                    self.non_subscriber_interfaces = value
                    self.non_subscriber_interfaces.value_namespace = name_space
                    self.non_subscriber_interfaces.value_namespace_prefix = name_space_prefix
                if(value_path == "report-threshold"):
                    self.report_threshold = value
                    self.report_threshold.value_namespace = name_space
                    self.report_threshold.value_namespace_prefix = name_space_prefix
                if(value_path == "routing-protocols-enable"):
                    self.routing_protocols_enable = value
                    self.routing_protocols_enable.value_namespace = name_space
                    self.routing_protocols_enable.value_namespace_prefix = name_space_prefix
                if(value_path == "sample-prob"):
                    self.sample_prob = value
                    self.sample_prob.value_namespace = name_space
                    self.sample_prob.value_namespace_prefix = name_space_prefix
                if(value_path == "subscriber-interfaces"):
                    self.subscriber_interfaces = value
                    self.subscriber_interfaces.value_namespace = name_space
                    self.subscriber_interfaces.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (self.flowtrap is not None and self.flowtrap.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.flowtrap is not None and self.flowtrap.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "Cisco-IOS-XR-lpts-punt-flowtrap-cfg:punt" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-lpts-lib-cfg:lpts/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "flowtrap"):
                if (self.flowtrap is None):
                    self.flowtrap = Lpts.Punt.Flowtrap()
                    self.flowtrap.parent = self
                    self._children_name_map["flowtrap"] = "flowtrap"
                return self.flowtrap

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "flowtrap"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.punt is not None and self.punt.has_data()) or
            (self.ipolicer is not None))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.ipolicer is not None and self.ipolicer.has_operation()) or
            (self.punt is not None and self.punt.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-lpts-lib-cfg:lpts" + path_buffer

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

        if (child_yang_name == "ipolicer"):
            if (self.ipolicer is None):
                self.ipolicer = Lpts.Ipolicer()
                self.ipolicer.parent = self
                self._children_name_map["ipolicer"] = "ipolicer"
            return self.ipolicer

        if (child_yang_name == "punt"):
            if (self.punt is None):
                self.punt = Lpts.Punt()
                self.punt.parent = self
                self._children_name_map["punt"] = "punt"
            return self.punt

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "ipolicer" or name == "punt"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Lpts()
        return self._top_entity


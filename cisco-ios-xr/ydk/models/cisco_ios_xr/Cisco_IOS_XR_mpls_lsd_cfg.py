""" Cisco_IOS_XR_mpls_lsd_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR mpls\-lsd package configuration.

This module contains definitions
for the following management objects\:
  mpls\-lsd\: MPLS LSD configuration data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class MplsIpTtlPropagateDisable(Enum):
    """
    MplsIpTtlPropagateDisable

    Mpls ip ttl propagate disable

    .. data:: all = 0

    	Disable IP TTL propagation for all MPLS packets

    .. data:: forward = 1

    	Disable IP TTL propagation for only forwarded

    	MPLS packets

    .. data:: local = 2

    	Disable IP TTL propagation for only locally

    	generated MPLS packets

    """

    all = Enum.YLeaf(0, "all")

    forward = Enum.YLeaf(1, "forward")

    local = Enum.YLeaf(2, "local")



class MplsLsd(Entity):
    """
    MPLS LSD configuration data
    
    .. attribute:: app_reg_delay_disable
    
    	Disable LSD application reg delay
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: ipv4
    
    	Configure IPv4 parameters
    	**type**\:   :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_lsd_cfg.MplsLsd.Ipv4>`
    
    .. attribute:: ipv6
    
    	Configure IPv6 parameters
    	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_lsd_cfg.MplsLsd.Ipv6>`
    
    .. attribute:: label_databases
    
    	Table of label databases
    	**type**\:   :py:class:`LabelDatabases <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_lsd_cfg.MplsLsd.LabelDatabases>`
    
    .. attribute:: mpls_entropy_label
    
    	Enable MPLS Entropy Label
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: mpls_ip_ttl_propagate_disable
    
    	Disable Propagation of IP TTL onto the label stack
    	**type**\:   :py:class:`MplsIpTtlPropagateDisable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_lsd_cfg.MplsIpTtlPropagateDisable>`
    
    

    """

    _prefix = 'mpls-lsd-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(MplsLsd, self).__init__()
        self._top_entity = None

        self.yang_name = "mpls-lsd"
        self.yang_parent_name = "Cisco-IOS-XR-mpls-lsd-cfg"

        self.app_reg_delay_disable = YLeaf(YType.empty, "app-reg-delay-disable")

        self.mpls_entropy_label = YLeaf(YType.empty, "mpls-entropy-label")

        self.mpls_ip_ttl_propagate_disable = YLeaf(YType.enumeration, "mpls-ip-ttl-propagate-disable")

        self.ipv4 = MplsLsd.Ipv4()
        self.ipv4.parent = self
        self._children_name_map["ipv4"] = "ipv4"
        self._children_yang_names.add("ipv4")

        self.ipv6 = MplsLsd.Ipv6()
        self.ipv6.parent = self
        self._children_name_map["ipv6"] = "ipv6"
        self._children_yang_names.add("ipv6")

        self.label_databases = MplsLsd.LabelDatabases()
        self.label_databases.parent = self
        self._children_name_map["label_databases"] = "label-databases"
        self._children_yang_names.add("label-databases")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("app_reg_delay_disable",
                        "mpls_entropy_label",
                        "mpls_ip_ttl_propagate_disable") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(MplsLsd, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(MplsLsd, self).__setattr__(name, value)


    class Ipv6(Entity):
        """
        Configure IPv6 parameters
        
        .. attribute:: ttl_expiration_pop
        
        	Number of labels to pop upon MPLS IP TTL expiry
        	**type**\:  int
        
        	**range:** 1..10
        
        

        """

        _prefix = 'mpls-lsd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(MplsLsd.Ipv6, self).__init__()

            self.yang_name = "ipv6"
            self.yang_parent_name = "mpls-lsd"

            self.ttl_expiration_pop = YLeaf(YType.uint32, "ttl-expiration-pop")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("ttl_expiration_pop") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(MplsLsd.Ipv6, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsLsd.Ipv6, self).__setattr__(name, value)

        def has_data(self):
            return self.ttl_expiration_pop.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.ttl_expiration_pop.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ipv6" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-mpls-lsd-cfg:mpls-lsd/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.ttl_expiration_pop.is_set or self.ttl_expiration_pop.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ttl_expiration_pop.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ttl-expiration-pop"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "ttl-expiration-pop"):
                self.ttl_expiration_pop = value
                self.ttl_expiration_pop.value_namespace = name_space
                self.ttl_expiration_pop.value_namespace_prefix = name_space_prefix


    class Ipv4(Entity):
        """
        Configure IPv4 parameters
        
        .. attribute:: ttl_expiration_pop
        
        	Number of labels to pop upon MPLS IP TTL expiry
        	**type**\:  int
        
        	**range:** 1..10
        
        

        """

        _prefix = 'mpls-lsd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(MplsLsd.Ipv4, self).__init__()

            self.yang_name = "ipv4"
            self.yang_parent_name = "mpls-lsd"

            self.ttl_expiration_pop = YLeaf(YType.uint32, "ttl-expiration-pop")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("ttl_expiration_pop") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(MplsLsd.Ipv4, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsLsd.Ipv4, self).__setattr__(name, value)

        def has_data(self):
            return self.ttl_expiration_pop.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.ttl_expiration_pop.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ipv4" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-mpls-lsd-cfg:mpls-lsd/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.ttl_expiration_pop.is_set or self.ttl_expiration_pop.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ttl_expiration_pop.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ttl-expiration-pop"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "ttl-expiration-pop"):
                self.ttl_expiration_pop = value
                self.ttl_expiration_pop.value_namespace = name_space
                self.ttl_expiration_pop.value_namespace_prefix = name_space_prefix


    class LabelDatabases(Entity):
        """
        Table of label databases
        
        .. attribute:: label_database
        
        	A label database
        	**type**\: list of    :py:class:`LabelDatabase <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_lsd_cfg.MplsLsd.LabelDatabases.LabelDatabase>`
        
        

        """

        _prefix = 'mpls-lsd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(MplsLsd.LabelDatabases, self).__init__()

            self.yang_name = "label-databases"
            self.yang_parent_name = "mpls-lsd"

            self.label_database = YList(self)

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
                        super(MplsLsd.LabelDatabases, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsLsd.LabelDatabases, self).__setattr__(name, value)


        class LabelDatabase(Entity):
            """
            A label database
            
            .. attribute:: label_database_id  <key>
            
            	Label database identifier
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: label_range
            
            	Label range
            	**type**\:   :py:class:`LabelRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_lsd_cfg.MplsLsd.LabelDatabases.LabelDatabase.LabelRange>`
            
            

            """

            _prefix = 'mpls-lsd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsLsd.LabelDatabases.LabelDatabase, self).__init__()

                self.yang_name = "label-database"
                self.yang_parent_name = "label-databases"

                self.label_database_id = YLeaf(YType.uint32, "label-database-id")

                self.label_range = MplsLsd.LabelDatabases.LabelDatabase.LabelRange()
                self.label_range.parent = self
                self._children_name_map["label_range"] = "label-range"
                self._children_yang_names.add("label-range")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("label_database_id") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsLsd.LabelDatabases.LabelDatabase, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsLsd.LabelDatabases.LabelDatabase, self).__setattr__(name, value)


            class LabelRange(Entity):
                """
                Label range
                
                .. attribute:: max_static_value
                
                	Maximum static label value
                	**type**\:  int
                
                	**range:** 0..1048575
                
                .. attribute:: max_value
                
                	Maximum label value
                	**type**\:  int
                
                	**range:** 16000..1048575
                
                .. attribute:: min_static_value
                
                	Minimum static label value
                	**type**\:  int
                
                	**range:** 0..1048575
                
                .. attribute:: minvalue
                
                	Minimum label value
                	**type**\:  int
                
                	**range:** 16000..1048575
                
                

                """

                _prefix = 'mpls-lsd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsLsd.LabelDatabases.LabelDatabase.LabelRange, self).__init__()

                    self.yang_name = "label-range"
                    self.yang_parent_name = "label-database"

                    self.max_static_value = YLeaf(YType.uint32, "max-static-value")

                    self.max_value = YLeaf(YType.uint32, "max-value")

                    self.min_static_value = YLeaf(YType.uint32, "min-static-value")

                    self.minvalue = YLeaf(YType.uint32, "minvalue")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("max_static_value",
                                    "max_value",
                                    "min_static_value",
                                    "minvalue") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsLsd.LabelDatabases.LabelDatabase.LabelRange, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsLsd.LabelDatabases.LabelDatabase.LabelRange, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.max_static_value.is_set or
                        self.max_value.is_set or
                        self.min_static_value.is_set or
                        self.minvalue.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.max_static_value.yfilter != YFilter.not_set or
                        self.max_value.yfilter != YFilter.not_set or
                        self.min_static_value.yfilter != YFilter.not_set or
                        self.minvalue.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "label-range" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.max_static_value.is_set or self.max_static_value.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.max_static_value.get_name_leafdata())
                    if (self.max_value.is_set or self.max_value.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.max_value.get_name_leafdata())
                    if (self.min_static_value.is_set or self.min_static_value.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.min_static_value.get_name_leafdata())
                    if (self.minvalue.is_set or self.minvalue.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.minvalue.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "max-static-value" or name == "max-value" or name == "min-static-value" or name == "minvalue"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "max-static-value"):
                        self.max_static_value = value
                        self.max_static_value.value_namespace = name_space
                        self.max_static_value.value_namespace_prefix = name_space_prefix
                    if(value_path == "max-value"):
                        self.max_value = value
                        self.max_value.value_namespace = name_space
                        self.max_value.value_namespace_prefix = name_space_prefix
                    if(value_path == "min-static-value"):
                        self.min_static_value = value
                        self.min_static_value.value_namespace = name_space
                        self.min_static_value.value_namespace_prefix = name_space_prefix
                    if(value_path == "minvalue"):
                        self.minvalue = value
                        self.minvalue.value_namespace = name_space
                        self.minvalue.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.label_database_id.is_set or
                    (self.label_range is not None and self.label_range.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.label_database_id.yfilter != YFilter.not_set or
                    (self.label_range is not None and self.label_range.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "label-database" + "[label-database-id='" + self.label_database_id.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-mpls-lsd-cfg:mpls-lsd/label-databases/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.label_database_id.is_set or self.label_database_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.label_database_id.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "label-range"):
                    if (self.label_range is None):
                        self.label_range = MplsLsd.LabelDatabases.LabelDatabase.LabelRange()
                        self.label_range.parent = self
                        self._children_name_map["label_range"] = "label-range"
                    return self.label_range

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "label-range" or name == "label-database-id"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "label-database-id"):
                    self.label_database_id = value
                    self.label_database_id.value_namespace = name_space
                    self.label_database_id.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.label_database:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.label_database:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "label-databases" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-mpls-lsd-cfg:mpls-lsd/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "label-database"):
                for c in self.label_database:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = MplsLsd.LabelDatabases.LabelDatabase()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.label_database.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "label-database"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            self.app_reg_delay_disable.is_set or
            self.mpls_entropy_label.is_set or
            self.mpls_ip_ttl_propagate_disable.is_set or
            (self.ipv4 is not None and self.ipv4.has_data()) or
            (self.ipv6 is not None and self.ipv6.has_data()) or
            (self.label_databases is not None and self.label_databases.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.app_reg_delay_disable.yfilter != YFilter.not_set or
            self.mpls_entropy_label.yfilter != YFilter.not_set or
            self.mpls_ip_ttl_propagate_disable.yfilter != YFilter.not_set or
            (self.ipv4 is not None and self.ipv4.has_operation()) or
            (self.ipv6 is not None and self.ipv6.has_operation()) or
            (self.label_databases is not None and self.label_databases.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-mpls-lsd-cfg:mpls-lsd" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.app_reg_delay_disable.is_set or self.app_reg_delay_disable.yfilter != YFilter.not_set):
            leaf_name_data.append(self.app_reg_delay_disable.get_name_leafdata())
        if (self.mpls_entropy_label.is_set or self.mpls_entropy_label.yfilter != YFilter.not_set):
            leaf_name_data.append(self.mpls_entropy_label.get_name_leafdata())
        if (self.mpls_ip_ttl_propagate_disable.is_set or self.mpls_ip_ttl_propagate_disable.yfilter != YFilter.not_set):
            leaf_name_data.append(self.mpls_ip_ttl_propagate_disable.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "ipv4"):
            if (self.ipv4 is None):
                self.ipv4 = MplsLsd.Ipv4()
                self.ipv4.parent = self
                self._children_name_map["ipv4"] = "ipv4"
            return self.ipv4

        if (child_yang_name == "ipv6"):
            if (self.ipv6 is None):
                self.ipv6 = MplsLsd.Ipv6()
                self.ipv6.parent = self
                self._children_name_map["ipv6"] = "ipv6"
            return self.ipv6

        if (child_yang_name == "label-databases"):
            if (self.label_databases is None):
                self.label_databases = MplsLsd.LabelDatabases()
                self.label_databases.parent = self
                self._children_name_map["label_databases"] = "label-databases"
            return self.label_databases

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "ipv4" or name == "ipv6" or name == "label-databases" or name == "app-reg-delay-disable" or name == "mpls-entropy-label" or name == "mpls-ip-ttl-propagate-disable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "app-reg-delay-disable"):
            self.app_reg_delay_disable = value
            self.app_reg_delay_disable.value_namespace = name_space
            self.app_reg_delay_disable.value_namespace_prefix = name_space_prefix
        if(value_path == "mpls-entropy-label"):
            self.mpls_entropy_label = value
            self.mpls_entropy_label.value_namespace = name_space
            self.mpls_entropy_label.value_namespace_prefix = name_space_prefix
        if(value_path == "mpls-ip-ttl-propagate-disable"):
            self.mpls_ip_ttl_propagate_disable = value
            self.mpls_ip_ttl_propagate_disable.value_namespace = name_space
            self.mpls_ip_ttl_propagate_disable.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = MplsLsd()
        return self._top_entity


""" Cisco_IOS_XR_ip_bfd_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-bfd package configuration.

This module contains definitions
for the following management objects\:
  bfd\: BFD Configuration

This YANG module augments the
  Cisco\-IOS\-XR\-snmp\-agent\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class BfdBundleCoexistenceBobBlb(Enum):
    """
    BfdBundleCoexistenceBobBlb

    Bfd bundle coexistence bob blb

    .. data:: inherited = 1

    	Inherited coexistence mode

    .. data:: logical = 2

    	Logical coexistence mode

    """

    inherited = Enum.YLeaf(1, "inherited")

    logical = Enum.YLeaf(2, "logical")


class BfdEchoStartupValidate(Enum):
    """
    BfdEchoStartupValidate

    Bfd echo startup validate

    .. data:: off = 0

    	Disable echo startup validation

    .. data:: on = 1

    	Enable echo startup validation

    .. data:: force = 2

    	Force echo startup validation

    """

    off = Enum.YLeaf(0, "off")

    on = Enum.YLeaf(1, "on")

    force = Enum.YLeaf(2, "force")


class BfdIfEchoUsage(Enum):
    """
    BfdIfEchoUsage

    Bfd if echo usage

    .. data:: enable = 0

    	Enable echo

    .. data:: disable = 1

    	Disable echo

    """

    enable = Enum.YLeaf(0, "enable")

    disable = Enum.YLeaf(1, "disable")


class BfdIfIpv6ChecksumUsage(Enum):
    """
    BfdIfIpv6ChecksumUsage

    Bfd if ipv6 checksum usage

    .. data:: disable = 0

    	Disable IPv6 checksum

    .. data:: enable = 1

    	Enable IPv6 checksum

    """

    disable = Enum.YLeaf(0, "disable")

    enable = Enum.YLeaf(1, "enable")



class Bfd(Entity):
    """
    BFD Configuration
    
    .. attribute:: bundle
    
    	Configuration related to BFD over Bundle
    	**type**\:   :py:class:`Bundle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg.Bfd.Bundle>`
    
    .. attribute:: echo_latency
    
    	BFD echo latency feature class container
    	**type**\:   :py:class:`EchoLatency <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg.Bfd.EchoLatency>`
    
    .. attribute:: echo_startup
    
    	BFD echo startup feature class container
    	**type**\:   :py:class:`EchoStartup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg.Bfd.EchoStartup>`
    
    .. attribute:: flap_damp
    
    	Flapping class container
    	**type**\:   :py:class:`FlapDamp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg.Bfd.FlapDamp>`
    
    .. attribute:: global_echo_min_interval
    
    	Configure echo min\-interval for bundle interface
    	**type**\:  int
    
    	**range:** 15..2000
    
    	**units**\: millisecond
    
    	**default value**\: 15
    
    .. attribute:: global_echo_usage
    
    	Echo configuration
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: global_ipv4_echo_source
    
    	IPv4 echo source address configuration
    	**type**\: one of the below types:
    
    	**type**\:  str
    
    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
    
    
    ----
    	**type**\:  str
    
    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
    
    
    ----
    .. attribute:: interfaces
    
    	Interface configuration
    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg.Bfd.Interfaces>`
    
    .. attribute:: ipv6_checksum_disable
    
    	To disable IPv6 checksum configuration
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: multi_path_includes
    
    	Multipath Include configuration
    	**type**\:   :py:class:`MultiPathIncludes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg.Bfd.MultiPathIncludes>`
    
    .. attribute:: single_hop_trap
    
    	Single hop trap configuration
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: ttl_drop_threshold
    
    	Multihop TTL Drop Threshold
    	**type**\:  int
    
    	**range:** 0..254
    
    

    """

    _prefix = 'ip-bfd-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Bfd, self).__init__()
        self._top_entity = None

        self.yang_name = "bfd"
        self.yang_parent_name = "Cisco-IOS-XR-ip-bfd-cfg"

        self.global_echo_min_interval = YLeaf(YType.uint32, "global-echo-min-interval")

        self.global_echo_usage = YLeaf(YType.empty, "global-echo-usage")

        self.global_ipv4_echo_source = YLeaf(YType.str, "global-ipv4-echo-source")

        self.ipv6_checksum_disable = YLeaf(YType.empty, "ipv6-checksum-disable")

        self.single_hop_trap = YLeaf(YType.empty, "single-hop-trap")

        self.ttl_drop_threshold = YLeaf(YType.uint32, "ttl-drop-threshold")

        self.bundle = Bfd.Bundle()
        self.bundle.parent = self
        self._children_name_map["bundle"] = "bundle"
        self._children_yang_names.add("bundle")

        self.echo_latency = Bfd.EchoLatency()
        self.echo_latency.parent = self
        self._children_name_map["echo_latency"] = "echo-latency"
        self._children_yang_names.add("echo-latency")

        self.echo_startup = Bfd.EchoStartup()
        self.echo_startup.parent = self
        self._children_name_map["echo_startup"] = "echo-startup"
        self._children_yang_names.add("echo-startup")

        self.flap_damp = Bfd.FlapDamp()
        self.flap_damp.parent = self
        self._children_name_map["flap_damp"] = "flap-damp"
        self._children_yang_names.add("flap-damp")

        self.interfaces = Bfd.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._children_yang_names.add("interfaces")

        self.multi_path_includes = Bfd.MultiPathIncludes()
        self.multi_path_includes.parent = self
        self._children_name_map["multi_path_includes"] = "multi-path-includes"
        self._children_yang_names.add("multi-path-includes")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("global_echo_min_interval",
                        "global_echo_usage",
                        "global_ipv4_echo_source",
                        "ipv6_checksum_disable",
                        "single_hop_trap",
                        "ttl_drop_threshold") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(Bfd, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Bfd, self).__setattr__(name, value)


    class FlapDamp(Entity):
        """
        Flapping class container
        
        .. attribute:: bundle_member
        
        	Bundle per member feature class container
        	**type**\:   :py:class:`BundleMember <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg.Bfd.FlapDamp.BundleMember>`
        
        .. attribute:: dampen_disable
        
        	Dampening Enable/Disable
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: extensions
        
        	Extensions to the BFD dampening feature
        	**type**\:   :py:class:`Extensions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg.Bfd.FlapDamp.Extensions>`
        
        .. attribute:: initial_delay
        
        	Initial delay before bringing up session
        	**type**\:  int
        
        	**range:** 1..3600000
        
        	**units**\: millisecond
        
        	**default value**\: 2000
        
        .. attribute:: maximum_delay
        
        	Maximum delay before bringing up session
        	**type**\:  int
        
        	**range:** 1..3600000
        
        	**units**\: millisecond
        
        	**default value**\: 120000
        
        .. attribute:: secondary_delay
        
        	Secondary delay before bringing up session
        	**type**\:  int
        
        	**range:** 1..3600000
        
        	**units**\: millisecond
        
        	**default value**\: 5000
        
        .. attribute:: threshold
        
        	Stability threshold to enable dampening
        	**type**\:  int
        
        	**range:** 60000..3600000
        
        	**units**\: millisecond
        
        	**default value**\: 120000
        
        

        """

        _prefix = 'ip-bfd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Bfd.FlapDamp, self).__init__()

            self.yang_name = "flap-damp"
            self.yang_parent_name = "bfd"

            self.dampen_disable = YLeaf(YType.empty, "dampen-disable")

            self.initial_delay = YLeaf(YType.uint32, "initial-delay")

            self.maximum_delay = YLeaf(YType.uint32, "maximum-delay")

            self.secondary_delay = YLeaf(YType.uint32, "secondary-delay")

            self.threshold = YLeaf(YType.uint32, "threshold")

            self.bundle_member = Bfd.FlapDamp.BundleMember()
            self.bundle_member.parent = self
            self._children_name_map["bundle_member"] = "bundle-member"
            self._children_yang_names.add("bundle-member")

            self.extensions = Bfd.FlapDamp.Extensions()
            self.extensions.parent = self
            self._children_name_map["extensions"] = "extensions"
            self._children_yang_names.add("extensions")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("dampen_disable",
                            "initial_delay",
                            "maximum_delay",
                            "secondary_delay",
                            "threshold") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Bfd.FlapDamp, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Bfd.FlapDamp, self).__setattr__(name, value)


        class BundleMember(Entity):
            """
            Bundle per member feature class container
            
            .. attribute:: initial_delay
            
            	Initial delay before bringing up session
            	**type**\:  int
            
            	**range:** 1..518400000
            
            	**units**\: millisecond
            
            	**default value**\: 16000
            
            .. attribute:: l3_only_mode
            
            	Apply immediate dampening and only when failure is L3 specific
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: maximum_delay
            
            	Maximum delay before bringing up session
            	**type**\:  int
            
            	**range:** 1..518400000
            
            	**units**\: millisecond
            
            	**default value**\: 600000
            
            .. attribute:: secondary_delay
            
            	Secondary delay before bringing up session
            	**type**\:  int
            
            	**range:** 1..518400000
            
            	**units**\: millisecond
            
            	**default value**\: 20000
            
            

            """

            _prefix = 'ip-bfd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Bfd.FlapDamp.BundleMember, self).__init__()

                self.yang_name = "bundle-member"
                self.yang_parent_name = "flap-damp"

                self.initial_delay = YLeaf(YType.uint32, "initial-delay")

                self.l3_only_mode = YLeaf(YType.empty, "l3-only-mode")

                self.maximum_delay = YLeaf(YType.uint32, "maximum-delay")

                self.secondary_delay = YLeaf(YType.uint32, "secondary-delay")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("initial_delay",
                                "l3_only_mode",
                                "maximum_delay",
                                "secondary_delay") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Bfd.FlapDamp.BundleMember, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Bfd.FlapDamp.BundleMember, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.initial_delay.is_set or
                    self.l3_only_mode.is_set or
                    self.maximum_delay.is_set or
                    self.secondary_delay.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.initial_delay.yfilter != YFilter.not_set or
                    self.l3_only_mode.yfilter != YFilter.not_set or
                    self.maximum_delay.yfilter != YFilter.not_set or
                    self.secondary_delay.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "bundle-member" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-bfd-cfg:bfd/flap-damp/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.initial_delay.is_set or self.initial_delay.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.initial_delay.get_name_leafdata())
                if (self.l3_only_mode.is_set or self.l3_only_mode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.l3_only_mode.get_name_leafdata())
                if (self.maximum_delay.is_set or self.maximum_delay.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.maximum_delay.get_name_leafdata())
                if (self.secondary_delay.is_set or self.secondary_delay.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.secondary_delay.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "initial-delay" or name == "l3-only-mode" or name == "maximum-delay" or name == "secondary-delay"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "initial-delay"):
                    self.initial_delay = value
                    self.initial_delay.value_namespace = name_space
                    self.initial_delay.value_namespace_prefix = name_space_prefix
                if(value_path == "l3-only-mode"):
                    self.l3_only_mode = value
                    self.l3_only_mode.value_namespace = name_space
                    self.l3_only_mode.value_namespace_prefix = name_space_prefix
                if(value_path == "maximum-delay"):
                    self.maximum_delay = value
                    self.maximum_delay.value_namespace = name_space
                    self.maximum_delay.value_namespace_prefix = name_space_prefix
                if(value_path == "secondary-delay"):
                    self.secondary_delay = value
                    self.secondary_delay.value_namespace = name_space
                    self.secondary_delay.value_namespace_prefix = name_space_prefix


        class Extensions(Entity):
            """
            Extensions to the BFD dampening feature
            
            .. attribute:: down_monitor
            
            	If set, DOWN state monitoring mode is enabled
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ip-bfd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Bfd.FlapDamp.Extensions, self).__init__()

                self.yang_name = "extensions"
                self.yang_parent_name = "flap-damp"

                self.down_monitor = YLeaf(YType.empty, "down-monitor")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("down_monitor") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Bfd.FlapDamp.Extensions, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Bfd.FlapDamp.Extensions, self).__setattr__(name, value)

            def has_data(self):
                return self.down_monitor.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.down_monitor.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "extensions" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-bfd-cfg:bfd/flap-damp/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.down_monitor.is_set or self.down_monitor.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.down_monitor.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "down-monitor"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "down-monitor"):
                    self.down_monitor = value
                    self.down_monitor.value_namespace = name_space
                    self.down_monitor.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                self.dampen_disable.is_set or
                self.initial_delay.is_set or
                self.maximum_delay.is_set or
                self.secondary_delay.is_set or
                self.threshold.is_set or
                (self.bundle_member is not None and self.bundle_member.has_data()) or
                (self.extensions is not None and self.extensions.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.dampen_disable.yfilter != YFilter.not_set or
                self.initial_delay.yfilter != YFilter.not_set or
                self.maximum_delay.yfilter != YFilter.not_set or
                self.secondary_delay.yfilter != YFilter.not_set or
                self.threshold.yfilter != YFilter.not_set or
                (self.bundle_member is not None and self.bundle_member.has_operation()) or
                (self.extensions is not None and self.extensions.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "flap-damp" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-bfd-cfg:bfd/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.dampen_disable.is_set or self.dampen_disable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dampen_disable.get_name_leafdata())
            if (self.initial_delay.is_set or self.initial_delay.yfilter != YFilter.not_set):
                leaf_name_data.append(self.initial_delay.get_name_leafdata())
            if (self.maximum_delay.is_set or self.maximum_delay.yfilter != YFilter.not_set):
                leaf_name_data.append(self.maximum_delay.get_name_leafdata())
            if (self.secondary_delay.is_set or self.secondary_delay.yfilter != YFilter.not_set):
                leaf_name_data.append(self.secondary_delay.get_name_leafdata())
            if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                leaf_name_data.append(self.threshold.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "bundle-member"):
                if (self.bundle_member is None):
                    self.bundle_member = Bfd.FlapDamp.BundleMember()
                    self.bundle_member.parent = self
                    self._children_name_map["bundle_member"] = "bundle-member"
                return self.bundle_member

            if (child_yang_name == "extensions"):
                if (self.extensions is None):
                    self.extensions = Bfd.FlapDamp.Extensions()
                    self.extensions.parent = self
                    self._children_name_map["extensions"] = "extensions"
                return self.extensions

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "bundle-member" or name == "extensions" or name == "dampen-disable" or name == "initial-delay" or name == "maximum-delay" or name == "secondary-delay" or name == "threshold"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "dampen-disable"):
                self.dampen_disable = value
                self.dampen_disable.value_namespace = name_space
                self.dampen_disable.value_namespace_prefix = name_space_prefix
            if(value_path == "initial-delay"):
                self.initial_delay = value
                self.initial_delay.value_namespace = name_space
                self.initial_delay.value_namespace_prefix = name_space_prefix
            if(value_path == "maximum-delay"):
                self.maximum_delay = value
                self.maximum_delay.value_namespace = name_space
                self.maximum_delay.value_namespace_prefix = name_space_prefix
            if(value_path == "secondary-delay"):
                self.secondary_delay = value
                self.secondary_delay.value_namespace = name_space
                self.secondary_delay.value_namespace_prefix = name_space_prefix
            if(value_path == "threshold"):
                self.threshold = value
                self.threshold.value_namespace = name_space
                self.threshold.value_namespace_prefix = name_space_prefix


    class EchoLatency(Entity):
        """
        BFD echo latency feature class container
        
        .. attribute:: detect
        
        	BFD echo latency detection
        	**type**\:   :py:class:`Detect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg.Bfd.EchoLatency.Detect>`
        
        

        """

        _prefix = 'ip-bfd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Bfd.EchoLatency, self).__init__()

            self.yang_name = "echo-latency"
            self.yang_parent_name = "bfd"

            self.detect = Bfd.EchoLatency.Detect()
            self.detect.parent = self
            self._children_name_map["detect"] = "detect"
            self._children_yang_names.add("detect")


        class Detect(Entity):
            """
            BFD echo latency detection
            
            .. attribute:: latency_detect_count
            
            	Echo latency detect count
            	**type**\:  int
            
            	**range:** 1..10
            
            	**default value**\: 1
            
            .. attribute:: latency_detect_enabled
            
            	If set, echo latency detect is enabled
            	**type**\:  bool
            
            	**default value**\: false
            
            .. attribute:: latency_detect_percentage
            
            	Echo latency detect percentage
            	**type**\:  int
            
            	**range:** 100..250
            
            	**units**\: percentage
            
            	**default value**\: 100
            
            

            """

            _prefix = 'ip-bfd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Bfd.EchoLatency.Detect, self).__init__()

                self.yang_name = "detect"
                self.yang_parent_name = "echo-latency"

                self.latency_detect_count = YLeaf(YType.uint32, "latency-detect-count")

                self.latency_detect_enabled = YLeaf(YType.boolean, "latency-detect-enabled")

                self.latency_detect_percentage = YLeaf(YType.uint32, "latency-detect-percentage")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("latency_detect_count",
                                "latency_detect_enabled",
                                "latency_detect_percentage") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Bfd.EchoLatency.Detect, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Bfd.EchoLatency.Detect, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.latency_detect_count.is_set or
                    self.latency_detect_enabled.is_set or
                    self.latency_detect_percentage.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.latency_detect_count.yfilter != YFilter.not_set or
                    self.latency_detect_enabled.yfilter != YFilter.not_set or
                    self.latency_detect_percentage.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "detect" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-bfd-cfg:bfd/echo-latency/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.latency_detect_count.is_set or self.latency_detect_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.latency_detect_count.get_name_leafdata())
                if (self.latency_detect_enabled.is_set or self.latency_detect_enabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.latency_detect_enabled.get_name_leafdata())
                if (self.latency_detect_percentage.is_set or self.latency_detect_percentage.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.latency_detect_percentage.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "latency-detect-count" or name == "latency-detect-enabled" or name == "latency-detect-percentage"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "latency-detect-count"):
                    self.latency_detect_count = value
                    self.latency_detect_count.value_namespace = name_space
                    self.latency_detect_count.value_namespace_prefix = name_space_prefix
                if(value_path == "latency-detect-enabled"):
                    self.latency_detect_enabled = value
                    self.latency_detect_enabled.value_namespace = name_space
                    self.latency_detect_enabled.value_namespace_prefix = name_space_prefix
                if(value_path == "latency-detect-percentage"):
                    self.latency_detect_percentage = value
                    self.latency_detect_percentage.value_namespace = name_space
                    self.latency_detect_percentage.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (self.detect is not None and self.detect.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.detect is not None and self.detect.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "echo-latency" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-bfd-cfg:bfd/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "detect"):
                if (self.detect is None):
                    self.detect = Bfd.EchoLatency.Detect()
                    self.detect.parent = self
                    self._children_name_map["detect"] = "detect"
                return self.detect

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "detect"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class EchoStartup(Entity):
        """
        BFD echo startup feature class container
        
        .. attribute:: validate
        
        	BFD echo validation prior to session bringup
        	**type**\:   :py:class:`BfdEchoStartupValidate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg.BfdEchoStartupValidate>`
        
        	**default value**\: off
        
        

        """

        _prefix = 'ip-bfd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Bfd.EchoStartup, self).__init__()

            self.yang_name = "echo-startup"
            self.yang_parent_name = "bfd"

            self.validate = YLeaf(YType.enumeration, "validate")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("validate") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Bfd.EchoStartup, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Bfd.EchoStartup, self).__setattr__(name, value)

        def has_data(self):
            return self.validate.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.validate.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "echo-startup" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-bfd-cfg:bfd/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.validate.is_set or self.validate.yfilter != YFilter.not_set):
                leaf_name_data.append(self.validate.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "validate"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "validate"):
                self.validate = value
                self.validate.value_namespace = name_space
                self.validate.value_namespace_prefix = name_space_prefix


    class Interfaces(Entity):
        """
        Interface configuration
        
        .. attribute:: interface
        
        	Single interface configuration
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg.Bfd.Interfaces.Interface>`
        
        

        """

        _prefix = 'ip-bfd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Bfd.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "bfd"

            self.interface = YList(self)

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
                        super(Bfd.Interfaces, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Bfd.Interfaces, self).__setattr__(name, value)


        class Interface(Entity):
            """
            Single interface configuration
            
            .. attribute:: interface_name  <key>
            
            	Interface Name
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: interface_echo_usage
            
            	Echo usage for this interface
            	**type**\:   :py:class:`BfdIfEchoUsage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg.BfdIfEchoUsage>`
            
            	**default value**\: enable
            
            .. attribute:: interface_ipv4_echo_source
            
            	Interface IPv4 echo source address configuration
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: ipv6_checksum
            
            	IPv6 checksum usage for this interface \- Interface config will always take precedence over global config
            	**type**\:   :py:class:`BfdIfIpv6ChecksumUsage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg.BfdIfIpv6ChecksumUsage>`
            
            	**default value**\: enable
            
            

            """

            _prefix = 'ip-bfd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Bfd.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.interface_echo_usage = YLeaf(YType.enumeration, "interface-echo-usage")

                self.interface_ipv4_echo_source = YLeaf(YType.str, "interface-ipv4-echo-source")

                self.ipv6_checksum = YLeaf(YType.enumeration, "ipv6-checksum")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("interface_name",
                                "interface_echo_usage",
                                "interface_ipv4_echo_source",
                                "ipv6_checksum") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Bfd.Interfaces.Interface, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Bfd.Interfaces.Interface, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.interface_name.is_set or
                    self.interface_echo_usage.is_set or
                    self.interface_ipv4_echo_source.is_set or
                    self.ipv6_checksum.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.interface_name.yfilter != YFilter.not_set or
                    self.interface_echo_usage.yfilter != YFilter.not_set or
                    self.interface_ipv4_echo_source.yfilter != YFilter.not_set or
                    self.ipv6_checksum.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-bfd-cfg:bfd/interfaces/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface_name.get_name_leafdata())
                if (self.interface_echo_usage.is_set or self.interface_echo_usage.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface_echo_usage.get_name_leafdata())
                if (self.interface_ipv4_echo_source.is_set or self.interface_ipv4_echo_source.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface_ipv4_echo_source.get_name_leafdata())
                if (self.ipv6_checksum.is_set or self.ipv6_checksum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipv6_checksum.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "interface-name" or name == "interface-echo-usage" or name == "interface-ipv4-echo-source" or name == "ipv6-checksum"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "interface-name"):
                    self.interface_name = value
                    self.interface_name.value_namespace = name_space
                    self.interface_name.value_namespace_prefix = name_space_prefix
                if(value_path == "interface-echo-usage"):
                    self.interface_echo_usage = value
                    self.interface_echo_usage.value_namespace = name_space
                    self.interface_echo_usage.value_namespace_prefix = name_space_prefix
                if(value_path == "interface-ipv4-echo-source"):
                    self.interface_ipv4_echo_source = value
                    self.interface_ipv4_echo_source.value_namespace = name_space
                    self.interface_ipv4_echo_source.value_namespace_prefix = name_space_prefix
                if(value_path == "ipv6-checksum"):
                    self.ipv6_checksum = value
                    self.ipv6_checksum.value_namespace = name_space
                    self.ipv6_checksum.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.interface:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.interface:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "interfaces" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-bfd-cfg:bfd/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "interface"):
                for c in self.interface:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Bfd.Interfaces.Interface()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.interface.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "interface"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class MultiPathIncludes(Entity):
        """
        Multipath Include configuration
        
        .. attribute:: multi_path_include
        
        	Location configuration
        	**type**\: list of    :py:class:`MultiPathInclude <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg.Bfd.MultiPathIncludes.MultiPathInclude>`
        
        

        """

        _prefix = 'ip-bfd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Bfd.MultiPathIncludes, self).__init__()

            self.yang_name = "multi-path-includes"
            self.yang_parent_name = "bfd"

            self.multi_path_include = YList(self)

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
                        super(Bfd.MultiPathIncludes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Bfd.MultiPathIncludes, self).__setattr__(name, value)


        class MultiPathInclude(Entity):
            """
            Location configuration
            
            .. attribute:: location  <key>
            
            	Location
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            

            """

            _prefix = 'ip-bfd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Bfd.MultiPathIncludes.MultiPathInclude, self).__init__()

                self.yang_name = "multi-path-include"
                self.yang_parent_name = "multi-path-includes"

                self.location = YLeaf(YType.str, "location")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("location") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Bfd.MultiPathIncludes.MultiPathInclude, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Bfd.MultiPathIncludes.MultiPathInclude, self).__setattr__(name, value)

            def has_data(self):
                return self.location.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.location.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "multi-path-include" + "[location='" + self.location.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-bfd-cfg:bfd/multi-path-includes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.location.is_set or self.location.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.location.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "location"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "location"):
                    self.location = value
                    self.location.value_namespace = name_space
                    self.location.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.multi_path_include:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.multi_path_include:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "multi-path-includes" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-bfd-cfg:bfd/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "multi-path-include"):
                for c in self.multi_path_include:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Bfd.MultiPathIncludes.MultiPathInclude()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.multi_path_include.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "multi-path-include"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Bundle(Entity):
        """
        Configuration related to BFD over Bundle
        
        .. attribute:: coexistence
        
        	Coexistence mode for BFD on bundle feature
        	**type**\:   :py:class:`Coexistence <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg.Bfd.Bundle.Coexistence>`
        
        

        """

        _prefix = 'ip-bfd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Bfd.Bundle, self).__init__()

            self.yang_name = "bundle"
            self.yang_parent_name = "bfd"

            self.coexistence = Bfd.Bundle.Coexistence()
            self.coexistence.parent = self
            self._children_name_map["coexistence"] = "coexistence"
            self._children_yang_names.add("coexistence")


        class Coexistence(Entity):
            """
            Coexistence mode for BFD on bundle feature
            
            .. attribute:: bob_blb
            
            	Coexistence mode for BoB and BLB feature
            	**type**\:   :py:class:`BfdBundleCoexistenceBobBlb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg.BfdBundleCoexistenceBobBlb>`
            
            

            """

            _prefix = 'ip-bfd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Bfd.Bundle.Coexistence, self).__init__()

                self.yang_name = "coexistence"
                self.yang_parent_name = "bundle"

                self.bob_blb = YLeaf(YType.enumeration, "bob-blb")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("bob_blb") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Bfd.Bundle.Coexistence, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Bfd.Bundle.Coexistence, self).__setattr__(name, value)

            def has_data(self):
                return self.bob_blb.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.bob_blb.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "coexistence" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-bfd-cfg:bfd/bundle/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.bob_blb.is_set or self.bob_blb.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bob_blb.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "bob-blb"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "bob-blb"):
                    self.bob_blb = value
                    self.bob_blb.value_namespace = name_space
                    self.bob_blb.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (self.coexistence is not None and self.coexistence.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.coexistence is not None and self.coexistence.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "bundle" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-bfd-cfg:bfd/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "coexistence"):
                if (self.coexistence is None):
                    self.coexistence = Bfd.Bundle.Coexistence()
                    self.coexistence.parent = self
                    self._children_name_map["coexistence"] = "coexistence"
                return self.coexistence

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "coexistence"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            self.global_echo_min_interval.is_set or
            self.global_echo_usage.is_set or
            self.global_ipv4_echo_source.is_set or
            self.ipv6_checksum_disable.is_set or
            self.single_hop_trap.is_set or
            self.ttl_drop_threshold.is_set or
            (self.bundle is not None and self.bundle.has_data()) or
            (self.echo_latency is not None and self.echo_latency.has_data()) or
            (self.echo_startup is not None and self.echo_startup.has_data()) or
            (self.flap_damp is not None and self.flap_damp.has_data()) or
            (self.interfaces is not None and self.interfaces.has_data()) or
            (self.multi_path_includes is not None and self.multi_path_includes.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.global_echo_min_interval.yfilter != YFilter.not_set or
            self.global_echo_usage.yfilter != YFilter.not_set or
            self.global_ipv4_echo_source.yfilter != YFilter.not_set or
            self.ipv6_checksum_disable.yfilter != YFilter.not_set or
            self.single_hop_trap.yfilter != YFilter.not_set or
            self.ttl_drop_threshold.yfilter != YFilter.not_set or
            (self.bundle is not None and self.bundle.has_operation()) or
            (self.echo_latency is not None and self.echo_latency.has_operation()) or
            (self.echo_startup is not None and self.echo_startup.has_operation()) or
            (self.flap_damp is not None and self.flap_damp.has_operation()) or
            (self.interfaces is not None and self.interfaces.has_operation()) or
            (self.multi_path_includes is not None and self.multi_path_includes.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ip-bfd-cfg:bfd" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.global_echo_min_interval.is_set or self.global_echo_min_interval.yfilter != YFilter.not_set):
            leaf_name_data.append(self.global_echo_min_interval.get_name_leafdata())
        if (self.global_echo_usage.is_set or self.global_echo_usage.yfilter != YFilter.not_set):
            leaf_name_data.append(self.global_echo_usage.get_name_leafdata())
        if (self.global_ipv4_echo_source.is_set or self.global_ipv4_echo_source.yfilter != YFilter.not_set):
            leaf_name_data.append(self.global_ipv4_echo_source.get_name_leafdata())
        if (self.ipv6_checksum_disable.is_set or self.ipv6_checksum_disable.yfilter != YFilter.not_set):
            leaf_name_data.append(self.ipv6_checksum_disable.get_name_leafdata())
        if (self.single_hop_trap.is_set or self.single_hop_trap.yfilter != YFilter.not_set):
            leaf_name_data.append(self.single_hop_trap.get_name_leafdata())
        if (self.ttl_drop_threshold.is_set or self.ttl_drop_threshold.yfilter != YFilter.not_set):
            leaf_name_data.append(self.ttl_drop_threshold.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "bundle"):
            if (self.bundle is None):
                self.bundle = Bfd.Bundle()
                self.bundle.parent = self
                self._children_name_map["bundle"] = "bundle"
            return self.bundle

        if (child_yang_name == "echo-latency"):
            if (self.echo_latency is None):
                self.echo_latency = Bfd.EchoLatency()
                self.echo_latency.parent = self
                self._children_name_map["echo_latency"] = "echo-latency"
            return self.echo_latency

        if (child_yang_name == "echo-startup"):
            if (self.echo_startup is None):
                self.echo_startup = Bfd.EchoStartup()
                self.echo_startup.parent = self
                self._children_name_map["echo_startup"] = "echo-startup"
            return self.echo_startup

        if (child_yang_name == "flap-damp"):
            if (self.flap_damp is None):
                self.flap_damp = Bfd.FlapDamp()
                self.flap_damp.parent = self
                self._children_name_map["flap_damp"] = "flap-damp"
            return self.flap_damp

        if (child_yang_name == "interfaces"):
            if (self.interfaces is None):
                self.interfaces = Bfd.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
            return self.interfaces

        if (child_yang_name == "multi-path-includes"):
            if (self.multi_path_includes is None):
                self.multi_path_includes = Bfd.MultiPathIncludes()
                self.multi_path_includes.parent = self
                self._children_name_map["multi_path_includes"] = "multi-path-includes"
            return self.multi_path_includes

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "bundle" or name == "echo-latency" or name == "echo-startup" or name == "flap-damp" or name == "interfaces" or name == "multi-path-includes" or name == "global-echo-min-interval" or name == "global-echo-usage" or name == "global-ipv4-echo-source" or name == "ipv6-checksum-disable" or name == "single-hop-trap" or name == "ttl-drop-threshold"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "global-echo-min-interval"):
            self.global_echo_min_interval = value
            self.global_echo_min_interval.value_namespace = name_space
            self.global_echo_min_interval.value_namespace_prefix = name_space_prefix
        if(value_path == "global-echo-usage"):
            self.global_echo_usage = value
            self.global_echo_usage.value_namespace = name_space
            self.global_echo_usage.value_namespace_prefix = name_space_prefix
        if(value_path == "global-ipv4-echo-source"):
            self.global_ipv4_echo_source = value
            self.global_ipv4_echo_source.value_namespace = name_space
            self.global_ipv4_echo_source.value_namespace_prefix = name_space_prefix
        if(value_path == "ipv6-checksum-disable"):
            self.ipv6_checksum_disable = value
            self.ipv6_checksum_disable.value_namespace = name_space
            self.ipv6_checksum_disable.value_namespace_prefix = name_space_prefix
        if(value_path == "single-hop-trap"):
            self.single_hop_trap = value
            self.single_hop_trap.value_namespace = name_space
            self.single_hop_trap.value_namespace_prefix = name_space_prefix
        if(value_path == "ttl-drop-threshold"):
            self.ttl_drop_threshold = value
            self.ttl_drop_threshold.value_namespace = name_space
            self.ttl_drop_threshold.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = Bfd()
        return self._top_entity


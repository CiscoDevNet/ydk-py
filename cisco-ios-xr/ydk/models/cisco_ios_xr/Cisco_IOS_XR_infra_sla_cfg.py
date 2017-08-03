""" Cisco_IOS_XR_infra_sla_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-sla package configuration.

This module contains definitions
for the following management objects\:
  sla\: SLA prtocol and profile Configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Sla(Entity):
    """
    SLA prtocol and profile Configuration
    
    .. attribute:: protocols
    
    	Table of all SLA protocols
    	**type**\:   :py:class:`Protocols <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg.Sla.Protocols>`
    
    

    """

    _prefix = 'infra-sla-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Sla, self).__init__()
        self._top_entity = None

        self.yang_name = "sla"
        self.yang_parent_name = "Cisco-IOS-XR-infra-sla-cfg"

        self.protocols = Sla.Protocols()
        self.protocols.parent = self
        self._children_name_map["protocols"] = "protocols"
        self._children_yang_names.add("protocols")


    class Protocols(Entity):
        """
        Table of all SLA protocols
        
        .. attribute:: ethernet
        
        	The Ethernet SLA protocol
        	**type**\:   :py:class:`Ethernet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg.Sla.Protocols.Ethernet>`
        
        

        """

        _prefix = 'infra-sla-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Sla.Protocols, self).__init__()

            self.yang_name = "protocols"
            self.yang_parent_name = "sla"

            self.ethernet = Sla.Protocols.Ethernet()
            self.ethernet.parent = self
            self._children_name_map["ethernet"] = "ethernet"
            self._children_yang_names.add("ethernet")


        class Ethernet(Entity):
            """
            The Ethernet SLA protocol
            
            .. attribute:: profiles
            
            	Table of SLA profiles on the protocol
            	**type**\:   :py:class:`Profiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg.Sla.Protocols.Ethernet.Profiles>`
            
            

            """

            _prefix = 'ethernet-cfm-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Sla.Protocols.Ethernet, self).__init__()

                self.yang_name = "ethernet"
                self.yang_parent_name = "protocols"

                self.profiles = Sla.Protocols.Ethernet.Profiles()
                self.profiles.parent = self
                self._children_name_map["profiles"] = "profiles"
                self._children_yang_names.add("profiles")


            class Profiles(Entity):
                """
                Table of SLA profiles on the protocol
                
                .. attribute:: profile
                
                	Name of the profile
                	**type**\: list of    :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg.Sla.Protocols.Ethernet.Profiles.Profile>`
                
                

                """

                _prefix = 'ethernet-cfm-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Sla.Protocols.Ethernet.Profiles, self).__init__()

                    self.yang_name = "profiles"
                    self.yang_parent_name = "ethernet"

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
                                super(Sla.Protocols.Ethernet.Profiles, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Sla.Protocols.Ethernet.Profiles, self).__setattr__(name, value)


                class Profile(Entity):
                    """
                    Name of the profile
                    
                    .. attribute:: profile_name  <key>
                    
                    	Profile name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: packet_type
                    
                    	The possible packet types are cfm\-loopback, cfm\-delay\-measurement, cfm\-delay\-measurement\-version\-0, cfm\-loss\-measurement and cfm\-synthetic\-loss\-measurement
                    	**type**\:  str
                    
                    .. attribute:: probe
                    
                    	Probe configuration for the SLA profile
                    	**type**\:   :py:class:`Probe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg.Sla.Protocols.Ethernet.Profiles.Profile.Probe>`
                    
                    .. attribute:: schedule
                    
                    	Schedule to use for probes within an operation
                    	**type**\:   :py:class:`Schedule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg.Sla.Protocols.Ethernet.Profiles.Profile.Schedule>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: statistics
                    
                    	Statistics configuration for the SLA profile
                    	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg.Sla.Protocols.Ethernet.Profiles.Profile.Statistics>`
                    
                    

                    """

                    _prefix = 'ethernet-cfm-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Sla.Protocols.Ethernet.Profiles.Profile, self).__init__()

                        self.yang_name = "profile"
                        self.yang_parent_name = "profiles"

                        self.profile_name = YLeaf(YType.str, "profile-name")

                        self.packet_type = YLeaf(YType.str, "packet-type")

                        self.probe = Sla.Protocols.Ethernet.Profiles.Profile.Probe()
                        self.probe.parent = self
                        self._children_name_map["probe"] = "probe"
                        self._children_yang_names.add("probe")

                        self.schedule = None
                        self._children_name_map["schedule"] = "schedule"
                        self._children_yang_names.add("schedule")

                        self.statistics = Sla.Protocols.Ethernet.Profiles.Profile.Statistics()
                        self.statistics.parent = self
                        self._children_name_map["statistics"] = "statistics"
                        self._children_yang_names.add("statistics")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("profile_name",
                                        "packet_type") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Sla.Protocols.Ethernet.Profiles.Profile, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Sla.Protocols.Ethernet.Profiles.Profile, self).__setattr__(name, value)


                    class Statistics(Entity):
                        """
                        Statistics configuration for the SLA profile
                        
                        .. attribute:: statistic
                        
                        	Type of statistic
                        	**type**\: list of    :py:class:`Statistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg.Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Sla.Protocols.Ethernet.Profiles.Profile.Statistics, self).__init__()

                            self.yang_name = "statistics"
                            self.yang_parent_name = "profile"

                            self.statistic = YList(self)

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
                                        super(Sla.Protocols.Ethernet.Profiles.Profile.Statistics, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Sla.Protocols.Ethernet.Profiles.Profile.Statistics, self).__setattr__(name, value)


                        class Statistic(Entity):
                            """
                            Type of statistic
                            
                            .. attribute:: statistic_name  <key>
                            
                            	The type of statistic to measure
                            	**type**\:   :py:class:`SlaStatisticTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes.SlaStatisticTypeEnum>`
                            
                            .. attribute:: aggregation
                            
                            	Aggregation to apply to results for the statistic
                            	**type**\:   :py:class:`Aggregation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg.Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic.Aggregation>`
                            
                            	**presence node**\: True
                            
                            .. attribute:: buckets_archive
                            
                            	Number of buckets to archive in memory
                            	**type**\:  int
                            
                            	**range:** 1..100
                            
                            .. attribute:: buckets_size
                            
                            	Size of the buckets into which statistics are collected
                            	**type**\:   :py:class:`BucketsSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg.Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic.BucketsSize>`
                            
                            	**presence node**\: True
                            
                            .. attribute:: enable
                            
                            	Enable statistic gathering of the metric
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'ethernet-cfm-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic, self).__init__()

                                self.yang_name = "statistic"
                                self.yang_parent_name = "statistics"

                                self.statistic_name = YLeaf(YType.enumeration, "statistic-name")

                                self.buckets_archive = YLeaf(YType.uint32, "buckets-archive")

                                self.enable = YLeaf(YType.empty, "enable")

                                self.aggregation = None
                                self._children_name_map["aggregation"] = "aggregation"
                                self._children_yang_names.add("aggregation")

                                self.buckets_size = None
                                self._children_name_map["buckets_size"] = "buckets-size"
                                self._children_yang_names.add("buckets-size")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("statistic_name",
                                                "buckets_archive",
                                                "enable") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic, self).__setattr__(name, value)


                            class BucketsSize(Entity):
                                """
                                Size of the buckets into which statistics
                                are collected
                                
                                .. attribute:: buckets_size
                                
                                	Size of each bucket
                                	**type**\:  int
                                
                                	**range:** 1..100
                                
                                	**mandatory**\: True
                                
                                .. attribute:: buckets_size_unit
                                
                                	Unit associated with the BucketsSize
                                	**type**\:   :py:class:`SlaBucketsSizeUnitsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes.SlaBucketsSizeUnitsEnum>`
                                
                                	**mandatory**\: True
                                
                                

                                This class is a :ref:`presence class<presence-class>`

                                """

                                _prefix = 'ethernet-cfm-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic.BucketsSize, self).__init__()

                                    self.yang_name = "buckets-size"
                                    self.yang_parent_name = "statistic"
                                    self.is_presence_container = True

                                    self.buckets_size = YLeaf(YType.uint32, "buckets-size")

                                    self.buckets_size_unit = YLeaf(YType.enumeration, "buckets-size-unit")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("buckets_size",
                                                    "buckets_size_unit") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic.BucketsSize, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic.BucketsSize, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.buckets_size.is_set or
                                        self.buckets_size_unit.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.buckets_size.yfilter != YFilter.not_set or
                                        self.buckets_size_unit.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "buckets-size" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.buckets_size.is_set or self.buckets_size.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.buckets_size.get_name_leafdata())
                                    if (self.buckets_size_unit.is_set or self.buckets_size_unit.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.buckets_size_unit.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "buckets-size" or name == "buckets-size-unit"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "buckets-size"):
                                        self.buckets_size = value
                                        self.buckets_size.value_namespace = name_space
                                        self.buckets_size.value_namespace_prefix = name_space_prefix
                                    if(value_path == "buckets-size-unit"):
                                        self.buckets_size_unit = value
                                        self.buckets_size_unit.value_namespace = name_space
                                        self.buckets_size_unit.value_namespace_prefix = name_space_prefix


                            class Aggregation(Entity):
                                """
                                Aggregation to apply to results for the
                                statistic
                                
                                .. attribute:: bins_count
                                
                                	Number of bins to aggregate results into (0 for no aggregation)
                                	**type**\:  int
                                
                                	**range:** 0..100
                                
                                	**mandatory**\: True
                                
                                .. attribute:: bins_width
                                
                                	Width of each bin
                                	**type**\:  int
                                
                                	**range:** 1..10000
                                
                                .. attribute:: bins_width_tenths
                                
                                	Tenths portion of the bin width
                                	**type**\:  int
                                
                                	**range:** 0..9
                                
                                

                                This class is a :ref:`presence class<presence-class>`

                                """

                                _prefix = 'ethernet-cfm-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic.Aggregation, self).__init__()

                                    self.yang_name = "aggregation"
                                    self.yang_parent_name = "statistic"
                                    self.is_presence_container = True

                                    self.bins_count = YLeaf(YType.uint32, "bins-count")

                                    self.bins_width = YLeaf(YType.uint32, "bins-width")

                                    self.bins_width_tenths = YLeaf(YType.uint32, "bins-width-tenths")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("bins_count",
                                                    "bins_width",
                                                    "bins_width_tenths") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic.Aggregation, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic.Aggregation, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.bins_count.is_set or
                                        self.bins_width.is_set or
                                        self.bins_width_tenths.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.bins_count.yfilter != YFilter.not_set or
                                        self.bins_width.yfilter != YFilter.not_set or
                                        self.bins_width_tenths.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "aggregation" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.bins_count.is_set or self.bins_count.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.bins_count.get_name_leafdata())
                                    if (self.bins_width.is_set or self.bins_width.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.bins_width.get_name_leafdata())
                                    if (self.bins_width_tenths.is_set or self.bins_width_tenths.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.bins_width_tenths.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "bins-count" or name == "bins-width" or name == "bins-width-tenths"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "bins-count"):
                                        self.bins_count = value
                                        self.bins_count.value_namespace = name_space
                                        self.bins_count.value_namespace_prefix = name_space_prefix
                                    if(value_path == "bins-width"):
                                        self.bins_width = value
                                        self.bins_width.value_namespace = name_space
                                        self.bins_width.value_namespace_prefix = name_space_prefix
                                    if(value_path == "bins-width-tenths"):
                                        self.bins_width_tenths = value
                                        self.bins_width_tenths.value_namespace = name_space
                                        self.bins_width_tenths.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.statistic_name.is_set or
                                    self.buckets_archive.is_set or
                                    self.enable.is_set or
                                    (self.aggregation is not None) or
                                    (self.buckets_size is not None))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.statistic_name.yfilter != YFilter.not_set or
                                    self.buckets_archive.yfilter != YFilter.not_set or
                                    self.enable.yfilter != YFilter.not_set or
                                    (self.aggregation is not None and self.aggregation.has_operation()) or
                                    (self.buckets_size is not None and self.buckets_size.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "statistic" + "[statistic-name='" + self.statistic_name.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.statistic_name.is_set or self.statistic_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.statistic_name.get_name_leafdata())
                                if (self.buckets_archive.is_set or self.buckets_archive.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.buckets_archive.get_name_leafdata())
                                if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.enable.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "aggregation"):
                                    if (self.aggregation is None):
                                        self.aggregation = Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic.Aggregation()
                                        self.aggregation.parent = self
                                        self._children_name_map["aggregation"] = "aggregation"
                                    return self.aggregation

                                if (child_yang_name == "buckets-size"):
                                    if (self.buckets_size is None):
                                        self.buckets_size = Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic.BucketsSize()
                                        self.buckets_size.parent = self
                                        self._children_name_map["buckets_size"] = "buckets-size"
                                    return self.buckets_size

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "aggregation" or name == "buckets-size" or name == "statistic-name" or name == "buckets-archive" or name == "enable"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "statistic-name"):
                                    self.statistic_name = value
                                    self.statistic_name.value_namespace = name_space
                                    self.statistic_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "buckets-archive"):
                                    self.buckets_archive = value
                                    self.buckets_archive.value_namespace = name_space
                                    self.buckets_archive.value_namespace_prefix = name_space_prefix
                                if(value_path == "enable"):
                                    self.enable = value
                                    self.enable.value_namespace = name_space
                                    self.enable.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.statistic:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.statistic:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "statistics" + path_buffer

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

                            if (child_yang_name == "statistic"):
                                for c in self.statistic:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.statistic.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "statistic"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class Schedule(Entity):
                        """
                        Schedule to use for probes within an
                        operation
                        
                        .. attribute:: probe_duration
                        
                        	Duration of each probe.  This must be specified if, and only if, ProbeDurationUnit is specified
                        	**type**\:  int
                        
                        	**range:** 1..3600
                        
                        .. attribute:: probe_duration_unit
                        
                        	Time unit associated with the ProbeDuration. The value must not be 'Once'
                        	**type**\:   :py:class:`SlaProbeDurationUnitsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes.SlaProbeDurationUnitsEnum>`
                        
                        .. attribute:: probe_interval
                        
                        	Interval between probes.  This must be specified if, and only if, ProbeIntervalUnit is not 'Week' or 'Day'
                        	**type**\:  int
                        
                        	**range:** 1..90
                        
                        .. attribute:: probe_interval_day
                        
                        	Day of week on which to schedule probes.  This must be specified if, and only if, ProbeIntervalUnit is 'Week'
                        	**type**\:   :py:class:`SlaProbeIntervalDayEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes.SlaProbeIntervalDayEnum>`
                        
                        .. attribute:: probe_interval_unit
                        
                        	Time unit associated with the ProbeInterval. The value must not be 'Once'.  If 'Week' or 'Day' is specified, probes are scheduled weekly or daily respectively
                        	**type**\:   :py:class:`SlaProbeIntervalUnitsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes.SlaProbeIntervalUnitsEnum>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: start_time_hour
                        
                        	Time after midnight (in UTC) to send the first packet each day
                        	**type**\:  int
                        
                        	**range:** 0..23
                        
                        .. attribute:: start_time_minute
                        
                        	Time after midnight (in UTC) to send the first packet each day. This must be specified if, and only if, StartTimeHour is specified
                        	**type**\:  int
                        
                        	**range:** 0..59
                        
                        .. attribute:: start_time_second
                        
                        	Time after midnight (in UTC) to send the first packet each day. This must only be specified if StartTimeHour is specified, and must not be specified if ProbeIntervalUnit is 'Week' or 'Day'
                        	**type**\:  int
                        
                        	**range:** 0..59
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ethernet-cfm-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Sla.Protocols.Ethernet.Profiles.Profile.Schedule, self).__init__()

                            self.yang_name = "schedule"
                            self.yang_parent_name = "profile"
                            self.is_presence_container = True

                            self.probe_duration = YLeaf(YType.uint32, "probe-duration")

                            self.probe_duration_unit = YLeaf(YType.enumeration, "probe-duration-unit")

                            self.probe_interval = YLeaf(YType.uint32, "probe-interval")

                            self.probe_interval_day = YLeaf(YType.enumeration, "probe-interval-day")

                            self.probe_interval_unit = YLeaf(YType.enumeration, "probe-interval-unit")

                            self.start_time_hour = YLeaf(YType.uint32, "start-time-hour")

                            self.start_time_minute = YLeaf(YType.uint32, "start-time-minute")

                            self.start_time_second = YLeaf(YType.uint32, "start-time-second")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("probe_duration",
                                            "probe_duration_unit",
                                            "probe_interval",
                                            "probe_interval_day",
                                            "probe_interval_unit",
                                            "start_time_hour",
                                            "start_time_minute",
                                            "start_time_second") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Sla.Protocols.Ethernet.Profiles.Profile.Schedule, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Sla.Protocols.Ethernet.Profiles.Profile.Schedule, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.probe_duration.is_set or
                                self.probe_duration_unit.is_set or
                                self.probe_interval.is_set or
                                self.probe_interval_day.is_set or
                                self.probe_interval_unit.is_set or
                                self.start_time_hour.is_set or
                                self.start_time_minute.is_set or
                                self.start_time_second.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.probe_duration.yfilter != YFilter.not_set or
                                self.probe_duration_unit.yfilter != YFilter.not_set or
                                self.probe_interval.yfilter != YFilter.not_set or
                                self.probe_interval_day.yfilter != YFilter.not_set or
                                self.probe_interval_unit.yfilter != YFilter.not_set or
                                self.start_time_hour.yfilter != YFilter.not_set or
                                self.start_time_minute.yfilter != YFilter.not_set or
                                self.start_time_second.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "schedule" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.probe_duration.is_set or self.probe_duration.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.probe_duration.get_name_leafdata())
                            if (self.probe_duration_unit.is_set or self.probe_duration_unit.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.probe_duration_unit.get_name_leafdata())
                            if (self.probe_interval.is_set or self.probe_interval.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.probe_interval.get_name_leafdata())
                            if (self.probe_interval_day.is_set or self.probe_interval_day.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.probe_interval_day.get_name_leafdata())
                            if (self.probe_interval_unit.is_set or self.probe_interval_unit.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.probe_interval_unit.get_name_leafdata())
                            if (self.start_time_hour.is_set or self.start_time_hour.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.start_time_hour.get_name_leafdata())
                            if (self.start_time_minute.is_set or self.start_time_minute.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.start_time_minute.get_name_leafdata())
                            if (self.start_time_second.is_set or self.start_time_second.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.start_time_second.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "probe-duration" or name == "probe-duration-unit" or name == "probe-interval" or name == "probe-interval-day" or name == "probe-interval-unit" or name == "start-time-hour" or name == "start-time-minute" or name == "start-time-second"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "probe-duration"):
                                self.probe_duration = value
                                self.probe_duration.value_namespace = name_space
                                self.probe_duration.value_namespace_prefix = name_space_prefix
                            if(value_path == "probe-duration-unit"):
                                self.probe_duration_unit = value
                                self.probe_duration_unit.value_namespace = name_space
                                self.probe_duration_unit.value_namespace_prefix = name_space_prefix
                            if(value_path == "probe-interval"):
                                self.probe_interval = value
                                self.probe_interval.value_namespace = name_space
                                self.probe_interval.value_namespace_prefix = name_space_prefix
                            if(value_path == "probe-interval-day"):
                                self.probe_interval_day = value
                                self.probe_interval_day.value_namespace = name_space
                                self.probe_interval_day.value_namespace_prefix = name_space_prefix
                            if(value_path == "probe-interval-unit"):
                                self.probe_interval_unit = value
                                self.probe_interval_unit.value_namespace = name_space
                                self.probe_interval_unit.value_namespace_prefix = name_space_prefix
                            if(value_path == "start-time-hour"):
                                self.start_time_hour = value
                                self.start_time_hour.value_namespace = name_space
                                self.start_time_hour.value_namespace_prefix = name_space_prefix
                            if(value_path == "start-time-minute"):
                                self.start_time_minute = value
                                self.start_time_minute.value_namespace = name_space
                                self.start_time_minute.value_namespace_prefix = name_space_prefix
                            if(value_path == "start-time-second"):
                                self.start_time_second = value
                                self.start_time_second.value_namespace = name_space
                                self.start_time_second.value_namespace_prefix = name_space_prefix


                    class Probe(Entity):
                        """
                        Probe configuration for the SLA profile
                        
                        .. attribute:: packet_size_and_padding
                        
                        	Minimum size to pad outgoing packet to
                        	**type**\:   :py:class:`PacketSizeAndPadding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg.Sla.Protocols.Ethernet.Profiles.Profile.Probe.PacketSizeAndPadding>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: priority
                        
                        	Priority class to assign to outgoing SLA packets
                        	**type**\:  int
                        
                        	**range:** 0..7
                        
                        .. attribute:: send
                        
                        	Schedule to use for packets within a burst.  The default value is to send a single packet once
                        	**type**\:   :py:class:`Send <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg.Sla.Protocols.Ethernet.Profiles.Profile.Probe.Send>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: synthetic_loss_calculation_packets
                        
                        	Number of packets to use in each FLR calculation
                        	**type**\:  int
                        
                        	**range:** 10..12096000
                        
                        

                        """

                        _prefix = 'ethernet-cfm-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Sla.Protocols.Ethernet.Profiles.Profile.Probe, self).__init__()

                            self.yang_name = "probe"
                            self.yang_parent_name = "profile"

                            self.priority = YLeaf(YType.uint32, "priority")

                            self.synthetic_loss_calculation_packets = YLeaf(YType.uint32, "synthetic-loss-calculation-packets")

                            self.packet_size_and_padding = None
                            self._children_name_map["packet_size_and_padding"] = "packet-size-and-padding"
                            self._children_yang_names.add("packet-size-and-padding")

                            self.send = None
                            self._children_name_map["send"] = "send"
                            self._children_yang_names.add("send")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("priority",
                                            "synthetic_loss_calculation_packets") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Sla.Protocols.Ethernet.Profiles.Profile.Probe, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Sla.Protocols.Ethernet.Profiles.Profile.Probe, self).__setattr__(name, value)


                        class Send(Entity):
                            """
                            Schedule to use for packets within a burst. 
                            The default value is to send a single packet
                            once.
                            
                            .. attribute:: burst_interval
                            
                            	Interval between bursts.  This must be specified if, and only if, the SendType is 'Burst' and the 'BurstIntervalUnit' is not 'Once'
                            	**type**\:  int
                            
                            	**range:** 1..3600
                            
                            .. attribute:: burst_interval_unit
                            
                            	Time unit associated with the BurstInterval .  This must be specified if, and only if, SendType is 'Burst'
                            	**type**\:   :py:class:`SlaBurstIntervalUnitsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes.SlaBurstIntervalUnitsEnum>`
                            
                            .. attribute:: packet_count
                            
                            	The number of packets in each burst.  This must be specified if, and only if, the SendType is 'Burst'
                            	**type**\:  int
                            
                            	**range:** 2..1200
                            
                            .. attribute:: packet_interval
                            
                            	Interval between packets.  This must be specified if, and only if, PacketIntervalUnit is not 'Once'
                            	**type**\:  int
                            
                            	**range:** 1..30000
                            
                            .. attribute:: packet_interval_unit
                            
                            	Time unit associated with the PacketInterval
                            	**type**\:   :py:class:`SlaPacketIntervalUnitsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes.SlaPacketIntervalUnitsEnum>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: send_type
                            
                            	The packet distribution\: single packets or bursts of packets.  If 'Burst' is specified , PacketCount and BurstInterval must be specified
                            	**type**\:   :py:class:`SlaSend <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes.SlaSend>`
                            
                            	**mandatory**\: True
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'ethernet-cfm-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.Profiles.Profile.Probe.Send, self).__init__()

                                self.yang_name = "send"
                                self.yang_parent_name = "probe"
                                self.is_presence_container = True

                                self.burst_interval = YLeaf(YType.uint32, "burst-interval")

                                self.burst_interval_unit = YLeaf(YType.enumeration, "burst-interval-unit")

                                self.packet_count = YLeaf(YType.uint32, "packet-count")

                                self.packet_interval = YLeaf(YType.uint32, "packet-interval")

                                self.packet_interval_unit = YLeaf(YType.enumeration, "packet-interval-unit")

                                self.send_type = YLeaf(YType.enumeration, "send-type")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("burst_interval",
                                                "burst_interval_unit",
                                                "packet_count",
                                                "packet_interval",
                                                "packet_interval_unit",
                                                "send_type") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Sla.Protocols.Ethernet.Profiles.Profile.Probe.Send, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Sla.Protocols.Ethernet.Profiles.Profile.Probe.Send, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.burst_interval.is_set or
                                    self.burst_interval_unit.is_set or
                                    self.packet_count.is_set or
                                    self.packet_interval.is_set or
                                    self.packet_interval_unit.is_set or
                                    self.send_type.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.burst_interval.yfilter != YFilter.not_set or
                                    self.burst_interval_unit.yfilter != YFilter.not_set or
                                    self.packet_count.yfilter != YFilter.not_set or
                                    self.packet_interval.yfilter != YFilter.not_set or
                                    self.packet_interval_unit.yfilter != YFilter.not_set or
                                    self.send_type.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "send" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.burst_interval.is_set or self.burst_interval.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.burst_interval.get_name_leafdata())
                                if (self.burst_interval_unit.is_set or self.burst_interval_unit.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.burst_interval_unit.get_name_leafdata())
                                if (self.packet_count.is_set or self.packet_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.packet_count.get_name_leafdata())
                                if (self.packet_interval.is_set or self.packet_interval.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.packet_interval.get_name_leafdata())
                                if (self.packet_interval_unit.is_set or self.packet_interval_unit.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.packet_interval_unit.get_name_leafdata())
                                if (self.send_type.is_set or self.send_type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.send_type.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "burst-interval" or name == "burst-interval-unit" or name == "packet-count" or name == "packet-interval" or name == "packet-interval-unit" or name == "send-type"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "burst-interval"):
                                    self.burst_interval = value
                                    self.burst_interval.value_namespace = name_space
                                    self.burst_interval.value_namespace_prefix = name_space_prefix
                                if(value_path == "burst-interval-unit"):
                                    self.burst_interval_unit = value
                                    self.burst_interval_unit.value_namespace = name_space
                                    self.burst_interval_unit.value_namespace_prefix = name_space_prefix
                                if(value_path == "packet-count"):
                                    self.packet_count = value
                                    self.packet_count.value_namespace = name_space
                                    self.packet_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "packet-interval"):
                                    self.packet_interval = value
                                    self.packet_interval.value_namespace = name_space
                                    self.packet_interval.value_namespace_prefix = name_space_prefix
                                if(value_path == "packet-interval-unit"):
                                    self.packet_interval_unit = value
                                    self.packet_interval_unit.value_namespace = name_space
                                    self.packet_interval_unit.value_namespace_prefix = name_space_prefix
                                if(value_path == "send-type"):
                                    self.send_type = value
                                    self.send_type.value_namespace = name_space
                                    self.send_type.value_namespace_prefix = name_space_prefix


                        class PacketSizeAndPadding(Entity):
                            """
                            Minimum size to pad outgoing packet to
                            
                            .. attribute:: padding_type
                            
                            	Type of padding to be used for the packet
                            	**type**\:   :py:class:`SlaPaddingPattern <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes.SlaPaddingPattern>`
                            
                            .. attribute:: padding_value
                            
                            	Pattern to be used for hex padding. This can be specified if, and only if, the PaddingType is 'Hex'
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{1,8}
                            
                            .. attribute:: size
                            
                            	Minimum size to pad outgoing packet to
                            	**type**\:  int
                            
                            	**range:** 1..9000
                            
                            	**mandatory**\: True
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'ethernet-cfm-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Sla.Protocols.Ethernet.Profiles.Profile.Probe.PacketSizeAndPadding, self).__init__()

                                self.yang_name = "packet-size-and-padding"
                                self.yang_parent_name = "probe"
                                self.is_presence_container = True

                                self.padding_type = YLeaf(YType.enumeration, "padding-type")

                                self.padding_value = YLeaf(YType.str, "padding-value")

                                self.size = YLeaf(YType.uint32, "size")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("padding_type",
                                                "padding_value",
                                                "size") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Sla.Protocols.Ethernet.Profiles.Profile.Probe.PacketSizeAndPadding, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Sla.Protocols.Ethernet.Profiles.Profile.Probe.PacketSizeAndPadding, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.padding_type.is_set or
                                    self.padding_value.is_set or
                                    self.size.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.padding_type.yfilter != YFilter.not_set or
                                    self.padding_value.yfilter != YFilter.not_set or
                                    self.size.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "packet-size-and-padding" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.padding_type.is_set or self.padding_type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.padding_type.get_name_leafdata())
                                if (self.padding_value.is_set or self.padding_value.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.padding_value.get_name_leafdata())
                                if (self.size.is_set or self.size.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.size.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "padding-type" or name == "padding-value" or name == "size"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "padding-type"):
                                    self.padding_type = value
                                    self.padding_type.value_namespace = name_space
                                    self.padding_type.value_namespace_prefix = name_space_prefix
                                if(value_path == "padding-value"):
                                    self.padding_value = value
                                    self.padding_value.value_namespace = name_space
                                    self.padding_value.value_namespace_prefix = name_space_prefix
                                if(value_path == "size"):
                                    self.size = value
                                    self.size.value_namespace = name_space
                                    self.size.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.priority.is_set or
                                self.synthetic_loss_calculation_packets.is_set or
                                (self.packet_size_and_padding is not None) or
                                (self.send is not None))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.priority.yfilter != YFilter.not_set or
                                self.synthetic_loss_calculation_packets.yfilter != YFilter.not_set or
                                (self.packet_size_and_padding is not None and self.packet_size_and_padding.has_operation()) or
                                (self.send is not None and self.send.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "probe" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.priority.is_set or self.priority.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.priority.get_name_leafdata())
                            if (self.synthetic_loss_calculation_packets.is_set or self.synthetic_loss_calculation_packets.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.synthetic_loss_calculation_packets.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "packet-size-and-padding"):
                                if (self.packet_size_and_padding is None):
                                    self.packet_size_and_padding = Sla.Protocols.Ethernet.Profiles.Profile.Probe.PacketSizeAndPadding()
                                    self.packet_size_and_padding.parent = self
                                    self._children_name_map["packet_size_and_padding"] = "packet-size-and-padding"
                                return self.packet_size_and_padding

                            if (child_yang_name == "send"):
                                if (self.send is None):
                                    self.send = Sla.Protocols.Ethernet.Profiles.Profile.Probe.Send()
                                    self.send.parent = self
                                    self._children_name_map["send"] = "send"
                                return self.send

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "packet-size-and-padding" or name == "send" or name == "priority" or name == "synthetic-loss-calculation-packets"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "priority"):
                                self.priority = value
                                self.priority.value_namespace = name_space
                                self.priority.value_namespace_prefix = name_space_prefix
                            if(value_path == "synthetic-loss-calculation-packets"):
                                self.synthetic_loss_calculation_packets = value
                                self.synthetic_loss_calculation_packets.value_namespace = name_space
                                self.synthetic_loss_calculation_packets.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.profile_name.is_set or
                            self.packet_type.is_set or
                            (self.probe is not None and self.probe.has_data()) or
                            (self.statistics is not None and self.statistics.has_data()) or
                            (self.schedule is not None))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.profile_name.yfilter != YFilter.not_set or
                            self.packet_type.yfilter != YFilter.not_set or
                            (self.probe is not None and self.probe.has_operation()) or
                            (self.schedule is not None and self.schedule.has_operation()) or
                            (self.statistics is not None and self.statistics.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "profile" + "[profile-name='" + self.profile_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-infra-sla-cfg:sla/protocols/Cisco-IOS-XR-ethernet-cfm-cfg:ethernet/profiles/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.profile_name.is_set or self.profile_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.profile_name.get_name_leafdata())
                        if (self.packet_type.is_set or self.packet_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.packet_type.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "probe"):
                            if (self.probe is None):
                                self.probe = Sla.Protocols.Ethernet.Profiles.Profile.Probe()
                                self.probe.parent = self
                                self._children_name_map["probe"] = "probe"
                            return self.probe

                        if (child_yang_name == "schedule"):
                            if (self.schedule is None):
                                self.schedule = Sla.Protocols.Ethernet.Profiles.Profile.Schedule()
                                self.schedule.parent = self
                                self._children_name_map["schedule"] = "schedule"
                            return self.schedule

                        if (child_yang_name == "statistics"):
                            if (self.statistics is None):
                                self.statistics = Sla.Protocols.Ethernet.Profiles.Profile.Statistics()
                                self.statistics.parent = self
                                self._children_name_map["statistics"] = "statistics"
                            return self.statistics

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "probe" or name == "schedule" or name == "statistics" or name == "profile-name" or name == "packet-type"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "profile-name"):
                            self.profile_name = value
                            self.profile_name.value_namespace = name_space
                            self.profile_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "packet-type"):
                            self.packet_type = value
                            self.packet_type.value_namespace = name_space
                            self.packet_type.value_namespace_prefix = name_space_prefix

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
                        path_buffer = "Cisco-IOS-XR-infra-sla-cfg:sla/protocols/Cisco-IOS-XR-ethernet-cfm-cfg:ethernet/%s" % self.get_segment_path()
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
                        c = Sla.Protocols.Ethernet.Profiles.Profile()
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
                path_buffer = "Cisco-IOS-XR-ethernet-cfm-cfg:ethernet" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-sla-cfg:sla/protocols/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "profiles"):
                    if (self.profiles is None):
                        self.profiles = Sla.Protocols.Ethernet.Profiles()
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

        def has_data(self):
            return (self.ethernet is not None and self.ethernet.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.ethernet is not None and self.ethernet.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "protocols" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-sla-cfg:sla/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ethernet"):
                if (self.ethernet is None):
                    self.ethernet = Sla.Protocols.Ethernet()
                    self.ethernet.parent = self
                    self._children_name_map["ethernet"] = "ethernet"
                return self.ethernet

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ethernet"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.protocols is not None and self.protocols.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.protocols is not None and self.protocols.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-infra-sla-cfg:sla" + path_buffer

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

        if (child_yang_name == "protocols"):
            if (self.protocols is None):
                self.protocols = Sla.Protocols()
                self.protocols.parent = self
                self._children_name_map["protocols"] = "protocols"
            return self.protocols

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "protocols"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Sla()
        return self._top_entity


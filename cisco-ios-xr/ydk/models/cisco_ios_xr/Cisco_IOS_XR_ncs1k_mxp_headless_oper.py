""" Cisco_IOS_XR_ncs1k_mxp_headless_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ncs1k\-mxp\-headless package operational data.

This module contains definitions
for the following management objects\:
  headless\-func\-data\: Information related to headless
    functionality

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class HeadlessFuncData(Entity):
    """
    Information related to headless functionality
    
    .. attribute:: ethernet_port_names
    
    	Ethernet Statistics collected during last headless operation
    	**type**\:   :py:class:`EthernetPortNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_headless_oper.HeadlessFuncData.EthernetPortNames>`
    
    .. attribute:: otn_port_names
    
    	OTN Statistics collected during last headless operation
    	**type**\:   :py:class:`OtnPortNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_headless_oper.HeadlessFuncData.OtnPortNames>`
    
    

    """

    _prefix = 'ncs1k-mxp-headless-oper'
    _revision = '2016-09-13'

    def __init__(self):
        super(HeadlessFuncData, self).__init__()
        self._top_entity = None

        self.yang_name = "headless-func-data"
        self.yang_parent_name = "Cisco-IOS-XR-ncs1k-mxp-headless-oper"

        self.ethernet_port_names = HeadlessFuncData.EthernetPortNames()
        self.ethernet_port_names.parent = self
        self._children_name_map["ethernet_port_names"] = "ethernet-port-names"
        self._children_yang_names.add("ethernet-port-names")

        self.otn_port_names = HeadlessFuncData.OtnPortNames()
        self.otn_port_names.parent = self
        self._children_name_map["otn_port_names"] = "otn-port-names"
        self._children_yang_names.add("otn-port-names")


    class OtnPortNames(Entity):
        """
        OTN Statistics collected during last headless
        operation
        
        .. attribute:: otn_port_name
        
        	port Name
        	**type**\: list of    :py:class:`OtnPortName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_headless_oper.HeadlessFuncData.OtnPortNames.OtnPortName>`
        
        

        """

        _prefix = 'ncs1k-mxp-headless-oper'
        _revision = '2016-09-13'

        def __init__(self):
            super(HeadlessFuncData.OtnPortNames, self).__init__()

            self.yang_name = "otn-port-names"
            self.yang_parent_name = "headless-func-data"

            self.otn_port_name = YList(self)

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
                        super(HeadlessFuncData.OtnPortNames, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(HeadlessFuncData.OtnPortNames, self).__setattr__(name, value)


        class OtnPortName(Entity):
            """
            port Name
            
            .. attribute:: name  <key>
            
            	Port name
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: headless_end_time
            
            	Headless End Time
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: headless_start_time
            
            	Headless Start Time
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: otn_statistics
            
            	OTN statistics
            	**type**\:   :py:class:`OtnStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_headless_oper.HeadlessFuncData.OtnPortNames.OtnPortName.OtnStatistics>`
            
            .. attribute:: started_stateful
            
            	Started Stateful
            	**type**\:  bool
            
            

            """

            _prefix = 'ncs1k-mxp-headless-oper'
            _revision = '2016-09-13'

            def __init__(self):
                super(HeadlessFuncData.OtnPortNames.OtnPortName, self).__init__()

                self.yang_name = "otn-port-name"
                self.yang_parent_name = "otn-port-names"

                self.name = YLeaf(YType.str, "name")

                self.headless_end_time = YLeaf(YType.str, "headless-end-time")

                self.headless_start_time = YLeaf(YType.str, "headless-start-time")

                self.started_stateful = YLeaf(YType.boolean, "started-stateful")

                self.otn_statistics = HeadlessFuncData.OtnPortNames.OtnPortName.OtnStatistics()
                self.otn_statistics.parent = self
                self._children_name_map["otn_statistics"] = "otn-statistics"
                self._children_yang_names.add("otn-statistics")

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
                                "headless_end_time",
                                "headless_start_time",
                                "started_stateful") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(HeadlessFuncData.OtnPortNames.OtnPortName, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(HeadlessFuncData.OtnPortNames.OtnPortName, self).__setattr__(name, value)


            class OtnStatistics(Entity):
                """
                OTN statistics
                
                .. attribute:: fec_ec
                
                	FecEc
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: fec_uc
                
                	FecUc
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: sm_bei
                
                	SmBei
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: sm_bip
                
                	SmBip
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'ncs1k-mxp-headless-oper'
                _revision = '2016-09-13'

                def __init__(self):
                    super(HeadlessFuncData.OtnPortNames.OtnPortName.OtnStatistics, self).__init__()

                    self.yang_name = "otn-statistics"
                    self.yang_parent_name = "otn-port-name"

                    self.fec_ec = YLeaf(YType.uint64, "fec-ec")

                    self.fec_uc = YLeaf(YType.uint64, "fec-uc")

                    self.sm_bei = YLeaf(YType.uint64, "sm-bei")

                    self.sm_bip = YLeaf(YType.uint64, "sm-bip")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("fec_ec",
                                    "fec_uc",
                                    "sm_bei",
                                    "sm_bip") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(HeadlessFuncData.OtnPortNames.OtnPortName.OtnStatistics, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(HeadlessFuncData.OtnPortNames.OtnPortName.OtnStatistics, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.fec_ec.is_set or
                        self.fec_uc.is_set or
                        self.sm_bei.is_set or
                        self.sm_bip.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.fec_ec.yfilter != YFilter.not_set or
                        self.fec_uc.yfilter != YFilter.not_set or
                        self.sm_bei.yfilter != YFilter.not_set or
                        self.sm_bip.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "otn-statistics" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.fec_ec.is_set or self.fec_ec.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.fec_ec.get_name_leafdata())
                    if (self.fec_uc.is_set or self.fec_uc.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.fec_uc.get_name_leafdata())
                    if (self.sm_bei.is_set or self.sm_bei.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sm_bei.get_name_leafdata())
                    if (self.sm_bip.is_set or self.sm_bip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sm_bip.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "fec-ec" or name == "fec-uc" or name == "sm-bei" or name == "sm-bip"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "fec-ec"):
                        self.fec_ec = value
                        self.fec_ec.value_namespace = name_space
                        self.fec_ec.value_namespace_prefix = name_space_prefix
                    if(value_path == "fec-uc"):
                        self.fec_uc = value
                        self.fec_uc.value_namespace = name_space
                        self.fec_uc.value_namespace_prefix = name_space_prefix
                    if(value_path == "sm-bei"):
                        self.sm_bei = value
                        self.sm_bei.value_namespace = name_space
                        self.sm_bei.value_namespace_prefix = name_space_prefix
                    if(value_path == "sm-bip"):
                        self.sm_bip = value
                        self.sm_bip.value_namespace = name_space
                        self.sm_bip.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.name.is_set or
                    self.headless_end_time.is_set or
                    self.headless_start_time.is_set or
                    self.started_stateful.is_set or
                    (self.otn_statistics is not None and self.otn_statistics.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    self.headless_end_time.yfilter != YFilter.not_set or
                    self.headless_start_time.yfilter != YFilter.not_set or
                    self.started_stateful.yfilter != YFilter.not_set or
                    (self.otn_statistics is not None and self.otn_statistics.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "otn-port-name" + "[name='" + self.name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ncs1k-mxp-headless-oper:headless-func-data/otn-port-names/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())
                if (self.headless_end_time.is_set or self.headless_end_time.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.headless_end_time.get_name_leafdata())
                if (self.headless_start_time.is_set or self.headless_start_time.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.headless_start_time.get_name_leafdata())
                if (self.started_stateful.is_set or self.started_stateful.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.started_stateful.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "otn-statistics"):
                    if (self.otn_statistics is None):
                        self.otn_statistics = HeadlessFuncData.OtnPortNames.OtnPortName.OtnStatistics()
                        self.otn_statistics.parent = self
                        self._children_name_map["otn_statistics"] = "otn-statistics"
                    return self.otn_statistics

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "otn-statistics" or name == "name" or name == "headless-end-time" or name == "headless-start-time" or name == "started-stateful"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix
                if(value_path == "headless-end-time"):
                    self.headless_end_time = value
                    self.headless_end_time.value_namespace = name_space
                    self.headless_end_time.value_namespace_prefix = name_space_prefix
                if(value_path == "headless-start-time"):
                    self.headless_start_time = value
                    self.headless_start_time.value_namespace = name_space
                    self.headless_start_time.value_namespace_prefix = name_space_prefix
                if(value_path == "started-stateful"):
                    self.started_stateful = value
                    self.started_stateful.value_namespace = name_space
                    self.started_stateful.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.otn_port_name:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.otn_port_name:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "otn-port-names" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ncs1k-mxp-headless-oper:headless-func-data/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "otn-port-name"):
                for c in self.otn_port_name:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = HeadlessFuncData.OtnPortNames.OtnPortName()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.otn_port_name.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "otn-port-name"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class EthernetPortNames(Entity):
        """
        Ethernet Statistics collected during last
        headless operation
        
        .. attribute:: ethernet_port_name
        
        	Port Name
        	**type**\: list of    :py:class:`EthernetPortName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_headless_oper.HeadlessFuncData.EthernetPortNames.EthernetPortName>`
        
        

        """

        _prefix = 'ncs1k-mxp-headless-oper'
        _revision = '2016-09-13'

        def __init__(self):
            super(HeadlessFuncData.EthernetPortNames, self).__init__()

            self.yang_name = "ethernet-port-names"
            self.yang_parent_name = "headless-func-data"

            self.ethernet_port_name = YList(self)

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
                        super(HeadlessFuncData.EthernetPortNames, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(HeadlessFuncData.EthernetPortNames, self).__setattr__(name, value)


        class EthernetPortName(Entity):
            """
            Port Name
            
            .. attribute:: name  <key>
            
            	Port name
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: ether_statistics
            
            	Ether Statistics
            	**type**\:   :py:class:`EtherStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_headless_oper.HeadlessFuncData.EthernetPortNames.EthernetPortName.EtherStatistics>`
            
            .. attribute:: headless_end_time
            
            	Headless End Time
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: headless_start_time
            
            	Headless Start Time
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: started_stateful
            
            	Started Stateful
            	**type**\:  bool
            
            

            """

            _prefix = 'ncs1k-mxp-headless-oper'
            _revision = '2016-09-13'

            def __init__(self):
                super(HeadlessFuncData.EthernetPortNames.EthernetPortName, self).__init__()

                self.yang_name = "ethernet-port-name"
                self.yang_parent_name = "ethernet-port-names"

                self.name = YLeaf(YType.str, "name")

                self.headless_end_time = YLeaf(YType.str, "headless-end-time")

                self.headless_start_time = YLeaf(YType.str, "headless-start-time")

                self.started_stateful = YLeaf(YType.boolean, "started-stateful")

                self.ether_statistics = HeadlessFuncData.EthernetPortNames.EthernetPortName.EtherStatistics()
                self.ether_statistics.parent = self
                self._children_name_map["ether_statistics"] = "ether-statistics"
                self._children_yang_names.add("ether-statistics")

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
                                "headless_end_time",
                                "headless_start_time",
                                "started_stateful") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(HeadlessFuncData.EthernetPortNames.EthernetPortName, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(HeadlessFuncData.EthernetPortNames.EthernetPortName, self).__setattr__(name, value)


            class EtherStatistics(Entity):
                """
                Ether Statistics
                
                .. attribute:: rx8021q_pkt
                
                	Rx8021QPkt
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_bytes_good
                
                	RxBytesGood
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_error_jabbers
                
                	RxErrorJabbers
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_lldp_pkt
                
                	RxLldpPkt
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_packets
                
                	RxPackets
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_pause
                
                	RxPause
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_pkt_drop
                
                	RxPktDrop
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_pkts1024_to1518_bytes
                
                	RxPkts1024To1518Bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_pkts128to255_bytes
                
                	RxPkts128to255Bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_pkts256_to511_bytes
                
                	RxPkts256To511Bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_pkts512_to1023_bytes
                
                	RxPkts512To1023Bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_pkts64_bytes
                
                	RxPkts64Bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_pkts65_to127_bytes
                
                	RxPkts65To127Bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_pkts_bad_fcs
                
                	RxPktsBadFcs
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_pkts_broadcast
                
                	RxPktsBroadcast
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_pkts_good
                
                	RxPktsGood
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_pkts_multicast
                
                	RxPktsMulticast
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_pkts_over_sized
                
                	RxPktsOverSized
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_pkts_under_sized
                
                	RxPktsUnderSized
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_pkts_unicast
                
                	RxPktsUnicast
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_recv_fragments
                
                	RxRecvFragments
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_total_bytes
                
                	RxTotalBytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_bad_fcs
                
                	TxBadFCS
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_bytes_good
                
                	TxBytesGood
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_fragments
                
                	TxFragments
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_jabber
                
                	TxJabber
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_packets
                
                	TxPackets
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_pause
                
                	TxPause
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_pkts_good
                
                	TxPktsGood
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_pkts_over_sized
                
                	TxPktsOverSized
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_pkts_under_sized
                
                	TxPktsUnderSized
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_total_bytes
                
                	TxTotalBytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'ncs1k-mxp-headless-oper'
                _revision = '2016-09-13'

                def __init__(self):
                    super(HeadlessFuncData.EthernetPortNames.EthernetPortName.EtherStatistics, self).__init__()

                    self.yang_name = "ether-statistics"
                    self.yang_parent_name = "ethernet-port-name"

                    self.rx8021q_pkt = YLeaf(YType.uint64, "rx8021q-pkt")

                    self.rx_bytes_good = YLeaf(YType.uint64, "rx-bytes-good")

                    self.rx_error_jabbers = YLeaf(YType.uint64, "rx-error-jabbers")

                    self.rx_lldp_pkt = YLeaf(YType.uint64, "rx-lldp-pkt")

                    self.rx_packets = YLeaf(YType.uint64, "rx-packets")

                    self.rx_pause = YLeaf(YType.uint64, "rx-pause")

                    self.rx_pkt_drop = YLeaf(YType.uint64, "rx-pkt-drop")

                    self.rx_pkts1024_to1518_bytes = YLeaf(YType.uint64, "rx-pkts1024-to1518-bytes")

                    self.rx_pkts128to255_bytes = YLeaf(YType.uint64, "rx-pkts128to255-bytes")

                    self.rx_pkts256_to511_bytes = YLeaf(YType.uint64, "rx-pkts256-to511-bytes")

                    self.rx_pkts512_to1023_bytes = YLeaf(YType.uint64, "rx-pkts512-to1023-bytes")

                    self.rx_pkts64_bytes = YLeaf(YType.uint64, "rx-pkts64-bytes")

                    self.rx_pkts65_to127_bytes = YLeaf(YType.uint64, "rx-pkts65-to127-bytes")

                    self.rx_pkts_bad_fcs = YLeaf(YType.uint64, "rx-pkts-bad-fcs")

                    self.rx_pkts_broadcast = YLeaf(YType.uint64, "rx-pkts-broadcast")

                    self.rx_pkts_good = YLeaf(YType.uint64, "rx-pkts-good")

                    self.rx_pkts_multicast = YLeaf(YType.uint64, "rx-pkts-multicast")

                    self.rx_pkts_over_sized = YLeaf(YType.uint64, "rx-pkts-over-sized")

                    self.rx_pkts_under_sized = YLeaf(YType.uint64, "rx-pkts-under-sized")

                    self.rx_pkts_unicast = YLeaf(YType.uint64, "rx-pkts-unicast")

                    self.rx_recv_fragments = YLeaf(YType.uint64, "rx-recv-fragments")

                    self.rx_total_bytes = YLeaf(YType.uint64, "rx-total-bytes")

                    self.tx_bad_fcs = YLeaf(YType.uint64, "tx-bad-fcs")

                    self.tx_bytes_good = YLeaf(YType.uint64, "tx-bytes-good")

                    self.tx_fragments = YLeaf(YType.uint64, "tx-fragments")

                    self.tx_jabber = YLeaf(YType.uint64, "tx-jabber")

                    self.tx_packets = YLeaf(YType.uint64, "tx-packets")

                    self.tx_pause = YLeaf(YType.uint64, "tx-pause")

                    self.tx_pkts_good = YLeaf(YType.uint64, "tx-pkts-good")

                    self.tx_pkts_over_sized = YLeaf(YType.uint64, "tx-pkts-over-sized")

                    self.tx_pkts_under_sized = YLeaf(YType.uint64, "tx-pkts-under-sized")

                    self.tx_total_bytes = YLeaf(YType.uint64, "tx-total-bytes")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("rx8021q_pkt",
                                    "rx_bytes_good",
                                    "rx_error_jabbers",
                                    "rx_lldp_pkt",
                                    "rx_packets",
                                    "rx_pause",
                                    "rx_pkt_drop",
                                    "rx_pkts1024_to1518_bytes",
                                    "rx_pkts128to255_bytes",
                                    "rx_pkts256_to511_bytes",
                                    "rx_pkts512_to1023_bytes",
                                    "rx_pkts64_bytes",
                                    "rx_pkts65_to127_bytes",
                                    "rx_pkts_bad_fcs",
                                    "rx_pkts_broadcast",
                                    "rx_pkts_good",
                                    "rx_pkts_multicast",
                                    "rx_pkts_over_sized",
                                    "rx_pkts_under_sized",
                                    "rx_pkts_unicast",
                                    "rx_recv_fragments",
                                    "rx_total_bytes",
                                    "tx_bad_fcs",
                                    "tx_bytes_good",
                                    "tx_fragments",
                                    "tx_jabber",
                                    "tx_packets",
                                    "tx_pause",
                                    "tx_pkts_good",
                                    "tx_pkts_over_sized",
                                    "tx_pkts_under_sized",
                                    "tx_total_bytes") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(HeadlessFuncData.EthernetPortNames.EthernetPortName.EtherStatistics, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(HeadlessFuncData.EthernetPortNames.EthernetPortName.EtherStatistics, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.rx8021q_pkt.is_set or
                        self.rx_bytes_good.is_set or
                        self.rx_error_jabbers.is_set or
                        self.rx_lldp_pkt.is_set or
                        self.rx_packets.is_set or
                        self.rx_pause.is_set or
                        self.rx_pkt_drop.is_set or
                        self.rx_pkts1024_to1518_bytes.is_set or
                        self.rx_pkts128to255_bytes.is_set or
                        self.rx_pkts256_to511_bytes.is_set or
                        self.rx_pkts512_to1023_bytes.is_set or
                        self.rx_pkts64_bytes.is_set or
                        self.rx_pkts65_to127_bytes.is_set or
                        self.rx_pkts_bad_fcs.is_set or
                        self.rx_pkts_broadcast.is_set or
                        self.rx_pkts_good.is_set or
                        self.rx_pkts_multicast.is_set or
                        self.rx_pkts_over_sized.is_set or
                        self.rx_pkts_under_sized.is_set or
                        self.rx_pkts_unicast.is_set or
                        self.rx_recv_fragments.is_set or
                        self.rx_total_bytes.is_set or
                        self.tx_bad_fcs.is_set or
                        self.tx_bytes_good.is_set or
                        self.tx_fragments.is_set or
                        self.tx_jabber.is_set or
                        self.tx_packets.is_set or
                        self.tx_pause.is_set or
                        self.tx_pkts_good.is_set or
                        self.tx_pkts_over_sized.is_set or
                        self.tx_pkts_under_sized.is_set or
                        self.tx_total_bytes.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.rx8021q_pkt.yfilter != YFilter.not_set or
                        self.rx_bytes_good.yfilter != YFilter.not_set or
                        self.rx_error_jabbers.yfilter != YFilter.not_set or
                        self.rx_lldp_pkt.yfilter != YFilter.not_set or
                        self.rx_packets.yfilter != YFilter.not_set or
                        self.rx_pause.yfilter != YFilter.not_set or
                        self.rx_pkt_drop.yfilter != YFilter.not_set or
                        self.rx_pkts1024_to1518_bytes.yfilter != YFilter.not_set or
                        self.rx_pkts128to255_bytes.yfilter != YFilter.not_set or
                        self.rx_pkts256_to511_bytes.yfilter != YFilter.not_set or
                        self.rx_pkts512_to1023_bytes.yfilter != YFilter.not_set or
                        self.rx_pkts64_bytes.yfilter != YFilter.not_set or
                        self.rx_pkts65_to127_bytes.yfilter != YFilter.not_set or
                        self.rx_pkts_bad_fcs.yfilter != YFilter.not_set or
                        self.rx_pkts_broadcast.yfilter != YFilter.not_set or
                        self.rx_pkts_good.yfilter != YFilter.not_set or
                        self.rx_pkts_multicast.yfilter != YFilter.not_set or
                        self.rx_pkts_over_sized.yfilter != YFilter.not_set or
                        self.rx_pkts_under_sized.yfilter != YFilter.not_set or
                        self.rx_pkts_unicast.yfilter != YFilter.not_set or
                        self.rx_recv_fragments.yfilter != YFilter.not_set or
                        self.rx_total_bytes.yfilter != YFilter.not_set or
                        self.tx_bad_fcs.yfilter != YFilter.not_set or
                        self.tx_bytes_good.yfilter != YFilter.not_set or
                        self.tx_fragments.yfilter != YFilter.not_set or
                        self.tx_jabber.yfilter != YFilter.not_set or
                        self.tx_packets.yfilter != YFilter.not_set or
                        self.tx_pause.yfilter != YFilter.not_set or
                        self.tx_pkts_good.yfilter != YFilter.not_set or
                        self.tx_pkts_over_sized.yfilter != YFilter.not_set or
                        self.tx_pkts_under_sized.yfilter != YFilter.not_set or
                        self.tx_total_bytes.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ether-statistics" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.rx8021q_pkt.is_set or self.rx8021q_pkt.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rx8021q_pkt.get_name_leafdata())
                    if (self.rx_bytes_good.is_set or self.rx_bytes_good.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rx_bytes_good.get_name_leafdata())
                    if (self.rx_error_jabbers.is_set or self.rx_error_jabbers.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rx_error_jabbers.get_name_leafdata())
                    if (self.rx_lldp_pkt.is_set or self.rx_lldp_pkt.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rx_lldp_pkt.get_name_leafdata())
                    if (self.rx_packets.is_set or self.rx_packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rx_packets.get_name_leafdata())
                    if (self.rx_pause.is_set or self.rx_pause.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rx_pause.get_name_leafdata())
                    if (self.rx_pkt_drop.is_set or self.rx_pkt_drop.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rx_pkt_drop.get_name_leafdata())
                    if (self.rx_pkts1024_to1518_bytes.is_set or self.rx_pkts1024_to1518_bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rx_pkts1024_to1518_bytes.get_name_leafdata())
                    if (self.rx_pkts128to255_bytes.is_set or self.rx_pkts128to255_bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rx_pkts128to255_bytes.get_name_leafdata())
                    if (self.rx_pkts256_to511_bytes.is_set or self.rx_pkts256_to511_bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rx_pkts256_to511_bytes.get_name_leafdata())
                    if (self.rx_pkts512_to1023_bytes.is_set or self.rx_pkts512_to1023_bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rx_pkts512_to1023_bytes.get_name_leafdata())
                    if (self.rx_pkts64_bytes.is_set or self.rx_pkts64_bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rx_pkts64_bytes.get_name_leafdata())
                    if (self.rx_pkts65_to127_bytes.is_set or self.rx_pkts65_to127_bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rx_pkts65_to127_bytes.get_name_leafdata())
                    if (self.rx_pkts_bad_fcs.is_set or self.rx_pkts_bad_fcs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rx_pkts_bad_fcs.get_name_leafdata())
                    if (self.rx_pkts_broadcast.is_set or self.rx_pkts_broadcast.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rx_pkts_broadcast.get_name_leafdata())
                    if (self.rx_pkts_good.is_set or self.rx_pkts_good.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rx_pkts_good.get_name_leafdata())
                    if (self.rx_pkts_multicast.is_set or self.rx_pkts_multicast.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rx_pkts_multicast.get_name_leafdata())
                    if (self.rx_pkts_over_sized.is_set or self.rx_pkts_over_sized.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rx_pkts_over_sized.get_name_leafdata())
                    if (self.rx_pkts_under_sized.is_set or self.rx_pkts_under_sized.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rx_pkts_under_sized.get_name_leafdata())
                    if (self.rx_pkts_unicast.is_set or self.rx_pkts_unicast.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rx_pkts_unicast.get_name_leafdata())
                    if (self.rx_recv_fragments.is_set or self.rx_recv_fragments.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rx_recv_fragments.get_name_leafdata())
                    if (self.rx_total_bytes.is_set or self.rx_total_bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rx_total_bytes.get_name_leafdata())
                    if (self.tx_bad_fcs.is_set or self.tx_bad_fcs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tx_bad_fcs.get_name_leafdata())
                    if (self.tx_bytes_good.is_set or self.tx_bytes_good.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tx_bytes_good.get_name_leafdata())
                    if (self.tx_fragments.is_set or self.tx_fragments.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tx_fragments.get_name_leafdata())
                    if (self.tx_jabber.is_set or self.tx_jabber.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tx_jabber.get_name_leafdata())
                    if (self.tx_packets.is_set or self.tx_packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tx_packets.get_name_leafdata())
                    if (self.tx_pause.is_set or self.tx_pause.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tx_pause.get_name_leafdata())
                    if (self.tx_pkts_good.is_set or self.tx_pkts_good.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tx_pkts_good.get_name_leafdata())
                    if (self.tx_pkts_over_sized.is_set or self.tx_pkts_over_sized.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tx_pkts_over_sized.get_name_leafdata())
                    if (self.tx_pkts_under_sized.is_set or self.tx_pkts_under_sized.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tx_pkts_under_sized.get_name_leafdata())
                    if (self.tx_total_bytes.is_set or self.tx_total_bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tx_total_bytes.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "rx8021q-pkt" or name == "rx-bytes-good" or name == "rx-error-jabbers" or name == "rx-lldp-pkt" or name == "rx-packets" or name == "rx-pause" or name == "rx-pkt-drop" or name == "rx-pkts1024-to1518-bytes" or name == "rx-pkts128to255-bytes" or name == "rx-pkts256-to511-bytes" or name == "rx-pkts512-to1023-bytes" or name == "rx-pkts64-bytes" or name == "rx-pkts65-to127-bytes" or name == "rx-pkts-bad-fcs" or name == "rx-pkts-broadcast" or name == "rx-pkts-good" or name == "rx-pkts-multicast" or name == "rx-pkts-over-sized" or name == "rx-pkts-under-sized" or name == "rx-pkts-unicast" or name == "rx-recv-fragments" or name == "rx-total-bytes" or name == "tx-bad-fcs" or name == "tx-bytes-good" or name == "tx-fragments" or name == "tx-jabber" or name == "tx-packets" or name == "tx-pause" or name == "tx-pkts-good" or name == "tx-pkts-over-sized" or name == "tx-pkts-under-sized" or name == "tx-total-bytes"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "rx8021q-pkt"):
                        self.rx8021q_pkt = value
                        self.rx8021q_pkt.value_namespace = name_space
                        self.rx8021q_pkt.value_namespace_prefix = name_space_prefix
                    if(value_path == "rx-bytes-good"):
                        self.rx_bytes_good = value
                        self.rx_bytes_good.value_namespace = name_space
                        self.rx_bytes_good.value_namespace_prefix = name_space_prefix
                    if(value_path == "rx-error-jabbers"):
                        self.rx_error_jabbers = value
                        self.rx_error_jabbers.value_namespace = name_space
                        self.rx_error_jabbers.value_namespace_prefix = name_space_prefix
                    if(value_path == "rx-lldp-pkt"):
                        self.rx_lldp_pkt = value
                        self.rx_lldp_pkt.value_namespace = name_space
                        self.rx_lldp_pkt.value_namespace_prefix = name_space_prefix
                    if(value_path == "rx-packets"):
                        self.rx_packets = value
                        self.rx_packets.value_namespace = name_space
                        self.rx_packets.value_namespace_prefix = name_space_prefix
                    if(value_path == "rx-pause"):
                        self.rx_pause = value
                        self.rx_pause.value_namespace = name_space
                        self.rx_pause.value_namespace_prefix = name_space_prefix
                    if(value_path == "rx-pkt-drop"):
                        self.rx_pkt_drop = value
                        self.rx_pkt_drop.value_namespace = name_space
                        self.rx_pkt_drop.value_namespace_prefix = name_space_prefix
                    if(value_path == "rx-pkts1024-to1518-bytes"):
                        self.rx_pkts1024_to1518_bytes = value
                        self.rx_pkts1024_to1518_bytes.value_namespace = name_space
                        self.rx_pkts1024_to1518_bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "rx-pkts128to255-bytes"):
                        self.rx_pkts128to255_bytes = value
                        self.rx_pkts128to255_bytes.value_namespace = name_space
                        self.rx_pkts128to255_bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "rx-pkts256-to511-bytes"):
                        self.rx_pkts256_to511_bytes = value
                        self.rx_pkts256_to511_bytes.value_namespace = name_space
                        self.rx_pkts256_to511_bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "rx-pkts512-to1023-bytes"):
                        self.rx_pkts512_to1023_bytes = value
                        self.rx_pkts512_to1023_bytes.value_namespace = name_space
                        self.rx_pkts512_to1023_bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "rx-pkts64-bytes"):
                        self.rx_pkts64_bytes = value
                        self.rx_pkts64_bytes.value_namespace = name_space
                        self.rx_pkts64_bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "rx-pkts65-to127-bytes"):
                        self.rx_pkts65_to127_bytes = value
                        self.rx_pkts65_to127_bytes.value_namespace = name_space
                        self.rx_pkts65_to127_bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "rx-pkts-bad-fcs"):
                        self.rx_pkts_bad_fcs = value
                        self.rx_pkts_bad_fcs.value_namespace = name_space
                        self.rx_pkts_bad_fcs.value_namespace_prefix = name_space_prefix
                    if(value_path == "rx-pkts-broadcast"):
                        self.rx_pkts_broadcast = value
                        self.rx_pkts_broadcast.value_namespace = name_space
                        self.rx_pkts_broadcast.value_namespace_prefix = name_space_prefix
                    if(value_path == "rx-pkts-good"):
                        self.rx_pkts_good = value
                        self.rx_pkts_good.value_namespace = name_space
                        self.rx_pkts_good.value_namespace_prefix = name_space_prefix
                    if(value_path == "rx-pkts-multicast"):
                        self.rx_pkts_multicast = value
                        self.rx_pkts_multicast.value_namespace = name_space
                        self.rx_pkts_multicast.value_namespace_prefix = name_space_prefix
                    if(value_path == "rx-pkts-over-sized"):
                        self.rx_pkts_over_sized = value
                        self.rx_pkts_over_sized.value_namespace = name_space
                        self.rx_pkts_over_sized.value_namespace_prefix = name_space_prefix
                    if(value_path == "rx-pkts-under-sized"):
                        self.rx_pkts_under_sized = value
                        self.rx_pkts_under_sized.value_namespace = name_space
                        self.rx_pkts_under_sized.value_namespace_prefix = name_space_prefix
                    if(value_path == "rx-pkts-unicast"):
                        self.rx_pkts_unicast = value
                        self.rx_pkts_unicast.value_namespace = name_space
                        self.rx_pkts_unicast.value_namespace_prefix = name_space_prefix
                    if(value_path == "rx-recv-fragments"):
                        self.rx_recv_fragments = value
                        self.rx_recv_fragments.value_namespace = name_space
                        self.rx_recv_fragments.value_namespace_prefix = name_space_prefix
                    if(value_path == "rx-total-bytes"):
                        self.rx_total_bytes = value
                        self.rx_total_bytes.value_namespace = name_space
                        self.rx_total_bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "tx-bad-fcs"):
                        self.tx_bad_fcs = value
                        self.tx_bad_fcs.value_namespace = name_space
                        self.tx_bad_fcs.value_namespace_prefix = name_space_prefix
                    if(value_path == "tx-bytes-good"):
                        self.tx_bytes_good = value
                        self.tx_bytes_good.value_namespace = name_space
                        self.tx_bytes_good.value_namespace_prefix = name_space_prefix
                    if(value_path == "tx-fragments"):
                        self.tx_fragments = value
                        self.tx_fragments.value_namespace = name_space
                        self.tx_fragments.value_namespace_prefix = name_space_prefix
                    if(value_path == "tx-jabber"):
                        self.tx_jabber = value
                        self.tx_jabber.value_namespace = name_space
                        self.tx_jabber.value_namespace_prefix = name_space_prefix
                    if(value_path == "tx-packets"):
                        self.tx_packets = value
                        self.tx_packets.value_namespace = name_space
                        self.tx_packets.value_namespace_prefix = name_space_prefix
                    if(value_path == "tx-pause"):
                        self.tx_pause = value
                        self.tx_pause.value_namespace = name_space
                        self.tx_pause.value_namespace_prefix = name_space_prefix
                    if(value_path == "tx-pkts-good"):
                        self.tx_pkts_good = value
                        self.tx_pkts_good.value_namespace = name_space
                        self.tx_pkts_good.value_namespace_prefix = name_space_prefix
                    if(value_path == "tx-pkts-over-sized"):
                        self.tx_pkts_over_sized = value
                        self.tx_pkts_over_sized.value_namespace = name_space
                        self.tx_pkts_over_sized.value_namespace_prefix = name_space_prefix
                    if(value_path == "tx-pkts-under-sized"):
                        self.tx_pkts_under_sized = value
                        self.tx_pkts_under_sized.value_namespace = name_space
                        self.tx_pkts_under_sized.value_namespace_prefix = name_space_prefix
                    if(value_path == "tx-total-bytes"):
                        self.tx_total_bytes = value
                        self.tx_total_bytes.value_namespace = name_space
                        self.tx_total_bytes.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.name.is_set or
                    self.headless_end_time.is_set or
                    self.headless_start_time.is_set or
                    self.started_stateful.is_set or
                    (self.ether_statistics is not None and self.ether_statistics.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    self.headless_end_time.yfilter != YFilter.not_set or
                    self.headless_start_time.yfilter != YFilter.not_set or
                    self.started_stateful.yfilter != YFilter.not_set or
                    (self.ether_statistics is not None and self.ether_statistics.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ethernet-port-name" + "[name='" + self.name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ncs1k-mxp-headless-oper:headless-func-data/ethernet-port-names/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())
                if (self.headless_end_time.is_set or self.headless_end_time.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.headless_end_time.get_name_leafdata())
                if (self.headless_start_time.is_set or self.headless_start_time.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.headless_start_time.get_name_leafdata())
                if (self.started_stateful.is_set or self.started_stateful.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.started_stateful.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "ether-statistics"):
                    if (self.ether_statistics is None):
                        self.ether_statistics = HeadlessFuncData.EthernetPortNames.EthernetPortName.EtherStatistics()
                        self.ether_statistics.parent = self
                        self._children_name_map["ether_statistics"] = "ether-statistics"
                    return self.ether_statistics

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ether-statistics" or name == "name" or name == "headless-end-time" or name == "headless-start-time" or name == "started-stateful"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix
                if(value_path == "headless-end-time"):
                    self.headless_end_time = value
                    self.headless_end_time.value_namespace = name_space
                    self.headless_end_time.value_namespace_prefix = name_space_prefix
                if(value_path == "headless-start-time"):
                    self.headless_start_time = value
                    self.headless_start_time.value_namespace = name_space
                    self.headless_start_time.value_namespace_prefix = name_space_prefix
                if(value_path == "started-stateful"):
                    self.started_stateful = value
                    self.started_stateful.value_namespace = name_space
                    self.started_stateful.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ethernet_port_name:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ethernet_port_name:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ethernet-port-names" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ncs1k-mxp-headless-oper:headless-func-data/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ethernet-port-name"):
                for c in self.ethernet_port_name:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = HeadlessFuncData.EthernetPortNames.EthernetPortName()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ethernet_port_name.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ethernet-port-name"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.ethernet_port_names is not None and self.ethernet_port_names.has_data()) or
            (self.otn_port_names is not None and self.otn_port_names.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.ethernet_port_names is not None and self.ethernet_port_names.has_operation()) or
            (self.otn_port_names is not None and self.otn_port_names.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ncs1k-mxp-headless-oper:headless-func-data" + path_buffer

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

        if (child_yang_name == "ethernet-port-names"):
            if (self.ethernet_port_names is None):
                self.ethernet_port_names = HeadlessFuncData.EthernetPortNames()
                self.ethernet_port_names.parent = self
                self._children_name_map["ethernet_port_names"] = "ethernet-port-names"
            return self.ethernet_port_names

        if (child_yang_name == "otn-port-names"):
            if (self.otn_port_names is None):
                self.otn_port_names = HeadlessFuncData.OtnPortNames()
                self.otn_port_names.parent = self
                self._children_name_map["otn_port_names"] = "otn-port-names"
            return self.otn_port_names

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "ethernet-port-names" or name == "otn-port-names"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = HeadlessFuncData()
        return self._top_entity


""" Cisco_IOS_XE_diffserv_target_oper 

This module contains a collection of YANG definitions for
Diffserv operational dataCopyright (c) 2017 by Cisco Systems, Inc.All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Direction(Identity):
    """
    This is identity of traffic direction
    
    

    """

    _prefix = 'diffserv-target-oper'
    _revision = '2017-02-09'

    def __init__(self):
        super(Direction, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-diffserv-target-oper", "Cisco-IOS-XE-diffserv-target-oper", "Cisco-IOS-XE-diffserv-target-oper:direction")


class DiffservInterfacesState(Entity):
    """
    Interface configuration parameters.
    
    .. attribute:: diffserv_interface
    
    	The list of configured interfaces on the device
    	**type**\: list of    :py:class:`DiffservInterface <ydk.models.cisco_ios_xe.Cisco_IOS_XE_diffserv_target_oper.DiffservInterfacesState.DiffservInterface>`
    
    

    """

    _prefix = 'diffserv-target-oper'
    _revision = '2017-02-09'

    def __init__(self):
        super(DiffservInterfacesState, self).__init__()
        self._top_entity = None

        self.yang_name = "diffserv-interfaces-state"
        self.yang_parent_name = "Cisco-IOS-XE-diffserv-target-oper"

        self.diffserv_interface = YList(self)

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
                    super(DiffservInterfacesState, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(DiffservInterfacesState, self).__setattr__(name, value)


    class DiffservInterface(Entity):
        """
        The list of configured interfaces on the device.
        
        .. attribute:: name  <key>
        
        	The name of the interface
        	**type**\:  str
        
        .. attribute:: diffserv_target_entry
        
        	policy target for inbound or outbound direction
        	**type**\: list of    :py:class:`DiffservTargetEntry <ydk.models.cisco_ios_xe.Cisco_IOS_XE_diffserv_target_oper.DiffservInterfacesState.DiffservInterface.DiffservTargetEntry>`
        
        

        """

        _prefix = 'diffserv-target-oper'
        _revision = '2017-02-09'

        def __init__(self):
            super(DiffservInterfacesState.DiffservInterface, self).__init__()

            self.yang_name = "diffserv-interface"
            self.yang_parent_name = "diffserv-interfaces-state"

            self.name = YLeaf(YType.str, "name")

            self.diffserv_target_entry = YList(self)

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
                        super(DiffservInterfacesState.DiffservInterface, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DiffservInterfacesState.DiffservInterface, self).__setattr__(name, value)


        class DiffservTargetEntry(Entity):
            """
            policy target for inbound or outbound direction
            
            .. attribute:: direction  <key>
            
            	Direction fo the traffic flow either inbound or outbound
            	**type**\:   :py:class:`Direction <ydk.models.cisco_ios_xe.Cisco_IOS_XE_diffserv_target_oper.Direction>`
            
            .. attribute:: policy_name  <key>
            
            	Policy entry name
            	**type**\:  str
            
            .. attribute:: diffserv_target_classifier_statistics
            
            	Statistics for each Classifier Entry in a Policy
            	**type**\: list of    :py:class:`DiffservTargetClassifierStatistics <ydk.models.cisco_ios_xe.Cisco_IOS_XE_diffserv_target_oper.DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics>`
            
            

            """

            _prefix = 'diffserv-target-oper'
            _revision = '2017-02-09'

            def __init__(self):
                super(DiffservInterfacesState.DiffservInterface.DiffservTargetEntry, self).__init__()

                self.yang_name = "diffserv-target-entry"
                self.yang_parent_name = "diffserv-interface"

                self.direction = YLeaf(YType.identityref, "direction")

                self.policy_name = YLeaf(YType.str, "policy-name")

                self.diffserv_target_classifier_statistics = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("direction",
                                "policy_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(DiffservInterfacesState.DiffservInterface.DiffservTargetEntry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(DiffservInterfacesState.DiffservInterface.DiffservTargetEntry, self).__setattr__(name, value)


            class DiffservTargetClassifierStatistics(Entity):
                """
                Statistics for each Classifier Entry in a Policy
                
                .. attribute:: classifier_entry_name  <key>
                
                	Classifier Entry Name
                	**type**\:  str
                
                .. attribute:: parent_path  <key>
                
                	Path of the Classifier Entry in a hierarchial policy 
                	**type**\:  str
                
                .. attribute:: classifier_entry_statistics
                
                	 This group defines the classifier filter statistics of  each classifier entry         
                	**type**\:   :py:class:`ClassifierEntryStatistics <ydk.models.cisco_ios_xe.Cisco_IOS_XE_diffserv_target_oper.DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.ClassifierEntryStatistics>`
                
                .. attribute:: meter_statistics
                
                	Meter statistics
                	**type**\: list of    :py:class:`MeterStatistics <ydk.models.cisco_ios_xe.Cisco_IOS_XE_diffserv_target_oper.DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.MeterStatistics>`
                
                .. attribute:: queuing_statistics
                
                	queue related statistics 
                	**type**\:   :py:class:`QueuingStatistics <ydk.models.cisco_ios_xe.Cisco_IOS_XE_diffserv_target_oper.DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics>`
                
                

                """

                _prefix = 'diffserv-target-oper'
                _revision = '2017-02-09'

                def __init__(self):
                    super(DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics, self).__init__()

                    self.yang_name = "diffserv-target-classifier-statistics"
                    self.yang_parent_name = "diffserv-target-entry"

                    self.classifier_entry_name = YLeaf(YType.str, "classifier-entry-name")

                    self.parent_path = YLeaf(YType.str, "parent-path")

                    self.classifier_entry_statistics = DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.ClassifierEntryStatistics()
                    self.classifier_entry_statistics.parent = self
                    self._children_name_map["classifier_entry_statistics"] = "classifier-entry-statistics"
                    self._children_yang_names.add("classifier-entry-statistics")

                    self.queuing_statistics = DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics()
                    self.queuing_statistics.parent = self
                    self._children_name_map["queuing_statistics"] = "queuing-statistics"
                    self._children_yang_names.add("queuing-statistics")

                    self.meter_statistics = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("classifier_entry_name",
                                    "parent_path") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics, self).__setattr__(name, value)


                class ClassifierEntryStatistics(Entity):
                    """
                    
                    This group defines the classifier filter statistics of 
                    each classifier entry
                           
                    
                    
                    .. attribute:: classified_bytes
                    
                    	 Number of total bytes which filtered   to the classifier\-entry
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: classified_pkts
                    
                    	 Number of total packets which filtered  to the classifier\-entry
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: classified_rate
                    
                    	 Rate of average data flow through the   classifier\-entry
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: bits-per-second
                    
                    

                    """

                    _prefix = 'diffserv-target-oper'
                    _revision = '2017-02-09'

                    def __init__(self):
                        super(DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.ClassifierEntryStatistics, self).__init__()

                        self.yang_name = "classifier-entry-statistics"
                        self.yang_parent_name = "diffserv-target-classifier-statistics"

                        self.classified_bytes = YLeaf(YType.uint64, "classified-bytes")

                        self.classified_pkts = YLeaf(YType.uint64, "classified-pkts")

                        self.classified_rate = YLeaf(YType.uint64, "classified-rate")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("classified_bytes",
                                        "classified_pkts",
                                        "classified_rate") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.ClassifierEntryStatistics, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.ClassifierEntryStatistics, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.classified_bytes.is_set or
                            self.classified_pkts.is_set or
                            self.classified_rate.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.classified_bytes.yfilter != YFilter.not_set or
                            self.classified_pkts.yfilter != YFilter.not_set or
                            self.classified_rate.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "classifier-entry-statistics" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.classified_bytes.is_set or self.classified_bytes.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.classified_bytes.get_name_leafdata())
                        if (self.classified_pkts.is_set or self.classified_pkts.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.classified_pkts.get_name_leafdata())
                        if (self.classified_rate.is_set or self.classified_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.classified_rate.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "classified-bytes" or name == "classified-pkts" or name == "classified-rate"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "classified-bytes"):
                            self.classified_bytes = value
                            self.classified_bytes.value_namespace = name_space
                            self.classified_bytes.value_namespace_prefix = name_space_prefix
                        if(value_path == "classified-pkts"):
                            self.classified_pkts = value
                            self.classified_pkts.value_namespace = name_space
                            self.classified_pkts.value_namespace_prefix = name_space_prefix
                        if(value_path == "classified-rate"):
                            self.classified_rate = value
                            self.classified_rate.value_namespace = name_space
                            self.classified_rate.value_namespace_prefix = name_space_prefix


                class MeterStatistics(Entity):
                    """
                    Meter statistics
                    
                    .. attribute:: meter_id  <key>
                    
                    	Meter Identifier
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: meter_failed_bytes
                    
                    	Bytes of packets which failed the meter
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: meter_failed_pkts
                    
                    	Number of packets which failed the meter
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: meter_succeed_bytes
                    
                    	Bytes of packets which succeed the meter
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: meter_succeed_pkts
                    
                    	Number of packets which succeed the meter
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'diffserv-target-oper'
                    _revision = '2017-02-09'

                    def __init__(self):
                        super(DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.MeterStatistics, self).__init__()

                        self.yang_name = "meter-statistics"
                        self.yang_parent_name = "diffserv-target-classifier-statistics"

                        self.meter_id = YLeaf(YType.uint16, "meter-id")

                        self.meter_failed_bytes = YLeaf(YType.uint64, "meter-failed-bytes")

                        self.meter_failed_pkts = YLeaf(YType.uint64, "meter-failed-pkts")

                        self.meter_succeed_bytes = YLeaf(YType.uint64, "meter-succeed-bytes")

                        self.meter_succeed_pkts = YLeaf(YType.uint64, "meter-succeed-pkts")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("meter_id",
                                        "meter_failed_bytes",
                                        "meter_failed_pkts",
                                        "meter_succeed_bytes",
                                        "meter_succeed_pkts") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.MeterStatistics, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.MeterStatistics, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.meter_id.is_set or
                            self.meter_failed_bytes.is_set or
                            self.meter_failed_pkts.is_set or
                            self.meter_succeed_bytes.is_set or
                            self.meter_succeed_pkts.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.meter_id.yfilter != YFilter.not_set or
                            self.meter_failed_bytes.yfilter != YFilter.not_set or
                            self.meter_failed_pkts.yfilter != YFilter.not_set or
                            self.meter_succeed_bytes.yfilter != YFilter.not_set or
                            self.meter_succeed_pkts.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "meter-statistics" + "[meter-id='" + self.meter_id.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.meter_id.is_set or self.meter_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.meter_id.get_name_leafdata())
                        if (self.meter_failed_bytes.is_set or self.meter_failed_bytes.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.meter_failed_bytes.get_name_leafdata())
                        if (self.meter_failed_pkts.is_set or self.meter_failed_pkts.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.meter_failed_pkts.get_name_leafdata())
                        if (self.meter_succeed_bytes.is_set or self.meter_succeed_bytes.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.meter_succeed_bytes.get_name_leafdata())
                        if (self.meter_succeed_pkts.is_set or self.meter_succeed_pkts.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.meter_succeed_pkts.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "meter-id" or name == "meter-failed-bytes" or name == "meter-failed-pkts" or name == "meter-succeed-bytes" or name == "meter-succeed-pkts"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "meter-id"):
                            self.meter_id = value
                            self.meter_id.value_namespace = name_space
                            self.meter_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "meter-failed-bytes"):
                            self.meter_failed_bytes = value
                            self.meter_failed_bytes.value_namespace = name_space
                            self.meter_failed_bytes.value_namespace_prefix = name_space_prefix
                        if(value_path == "meter-failed-pkts"):
                            self.meter_failed_pkts = value
                            self.meter_failed_pkts.value_namespace = name_space
                            self.meter_failed_pkts.value_namespace_prefix = name_space_prefix
                        if(value_path == "meter-succeed-bytes"):
                            self.meter_succeed_bytes = value
                            self.meter_succeed_bytes.value_namespace = name_space
                            self.meter_succeed_bytes.value_namespace_prefix = name_space_prefix
                        if(value_path == "meter-succeed-pkts"):
                            self.meter_succeed_pkts = value
                            self.meter_succeed_pkts.value_namespace = name_space
                            self.meter_succeed_pkts.value_namespace_prefix = name_space_prefix


                class QueuingStatistics(Entity):
                    """
                    queue related statistics 
                    
                    .. attribute:: drop_bytes
                    
                    	Total number of bytes dropped 
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: drop_pkts
                    
                    	Total number of packets dropped 
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: output_bytes
                    
                    	Number of bytes transmitted from queue 
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: output_pkts
                    
                    	Number of packets transmitted from queue 
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: queue_size_bytes
                    
                    	Number of bytes currently buffered 
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: queue_size_pkts
                    
                    	Number of packets currently buffered 
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: wred_stats
                    
                    	Container for WRED statistics
                    	**type**\:   :py:class:`WredStats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_diffserv_target_oper.DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics.WredStats>`
                    
                    

                    """

                    _prefix = 'diffserv-target-oper'
                    _revision = '2017-02-09'

                    def __init__(self):
                        super(DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics, self).__init__()

                        self.yang_name = "queuing-statistics"
                        self.yang_parent_name = "diffserv-target-classifier-statistics"

                        self.drop_bytes = YLeaf(YType.uint64, "drop-bytes")

                        self.drop_pkts = YLeaf(YType.uint64, "drop-pkts")

                        self.output_bytes = YLeaf(YType.uint64, "output-bytes")

                        self.output_pkts = YLeaf(YType.uint64, "output-pkts")

                        self.queue_size_bytes = YLeaf(YType.uint64, "queue-size-bytes")

                        self.queue_size_pkts = YLeaf(YType.uint64, "queue-size-pkts")

                        self.wred_stats = DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics.WredStats()
                        self.wred_stats.parent = self
                        self._children_name_map["wred_stats"] = "wred-stats"
                        self._children_yang_names.add("wred-stats")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("drop_bytes",
                                        "drop_pkts",
                                        "output_bytes",
                                        "output_pkts",
                                        "queue_size_bytes",
                                        "queue_size_pkts") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics, self).__setattr__(name, value)


                    class WredStats(Entity):
                        """
                        Container for WRED statistics
                        
                        .. attribute:: early_drop_bytes
                        
                        	Early drop bytes 
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: early_drop_pkts
                        
                        	Early drop packets 
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'diffserv-target-oper'
                        _revision = '2017-02-09'

                        def __init__(self):
                            super(DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics.WredStats, self).__init__()

                            self.yang_name = "wred-stats"
                            self.yang_parent_name = "queuing-statistics"

                            self.early_drop_bytes = YLeaf(YType.uint64, "early-drop-bytes")

                            self.early_drop_pkts = YLeaf(YType.uint64, "early-drop-pkts")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("early_drop_bytes",
                                            "early_drop_pkts") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics.WredStats, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics.WredStats, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.early_drop_bytes.is_set or
                                self.early_drop_pkts.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.early_drop_bytes.yfilter != YFilter.not_set or
                                self.early_drop_pkts.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "wred-stats" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.early_drop_bytes.is_set or self.early_drop_bytes.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.early_drop_bytes.get_name_leafdata())
                            if (self.early_drop_pkts.is_set or self.early_drop_pkts.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.early_drop_pkts.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "early-drop-bytes" or name == "early-drop-pkts"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "early-drop-bytes"):
                                self.early_drop_bytes = value
                                self.early_drop_bytes.value_namespace = name_space
                                self.early_drop_bytes.value_namespace_prefix = name_space_prefix
                            if(value_path == "early-drop-pkts"):
                                self.early_drop_pkts = value
                                self.early_drop_pkts.value_namespace = name_space
                                self.early_drop_pkts.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.drop_bytes.is_set or
                            self.drop_pkts.is_set or
                            self.output_bytes.is_set or
                            self.output_pkts.is_set or
                            self.queue_size_bytes.is_set or
                            self.queue_size_pkts.is_set or
                            (self.wred_stats is not None and self.wred_stats.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.drop_bytes.yfilter != YFilter.not_set or
                            self.drop_pkts.yfilter != YFilter.not_set or
                            self.output_bytes.yfilter != YFilter.not_set or
                            self.output_pkts.yfilter != YFilter.not_set or
                            self.queue_size_bytes.yfilter != YFilter.not_set or
                            self.queue_size_pkts.yfilter != YFilter.not_set or
                            (self.wred_stats is not None and self.wred_stats.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "queuing-statistics" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.drop_bytes.is_set or self.drop_bytes.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.drop_bytes.get_name_leafdata())
                        if (self.drop_pkts.is_set or self.drop_pkts.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.drop_pkts.get_name_leafdata())
                        if (self.output_bytes.is_set or self.output_bytes.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_bytes.get_name_leafdata())
                        if (self.output_pkts.is_set or self.output_pkts.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_pkts.get_name_leafdata())
                        if (self.queue_size_bytes.is_set or self.queue_size_bytes.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.queue_size_bytes.get_name_leafdata())
                        if (self.queue_size_pkts.is_set or self.queue_size_pkts.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.queue_size_pkts.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "wred-stats"):
                            if (self.wred_stats is None):
                                self.wred_stats = DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics.WredStats()
                                self.wred_stats.parent = self
                                self._children_name_map["wred_stats"] = "wred-stats"
                            return self.wred_stats

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "wred-stats" or name == "drop-bytes" or name == "drop-pkts" or name == "output-bytes" or name == "output-pkts" or name == "queue-size-bytes" or name == "queue-size-pkts"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "drop-bytes"):
                            self.drop_bytes = value
                            self.drop_bytes.value_namespace = name_space
                            self.drop_bytes.value_namespace_prefix = name_space_prefix
                        if(value_path == "drop-pkts"):
                            self.drop_pkts = value
                            self.drop_pkts.value_namespace = name_space
                            self.drop_pkts.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-bytes"):
                            self.output_bytes = value
                            self.output_bytes.value_namespace = name_space
                            self.output_bytes.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-pkts"):
                            self.output_pkts = value
                            self.output_pkts.value_namespace = name_space
                            self.output_pkts.value_namespace_prefix = name_space_prefix
                        if(value_path == "queue-size-bytes"):
                            self.queue_size_bytes = value
                            self.queue_size_bytes.value_namespace = name_space
                            self.queue_size_bytes.value_namespace_prefix = name_space_prefix
                        if(value_path == "queue-size-pkts"):
                            self.queue_size_pkts = value
                            self.queue_size_pkts.value_namespace = name_space
                            self.queue_size_pkts.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.meter_statistics:
                        if (c.has_data()):
                            return True
                    return (
                        self.classifier_entry_name.is_set or
                        self.parent_path.is_set or
                        (self.classifier_entry_statistics is not None and self.classifier_entry_statistics.has_data()) or
                        (self.queuing_statistics is not None and self.queuing_statistics.has_data()))

                def has_operation(self):
                    for c in self.meter_statistics:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.classifier_entry_name.yfilter != YFilter.not_set or
                        self.parent_path.yfilter != YFilter.not_set or
                        (self.classifier_entry_statistics is not None and self.classifier_entry_statistics.has_operation()) or
                        (self.queuing_statistics is not None and self.queuing_statistics.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "diffserv-target-classifier-statistics" + "[classifier-entry-name='" + self.classifier_entry_name.get() + "']" + "[parent-path='" + self.parent_path.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.classifier_entry_name.is_set or self.classifier_entry_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.classifier_entry_name.get_name_leafdata())
                    if (self.parent_path.is_set or self.parent_path.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.parent_path.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "classifier-entry-statistics"):
                        if (self.classifier_entry_statistics is None):
                            self.classifier_entry_statistics = DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.ClassifierEntryStatistics()
                            self.classifier_entry_statistics.parent = self
                            self._children_name_map["classifier_entry_statistics"] = "classifier-entry-statistics"
                        return self.classifier_entry_statistics

                    if (child_yang_name == "meter-statistics"):
                        for c in self.meter_statistics:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.MeterStatistics()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.meter_statistics.append(c)
                        return c

                    if (child_yang_name == "queuing-statistics"):
                        if (self.queuing_statistics is None):
                            self.queuing_statistics = DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics()
                            self.queuing_statistics.parent = self
                            self._children_name_map["queuing_statistics"] = "queuing-statistics"
                        return self.queuing_statistics

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "classifier-entry-statistics" or name == "meter-statistics" or name == "queuing-statistics" or name == "classifier-entry-name" or name == "parent-path"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "classifier-entry-name"):
                        self.classifier_entry_name = value
                        self.classifier_entry_name.value_namespace = name_space
                        self.classifier_entry_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "parent-path"):
                        self.parent_path = value
                        self.parent_path.value_namespace = name_space
                        self.parent_path.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.diffserv_target_classifier_statistics:
                    if (c.has_data()):
                        return True
                return (
                    self.direction.is_set or
                    self.policy_name.is_set)

            def has_operation(self):
                for c in self.diffserv_target_classifier_statistics:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.direction.yfilter != YFilter.not_set or
                    self.policy_name.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "diffserv-target-entry" + "[direction='" + self.direction.get() + "']" + "[policy-name='" + self.policy_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.direction.is_set or self.direction.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.direction.get_name_leafdata())
                if (self.policy_name.is_set or self.policy_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.policy_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "diffserv-target-classifier-statistics"):
                    for c in self.diffserv_target_classifier_statistics:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.diffserv_target_classifier_statistics.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "diffserv-target-classifier-statistics" or name == "direction" or name == "policy-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "direction"):
                    self.direction = value
                    self.direction.value_namespace = name_space
                    self.direction.value_namespace_prefix = name_space_prefix
                if(value_path == "policy-name"):
                    self.policy_name = value
                    self.policy_name.value_namespace = name_space
                    self.policy_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.diffserv_target_entry:
                if (c.has_data()):
                    return True
            return self.name.is_set

        def has_operation(self):
            for c in self.diffserv_target_entry:
                if (c.has_operation()):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.name.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "diffserv-interface" + "[name='" + self.name.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XE-diffserv-target-oper:diffserv-interfaces-state/%s" % self.get_segment_path()
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

            if (child_yang_name == "diffserv-target-entry"):
                for c in self.diffserv_target_entry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = DiffservInterfacesState.DiffservInterface.DiffservTargetEntry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.diffserv_target_entry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "diffserv-target-entry" or name == "name"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "name"):
                self.name = value
                self.name.value_namespace = name_space
                self.name.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.diffserv_interface:
            if (c.has_data()):
                return True
        return False

    def has_operation(self):
        for c in self.diffserv_interface:
            if (c.has_operation()):
                return True
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XE-diffserv-target-oper:diffserv-interfaces-state" + path_buffer

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

        if (child_yang_name == "diffserv-interface"):
            for c in self.diffserv_interface:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = DiffservInterfacesState.DiffservInterface()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.diffserv_interface.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "diffserv-interface"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = DiffservInterfacesState()
        return self._top_entity

class Outbound(Identity):
    """
    Direction of traffic going out of the network entry
    
    

    """

    _prefix = 'diffserv-target-oper'
    _revision = '2017-02-09'

    def __init__(self):
        super(Outbound, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-diffserv-target-oper", "Cisco-IOS-XE-diffserv-target-oper", "Cisco-IOS-XE-diffserv-target-oper:outbound")


class Inbound(Identity):
    """
    Direction of traffic coming into the network entry
    
    

    """

    _prefix = 'diffserv-target-oper'
    _revision = '2017-02-09'

    def __init__(self):
        super(Inbound, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-diffserv-target-oper", "Cisco-IOS-XE-diffserv-target-oper", "Cisco-IOS-XE-diffserv-target-oper:inbound")



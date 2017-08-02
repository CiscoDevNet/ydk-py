""" ietf_diffserv_classifier 

This module contains a collection of YANG definitions for
configuring diffserv specification implementations.

Copyright (c) 2014 IETF Trust and the persons identified as
authors of the code.  All rights reserved.

Redistribution and use in source and binary forms, with or
without modification, is permitted pursuant to, and subject
to the license terms contained in, the Simplified BSD License
set forth in Section 4.c of the IETF Trust's Legal Provisions
Relating to IETF Documents
(http\://trustee.ietf.org/license\-info).

This version of this YANG module is part of RFC XXXX; see
the RFC itself for full legal notices.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class FilterType(Identity):
    """
     This is identity of base filter\-type
    
    

    """

    _prefix = 'classifier'
    _revision = '2015-04-07'

    def __init__(self):
        super(FilterType, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-classifier", "ietf-diffserv-classifier", "ietf-diffserv-classifier:filter-type")


class ClassifierEntryFilterOperationType(Identity):
    """
    Classifier entry filter logical operation
    
    

    """

    _prefix = 'classifier'
    _revision = '2015-04-07'

    def __init__(self):
        super(ClassifierEntryFilterOperationType, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-classifier", "ietf-diffserv-classifier", "ietf-diffserv-classifier:classifier-entry-filter-operation-type")


class Classifiers(Entity):
    """
    list of classifier entry
    
    .. attribute:: classifier_entry
    
    	classifier entry template
    	**type**\: list of    :py:class:`ClassifierEntry <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry>`
    
    

    """

    _prefix = 'classifier'
    _revision = '2015-04-07'

    def __init__(self):
        super(Classifiers, self).__init__()
        self._top_entity = None

        self.yang_name = "classifiers"
        self.yang_parent_name = "ietf-diffserv-classifier"

        self.classifier_entry = YList(self)

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
                    super(Classifiers, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Classifiers, self).__setattr__(name, value)


    class ClassifierEntry(Entity):
        """
        classifier entry template
        
        .. attribute:: classifier_entry_name  <key>
        
        	Diffserv classifier name
        	**type**\:  str
        
        .. attribute:: classifier_entry_descr
        
        	Description of the class template
        	**type**\:  str
        
        .. attribute:: classifier_entry_filter_operation
        
        	Filters are applicable as any or all filters
        	**type**\:   :py:class:`ClassifierEntryFilterOperationType <ydk.models.ietf.ietf_diffserv_classifier.ClassifierEntryFilterOperationType>`
        
        	**default value**\: match-any-filter
        
        .. attribute:: filter_entry
        
        	Filter configuration
        	**type**\: list of    :py:class:`FilterEntry <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry>`
        
        

        """

        _prefix = 'classifier'
        _revision = '2015-04-07'

        def __init__(self):
            super(Classifiers.ClassifierEntry, self).__init__()

            self.yang_name = "classifier-entry"
            self.yang_parent_name = "classifiers"

            self.classifier_entry_name = YLeaf(YType.str, "classifier-entry-name")

            self.classifier_entry_descr = YLeaf(YType.str, "classifier-entry-descr")

            self.classifier_entry_filter_operation = YLeaf(YType.identityref, "classifier-entry-filter-operation")

            self.filter_entry = YList(self)

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
                            "classifier_entry_descr",
                            "classifier_entry_filter_operation") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Classifiers.ClassifierEntry, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Classifiers.ClassifierEntry, self).__setattr__(name, value)


        class FilterEntry(Entity):
            """
            Filter configuration
            
            .. attribute:: filter_type  <key>
            
            	This leaf defines type of the filter
            	**type**\:   :py:class:`FilterType <ydk.models.ietf.ietf_diffserv_classifier.FilterType>`
            
            .. attribute:: filter_logical_not  <key>
            
            	 This is logical\-not operator for a filter. When true, it  indicates filter looks for absence of a pattern defined  by the filter 
            	**type**\:  bool
            
            .. attribute:: destination_ip_address_cfg
            
            	list of destination ip address
            	**type**\: list of    :py:class:`DestinationIpAddressCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.DestinationIpAddressCfg>`
            
            .. attribute:: destination_port_cfg
            
            	list of ranges of destination port
            	**type**\: list of    :py:class:`DestinationPortCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.DestinationPortCfg>`
            
            .. attribute:: dscp_cfg
            
            	list of dscp ranges
            	**type**\: list of    :py:class:`DscpCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.DscpCfg>`
            
            .. attribute:: protocol_cfg
            
            	list of ranges of protocol values
            	**type**\: list of    :py:class:`ProtocolCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.ProtocolCfg>`
            
            .. attribute:: source_ip_address_cfg
            
            	list of source ip address
            	**type**\: list of    :py:class:`SourceIpAddressCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.SourceIpAddressCfg>`
            
            .. attribute:: source_port_cfg
            
            	list of ranges of source port
            	**type**\: list of    :py:class:`SourcePortCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.SourcePortCfg>`
            
            

            """

            _prefix = 'classifier'
            _revision = '2015-04-07'

            def __init__(self):
                super(Classifiers.ClassifierEntry.FilterEntry, self).__init__()

                self.yang_name = "filter-entry"
                self.yang_parent_name = "classifier-entry"

                self.filter_type = YLeaf(YType.identityref, "filter-type")

                self.filter_logical_not = YLeaf(YType.boolean, "filter-logical-not")

                self.destination_ip_address_cfg = YList(self)
                self.destination_port_cfg = YList(self)
                self.dscp_cfg = YList(self)
                self.protocol_cfg = YList(self)
                self.source_ip_address_cfg = YList(self)
                self.source_port_cfg = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("filter_type",
                                "filter_logical_not") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Classifiers.ClassifierEntry.FilterEntry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Classifiers.ClassifierEntry.FilterEntry, self).__setattr__(name, value)


            class DscpCfg(Entity):
                """
                list of dscp ranges
                
                .. attribute:: dscp_min  <key>
                
                	Minimum value of dscp range
                	**type**\:  int
                
                	**range:** 0..63
                
                .. attribute:: dscp_max  <key>
                
                	maximum value of dscp range
                	**type**\:  int
                
                	**range:** 0..63
                
                

                """

                _prefix = 'classifier'
                _revision = '2015-04-07'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.DscpCfg, self).__init__()

                    self.yang_name = "dscp-cfg"
                    self.yang_parent_name = "filter-entry"

                    self.dscp_min = YLeaf(YType.uint8, "dscp-min")

                    self.dscp_max = YLeaf(YType.uint8, "dscp-max")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("dscp_min",
                                    "dscp_max") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Classifiers.ClassifierEntry.FilterEntry.DscpCfg, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Classifiers.ClassifierEntry.FilterEntry.DscpCfg, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.dscp_min.is_set or
                        self.dscp_max.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.dscp_min.yfilter != YFilter.not_set or
                        self.dscp_max.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "dscp-cfg" + "[dscp-min='" + self.dscp_min.get() + "']" + "[dscp-max='" + self.dscp_max.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.dscp_min.is_set or self.dscp_min.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dscp_min.get_name_leafdata())
                    if (self.dscp_max.is_set or self.dscp_max.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dscp_max.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "dscp-min" or name == "dscp-max"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "dscp-min"):
                        self.dscp_min = value
                        self.dscp_min.value_namespace = name_space
                        self.dscp_min.value_namespace_prefix = name_space_prefix
                    if(value_path == "dscp-max"):
                        self.dscp_max = value
                        self.dscp_max.value_namespace = name_space
                        self.dscp_max.value_namespace_prefix = name_space_prefix


            class SourceIpAddressCfg(Entity):
                """
                list of source ip address
                
                .. attribute:: source_ip_addr  <key>
                
                	source ip prefix
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                
                
                ----
                

                """

                _prefix = 'classifier'
                _revision = '2015-04-07'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.SourceIpAddressCfg, self).__init__()

                    self.yang_name = "source-ip-address-cfg"
                    self.yang_parent_name = "filter-entry"

                    self.source_ip_addr = YLeaf(YType.str, "source-ip-addr")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("source_ip_addr") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Classifiers.ClassifierEntry.FilterEntry.SourceIpAddressCfg, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Classifiers.ClassifierEntry.FilterEntry.SourceIpAddressCfg, self).__setattr__(name, value)

                def has_data(self):
                    return self.source_ip_addr.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.source_ip_addr.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "source-ip-address-cfg" + "[source-ip-addr='" + self.source_ip_addr.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.source_ip_addr.is_set or self.source_ip_addr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.source_ip_addr.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "source-ip-addr"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "source-ip-addr"):
                        self.source_ip_addr = value
                        self.source_ip_addr.value_namespace = name_space
                        self.source_ip_addr.value_namespace_prefix = name_space_prefix


            class DestinationIpAddressCfg(Entity):
                """
                list of destination ip address
                
                .. attribute:: destination_ip_addr  <key>
                
                	destination ip prefix
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                
                
                ----
                

                """

                _prefix = 'classifier'
                _revision = '2015-04-07'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.DestinationIpAddressCfg, self).__init__()

                    self.yang_name = "destination-ip-address-cfg"
                    self.yang_parent_name = "filter-entry"

                    self.destination_ip_addr = YLeaf(YType.str, "destination-ip-addr")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("destination_ip_addr") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Classifiers.ClassifierEntry.FilterEntry.DestinationIpAddressCfg, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Classifiers.ClassifierEntry.FilterEntry.DestinationIpAddressCfg, self).__setattr__(name, value)

                def has_data(self):
                    return self.destination_ip_addr.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.destination_ip_addr.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "destination-ip-address-cfg" + "[destination-ip-addr='" + self.destination_ip_addr.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.destination_ip_addr.is_set or self.destination_ip_addr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.destination_ip_addr.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "destination-ip-addr"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "destination-ip-addr"):
                        self.destination_ip_addr = value
                        self.destination_ip_addr.value_namespace = name_space
                        self.destination_ip_addr.value_namespace_prefix = name_space_prefix


            class SourcePortCfg(Entity):
                """
                list of ranges of source port
                
                .. attribute:: source_port_min  <key>
                
                	minimum value of source port range
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: source_port_max  <key>
                
                	maximum value of source port range
                	**type**\:  int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'classifier'
                _revision = '2015-04-07'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.SourcePortCfg, self).__init__()

                    self.yang_name = "source-port-cfg"
                    self.yang_parent_name = "filter-entry"

                    self.source_port_min = YLeaf(YType.uint16, "source-port-min")

                    self.source_port_max = YLeaf(YType.uint16, "source-port-max")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("source_port_min",
                                    "source_port_max") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Classifiers.ClassifierEntry.FilterEntry.SourcePortCfg, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Classifiers.ClassifierEntry.FilterEntry.SourcePortCfg, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.source_port_min.is_set or
                        self.source_port_max.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.source_port_min.yfilter != YFilter.not_set or
                        self.source_port_max.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "source-port-cfg" + "[source-port-min='" + self.source_port_min.get() + "']" + "[source-port-max='" + self.source_port_max.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.source_port_min.is_set or self.source_port_min.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.source_port_min.get_name_leafdata())
                    if (self.source_port_max.is_set or self.source_port_max.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.source_port_max.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "source-port-min" or name == "source-port-max"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "source-port-min"):
                        self.source_port_min = value
                        self.source_port_min.value_namespace = name_space
                        self.source_port_min.value_namespace_prefix = name_space_prefix
                    if(value_path == "source-port-max"):
                        self.source_port_max = value
                        self.source_port_max.value_namespace = name_space
                        self.source_port_max.value_namespace_prefix = name_space_prefix


            class DestinationPortCfg(Entity):
                """
                list of ranges of destination port
                
                .. attribute:: destination_port_min  <key>
                
                	minimum value of destination port range
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: destination_port_max  <key>
                
                	maximum value of destination port range
                	**type**\:  int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'classifier'
                _revision = '2015-04-07'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.DestinationPortCfg, self).__init__()

                    self.yang_name = "destination-port-cfg"
                    self.yang_parent_name = "filter-entry"

                    self.destination_port_min = YLeaf(YType.uint16, "destination-port-min")

                    self.destination_port_max = YLeaf(YType.uint16, "destination-port-max")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("destination_port_min",
                                    "destination_port_max") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Classifiers.ClassifierEntry.FilterEntry.DestinationPortCfg, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Classifiers.ClassifierEntry.FilterEntry.DestinationPortCfg, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.destination_port_min.is_set or
                        self.destination_port_max.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.destination_port_min.yfilter != YFilter.not_set or
                        self.destination_port_max.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "destination-port-cfg" + "[destination-port-min='" + self.destination_port_min.get() + "']" + "[destination-port-max='" + self.destination_port_max.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.destination_port_min.is_set or self.destination_port_min.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.destination_port_min.get_name_leafdata())
                    if (self.destination_port_max.is_set or self.destination_port_max.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.destination_port_max.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "destination-port-min" or name == "destination-port-max"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "destination-port-min"):
                        self.destination_port_min = value
                        self.destination_port_min.value_namespace = name_space
                        self.destination_port_min.value_namespace_prefix = name_space_prefix
                    if(value_path == "destination-port-max"):
                        self.destination_port_max = value
                        self.destination_port_max.value_namespace = name_space
                        self.destination_port_max.value_namespace_prefix = name_space_prefix


            class ProtocolCfg(Entity):
                """
                list of ranges of protocol values
                
                .. attribute:: protocol_min  <key>
                
                	minimum value of protocol range
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: protocol_max  <key>
                
                	maximum value of protocol range
                	**type**\:  int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'classifier'
                _revision = '2015-04-07'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.ProtocolCfg, self).__init__()

                    self.yang_name = "protocol-cfg"
                    self.yang_parent_name = "filter-entry"

                    self.protocol_min = YLeaf(YType.uint8, "protocol-min")

                    self.protocol_max = YLeaf(YType.uint8, "protocol-max")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("protocol_min",
                                    "protocol_max") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Classifiers.ClassifierEntry.FilterEntry.ProtocolCfg, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Classifiers.ClassifierEntry.FilterEntry.ProtocolCfg, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.protocol_min.is_set or
                        self.protocol_max.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.protocol_min.yfilter != YFilter.not_set or
                        self.protocol_max.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "protocol-cfg" + "[protocol-min='" + self.protocol_min.get() + "']" + "[protocol-max='" + self.protocol_max.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.protocol_min.is_set or self.protocol_min.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.protocol_min.get_name_leafdata())
                    if (self.protocol_max.is_set or self.protocol_max.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.protocol_max.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "protocol-min" or name == "protocol-max"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "protocol-min"):
                        self.protocol_min = value
                        self.protocol_min.value_namespace = name_space
                        self.protocol_min.value_namespace_prefix = name_space_prefix
                    if(value_path == "protocol-max"):
                        self.protocol_max = value
                        self.protocol_max.value_namespace = name_space
                        self.protocol_max.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.destination_ip_address_cfg:
                    if (c.has_data()):
                        return True
                for c in self.destination_port_cfg:
                    if (c.has_data()):
                        return True
                for c in self.dscp_cfg:
                    if (c.has_data()):
                        return True
                for c in self.protocol_cfg:
                    if (c.has_data()):
                        return True
                for c in self.source_ip_address_cfg:
                    if (c.has_data()):
                        return True
                for c in self.source_port_cfg:
                    if (c.has_data()):
                        return True
                return (
                    self.filter_type.is_set or
                    self.filter_logical_not.is_set)

            def has_operation(self):
                for c in self.destination_ip_address_cfg:
                    if (c.has_operation()):
                        return True
                for c in self.destination_port_cfg:
                    if (c.has_operation()):
                        return True
                for c in self.dscp_cfg:
                    if (c.has_operation()):
                        return True
                for c in self.protocol_cfg:
                    if (c.has_operation()):
                        return True
                for c in self.source_ip_address_cfg:
                    if (c.has_operation()):
                        return True
                for c in self.source_port_cfg:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.filter_type.yfilter != YFilter.not_set or
                    self.filter_logical_not.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "filter-entry" + "[filter-type='" + self.filter_type.get() + "']" + "[filter-logical-not='" + self.filter_logical_not.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.filter_type.is_set or self.filter_type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.filter_type.get_name_leafdata())
                if (self.filter_logical_not.is_set or self.filter_logical_not.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.filter_logical_not.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "destination-ip-address-cfg"):
                    for c in self.destination_ip_address_cfg:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Classifiers.ClassifierEntry.FilterEntry.DestinationIpAddressCfg()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.destination_ip_address_cfg.append(c)
                    return c

                if (child_yang_name == "destination-port-cfg"):
                    for c in self.destination_port_cfg:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Classifiers.ClassifierEntry.FilterEntry.DestinationPortCfg()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.destination_port_cfg.append(c)
                    return c

                if (child_yang_name == "dscp-cfg"):
                    for c in self.dscp_cfg:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Classifiers.ClassifierEntry.FilterEntry.DscpCfg()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.dscp_cfg.append(c)
                    return c

                if (child_yang_name == "protocol-cfg"):
                    for c in self.protocol_cfg:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Classifiers.ClassifierEntry.FilterEntry.ProtocolCfg()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.protocol_cfg.append(c)
                    return c

                if (child_yang_name == "source-ip-address-cfg"):
                    for c in self.source_ip_address_cfg:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Classifiers.ClassifierEntry.FilterEntry.SourceIpAddressCfg()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.source_ip_address_cfg.append(c)
                    return c

                if (child_yang_name == "source-port-cfg"):
                    for c in self.source_port_cfg:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Classifiers.ClassifierEntry.FilterEntry.SourcePortCfg()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.source_port_cfg.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "destination-ip-address-cfg" or name == "destination-port-cfg" or name == "dscp-cfg" or name == "protocol-cfg" or name == "source-ip-address-cfg" or name == "source-port-cfg" or name == "filter-type" or name == "filter-logical-not"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "filter-type"):
                    self.filter_type = value
                    self.filter_type.value_namespace = name_space
                    self.filter_type.value_namespace_prefix = name_space_prefix
                if(value_path == "filter-logical-not"):
                    self.filter_logical_not = value
                    self.filter_logical_not.value_namespace = name_space
                    self.filter_logical_not.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.filter_entry:
                if (c.has_data()):
                    return True
            return (
                self.classifier_entry_name.is_set or
                self.classifier_entry_descr.is_set or
                self.classifier_entry_filter_operation.is_set)

        def has_operation(self):
            for c in self.filter_entry:
                if (c.has_operation()):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.classifier_entry_name.yfilter != YFilter.not_set or
                self.classifier_entry_descr.yfilter != YFilter.not_set or
                self.classifier_entry_filter_operation.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "classifier-entry" + "[classifier-entry-name='" + self.classifier_entry_name.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ietf-diffserv-classifier:classifiers/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.classifier_entry_name.is_set or self.classifier_entry_name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.classifier_entry_name.get_name_leafdata())
            if (self.classifier_entry_descr.is_set or self.classifier_entry_descr.yfilter != YFilter.not_set):
                leaf_name_data.append(self.classifier_entry_descr.get_name_leafdata())
            if (self.classifier_entry_filter_operation.is_set or self.classifier_entry_filter_operation.yfilter != YFilter.not_set):
                leaf_name_data.append(self.classifier_entry_filter_operation.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "filter-entry"):
                for c in self.filter_entry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Classifiers.ClassifierEntry.FilterEntry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.filter_entry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "filter-entry" or name == "classifier-entry-name" or name == "classifier-entry-descr" or name == "classifier-entry-filter-operation"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "classifier-entry-name"):
                self.classifier_entry_name = value
                self.classifier_entry_name.value_namespace = name_space
                self.classifier_entry_name.value_namespace_prefix = name_space_prefix
            if(value_path == "classifier-entry-descr"):
                self.classifier_entry_descr = value
                self.classifier_entry_descr.value_namespace = name_space
                self.classifier_entry_descr.value_namespace_prefix = name_space_prefix
            if(value_path == "classifier-entry-filter-operation"):
                self.classifier_entry_filter_operation = value
                self.classifier_entry_filter_operation.value_namespace = name_space
                self.classifier_entry_filter_operation.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.classifier_entry:
            if (c.has_data()):
                return True
        return False

    def has_operation(self):
        for c in self.classifier_entry:
            if (c.has_operation()):
                return True
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "ietf-diffserv-classifier:classifiers" + path_buffer

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

        if (child_yang_name == "classifier-entry"):
            for c in self.classifier_entry:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = Classifiers.ClassifierEntry()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.classifier_entry.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "classifier-entry"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Classifiers()
        return self._top_entity

class MatchAnyFilter(Identity):
    """
    Classifier entry filter logical OR operation
    
    

    """

    _prefix = 'classifier'
    _revision = '2015-04-07'

    def __init__(self):
        super(MatchAnyFilter, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-classifier", "ietf-diffserv-classifier", "ietf-diffserv-classifier:match-any-filter")


class Dscp(Identity):
    """
    DSCP filter\-type
    
    

    """

    _prefix = 'classifier'
    _revision = '2015-04-07'

    def __init__(self):
        super(Dscp, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-classifier", "ietf-diffserv-classifier", "ietf-diffserv-classifier:dscp")


class SourceIpAddress(Identity):
    """
    source\-ip\-address filter\-type
    
    

    """

    _prefix = 'classifier'
    _revision = '2015-04-07'

    def __init__(self):
        super(SourceIpAddress, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-classifier", "ietf-diffserv-classifier", "ietf-diffserv-classifier:source-ip-address")


class DestinationIpAddress(Identity):
    """
    destination\-ip\-address filter\-type
    
    

    """

    _prefix = 'classifier'
    _revision = '2015-04-07'

    def __init__(self):
        super(DestinationIpAddress, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-classifier", "ietf-diffserv-classifier", "ietf-diffserv-classifier:destination-ip-address")


class MatchAllFilter(Identity):
    """
    Classifier entry filter logical AND operation
    
    

    """

    _prefix = 'classifier'
    _revision = '2015-04-07'

    def __init__(self):
        super(MatchAllFilter, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-classifier", "ietf-diffserv-classifier", "ietf-diffserv-classifier:match-all-filter")


class SourcePort(Identity):
    """
    source\-port filter\-type
    
    

    """

    _prefix = 'classifier'
    _revision = '2015-04-07'

    def __init__(self):
        super(SourcePort, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-classifier", "ietf-diffserv-classifier", "ietf-diffserv-classifier:source-port")


class DestinationPort(Identity):
    """
    destination\-port filter\-type
    
    

    """

    _prefix = 'classifier'
    _revision = '2015-04-07'

    def __init__(self):
        super(DestinationPort, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-classifier", "ietf-diffserv-classifier", "ietf-diffserv-classifier:destination-port")


class Protocol(Identity):
    """
    protocol filter\-type
    
    

    """

    _prefix = 'classifier'
    _revision = '2015-04-07'

    def __init__(self):
        super(Protocol, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-classifier", "ietf-diffserv-classifier", "ietf-diffserv-classifier:protocol")



""" ietf_diffserv_policy 

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



class ActionType(Identity):
    """
    This base identity type defines action\-types
    
    

    """

    _prefix = 'policy'
    _revision = '2015-04-07'

    def __init__(self):
        super(ActionType, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-policy", "ietf-diffserv-policy", "ietf-diffserv-policy:action-type")


class Policies(Entity):
    """
    list of policy templates
    
    .. attribute:: policy_entry
    
    	policy template
    	**type**\: list of    :py:class:`PolicyEntry <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry>`
    
    

    """

    _prefix = 'policy'
    _revision = '2015-04-07'

    def __init__(self):
        super(Policies, self).__init__()
        self._top_entity = None

        self.yang_name = "policies"
        self.yang_parent_name = "ietf-diffserv-policy"

        self.policy_entry = YList(self)

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
                    super(Policies, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Policies, self).__setattr__(name, value)


    class PolicyEntry(Entity):
        """
        policy template
        
        .. attribute:: policy_name  <key>
        
        	Diffserv policy name
        	**type**\:  str
        
        .. attribute:: classifier_entry
        
        	Classifier entry configuration in a policy
        	**type**\: list of    :py:class:`ClassifierEntry <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry>`
        
        .. attribute:: policy_descr
        
        	Diffserv policy description
        	**type**\:  str
        
        .. attribute:: policy_type
        
        	Type of the policy\-map
        	**type**\:   :py:class:`PolicyType <ydk.models.cisco_ios_xe.policy_types.PolicyType>`
        
        	**default value**\: policy-types:qos
        
        

        """

        _prefix = 'policy'
        _revision = '2015-04-07'

        def __init__(self):
            super(Policies.PolicyEntry, self).__init__()

            self.yang_name = "policy-entry"
            self.yang_parent_name = "policies"

            self.policy_name = YLeaf(YType.str, "policy-name")

            self.policy_descr = YLeaf(YType.str, "policy-descr")

            self.policy_type = YLeaf(YType.identityref, "cisco-policy:policy-type")

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
                if name in ("policy_name",
                            "policy_descr",
                            "policy_type") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Policies.PolicyEntry, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Policies.PolicyEntry, self).__setattr__(name, value)


        class ClassifierEntry(Entity):
            """
            Classifier entry configuration in a policy
            
            .. attribute:: classifier_entry_name  <key>
            
            	Diffserv classifier entry name
            	**type**\:  str
            
            .. attribute:: classifier_action_entry_cfg
            
            	Configuration of classifier & associated actions
            	**type**\: list of    :py:class:`ClassifierActionEntryCfg <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg>`
            
            .. attribute:: classifier_entry_filter_oper
            
            	Filters are applicable as any or all filters
            	**type**\:   :py:class:`ClassifierEntryFilterOperationType <ydk.models.ietf.ietf_diffserv_classifier.ClassifierEntryFilterOperationType>`
            
            	**default value**\: match-any-filter
            
            .. attribute:: classifier_entry_inline
            
            	Indication of inline classifier entry
            	**type**\:  bool
            
            	**default value**\: false
            
            .. attribute:: filter_entry
            
            	Filters configured inline in a policy
            	**type**\: list of    :py:class:`FilterEntry <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.FilterEntry>`
            
            

            """

            _prefix = 'policy'
            _revision = '2015-04-07'

            def __init__(self):
                super(Policies.PolicyEntry.ClassifierEntry, self).__init__()

                self.yang_name = "classifier-entry"
                self.yang_parent_name = "policy-entry"

                self.classifier_entry_name = YLeaf(YType.str, "classifier-entry-name")

                self.classifier_entry_filter_oper = YLeaf(YType.identityref, "classifier-entry-filter-oper")

                self.classifier_entry_inline = YLeaf(YType.boolean, "classifier-entry-inline")

                self.classifier_action_entry_cfg = YList(self)
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
                                "classifier_entry_filter_oper",
                                "classifier_entry_inline") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Policies.PolicyEntry.ClassifierEntry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Policies.PolicyEntry.ClassifierEntry, self).__setattr__(name, value)


            class FilterEntry(Entity):
                """
                Filters configured inline in a policy
                
                .. attribute:: filter_type  <key>
                
                	This leaf defines type of the filter
                	**type**\:   :py:class:`FilterType <ydk.models.ietf.ietf_diffserv_classifier.FilterType>`
                
                .. attribute:: filter_logical_not  <key>
                
                	 This is logical\-not operator for a filter. When true, it  indicates filter looks for absence of a pattern defined  by the filter 
                	**type**\:  bool
                
                .. attribute:: destination_ip_address_cfg
                
                	list of destination ip address
                	**type**\: list of    :py:class:`DestinationIpAddressCfg <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.FilterEntry.DestinationIpAddressCfg>`
                
                .. attribute:: destination_port_cfg
                
                	list of ranges of destination port
                	**type**\: list of    :py:class:`DestinationPortCfg <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.FilterEntry.DestinationPortCfg>`
                
                .. attribute:: dscp_cfg
                
                	list of dscp ranges
                	**type**\: list of    :py:class:`DscpCfg <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.FilterEntry.DscpCfg>`
                
                .. attribute:: protocol_cfg
                
                	list of ranges of protocol values
                	**type**\: list of    :py:class:`ProtocolCfg <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.FilterEntry.ProtocolCfg>`
                
                .. attribute:: source_ip_address_cfg
                
                	list of source ip address
                	**type**\: list of    :py:class:`SourceIpAddressCfg <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.FilterEntry.SourceIpAddressCfg>`
                
                .. attribute:: source_port_cfg
                
                	list of ranges of source port
                	**type**\: list of    :py:class:`SourcePortCfg <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.FilterEntry.SourcePortCfg>`
                
                

                """

                _prefix = 'policy'
                _revision = '2015-04-07'

                def __init__(self):
                    super(Policies.PolicyEntry.ClassifierEntry.FilterEntry, self).__init__()

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
                                super(Policies.PolicyEntry.ClassifierEntry.FilterEntry, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Policies.PolicyEntry.ClassifierEntry.FilterEntry, self).__setattr__(name, value)


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

                    _prefix = 'policy'
                    _revision = '2015-04-07'

                    def __init__(self):
                        super(Policies.PolicyEntry.ClassifierEntry.FilterEntry.DscpCfg, self).__init__()

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
                                    super(Policies.PolicyEntry.ClassifierEntry.FilterEntry.DscpCfg, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Policies.PolicyEntry.ClassifierEntry.FilterEntry.DscpCfg, self).__setattr__(name, value)

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

                    _prefix = 'policy'
                    _revision = '2015-04-07'

                    def __init__(self):
                        super(Policies.PolicyEntry.ClassifierEntry.FilterEntry.SourceIpAddressCfg, self).__init__()

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
                                    super(Policies.PolicyEntry.ClassifierEntry.FilterEntry.SourceIpAddressCfg, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Policies.PolicyEntry.ClassifierEntry.FilterEntry.SourceIpAddressCfg, self).__setattr__(name, value)

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

                    _prefix = 'policy'
                    _revision = '2015-04-07'

                    def __init__(self):
                        super(Policies.PolicyEntry.ClassifierEntry.FilterEntry.DestinationIpAddressCfg, self).__init__()

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
                                    super(Policies.PolicyEntry.ClassifierEntry.FilterEntry.DestinationIpAddressCfg, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Policies.PolicyEntry.ClassifierEntry.FilterEntry.DestinationIpAddressCfg, self).__setattr__(name, value)

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

                    _prefix = 'policy'
                    _revision = '2015-04-07'

                    def __init__(self):
                        super(Policies.PolicyEntry.ClassifierEntry.FilterEntry.SourcePortCfg, self).__init__()

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
                                    super(Policies.PolicyEntry.ClassifierEntry.FilterEntry.SourcePortCfg, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Policies.PolicyEntry.ClassifierEntry.FilterEntry.SourcePortCfg, self).__setattr__(name, value)

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

                    _prefix = 'policy'
                    _revision = '2015-04-07'

                    def __init__(self):
                        super(Policies.PolicyEntry.ClassifierEntry.FilterEntry.DestinationPortCfg, self).__init__()

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
                                    super(Policies.PolicyEntry.ClassifierEntry.FilterEntry.DestinationPortCfg, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Policies.PolicyEntry.ClassifierEntry.FilterEntry.DestinationPortCfg, self).__setattr__(name, value)

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

                    _prefix = 'policy'
                    _revision = '2015-04-07'

                    def __init__(self):
                        super(Policies.PolicyEntry.ClassifierEntry.FilterEntry.ProtocolCfg, self).__init__()

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
                                    super(Policies.PolicyEntry.ClassifierEntry.FilterEntry.ProtocolCfg, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Policies.PolicyEntry.ClassifierEntry.FilterEntry.ProtocolCfg, self).__setattr__(name, value)

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
                        c = Policies.PolicyEntry.ClassifierEntry.FilterEntry.DestinationIpAddressCfg()
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
                        c = Policies.PolicyEntry.ClassifierEntry.FilterEntry.DestinationPortCfg()
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
                        c = Policies.PolicyEntry.ClassifierEntry.FilterEntry.DscpCfg()
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
                        c = Policies.PolicyEntry.ClassifierEntry.FilterEntry.ProtocolCfg()
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
                        c = Policies.PolicyEntry.ClassifierEntry.FilterEntry.SourceIpAddressCfg()
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
                        c = Policies.PolicyEntry.ClassifierEntry.FilterEntry.SourcePortCfg()
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


            class ClassifierActionEntryCfg(Entity):
                """
                Configuration of classifier & associated actions
                
                .. attribute:: action_type  <key>
                
                	This defines action type 
                	**type**\:   :py:class:`ActionType <ydk.models.ietf.ietf_diffserv_policy.ActionType>`
                
                .. attribute:: drop_cfg
                
                	Always Drop configuration container
                	**type**\:   :py:class:`DropCfg <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.DropCfg>`
                
                .. attribute:: marking_cfg
                
                	Marking configuration container
                	**type**\:   :py:class:`MarkingCfg <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MarkingCfg>`
                
                .. attribute:: max_rate_cfg
                
                	maximum rate attributes
                	**type**\:   :py:class:`MaxRateCfg <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MaxRateCfg>`
                
                .. attribute:: meter_cfg
                
                	Meter list configuration container
                	**type**\:   :py:class:`MeterCfg <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg>`
                
                .. attribute:: min_rate_cfg
                
                	min guaranteed bandwidth
                	**type**\:   :py:class:`MinRateCfg <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MinRateCfg>`
                
                .. attribute:: priority_cfg
                
                	priority attributes container
                	**type**\:   :py:class:`PriorityCfg <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.PriorityCfg>`
                
                .. attribute:: random_detect_cfg
                
                	Random Detect configuration container
                	**type**\:   :py:class:`RandomDetectCfg <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg>`
                
                .. attribute:: tail_drop_cfg
                
                	Tail Drop configuration container
                	**type**\:   :py:class:`TailDropCfg <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.TailDropCfg>`
                
                

                """

                _prefix = 'policy'
                _revision = '2015-04-07'

                def __init__(self):
                    super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg, self).__init__()

                    self.yang_name = "classifier-action-entry-cfg"
                    self.yang_parent_name = "classifier-entry"

                    self.action_type = YLeaf(YType.identityref, "action-type")

                    self.drop_cfg = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.DropCfg()
                    self.drop_cfg.parent = self
                    self._children_name_map["drop_cfg"] = "drop-cfg"
                    self._children_yang_names.add("drop-cfg")

                    self.marking_cfg = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MarkingCfg()
                    self.marking_cfg.parent = self
                    self._children_name_map["marking_cfg"] = "marking-cfg"
                    self._children_yang_names.add("marking-cfg")

                    self.max_rate_cfg = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MaxRateCfg()
                    self.max_rate_cfg.parent = self
                    self._children_name_map["max_rate_cfg"] = "max-rate-cfg"
                    self._children_yang_names.add("max-rate-cfg")

                    self.meter_cfg = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg()
                    self.meter_cfg.parent = self
                    self._children_name_map["meter_cfg"] = "meter-cfg"
                    self._children_yang_names.add("meter-cfg")

                    self.min_rate_cfg = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MinRateCfg()
                    self.min_rate_cfg.parent = self
                    self._children_name_map["min_rate_cfg"] = "min-rate-cfg"
                    self._children_yang_names.add("min-rate-cfg")

                    self.priority_cfg = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.PriorityCfg()
                    self.priority_cfg.parent = self
                    self._children_name_map["priority_cfg"] = "priority-cfg"
                    self._children_yang_names.add("priority-cfg")

                    self.random_detect_cfg = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg()
                    self.random_detect_cfg.parent = self
                    self._children_name_map["random_detect_cfg"] = "random-detect-cfg"
                    self._children_yang_names.add("random-detect-cfg")

                    self.tail_drop_cfg = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.TailDropCfg()
                    self.tail_drop_cfg.parent = self
                    self._children_name_map["tail_drop_cfg"] = "tail-drop-cfg"
                    self._children_yang_names.add("tail-drop-cfg")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("action_type") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg, self).__setattr__(name, value)


                class MarkingCfg(Entity):
                    """
                    Marking configuration container
                    
                    .. attribute:: dscp
                    
                    	dscp marking
                    	**type**\:  int
                    
                    	**range:** 0..63
                    
                    

                    """

                    _prefix = 'action'
                    _revision = '2015-04-07'

                    def __init__(self):
                        super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MarkingCfg, self).__init__()

                        self.yang_name = "marking-cfg"
                        self.yang_parent_name = "classifier-action-entry-cfg"

                        self.dscp = YLeaf(YType.uint8, "dscp")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("dscp") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MarkingCfg, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MarkingCfg, self).__setattr__(name, value)

                    def has_data(self):
                        return self.dscp.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.dscp.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ietf-diffserv-action:marking-cfg" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.dscp.is_set or self.dscp.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dscp.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "dscp"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "dscp"):
                            self.dscp = value
                            self.dscp.value_namespace = name_space
                            self.dscp.value_namespace_prefix = name_space_prefix


                class PriorityCfg(Entity):
                    """
                    priority attributes container
                    
                    .. attribute:: priority_level
                    
                    	priority level
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: rate_burst
                    
                    	absolute priority rate with/without burst rateand absolute percent
                    	**type**\:   :py:class:`RateBurst <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.PriorityCfg.RateBurst>`
                    
                    

                    """

                    _prefix = 'action'
                    _revision = '2015-04-07'

                    def __init__(self):
                        super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.PriorityCfg, self).__init__()

                        self.yang_name = "priority-cfg"
                        self.yang_parent_name = "classifier-action-entry-cfg"

                        self.priority_level = YLeaf(YType.uint8, "priority-level")

                        self.rate_burst = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.PriorityCfg.RateBurst()
                        self.rate_burst.parent = self
                        self._children_name_map["rate_burst"] = "rate-burst"
                        self._children_yang_names.add("rate-burst")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("priority_level") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.PriorityCfg, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.PriorityCfg, self).__setattr__(name, value)


                    class RateBurst(Entity):
                        """
                        absolute priority rate with/without burst rateand absolute percent
                        
                        .. attribute:: absolute_rate_metric
                        
                        	Metric
                        	**type**\:   :py:class:`Metric <ydk.models.cisco_ios_xe.policy_types.Metric>`
                        
                        	**default value**\: none
                        
                        .. attribute:: absolute_rate_units
                        
                        	Rate basic units
                        	**type**\:   :py:class:`RateUnit <ydk.models.cisco_ios_xe.policy_types.RateUnit>`
                        
                        .. attribute:: burst_interval
                        
                        	burst interval
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: microsecond
                        
                        .. attribute:: burst_size
                        
                        	burst size
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: bytes
                        
                        .. attribute:: rate
                        
                        	Rate value
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: bits-per-second
                        
                        .. attribute:: rate_percent
                        
                        	percent
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: rate_ratio
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 1..65532
                        
                        

                        """

                        _prefix = 'action'
                        _revision = '2015-04-07'

                        def __init__(self):
                            super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.PriorityCfg.RateBurst, self).__init__()

                            self.yang_name = "rate-burst"
                            self.yang_parent_name = "priority-cfg"

                            self.absolute_rate_metric = YLeaf(YType.enumeration, "absolute-rate-metric")

                            self.absolute_rate_units = YLeaf(YType.enumeration, "absolute-rate-units")

                            self.burst_interval = YLeaf(YType.uint64, "burst-interval")

                            self.burst_size = YLeaf(YType.uint64, "burst-size")

                            self.rate = YLeaf(YType.uint64, "rate")

                            self.rate_percent = YLeaf(YType.uint8, "rate-percent")

                            self.rate_ratio = YLeaf(YType.uint32, "rate-ratio")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("absolute_rate_metric",
                                            "absolute_rate_units",
                                            "burst_interval",
                                            "burst_size",
                                            "rate",
                                            "rate_percent",
                                            "rate_ratio") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.PriorityCfg.RateBurst, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.PriorityCfg.RateBurst, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.absolute_rate_metric.is_set or
                                self.absolute_rate_units.is_set or
                                self.burst_interval.is_set or
                                self.burst_size.is_set or
                                self.rate.is_set or
                                self.rate_percent.is_set or
                                self.rate_ratio.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.absolute_rate_metric.yfilter != YFilter.not_set or
                                self.absolute_rate_units.yfilter != YFilter.not_set or
                                self.burst_interval.yfilter != YFilter.not_set or
                                self.burst_size.yfilter != YFilter.not_set or
                                self.rate.yfilter != YFilter.not_set or
                                self.rate_percent.yfilter != YFilter.not_set or
                                self.rate_ratio.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "rate-burst" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.absolute_rate_metric.is_set or self.absolute_rate_metric.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.absolute_rate_metric.get_name_leafdata())
                            if (self.absolute_rate_units.is_set or self.absolute_rate_units.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.absolute_rate_units.get_name_leafdata())
                            if (self.burst_interval.is_set or self.burst_interval.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.burst_interval.get_name_leafdata())
                            if (self.burst_size.is_set or self.burst_size.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.burst_size.get_name_leafdata())
                            if (self.rate.is_set or self.rate.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.rate.get_name_leafdata())
                            if (self.rate_percent.is_set or self.rate_percent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.rate_percent.get_name_leafdata())
                            if (self.rate_ratio.is_set or self.rate_ratio.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.rate_ratio.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "absolute-rate-metric" or name == "absolute-rate-units" or name == "burst-interval" or name == "burst-size" or name == "rate" or name == "rate-percent" or name == "rate-ratio"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "absolute-rate-metric"):
                                self.absolute_rate_metric = value
                                self.absolute_rate_metric.value_namespace = name_space
                                self.absolute_rate_metric.value_namespace_prefix = name_space_prefix
                            if(value_path == "absolute-rate-units"):
                                self.absolute_rate_units = value
                                self.absolute_rate_units.value_namespace = name_space
                                self.absolute_rate_units.value_namespace_prefix = name_space_prefix
                            if(value_path == "burst-interval"):
                                self.burst_interval = value
                                self.burst_interval.value_namespace = name_space
                                self.burst_interval.value_namespace_prefix = name_space_prefix
                            if(value_path == "burst-size"):
                                self.burst_size = value
                                self.burst_size.value_namespace = name_space
                                self.burst_size.value_namespace_prefix = name_space_prefix
                            if(value_path == "rate"):
                                self.rate = value
                                self.rate.value_namespace = name_space
                                self.rate.value_namespace_prefix = name_space_prefix
                            if(value_path == "rate-percent"):
                                self.rate_percent = value
                                self.rate_percent.value_namespace = name_space
                                self.rate_percent.value_namespace_prefix = name_space_prefix
                            if(value_path == "rate-ratio"):
                                self.rate_ratio = value
                                self.rate_ratio.value_namespace = name_space
                                self.rate_ratio.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.priority_level.is_set or
                            (self.rate_burst is not None and self.rate_burst.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.priority_level.yfilter != YFilter.not_set or
                            (self.rate_burst is not None and self.rate_burst.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ietf-diffserv-action:priority-cfg" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.priority_level.is_set or self.priority_level.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.priority_level.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "rate-burst"):
                            if (self.rate_burst is None):
                                self.rate_burst = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.PriorityCfg.RateBurst()
                                self.rate_burst.parent = self
                                self._children_name_map["rate_burst"] = "rate-burst"
                            return self.rate_burst

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "rate-burst" or name == "priority-level"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "priority-level"):
                            self.priority_level = value
                            self.priority_level.value_namespace = name_space
                            self.priority_level.value_namespace_prefix = name_space_prefix


                class MeterCfg(Entity):
                    """
                    Meter list configuration container
                    
                    .. attribute:: meter_list
                    
                    	Meter configuration
                    	**type**\: list of    :py:class:`MeterList <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg.MeterList>`
                    
                    

                    """

                    _prefix = 'action'
                    _revision = '2015-04-07'

                    def __init__(self):
                        super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg, self).__init__()

                        self.yang_name = "meter-cfg"
                        self.yang_parent_name = "classifier-action-entry-cfg"

                        self.meter_list = YList(self)

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
                                    super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg, self).__setattr__(name, value)


                    class MeterList(Entity):
                        """
                        Meter configuration
                        
                        .. attribute:: meter_id  <key>
                        
                        	meter identifier
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: burst_interval
                        
                        	burst interval
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: microsecond
                        
                        .. attribute:: burst_size
                        
                        	burst size
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: bytes
                        
                        .. attribute:: color
                        
                        	color aware & color blind attributes container
                        	**type**\:   :py:class:`Color <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg.MeterList.Color>`
                        
                        .. attribute:: fail_action
                        
                        	exceed action
                        	**type**\:   :py:class:`FailAction <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg.MeterList.FailAction>`
                        
                        .. attribute:: meter_rate
                        
                        	meter rate
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: bits-per-second
                        
                        .. attribute:: succeed_action
                        
                        	confirm action
                        	**type**\:   :py:class:`SucceedAction <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg.MeterList.SucceedAction>`
                        
                        

                        """

                        _prefix = 'action'
                        _revision = '2015-04-07'

                        def __init__(self):
                            super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg.MeterList, self).__init__()

                            self.yang_name = "meter-list"
                            self.yang_parent_name = "meter-cfg"

                            self.meter_id = YLeaf(YType.uint16, "meter-id")

                            self.burst_interval = YLeaf(YType.uint64, "burst-interval")

                            self.burst_size = YLeaf(YType.uint64, "burst-size")

                            self.meter_rate = YLeaf(YType.uint64, "meter-rate")

                            self.color = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg.MeterList.Color()
                            self.color.parent = self
                            self._children_name_map["color"] = "color"
                            self._children_yang_names.add("color")

                            self.fail_action = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg.MeterList.FailAction()
                            self.fail_action.parent = self
                            self._children_name_map["fail_action"] = "fail-action"
                            self._children_yang_names.add("fail-action")

                            self.succeed_action = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg.MeterList.SucceedAction()
                            self.succeed_action.parent = self
                            self._children_name_map["succeed_action"] = "succeed-action"
                            self._children_yang_names.add("succeed-action")

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
                                            "burst_interval",
                                            "burst_size",
                                            "meter_rate") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg.MeterList, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg.MeterList, self).__setattr__(name, value)


                        class Color(Entity):
                            """
                            color aware & color blind attributes container
                            
                            .. attribute:: classifier_entry_descr
                            
                            	Description of the class template
                            	**type**\:  str
                            
                            .. attribute:: classifier_entry_filter_operation
                            
                            	Filters are applicable as any or all filters
                            	**type**\:   :py:class:`ClassifierEntryFilterOperationType <ydk.models.ietf.ietf_diffserv_classifier.ClassifierEntryFilterOperationType>`
                            
                            	**default value**\: match-any-filter
                            
                            .. attribute:: classifier_entry_name
                            
                            	Diffserv classifier name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'action'
                            _revision = '2015-04-07'

                            def __init__(self):
                                super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg.MeterList.Color, self).__init__()

                                self.yang_name = "color"
                                self.yang_parent_name = "meter-list"

                                self.classifier_entry_descr = YLeaf(YType.str, "classifier-entry-descr")

                                self.classifier_entry_filter_operation = YLeaf(YType.identityref, "classifier-entry-filter-operation")

                                self.classifier_entry_name = YLeaf(YType.str, "classifier-entry-name")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("classifier_entry_descr",
                                                "classifier_entry_filter_operation",
                                                "classifier_entry_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg.MeterList.Color, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg.MeterList.Color, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.classifier_entry_descr.is_set or
                                    self.classifier_entry_filter_operation.is_set or
                                    self.classifier_entry_name.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.classifier_entry_descr.yfilter != YFilter.not_set or
                                    self.classifier_entry_filter_operation.yfilter != YFilter.not_set or
                                    self.classifier_entry_name.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "color" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.classifier_entry_descr.is_set or self.classifier_entry_descr.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.classifier_entry_descr.get_name_leafdata())
                                if (self.classifier_entry_filter_operation.is_set or self.classifier_entry_filter_operation.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.classifier_entry_filter_operation.get_name_leafdata())
                                if (self.classifier_entry_name.is_set or self.classifier_entry_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.classifier_entry_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "classifier-entry-descr" or name == "classifier-entry-filter-operation" or name == "classifier-entry-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "classifier-entry-descr"):
                                    self.classifier_entry_descr = value
                                    self.classifier_entry_descr.value_namespace = name_space
                                    self.classifier_entry_descr.value_namespace_prefix = name_space_prefix
                                if(value_path == "classifier-entry-filter-operation"):
                                    self.classifier_entry_filter_operation = value
                                    self.classifier_entry_filter_operation.value_namespace = name_space
                                    self.classifier_entry_filter_operation.value_namespace_prefix = name_space_prefix
                                if(value_path == "classifier-entry-name"):
                                    self.classifier_entry_name = value
                                    self.classifier_entry_name.value_namespace = name_space
                                    self.classifier_entry_name.value_namespace_prefix = name_space_prefix


                        class SucceedAction(Entity):
                            """
                            confirm action
                            
                            .. attribute:: drop_action
                            
                            	always drop algorithm
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: dscp
                            
                            	dscp marking
                            	**type**\:  int
                            
                            	**range:** 0..63
                            
                            .. attribute:: meter_action_type
                            
                            	meter action type
                            	**type**\:   :py:class:`MeterActionType <ydk.models.ietf.ietf_diffserv_action.MeterActionType>`
                            
                            .. attribute:: next_meter_id
                            
                            	next meter identifier
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'action'
                            _revision = '2015-04-07'

                            def __init__(self):
                                super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg.MeterList.SucceedAction, self).__init__()

                                self.yang_name = "succeed-action"
                                self.yang_parent_name = "meter-list"

                                self.drop_action = YLeaf(YType.empty, "drop-action")

                                self.dscp = YLeaf(YType.uint8, "dscp")

                                self.meter_action_type = YLeaf(YType.identityref, "meter-action-type")

                                self.next_meter_id = YLeaf(YType.uint16, "next-meter-id")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("drop_action",
                                                "dscp",
                                                "meter_action_type",
                                                "next_meter_id") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg.MeterList.SucceedAction, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg.MeterList.SucceedAction, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.drop_action.is_set or
                                    self.dscp.is_set or
                                    self.meter_action_type.is_set or
                                    self.next_meter_id.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.drop_action.yfilter != YFilter.not_set or
                                    self.dscp.yfilter != YFilter.not_set or
                                    self.meter_action_type.yfilter != YFilter.not_set or
                                    self.next_meter_id.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "succeed-action" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.drop_action.is_set or self.drop_action.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.drop_action.get_name_leafdata())
                                if (self.dscp.is_set or self.dscp.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.dscp.get_name_leafdata())
                                if (self.meter_action_type.is_set or self.meter_action_type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.meter_action_type.get_name_leafdata())
                                if (self.next_meter_id.is_set or self.next_meter_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.next_meter_id.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "drop-action" or name == "dscp" or name == "meter-action-type" or name == "next-meter-id"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "drop-action"):
                                    self.drop_action = value
                                    self.drop_action.value_namespace = name_space
                                    self.drop_action.value_namespace_prefix = name_space_prefix
                                if(value_path == "dscp"):
                                    self.dscp = value
                                    self.dscp.value_namespace = name_space
                                    self.dscp.value_namespace_prefix = name_space_prefix
                                if(value_path == "meter-action-type"):
                                    self.meter_action_type = value
                                    self.meter_action_type.value_namespace = name_space
                                    self.meter_action_type.value_namespace_prefix = name_space_prefix
                                if(value_path == "next-meter-id"):
                                    self.next_meter_id = value
                                    self.next_meter_id.value_namespace = name_space
                                    self.next_meter_id.value_namespace_prefix = name_space_prefix


                        class FailAction(Entity):
                            """
                            exceed action
                            
                            .. attribute:: drop_action
                            
                            	always drop algorithm
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: dscp
                            
                            	dscp marking
                            	**type**\:  int
                            
                            	**range:** 0..63
                            
                            .. attribute:: meter_action_type
                            
                            	meter action type
                            	**type**\:   :py:class:`MeterActionType <ydk.models.ietf.ietf_diffserv_action.MeterActionType>`
                            
                            .. attribute:: next_meter_id
                            
                            	next meter identifier
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'action'
                            _revision = '2015-04-07'

                            def __init__(self):
                                super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg.MeterList.FailAction, self).__init__()

                                self.yang_name = "fail-action"
                                self.yang_parent_name = "meter-list"

                                self.drop_action = YLeaf(YType.empty, "drop-action")

                                self.dscp = YLeaf(YType.uint8, "dscp")

                                self.meter_action_type = YLeaf(YType.identityref, "meter-action-type")

                                self.next_meter_id = YLeaf(YType.uint16, "next-meter-id")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("drop_action",
                                                "dscp",
                                                "meter_action_type",
                                                "next_meter_id") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg.MeterList.FailAction, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg.MeterList.FailAction, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.drop_action.is_set or
                                    self.dscp.is_set or
                                    self.meter_action_type.is_set or
                                    self.next_meter_id.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.drop_action.yfilter != YFilter.not_set or
                                    self.dscp.yfilter != YFilter.not_set or
                                    self.meter_action_type.yfilter != YFilter.not_set or
                                    self.next_meter_id.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "fail-action" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.drop_action.is_set or self.drop_action.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.drop_action.get_name_leafdata())
                                if (self.dscp.is_set or self.dscp.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.dscp.get_name_leafdata())
                                if (self.meter_action_type.is_set or self.meter_action_type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.meter_action_type.get_name_leafdata())
                                if (self.next_meter_id.is_set or self.next_meter_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.next_meter_id.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "drop-action" or name == "dscp" or name == "meter-action-type" or name == "next-meter-id"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "drop-action"):
                                    self.drop_action = value
                                    self.drop_action.value_namespace = name_space
                                    self.drop_action.value_namespace_prefix = name_space_prefix
                                if(value_path == "dscp"):
                                    self.dscp = value
                                    self.dscp.value_namespace = name_space
                                    self.dscp.value_namespace_prefix = name_space_prefix
                                if(value_path == "meter-action-type"):
                                    self.meter_action_type = value
                                    self.meter_action_type.value_namespace = name_space
                                    self.meter_action_type.value_namespace_prefix = name_space_prefix
                                if(value_path == "next-meter-id"):
                                    self.next_meter_id = value
                                    self.next_meter_id.value_namespace = name_space
                                    self.next_meter_id.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.meter_id.is_set or
                                self.burst_interval.is_set or
                                self.burst_size.is_set or
                                self.meter_rate.is_set or
                                (self.color is not None and self.color.has_data()) or
                                (self.fail_action is not None and self.fail_action.has_data()) or
                                (self.succeed_action is not None and self.succeed_action.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.meter_id.yfilter != YFilter.not_set or
                                self.burst_interval.yfilter != YFilter.not_set or
                                self.burst_size.yfilter != YFilter.not_set or
                                self.meter_rate.yfilter != YFilter.not_set or
                                (self.color is not None and self.color.has_operation()) or
                                (self.fail_action is not None and self.fail_action.has_operation()) or
                                (self.succeed_action is not None and self.succeed_action.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "meter-list" + "[meter-id='" + self.meter_id.get() + "']" + path_buffer

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
                            if (self.burst_interval.is_set or self.burst_interval.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.burst_interval.get_name_leafdata())
                            if (self.burst_size.is_set or self.burst_size.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.burst_size.get_name_leafdata())
                            if (self.meter_rate.is_set or self.meter_rate.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.meter_rate.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "color"):
                                if (self.color is None):
                                    self.color = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg.MeterList.Color()
                                    self.color.parent = self
                                    self._children_name_map["color"] = "color"
                                return self.color

                            if (child_yang_name == "fail-action"):
                                if (self.fail_action is None):
                                    self.fail_action = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg.MeterList.FailAction()
                                    self.fail_action.parent = self
                                    self._children_name_map["fail_action"] = "fail-action"
                                return self.fail_action

                            if (child_yang_name == "succeed-action"):
                                if (self.succeed_action is None):
                                    self.succeed_action = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg.MeterList.SucceedAction()
                                    self.succeed_action.parent = self
                                    self._children_name_map["succeed_action"] = "succeed-action"
                                return self.succeed_action

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "color" or name == "fail-action" or name == "succeed-action" or name == "meter-id" or name == "burst-interval" or name == "burst-size" or name == "meter-rate"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "meter-id"):
                                self.meter_id = value
                                self.meter_id.value_namespace = name_space
                                self.meter_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "burst-interval"):
                                self.burst_interval = value
                                self.burst_interval.value_namespace = name_space
                                self.burst_interval.value_namespace_prefix = name_space_prefix
                            if(value_path == "burst-size"):
                                self.burst_size = value
                                self.burst_size.value_namespace = name_space
                                self.burst_size.value_namespace_prefix = name_space_prefix
                            if(value_path == "meter-rate"):
                                self.meter_rate = value
                                self.meter_rate.value_namespace = name_space
                                self.meter_rate.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.meter_list:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.meter_list:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ietf-diffserv-action:meter-cfg" + path_buffer

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

                        if (child_yang_name == "meter-list"):
                            for c in self.meter_list:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg.MeterList()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.meter_list.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "meter-list"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class MinRateCfg(Entity):
                    """
                    min guaranteed bandwidth
                    
                    .. attribute:: absolute_rate_metric
                    
                    	Metric
                    	**type**\:   :py:class:`Metric <ydk.models.cisco_ios_xe.policy_types.Metric>`
                    
                    	**default value**\: none
                    
                    .. attribute:: absolute_rate_units
                    
                    	Rate basic units
                    	**type**\:   :py:class:`RateUnit <ydk.models.cisco_ios_xe.policy_types.RateUnit>`
                    
                    .. attribute:: bw_excess_share_cfg
                    
                    	share the bandwidth remaming
                    	**type**\:   :py:class:`BwExcessShareCfg <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MinRateCfg.BwExcessShareCfg>`
                    
                    .. attribute:: min_rate
                    
                    	minimum rate
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: bits-per-second
                    
                    .. attribute:: rate_percent
                    
                    	percent
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    .. attribute:: rate_ratio
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 1..65532
                    
                    

                    """

                    _prefix = 'action'
                    _revision = '2015-04-07'

                    def __init__(self):
                        super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MinRateCfg, self).__init__()

                        self.yang_name = "min-rate-cfg"
                        self.yang_parent_name = "classifier-action-entry-cfg"

                        self.absolute_rate_metric = YLeaf(YType.enumeration, "absolute-rate-metric")

                        self.absolute_rate_units = YLeaf(YType.enumeration, "absolute-rate-units")

                        self.min_rate = YLeaf(YType.uint64, "min-rate")

                        self.rate_percent = YLeaf(YType.uint8, "rate-percent")

                        self.rate_ratio = YLeaf(YType.uint32, "rate-ratio")

                        self.bw_excess_share_cfg = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MinRateCfg.BwExcessShareCfg()
                        self.bw_excess_share_cfg.parent = self
                        self._children_name_map["bw_excess_share_cfg"] = "bw-excess-share-cfg"
                        self._children_yang_names.add("bw-excess-share-cfg")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("absolute_rate_metric",
                                        "absolute_rate_units",
                                        "min_rate",
                                        "rate_percent",
                                        "rate_ratio") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MinRateCfg, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MinRateCfg, self).__setattr__(name, value)


                    class BwExcessShareCfg(Entity):
                        """
                        share the bandwidth remaming
                        
                        .. attribute:: absolute_rate_metric
                        
                        	Metric
                        	**type**\:   :py:class:`Metric <ydk.models.cisco_ios_xe.policy_types.Metric>`
                        
                        	**default value**\: none
                        
                        .. attribute:: absolute_rate_units
                        
                        	Rate basic units
                        	**type**\:   :py:class:`RateUnit <ydk.models.cisco_ios_xe.policy_types.RateUnit>`
                        
                        .. attribute:: rate_percent
                        
                        	percent
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: rate_ratio
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 1..65532
                        
                        .. attribute:: value
                        
                        	percentage or ratio value
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'action'
                        _revision = '2015-04-07'

                        def __init__(self):
                            super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MinRateCfg.BwExcessShareCfg, self).__init__()

                            self.yang_name = "bw-excess-share-cfg"
                            self.yang_parent_name = "min-rate-cfg"

                            self.absolute_rate_metric = YLeaf(YType.enumeration, "absolute-rate-metric")

                            self.absolute_rate_units = YLeaf(YType.enumeration, "absolute-rate-units")

                            self.rate_percent = YLeaf(YType.uint8, "rate-percent")

                            self.rate_ratio = YLeaf(YType.uint32, "rate-ratio")

                            self.value = YLeaf(YType.uint32, "value")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("absolute_rate_metric",
                                            "absolute_rate_units",
                                            "rate_percent",
                                            "rate_ratio",
                                            "value") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MinRateCfg.BwExcessShareCfg, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MinRateCfg.BwExcessShareCfg, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.absolute_rate_metric.is_set or
                                self.absolute_rate_units.is_set or
                                self.rate_percent.is_set or
                                self.rate_ratio.is_set or
                                self.value.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.absolute_rate_metric.yfilter != YFilter.not_set or
                                self.absolute_rate_units.yfilter != YFilter.not_set or
                                self.rate_percent.yfilter != YFilter.not_set or
                                self.rate_ratio.yfilter != YFilter.not_set or
                                self.value.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "bw-excess-share-cfg" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.absolute_rate_metric.is_set or self.absolute_rate_metric.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.absolute_rate_metric.get_name_leafdata())
                            if (self.absolute_rate_units.is_set or self.absolute_rate_units.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.absolute_rate_units.get_name_leafdata())
                            if (self.rate_percent.is_set or self.rate_percent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.rate_percent.get_name_leafdata())
                            if (self.rate_ratio.is_set or self.rate_ratio.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.rate_ratio.get_name_leafdata())
                            if (self.value.is_set or self.value.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.value.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "absolute-rate-metric" or name == "absolute-rate-units" or name == "rate-percent" or name == "rate-ratio" or name == "value"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "absolute-rate-metric"):
                                self.absolute_rate_metric = value
                                self.absolute_rate_metric.value_namespace = name_space
                                self.absolute_rate_metric.value_namespace_prefix = name_space_prefix
                            if(value_path == "absolute-rate-units"):
                                self.absolute_rate_units = value
                                self.absolute_rate_units.value_namespace = name_space
                                self.absolute_rate_units.value_namespace_prefix = name_space_prefix
                            if(value_path == "rate-percent"):
                                self.rate_percent = value
                                self.rate_percent.value_namespace = name_space
                                self.rate_percent.value_namespace_prefix = name_space_prefix
                            if(value_path == "rate-ratio"):
                                self.rate_ratio = value
                                self.rate_ratio.value_namespace = name_space
                                self.rate_ratio.value_namespace_prefix = name_space_prefix
                            if(value_path == "value"):
                                self.value = value
                                self.value.value_namespace = name_space
                                self.value.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.absolute_rate_metric.is_set or
                            self.absolute_rate_units.is_set or
                            self.min_rate.is_set or
                            self.rate_percent.is_set or
                            self.rate_ratio.is_set or
                            (self.bw_excess_share_cfg is not None and self.bw_excess_share_cfg.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.absolute_rate_metric.yfilter != YFilter.not_set or
                            self.absolute_rate_units.yfilter != YFilter.not_set or
                            self.min_rate.yfilter != YFilter.not_set or
                            self.rate_percent.yfilter != YFilter.not_set or
                            self.rate_ratio.yfilter != YFilter.not_set or
                            (self.bw_excess_share_cfg is not None and self.bw_excess_share_cfg.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ietf-diffserv-action:min-rate-cfg" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.absolute_rate_metric.is_set or self.absolute_rate_metric.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.absolute_rate_metric.get_name_leafdata())
                        if (self.absolute_rate_units.is_set or self.absolute_rate_units.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.absolute_rate_units.get_name_leafdata())
                        if (self.min_rate.is_set or self.min_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.min_rate.get_name_leafdata())
                        if (self.rate_percent.is_set or self.rate_percent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rate_percent.get_name_leafdata())
                        if (self.rate_ratio.is_set or self.rate_ratio.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rate_ratio.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "bw-excess-share-cfg"):
                            if (self.bw_excess_share_cfg is None):
                                self.bw_excess_share_cfg = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MinRateCfg.BwExcessShareCfg()
                                self.bw_excess_share_cfg.parent = self
                                self._children_name_map["bw_excess_share_cfg"] = "bw-excess-share-cfg"
                            return self.bw_excess_share_cfg

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "bw-excess-share-cfg" or name == "absolute-rate-metric" or name == "absolute-rate-units" or name == "min-rate" or name == "rate-percent" or name == "rate-ratio"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "absolute-rate-metric"):
                            self.absolute_rate_metric = value
                            self.absolute_rate_metric.value_namespace = name_space
                            self.absolute_rate_metric.value_namespace_prefix = name_space_prefix
                        if(value_path == "absolute-rate-units"):
                            self.absolute_rate_units = value
                            self.absolute_rate_units.value_namespace = name_space
                            self.absolute_rate_units.value_namespace_prefix = name_space_prefix
                        if(value_path == "min-rate"):
                            self.min_rate = value
                            self.min_rate.value_namespace = name_space
                            self.min_rate.value_namespace_prefix = name_space_prefix
                        if(value_path == "rate-percent"):
                            self.rate_percent = value
                            self.rate_percent.value_namespace = name_space
                            self.rate_percent.value_namespace_prefix = name_space_prefix
                        if(value_path == "rate-ratio"):
                            self.rate_ratio = value
                            self.rate_ratio.value_namespace = name_space
                            self.rate_ratio.value_namespace_prefix = name_space_prefix


                class MaxRateCfg(Entity):
                    """
                    maximum rate attributes
                    
                    .. attribute:: absolute_rate
                    
                    	rate in bits per second
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: bits-per-second
                    
                    .. attribute:: absolute_rate_metric
                    
                    	Metric
                    	**type**\:   :py:class:`Metric <ydk.models.cisco_ios_xe.policy_types.Metric>`
                    
                    	**default value**\: none
                    
                    .. attribute:: absolute_rate_units
                    
                    	Rate basic units
                    	**type**\:   :py:class:`RateUnit <ydk.models.cisco_ios_xe.policy_types.RateUnit>`
                    
                    .. attribute:: burst_interval
                    
                    	burst interval
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: microsecond
                    
                    .. attribute:: burst_size
                    
                    	burst size
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: bytes
                    
                    .. attribute:: rate_percent
                    
                    	percent
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    .. attribute:: rate_ratio
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 1..65532
                    
                    

                    """

                    _prefix = 'action'
                    _revision = '2015-04-07'

                    def __init__(self):
                        super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MaxRateCfg, self).__init__()

                        self.yang_name = "max-rate-cfg"
                        self.yang_parent_name = "classifier-action-entry-cfg"

                        self.absolute_rate = YLeaf(YType.uint64, "absolute-rate")

                        self.absolute_rate_metric = YLeaf(YType.enumeration, "absolute-rate-metric")

                        self.absolute_rate_units = YLeaf(YType.enumeration, "absolute-rate-units")

                        self.burst_interval = YLeaf(YType.uint64, "burst-interval")

                        self.burst_size = YLeaf(YType.uint64, "burst-size")

                        self.rate_percent = YLeaf(YType.uint8, "rate-percent")

                        self.rate_ratio = YLeaf(YType.uint32, "rate-ratio")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("absolute_rate",
                                        "absolute_rate_metric",
                                        "absolute_rate_units",
                                        "burst_interval",
                                        "burst_size",
                                        "rate_percent",
                                        "rate_ratio") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MaxRateCfg, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MaxRateCfg, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.absolute_rate.is_set or
                            self.absolute_rate_metric.is_set or
                            self.absolute_rate_units.is_set or
                            self.burst_interval.is_set or
                            self.burst_size.is_set or
                            self.rate_percent.is_set or
                            self.rate_ratio.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.absolute_rate.yfilter != YFilter.not_set or
                            self.absolute_rate_metric.yfilter != YFilter.not_set or
                            self.absolute_rate_units.yfilter != YFilter.not_set or
                            self.burst_interval.yfilter != YFilter.not_set or
                            self.burst_size.yfilter != YFilter.not_set or
                            self.rate_percent.yfilter != YFilter.not_set or
                            self.rate_ratio.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ietf-diffserv-action:max-rate-cfg" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.absolute_rate.is_set or self.absolute_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.absolute_rate.get_name_leafdata())
                        if (self.absolute_rate_metric.is_set or self.absolute_rate_metric.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.absolute_rate_metric.get_name_leafdata())
                        if (self.absolute_rate_units.is_set or self.absolute_rate_units.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.absolute_rate_units.get_name_leafdata())
                        if (self.burst_interval.is_set or self.burst_interval.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.burst_interval.get_name_leafdata())
                        if (self.burst_size.is_set or self.burst_size.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.burst_size.get_name_leafdata())
                        if (self.rate_percent.is_set or self.rate_percent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rate_percent.get_name_leafdata())
                        if (self.rate_ratio.is_set or self.rate_ratio.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rate_ratio.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "absolute-rate" or name == "absolute-rate-metric" or name == "absolute-rate-units" or name == "burst-interval" or name == "burst-size" or name == "rate-percent" or name == "rate-ratio"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "absolute-rate"):
                            self.absolute_rate = value
                            self.absolute_rate.value_namespace = name_space
                            self.absolute_rate.value_namespace_prefix = name_space_prefix
                        if(value_path == "absolute-rate-metric"):
                            self.absolute_rate_metric = value
                            self.absolute_rate_metric.value_namespace = name_space
                            self.absolute_rate_metric.value_namespace_prefix = name_space_prefix
                        if(value_path == "absolute-rate-units"):
                            self.absolute_rate_units = value
                            self.absolute_rate_units.value_namespace = name_space
                            self.absolute_rate_units.value_namespace_prefix = name_space_prefix
                        if(value_path == "burst-interval"):
                            self.burst_interval = value
                            self.burst_interval.value_namespace = name_space
                            self.burst_interval.value_namespace_prefix = name_space_prefix
                        if(value_path == "burst-size"):
                            self.burst_size = value
                            self.burst_size.value_namespace = name_space
                            self.burst_size.value_namespace_prefix = name_space_prefix
                        if(value_path == "rate-percent"):
                            self.rate_percent = value
                            self.rate_percent.value_namespace = name_space
                            self.rate_percent.value_namespace_prefix = name_space_prefix
                        if(value_path == "rate-ratio"):
                            self.rate_ratio = value
                            self.rate_ratio.value_namespace = name_space
                            self.rate_ratio.value_namespace_prefix = name_space_prefix


                class DropCfg(Entity):
                    """
                    Always Drop configuration container
                    
                    .. attribute:: drop_action
                    
                    	always drop algorithm
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'action'
                    _revision = '2015-04-07'

                    def __init__(self):
                        super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.DropCfg, self).__init__()

                        self.yang_name = "drop-cfg"
                        self.yang_parent_name = "classifier-action-entry-cfg"

                        self.drop_action = YLeaf(YType.empty, "drop-action")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("drop_action") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.DropCfg, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.DropCfg, self).__setattr__(name, value)

                    def has_data(self):
                        return self.drop_action.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.drop_action.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ietf-diffserv-action:drop-cfg" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.drop_action.is_set or self.drop_action.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.drop_action.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "drop-action"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "drop-action"):
                            self.drop_action = value
                            self.drop_action.value_namespace = name_space
                            self.drop_action.value_namespace_prefix = name_space_prefix


                class TailDropCfg(Entity):
                    """
                    Tail Drop configuration container
                    
                    .. attribute:: qlimit_dscp_thresh
                    
                    	the queue limit per dscp range
                    	**type**\: list of    :py:class:`QlimitDscpThresh <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.TailDropCfg.QlimitDscpThresh>`
                    
                    

                    """

                    _prefix = 'action'
                    _revision = '2015-04-07'

                    def __init__(self):
                        super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.TailDropCfg, self).__init__()

                        self.yang_name = "tail-drop-cfg"
                        self.yang_parent_name = "classifier-action-entry-cfg"

                        self.qlimit_dscp_thresh = YList(self)

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
                                    super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.TailDropCfg, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.TailDropCfg, self).__setattr__(name, value)


                    class QlimitDscpThresh(Entity):
                        """
                        the queue limit per dscp range
                        
                        .. attribute:: dscp_min  <key>
                        
                        	Minimum of dscp range
                        	**type**\:  int
                        
                        	**range:** 0..63
                        
                        .. attribute:: dscp_max  <key>
                        
                        	Maximum of dscp range
                        	**type**\:  int
                        
                        	**range:** 0..63
                        
                        .. attribute:: threshold
                        
                        	threshold
                        	**type**\:   :py:class:`Threshold <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.TailDropCfg.QlimitDscpThresh.Threshold>`
                        
                        

                        """

                        _prefix = 'action'
                        _revision = '2015-04-07'

                        def __init__(self):
                            super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.TailDropCfg.QlimitDscpThresh, self).__init__()

                            self.yang_name = "qlimit-dscp-thresh"
                            self.yang_parent_name = "tail-drop-cfg"

                            self.dscp_min = YLeaf(YType.uint8, "dscp-min")

                            self.dscp_max = YLeaf(YType.uint8, "dscp-max")

                            self.threshold = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.TailDropCfg.QlimitDscpThresh.Threshold()
                            self.threshold.parent = self
                            self._children_name_map["threshold"] = "threshold"
                            self._children_yang_names.add("threshold")

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
                                        super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.TailDropCfg.QlimitDscpThresh, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.TailDropCfg.QlimitDscpThresh, self).__setattr__(name, value)


                        class Threshold(Entity):
                            """
                            threshold
                            
                            .. attribute:: threshold_interval
                            
                            	Threshold interval
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: microsecond
                            
                            .. attribute:: threshold_size
                            
                            	Threshold size
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: bytes
                            
                            

                            """

                            _prefix = 'action'
                            _revision = '2015-04-07'

                            def __init__(self):
                                super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.TailDropCfg.QlimitDscpThresh.Threshold, self).__init__()

                                self.yang_name = "threshold"
                                self.yang_parent_name = "qlimit-dscp-thresh"

                                self.threshold_interval = YLeaf(YType.uint64, "threshold-interval")

                                self.threshold_size = YLeaf(YType.uint64, "threshold-size")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("threshold_interval",
                                                "threshold_size") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.TailDropCfg.QlimitDscpThresh.Threshold, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.TailDropCfg.QlimitDscpThresh.Threshold, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.threshold_interval.is_set or
                                    self.threshold_size.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.threshold_interval.yfilter != YFilter.not_set or
                                    self.threshold_size.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "threshold" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.threshold_interval.is_set or self.threshold_interval.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.threshold_interval.get_name_leafdata())
                                if (self.threshold_size.is_set or self.threshold_size.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.threshold_size.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "threshold-interval" or name == "threshold-size"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "threshold-interval"):
                                    self.threshold_interval = value
                                    self.threshold_interval.value_namespace = name_space
                                    self.threshold_interval.value_namespace_prefix = name_space_prefix
                                if(value_path == "threshold-size"):
                                    self.threshold_size = value
                                    self.threshold_size.value_namespace = name_space
                                    self.threshold_size.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.dscp_min.is_set or
                                self.dscp_max.is_set or
                                (self.threshold is not None and self.threshold.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.dscp_min.yfilter != YFilter.not_set or
                                self.dscp_max.yfilter != YFilter.not_set or
                                (self.threshold is not None and self.threshold.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "qlimit-dscp-thresh" + "[dscp-min='" + self.dscp_min.get() + "']" + "[dscp-max='" + self.dscp_max.get() + "']" + path_buffer

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

                            if (child_yang_name == "threshold"):
                                if (self.threshold is None):
                                    self.threshold = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.TailDropCfg.QlimitDscpThresh.Threshold()
                                    self.threshold.parent = self
                                    self._children_name_map["threshold"] = "threshold"
                                return self.threshold

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "threshold" or name == "dscp-min" or name == "dscp-max"):
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

                    def has_data(self):
                        for c in self.qlimit_dscp_thresh:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.qlimit_dscp_thresh:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ietf-diffserv-action:tail-drop-cfg" + path_buffer

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

                        if (child_yang_name == "qlimit-dscp-thresh"):
                            for c in self.qlimit_dscp_thresh:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.TailDropCfg.QlimitDscpThresh()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.qlimit_dscp_thresh.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "qlimit-dscp-thresh"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class RandomDetectCfg(Entity):
                    """
                    Random Detect configuration container
                    
                    .. attribute:: exp_weighting_const
                    
                    	Exponential weighting constant factor for red profile 
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: mark_probability
                    
                    	Mark probability
                    	**type**\:  int
                    
                    	**range:** 1..1000
                    
                    .. attribute:: red_max_thresh
                    
                    	Maximum threshold
                    	**type**\:   :py:class:`RedMaxThresh <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg.RedMaxThresh>`
                    
                    .. attribute:: red_min_thresh
                    
                    	Minimum threshold
                    	**type**\:   :py:class:`RedMinThresh <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg.RedMinThresh>`
                    
                    

                    """

                    _prefix = 'action'
                    _revision = '2015-04-07'

                    def __init__(self):
                        super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg, self).__init__()

                        self.yang_name = "random-detect-cfg"
                        self.yang_parent_name = "classifier-action-entry-cfg"

                        self.exp_weighting_const = YLeaf(YType.uint32, "exp-weighting-const")

                        self.mark_probability = YLeaf(YType.uint32, "mark-probability")

                        self.red_max_thresh = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg.RedMaxThresh()
                        self.red_max_thresh.parent = self
                        self._children_name_map["red_max_thresh"] = "red-max-thresh"
                        self._children_yang_names.add("red-max-thresh")

                        self.red_min_thresh = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg.RedMinThresh()
                        self.red_min_thresh.parent = self
                        self._children_name_map["red_min_thresh"] = "red-min-thresh"
                        self._children_yang_names.add("red-min-thresh")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("exp_weighting_const",
                                        "mark_probability") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg, self).__setattr__(name, value)


                    class RedMinThresh(Entity):
                        """
                        Minimum threshold
                        
                        .. attribute:: threshold
                        
                        	threshold
                        	**type**\:   :py:class:`Threshold <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg.RedMinThresh.Threshold>`
                        
                        

                        """

                        _prefix = 'action'
                        _revision = '2015-04-07'

                        def __init__(self):
                            super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg.RedMinThresh, self).__init__()

                            self.yang_name = "red-min-thresh"
                            self.yang_parent_name = "random-detect-cfg"

                            self.threshold = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg.RedMinThresh.Threshold()
                            self.threshold.parent = self
                            self._children_name_map["threshold"] = "threshold"
                            self._children_yang_names.add("threshold")


                        class Threshold(Entity):
                            """
                            threshold
                            
                            .. attribute:: threshold_interval
                            
                            	Threshold interval
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: microsecond
                            
                            .. attribute:: threshold_size
                            
                            	Threshold size
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: bytes
                            
                            

                            """

                            _prefix = 'action'
                            _revision = '2015-04-07'

                            def __init__(self):
                                super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg.RedMinThresh.Threshold, self).__init__()

                                self.yang_name = "threshold"
                                self.yang_parent_name = "red-min-thresh"

                                self.threshold_interval = YLeaf(YType.uint64, "threshold-interval")

                                self.threshold_size = YLeaf(YType.uint64, "threshold-size")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("threshold_interval",
                                                "threshold_size") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg.RedMinThresh.Threshold, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg.RedMinThresh.Threshold, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.threshold_interval.is_set or
                                    self.threshold_size.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.threshold_interval.yfilter != YFilter.not_set or
                                    self.threshold_size.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "threshold" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.threshold_interval.is_set or self.threshold_interval.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.threshold_interval.get_name_leafdata())
                                if (self.threshold_size.is_set or self.threshold_size.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.threshold_size.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "threshold-interval" or name == "threshold-size"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "threshold-interval"):
                                    self.threshold_interval = value
                                    self.threshold_interval.value_namespace = name_space
                                    self.threshold_interval.value_namespace_prefix = name_space_prefix
                                if(value_path == "threshold-size"):
                                    self.threshold_size = value
                                    self.threshold_size.value_namespace = name_space
                                    self.threshold_size.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (self.threshold is not None and self.threshold.has_data())

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.threshold is not None and self.threshold.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "red-min-thresh" + path_buffer

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

                            if (child_yang_name == "threshold"):
                                if (self.threshold is None):
                                    self.threshold = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg.RedMinThresh.Threshold()
                                    self.threshold.parent = self
                                    self._children_name_map["threshold"] = "threshold"
                                return self.threshold

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "threshold"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class RedMaxThresh(Entity):
                        """
                        Maximum threshold
                        
                        .. attribute:: threshold
                        
                        	threshold
                        	**type**\:   :py:class:`Threshold <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg.RedMaxThresh.Threshold>`
                        
                        

                        """

                        _prefix = 'action'
                        _revision = '2015-04-07'

                        def __init__(self):
                            super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg.RedMaxThresh, self).__init__()

                            self.yang_name = "red-max-thresh"
                            self.yang_parent_name = "random-detect-cfg"

                            self.threshold = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg.RedMaxThresh.Threshold()
                            self.threshold.parent = self
                            self._children_name_map["threshold"] = "threshold"
                            self._children_yang_names.add("threshold")


                        class Threshold(Entity):
                            """
                            threshold
                            
                            .. attribute:: threshold_interval
                            
                            	Threshold interval
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: microsecond
                            
                            .. attribute:: threshold_size
                            
                            	Threshold size
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: bytes
                            
                            

                            """

                            _prefix = 'action'
                            _revision = '2015-04-07'

                            def __init__(self):
                                super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg.RedMaxThresh.Threshold, self).__init__()

                                self.yang_name = "threshold"
                                self.yang_parent_name = "red-max-thresh"

                                self.threshold_interval = YLeaf(YType.uint64, "threshold-interval")

                                self.threshold_size = YLeaf(YType.uint64, "threshold-size")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("threshold_interval",
                                                "threshold_size") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg.RedMaxThresh.Threshold, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg.RedMaxThresh.Threshold, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.threshold_interval.is_set or
                                    self.threshold_size.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.threshold_interval.yfilter != YFilter.not_set or
                                    self.threshold_size.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "threshold" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.threshold_interval.is_set or self.threshold_interval.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.threshold_interval.get_name_leafdata())
                                if (self.threshold_size.is_set or self.threshold_size.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.threshold_size.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "threshold-interval" or name == "threshold-size"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "threshold-interval"):
                                    self.threshold_interval = value
                                    self.threshold_interval.value_namespace = name_space
                                    self.threshold_interval.value_namespace_prefix = name_space_prefix
                                if(value_path == "threshold-size"):
                                    self.threshold_size = value
                                    self.threshold_size.value_namespace = name_space
                                    self.threshold_size.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (self.threshold is not None and self.threshold.has_data())

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.threshold is not None and self.threshold.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "red-max-thresh" + path_buffer

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

                            if (child_yang_name == "threshold"):
                                if (self.threshold is None):
                                    self.threshold = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg.RedMaxThresh.Threshold()
                                    self.threshold.parent = self
                                    self._children_name_map["threshold"] = "threshold"
                                return self.threshold

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "threshold"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.exp_weighting_const.is_set or
                            self.mark_probability.is_set or
                            (self.red_max_thresh is not None and self.red_max_thresh.has_data()) or
                            (self.red_min_thresh is not None and self.red_min_thresh.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.exp_weighting_const.yfilter != YFilter.not_set or
                            self.mark_probability.yfilter != YFilter.not_set or
                            (self.red_max_thresh is not None and self.red_max_thresh.has_operation()) or
                            (self.red_min_thresh is not None and self.red_min_thresh.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ietf-diffserv-action:random-detect-cfg" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.exp_weighting_const.is_set or self.exp_weighting_const.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.exp_weighting_const.get_name_leafdata())
                        if (self.mark_probability.is_set or self.mark_probability.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mark_probability.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "red-max-thresh"):
                            if (self.red_max_thresh is None):
                                self.red_max_thresh = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg.RedMaxThresh()
                                self.red_max_thresh.parent = self
                                self._children_name_map["red_max_thresh"] = "red-max-thresh"
                            return self.red_max_thresh

                        if (child_yang_name == "red-min-thresh"):
                            if (self.red_min_thresh is None):
                                self.red_min_thresh = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg.RedMinThresh()
                                self.red_min_thresh.parent = self
                                self._children_name_map["red_min_thresh"] = "red-min-thresh"
                            return self.red_min_thresh

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "red-max-thresh" or name == "red-min-thresh" or name == "exp-weighting-const" or name == "mark-probability"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "exp-weighting-const"):
                            self.exp_weighting_const = value
                            self.exp_weighting_const.value_namespace = name_space
                            self.exp_weighting_const.value_namespace_prefix = name_space_prefix
                        if(value_path == "mark-probability"):
                            self.mark_probability = value
                            self.mark_probability.value_namespace = name_space
                            self.mark_probability.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.action_type.is_set or
                        (self.drop_cfg is not None and self.drop_cfg.has_data()) or
                        (self.marking_cfg is not None and self.marking_cfg.has_data()) or
                        (self.max_rate_cfg is not None and self.max_rate_cfg.has_data()) or
                        (self.meter_cfg is not None and self.meter_cfg.has_data()) or
                        (self.min_rate_cfg is not None and self.min_rate_cfg.has_data()) or
                        (self.priority_cfg is not None and self.priority_cfg.has_data()) or
                        (self.random_detect_cfg is not None and self.random_detect_cfg.has_data()) or
                        (self.tail_drop_cfg is not None and self.tail_drop_cfg.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.action_type.yfilter != YFilter.not_set or
                        (self.drop_cfg is not None and self.drop_cfg.has_operation()) or
                        (self.marking_cfg is not None and self.marking_cfg.has_operation()) or
                        (self.max_rate_cfg is not None and self.max_rate_cfg.has_operation()) or
                        (self.meter_cfg is not None and self.meter_cfg.has_operation()) or
                        (self.min_rate_cfg is not None and self.min_rate_cfg.has_operation()) or
                        (self.priority_cfg is not None and self.priority_cfg.has_operation()) or
                        (self.random_detect_cfg is not None and self.random_detect_cfg.has_operation()) or
                        (self.tail_drop_cfg is not None and self.tail_drop_cfg.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "classifier-action-entry-cfg" + "[action-type='" + self.action_type.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.action_type.is_set or self.action_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.action_type.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "drop-cfg"):
                        if (self.drop_cfg is None):
                            self.drop_cfg = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.DropCfg()
                            self.drop_cfg.parent = self
                            self._children_name_map["drop_cfg"] = "drop-cfg"
                        return self.drop_cfg

                    if (child_yang_name == "marking-cfg"):
                        if (self.marking_cfg is None):
                            self.marking_cfg = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MarkingCfg()
                            self.marking_cfg.parent = self
                            self._children_name_map["marking_cfg"] = "marking-cfg"
                        return self.marking_cfg

                    if (child_yang_name == "max-rate-cfg"):
                        if (self.max_rate_cfg is None):
                            self.max_rate_cfg = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MaxRateCfg()
                            self.max_rate_cfg.parent = self
                            self._children_name_map["max_rate_cfg"] = "max-rate-cfg"
                        return self.max_rate_cfg

                    if (child_yang_name == "meter-cfg"):
                        if (self.meter_cfg is None):
                            self.meter_cfg = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg()
                            self.meter_cfg.parent = self
                            self._children_name_map["meter_cfg"] = "meter-cfg"
                        return self.meter_cfg

                    if (child_yang_name == "min-rate-cfg"):
                        if (self.min_rate_cfg is None):
                            self.min_rate_cfg = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MinRateCfg()
                            self.min_rate_cfg.parent = self
                            self._children_name_map["min_rate_cfg"] = "min-rate-cfg"
                        return self.min_rate_cfg

                    if (child_yang_name == "priority-cfg"):
                        if (self.priority_cfg is None):
                            self.priority_cfg = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.PriorityCfg()
                            self.priority_cfg.parent = self
                            self._children_name_map["priority_cfg"] = "priority-cfg"
                        return self.priority_cfg

                    if (child_yang_name == "random-detect-cfg"):
                        if (self.random_detect_cfg is None):
                            self.random_detect_cfg = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg()
                            self.random_detect_cfg.parent = self
                            self._children_name_map["random_detect_cfg"] = "random-detect-cfg"
                        return self.random_detect_cfg

                    if (child_yang_name == "tail-drop-cfg"):
                        if (self.tail_drop_cfg is None):
                            self.tail_drop_cfg = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.TailDropCfg()
                            self.tail_drop_cfg.parent = self
                            self._children_name_map["tail_drop_cfg"] = "tail-drop-cfg"
                        return self.tail_drop_cfg

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "drop-cfg" or name == "marking-cfg" or name == "max-rate-cfg" or name == "meter-cfg" or name == "min-rate-cfg" or name == "priority-cfg" or name == "random-detect-cfg" or name == "tail-drop-cfg" or name == "action-type"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "action-type"):
                        self.action_type = value
                        self.action_type.value_namespace = name_space
                        self.action_type.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.classifier_action_entry_cfg:
                    if (c.has_data()):
                        return True
                for c in self.filter_entry:
                    if (c.has_data()):
                        return True
                return (
                    self.classifier_entry_name.is_set or
                    self.classifier_entry_filter_oper.is_set or
                    self.classifier_entry_inline.is_set)

            def has_operation(self):
                for c in self.classifier_action_entry_cfg:
                    if (c.has_operation()):
                        return True
                for c in self.filter_entry:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.classifier_entry_name.yfilter != YFilter.not_set or
                    self.classifier_entry_filter_oper.yfilter != YFilter.not_set or
                    self.classifier_entry_inline.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "classifier-entry" + "[classifier-entry-name='" + self.classifier_entry_name.get() + "']" + path_buffer

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
                if (self.classifier_entry_filter_oper.is_set or self.classifier_entry_filter_oper.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.classifier_entry_filter_oper.get_name_leafdata())
                if (self.classifier_entry_inline.is_set or self.classifier_entry_inline.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.classifier_entry_inline.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "classifier-action-entry-cfg"):
                    for c in self.classifier_action_entry_cfg:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.classifier_action_entry_cfg.append(c)
                    return c

                if (child_yang_name == "filter-entry"):
                    for c in self.filter_entry:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Policies.PolicyEntry.ClassifierEntry.FilterEntry()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.filter_entry.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "classifier-action-entry-cfg" or name == "filter-entry" or name == "classifier-entry-name" or name == "classifier-entry-filter-oper" or name == "classifier-entry-inline"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "classifier-entry-name"):
                    self.classifier_entry_name = value
                    self.classifier_entry_name.value_namespace = name_space
                    self.classifier_entry_name.value_namespace_prefix = name_space_prefix
                if(value_path == "classifier-entry-filter-oper"):
                    self.classifier_entry_filter_oper = value
                    self.classifier_entry_filter_oper.value_namespace = name_space
                    self.classifier_entry_filter_oper.value_namespace_prefix = name_space_prefix
                if(value_path == "classifier-entry-inline"):
                    self.classifier_entry_inline = value
                    self.classifier_entry_inline.value_namespace = name_space
                    self.classifier_entry_inline.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.classifier_entry:
                if (c.has_data()):
                    return True
            return (
                self.policy_name.is_set or
                self.policy_descr.is_set or
                self.policy_type.is_set)

        def has_operation(self):
            for c in self.classifier_entry:
                if (c.has_operation()):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.policy_name.yfilter != YFilter.not_set or
                self.policy_descr.yfilter != YFilter.not_set or
                self.policy_type.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "policy-entry" + "[policy-name='" + self.policy_name.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ietf-diffserv-policy:policies/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.policy_name.is_set or self.policy_name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.policy_name.get_name_leafdata())
            if (self.policy_descr.is_set or self.policy_descr.yfilter != YFilter.not_set):
                leaf_name_data.append(self.policy_descr.get_name_leafdata())
            if (self.policy_type.is_set or self.policy_type.yfilter != YFilter.not_set):
                leaf_name_data.append(self.policy_type.get_name_leafdata())

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
                c = Policies.PolicyEntry.ClassifierEntry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.classifier_entry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "classifier-entry" or name == "policy-name" or name == "policy-descr" or name == "policy-type"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "policy-name"):
                self.policy_name = value
                self.policy_name.value_namespace = name_space
                self.policy_name.value_namespace_prefix = name_space_prefix
            if(value_path == "policy-descr"):
                self.policy_descr = value
                self.policy_descr.value_namespace = name_space
                self.policy_descr.value_namespace_prefix = name_space_prefix
            if(value_path == "policy-type"):
                self.policy_type = value
                self.policy_type.value_namespace = name_space
                self.policy_type.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.policy_entry:
            if (c.has_data()):
                return True
        return False

    def has_operation(self):
        for c in self.policy_entry:
            if (c.has_operation()):
                return True
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "ietf-diffserv-policy:policies" + path_buffer

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

        if (child_yang_name == "policy-entry"):
            for c in self.policy_entry:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = Policies.PolicyEntry()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.policy_entry.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "policy-entry"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Policies()
        return self._top_entity


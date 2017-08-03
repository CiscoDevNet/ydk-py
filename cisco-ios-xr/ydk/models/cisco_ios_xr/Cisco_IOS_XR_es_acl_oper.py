""" Cisco_IOS_XR_es_acl_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR es\-acl package operational data.

This module contains definitions
for the following management objects\:
  es\-acl\: Root class of ES ACL Oper schema tree

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class AclAce1(Enum):
    """
    AclAce1

    ACE Types

    .. data:: normal = 0

    	This is Normal ACE

    .. data:: remark = 1

    	This is Remark ACE

    .. data:: abf = 2

    	This is ABF ACE

    """

    normal = Enum.YLeaf(0, "normal")

    remark = Enum.YLeaf(1, "remark")

    abf = Enum.YLeaf(2, "abf")


class AclAce1(Enum):
    """
    AclAce1

    ACE Types

    .. data:: normal = 0

    	This is Normal ACE

    .. data:: remark = 1

    	This is Remark ACE

    .. data:: abf = 2

    	This is ABF ACE

    """

    normal = Enum.YLeaf(0, "normal")

    remark = Enum.YLeaf(1, "remark")

    abf = Enum.YLeaf(2, "abf")


class AclAction(Enum):
    """
    AclAction

    Acl action

    .. data:: deny = 0

    	Deny

    .. data:: permit = 1

    	Permit

    .. data:: encrypt = 2

    	Encrypt

    .. data:: bypass = 3

    	Bypass

    .. data:: fallthrough = 4

    	Fallthrough

    .. data:: invalid = 5

    	Invalid

    """

    deny = Enum.YLeaf(0, "deny")

    permit = Enum.YLeaf(1, "permit")

    encrypt = Enum.YLeaf(2, "encrypt")

    bypass = Enum.YLeaf(3, "bypass")

    fallthrough = Enum.YLeaf(4, "fallthrough")

    invalid = Enum.YLeaf(5, "invalid")



class EsAcl(Entity):
    """
    Root class of ES ACL Oper schema tree
    
    .. attribute:: active
    
    	Out Of Resources, Limits to the resources allocatable
    	**type**\:   :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.EsAcl.Active>`
    
    

    """

    _prefix = 'es-acl-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(EsAcl, self).__init__()
        self._top_entity = None

        self.yang_name = "es-acl"
        self.yang_parent_name = "Cisco-IOS-XR-es-acl-oper"

        self.active = EsAcl.Active()
        self.active.parent = self
        self._children_name_map["active"] = "active"
        self._children_yang_names.add("active")


    class Active(Entity):
        """
        Out Of Resources, Limits to the resources
        allocatable
        
        .. attribute:: list
        
        	List containing ACLs
        	**type**\:   :py:class:`List <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.EsAcl.Active.List>`
        
        .. attribute:: oor
        
        	Out Of Resources, Limits to the resources allocatable
        	**type**\:   :py:class:`Oor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.EsAcl.Active.Oor>`
        
        .. attribute:: oor_acls
        
        	Resource occupation details for ACLs
        	**type**\:   :py:class:`OorAcls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.EsAcl.Active.OorAcls>`
        
        .. attribute:: usages
        
        	Table of Usage statistics of ACLs at different nodes
        	**type**\:   :py:class:`Usages <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.EsAcl.Active.Usages>`
        
        

        """

        _prefix = 'es-acl-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(EsAcl.Active, self).__init__()

            self.yang_name = "active"
            self.yang_parent_name = "es-acl"

            self.list = EsAcl.Active.List()
            self.list.parent = self
            self._children_name_map["list"] = "list"
            self._children_yang_names.add("list")

            self.oor = EsAcl.Active.Oor()
            self.oor.parent = self
            self._children_name_map["oor"] = "oor"
            self._children_yang_names.add("oor")

            self.oor_acls = EsAcl.Active.OorAcls()
            self.oor_acls.parent = self
            self._children_name_map["oor_acls"] = "oor-acls"
            self._children_yang_names.add("oor-acls")

            self.usages = EsAcl.Active.Usages()
            self.usages.parent = self
            self._children_name_map["usages"] = "usages"
            self._children_yang_names.add("usages")


        class Oor(Entity):
            """
            Out Of Resources, Limits to the resources
            allocatable
            
            .. attribute:: acl_summary
            
            	Resource Limits pertaining to ACLs only
            	**type**\:   :py:class:`AclSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.EsAcl.Active.Oor.AclSummary>`
            
            

            """

            _prefix = 'es-acl-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(EsAcl.Active.Oor, self).__init__()

                self.yang_name = "oor"
                self.yang_parent_name = "active"

                self.acl_summary = EsAcl.Active.Oor.AclSummary()
                self.acl_summary.parent = self
                self._children_name_map["acl_summary"] = "acl-summary"
                self._children_yang_names.add("acl-summary")


            class AclSummary(Entity):
                """
                Resource Limits pertaining to ACLs only
                
                .. attribute:: details
                
                	Details containing the resource limits of the ACLs
                	**type**\:   :py:class:`Details <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.EsAcl.Active.Oor.AclSummary.Details>`
                
                

                """

                _prefix = 'es-acl-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(EsAcl.Active.Oor.AclSummary, self).__init__()

                    self.yang_name = "acl-summary"
                    self.yang_parent_name = "oor"

                    self.details = EsAcl.Active.Oor.AclSummary.Details()
                    self.details.parent = self
                    self._children_name_map["details"] = "details"
                    self._children_yang_names.add("details")


                class Details(Entity):
                    """
                    Details containing the resource limits of the
                    ACLs
                    
                    .. attribute:: current_configured_ac_es
                    
                    	Current configured aces
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: current_configured_ac_ls
                    
                    	Current configured acls
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: maximum_configurable_ac_es
                    
                    	max configurable aces
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: maximum_configurable_ac_ls
                    
                    	max configurable acls
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'es-acl-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(EsAcl.Active.Oor.AclSummary.Details, self).__init__()

                        self.yang_name = "details"
                        self.yang_parent_name = "acl-summary"

                        self.current_configured_ac_es = YLeaf(YType.uint32, "current-configured-ac-es")

                        self.current_configured_ac_ls = YLeaf(YType.uint32, "current-configured-ac-ls")

                        self.maximum_configurable_ac_es = YLeaf(YType.uint32, "maximum-configurable-ac-es")

                        self.maximum_configurable_ac_ls = YLeaf(YType.uint32, "maximum-configurable-ac-ls")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("current_configured_ac_es",
                                        "current_configured_ac_ls",
                                        "maximum_configurable_ac_es",
                                        "maximum_configurable_ac_ls") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(EsAcl.Active.Oor.AclSummary.Details, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(EsAcl.Active.Oor.AclSummary.Details, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.current_configured_ac_es.is_set or
                            self.current_configured_ac_ls.is_set or
                            self.maximum_configurable_ac_es.is_set or
                            self.maximum_configurable_ac_ls.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.current_configured_ac_es.yfilter != YFilter.not_set or
                            self.current_configured_ac_ls.yfilter != YFilter.not_set or
                            self.maximum_configurable_ac_es.yfilter != YFilter.not_set or
                            self.maximum_configurable_ac_ls.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "details" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-es-acl-oper:es-acl/active/oor/acl-summary/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.current_configured_ac_es.is_set or self.current_configured_ac_es.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.current_configured_ac_es.get_name_leafdata())
                        if (self.current_configured_ac_ls.is_set or self.current_configured_ac_ls.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.current_configured_ac_ls.get_name_leafdata())
                        if (self.maximum_configurable_ac_es.is_set or self.maximum_configurable_ac_es.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.maximum_configurable_ac_es.get_name_leafdata())
                        if (self.maximum_configurable_ac_ls.is_set or self.maximum_configurable_ac_ls.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.maximum_configurable_ac_ls.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "current-configured-ac-es" or name == "current-configured-ac-ls" or name == "maximum-configurable-ac-es" or name == "maximum-configurable-ac-ls"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "current-configured-ac-es"):
                            self.current_configured_ac_es = value
                            self.current_configured_ac_es.value_namespace = name_space
                            self.current_configured_ac_es.value_namespace_prefix = name_space_prefix
                        if(value_path == "current-configured-ac-ls"):
                            self.current_configured_ac_ls = value
                            self.current_configured_ac_ls.value_namespace = name_space
                            self.current_configured_ac_ls.value_namespace_prefix = name_space_prefix
                        if(value_path == "maximum-configurable-ac-es"):
                            self.maximum_configurable_ac_es = value
                            self.maximum_configurable_ac_es.value_namespace = name_space
                            self.maximum_configurable_ac_es.value_namespace_prefix = name_space_prefix
                        if(value_path == "maximum-configurable-ac-ls"):
                            self.maximum_configurable_ac_ls = value
                            self.maximum_configurable_ac_ls.value_namespace = name_space
                            self.maximum_configurable_ac_ls.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (self.details is not None and self.details.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.details is not None and self.details.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "acl-summary" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-es-acl-oper:es-acl/active/oor/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "details"):
                        if (self.details is None):
                            self.details = EsAcl.Active.Oor.AclSummary.Details()
                            self.details.parent = self
                            self._children_name_map["details"] = "details"
                        return self.details

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "details"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (self.acl_summary is not None and self.acl_summary.has_data())

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.acl_summary is not None and self.acl_summary.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "oor" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-es-acl-oper:es-acl/active/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "acl-summary"):
                    if (self.acl_summary is None):
                        self.acl_summary = EsAcl.Active.Oor.AclSummary()
                        self.acl_summary.parent = self
                        self._children_name_map["acl_summary"] = "acl-summary"
                    return self.acl_summary

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "acl-summary"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class List(Entity):
            """
            List containing ACLs
            
            .. attribute:: acls
            
            	ACL class displaying Usage and Entries
            	**type**\:   :py:class:`Acls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.EsAcl.Active.List.Acls>`
            
            

            """

            _prefix = 'es-acl-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(EsAcl.Active.List, self).__init__()

                self.yang_name = "list"
                self.yang_parent_name = "active"

                self.acls = EsAcl.Active.List.Acls()
                self.acls.parent = self
                self._children_name_map["acls"] = "acls"
                self._children_yang_names.add("acls")


            class Acls(Entity):
                """
                ACL class displaying Usage and Entries
                
                .. attribute:: acl
                
                	Name of the Access List
                	**type**\: list of    :py:class:`Acl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.EsAcl.Active.List.Acls.Acl>`
                
                

                """

                _prefix = 'es-acl-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(EsAcl.Active.List.Acls, self).__init__()

                    self.yang_name = "acls"
                    self.yang_parent_name = "list"

                    self.acl = YList(self)

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
                                super(EsAcl.Active.List.Acls, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(EsAcl.Active.List.Acls, self).__setattr__(name, value)


                class Acl(Entity):
                    """
                    Name of the Access List
                    
                    .. attribute:: name  <key>
                    
                    	Name of the Access List
                    	**type**\:  str
                    
                    	**length:** 1..65
                    
                    .. attribute:: acl_sequence_numbers
                    
                    	Table of all the SequenceNumbers per ACL
                    	**type**\:   :py:class:`AclSequenceNumbers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.EsAcl.Active.List.Acls.Acl.AclSequenceNumbers>`
                    
                    

                    """

                    _prefix = 'es-acl-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(EsAcl.Active.List.Acls.Acl, self).__init__()

                        self.yang_name = "acl"
                        self.yang_parent_name = "acls"

                        self.name = YLeaf(YType.str, "name")

                        self.acl_sequence_numbers = EsAcl.Active.List.Acls.Acl.AclSequenceNumbers()
                        self.acl_sequence_numbers.parent = self
                        self._children_name_map["acl_sequence_numbers"] = "acl-sequence-numbers"
                        self._children_yang_names.add("acl-sequence-numbers")

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
                                    super(EsAcl.Active.List.Acls.Acl, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(EsAcl.Active.List.Acls.Acl, self).__setattr__(name, value)


                    class AclSequenceNumbers(Entity):
                        """
                        Table of all the SequenceNumbers per ACL
                        
                        .. attribute:: acl_sequence_number
                        
                        	Sequence Number of an ACL entry
                        	**type**\: list of    :py:class:`AclSequenceNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.EsAcl.Active.List.Acls.Acl.AclSequenceNumbers.AclSequenceNumber>`
                        
                        

                        """

                        _prefix = 'es-acl-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(EsAcl.Active.List.Acls.Acl.AclSequenceNumbers, self).__init__()

                            self.yang_name = "acl-sequence-numbers"
                            self.yang_parent_name = "acl"

                            self.acl_sequence_number = YList(self)

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
                                        super(EsAcl.Active.List.Acls.Acl.AclSequenceNumbers, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(EsAcl.Active.List.Acls.Acl.AclSequenceNumbers, self).__setattr__(name, value)


                        class AclSequenceNumber(Entity):
                            """
                            Sequence Number of an ACL entry
                            
                            .. attribute:: sequence_number  <key>
                            
                            	ACLEntry Sequence Number
                            	**type**\:  int
                            
                            	**range:** 1..2147483646
                            
                            .. attribute:: ace_sequence_number
                            
                            	ACE sequence number
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ace_type
                            
                            	ACE type (acl, remark)
                            	**type**\:   :py:class:`AclAce1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.AclAce1>`
                            
                            .. attribute:: acl_name
                            
                            	Acl Name
                            	**type**\:  str
                            
                            .. attribute:: capture
                            
                            	Capture option, TRUE if enabled
                            	**type**\:  bool
                            
                            .. attribute:: cos
                            
                            	COS value
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: dei
                            
                            	DEI bit
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: destination_address
                            
                            	Destination MAC address
                            	**type**\:  str
                            
                            	**pattern:** [a\-fA\-F0\-9]{4}(\\.[a\-fA\-F0\-9]{4}){2}
                            
                            .. attribute:: destination_wild_card_bits
                            
                            	Destination wild card bits
                            	**type**\:  str
                            
                            	**pattern:** [a\-fA\-F0\-9]{4}(\\.[a\-fA\-F0\-9]{4}){2}
                            
                            .. attribute:: ether_type_number
                            
                            	Ethernet type Number
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: grant
                            
                            	Grant value permit/deny 
                            	**type**\:   :py:class:`AclAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.AclAction>`
                            
                            .. attribute:: hits
                            
                            	ACE hit number
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: inner_header_cos
                            
                            	Inner header COS value
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: inner_header_dei
                            
                            	Inner header DEI bit
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: inner_header_vlan1
                            
                            	Inner header VLAN ID/range lower limit
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: inner_header_vlan2
                            
                            	Inner header VLAN ID range higher limit
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: log_option
                            
                            	Log option
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: remark
                            
                            	Remark string
                            	**type**\:  str
                            
                            .. attribute:: sequence_string
                            
                            	Sequence Sring
                            	**type**\:  str
                            
                            .. attribute:: source_address
                            
                            	Source MAC address
                            	**type**\:  str
                            
                            	**pattern:** [a\-fA\-F0\-9]{4}(\\.[a\-fA\-F0\-9]{4}){2}
                            
                            .. attribute:: source_wild_card_bits
                            
                            	Source wild card bits
                            	**type**\:  str
                            
                            	**pattern:** [a\-fA\-F0\-9]{4}(\\.[a\-fA\-F0\-9]{4}){2}
                            
                            .. attribute:: vlan1
                            
                            	VLAN ID/range lower limit
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: vlan2
                            
                            	VLAN ID range higher limit
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'es-acl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(EsAcl.Active.List.Acls.Acl.AclSequenceNumbers.AclSequenceNumber, self).__init__()

                                self.yang_name = "acl-sequence-number"
                                self.yang_parent_name = "acl-sequence-numbers"

                                self.sequence_number = YLeaf(YType.uint32, "sequence-number")

                                self.ace_sequence_number = YLeaf(YType.uint32, "ace-sequence-number")

                                self.ace_type = YLeaf(YType.enumeration, "ace-type")

                                self.acl_name = YLeaf(YType.str, "acl-name")

                                self.capture = YLeaf(YType.boolean, "capture")

                                self.cos = YLeaf(YType.uint8, "cos")

                                self.dei = YLeaf(YType.uint8, "dei")

                                self.destination_address = YLeaf(YType.str, "destination-address")

                                self.destination_wild_card_bits = YLeaf(YType.str, "destination-wild-card-bits")

                                self.ether_type_number = YLeaf(YType.uint16, "ether-type-number")

                                self.grant = YLeaf(YType.enumeration, "grant")

                                self.hits = YLeaf(YType.uint64, "hits")

                                self.inner_header_cos = YLeaf(YType.uint8, "inner-header-cos")

                                self.inner_header_dei = YLeaf(YType.uint8, "inner-header-dei")

                                self.inner_header_vlan1 = YLeaf(YType.uint16, "inner-header-vlan1")

                                self.inner_header_vlan2 = YLeaf(YType.uint16, "inner-header-vlan2")

                                self.log_option = YLeaf(YType.uint8, "log-option")

                                self.remark = YLeaf(YType.str, "remark")

                                self.sequence_string = YLeaf(YType.str, "sequence-string")

                                self.source_address = YLeaf(YType.str, "source-address")

                                self.source_wild_card_bits = YLeaf(YType.str, "source-wild-card-bits")

                                self.vlan1 = YLeaf(YType.uint16, "vlan1")

                                self.vlan2 = YLeaf(YType.uint16, "vlan2")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("sequence_number",
                                                "ace_sequence_number",
                                                "ace_type",
                                                "acl_name",
                                                "capture",
                                                "cos",
                                                "dei",
                                                "destination_address",
                                                "destination_wild_card_bits",
                                                "ether_type_number",
                                                "grant",
                                                "hits",
                                                "inner_header_cos",
                                                "inner_header_dei",
                                                "inner_header_vlan1",
                                                "inner_header_vlan2",
                                                "log_option",
                                                "remark",
                                                "sequence_string",
                                                "source_address",
                                                "source_wild_card_bits",
                                                "vlan1",
                                                "vlan2") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(EsAcl.Active.List.Acls.Acl.AclSequenceNumbers.AclSequenceNumber, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(EsAcl.Active.List.Acls.Acl.AclSequenceNumbers.AclSequenceNumber, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.sequence_number.is_set or
                                    self.ace_sequence_number.is_set or
                                    self.ace_type.is_set or
                                    self.acl_name.is_set or
                                    self.capture.is_set or
                                    self.cos.is_set or
                                    self.dei.is_set or
                                    self.destination_address.is_set or
                                    self.destination_wild_card_bits.is_set or
                                    self.ether_type_number.is_set or
                                    self.grant.is_set or
                                    self.hits.is_set or
                                    self.inner_header_cos.is_set or
                                    self.inner_header_dei.is_set or
                                    self.inner_header_vlan1.is_set or
                                    self.inner_header_vlan2.is_set or
                                    self.log_option.is_set or
                                    self.remark.is_set or
                                    self.sequence_string.is_set or
                                    self.source_address.is_set or
                                    self.source_wild_card_bits.is_set or
                                    self.vlan1.is_set or
                                    self.vlan2.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.sequence_number.yfilter != YFilter.not_set or
                                    self.ace_sequence_number.yfilter != YFilter.not_set or
                                    self.ace_type.yfilter != YFilter.not_set or
                                    self.acl_name.yfilter != YFilter.not_set or
                                    self.capture.yfilter != YFilter.not_set or
                                    self.cos.yfilter != YFilter.not_set or
                                    self.dei.yfilter != YFilter.not_set or
                                    self.destination_address.yfilter != YFilter.not_set or
                                    self.destination_wild_card_bits.yfilter != YFilter.not_set or
                                    self.ether_type_number.yfilter != YFilter.not_set or
                                    self.grant.yfilter != YFilter.not_set or
                                    self.hits.yfilter != YFilter.not_set or
                                    self.inner_header_cos.yfilter != YFilter.not_set or
                                    self.inner_header_dei.yfilter != YFilter.not_set or
                                    self.inner_header_vlan1.yfilter != YFilter.not_set or
                                    self.inner_header_vlan2.yfilter != YFilter.not_set or
                                    self.log_option.yfilter != YFilter.not_set or
                                    self.remark.yfilter != YFilter.not_set or
                                    self.sequence_string.yfilter != YFilter.not_set or
                                    self.source_address.yfilter != YFilter.not_set or
                                    self.source_wild_card_bits.yfilter != YFilter.not_set or
                                    self.vlan1.yfilter != YFilter.not_set or
                                    self.vlan2.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "acl-sequence-number" + "[sequence-number='" + self.sequence_number.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.sequence_number.is_set or self.sequence_number.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.sequence_number.get_name_leafdata())
                                if (self.ace_sequence_number.is_set or self.ace_sequence_number.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ace_sequence_number.get_name_leafdata())
                                if (self.ace_type.is_set or self.ace_type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ace_type.get_name_leafdata())
                                if (self.acl_name.is_set or self.acl_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.acl_name.get_name_leafdata())
                                if (self.capture.is_set or self.capture.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.capture.get_name_leafdata())
                                if (self.cos.is_set or self.cos.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.cos.get_name_leafdata())
                                if (self.dei.is_set or self.dei.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.dei.get_name_leafdata())
                                if (self.destination_address.is_set or self.destination_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.destination_address.get_name_leafdata())
                                if (self.destination_wild_card_bits.is_set or self.destination_wild_card_bits.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.destination_wild_card_bits.get_name_leafdata())
                                if (self.ether_type_number.is_set or self.ether_type_number.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ether_type_number.get_name_leafdata())
                                if (self.grant.is_set or self.grant.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.grant.get_name_leafdata())
                                if (self.hits.is_set or self.hits.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.hits.get_name_leafdata())
                                if (self.inner_header_cos.is_set or self.inner_header_cos.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.inner_header_cos.get_name_leafdata())
                                if (self.inner_header_dei.is_set or self.inner_header_dei.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.inner_header_dei.get_name_leafdata())
                                if (self.inner_header_vlan1.is_set or self.inner_header_vlan1.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.inner_header_vlan1.get_name_leafdata())
                                if (self.inner_header_vlan2.is_set or self.inner_header_vlan2.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.inner_header_vlan2.get_name_leafdata())
                                if (self.log_option.is_set or self.log_option.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.log_option.get_name_leafdata())
                                if (self.remark.is_set or self.remark.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.remark.get_name_leafdata())
                                if (self.sequence_string.is_set or self.sequence_string.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.sequence_string.get_name_leafdata())
                                if (self.source_address.is_set or self.source_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.source_address.get_name_leafdata())
                                if (self.source_wild_card_bits.is_set or self.source_wild_card_bits.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.source_wild_card_bits.get_name_leafdata())
                                if (self.vlan1.is_set or self.vlan1.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.vlan1.get_name_leafdata())
                                if (self.vlan2.is_set or self.vlan2.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.vlan2.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "sequence-number" or name == "ace-sequence-number" or name == "ace-type" or name == "acl-name" or name == "capture" or name == "cos" or name == "dei" or name == "destination-address" or name == "destination-wild-card-bits" or name == "ether-type-number" or name == "grant" or name == "hits" or name == "inner-header-cos" or name == "inner-header-dei" or name == "inner-header-vlan1" or name == "inner-header-vlan2" or name == "log-option" or name == "remark" or name == "sequence-string" or name == "source-address" or name == "source-wild-card-bits" or name == "vlan1" or name == "vlan2"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "sequence-number"):
                                    self.sequence_number = value
                                    self.sequence_number.value_namespace = name_space
                                    self.sequence_number.value_namespace_prefix = name_space_prefix
                                if(value_path == "ace-sequence-number"):
                                    self.ace_sequence_number = value
                                    self.ace_sequence_number.value_namespace = name_space
                                    self.ace_sequence_number.value_namespace_prefix = name_space_prefix
                                if(value_path == "ace-type"):
                                    self.ace_type = value
                                    self.ace_type.value_namespace = name_space
                                    self.ace_type.value_namespace_prefix = name_space_prefix
                                if(value_path == "acl-name"):
                                    self.acl_name = value
                                    self.acl_name.value_namespace = name_space
                                    self.acl_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "capture"):
                                    self.capture = value
                                    self.capture.value_namespace = name_space
                                    self.capture.value_namespace_prefix = name_space_prefix
                                if(value_path == "cos"):
                                    self.cos = value
                                    self.cos.value_namespace = name_space
                                    self.cos.value_namespace_prefix = name_space_prefix
                                if(value_path == "dei"):
                                    self.dei = value
                                    self.dei.value_namespace = name_space
                                    self.dei.value_namespace_prefix = name_space_prefix
                                if(value_path == "destination-address"):
                                    self.destination_address = value
                                    self.destination_address.value_namespace = name_space
                                    self.destination_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "destination-wild-card-bits"):
                                    self.destination_wild_card_bits = value
                                    self.destination_wild_card_bits.value_namespace = name_space
                                    self.destination_wild_card_bits.value_namespace_prefix = name_space_prefix
                                if(value_path == "ether-type-number"):
                                    self.ether_type_number = value
                                    self.ether_type_number.value_namespace = name_space
                                    self.ether_type_number.value_namespace_prefix = name_space_prefix
                                if(value_path == "grant"):
                                    self.grant = value
                                    self.grant.value_namespace = name_space
                                    self.grant.value_namespace_prefix = name_space_prefix
                                if(value_path == "hits"):
                                    self.hits = value
                                    self.hits.value_namespace = name_space
                                    self.hits.value_namespace_prefix = name_space_prefix
                                if(value_path == "inner-header-cos"):
                                    self.inner_header_cos = value
                                    self.inner_header_cos.value_namespace = name_space
                                    self.inner_header_cos.value_namespace_prefix = name_space_prefix
                                if(value_path == "inner-header-dei"):
                                    self.inner_header_dei = value
                                    self.inner_header_dei.value_namespace = name_space
                                    self.inner_header_dei.value_namespace_prefix = name_space_prefix
                                if(value_path == "inner-header-vlan1"):
                                    self.inner_header_vlan1 = value
                                    self.inner_header_vlan1.value_namespace = name_space
                                    self.inner_header_vlan1.value_namespace_prefix = name_space_prefix
                                if(value_path == "inner-header-vlan2"):
                                    self.inner_header_vlan2 = value
                                    self.inner_header_vlan2.value_namespace = name_space
                                    self.inner_header_vlan2.value_namespace_prefix = name_space_prefix
                                if(value_path == "log-option"):
                                    self.log_option = value
                                    self.log_option.value_namespace = name_space
                                    self.log_option.value_namespace_prefix = name_space_prefix
                                if(value_path == "remark"):
                                    self.remark = value
                                    self.remark.value_namespace = name_space
                                    self.remark.value_namespace_prefix = name_space_prefix
                                if(value_path == "sequence-string"):
                                    self.sequence_string = value
                                    self.sequence_string.value_namespace = name_space
                                    self.sequence_string.value_namespace_prefix = name_space_prefix
                                if(value_path == "source-address"):
                                    self.source_address = value
                                    self.source_address.value_namespace = name_space
                                    self.source_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "source-wild-card-bits"):
                                    self.source_wild_card_bits = value
                                    self.source_wild_card_bits.value_namespace = name_space
                                    self.source_wild_card_bits.value_namespace_prefix = name_space_prefix
                                if(value_path == "vlan1"):
                                    self.vlan1 = value
                                    self.vlan1.value_namespace = name_space
                                    self.vlan1.value_namespace_prefix = name_space_prefix
                                if(value_path == "vlan2"):
                                    self.vlan2 = value
                                    self.vlan2.value_namespace = name_space
                                    self.vlan2.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.acl_sequence_number:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.acl_sequence_number:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "acl-sequence-numbers" + path_buffer

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

                            if (child_yang_name == "acl-sequence-number"):
                                for c in self.acl_sequence_number:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = EsAcl.Active.List.Acls.Acl.AclSequenceNumbers.AclSequenceNumber()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.acl_sequence_number.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "acl-sequence-number"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.name.is_set or
                            (self.acl_sequence_numbers is not None and self.acl_sequence_numbers.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set or
                            (self.acl_sequence_numbers is not None and self.acl_sequence_numbers.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "acl" + "[name='" + self.name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-es-acl-oper:es-acl/active/list/acls/%s" % self.get_segment_path()
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

                        if (child_yang_name == "acl-sequence-numbers"):
                            if (self.acl_sequence_numbers is None):
                                self.acl_sequence_numbers = EsAcl.Active.List.Acls.Acl.AclSequenceNumbers()
                                self.acl_sequence_numbers.parent = self
                                self._children_name_map["acl_sequence_numbers"] = "acl-sequence-numbers"
                            return self.acl_sequence_numbers

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "acl-sequence-numbers" or name == "name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.acl:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.acl:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "acls" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-es-acl-oper:es-acl/active/list/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "acl"):
                        for c in self.acl:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = EsAcl.Active.List.Acls.Acl()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.acl.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "acl"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (self.acls is not None and self.acls.has_data())

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.acls is not None and self.acls.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "list" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-es-acl-oper:es-acl/active/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "acls"):
                    if (self.acls is None):
                        self.acls = EsAcl.Active.List.Acls()
                        self.acls.parent = self
                        self._children_name_map["acls"] = "acls"
                    return self.acls

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "acls"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class OorAcls(Entity):
            """
            Resource occupation details for ACLs
            
            .. attribute:: oor_acl
            
            	Resource occupation details for a particular ACL
            	**type**\: list of    :py:class:`OorAcl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.EsAcl.Active.OorAcls.OorAcl>`
            
            

            """

            _prefix = 'es-acl-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(EsAcl.Active.OorAcls, self).__init__()

                self.yang_name = "oor-acls"
                self.yang_parent_name = "active"

                self.oor_acl = YList(self)

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
                            super(EsAcl.Active.OorAcls, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(EsAcl.Active.OorAcls, self).__setattr__(name, value)


            class OorAcl(Entity):
                """
                Resource occupation details for a particular
                ACL
                
                .. attribute:: name  <key>
                
                	Name of the Access List
                	**type**\:  str
                
                	**length:** 1..65
                
                .. attribute:: current_configured_ac_es
                
                	Current configured aces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: current_configured_ac_ls
                
                	Current configured acls
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: maximum_configurable_ac_es
                
                	max configurable aces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: maximum_configurable_ac_ls
                
                	max configurable acls
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'es-acl-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(EsAcl.Active.OorAcls.OorAcl, self).__init__()

                    self.yang_name = "oor-acl"
                    self.yang_parent_name = "oor-acls"

                    self.name = YLeaf(YType.str, "name")

                    self.current_configured_ac_es = YLeaf(YType.uint32, "current-configured-ac-es")

                    self.current_configured_ac_ls = YLeaf(YType.uint32, "current-configured-ac-ls")

                    self.maximum_configurable_ac_es = YLeaf(YType.uint32, "maximum-configurable-ac-es")

                    self.maximum_configurable_ac_ls = YLeaf(YType.uint32, "maximum-configurable-ac-ls")

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
                                    "current_configured_ac_es",
                                    "current_configured_ac_ls",
                                    "maximum_configurable_ac_es",
                                    "maximum_configurable_ac_ls") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(EsAcl.Active.OorAcls.OorAcl, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(EsAcl.Active.OorAcls.OorAcl, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.name.is_set or
                        self.current_configured_ac_es.is_set or
                        self.current_configured_ac_ls.is_set or
                        self.maximum_configurable_ac_es.is_set or
                        self.maximum_configurable_ac_ls.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set or
                        self.current_configured_ac_es.yfilter != YFilter.not_set or
                        self.current_configured_ac_ls.yfilter != YFilter.not_set or
                        self.maximum_configurable_ac_es.yfilter != YFilter.not_set or
                        self.maximum_configurable_ac_ls.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "oor-acl" + "[name='" + self.name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-es-acl-oper:es-acl/active/oor-acls/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.name.get_name_leafdata())
                    if (self.current_configured_ac_es.is_set or self.current_configured_ac_es.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.current_configured_ac_es.get_name_leafdata())
                    if (self.current_configured_ac_ls.is_set or self.current_configured_ac_ls.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.current_configured_ac_ls.get_name_leafdata())
                    if (self.maximum_configurable_ac_es.is_set or self.maximum_configurable_ac_es.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.maximum_configurable_ac_es.get_name_leafdata())
                    if (self.maximum_configurable_ac_ls.is_set or self.maximum_configurable_ac_ls.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.maximum_configurable_ac_ls.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "name" or name == "current-configured-ac-es" or name == "current-configured-ac-ls" or name == "maximum-configurable-ac-es" or name == "maximum-configurable-ac-ls"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix
                    if(value_path == "current-configured-ac-es"):
                        self.current_configured_ac_es = value
                        self.current_configured_ac_es.value_namespace = name_space
                        self.current_configured_ac_es.value_namespace_prefix = name_space_prefix
                    if(value_path == "current-configured-ac-ls"):
                        self.current_configured_ac_ls = value
                        self.current_configured_ac_ls.value_namespace = name_space
                        self.current_configured_ac_ls.value_namespace_prefix = name_space_prefix
                    if(value_path == "maximum-configurable-ac-es"):
                        self.maximum_configurable_ac_es = value
                        self.maximum_configurable_ac_es.value_namespace = name_space
                        self.maximum_configurable_ac_es.value_namespace_prefix = name_space_prefix
                    if(value_path == "maximum-configurable-ac-ls"):
                        self.maximum_configurable_ac_ls = value
                        self.maximum_configurable_ac_ls.value_namespace = name_space
                        self.maximum_configurable_ac_ls.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.oor_acl:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.oor_acl:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "oor-acls" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-es-acl-oper:es-acl/active/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "oor-acl"):
                    for c in self.oor_acl:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = EsAcl.Active.OorAcls.OorAcl()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.oor_acl.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "oor-acl"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Usages(Entity):
            """
            Table of Usage statistics of ACLs at different
            nodes
            
            .. attribute:: usage
            
            	Usage statistics of an ACL at a node
            	**type**\: list of    :py:class:`Usage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.EsAcl.Active.Usages.Usage>`
            
            

            """

            _prefix = 'es-acl-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(EsAcl.Active.Usages, self).__init__()

                self.yang_name = "usages"
                self.yang_parent_name = "active"

                self.usage = YList(self)

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
                            super(EsAcl.Active.Usages, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(EsAcl.Active.Usages, self).__setattr__(name, value)


            class Usage(Entity):
                """
                Usage statistics of an ACL at a node
                
                .. attribute:: application_id
                
                	Application ID
                	**type**\:   :py:class:`AclUsageAppIdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_common_acl_datatypes.AclUsageAppIdEnum>`
                
                .. attribute:: location
                
                	Node where ACL is applied
                	**type**\:  str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: name
                
                	Name of the ACL
                	**type**\:  str
                
                	**length:** 1..65
                
                .. attribute:: usage_details
                
                	Usage Statistics Details
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'es-acl-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(EsAcl.Active.Usages.Usage, self).__init__()

                    self.yang_name = "usage"
                    self.yang_parent_name = "usages"

                    self.application_id = YLeaf(YType.enumeration, "application-id")

                    self.location = YLeaf(YType.str, "location")

                    self.name = YLeaf(YType.str, "name")

                    self.usage_details = YLeaf(YType.str, "usage-details")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("application_id",
                                    "location",
                                    "name",
                                    "usage_details") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(EsAcl.Active.Usages.Usage, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(EsAcl.Active.Usages.Usage, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.application_id.is_set or
                        self.location.is_set or
                        self.name.is_set or
                        self.usage_details.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.application_id.yfilter != YFilter.not_set or
                        self.location.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set or
                        self.usage_details.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "usage" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-es-acl-oper:es-acl/active/usages/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.application_id.is_set or self.application_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.application_id.get_name_leafdata())
                    if (self.location.is_set or self.location.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.location.get_name_leafdata())
                    if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.name.get_name_leafdata())
                    if (self.usage_details.is_set or self.usage_details.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.usage_details.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "application-id" or name == "location" or name == "name" or name == "usage-details"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "application-id"):
                        self.application_id = value
                        self.application_id.value_namespace = name_space
                        self.application_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "location"):
                        self.location = value
                        self.location.value_namespace = name_space
                        self.location.value_namespace_prefix = name_space_prefix
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix
                    if(value_path == "usage-details"):
                        self.usage_details = value
                        self.usage_details.value_namespace = name_space
                        self.usage_details.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.usage:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.usage:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "usages" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-es-acl-oper:es-acl/active/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "usage"):
                    for c in self.usage:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = EsAcl.Active.Usages.Usage()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.usage.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "usage"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                (self.list is not None and self.list.has_data()) or
                (self.oor is not None and self.oor.has_data()) or
                (self.oor_acls is not None and self.oor_acls.has_data()) or
                (self.usages is not None and self.usages.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.list is not None and self.list.has_operation()) or
                (self.oor is not None and self.oor.has_operation()) or
                (self.oor_acls is not None and self.oor_acls.has_operation()) or
                (self.usages is not None and self.usages.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "active" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-es-acl-oper:es-acl/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "list"):
                if (self.list is None):
                    self.list = EsAcl.Active.List()
                    self.list.parent = self
                    self._children_name_map["list"] = "list"
                return self.list

            if (child_yang_name == "oor"):
                if (self.oor is None):
                    self.oor = EsAcl.Active.Oor()
                    self.oor.parent = self
                    self._children_name_map["oor"] = "oor"
                return self.oor

            if (child_yang_name == "oor-acls"):
                if (self.oor_acls is None):
                    self.oor_acls = EsAcl.Active.OorAcls()
                    self.oor_acls.parent = self
                    self._children_name_map["oor_acls"] = "oor-acls"
                return self.oor_acls

            if (child_yang_name == "usages"):
                if (self.usages is None):
                    self.usages = EsAcl.Active.Usages()
                    self.usages.parent = self
                    self._children_name_map["usages"] = "usages"
                return self.usages

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "list" or name == "oor" or name == "oor-acls" or name == "usages"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.active is not None and self.active.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.active is not None and self.active.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-es-acl-oper:es-acl" + path_buffer

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

        if (child_yang_name == "active"):
            if (self.active is None):
                self.active = EsAcl.Active()
                self.active.parent = self
                self._children_name_map["active"] = "active"
            return self.active

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "active"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = EsAcl()
        return self._top_entity


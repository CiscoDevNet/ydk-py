""" Cisco_IOS_XE_cfm_oper 

This module contains a collection of YANG definitions for
monitoring memory usage of processes in a Network Element.Copyright (c) 2016\-2017 by Cisco Systems, Inc.All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class CfmLastClearedType(Enum):
    """
    CfmLastClearedType

    .. data:: never_cleared = 0

    .. data:: cleared_before = 1

    """

    never_cleared = Enum.YLeaf(0, "never-cleared")

    cleared_before = Enum.YLeaf(1, "cleared-before")



class CfmStatistics(Entity):
    """
    Data nodes for CFM Statistics.
    
    .. attribute:: cfm_meps
    
    	
    	**type**\:   :py:class:`CfmMeps <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cfm_oper.CfmStatistics.CfmMeps>`
    
    

    """

    _prefix = 'cfm-stats-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(CfmStatistics, self).__init__()
        self._top_entity = None

        self.yang_name = "cfm-statistics"
        self.yang_parent_name = "Cisco-IOS-XE-cfm-oper"

        self.cfm_meps = CfmStatistics.CfmMeps()
        self.cfm_meps.parent = self
        self._children_name_map["cfm_meps"] = "cfm-meps"
        self._children_yang_names.add("cfm-meps")


    class CfmMeps(Entity):
        """
        
        
        .. attribute:: cfm_mep
        
        	The list of MEP entries in the system
        	**type**\: list of    :py:class:`CfmMep <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cfm_oper.CfmStatistics.CfmMeps.CfmMep>`
        
        

        """

        _prefix = 'cfm-stats-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            super(CfmStatistics.CfmMeps, self).__init__()

            self.yang_name = "cfm-meps"
            self.yang_parent_name = "cfm-statistics"

            self.cfm_mep = YList(self)

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
                        super(CfmStatistics.CfmMeps, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CfmStatistics.CfmMeps, self).__setattr__(name, value)


        class CfmMep(Entity):
            """
            The list of MEP entries in the system.
            
            .. attribute:: domain_name  <key>
            
            	The name of the Domain corresponding the the MEP
            	**type**\:  str
            
            .. attribute:: ma_name  <key>
            
            	The name of the MA corresponding the the MEP
            	**type**\:  str
            
            .. attribute:: mpid  <key>
            
            	ID of the MEP
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccm_seq_errors
            
            	The number of CCM sequence number errors detected
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ccm_transmitted
            
            	The number of CCMs transmitted from the local MEP
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: last_cleared
            
            	
            	**type**\:   :py:class:`LastCleared <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cfm_oper.CfmStatistics.CfmMeps.CfmMep.LastCleared>`
            
            .. attribute:: lbr_received_bad
            
            	The number of loopback reply packets received  with corrupted data pattern
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: lbr_received_ok
            
            	The number of valid loopback reply packets received
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: lbr_seq_errors
            
            	The number of loopback reply packets received  with sequence number errors
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: lbr_transmitted
            
            	The number of loopback reply packets transmitted from the local MEP
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ltr_unexpected
            
            	The number of unexpected linktrace reply packets  received at this MEP
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'cfm-stats-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(CfmStatistics.CfmMeps.CfmMep, self).__init__()

                self.yang_name = "cfm-mep"
                self.yang_parent_name = "cfm-meps"

                self.domain_name = YLeaf(YType.str, "domain-name")

                self.ma_name = YLeaf(YType.str, "ma-name")

                self.mpid = YLeaf(YType.uint32, "mpid")

                self.ccm_seq_errors = YLeaf(YType.uint64, "ccm-seq-errors")

                self.ccm_transmitted = YLeaf(YType.uint64, "ccm-transmitted")

                self.lbr_received_bad = YLeaf(YType.uint64, "lbr-received-bad")

                self.lbr_received_ok = YLeaf(YType.uint64, "lbr-received-ok")

                self.lbr_seq_errors = YLeaf(YType.uint64, "lbr-seq-errors")

                self.lbr_transmitted = YLeaf(YType.uint64, "lbr-transmitted")

                self.ltr_unexpected = YLeaf(YType.uint64, "ltr-unexpected")

                self.last_cleared = CfmStatistics.CfmMeps.CfmMep.LastCleared()
                self.last_cleared.parent = self
                self._children_name_map["last_cleared"] = "last-cleared"
                self._children_yang_names.add("last-cleared")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("domain_name",
                                "ma_name",
                                "mpid",
                                "ccm_seq_errors",
                                "ccm_transmitted",
                                "lbr_received_bad",
                                "lbr_received_ok",
                                "lbr_seq_errors",
                                "lbr_transmitted",
                                "ltr_unexpected") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CfmStatistics.CfmMeps.CfmMep, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CfmStatistics.CfmMeps.CfmMep, self).__setattr__(name, value)


            class LastCleared(Entity):
                """
                
                
                .. attribute:: never
                
                	
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: time
                
                	
                	**type**\:  str
                
                

                """

                _prefix = 'cfm-stats-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(CfmStatistics.CfmMeps.CfmMep.LastCleared, self).__init__()

                    self.yang_name = "last-cleared"
                    self.yang_parent_name = "cfm-mep"

                    self.never = YLeaf(YType.empty, "never")

                    self.time = YLeaf(YType.str, "time")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("never",
                                    "time") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(CfmStatistics.CfmMeps.CfmMep.LastCleared, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(CfmStatistics.CfmMeps.CfmMep.LastCleared, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.never.is_set or
                        self.time.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.never.yfilter != YFilter.not_set or
                        self.time.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "last-cleared" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.never.is_set or self.never.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.never.get_name_leafdata())
                    if (self.time.is_set or self.time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.time.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "never" or name == "time"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "never"):
                        self.never = value
                        self.never.value_namespace = name_space
                        self.never.value_namespace_prefix = name_space_prefix
                    if(value_path == "time"):
                        self.time = value
                        self.time.value_namespace = name_space
                        self.time.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.domain_name.is_set or
                    self.ma_name.is_set or
                    self.mpid.is_set or
                    self.ccm_seq_errors.is_set or
                    self.ccm_transmitted.is_set or
                    self.lbr_received_bad.is_set or
                    self.lbr_received_ok.is_set or
                    self.lbr_seq_errors.is_set or
                    self.lbr_transmitted.is_set or
                    self.ltr_unexpected.is_set or
                    (self.last_cleared is not None and self.last_cleared.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.domain_name.yfilter != YFilter.not_set or
                    self.ma_name.yfilter != YFilter.not_set or
                    self.mpid.yfilter != YFilter.not_set or
                    self.ccm_seq_errors.yfilter != YFilter.not_set or
                    self.ccm_transmitted.yfilter != YFilter.not_set or
                    self.lbr_received_bad.yfilter != YFilter.not_set or
                    self.lbr_received_ok.yfilter != YFilter.not_set or
                    self.lbr_seq_errors.yfilter != YFilter.not_set or
                    self.lbr_transmitted.yfilter != YFilter.not_set or
                    self.ltr_unexpected.yfilter != YFilter.not_set or
                    (self.last_cleared is not None and self.last_cleared.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cfm-mep" + "[domain-name='" + self.domain_name.get() + "']" + "[ma-name='" + self.ma_name.get() + "']" + "[mpid='" + self.mpid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XE-cfm-oper:cfm-statistics/cfm-meps/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.domain_name.is_set or self.domain_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.domain_name.get_name_leafdata())
                if (self.ma_name.is_set or self.ma_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ma_name.get_name_leafdata())
                if (self.mpid.is_set or self.mpid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mpid.get_name_leafdata())
                if (self.ccm_seq_errors.is_set or self.ccm_seq_errors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccm_seq_errors.get_name_leafdata())
                if (self.ccm_transmitted.is_set or self.ccm_transmitted.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccm_transmitted.get_name_leafdata())
                if (self.lbr_received_bad.is_set or self.lbr_received_bad.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lbr_received_bad.get_name_leafdata())
                if (self.lbr_received_ok.is_set or self.lbr_received_ok.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lbr_received_ok.get_name_leafdata())
                if (self.lbr_seq_errors.is_set or self.lbr_seq_errors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lbr_seq_errors.get_name_leafdata())
                if (self.lbr_transmitted.is_set or self.lbr_transmitted.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lbr_transmitted.get_name_leafdata())
                if (self.ltr_unexpected.is_set or self.ltr_unexpected.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ltr_unexpected.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "last-cleared"):
                    if (self.last_cleared is None):
                        self.last_cleared = CfmStatistics.CfmMeps.CfmMep.LastCleared()
                        self.last_cleared.parent = self
                        self._children_name_map["last_cleared"] = "last-cleared"
                    return self.last_cleared

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "last-cleared" or name == "domain-name" or name == "ma-name" or name == "mpid" or name == "ccm-seq-errors" or name == "ccm-transmitted" or name == "lbr-received-bad" or name == "lbr-received-ok" or name == "lbr-seq-errors" or name == "lbr-transmitted" or name == "ltr-unexpected"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "domain-name"):
                    self.domain_name = value
                    self.domain_name.value_namespace = name_space
                    self.domain_name.value_namespace_prefix = name_space_prefix
                if(value_path == "ma-name"):
                    self.ma_name = value
                    self.ma_name.value_namespace = name_space
                    self.ma_name.value_namespace_prefix = name_space_prefix
                if(value_path == "mpid"):
                    self.mpid = value
                    self.mpid.value_namespace = name_space
                    self.mpid.value_namespace_prefix = name_space_prefix
                if(value_path == "ccm-seq-errors"):
                    self.ccm_seq_errors = value
                    self.ccm_seq_errors.value_namespace = name_space
                    self.ccm_seq_errors.value_namespace_prefix = name_space_prefix
                if(value_path == "ccm-transmitted"):
                    self.ccm_transmitted = value
                    self.ccm_transmitted.value_namespace = name_space
                    self.ccm_transmitted.value_namespace_prefix = name_space_prefix
                if(value_path == "lbr-received-bad"):
                    self.lbr_received_bad = value
                    self.lbr_received_bad.value_namespace = name_space
                    self.lbr_received_bad.value_namespace_prefix = name_space_prefix
                if(value_path == "lbr-received-ok"):
                    self.lbr_received_ok = value
                    self.lbr_received_ok.value_namespace = name_space
                    self.lbr_received_ok.value_namespace_prefix = name_space_prefix
                if(value_path == "lbr-seq-errors"):
                    self.lbr_seq_errors = value
                    self.lbr_seq_errors.value_namespace = name_space
                    self.lbr_seq_errors.value_namespace_prefix = name_space_prefix
                if(value_path == "lbr-transmitted"):
                    self.lbr_transmitted = value
                    self.lbr_transmitted.value_namespace = name_space
                    self.lbr_transmitted.value_namespace_prefix = name_space_prefix
                if(value_path == "ltr-unexpected"):
                    self.ltr_unexpected = value
                    self.ltr_unexpected.value_namespace = name_space
                    self.ltr_unexpected.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cfm_mep:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cfm_mep:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cfm-meps" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XE-cfm-oper:cfm-statistics/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cfm-mep"):
                for c in self.cfm_mep:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CfmStatistics.CfmMeps.CfmMep()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cfm_mep.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cfm-mep"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.cfm_meps is not None and self.cfm_meps.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cfm_meps is not None and self.cfm_meps.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XE-cfm-oper:cfm-statistics" + path_buffer

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

        if (child_yang_name == "cfm-meps"):
            if (self.cfm_meps is None):
                self.cfm_meps = CfmStatistics.CfmMeps()
                self.cfm_meps.parent = self
                self._children_name_map["cfm_meps"] = "cfm-meps"
            return self.cfm_meps

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cfm-meps"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CfmStatistics()
        return self._top_entity


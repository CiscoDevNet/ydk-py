""" Cisco_IOS_XR_ncs1k_mxp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ncs1k\-mxp package operational data.

This module contains definitions
for the following management objects\:
  hw\-module\: mxp hw\-module command chain

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class HwModuleSliceStatus(Enum):
    """
    HwModuleSliceStatus

    Hw module slice status

    .. data:: not_provisioned = 0

    	Not Provisioned

    .. data:: provisioning_in_progress = 1

    	Provisioning In-Progress

    .. data:: provisioned = 2

    	Provisioned

    .. data:: provisioning_failed = 3

    	Provisioning Failed

    .. data:: provisioning_scheduled = 4

    	Provisioning Scheduled

    .. data:: reprovisioning_aborted = 5

    	Reprovisioning Aborted

    """

    not_provisioned = Enum.YLeaf(0, "not-provisioned")

    provisioning_in_progress = Enum.YLeaf(1, "provisioning-in-progress")

    provisioned = Enum.YLeaf(2, "provisioned")

    provisioning_failed = Enum.YLeaf(3, "provisioning-failed")

    provisioning_scheduled = Enum.YLeaf(4, "provisioning-scheduled")

    reprovisioning_aborted = Enum.YLeaf(5, "reprovisioning-aborted")



class HwModule(Entity):
    """
    mxp hw\-module command chain
    
    .. attribute:: slice_all
    
    	Information for all slices
    	**type**\:   :py:class:`SliceAll <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper.HwModule.SliceAll>`
    
    .. attribute:: slice_ids
    
    	Slice information
    	**type**\:   :py:class:`SliceIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper.HwModule.SliceIds>`
    
    

    """

    _prefix = 'ncs1k-mxp-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(HwModule, self).__init__()
        self._top_entity = None

        self.yang_name = "hw-module"
        self.yang_parent_name = "Cisco-IOS-XR-ncs1k-mxp-oper"

        self.slice_all = HwModule.SliceAll()
        self.slice_all.parent = self
        self._children_name_map["slice_all"] = "slice-all"
        self._children_yang_names.add("slice-all")

        self.slice_ids = HwModule.SliceIds()
        self.slice_ids.parent = self
        self._children_name_map["slice_ids"] = "slice-ids"
        self._children_yang_names.add("slice-ids")


    class SliceIds(Entity):
        """
        Slice information
        
        .. attribute:: slice_id
        
        	Per slice num data
        	**type**\: list of    :py:class:`SliceId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper.HwModule.SliceIds.SliceId>`
        
        

        """

        _prefix = 'ncs1k-mxp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(HwModule.SliceIds, self).__init__()

            self.yang_name = "slice-ids"
            self.yang_parent_name = "hw-module"

            self.slice_id = YList(self)

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
                        super(HwModule.SliceIds, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(HwModule.SliceIds, self).__setattr__(name, value)


        class SliceId(Entity):
            """
            Per slice num data
            
            .. attribute:: slice_num  <key>
            
            	Details associated with a particular slice number
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: slice_info
            
            	slice info
            	**type**\: list of    :py:class:`SliceInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper.HwModule.SliceIds.SliceId.SliceInfo>`
            
            

            """

            _prefix = 'ncs1k-mxp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(HwModule.SliceIds.SliceId, self).__init__()

                self.yang_name = "slice-id"
                self.yang_parent_name = "slice-ids"

                self.slice_num = YLeaf(YType.int32, "slice-num")

                self.slice_info = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("slice_num") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(HwModule.SliceIds.SliceId, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(HwModule.SliceIds.SliceId, self).__setattr__(name, value)


            class SliceInfo(Entity):
                """
                slice info
                
                .. attribute:: client_port
                
                	client port
                	**type**\: list of    :py:class:`ClientPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper.HwModule.SliceIds.SliceId.SliceInfo.ClientPort>`
                
                .. attribute:: client_rate
                
                	ClientRate
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: dp_fpga_fw_type
                
                	DpFpgaFwType
                	**type**\:  str
                
                	**length:** 0..10
                
                .. attribute:: dp_fpga_fw_ver
                
                	DpFpgaFwVer
                	**type**\:  str
                
                	**length:** 0..10
                
                .. attribute:: encryption_supported
                
                	EncryptionSupported
                	**type**\:  bool
                
                .. attribute:: hardware_status
                
                	HardwareStatus
                	**type**\:   :py:class:`HwModuleSliceStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper.HwModuleSliceStatus>`
                
                .. attribute:: lldp_drop_status
                
                	LldpDropStatus
                	**type**\:  bool
                
                .. attribute:: need_upg
                
                	NeedUpg
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: slice_id
                
                	SliceId
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: trunk_rate
                
                	TrunkRate
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ncs1k-mxp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(HwModule.SliceIds.SliceId.SliceInfo, self).__init__()

                    self.yang_name = "slice-info"
                    self.yang_parent_name = "slice-id"

                    self.client_rate = YLeaf(YType.uint32, "client-rate")

                    self.dp_fpga_fw_type = YLeaf(YType.str, "dp-fpga-fw-type")

                    self.dp_fpga_fw_ver = YLeaf(YType.str, "dp-fpga-fw-ver")

                    self.encryption_supported = YLeaf(YType.boolean, "encryption-supported")

                    self.hardware_status = YLeaf(YType.enumeration, "hardware-status")

                    self.lldp_drop_status = YLeaf(YType.boolean, "lldp-drop-status")

                    self.need_upg = YLeaf(YType.uint32, "need-upg")

                    self.slice_id = YLeaf(YType.uint32, "slice-id")

                    self.trunk_rate = YLeaf(YType.uint32, "trunk-rate")

                    self.client_port = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("client_rate",
                                    "dp_fpga_fw_type",
                                    "dp_fpga_fw_ver",
                                    "encryption_supported",
                                    "hardware_status",
                                    "lldp_drop_status",
                                    "need_upg",
                                    "slice_id",
                                    "trunk_rate") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(HwModule.SliceIds.SliceId.SliceInfo, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(HwModule.SliceIds.SliceId.SliceInfo, self).__setattr__(name, value)


                class ClientPort(Entity):
                    """
                    client port
                    
                    .. attribute:: client_name
                    
                    	ClientName
                    	**type**\:  str
                    
                    	**length:** 0..64
                    
                    .. attribute:: if_index
                    
                    	IfIndex
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: trunk_port
                    
                    	trunk port
                    	**type**\: list of    :py:class:`TrunkPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper.HwModule.SliceIds.SliceId.SliceInfo.ClientPort.TrunkPort>`
                    
                    

                    """

                    _prefix = 'ncs1k-mxp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(HwModule.SliceIds.SliceId.SliceInfo.ClientPort, self).__init__()

                        self.yang_name = "client-port"
                        self.yang_parent_name = "slice-info"

                        self.client_name = YLeaf(YType.str, "client-name")

                        self.if_index = YLeaf(YType.uint32, "if-index")

                        self.trunk_port = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("client_name",
                                        "if_index") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(HwModule.SliceIds.SliceId.SliceInfo.ClientPort, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(HwModule.SliceIds.SliceId.SliceInfo.ClientPort, self).__setattr__(name, value)


                    class TrunkPort(Entity):
                        """
                        trunk port
                        
                        .. attribute:: if_index
                        
                        	IfIndex
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percentage
                        
                        	Percentage
                        	**type**\:  str
                        
                        	**length:** 0..8
                        
                        .. attribute:: trunk_name
                        
                        	TrunkName
                        	**type**\:  str
                        
                        	**length:** 0..64
                        
                        

                        """

                        _prefix = 'ncs1k-mxp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(HwModule.SliceIds.SliceId.SliceInfo.ClientPort.TrunkPort, self).__init__()

                            self.yang_name = "trunk-port"
                            self.yang_parent_name = "client-port"

                            self.if_index = YLeaf(YType.uint32, "if-index")

                            self.percentage = YLeaf(YType.str, "percentage")

                            self.trunk_name = YLeaf(YType.str, "trunk-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("if_index",
                                            "percentage",
                                            "trunk_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(HwModule.SliceIds.SliceId.SliceInfo.ClientPort.TrunkPort, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(HwModule.SliceIds.SliceId.SliceInfo.ClientPort.TrunkPort, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.if_index.is_set or
                                self.percentage.is_set or
                                self.trunk_name.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.if_index.yfilter != YFilter.not_set or
                                self.percentage.yfilter != YFilter.not_set or
                                self.trunk_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "trunk-port" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.if_index.is_set or self.if_index.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.if_index.get_name_leafdata())
                            if (self.percentage.is_set or self.percentage.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.percentage.get_name_leafdata())
                            if (self.trunk_name.is_set or self.trunk_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.trunk_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "if-index" or name == "percentage" or name == "trunk-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "if-index"):
                                self.if_index = value
                                self.if_index.value_namespace = name_space
                                self.if_index.value_namespace_prefix = name_space_prefix
                            if(value_path == "percentage"):
                                self.percentage = value
                                self.percentage.value_namespace = name_space
                                self.percentage.value_namespace_prefix = name_space_prefix
                            if(value_path == "trunk-name"):
                                self.trunk_name = value
                                self.trunk_name.value_namespace = name_space
                                self.trunk_name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.trunk_port:
                            if (c.has_data()):
                                return True
                        return (
                            self.client_name.is_set or
                            self.if_index.is_set)

                    def has_operation(self):
                        for c in self.trunk_port:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.client_name.yfilter != YFilter.not_set or
                            self.if_index.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "client-port" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.client_name.is_set or self.client_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.client_name.get_name_leafdata())
                        if (self.if_index.is_set or self.if_index.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.if_index.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "trunk-port"):
                            for c in self.trunk_port:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = HwModule.SliceIds.SliceId.SliceInfo.ClientPort.TrunkPort()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.trunk_port.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "trunk-port" or name == "client-name" or name == "if-index"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "client-name"):
                            self.client_name = value
                            self.client_name.value_namespace = name_space
                            self.client_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "if-index"):
                            self.if_index = value
                            self.if_index.value_namespace = name_space
                            self.if_index.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.client_port:
                        if (c.has_data()):
                            return True
                    return (
                        self.client_rate.is_set or
                        self.dp_fpga_fw_type.is_set or
                        self.dp_fpga_fw_ver.is_set or
                        self.encryption_supported.is_set or
                        self.hardware_status.is_set or
                        self.lldp_drop_status.is_set or
                        self.need_upg.is_set or
                        self.slice_id.is_set or
                        self.trunk_rate.is_set)

                def has_operation(self):
                    for c in self.client_port:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.client_rate.yfilter != YFilter.not_set or
                        self.dp_fpga_fw_type.yfilter != YFilter.not_set or
                        self.dp_fpga_fw_ver.yfilter != YFilter.not_set or
                        self.encryption_supported.yfilter != YFilter.not_set or
                        self.hardware_status.yfilter != YFilter.not_set or
                        self.lldp_drop_status.yfilter != YFilter.not_set or
                        self.need_upg.yfilter != YFilter.not_set or
                        self.slice_id.yfilter != YFilter.not_set or
                        self.trunk_rate.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "slice-info" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.client_rate.is_set or self.client_rate.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.client_rate.get_name_leafdata())
                    if (self.dp_fpga_fw_type.is_set or self.dp_fpga_fw_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dp_fpga_fw_type.get_name_leafdata())
                    if (self.dp_fpga_fw_ver.is_set or self.dp_fpga_fw_ver.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dp_fpga_fw_ver.get_name_leafdata())
                    if (self.encryption_supported.is_set or self.encryption_supported.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.encryption_supported.get_name_leafdata())
                    if (self.hardware_status.is_set or self.hardware_status.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.hardware_status.get_name_leafdata())
                    if (self.lldp_drop_status.is_set or self.lldp_drop_status.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.lldp_drop_status.get_name_leafdata())
                    if (self.need_upg.is_set or self.need_upg.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.need_upg.get_name_leafdata())
                    if (self.slice_id.is_set or self.slice_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.slice_id.get_name_leafdata())
                    if (self.trunk_rate.is_set or self.trunk_rate.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.trunk_rate.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "client-port"):
                        for c in self.client_port:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = HwModule.SliceIds.SliceId.SliceInfo.ClientPort()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.client_port.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "client-port" or name == "client-rate" or name == "dp-fpga-fw-type" or name == "dp-fpga-fw-ver" or name == "encryption-supported" or name == "hardware-status" or name == "lldp-drop-status" or name == "need-upg" or name == "slice-id" or name == "trunk-rate"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "client-rate"):
                        self.client_rate = value
                        self.client_rate.value_namespace = name_space
                        self.client_rate.value_namespace_prefix = name_space_prefix
                    if(value_path == "dp-fpga-fw-type"):
                        self.dp_fpga_fw_type = value
                        self.dp_fpga_fw_type.value_namespace = name_space
                        self.dp_fpga_fw_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "dp-fpga-fw-ver"):
                        self.dp_fpga_fw_ver = value
                        self.dp_fpga_fw_ver.value_namespace = name_space
                        self.dp_fpga_fw_ver.value_namespace_prefix = name_space_prefix
                    if(value_path == "encryption-supported"):
                        self.encryption_supported = value
                        self.encryption_supported.value_namespace = name_space
                        self.encryption_supported.value_namespace_prefix = name_space_prefix
                    if(value_path == "hardware-status"):
                        self.hardware_status = value
                        self.hardware_status.value_namespace = name_space
                        self.hardware_status.value_namespace_prefix = name_space_prefix
                    if(value_path == "lldp-drop-status"):
                        self.lldp_drop_status = value
                        self.lldp_drop_status.value_namespace = name_space
                        self.lldp_drop_status.value_namespace_prefix = name_space_prefix
                    if(value_path == "need-upg"):
                        self.need_upg = value
                        self.need_upg.value_namespace = name_space
                        self.need_upg.value_namespace_prefix = name_space_prefix
                    if(value_path == "slice-id"):
                        self.slice_id = value
                        self.slice_id.value_namespace = name_space
                        self.slice_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "trunk-rate"):
                        self.trunk_rate = value
                        self.trunk_rate.value_namespace = name_space
                        self.trunk_rate.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.slice_info:
                    if (c.has_data()):
                        return True
                return self.slice_num.is_set

            def has_operation(self):
                for c in self.slice_info:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.slice_num.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "slice-id" + "[slice-num='" + self.slice_num.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ncs1k-mxp-oper:hw-module/slice-ids/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.slice_num.is_set or self.slice_num.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.slice_num.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "slice-info"):
                    for c in self.slice_info:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = HwModule.SliceIds.SliceId.SliceInfo()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.slice_info.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "slice-info" or name == "slice-num"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "slice-num"):
                    self.slice_num = value
                    self.slice_num.value_namespace = name_space
                    self.slice_num.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.slice_id:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.slice_id:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "slice-ids" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ncs1k-mxp-oper:hw-module/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "slice-id"):
                for c in self.slice_id:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = HwModule.SliceIds.SliceId()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.slice_id.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "slice-id"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class SliceAll(Entity):
        """
        Information for all slices
        
        .. attribute:: slice_info
        
        	slice info
        	**type**\: list of    :py:class:`SliceInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper.HwModule.SliceAll.SliceInfo>`
        
        

        """

        _prefix = 'ncs1k-mxp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(HwModule.SliceAll, self).__init__()

            self.yang_name = "slice-all"
            self.yang_parent_name = "hw-module"

            self.slice_info = YList(self)

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
                        super(HwModule.SliceAll, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(HwModule.SliceAll, self).__setattr__(name, value)


        class SliceInfo(Entity):
            """
            slice info
            
            .. attribute:: client_port
            
            	client port
            	**type**\: list of    :py:class:`ClientPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper.HwModule.SliceAll.SliceInfo.ClientPort>`
            
            .. attribute:: client_rate
            
            	ClientRate
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dp_fpga_fw_type
            
            	DpFpgaFwType
            	**type**\:  str
            
            	**length:** 0..10
            
            .. attribute:: dp_fpga_fw_ver
            
            	DpFpgaFwVer
            	**type**\:  str
            
            	**length:** 0..10
            
            .. attribute:: encryption_supported
            
            	EncryptionSupported
            	**type**\:  bool
            
            .. attribute:: hardware_status
            
            	HardwareStatus
            	**type**\:   :py:class:`HwModuleSliceStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper.HwModuleSliceStatus>`
            
            .. attribute:: lldp_drop_status
            
            	LldpDropStatus
            	**type**\:  bool
            
            .. attribute:: need_upg
            
            	NeedUpg
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: slice_id
            
            	SliceId
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: trunk_rate
            
            	TrunkRate
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'ncs1k-mxp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(HwModule.SliceAll.SliceInfo, self).__init__()

                self.yang_name = "slice-info"
                self.yang_parent_name = "slice-all"

                self.client_rate = YLeaf(YType.uint32, "client-rate")

                self.dp_fpga_fw_type = YLeaf(YType.str, "dp-fpga-fw-type")

                self.dp_fpga_fw_ver = YLeaf(YType.str, "dp-fpga-fw-ver")

                self.encryption_supported = YLeaf(YType.boolean, "encryption-supported")

                self.hardware_status = YLeaf(YType.enumeration, "hardware-status")

                self.lldp_drop_status = YLeaf(YType.boolean, "lldp-drop-status")

                self.need_upg = YLeaf(YType.uint32, "need-upg")

                self.slice_id = YLeaf(YType.uint32, "slice-id")

                self.trunk_rate = YLeaf(YType.uint32, "trunk-rate")

                self.client_port = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("client_rate",
                                "dp_fpga_fw_type",
                                "dp_fpga_fw_ver",
                                "encryption_supported",
                                "hardware_status",
                                "lldp_drop_status",
                                "need_upg",
                                "slice_id",
                                "trunk_rate") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(HwModule.SliceAll.SliceInfo, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(HwModule.SliceAll.SliceInfo, self).__setattr__(name, value)


            class ClientPort(Entity):
                """
                client port
                
                .. attribute:: client_name
                
                	ClientName
                	**type**\:  str
                
                	**length:** 0..64
                
                .. attribute:: if_index
                
                	IfIndex
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: trunk_port
                
                	trunk port
                	**type**\: list of    :py:class:`TrunkPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper.HwModule.SliceAll.SliceInfo.ClientPort.TrunkPort>`
                
                

                """

                _prefix = 'ncs1k-mxp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(HwModule.SliceAll.SliceInfo.ClientPort, self).__init__()

                    self.yang_name = "client-port"
                    self.yang_parent_name = "slice-info"

                    self.client_name = YLeaf(YType.str, "client-name")

                    self.if_index = YLeaf(YType.uint32, "if-index")

                    self.trunk_port = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("client_name",
                                    "if_index") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(HwModule.SliceAll.SliceInfo.ClientPort, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(HwModule.SliceAll.SliceInfo.ClientPort, self).__setattr__(name, value)


                class TrunkPort(Entity):
                    """
                    trunk port
                    
                    .. attribute:: if_index
                    
                    	IfIndex
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: percentage
                    
                    	Percentage
                    	**type**\:  str
                    
                    	**length:** 0..8
                    
                    .. attribute:: trunk_name
                    
                    	TrunkName
                    	**type**\:  str
                    
                    	**length:** 0..64
                    
                    

                    """

                    _prefix = 'ncs1k-mxp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(HwModule.SliceAll.SliceInfo.ClientPort.TrunkPort, self).__init__()

                        self.yang_name = "trunk-port"
                        self.yang_parent_name = "client-port"

                        self.if_index = YLeaf(YType.uint32, "if-index")

                        self.percentage = YLeaf(YType.str, "percentage")

                        self.trunk_name = YLeaf(YType.str, "trunk-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("if_index",
                                        "percentage",
                                        "trunk_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(HwModule.SliceAll.SliceInfo.ClientPort.TrunkPort, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(HwModule.SliceAll.SliceInfo.ClientPort.TrunkPort, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.if_index.is_set or
                            self.percentage.is_set or
                            self.trunk_name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.if_index.yfilter != YFilter.not_set or
                            self.percentage.yfilter != YFilter.not_set or
                            self.trunk_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "trunk-port" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ncs1k-mxp-oper:hw-module/slice-all/slice-info/client-port/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.if_index.is_set or self.if_index.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.if_index.get_name_leafdata())
                        if (self.percentage.is_set or self.percentage.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.percentage.get_name_leafdata())
                        if (self.trunk_name.is_set or self.trunk_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.trunk_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "if-index" or name == "percentage" or name == "trunk-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "if-index"):
                            self.if_index = value
                            self.if_index.value_namespace = name_space
                            self.if_index.value_namespace_prefix = name_space_prefix
                        if(value_path == "percentage"):
                            self.percentage = value
                            self.percentage.value_namespace = name_space
                            self.percentage.value_namespace_prefix = name_space_prefix
                        if(value_path == "trunk-name"):
                            self.trunk_name = value
                            self.trunk_name.value_namespace = name_space
                            self.trunk_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.trunk_port:
                        if (c.has_data()):
                            return True
                    return (
                        self.client_name.is_set or
                        self.if_index.is_set)

                def has_operation(self):
                    for c in self.trunk_port:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.client_name.yfilter != YFilter.not_set or
                        self.if_index.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "client-port" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ncs1k-mxp-oper:hw-module/slice-all/slice-info/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.client_name.is_set or self.client_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.client_name.get_name_leafdata())
                    if (self.if_index.is_set or self.if_index.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.if_index.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "trunk-port"):
                        for c in self.trunk_port:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = HwModule.SliceAll.SliceInfo.ClientPort.TrunkPort()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.trunk_port.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "trunk-port" or name == "client-name" or name == "if-index"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "client-name"):
                        self.client_name = value
                        self.client_name.value_namespace = name_space
                        self.client_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "if-index"):
                        self.if_index = value
                        self.if_index.value_namespace = name_space
                        self.if_index.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.client_port:
                    if (c.has_data()):
                        return True
                return (
                    self.client_rate.is_set or
                    self.dp_fpga_fw_type.is_set or
                    self.dp_fpga_fw_ver.is_set or
                    self.encryption_supported.is_set or
                    self.hardware_status.is_set or
                    self.lldp_drop_status.is_set or
                    self.need_upg.is_set or
                    self.slice_id.is_set or
                    self.trunk_rate.is_set)

            def has_operation(self):
                for c in self.client_port:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.client_rate.yfilter != YFilter.not_set or
                    self.dp_fpga_fw_type.yfilter != YFilter.not_set or
                    self.dp_fpga_fw_ver.yfilter != YFilter.not_set or
                    self.encryption_supported.yfilter != YFilter.not_set or
                    self.hardware_status.yfilter != YFilter.not_set or
                    self.lldp_drop_status.yfilter != YFilter.not_set or
                    self.need_upg.yfilter != YFilter.not_set or
                    self.slice_id.yfilter != YFilter.not_set or
                    self.trunk_rate.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "slice-info" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ncs1k-mxp-oper:hw-module/slice-all/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.client_rate.is_set or self.client_rate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.client_rate.get_name_leafdata())
                if (self.dp_fpga_fw_type.is_set or self.dp_fpga_fw_type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dp_fpga_fw_type.get_name_leafdata())
                if (self.dp_fpga_fw_ver.is_set or self.dp_fpga_fw_ver.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dp_fpga_fw_ver.get_name_leafdata())
                if (self.encryption_supported.is_set or self.encryption_supported.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.encryption_supported.get_name_leafdata())
                if (self.hardware_status.is_set or self.hardware_status.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hardware_status.get_name_leafdata())
                if (self.lldp_drop_status.is_set or self.lldp_drop_status.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldp_drop_status.get_name_leafdata())
                if (self.need_upg.is_set or self.need_upg.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.need_upg.get_name_leafdata())
                if (self.slice_id.is_set or self.slice_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.slice_id.get_name_leafdata())
                if (self.trunk_rate.is_set or self.trunk_rate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.trunk_rate.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "client-port"):
                    for c in self.client_port:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = HwModule.SliceAll.SliceInfo.ClientPort()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.client_port.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "client-port" or name == "client-rate" or name == "dp-fpga-fw-type" or name == "dp-fpga-fw-ver" or name == "encryption-supported" or name == "hardware-status" or name == "lldp-drop-status" or name == "need-upg" or name == "slice-id" or name == "trunk-rate"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "client-rate"):
                    self.client_rate = value
                    self.client_rate.value_namespace = name_space
                    self.client_rate.value_namespace_prefix = name_space_prefix
                if(value_path == "dp-fpga-fw-type"):
                    self.dp_fpga_fw_type = value
                    self.dp_fpga_fw_type.value_namespace = name_space
                    self.dp_fpga_fw_type.value_namespace_prefix = name_space_prefix
                if(value_path == "dp-fpga-fw-ver"):
                    self.dp_fpga_fw_ver = value
                    self.dp_fpga_fw_ver.value_namespace = name_space
                    self.dp_fpga_fw_ver.value_namespace_prefix = name_space_prefix
                if(value_path == "encryption-supported"):
                    self.encryption_supported = value
                    self.encryption_supported.value_namespace = name_space
                    self.encryption_supported.value_namespace_prefix = name_space_prefix
                if(value_path == "hardware-status"):
                    self.hardware_status = value
                    self.hardware_status.value_namespace = name_space
                    self.hardware_status.value_namespace_prefix = name_space_prefix
                if(value_path == "lldp-drop-status"):
                    self.lldp_drop_status = value
                    self.lldp_drop_status.value_namespace = name_space
                    self.lldp_drop_status.value_namespace_prefix = name_space_prefix
                if(value_path == "need-upg"):
                    self.need_upg = value
                    self.need_upg.value_namespace = name_space
                    self.need_upg.value_namespace_prefix = name_space_prefix
                if(value_path == "slice-id"):
                    self.slice_id = value
                    self.slice_id.value_namespace = name_space
                    self.slice_id.value_namespace_prefix = name_space_prefix
                if(value_path == "trunk-rate"):
                    self.trunk_rate = value
                    self.trunk_rate.value_namespace = name_space
                    self.trunk_rate.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.slice_info:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.slice_info:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "slice-all" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ncs1k-mxp-oper:hw-module/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "slice-info"):
                for c in self.slice_info:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = HwModule.SliceAll.SliceInfo()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.slice_info.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "slice-info"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.slice_all is not None and self.slice_all.has_data()) or
            (self.slice_ids is not None and self.slice_ids.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.slice_all is not None and self.slice_all.has_operation()) or
            (self.slice_ids is not None and self.slice_ids.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ncs1k-mxp-oper:hw-module" + path_buffer

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

        if (child_yang_name == "slice-all"):
            if (self.slice_all is None):
                self.slice_all = HwModule.SliceAll()
                self.slice_all.parent = self
                self._children_name_map["slice_all"] = "slice-all"
            return self.slice_all

        if (child_yang_name == "slice-ids"):
            if (self.slice_ids is None):
                self.slice_ids = HwModule.SliceIds()
                self.slice_ids.parent = self
                self._children_name_map["slice_ids"] = "slice-ids"
            return self.slice_ids

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "slice-all" or name == "slice-ids"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = HwModule()
        return self._top_entity


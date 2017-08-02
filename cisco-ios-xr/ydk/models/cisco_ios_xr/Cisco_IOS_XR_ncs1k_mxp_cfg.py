""" Cisco_IOS_XR_ncs1k_mxp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ncs1k\-mxp package configuration.

This module contains definitions
for the following management objects\:
  hardware\-module\: NCS1k HW module config

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class ClientDataRate(Enum):
    """
    ClientDataRate

    Client data rate

    .. data:: ten_gig = 1

    	TenGig

    .. data:: forty_gig = 2

    	FortyGig

    .. data:: hundred_gig = 3

    	HundredGig

    """

    ten_gig = Enum.YLeaf(1, "ten-gig")

    forty_gig = Enum.YLeaf(2, "forty-gig")

    hundred_gig = Enum.YLeaf(3, "hundred-gig")


class Fec(Enum):
    """
    Fec

    Fec

    .. data:: sd7 = 1

    	SoftDecision7

    .. data:: sd20 = 2

    	SoftDecision20

    """

    sd7 = Enum.YLeaf(1, "sd7")

    sd20 = Enum.YLeaf(2, "sd20")


class TrunkDataRate(Enum):
    """
    TrunkDataRate

    Trunk data rate

    .. data:: hundred_gig = 2

    	HundredGig

    .. data:: two_hundred_gig = 3

    	TwoHundredGig

    .. data:: two_hundred_fifty_gig = 4

    	TwoHundredFiftyGig

    """

    hundred_gig = Enum.YLeaf(2, "hundred-gig")

    two_hundred_gig = Enum.YLeaf(3, "two-hundred-gig")

    two_hundred_fifty_gig = Enum.YLeaf(4, "two-hundred-fifty-gig")



class HardwareModule(Entity):
    """
    NCS1k HW module config
    
    .. attribute:: node
    
    	Node
    	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_cfg.HardwareModule.Node>`
    
    

    """

    _prefix = 'ncs1k-mxp-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(HardwareModule, self).__init__()
        self._top_entity = None

        self.yang_name = "hardware-module"
        self.yang_parent_name = "Cisco-IOS-XR-ncs1k-mxp-cfg"

        self.node = YList(self)

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
                    super(HardwareModule, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(HardwareModule, self).__setattr__(name, value)


    class Node(Entity):
        """
        Node
        
        .. attribute:: location  <key>
        
        	Fully qualified line card specification
        	**type**\:  str
        
        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
        
        .. attribute:: slice
        
        	Slice to be Provisioned
        	**type**\: list of    :py:class:`Slice <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_cfg.HardwareModule.Node.Slice>`
        
        

        """

        _prefix = 'ncs1k-mxp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(HardwareModule.Node, self).__init__()

            self.yang_name = "node"
            self.yang_parent_name = "hardware-module"

            self.location = YLeaf(YType.str, "location")

            self.slice = YList(self)

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
                        super(HardwareModule.Node, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(HardwareModule.Node, self).__setattr__(name, value)


        class Slice(Entity):
            """
            Slice to be Provisioned
            
            .. attribute:: slice_id  <key>
            
            	Set Slice
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: lldp
            
            	Drop LLDP Packets
            	**type**\:  bool
            
            .. attribute:: values
            
            	Data rates & FEC
            	**type**\:   :py:class:`Values <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_cfg.HardwareModule.Node.Slice.Values>`
            
            

            """

            _prefix = 'ncs1k-mxp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(HardwareModule.Node.Slice, self).__init__()

                self.yang_name = "slice"
                self.yang_parent_name = "node"

                self.slice_id = YLeaf(YType.str, "slice-id")

                self.lldp = YLeaf(YType.boolean, "lldp")

                self.values = HardwareModule.Node.Slice.Values()
                self.values.parent = self
                self._children_name_map["values"] = "values"
                self._children_yang_names.add("values")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("slice_id",
                                "lldp") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(HardwareModule.Node.Slice, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(HardwareModule.Node.Slice, self).__setattr__(name, value)


            class Values(Entity):
                """
                Data rates & FEC
                
                .. attribute:: client_rate
                
                	Client Rate
                	**type**\:   :py:class:`ClientDataRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_cfg.ClientDataRate>`
                
                .. attribute:: encrypted
                
                	Encrypted
                	**type**\:  bool
                
                	**default value**\: false
                
                .. attribute:: fec
                
                	FEC
                	**type**\:   :py:class:`Fec <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_cfg.Fec>`
                
                .. attribute:: trunk_rate
                
                	TrunkRate
                	**type**\:   :py:class:`TrunkDataRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_cfg.TrunkDataRate>`
                
                

                """

                _prefix = 'ncs1k-mxp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(HardwareModule.Node.Slice.Values, self).__init__()

                    self.yang_name = "values"
                    self.yang_parent_name = "slice"

                    self.client_rate = YLeaf(YType.enumeration, "client-rate")

                    self.encrypted = YLeaf(YType.boolean, "encrypted")

                    self.fec = YLeaf(YType.enumeration, "fec")

                    self.trunk_rate = YLeaf(YType.enumeration, "trunk-rate")

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
                                    "encrypted",
                                    "fec",
                                    "trunk_rate") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(HardwareModule.Node.Slice.Values, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(HardwareModule.Node.Slice.Values, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.client_rate.is_set or
                        self.encrypted.is_set or
                        self.fec.is_set or
                        self.trunk_rate.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.client_rate.yfilter != YFilter.not_set or
                        self.encrypted.yfilter != YFilter.not_set or
                        self.fec.yfilter != YFilter.not_set or
                        self.trunk_rate.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "values" + path_buffer

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
                    if (self.encrypted.is_set or self.encrypted.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.encrypted.get_name_leafdata())
                    if (self.fec.is_set or self.fec.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.fec.get_name_leafdata())
                    if (self.trunk_rate.is_set or self.trunk_rate.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.trunk_rate.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "client-rate" or name == "encrypted" or name == "fec" or name == "trunk-rate"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "client-rate"):
                        self.client_rate = value
                        self.client_rate.value_namespace = name_space
                        self.client_rate.value_namespace_prefix = name_space_prefix
                    if(value_path == "encrypted"):
                        self.encrypted = value
                        self.encrypted.value_namespace = name_space
                        self.encrypted.value_namespace_prefix = name_space_prefix
                    if(value_path == "fec"):
                        self.fec = value
                        self.fec.value_namespace = name_space
                        self.fec.value_namespace_prefix = name_space_prefix
                    if(value_path == "trunk-rate"):
                        self.trunk_rate = value
                        self.trunk_rate.value_namespace = name_space
                        self.trunk_rate.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.slice_id.is_set or
                    self.lldp.is_set or
                    (self.values is not None and self.values.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.slice_id.yfilter != YFilter.not_set or
                    self.lldp.yfilter != YFilter.not_set or
                    (self.values is not None and self.values.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "slice" + "[slice-id='" + self.slice_id.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.slice_id.is_set or self.slice_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.slice_id.get_name_leafdata())
                if (self.lldp.is_set or self.lldp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lldp.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "values"):
                    if (self.values is None):
                        self.values = HardwareModule.Node.Slice.Values()
                        self.values.parent = self
                        self._children_name_map["values"] = "values"
                    return self.values

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "values" or name == "slice-id" or name == "lldp"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "slice-id"):
                    self.slice_id = value
                    self.slice_id.value_namespace = name_space
                    self.slice_id.value_namespace_prefix = name_space_prefix
                if(value_path == "lldp"):
                    self.lldp = value
                    self.lldp.value_namespace = name_space
                    self.lldp.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.slice:
                if (c.has_data()):
                    return True
            return self.location.is_set

        def has_operation(self):
            for c in self.slice:
                if (c.has_operation()):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.location.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "node" + "[location='" + self.location.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ncs1k-mxp-cfg:hardware-module/%s" % self.get_segment_path()
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

            if (child_yang_name == "slice"):
                for c in self.slice:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = HardwareModule.Node.Slice()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.slice.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "slice" or name == "location"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "location"):
                self.location = value
                self.location.value_namespace = name_space
                self.location.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.node:
            if (c.has_data()):
                return True
        return False

    def has_operation(self):
        for c in self.node:
            if (c.has_operation()):
                return True
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ncs1k-mxp-cfg:hardware-module" + path_buffer

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

        if (child_yang_name == "node"):
            for c in self.node:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = HardwareModule.Node()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.node.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "node"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = HardwareModule()
        return self._top_entity


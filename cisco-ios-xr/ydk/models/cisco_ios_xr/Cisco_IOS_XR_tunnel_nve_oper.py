""" Cisco_IOS_XR_tunnel_nve_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR tunnel\-nve package operational data.

This module contains definitions
for the following management objects\:
  nve\: NVE operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Nve(Entity):
    """
    NVE operational data
    
    .. attribute:: interfaces
    
    	Table for NVE interface attributes
    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_nve_oper.Nve.Interfaces>`
    
    .. attribute:: vnis
    
    	Table for VNIs
    	**type**\:   :py:class:`Vnis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_nve_oper.Nve.Vnis>`
    
    

    """

    _prefix = 'tunnel-nve-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Nve, self).__init__()
        self._top_entity = None

        self.yang_name = "nve"
        self.yang_parent_name = "Cisco-IOS-XR-tunnel-nve-oper"

        self.interfaces = Nve.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._children_yang_names.add("interfaces")

        self.vnis = Nve.Vnis()
        self.vnis.parent = self
        self._children_name_map["vnis"] = "vnis"
        self._children_yang_names.add("vnis")


    class Vnis(Entity):
        """
        Table for VNIs
        
        .. attribute:: vni
        
        	The attributes for a particular VNI
        	**type**\: list of    :py:class:`Vni <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_nve_oper.Nve.Vnis.Vni>`
        
        

        """

        _prefix = 'tunnel-nve-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Nve.Vnis, self).__init__()

            self.yang_name = "vnis"
            self.yang_parent_name = "nve"

            self.vni = YList(self)

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
                        super(Nve.Vnis, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Nve.Vnis, self).__setattr__(name, value)


        class Vni(Entity):
            """
            The attributes for a particular VNI
            
            .. attribute:: vni  <key>
            
            	VNI ID
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: bvi_ifh
            
            	BVI Interface Handle
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: bvi_mac
            
            	BVI MAC address
            	**type**\:  str
            
            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
            
            .. attribute:: bvi_state
            
            	BVI Interface Oper State
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: flags
            
            	Flags
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: interface_name
            
            	NVE Interface name
            	**type**\:  str
            
            .. attribute:: ipv4_tbl_id
            
            	IPv4 Table ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipv6_tbl_id
            
            	IPv6 Table ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mcast_flags
            
            	McastFlags
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mcast_ipv4_address
            
            	MCAST IPv4 Address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: state
            
            	State
            	**type**\:  int
            
            	**range:** \-128..127
            
            .. attribute:: topo_id
            
            	L2RIB Topology ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: topo_name
            
            	L2RIB Topology Name
            	**type**\:  str
            
            	**length:** 0..50
            
            .. attribute:: topo_valid
            
            	TOPO ID valid flag
            	**type**\:  bool
            
            .. attribute:: udp_port
            
            	UDP Port
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vni_max
            
            	VNI Max in Range
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vni_min
            
            	VNI Min in Range
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vni_xr
            
            	VNI Number
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vrf_id
            
            	L3 VRF ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vrf_name
            
            	L3 VRF Name
            	**type**\:  str
            
            .. attribute:: vrf_vni
            
            	VRF VNI
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'tunnel-nve-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Nve.Vnis.Vni, self).__init__()

                self.yang_name = "vni"
                self.yang_parent_name = "vnis"

                self.vni = YLeaf(YType.str, "vni")

                self.bvi_ifh = YLeaf(YType.uint32, "bvi-ifh")

                self.bvi_mac = YLeaf(YType.str, "bvi-mac")

                self.bvi_state = YLeaf(YType.uint8, "bvi-state")

                self.flags = YLeaf(YType.uint32, "flags")

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.ipv4_tbl_id = YLeaf(YType.uint32, "ipv4-tbl-id")

                self.ipv6_tbl_id = YLeaf(YType.uint32, "ipv6-tbl-id")

                self.mcast_flags = YLeaf(YType.uint32, "mcast-flags")

                self.mcast_ipv4_address = YLeaf(YType.str, "mcast-ipv4-address")

                self.state = YLeaf(YType.int8, "state")

                self.topo_id = YLeaf(YType.uint32, "topo-id")

                self.topo_name = YLeaf(YType.str, "topo-name")

                self.topo_valid = YLeaf(YType.boolean, "topo-valid")

                self.udp_port = YLeaf(YType.uint32, "udp-port")

                self.vni_max = YLeaf(YType.uint32, "vni-max")

                self.vni_min = YLeaf(YType.uint32, "vni-min")

                self.vni_xr = YLeaf(YType.uint32, "vni-xr")

                self.vrf_id = YLeaf(YType.uint32, "vrf-id")

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.vrf_vni = YLeaf(YType.uint32, "vrf-vni")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("vni",
                                "bvi_ifh",
                                "bvi_mac",
                                "bvi_state",
                                "flags",
                                "interface_name",
                                "ipv4_tbl_id",
                                "ipv6_tbl_id",
                                "mcast_flags",
                                "mcast_ipv4_address",
                                "state",
                                "topo_id",
                                "topo_name",
                                "topo_valid",
                                "udp_port",
                                "vni_max",
                                "vni_min",
                                "vni_xr",
                                "vrf_id",
                                "vrf_name",
                                "vrf_vni") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Nve.Vnis.Vni, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Nve.Vnis.Vni, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.vni.is_set or
                    self.bvi_ifh.is_set or
                    self.bvi_mac.is_set or
                    self.bvi_state.is_set or
                    self.flags.is_set or
                    self.interface_name.is_set or
                    self.ipv4_tbl_id.is_set or
                    self.ipv6_tbl_id.is_set or
                    self.mcast_flags.is_set or
                    self.mcast_ipv4_address.is_set or
                    self.state.is_set or
                    self.topo_id.is_set or
                    self.topo_name.is_set or
                    self.topo_valid.is_set or
                    self.udp_port.is_set or
                    self.vni_max.is_set or
                    self.vni_min.is_set or
                    self.vni_xr.is_set or
                    self.vrf_id.is_set or
                    self.vrf_name.is_set or
                    self.vrf_vni.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.vni.yfilter != YFilter.not_set or
                    self.bvi_ifh.yfilter != YFilter.not_set or
                    self.bvi_mac.yfilter != YFilter.not_set or
                    self.bvi_state.yfilter != YFilter.not_set or
                    self.flags.yfilter != YFilter.not_set or
                    self.interface_name.yfilter != YFilter.not_set or
                    self.ipv4_tbl_id.yfilter != YFilter.not_set or
                    self.ipv6_tbl_id.yfilter != YFilter.not_set or
                    self.mcast_flags.yfilter != YFilter.not_set or
                    self.mcast_ipv4_address.yfilter != YFilter.not_set or
                    self.state.yfilter != YFilter.not_set or
                    self.topo_id.yfilter != YFilter.not_set or
                    self.topo_name.yfilter != YFilter.not_set or
                    self.topo_valid.yfilter != YFilter.not_set or
                    self.udp_port.yfilter != YFilter.not_set or
                    self.vni_max.yfilter != YFilter.not_set or
                    self.vni_min.yfilter != YFilter.not_set or
                    self.vni_xr.yfilter != YFilter.not_set or
                    self.vrf_id.yfilter != YFilter.not_set or
                    self.vrf_name.yfilter != YFilter.not_set or
                    self.vrf_vni.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vni" + "[vni='" + self.vni.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-tunnel-nve-oper:nve/vnis/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.vni.is_set or self.vni.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vni.get_name_leafdata())
                if (self.bvi_ifh.is_set or self.bvi_ifh.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bvi_ifh.get_name_leafdata())
                if (self.bvi_mac.is_set or self.bvi_mac.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bvi_mac.get_name_leafdata())
                if (self.bvi_state.is_set or self.bvi_state.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bvi_state.get_name_leafdata())
                if (self.flags.is_set or self.flags.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.flags.get_name_leafdata())
                if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface_name.get_name_leafdata())
                if (self.ipv4_tbl_id.is_set or self.ipv4_tbl_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipv4_tbl_id.get_name_leafdata())
                if (self.ipv6_tbl_id.is_set or self.ipv6_tbl_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipv6_tbl_id.get_name_leafdata())
                if (self.mcast_flags.is_set or self.mcast_flags.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mcast_flags.get_name_leafdata())
                if (self.mcast_ipv4_address.is_set or self.mcast_ipv4_address.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mcast_ipv4_address.get_name_leafdata())
                if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.state.get_name_leafdata())
                if (self.topo_id.is_set or self.topo_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.topo_id.get_name_leafdata())
                if (self.topo_name.is_set or self.topo_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.topo_name.get_name_leafdata())
                if (self.topo_valid.is_set or self.topo_valid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.topo_valid.get_name_leafdata())
                if (self.udp_port.is_set or self.udp_port.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.udp_port.get_name_leafdata())
                if (self.vni_max.is_set or self.vni_max.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vni_max.get_name_leafdata())
                if (self.vni_min.is_set or self.vni_min.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vni_min.get_name_leafdata())
                if (self.vni_xr.is_set or self.vni_xr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vni_xr.get_name_leafdata())
                if (self.vrf_id.is_set or self.vrf_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_id.get_name_leafdata())
                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_name.get_name_leafdata())
                if (self.vrf_vni.is_set or self.vrf_vni.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_vni.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "vni" or name == "bvi-ifh" or name == "bvi-mac" or name == "bvi-state" or name == "flags" or name == "interface-name" or name == "ipv4-tbl-id" or name == "ipv6-tbl-id" or name == "mcast-flags" or name == "mcast-ipv4-address" or name == "state" or name == "topo-id" or name == "topo-name" or name == "topo-valid" or name == "udp-port" or name == "vni-max" or name == "vni-min" or name == "vni-xr" or name == "vrf-id" or name == "vrf-name" or name == "vrf-vni"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "vni"):
                    self.vni = value
                    self.vni.value_namespace = name_space
                    self.vni.value_namespace_prefix = name_space_prefix
                if(value_path == "bvi-ifh"):
                    self.bvi_ifh = value
                    self.bvi_ifh.value_namespace = name_space
                    self.bvi_ifh.value_namespace_prefix = name_space_prefix
                if(value_path == "bvi-mac"):
                    self.bvi_mac = value
                    self.bvi_mac.value_namespace = name_space
                    self.bvi_mac.value_namespace_prefix = name_space_prefix
                if(value_path == "bvi-state"):
                    self.bvi_state = value
                    self.bvi_state.value_namespace = name_space
                    self.bvi_state.value_namespace_prefix = name_space_prefix
                if(value_path == "flags"):
                    self.flags = value
                    self.flags.value_namespace = name_space
                    self.flags.value_namespace_prefix = name_space_prefix
                if(value_path == "interface-name"):
                    self.interface_name = value
                    self.interface_name.value_namespace = name_space
                    self.interface_name.value_namespace_prefix = name_space_prefix
                if(value_path == "ipv4-tbl-id"):
                    self.ipv4_tbl_id = value
                    self.ipv4_tbl_id.value_namespace = name_space
                    self.ipv4_tbl_id.value_namespace_prefix = name_space_prefix
                if(value_path == "ipv6-tbl-id"):
                    self.ipv6_tbl_id = value
                    self.ipv6_tbl_id.value_namespace = name_space
                    self.ipv6_tbl_id.value_namespace_prefix = name_space_prefix
                if(value_path == "mcast-flags"):
                    self.mcast_flags = value
                    self.mcast_flags.value_namespace = name_space
                    self.mcast_flags.value_namespace_prefix = name_space_prefix
                if(value_path == "mcast-ipv4-address"):
                    self.mcast_ipv4_address = value
                    self.mcast_ipv4_address.value_namespace = name_space
                    self.mcast_ipv4_address.value_namespace_prefix = name_space_prefix
                if(value_path == "state"):
                    self.state = value
                    self.state.value_namespace = name_space
                    self.state.value_namespace_prefix = name_space_prefix
                if(value_path == "topo-id"):
                    self.topo_id = value
                    self.topo_id.value_namespace = name_space
                    self.topo_id.value_namespace_prefix = name_space_prefix
                if(value_path == "topo-name"):
                    self.topo_name = value
                    self.topo_name.value_namespace = name_space
                    self.topo_name.value_namespace_prefix = name_space_prefix
                if(value_path == "topo-valid"):
                    self.topo_valid = value
                    self.topo_valid.value_namespace = name_space
                    self.topo_valid.value_namespace_prefix = name_space_prefix
                if(value_path == "udp-port"):
                    self.udp_port = value
                    self.udp_port.value_namespace = name_space
                    self.udp_port.value_namespace_prefix = name_space_prefix
                if(value_path == "vni-max"):
                    self.vni_max = value
                    self.vni_max.value_namespace = name_space
                    self.vni_max.value_namespace_prefix = name_space_prefix
                if(value_path == "vni-min"):
                    self.vni_min = value
                    self.vni_min.value_namespace = name_space
                    self.vni_min.value_namespace_prefix = name_space_prefix
                if(value_path == "vni-xr"):
                    self.vni_xr = value
                    self.vni_xr.value_namespace = name_space
                    self.vni_xr.value_namespace_prefix = name_space_prefix
                if(value_path == "vrf-id"):
                    self.vrf_id = value
                    self.vrf_id.value_namespace = name_space
                    self.vrf_id.value_namespace_prefix = name_space_prefix
                if(value_path == "vrf-name"):
                    self.vrf_name = value
                    self.vrf_name.value_namespace = name_space
                    self.vrf_name.value_namespace_prefix = name_space_prefix
                if(value_path == "vrf-vni"):
                    self.vrf_vni = value
                    self.vrf_vni.value_namespace = name_space
                    self.vrf_vni.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.vni:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.vni:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "vnis" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-tunnel-nve-oper:nve/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "vni"):
                for c in self.vni:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Nve.Vnis.Vni()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.vni.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "vni"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Interfaces(Entity):
        """
        Table for NVE interface attributes
        
        .. attribute:: interface
        
        	The attributes for a particular interface
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_nve_oper.Nve.Interfaces.Interface>`
        
        

        """

        _prefix = 'tunnel-nve-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Nve.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "nve"

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
                        super(Nve.Interfaces, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Nve.Interfaces, self).__setattr__(name, value)


        class Interface(Entity):
            """
            The attributes for a particular interface
            
            .. attribute:: interface_name  <key>
            
            	Interface Name
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: admin_state
            
            	Admin State
            	**type**\:  int
            
            	**range:** \-128..127
            
            .. attribute:: any_cast_source_interface_name
            
            	Anycast Source Interface name
            	**type**\:  str
            
            .. attribute:: any_cast_source_ipv4_address
            
            	Anycast Source IPv4 Address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: any_cast_source_state
            
            	Anycast Source Interface State
            	**type**\:  int
            
            	**range:** \-128..127
            
            .. attribute:: encap
            
            	Encap
            	**type**\:  int
            
            	**range:** \-128..127
            
            .. attribute:: flags
            
            	Flags
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: if_handle
            
            	NVE IfHandle
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: interface_name_xr
            
            	Interface name
            	**type**\:  str
            
            .. attribute:: source_interface_name
            
            	Source Interface name
            	**type**\:  str
            
            .. attribute:: source_ipv4_address
            
            	Source IPv4 Address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: source_state
            
            	Source Intf State
            	**type**\:  int
            
            	**range:** \-128..127
            
            .. attribute:: state
            
            	State
            	**type**\:  int
            
            	**range:** \-128..127
            
            .. attribute:: sync_mcast_flags
            
            	Sync McastFlags
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sync_mcast_ipv4_address
            
            	MCAST sync group IPv4 Address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: udp_port
            
            	UDP Port
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'tunnel-nve-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Nve.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.admin_state = YLeaf(YType.int8, "admin-state")

                self.any_cast_source_interface_name = YLeaf(YType.str, "any-cast-source-interface-name")

                self.any_cast_source_ipv4_address = YLeaf(YType.str, "any-cast-source-ipv4-address")

                self.any_cast_source_state = YLeaf(YType.int8, "any-cast-source-state")

                self.encap = YLeaf(YType.int8, "encap")

                self.flags = YLeaf(YType.uint32, "flags")

                self.if_handle = YLeaf(YType.uint64, "if-handle")

                self.interface_name_xr = YLeaf(YType.str, "interface-name-xr")

                self.source_interface_name = YLeaf(YType.str, "source-interface-name")

                self.source_ipv4_address = YLeaf(YType.str, "source-ipv4-address")

                self.source_state = YLeaf(YType.int8, "source-state")

                self.state = YLeaf(YType.int8, "state")

                self.sync_mcast_flags = YLeaf(YType.uint32, "sync-mcast-flags")

                self.sync_mcast_ipv4_address = YLeaf(YType.str, "sync-mcast-ipv4-address")

                self.udp_port = YLeaf(YType.uint32, "udp-port")

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
                                "admin_state",
                                "any_cast_source_interface_name",
                                "any_cast_source_ipv4_address",
                                "any_cast_source_state",
                                "encap",
                                "flags",
                                "if_handle",
                                "interface_name_xr",
                                "source_interface_name",
                                "source_ipv4_address",
                                "source_state",
                                "state",
                                "sync_mcast_flags",
                                "sync_mcast_ipv4_address",
                                "udp_port") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Nve.Interfaces.Interface, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Nve.Interfaces.Interface, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.interface_name.is_set or
                    self.admin_state.is_set or
                    self.any_cast_source_interface_name.is_set or
                    self.any_cast_source_ipv4_address.is_set or
                    self.any_cast_source_state.is_set or
                    self.encap.is_set or
                    self.flags.is_set or
                    self.if_handle.is_set or
                    self.interface_name_xr.is_set or
                    self.source_interface_name.is_set or
                    self.source_ipv4_address.is_set or
                    self.source_state.is_set or
                    self.state.is_set or
                    self.sync_mcast_flags.is_set or
                    self.sync_mcast_ipv4_address.is_set or
                    self.udp_port.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.interface_name.yfilter != YFilter.not_set or
                    self.admin_state.yfilter != YFilter.not_set or
                    self.any_cast_source_interface_name.yfilter != YFilter.not_set or
                    self.any_cast_source_ipv4_address.yfilter != YFilter.not_set or
                    self.any_cast_source_state.yfilter != YFilter.not_set or
                    self.encap.yfilter != YFilter.not_set or
                    self.flags.yfilter != YFilter.not_set or
                    self.if_handle.yfilter != YFilter.not_set or
                    self.interface_name_xr.yfilter != YFilter.not_set or
                    self.source_interface_name.yfilter != YFilter.not_set or
                    self.source_ipv4_address.yfilter != YFilter.not_set or
                    self.source_state.yfilter != YFilter.not_set or
                    self.state.yfilter != YFilter.not_set or
                    self.sync_mcast_flags.yfilter != YFilter.not_set or
                    self.sync_mcast_ipv4_address.yfilter != YFilter.not_set or
                    self.udp_port.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-tunnel-nve-oper:nve/interfaces/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface_name.get_name_leafdata())
                if (self.admin_state.is_set or self.admin_state.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.admin_state.get_name_leafdata())
                if (self.any_cast_source_interface_name.is_set or self.any_cast_source_interface_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.any_cast_source_interface_name.get_name_leafdata())
                if (self.any_cast_source_ipv4_address.is_set or self.any_cast_source_ipv4_address.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.any_cast_source_ipv4_address.get_name_leafdata())
                if (self.any_cast_source_state.is_set or self.any_cast_source_state.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.any_cast_source_state.get_name_leafdata())
                if (self.encap.is_set or self.encap.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.encap.get_name_leafdata())
                if (self.flags.is_set or self.flags.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.flags.get_name_leafdata())
                if (self.if_handle.is_set or self.if_handle.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.if_handle.get_name_leafdata())
                if (self.interface_name_xr.is_set or self.interface_name_xr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface_name_xr.get_name_leafdata())
                if (self.source_interface_name.is_set or self.source_interface_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.source_interface_name.get_name_leafdata())
                if (self.source_ipv4_address.is_set or self.source_ipv4_address.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.source_ipv4_address.get_name_leafdata())
                if (self.source_state.is_set or self.source_state.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.source_state.get_name_leafdata())
                if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.state.get_name_leafdata())
                if (self.sync_mcast_flags.is_set or self.sync_mcast_flags.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sync_mcast_flags.get_name_leafdata())
                if (self.sync_mcast_ipv4_address.is_set or self.sync_mcast_ipv4_address.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sync_mcast_ipv4_address.get_name_leafdata())
                if (self.udp_port.is_set or self.udp_port.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.udp_port.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "interface-name" or name == "admin-state" or name == "any-cast-source-interface-name" or name == "any-cast-source-ipv4-address" or name == "any-cast-source-state" or name == "encap" or name == "flags" or name == "if-handle" or name == "interface-name-xr" or name == "source-interface-name" or name == "source-ipv4-address" or name == "source-state" or name == "state" or name == "sync-mcast-flags" or name == "sync-mcast-ipv4-address" or name == "udp-port"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "interface-name"):
                    self.interface_name = value
                    self.interface_name.value_namespace = name_space
                    self.interface_name.value_namespace_prefix = name_space_prefix
                if(value_path == "admin-state"):
                    self.admin_state = value
                    self.admin_state.value_namespace = name_space
                    self.admin_state.value_namespace_prefix = name_space_prefix
                if(value_path == "any-cast-source-interface-name"):
                    self.any_cast_source_interface_name = value
                    self.any_cast_source_interface_name.value_namespace = name_space
                    self.any_cast_source_interface_name.value_namespace_prefix = name_space_prefix
                if(value_path == "any-cast-source-ipv4-address"):
                    self.any_cast_source_ipv4_address = value
                    self.any_cast_source_ipv4_address.value_namespace = name_space
                    self.any_cast_source_ipv4_address.value_namespace_prefix = name_space_prefix
                if(value_path == "any-cast-source-state"):
                    self.any_cast_source_state = value
                    self.any_cast_source_state.value_namespace = name_space
                    self.any_cast_source_state.value_namespace_prefix = name_space_prefix
                if(value_path == "encap"):
                    self.encap = value
                    self.encap.value_namespace = name_space
                    self.encap.value_namespace_prefix = name_space_prefix
                if(value_path == "flags"):
                    self.flags = value
                    self.flags.value_namespace = name_space
                    self.flags.value_namespace_prefix = name_space_prefix
                if(value_path == "if-handle"):
                    self.if_handle = value
                    self.if_handle.value_namespace = name_space
                    self.if_handle.value_namespace_prefix = name_space_prefix
                if(value_path == "interface-name-xr"):
                    self.interface_name_xr = value
                    self.interface_name_xr.value_namespace = name_space
                    self.interface_name_xr.value_namespace_prefix = name_space_prefix
                if(value_path == "source-interface-name"):
                    self.source_interface_name = value
                    self.source_interface_name.value_namespace = name_space
                    self.source_interface_name.value_namespace_prefix = name_space_prefix
                if(value_path == "source-ipv4-address"):
                    self.source_ipv4_address = value
                    self.source_ipv4_address.value_namespace = name_space
                    self.source_ipv4_address.value_namespace_prefix = name_space_prefix
                if(value_path == "source-state"):
                    self.source_state = value
                    self.source_state.value_namespace = name_space
                    self.source_state.value_namespace_prefix = name_space_prefix
                if(value_path == "state"):
                    self.state = value
                    self.state.value_namespace = name_space
                    self.state.value_namespace_prefix = name_space_prefix
                if(value_path == "sync-mcast-flags"):
                    self.sync_mcast_flags = value
                    self.sync_mcast_flags.value_namespace = name_space
                    self.sync_mcast_flags.value_namespace_prefix = name_space_prefix
                if(value_path == "sync-mcast-ipv4-address"):
                    self.sync_mcast_ipv4_address = value
                    self.sync_mcast_ipv4_address.value_namespace = name_space
                    self.sync_mcast_ipv4_address.value_namespace_prefix = name_space_prefix
                if(value_path == "udp-port"):
                    self.udp_port = value
                    self.udp_port.value_namespace = name_space
                    self.udp_port.value_namespace_prefix = name_space_prefix

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
                path_buffer = "Cisco-IOS-XR-tunnel-nve-oper:nve/%s" % self.get_segment_path()
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
                c = Nve.Interfaces.Interface()
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

    def has_data(self):
        return (
            (self.interfaces is not None and self.interfaces.has_data()) or
            (self.vnis is not None and self.vnis.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.interfaces is not None and self.interfaces.has_operation()) or
            (self.vnis is not None and self.vnis.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-tunnel-nve-oper:nve" + path_buffer

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

        if (child_yang_name == "interfaces"):
            if (self.interfaces is None):
                self.interfaces = Nve.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
            return self.interfaces

        if (child_yang_name == "vnis"):
            if (self.vnis is None):
                self.vnis = Nve.Vnis()
                self.vnis.parent = self
                self._children_name_map["vnis"] = "vnis"
            return self.vnis

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "interfaces" or name == "vnis"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Nve()
        return self._top_entity


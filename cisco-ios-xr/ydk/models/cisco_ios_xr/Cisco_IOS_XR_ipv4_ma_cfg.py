""" Cisco_IOS_XR_ipv4_ma_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-ma package configuration.

This module contains definitions
for the following management objects\:
  ipv4\-network\-global\: IPv4 network global configuration data
  subscriber\-pta\: subscriber pta

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Ipv4Qppb(Enum):
    """
    Ipv4Qppb

    Ipv4 qppb

    .. data:: none = 0

    	No QPPB configuration

    .. data:: ip_prec = 1

    	Enable ip-precedence based QPPB

    .. data:: qos_grp = 2

    	Enable qos-group based QPPB

    .. data:: both = 3

    	Enable both ip-precedence and qos-group based

    	QPPB

    """

    none = Enum.YLeaf(0, "none")

    ip_prec = Enum.YLeaf(1, "ip-prec")

    qos_grp = Enum.YLeaf(2, "qos-grp")

    both = Enum.YLeaf(3, "both")



class Ipv4NetworkGlobal(Entity):
    """
    IPv4 network global configuration data
    
    .. attribute:: qppb
    
    	QPPB
    	**type**\:   :py:class:`Qppb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_cfg.Ipv4NetworkGlobal.Qppb>`
    
    .. attribute:: reassemble_max_packets
    
    	Percentage of total packets available in the system
    	**type**\:  int
    
    	**range:** 1..50
    
    	**units**\: percentage
    
    .. attribute:: reassemble_time_out
    
    	Number of seconds a reassembly queue will hold before timeout
    	**type**\:  int
    
    	**range:** 1..120
    
    	**units**\: second
    
    .. attribute:: source_route
    
    	The flag for enabling whether to process packets with source routing header options
    	**type**\:  bool
    
    	**default value**\: true
    
    .. attribute:: unnumbered
    
    	Enable IPv4 processing without an explicit address
    	**type**\:   :py:class:`Unnumbered <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_cfg.Ipv4NetworkGlobal.Unnumbered>`
    
    

    """

    _prefix = 'ipv4-ma-cfg'
    _revision = '2015-07-30'

    def __init__(self):
        super(Ipv4NetworkGlobal, self).__init__()
        self._top_entity = None

        self.yang_name = "ipv4-network-global"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-ma-cfg"

        self.reassemble_max_packets = YLeaf(YType.uint32, "reassemble-max-packets")

        self.reassemble_time_out = YLeaf(YType.uint32, "reassemble-time-out")

        self.source_route = YLeaf(YType.boolean, "source-route")

        self.qppb = Ipv4NetworkGlobal.Qppb()
        self.qppb.parent = self
        self._children_name_map["qppb"] = "qppb"
        self._children_yang_names.add("qppb")

        self.unnumbered = Ipv4NetworkGlobal.Unnumbered()
        self.unnumbered.parent = self
        self._children_name_map["unnumbered"] = "unnumbered"
        self._children_yang_names.add("unnumbered")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("reassemble_max_packets",
                        "reassemble_time_out",
                        "source_route") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(Ipv4NetworkGlobal, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Ipv4NetworkGlobal, self).__setattr__(name, value)


    class Unnumbered(Entity):
        """
        Enable IPv4 processing without an explicit
        address
        
        .. attribute:: mpls
        
        	Configure MPLS routing protocol parameters
        	**type**\:   :py:class:`Mpls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_cfg.Ipv4NetworkGlobal.Unnumbered.Mpls>`
        
        

        """

        _prefix = 'ipv4-ma-cfg'
        _revision = '2015-07-30'

        def __init__(self):
            super(Ipv4NetworkGlobal.Unnumbered, self).__init__()

            self.yang_name = "unnumbered"
            self.yang_parent_name = "ipv4-network-global"

            self.mpls = Ipv4NetworkGlobal.Unnumbered.Mpls()
            self.mpls.parent = self
            self._children_name_map["mpls"] = "mpls"
            self._children_yang_names.add("mpls")


        class Mpls(Entity):
            """
            Configure MPLS routing protocol parameters
            
            .. attribute:: te
            
            	IPv4 commands for MPLS Traffic Engineering
            	**type**\:   :py:class:`Te <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_cfg.Ipv4NetworkGlobal.Unnumbered.Mpls.Te>`
            
            

            """

            _prefix = 'ipv4-ma-cfg'
            _revision = '2015-07-30'

            def __init__(self):
                super(Ipv4NetworkGlobal.Unnumbered.Mpls, self).__init__()

                self.yang_name = "mpls"
                self.yang_parent_name = "unnumbered"

                self.te = Ipv4NetworkGlobal.Unnumbered.Mpls.Te()
                self.te.parent = self
                self._children_name_map["te"] = "te"
                self._children_yang_names.add("te")


            class Te(Entity):
                """
                IPv4 commands for MPLS Traffic Engineering
                
                .. attribute:: interface
                
                	Enable IP processing without an explicit address on MPLS Traffic\-Eng
                	**type**\:  str
                
                

                """

                _prefix = 'ipv4-ma-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    super(Ipv4NetworkGlobal.Unnumbered.Mpls.Te, self).__init__()

                    self.yang_name = "te"
                    self.yang_parent_name = "mpls"

                    self.interface = YLeaf(YType.str, "interface")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("interface") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Ipv4NetworkGlobal.Unnumbered.Mpls.Te, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ipv4NetworkGlobal.Unnumbered.Mpls.Te, self).__setattr__(name, value)

                def has_data(self):
                    return self.interface.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.interface.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "te" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv4-ma-cfg:ipv4-network-global/unnumbered/mpls/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "interface"):
                        self.interface = value
                        self.interface.value_namespace = name_space
                        self.interface.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (self.te is not None and self.te.has_data())

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.te is not None and self.te.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mpls" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-ma-cfg:ipv4-network-global/unnumbered/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "te"):
                    if (self.te is None):
                        self.te = Ipv4NetworkGlobal.Unnumbered.Mpls.Te()
                        self.te.parent = self
                        self._children_name_map["te"] = "te"
                    return self.te

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "te"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (self.mpls is not None and self.mpls.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.mpls is not None and self.mpls.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "unnumbered" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-ma-cfg:ipv4-network-global/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mpls"):
                if (self.mpls is None):
                    self.mpls = Ipv4NetworkGlobal.Unnumbered.Mpls()
                    self.mpls.parent = self
                    self._children_name_map["mpls"] = "mpls"
                return self.mpls

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mpls"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Qppb(Entity):
        """
        QPPB
        
        .. attribute:: destination
        
        	QPPB configuration on destination
        	**type**\:   :py:class:`Ipv4Qppb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_cfg.Ipv4Qppb>`
        
        .. attribute:: source
        
        	QPPB configuration on source
        	**type**\:   :py:class:`Ipv4Qppb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_cfg.Ipv4Qppb>`
        
        

        """

        _prefix = 'ipv4-ma-cfg'
        _revision = '2015-07-30'

        def __init__(self):
            super(Ipv4NetworkGlobal.Qppb, self).__init__()

            self.yang_name = "qppb"
            self.yang_parent_name = "ipv4-network-global"

            self.destination = YLeaf(YType.enumeration, "destination")

            self.source = YLeaf(YType.enumeration, "source")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("destination",
                            "source") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Ipv4NetworkGlobal.Qppb, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ipv4NetworkGlobal.Qppb, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.destination.is_set or
                self.source.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.destination.yfilter != YFilter.not_set or
                self.source.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "qppb" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-ma-cfg:ipv4-network-global/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.destination.is_set or self.destination.yfilter != YFilter.not_set):
                leaf_name_data.append(self.destination.get_name_leafdata())
            if (self.source.is_set or self.source.yfilter != YFilter.not_set):
                leaf_name_data.append(self.source.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "destination" or name == "source"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "destination"):
                self.destination = value
                self.destination.value_namespace = name_space
                self.destination.value_namespace_prefix = name_space_prefix
            if(value_path == "source"):
                self.source = value
                self.source.value_namespace = name_space
                self.source.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            self.reassemble_max_packets.is_set or
            self.reassemble_time_out.is_set or
            self.source_route.is_set or
            (self.qppb is not None and self.qppb.has_data()) or
            (self.unnumbered is not None and self.unnumbered.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.reassemble_max_packets.yfilter != YFilter.not_set or
            self.reassemble_time_out.yfilter != YFilter.not_set or
            self.source_route.yfilter != YFilter.not_set or
            (self.qppb is not None and self.qppb.has_operation()) or
            (self.unnumbered is not None and self.unnumbered.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ipv4-ma-cfg:ipv4-network-global" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.reassemble_max_packets.is_set or self.reassemble_max_packets.yfilter != YFilter.not_set):
            leaf_name_data.append(self.reassemble_max_packets.get_name_leafdata())
        if (self.reassemble_time_out.is_set or self.reassemble_time_out.yfilter != YFilter.not_set):
            leaf_name_data.append(self.reassemble_time_out.get_name_leafdata())
        if (self.source_route.is_set or self.source_route.yfilter != YFilter.not_set):
            leaf_name_data.append(self.source_route.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "qppb"):
            if (self.qppb is None):
                self.qppb = Ipv4NetworkGlobal.Qppb()
                self.qppb.parent = self
                self._children_name_map["qppb"] = "qppb"
            return self.qppb

        if (child_yang_name == "unnumbered"):
            if (self.unnumbered is None):
                self.unnumbered = Ipv4NetworkGlobal.Unnumbered()
                self.unnumbered.parent = self
                self._children_name_map["unnumbered"] = "unnumbered"
            return self.unnumbered

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "qppb" or name == "unnumbered" or name == "reassemble-max-packets" or name == "reassemble-time-out" or name == "source-route"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "reassemble-max-packets"):
            self.reassemble_max_packets = value
            self.reassemble_max_packets.value_namespace = name_space
            self.reassemble_max_packets.value_namespace_prefix = name_space_prefix
        if(value_path == "reassemble-time-out"):
            self.reassemble_time_out = value
            self.reassemble_time_out.value_namespace = name_space
            self.reassemble_time_out.value_namespace_prefix = name_space_prefix
        if(value_path == "source-route"):
            self.source_route = value
            self.source_route.value_namespace = name_space
            self.source_route.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = Ipv4NetworkGlobal()
        return self._top_entity

class SubscriberPta(Entity):
    """
    subscriber pta
    
    .. attribute:: tcp_mss_adjust
    
    	TCP MSS Adjust (bytes)
    	**type**\:  int
    
    	**range:** 1280..1536
    
    	**units**\: byte
    
    

    """

    _prefix = 'ipv4-ma-cfg'
    _revision = '2015-07-30'

    def __init__(self):
        super(SubscriberPta, self).__init__()
        self._top_entity = None

        self.yang_name = "subscriber-pta"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-ma-cfg"

        self.tcp_mss_adjust = YLeaf(YType.uint32, "tcp-mss-adjust")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("tcp_mss_adjust") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(SubscriberPta, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(SubscriberPta, self).__setattr__(name, value)

    def has_data(self):
        return self.tcp_mss_adjust.is_set

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.tcp_mss_adjust.yfilter != YFilter.not_set)

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ipv4-ma-cfg:subscriber-pta" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.tcp_mss_adjust.is_set or self.tcp_mss_adjust.yfilter != YFilter.not_set):
            leaf_name_data.append(self.tcp_mss_adjust.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "tcp-mss-adjust"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "tcp-mss-adjust"):
            self.tcp_mss_adjust = value
            self.tcp_mss_adjust.value_namespace = name_space
            self.tcp_mss_adjust.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = SubscriberPta()
        return self._top_entity


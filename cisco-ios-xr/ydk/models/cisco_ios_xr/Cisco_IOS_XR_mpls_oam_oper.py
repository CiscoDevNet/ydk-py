""" Cisco_IOS_XR_mpls_oam_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR mpls\-oam package operational data.

This module contains definitions
for the following management objects\:
  mpls\-oam\: MPLS OAM operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class LspvBagInterfaceState(Enum):
    """
    LspvBagInterfaceState

    LSPV interface state

    .. data:: not_ready = 0

    	Not ready

    .. data:: admin_down = 1

    	Admin down

    .. data:: down = 2

    	Down

    .. data:: up = 3

    	UP

    .. data:: shutdown = 4

    	Shutdown

    .. data:: error_disable = 5

    	Error disable

    .. data:: down_immediate = 6

    	Immediate down

    .. data:: admin_immediate = 7

    	Immediate admin

    .. data:: graceful_down = 8

    	Graceful down

    .. data:: begin_shutdown = 9

    	Begin shutdown

    .. data:: end_shutdown = 10

    	End shutdown

    .. data:: begin_error_disable = 11

    	Begin error disable

    .. data:: end_error_disable = 12

    	End error disable

    .. data:: begin_graceful_down = 13

    	Begin graceful down

    .. data:: reset = 14

    	Reset

    .. data:: operational = 15

    	Operational

    .. data:: not_operational = 16

    	Not operational

    .. data:: not_known = 17

    	Unknown

    """

    not_ready = Enum.YLeaf(0, "not-ready")

    admin_down = Enum.YLeaf(1, "admin-down")

    down = Enum.YLeaf(2, "down")

    up = Enum.YLeaf(3, "up")

    shutdown = Enum.YLeaf(4, "shutdown")

    error_disable = Enum.YLeaf(5, "error-disable")

    down_immediate = Enum.YLeaf(6, "down-immediate")

    admin_immediate = Enum.YLeaf(7, "admin-immediate")

    graceful_down = Enum.YLeaf(8, "graceful-down")

    begin_shutdown = Enum.YLeaf(9, "begin-shutdown")

    end_shutdown = Enum.YLeaf(10, "end-shutdown")

    begin_error_disable = Enum.YLeaf(11, "begin-error-disable")

    end_error_disable = Enum.YLeaf(12, "end-error-disable")

    begin_graceful_down = Enum.YLeaf(13, "begin-graceful-down")

    reset = Enum.YLeaf(14, "reset")

    operational = Enum.YLeaf(15, "operational")

    not_operational = Enum.YLeaf(16, "not-operational")

    not_known = Enum.YLeaf(17, "not-known")



class MplsOam(Entity):
    """
    MPLS OAM operational data
    
    .. attribute:: global_
    
    	LSPV global counters operational data
    	**type**\:   :py:class:`Global_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Global_>`
    
    .. attribute:: interface
    
    	MPLS OAM interface operational data
    	**type**\:   :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface>`
    
    .. attribute:: packet
    
    	LSPV packet counters operational data
    	**type**\:   :py:class:`Packet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet>`
    
    

    """

    _prefix = 'mpls-oam-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(MplsOam, self).__init__()
        self._top_entity = None

        self.yang_name = "mpls-oam"
        self.yang_parent_name = "Cisco-IOS-XR-mpls-oam-oper"

        self.global_ = MplsOam.Global_()
        self.global_.parent = self
        self._children_name_map["global_"] = "global"
        self._children_yang_names.add("global")

        self.interface = MplsOam.Interface()
        self.interface.parent = self
        self._children_name_map["interface"] = "interface"
        self._children_yang_names.add("interface")

        self.packet = MplsOam.Packet()
        self.packet.parent = self
        self._children_name_map["packet"] = "packet"
        self._children_yang_names.add("packet")


    class Interface(Entity):
        """
        MPLS OAM interface operational data
        
        .. attribute:: briefs
        
        	MPLS OAM interface detail data
        	**type**\:   :py:class:`Briefs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Briefs>`
        
        .. attribute:: details
        
        	MPLS OAM interface detail data
        	**type**\:   :py:class:`Details <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details>`
        
        

        """

        _prefix = 'mpls-oam-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(MplsOam.Interface, self).__init__()

            self.yang_name = "interface"
            self.yang_parent_name = "mpls-oam"

            self.briefs = MplsOam.Interface.Briefs()
            self.briefs.parent = self
            self._children_name_map["briefs"] = "briefs"
            self._children_yang_names.add("briefs")

            self.details = MplsOam.Interface.Details()
            self.details.parent = self
            self._children_name_map["details"] = "details"
            self._children_yang_names.add("details")


        class Briefs(Entity):
            """
            MPLS OAM interface detail data
            
            .. attribute:: brief
            
            	MPLS OAM interface operational data
            	**type**\: list of    :py:class:`Brief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Briefs.Brief>`
            
            

            """

            _prefix = 'mpls-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsOam.Interface.Briefs, self).__init__()

                self.yang_name = "briefs"
                self.yang_parent_name = "interface"

                self.brief = YList(self)

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
                            super(MplsOam.Interface.Briefs, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsOam.Interface.Briefs, self).__setattr__(name, value)


            class Brief(Entity):
                """
                MPLS OAM interface operational data
                
                .. attribute:: interface_name  <key>
                
                	Interface name
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: interface_name_xr
                
                	Interface name
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: mtu
                
                	Interface MTU
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: prefix_length
                
                	Prefix length (IPv4)
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: prefix_length_v6
                
                	Prefix length (IPv6)
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: primary_address
                
                	Primary interface address (IPv4)
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: primary_address_v6
                
                	Primary interface address (IPv6)
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: state
                
                	Interface state
                	**type**\:   :py:class:`LspvBagInterfaceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.LspvBagInterfaceState>`
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Interface.Briefs.Brief, self).__init__()

                    self.yang_name = "brief"
                    self.yang_parent_name = "briefs"

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.interface_name_xr = YLeaf(YType.str, "interface-name-xr")

                    self.mtu = YLeaf(YType.uint32, "mtu")

                    self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                    self.prefix_length_v6 = YLeaf(YType.uint32, "prefix-length-v6")

                    self.primary_address = YLeaf(YType.str, "primary-address")

                    self.primary_address_v6 = YLeaf(YType.str, "primary-address-v6")

                    self.state = YLeaf(YType.enumeration, "state")

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
                                    "interface_name_xr",
                                    "mtu",
                                    "prefix_length",
                                    "prefix_length_v6",
                                    "primary_address",
                                    "primary_address_v6",
                                    "state") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsOam.Interface.Briefs.Brief, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsOam.Interface.Briefs.Brief, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.interface_name.is_set or
                        self.interface_name_xr.is_set or
                        self.mtu.is_set or
                        self.prefix_length.is_set or
                        self.prefix_length_v6.is_set or
                        self.primary_address.is_set or
                        self.primary_address_v6.is_set or
                        self.state.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.interface_name.yfilter != YFilter.not_set or
                        self.interface_name_xr.yfilter != YFilter.not_set or
                        self.mtu.yfilter != YFilter.not_set or
                        self.prefix_length.yfilter != YFilter.not_set or
                        self.prefix_length_v6.yfilter != YFilter.not_set or
                        self.primary_address.yfilter != YFilter.not_set or
                        self.primary_address_v6.yfilter != YFilter.not_set or
                        self.state.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "brief" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/interface/briefs/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_name.get_name_leafdata())
                    if (self.interface_name_xr.is_set or self.interface_name_xr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_name_xr.get_name_leafdata())
                    if (self.mtu.is_set or self.mtu.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mtu.get_name_leafdata())
                    if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prefix_length.get_name_leafdata())
                    if (self.prefix_length_v6.is_set or self.prefix_length_v6.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prefix_length_v6.get_name_leafdata())
                    if (self.primary_address.is_set or self.primary_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.primary_address.get_name_leafdata())
                    if (self.primary_address_v6.is_set or self.primary_address_v6.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.primary_address_v6.get_name_leafdata())
                    if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.state.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface-name" or name == "interface-name-xr" or name == "mtu" or name == "prefix-length" or name == "prefix-length-v6" or name == "primary-address" or name == "primary-address-v6" or name == "state"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "interface-name"):
                        self.interface_name = value
                        self.interface_name.value_namespace = name_space
                        self.interface_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "interface-name-xr"):
                        self.interface_name_xr = value
                        self.interface_name_xr.value_namespace = name_space
                        self.interface_name_xr.value_namespace_prefix = name_space_prefix
                    if(value_path == "mtu"):
                        self.mtu = value
                        self.mtu.value_namespace = name_space
                        self.mtu.value_namespace_prefix = name_space_prefix
                    if(value_path == "prefix-length"):
                        self.prefix_length = value
                        self.prefix_length.value_namespace = name_space
                        self.prefix_length.value_namespace_prefix = name_space_prefix
                    if(value_path == "prefix-length-v6"):
                        self.prefix_length_v6 = value
                        self.prefix_length_v6.value_namespace = name_space
                        self.prefix_length_v6.value_namespace_prefix = name_space_prefix
                    if(value_path == "primary-address"):
                        self.primary_address = value
                        self.primary_address.value_namespace = name_space
                        self.primary_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "primary-address-v6"):
                        self.primary_address_v6 = value
                        self.primary_address_v6.value_namespace = name_space
                        self.primary_address_v6.value_namespace_prefix = name_space_prefix
                    if(value_path == "state"):
                        self.state = value
                        self.state.value_namespace = name_space
                        self.state.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.brief:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.brief:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "briefs" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/interface/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "brief"):
                    for c in self.brief:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = MplsOam.Interface.Briefs.Brief()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.brief.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "brief"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Details(Entity):
            """
            MPLS OAM interface detail data
            
            .. attribute:: detail
            
            	MPLS OAM interface operational data
            	**type**\: list of    :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail>`
            
            

            """

            _prefix = 'mpls-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsOam.Interface.Details, self).__init__()

                self.yang_name = "details"
                self.yang_parent_name = "interface"

                self.detail = YList(self)

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
                            super(MplsOam.Interface.Details, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsOam.Interface.Details, self).__setattr__(name, value)


            class Detail(Entity):
                """
                MPLS OAM interface operational data
                
                .. attribute:: interface_name  <key>
                
                	Interface name
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: interface_brief
                
                	Interface brief
                	**type**\:   :py:class:`InterfaceBrief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.InterfaceBrief>`
                
                .. attribute:: packet_statistics
                
                	Packet statistics
                	**type**\:   :py:class:`PacketStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics>`
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Interface.Details.Detail, self).__init__()

                    self.yang_name = "detail"
                    self.yang_parent_name = "details"

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.interface_brief = MplsOam.Interface.Details.Detail.InterfaceBrief()
                    self.interface_brief.parent = self
                    self._children_name_map["interface_brief"] = "interface-brief"
                    self._children_yang_names.add("interface-brief")

                    self.packet_statistics = MplsOam.Interface.Details.Detail.PacketStatistics()
                    self.packet_statistics.parent = self
                    self._children_name_map["packet_statistics"] = "packet-statistics"
                    self._children_yang_names.add("packet-statistics")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("interface_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsOam.Interface.Details.Detail, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsOam.Interface.Details.Detail, self).__setattr__(name, value)


                class InterfaceBrief(Entity):
                    """
                    Interface brief
                    
                    .. attribute:: interface_name_xr
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: mtu
                    
                    	Interface MTU
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prefix_length
                    
                    	Prefix length (IPv4)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prefix_length_v6
                    
                    	Prefix length (IPv6)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: primary_address
                    
                    	Primary interface address (IPv4)
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: primary_address_v6
                    
                    	Primary interface address (IPv6)
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: state
                    
                    	Interface state
                    	**type**\:   :py:class:`LspvBagInterfaceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.LspvBagInterfaceState>`
                    
                    

                    """

                    _prefix = 'mpls-oam-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MplsOam.Interface.Details.Detail.InterfaceBrief, self).__init__()

                        self.yang_name = "interface-brief"
                        self.yang_parent_name = "detail"

                        self.interface_name_xr = YLeaf(YType.str, "interface-name-xr")

                        self.mtu = YLeaf(YType.uint32, "mtu")

                        self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                        self.prefix_length_v6 = YLeaf(YType.uint32, "prefix-length-v6")

                        self.primary_address = YLeaf(YType.str, "primary-address")

                        self.primary_address_v6 = YLeaf(YType.str, "primary-address-v6")

                        self.state = YLeaf(YType.enumeration, "state")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface_name_xr",
                                        "mtu",
                                        "prefix_length",
                                        "prefix_length_v6",
                                        "primary_address",
                                        "primary_address_v6",
                                        "state") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MplsOam.Interface.Details.Detail.InterfaceBrief, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MplsOam.Interface.Details.Detail.InterfaceBrief, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.interface_name_xr.is_set or
                            self.mtu.is_set or
                            self.prefix_length.is_set or
                            self.prefix_length_v6.is_set or
                            self.primary_address.is_set or
                            self.primary_address_v6.is_set or
                            self.state.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name_xr.yfilter != YFilter.not_set or
                            self.mtu.yfilter != YFilter.not_set or
                            self.prefix_length.yfilter != YFilter.not_set or
                            self.prefix_length_v6.yfilter != YFilter.not_set or
                            self.primary_address.yfilter != YFilter.not_set or
                            self.primary_address_v6.yfilter != YFilter.not_set or
                            self.state.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface-brief" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface_name_xr.is_set or self.interface_name_xr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name_xr.get_name_leafdata())
                        if (self.mtu.is_set or self.mtu.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mtu.get_name_leafdata())
                        if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix_length.get_name_leafdata())
                        if (self.prefix_length_v6.is_set or self.prefix_length_v6.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix_length_v6.get_name_leafdata())
                        if (self.primary_address.is_set or self.primary_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.primary_address.get_name_leafdata())
                        if (self.primary_address_v6.is_set or self.primary_address_v6.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.primary_address_v6.get_name_leafdata())
                        if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.state.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "interface-name-xr" or name == "mtu" or name == "prefix-length" or name == "prefix-length-v6" or name == "primary-address" or name == "primary-address-v6" or name == "state"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name-xr"):
                            self.interface_name_xr = value
                            self.interface_name_xr.value_namespace = name_space
                            self.interface_name_xr.value_namespace_prefix = name_space_prefix
                        if(value_path == "mtu"):
                            self.mtu = value
                            self.mtu.value_namespace = name_space
                            self.mtu.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix-length"):
                            self.prefix_length = value
                            self.prefix_length.value_namespace = name_space
                            self.prefix_length.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix-length-v6"):
                            self.prefix_length_v6 = value
                            self.prefix_length_v6.value_namespace = name_space
                            self.prefix_length_v6.value_namespace_prefix = name_space_prefix
                        if(value_path == "primary-address"):
                            self.primary_address = value
                            self.primary_address.value_namespace = name_space
                            self.primary_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "primary-address-v6"):
                            self.primary_address_v6 = value
                            self.primary_address_v6.value_namespace = name_space
                            self.primary_address_v6.value_namespace_prefix = name_space_prefix
                        if(value_path == "state"):
                            self.state = value
                            self.state.value_namespace = name_space
                            self.state.value_namespace_prefix = name_space_prefix


                class PacketStatistics(Entity):
                    """
                    Packet statistics
                    
                    .. attribute:: protect_rep_sent
                    
                    	Protect Reply Packet transmit counts
                    	**type**\:   :py:class:`ProtectRepSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent>`
                    
                    .. attribute:: protect_req_sent
                    
                    	Protect Request Packet transmit counts
                    	**type**\:   :py:class:`ProtectReqSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent>`
                    
                    .. attribute:: received
                    
                    	Packet reception counts
                    	**type**\:   :py:class:`Received <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received>`
                    
                    .. attribute:: sent
                    
                    	Packet transmit counts
                    	**type**\:   :py:class:`Sent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Sent>`
                    
                    .. attribute:: working_rep_sent
                    
                    	Working Reply Packet transmit counts
                    	**type**\:   :py:class:`WorkingRepSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent>`
                    
                    .. attribute:: working_req_sent
                    
                    	Working Request Packet transmit counts
                    	**type**\:   :py:class:`WorkingReqSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent>`
                    
                    

                    """

                    _prefix = 'mpls-oam-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MplsOam.Interface.Details.Detail.PacketStatistics, self).__init__()

                        self.yang_name = "packet-statistics"
                        self.yang_parent_name = "detail"

                        self.protect_rep_sent = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent()
                        self.protect_rep_sent.parent = self
                        self._children_name_map["protect_rep_sent"] = "protect-rep-sent"
                        self._children_yang_names.add("protect-rep-sent")

                        self.protect_req_sent = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent()
                        self.protect_req_sent.parent = self
                        self._children_name_map["protect_req_sent"] = "protect-req-sent"
                        self._children_yang_names.add("protect-req-sent")

                        self.received = MplsOam.Interface.Details.Detail.PacketStatistics.Received()
                        self.received.parent = self
                        self._children_name_map["received"] = "received"
                        self._children_yang_names.add("received")

                        self.sent = MplsOam.Interface.Details.Detail.PacketStatistics.Sent()
                        self.sent.parent = self
                        self._children_name_map["sent"] = "sent"
                        self._children_yang_names.add("sent")

                        self.working_rep_sent = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent()
                        self.working_rep_sent.parent = self
                        self._children_name_map["working_rep_sent"] = "working-rep-sent"
                        self._children_yang_names.add("working-rep-sent")

                        self.working_req_sent = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent()
                        self.working_req_sent.parent = self
                        self._children_name_map["working_req_sent"] = "working-req-sent"
                        self._children_yang_names.add("working-req-sent")


                    class Received(Entity):
                        """
                        Packet reception counts
                        
                        .. attribute:: protect_protocol_received_good_reply
                        
                        	Protect Protocol Received good reply
                        	**type**\:   :py:class:`ProtectProtocolReceivedGoodReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodReply>`
                        
                        .. attribute:: protect_protocol_received_good_request
                        
                        	Protect Protocol Received good request
                        	**type**\:   :py:class:`ProtectProtocolReceivedGoodRequest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodRequest>`
                        
                        .. attribute:: received_error_general
                        
                        	General error
                        	**type**\:   :py:class:`ReceivedErrorGeneral <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorGeneral>`
                        
                        .. attribute:: received_error_ip_header
                        
                        	IP header error
                        	**type**\:   :py:class:`ReceivedErrorIpHeader <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorIpHeader>`
                        
                        .. attribute:: received_error_no_interface
                        
                        	Error no Interfaces
                        	**type**\:   :py:class:`ReceivedErrorNoInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoInterface>`
                        
                        .. attribute:: received_error_no_memory
                        
                        	Error no memory
                        	**type**\:   :py:class:`ReceivedErrorNoMemory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoMemory>`
                        
                        .. attribute:: received_error_queue_full
                        
                        	Dropped queue full
                        	**type**\:   :py:class:`ReceivedErrorQueueFull <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorQueueFull>`
                        
                        .. attribute:: received_error_runt
                        
                        	RUNT error
                        	**type**\:   :py:class:`ReceivedErrorRunt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorRunt>`
                        
                        .. attribute:: received_error_udp_header
                        
                        	UDP header error
                        	**type**\:   :py:class:`ReceivedErrorUdpHeader <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorUdpHeader>`
                        
                        .. attribute:: received_good_bfd_reply
                        
                        	Received Reply with BFD TLV
                        	**type**\:   :py:class:`ReceivedGoodBfdReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdReply>`
                        
                        .. attribute:: received_good_bfd_request
                        
                        	Received Reqeust with BFD TLV
                        	**type**\:   :py:class:`ReceivedGoodBfdRequest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdRequest>`
                        
                        .. attribute:: received_good_reply
                        
                        	Received good reply
                        	**type**\:   :py:class:`ReceivedGoodReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodReply>`
                        
                        .. attribute:: received_good_request
                        
                        	Received good request
                        	**type**\:   :py:class:`ReceivedGoodRequest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodRequest>`
                        
                        .. attribute:: received_unknown
                        
                        	Received unknown packets
                        	**type**\:   :py:class:`ReceivedUnknown <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedUnknown>`
                        
                        

                        """

                        _prefix = 'mpls-oam-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsOam.Interface.Details.Detail.PacketStatistics.Received, self).__init__()

                            self.yang_name = "received"
                            self.yang_parent_name = "packet-statistics"

                            self.protect_protocol_received_good_reply = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodReply()
                            self.protect_protocol_received_good_reply.parent = self
                            self._children_name_map["protect_protocol_received_good_reply"] = "protect-protocol-received-good-reply"
                            self._children_yang_names.add("protect-protocol-received-good-reply")

                            self.protect_protocol_received_good_request = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodRequest()
                            self.protect_protocol_received_good_request.parent = self
                            self._children_name_map["protect_protocol_received_good_request"] = "protect-protocol-received-good-request"
                            self._children_yang_names.add("protect-protocol-received-good-request")

                            self.received_error_general = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorGeneral()
                            self.received_error_general.parent = self
                            self._children_name_map["received_error_general"] = "received-error-general"
                            self._children_yang_names.add("received-error-general")

                            self.received_error_ip_header = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorIpHeader()
                            self.received_error_ip_header.parent = self
                            self._children_name_map["received_error_ip_header"] = "received-error-ip-header"
                            self._children_yang_names.add("received-error-ip-header")

                            self.received_error_no_interface = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoInterface()
                            self.received_error_no_interface.parent = self
                            self._children_name_map["received_error_no_interface"] = "received-error-no-interface"
                            self._children_yang_names.add("received-error-no-interface")

                            self.received_error_no_memory = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoMemory()
                            self.received_error_no_memory.parent = self
                            self._children_name_map["received_error_no_memory"] = "received-error-no-memory"
                            self._children_yang_names.add("received-error-no-memory")

                            self.received_error_queue_full = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorQueueFull()
                            self.received_error_queue_full.parent = self
                            self._children_name_map["received_error_queue_full"] = "received-error-queue-full"
                            self._children_yang_names.add("received-error-queue-full")

                            self.received_error_runt = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorRunt()
                            self.received_error_runt.parent = self
                            self._children_name_map["received_error_runt"] = "received-error-runt"
                            self._children_yang_names.add("received-error-runt")

                            self.received_error_udp_header = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorUdpHeader()
                            self.received_error_udp_header.parent = self
                            self._children_name_map["received_error_udp_header"] = "received-error-udp-header"
                            self._children_yang_names.add("received-error-udp-header")

                            self.received_good_bfd_reply = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdReply()
                            self.received_good_bfd_reply.parent = self
                            self._children_name_map["received_good_bfd_reply"] = "received-good-bfd-reply"
                            self._children_yang_names.add("received-good-bfd-reply")

                            self.received_good_bfd_request = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdRequest()
                            self.received_good_bfd_request.parent = self
                            self._children_name_map["received_good_bfd_request"] = "received-good-bfd-request"
                            self._children_yang_names.add("received-good-bfd-request")

                            self.received_good_reply = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodReply()
                            self.received_good_reply.parent = self
                            self._children_name_map["received_good_reply"] = "received-good-reply"
                            self._children_yang_names.add("received-good-reply")

                            self.received_good_request = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodRequest()
                            self.received_good_request.parent = self
                            self._children_name_map["received_good_request"] = "received-good-request"
                            self._children_yang_names.add("received-good-request")

                            self.received_unknown = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedUnknown()
                            self.received_unknown.parent = self
                            self._children_name_map["received_unknown"] = "received-unknown"
                            self._children_yang_names.add("received-unknown")


                        class ReceivedGoodRequest(Entity):
                            """
                            Received good request
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodRequest, self).__init__()

                                self.yang_name = "received-good-request"
                                self.yang_parent_name = "received"

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("bytes",
                                                "packets") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodRequest, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodRequest, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.bytes.is_set or
                                    self.packets.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.bytes.yfilter != YFilter.not_set or
                                    self.packets.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "received-good-request" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bytes.get_name_leafdata())
                                if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.packets.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bytes" or name == "packets"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "bytes"):
                                    self.bytes = value
                                    self.bytes.value_namespace = name_space
                                    self.bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "packets"):
                                    self.packets = value
                                    self.packets.value_namespace = name_space
                                    self.packets.value_namespace_prefix = name_space_prefix


                        class ReceivedGoodReply(Entity):
                            """
                            Received good reply
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodReply, self).__init__()

                                self.yang_name = "received-good-reply"
                                self.yang_parent_name = "received"

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("bytes",
                                                "packets") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodReply, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodReply, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.bytes.is_set or
                                    self.packets.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.bytes.yfilter != YFilter.not_set or
                                    self.packets.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "received-good-reply" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bytes.get_name_leafdata())
                                if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.packets.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bytes" or name == "packets"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "bytes"):
                                    self.bytes = value
                                    self.bytes.value_namespace = name_space
                                    self.bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "packets"):
                                    self.packets = value
                                    self.packets.value_namespace = name_space
                                    self.packets.value_namespace_prefix = name_space_prefix


                        class ReceivedUnknown(Entity):
                            """
                            Received unknown packets
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedUnknown, self).__init__()

                                self.yang_name = "received-unknown"
                                self.yang_parent_name = "received"

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("bytes",
                                                "packets") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedUnknown, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedUnknown, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.bytes.is_set or
                                    self.packets.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.bytes.yfilter != YFilter.not_set or
                                    self.packets.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "received-unknown" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bytes.get_name_leafdata())
                                if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.packets.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bytes" or name == "packets"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "bytes"):
                                    self.bytes = value
                                    self.bytes.value_namespace = name_space
                                    self.bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "packets"):
                                    self.packets = value
                                    self.packets.value_namespace = name_space
                                    self.packets.value_namespace_prefix = name_space_prefix


                        class ReceivedErrorIpHeader(Entity):
                            """
                            IP header error
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorIpHeader, self).__init__()

                                self.yang_name = "received-error-ip-header"
                                self.yang_parent_name = "received"

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("bytes",
                                                "packets") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorIpHeader, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorIpHeader, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.bytes.is_set or
                                    self.packets.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.bytes.yfilter != YFilter.not_set or
                                    self.packets.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "received-error-ip-header" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bytes.get_name_leafdata())
                                if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.packets.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bytes" or name == "packets"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "bytes"):
                                    self.bytes = value
                                    self.bytes.value_namespace = name_space
                                    self.bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "packets"):
                                    self.packets = value
                                    self.packets.value_namespace = name_space
                                    self.packets.value_namespace_prefix = name_space_prefix


                        class ReceivedErrorUdpHeader(Entity):
                            """
                            UDP header error
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorUdpHeader, self).__init__()

                                self.yang_name = "received-error-udp-header"
                                self.yang_parent_name = "received"

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("bytes",
                                                "packets") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorUdpHeader, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorUdpHeader, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.bytes.is_set or
                                    self.packets.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.bytes.yfilter != YFilter.not_set or
                                    self.packets.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "received-error-udp-header" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bytes.get_name_leafdata())
                                if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.packets.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bytes" or name == "packets"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "bytes"):
                                    self.bytes = value
                                    self.bytes.value_namespace = name_space
                                    self.bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "packets"):
                                    self.packets = value
                                    self.packets.value_namespace = name_space
                                    self.packets.value_namespace_prefix = name_space_prefix


                        class ReceivedErrorRunt(Entity):
                            """
                            RUNT error
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorRunt, self).__init__()

                                self.yang_name = "received-error-runt"
                                self.yang_parent_name = "received"

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("bytes",
                                                "packets") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorRunt, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorRunt, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.bytes.is_set or
                                    self.packets.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.bytes.yfilter != YFilter.not_set or
                                    self.packets.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "received-error-runt" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bytes.get_name_leafdata())
                                if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.packets.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bytes" or name == "packets"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "bytes"):
                                    self.bytes = value
                                    self.bytes.value_namespace = name_space
                                    self.bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "packets"):
                                    self.packets = value
                                    self.packets.value_namespace = name_space
                                    self.packets.value_namespace_prefix = name_space_prefix


                        class ReceivedErrorQueueFull(Entity):
                            """
                            Dropped queue full
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorQueueFull, self).__init__()

                                self.yang_name = "received-error-queue-full"
                                self.yang_parent_name = "received"

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("bytes",
                                                "packets") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorQueueFull, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorQueueFull, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.bytes.is_set or
                                    self.packets.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.bytes.yfilter != YFilter.not_set or
                                    self.packets.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "received-error-queue-full" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bytes.get_name_leafdata())
                                if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.packets.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bytes" or name == "packets"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "bytes"):
                                    self.bytes = value
                                    self.bytes.value_namespace = name_space
                                    self.bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "packets"):
                                    self.packets = value
                                    self.packets.value_namespace = name_space
                                    self.packets.value_namespace_prefix = name_space_prefix


                        class ReceivedErrorGeneral(Entity):
                            """
                            General error
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorGeneral, self).__init__()

                                self.yang_name = "received-error-general"
                                self.yang_parent_name = "received"

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("bytes",
                                                "packets") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorGeneral, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorGeneral, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.bytes.is_set or
                                    self.packets.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.bytes.yfilter != YFilter.not_set or
                                    self.packets.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "received-error-general" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bytes.get_name_leafdata())
                                if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.packets.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bytes" or name == "packets"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "bytes"):
                                    self.bytes = value
                                    self.bytes.value_namespace = name_space
                                    self.bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "packets"):
                                    self.packets = value
                                    self.packets.value_namespace = name_space
                                    self.packets.value_namespace_prefix = name_space_prefix


                        class ReceivedErrorNoInterface(Entity):
                            """
                            Error no Interfaces
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoInterface, self).__init__()

                                self.yang_name = "received-error-no-interface"
                                self.yang_parent_name = "received"

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("bytes",
                                                "packets") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoInterface, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoInterface, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.bytes.is_set or
                                    self.packets.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.bytes.yfilter != YFilter.not_set or
                                    self.packets.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "received-error-no-interface" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bytes.get_name_leafdata())
                                if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.packets.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bytes" or name == "packets"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "bytes"):
                                    self.bytes = value
                                    self.bytes.value_namespace = name_space
                                    self.bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "packets"):
                                    self.packets = value
                                    self.packets.value_namespace = name_space
                                    self.packets.value_namespace_prefix = name_space_prefix


                        class ReceivedErrorNoMemory(Entity):
                            """
                            Error no memory
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoMemory, self).__init__()

                                self.yang_name = "received-error-no-memory"
                                self.yang_parent_name = "received"

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("bytes",
                                                "packets") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoMemory, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoMemory, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.bytes.is_set or
                                    self.packets.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.bytes.yfilter != YFilter.not_set or
                                    self.packets.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "received-error-no-memory" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bytes.get_name_leafdata())
                                if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.packets.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bytes" or name == "packets"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "bytes"):
                                    self.bytes = value
                                    self.bytes.value_namespace = name_space
                                    self.bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "packets"):
                                    self.packets = value
                                    self.packets.value_namespace = name_space
                                    self.packets.value_namespace_prefix = name_space_prefix


                        class ProtectProtocolReceivedGoodRequest(Entity):
                            """
                            Protect Protocol Received good request
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodRequest, self).__init__()

                                self.yang_name = "protect-protocol-received-good-request"
                                self.yang_parent_name = "received"

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("bytes",
                                                "packets") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodRequest, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodRequest, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.bytes.is_set or
                                    self.packets.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.bytes.yfilter != YFilter.not_set or
                                    self.packets.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "protect-protocol-received-good-request" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bytes.get_name_leafdata())
                                if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.packets.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bytes" or name == "packets"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "bytes"):
                                    self.bytes = value
                                    self.bytes.value_namespace = name_space
                                    self.bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "packets"):
                                    self.packets = value
                                    self.packets.value_namespace = name_space
                                    self.packets.value_namespace_prefix = name_space_prefix


                        class ProtectProtocolReceivedGoodReply(Entity):
                            """
                            Protect Protocol Received good reply
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodReply, self).__init__()

                                self.yang_name = "protect-protocol-received-good-reply"
                                self.yang_parent_name = "received"

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("bytes",
                                                "packets") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodReply, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodReply, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.bytes.is_set or
                                    self.packets.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.bytes.yfilter != YFilter.not_set or
                                    self.packets.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "protect-protocol-received-good-reply" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bytes.get_name_leafdata())
                                if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.packets.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bytes" or name == "packets"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "bytes"):
                                    self.bytes = value
                                    self.bytes.value_namespace = name_space
                                    self.bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "packets"):
                                    self.packets = value
                                    self.packets.value_namespace = name_space
                                    self.packets.value_namespace_prefix = name_space_prefix


                        class ReceivedGoodBfdRequest(Entity):
                            """
                            Received Reqeust with BFD TLV
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdRequest, self).__init__()

                                self.yang_name = "received-good-bfd-request"
                                self.yang_parent_name = "received"

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("bytes",
                                                "packets") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdRequest, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdRequest, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.bytes.is_set or
                                    self.packets.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.bytes.yfilter != YFilter.not_set or
                                    self.packets.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "received-good-bfd-request" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bytes.get_name_leafdata())
                                if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.packets.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bytes" or name == "packets"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "bytes"):
                                    self.bytes = value
                                    self.bytes.value_namespace = name_space
                                    self.bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "packets"):
                                    self.packets = value
                                    self.packets.value_namespace = name_space
                                    self.packets.value_namespace_prefix = name_space_prefix


                        class ReceivedGoodBfdReply(Entity):
                            """
                            Received Reply with BFD TLV
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdReply, self).__init__()

                                self.yang_name = "received-good-bfd-reply"
                                self.yang_parent_name = "received"

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("bytes",
                                                "packets") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdReply, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdReply, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.bytes.is_set or
                                    self.packets.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.bytes.yfilter != YFilter.not_set or
                                    self.packets.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "received-good-bfd-reply" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bytes.get_name_leafdata())
                                if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.packets.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bytes" or name == "packets"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "bytes"):
                                    self.bytes = value
                                    self.bytes.value_namespace = name_space
                                    self.bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "packets"):
                                    self.packets = value
                                    self.packets.value_namespace = name_space
                                    self.packets.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                (self.protect_protocol_received_good_reply is not None and self.protect_protocol_received_good_reply.has_data()) or
                                (self.protect_protocol_received_good_request is not None and self.protect_protocol_received_good_request.has_data()) or
                                (self.received_error_general is not None and self.received_error_general.has_data()) or
                                (self.received_error_ip_header is not None and self.received_error_ip_header.has_data()) or
                                (self.received_error_no_interface is not None and self.received_error_no_interface.has_data()) or
                                (self.received_error_no_memory is not None and self.received_error_no_memory.has_data()) or
                                (self.received_error_queue_full is not None and self.received_error_queue_full.has_data()) or
                                (self.received_error_runt is not None and self.received_error_runt.has_data()) or
                                (self.received_error_udp_header is not None and self.received_error_udp_header.has_data()) or
                                (self.received_good_bfd_reply is not None and self.received_good_bfd_reply.has_data()) or
                                (self.received_good_bfd_request is not None and self.received_good_bfd_request.has_data()) or
                                (self.received_good_reply is not None and self.received_good_reply.has_data()) or
                                (self.received_good_request is not None and self.received_good_request.has_data()) or
                                (self.received_unknown is not None and self.received_unknown.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.protect_protocol_received_good_reply is not None and self.protect_protocol_received_good_reply.has_operation()) or
                                (self.protect_protocol_received_good_request is not None and self.protect_protocol_received_good_request.has_operation()) or
                                (self.received_error_general is not None and self.received_error_general.has_operation()) or
                                (self.received_error_ip_header is not None and self.received_error_ip_header.has_operation()) or
                                (self.received_error_no_interface is not None and self.received_error_no_interface.has_operation()) or
                                (self.received_error_no_memory is not None and self.received_error_no_memory.has_operation()) or
                                (self.received_error_queue_full is not None and self.received_error_queue_full.has_operation()) or
                                (self.received_error_runt is not None and self.received_error_runt.has_operation()) or
                                (self.received_error_udp_header is not None and self.received_error_udp_header.has_operation()) or
                                (self.received_good_bfd_reply is not None and self.received_good_bfd_reply.has_operation()) or
                                (self.received_good_bfd_request is not None and self.received_good_bfd_request.has_operation()) or
                                (self.received_good_reply is not None and self.received_good_reply.has_operation()) or
                                (self.received_good_request is not None and self.received_good_request.has_operation()) or
                                (self.received_unknown is not None and self.received_unknown.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "received" + path_buffer

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

                            if (child_yang_name == "protect-protocol-received-good-reply"):
                                if (self.protect_protocol_received_good_reply is None):
                                    self.protect_protocol_received_good_reply = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodReply()
                                    self.protect_protocol_received_good_reply.parent = self
                                    self._children_name_map["protect_protocol_received_good_reply"] = "protect-protocol-received-good-reply"
                                return self.protect_protocol_received_good_reply

                            if (child_yang_name == "protect-protocol-received-good-request"):
                                if (self.protect_protocol_received_good_request is None):
                                    self.protect_protocol_received_good_request = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodRequest()
                                    self.protect_protocol_received_good_request.parent = self
                                    self._children_name_map["protect_protocol_received_good_request"] = "protect-protocol-received-good-request"
                                return self.protect_protocol_received_good_request

                            if (child_yang_name == "received-error-general"):
                                if (self.received_error_general is None):
                                    self.received_error_general = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorGeneral()
                                    self.received_error_general.parent = self
                                    self._children_name_map["received_error_general"] = "received-error-general"
                                return self.received_error_general

                            if (child_yang_name == "received-error-ip-header"):
                                if (self.received_error_ip_header is None):
                                    self.received_error_ip_header = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorIpHeader()
                                    self.received_error_ip_header.parent = self
                                    self._children_name_map["received_error_ip_header"] = "received-error-ip-header"
                                return self.received_error_ip_header

                            if (child_yang_name == "received-error-no-interface"):
                                if (self.received_error_no_interface is None):
                                    self.received_error_no_interface = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoInterface()
                                    self.received_error_no_interface.parent = self
                                    self._children_name_map["received_error_no_interface"] = "received-error-no-interface"
                                return self.received_error_no_interface

                            if (child_yang_name == "received-error-no-memory"):
                                if (self.received_error_no_memory is None):
                                    self.received_error_no_memory = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoMemory()
                                    self.received_error_no_memory.parent = self
                                    self._children_name_map["received_error_no_memory"] = "received-error-no-memory"
                                return self.received_error_no_memory

                            if (child_yang_name == "received-error-queue-full"):
                                if (self.received_error_queue_full is None):
                                    self.received_error_queue_full = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorQueueFull()
                                    self.received_error_queue_full.parent = self
                                    self._children_name_map["received_error_queue_full"] = "received-error-queue-full"
                                return self.received_error_queue_full

                            if (child_yang_name == "received-error-runt"):
                                if (self.received_error_runt is None):
                                    self.received_error_runt = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorRunt()
                                    self.received_error_runt.parent = self
                                    self._children_name_map["received_error_runt"] = "received-error-runt"
                                return self.received_error_runt

                            if (child_yang_name == "received-error-udp-header"):
                                if (self.received_error_udp_header is None):
                                    self.received_error_udp_header = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorUdpHeader()
                                    self.received_error_udp_header.parent = self
                                    self._children_name_map["received_error_udp_header"] = "received-error-udp-header"
                                return self.received_error_udp_header

                            if (child_yang_name == "received-good-bfd-reply"):
                                if (self.received_good_bfd_reply is None):
                                    self.received_good_bfd_reply = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdReply()
                                    self.received_good_bfd_reply.parent = self
                                    self._children_name_map["received_good_bfd_reply"] = "received-good-bfd-reply"
                                return self.received_good_bfd_reply

                            if (child_yang_name == "received-good-bfd-request"):
                                if (self.received_good_bfd_request is None):
                                    self.received_good_bfd_request = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdRequest()
                                    self.received_good_bfd_request.parent = self
                                    self._children_name_map["received_good_bfd_request"] = "received-good-bfd-request"
                                return self.received_good_bfd_request

                            if (child_yang_name == "received-good-reply"):
                                if (self.received_good_reply is None):
                                    self.received_good_reply = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodReply()
                                    self.received_good_reply.parent = self
                                    self._children_name_map["received_good_reply"] = "received-good-reply"
                                return self.received_good_reply

                            if (child_yang_name == "received-good-request"):
                                if (self.received_good_request is None):
                                    self.received_good_request = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodRequest()
                                    self.received_good_request.parent = self
                                    self._children_name_map["received_good_request"] = "received-good-request"
                                return self.received_good_request

                            if (child_yang_name == "received-unknown"):
                                if (self.received_unknown is None):
                                    self.received_unknown = MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedUnknown()
                                    self.received_unknown.parent = self
                                    self._children_name_map["received_unknown"] = "received-unknown"
                                return self.received_unknown

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "protect-protocol-received-good-reply" or name == "protect-protocol-received-good-request" or name == "received-error-general" or name == "received-error-ip-header" or name == "received-error-no-interface" or name == "received-error-no-memory" or name == "received-error-queue-full" or name == "received-error-runt" or name == "received-error-udp-header" or name == "received-good-bfd-reply" or name == "received-good-bfd-request" or name == "received-good-reply" or name == "received-good-request" or name == "received-unknown"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class Sent(Entity):
                        """
                        Packet transmit counts
                        
                        .. attribute:: bfd_no_reply
                        
                        	No Reply action for echo reqeust of BFD bootstrap
                        	**type**\:   :py:class:`BfdNoReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Sent.BfdNoReply>`
                        
                        .. attribute:: transmit_bfd_good
                        
                        	Transmit good BFD request packets
                        	**type**\:   :py:class:`TransmitBfdGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitBfdGood>`
                        
                        .. attribute:: transmit_drop
                        
                        	Transmit drop packets
                        	**type**\:   :py:class:`TransmitDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitDrop>`
                        
                        .. attribute:: transmit_good
                        
                        	Transmit good packets
                        	**type**\:   :py:class:`TransmitGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitGood>`
                        
                        

                        """

                        _prefix = 'mpls-oam-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsOam.Interface.Details.Detail.PacketStatistics.Sent, self).__init__()

                            self.yang_name = "sent"
                            self.yang_parent_name = "packet-statistics"

                            self.bfd_no_reply = MplsOam.Interface.Details.Detail.PacketStatistics.Sent.BfdNoReply()
                            self.bfd_no_reply.parent = self
                            self._children_name_map["bfd_no_reply"] = "bfd-no-reply"
                            self._children_yang_names.add("bfd-no-reply")

                            self.transmit_bfd_good = MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitBfdGood()
                            self.transmit_bfd_good.parent = self
                            self._children_name_map["transmit_bfd_good"] = "transmit-bfd-good"
                            self._children_yang_names.add("transmit-bfd-good")

                            self.transmit_drop = MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitDrop()
                            self.transmit_drop.parent = self
                            self._children_name_map["transmit_drop"] = "transmit-drop"
                            self._children_yang_names.add("transmit-drop")

                            self.transmit_good = MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitGood()
                            self.transmit_good.parent = self
                            self._children_name_map["transmit_good"] = "transmit-good"
                            self._children_yang_names.add("transmit-good")


                        class TransmitGood(Entity):
                            """
                            Transmit good packets
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitGood, self).__init__()

                                self.yang_name = "transmit-good"
                                self.yang_parent_name = "sent"

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("bytes",
                                                "packets") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitGood, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitGood, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.bytes.is_set or
                                    self.packets.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.bytes.yfilter != YFilter.not_set or
                                    self.packets.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "transmit-good" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bytes.get_name_leafdata())
                                if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.packets.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bytes" or name == "packets"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "bytes"):
                                    self.bytes = value
                                    self.bytes.value_namespace = name_space
                                    self.bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "packets"):
                                    self.packets = value
                                    self.packets.value_namespace = name_space
                                    self.packets.value_namespace_prefix = name_space_prefix


                        class TransmitDrop(Entity):
                            """
                            Transmit drop packets
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitDrop, self).__init__()

                                self.yang_name = "transmit-drop"
                                self.yang_parent_name = "sent"

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("bytes",
                                                "packets") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitDrop, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitDrop, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.bytes.is_set or
                                    self.packets.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.bytes.yfilter != YFilter.not_set or
                                    self.packets.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "transmit-drop" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bytes.get_name_leafdata())
                                if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.packets.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bytes" or name == "packets"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "bytes"):
                                    self.bytes = value
                                    self.bytes.value_namespace = name_space
                                    self.bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "packets"):
                                    self.packets = value
                                    self.packets.value_namespace = name_space
                                    self.packets.value_namespace_prefix = name_space_prefix


                        class TransmitBfdGood(Entity):
                            """
                            Transmit good BFD request packets
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitBfdGood, self).__init__()

                                self.yang_name = "transmit-bfd-good"
                                self.yang_parent_name = "sent"

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("bytes",
                                                "packets") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitBfdGood, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitBfdGood, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.bytes.is_set or
                                    self.packets.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.bytes.yfilter != YFilter.not_set or
                                    self.packets.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "transmit-bfd-good" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bytes.get_name_leafdata())
                                if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.packets.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bytes" or name == "packets"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "bytes"):
                                    self.bytes = value
                                    self.bytes.value_namespace = name_space
                                    self.bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "packets"):
                                    self.packets = value
                                    self.packets.value_namespace = name_space
                                    self.packets.value_namespace_prefix = name_space_prefix


                        class BfdNoReply(Entity):
                            """
                            No Reply action for echo reqeust of BFD
                            bootstrap
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.Sent.BfdNoReply, self).__init__()

                                self.yang_name = "bfd-no-reply"
                                self.yang_parent_name = "sent"

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("bytes",
                                                "packets") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsOam.Interface.Details.Detail.PacketStatistics.Sent.BfdNoReply, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsOam.Interface.Details.Detail.PacketStatistics.Sent.BfdNoReply, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.bytes.is_set or
                                    self.packets.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.bytes.yfilter != YFilter.not_set or
                                    self.packets.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "bfd-no-reply" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bytes.get_name_leafdata())
                                if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.packets.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bytes" or name == "packets"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "bytes"):
                                    self.bytes = value
                                    self.bytes.value_namespace = name_space
                                    self.bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "packets"):
                                    self.packets = value
                                    self.packets.value_namespace = name_space
                                    self.packets.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                (self.bfd_no_reply is not None and self.bfd_no_reply.has_data()) or
                                (self.transmit_bfd_good is not None and self.transmit_bfd_good.has_data()) or
                                (self.transmit_drop is not None and self.transmit_drop.has_data()) or
                                (self.transmit_good is not None and self.transmit_good.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.bfd_no_reply is not None and self.bfd_no_reply.has_operation()) or
                                (self.transmit_bfd_good is not None and self.transmit_bfd_good.has_operation()) or
                                (self.transmit_drop is not None and self.transmit_drop.has_operation()) or
                                (self.transmit_good is not None and self.transmit_good.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "sent" + path_buffer

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

                            if (child_yang_name == "bfd-no-reply"):
                                if (self.bfd_no_reply is None):
                                    self.bfd_no_reply = MplsOam.Interface.Details.Detail.PacketStatistics.Sent.BfdNoReply()
                                    self.bfd_no_reply.parent = self
                                    self._children_name_map["bfd_no_reply"] = "bfd-no-reply"
                                return self.bfd_no_reply

                            if (child_yang_name == "transmit-bfd-good"):
                                if (self.transmit_bfd_good is None):
                                    self.transmit_bfd_good = MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitBfdGood()
                                    self.transmit_bfd_good.parent = self
                                    self._children_name_map["transmit_bfd_good"] = "transmit-bfd-good"
                                return self.transmit_bfd_good

                            if (child_yang_name == "transmit-drop"):
                                if (self.transmit_drop is None):
                                    self.transmit_drop = MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitDrop()
                                    self.transmit_drop.parent = self
                                    self._children_name_map["transmit_drop"] = "transmit-drop"
                                return self.transmit_drop

                            if (child_yang_name == "transmit-good"):
                                if (self.transmit_good is None):
                                    self.transmit_good = MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitGood()
                                    self.transmit_good.parent = self
                                    self._children_name_map["transmit_good"] = "transmit-good"
                                return self.transmit_good

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "bfd-no-reply" or name == "transmit-bfd-good" or name == "transmit-drop" or name == "transmit-good"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class WorkingReqSent(Entity):
                        """
                        Working Request Packet transmit counts
                        
                        .. attribute:: bfd_no_reply
                        
                        	No Reply action for echo reqeust of BFD bootstrap
                        	**type**\:   :py:class:`BfdNoReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.BfdNoReply>`
                        
                        .. attribute:: transmit_bfd_good
                        
                        	Transmit good BFD request packets
                        	**type**\:   :py:class:`TransmitBfdGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitBfdGood>`
                        
                        .. attribute:: transmit_drop
                        
                        	Transmit drop packets
                        	**type**\:   :py:class:`TransmitDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitDrop>`
                        
                        .. attribute:: transmit_good
                        
                        	Transmit good packets
                        	**type**\:   :py:class:`TransmitGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitGood>`
                        
                        

                        """

                        _prefix = 'mpls-oam-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent, self).__init__()

                            self.yang_name = "working-req-sent"
                            self.yang_parent_name = "packet-statistics"

                            self.bfd_no_reply = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.BfdNoReply()
                            self.bfd_no_reply.parent = self
                            self._children_name_map["bfd_no_reply"] = "bfd-no-reply"
                            self._children_yang_names.add("bfd-no-reply")

                            self.transmit_bfd_good = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitBfdGood()
                            self.transmit_bfd_good.parent = self
                            self._children_name_map["transmit_bfd_good"] = "transmit-bfd-good"
                            self._children_yang_names.add("transmit-bfd-good")

                            self.transmit_drop = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitDrop()
                            self.transmit_drop.parent = self
                            self._children_name_map["transmit_drop"] = "transmit-drop"
                            self._children_yang_names.add("transmit-drop")

                            self.transmit_good = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitGood()
                            self.transmit_good.parent = self
                            self._children_name_map["transmit_good"] = "transmit-good"
                            self._children_yang_names.add("transmit-good")


                        class TransmitGood(Entity):
                            """
                            Transmit good packets
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitGood, self).__init__()

                                self.yang_name = "transmit-good"
                                self.yang_parent_name = "working-req-sent"

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("bytes",
                                                "packets") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitGood, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitGood, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.bytes.is_set or
                                    self.packets.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.bytes.yfilter != YFilter.not_set or
                                    self.packets.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "transmit-good" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bytes.get_name_leafdata())
                                if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.packets.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bytes" or name == "packets"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "bytes"):
                                    self.bytes = value
                                    self.bytes.value_namespace = name_space
                                    self.bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "packets"):
                                    self.packets = value
                                    self.packets.value_namespace = name_space
                                    self.packets.value_namespace_prefix = name_space_prefix


                        class TransmitDrop(Entity):
                            """
                            Transmit drop packets
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitDrop, self).__init__()

                                self.yang_name = "transmit-drop"
                                self.yang_parent_name = "working-req-sent"

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("bytes",
                                                "packets") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitDrop, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitDrop, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.bytes.is_set or
                                    self.packets.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.bytes.yfilter != YFilter.not_set or
                                    self.packets.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "transmit-drop" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bytes.get_name_leafdata())
                                if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.packets.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bytes" or name == "packets"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "bytes"):
                                    self.bytes = value
                                    self.bytes.value_namespace = name_space
                                    self.bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "packets"):
                                    self.packets = value
                                    self.packets.value_namespace = name_space
                                    self.packets.value_namespace_prefix = name_space_prefix


                        class TransmitBfdGood(Entity):
                            """
                            Transmit good BFD request packets
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitBfdGood, self).__init__()

                                self.yang_name = "transmit-bfd-good"
                                self.yang_parent_name = "working-req-sent"

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("bytes",
                                                "packets") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitBfdGood, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitBfdGood, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.bytes.is_set or
                                    self.packets.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.bytes.yfilter != YFilter.not_set or
                                    self.packets.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "transmit-bfd-good" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bytes.get_name_leafdata())
                                if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.packets.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bytes" or name == "packets"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "bytes"):
                                    self.bytes = value
                                    self.bytes.value_namespace = name_space
                                    self.bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "packets"):
                                    self.packets = value
                                    self.packets.value_namespace = name_space
                                    self.packets.value_namespace_prefix = name_space_prefix


                        class BfdNoReply(Entity):
                            """
                            No Reply action for echo reqeust of BFD
                            bootstrap
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.BfdNoReply, self).__init__()

                                self.yang_name = "bfd-no-reply"
                                self.yang_parent_name = "working-req-sent"

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("bytes",
                                                "packets") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.BfdNoReply, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.BfdNoReply, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.bytes.is_set or
                                    self.packets.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.bytes.yfilter != YFilter.not_set or
                                    self.packets.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "bfd-no-reply" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bytes.get_name_leafdata())
                                if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.packets.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bytes" or name == "packets"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "bytes"):
                                    self.bytes = value
                                    self.bytes.value_namespace = name_space
                                    self.bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "packets"):
                                    self.packets = value
                                    self.packets.value_namespace = name_space
                                    self.packets.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                (self.bfd_no_reply is not None and self.bfd_no_reply.has_data()) or
                                (self.transmit_bfd_good is not None and self.transmit_bfd_good.has_data()) or
                                (self.transmit_drop is not None and self.transmit_drop.has_data()) or
                                (self.transmit_good is not None and self.transmit_good.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.bfd_no_reply is not None and self.bfd_no_reply.has_operation()) or
                                (self.transmit_bfd_good is not None and self.transmit_bfd_good.has_operation()) or
                                (self.transmit_drop is not None and self.transmit_drop.has_operation()) or
                                (self.transmit_good is not None and self.transmit_good.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "working-req-sent" + path_buffer

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

                            if (child_yang_name == "bfd-no-reply"):
                                if (self.bfd_no_reply is None):
                                    self.bfd_no_reply = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.BfdNoReply()
                                    self.bfd_no_reply.parent = self
                                    self._children_name_map["bfd_no_reply"] = "bfd-no-reply"
                                return self.bfd_no_reply

                            if (child_yang_name == "transmit-bfd-good"):
                                if (self.transmit_bfd_good is None):
                                    self.transmit_bfd_good = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitBfdGood()
                                    self.transmit_bfd_good.parent = self
                                    self._children_name_map["transmit_bfd_good"] = "transmit-bfd-good"
                                return self.transmit_bfd_good

                            if (child_yang_name == "transmit-drop"):
                                if (self.transmit_drop is None):
                                    self.transmit_drop = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitDrop()
                                    self.transmit_drop.parent = self
                                    self._children_name_map["transmit_drop"] = "transmit-drop"
                                return self.transmit_drop

                            if (child_yang_name == "transmit-good"):
                                if (self.transmit_good is None):
                                    self.transmit_good = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitGood()
                                    self.transmit_good.parent = self
                                    self._children_name_map["transmit_good"] = "transmit-good"
                                return self.transmit_good

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "bfd-no-reply" or name == "transmit-bfd-good" or name == "transmit-drop" or name == "transmit-good"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class WorkingRepSent(Entity):
                        """
                        Working Reply Packet transmit counts
                        
                        .. attribute:: bfd_no_reply
                        
                        	No Reply action for echo reqeust of BFD bootstrap
                        	**type**\:   :py:class:`BfdNoReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.BfdNoReply>`
                        
                        .. attribute:: transmit_bfd_good
                        
                        	Transmit good BFD request packets
                        	**type**\:   :py:class:`TransmitBfdGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitBfdGood>`
                        
                        .. attribute:: transmit_drop
                        
                        	Transmit drop packets
                        	**type**\:   :py:class:`TransmitDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitDrop>`
                        
                        .. attribute:: transmit_good
                        
                        	Transmit good packets
                        	**type**\:   :py:class:`TransmitGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitGood>`
                        
                        

                        """

                        _prefix = 'mpls-oam-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent, self).__init__()

                            self.yang_name = "working-rep-sent"
                            self.yang_parent_name = "packet-statistics"

                            self.bfd_no_reply = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.BfdNoReply()
                            self.bfd_no_reply.parent = self
                            self._children_name_map["bfd_no_reply"] = "bfd-no-reply"
                            self._children_yang_names.add("bfd-no-reply")

                            self.transmit_bfd_good = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitBfdGood()
                            self.transmit_bfd_good.parent = self
                            self._children_name_map["transmit_bfd_good"] = "transmit-bfd-good"
                            self._children_yang_names.add("transmit-bfd-good")

                            self.transmit_drop = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitDrop()
                            self.transmit_drop.parent = self
                            self._children_name_map["transmit_drop"] = "transmit-drop"
                            self._children_yang_names.add("transmit-drop")

                            self.transmit_good = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitGood()
                            self.transmit_good.parent = self
                            self._children_name_map["transmit_good"] = "transmit-good"
                            self._children_yang_names.add("transmit-good")


                        class TransmitGood(Entity):
                            """
                            Transmit good packets
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitGood, self).__init__()

                                self.yang_name = "transmit-good"
                                self.yang_parent_name = "working-rep-sent"

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("bytes",
                                                "packets") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitGood, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitGood, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.bytes.is_set or
                                    self.packets.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.bytes.yfilter != YFilter.not_set or
                                    self.packets.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "transmit-good" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bytes.get_name_leafdata())
                                if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.packets.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bytes" or name == "packets"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "bytes"):
                                    self.bytes = value
                                    self.bytes.value_namespace = name_space
                                    self.bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "packets"):
                                    self.packets = value
                                    self.packets.value_namespace = name_space
                                    self.packets.value_namespace_prefix = name_space_prefix


                        class TransmitDrop(Entity):
                            """
                            Transmit drop packets
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitDrop, self).__init__()

                                self.yang_name = "transmit-drop"
                                self.yang_parent_name = "working-rep-sent"

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("bytes",
                                                "packets") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitDrop, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitDrop, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.bytes.is_set or
                                    self.packets.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.bytes.yfilter != YFilter.not_set or
                                    self.packets.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "transmit-drop" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bytes.get_name_leafdata())
                                if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.packets.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bytes" or name == "packets"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "bytes"):
                                    self.bytes = value
                                    self.bytes.value_namespace = name_space
                                    self.bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "packets"):
                                    self.packets = value
                                    self.packets.value_namespace = name_space
                                    self.packets.value_namespace_prefix = name_space_prefix


                        class TransmitBfdGood(Entity):
                            """
                            Transmit good BFD request packets
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitBfdGood, self).__init__()

                                self.yang_name = "transmit-bfd-good"
                                self.yang_parent_name = "working-rep-sent"

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("bytes",
                                                "packets") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitBfdGood, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitBfdGood, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.bytes.is_set or
                                    self.packets.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.bytes.yfilter != YFilter.not_set or
                                    self.packets.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "transmit-bfd-good" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bytes.get_name_leafdata())
                                if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.packets.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bytes" or name == "packets"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "bytes"):
                                    self.bytes = value
                                    self.bytes.value_namespace = name_space
                                    self.bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "packets"):
                                    self.packets = value
                                    self.packets.value_namespace = name_space
                                    self.packets.value_namespace_prefix = name_space_prefix


                        class BfdNoReply(Entity):
                            """
                            No Reply action for echo reqeust of BFD
                            bootstrap
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.BfdNoReply, self).__init__()

                                self.yang_name = "bfd-no-reply"
                                self.yang_parent_name = "working-rep-sent"

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("bytes",
                                                "packets") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.BfdNoReply, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.BfdNoReply, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.bytes.is_set or
                                    self.packets.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.bytes.yfilter != YFilter.not_set or
                                    self.packets.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "bfd-no-reply" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bytes.get_name_leafdata())
                                if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.packets.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bytes" or name == "packets"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "bytes"):
                                    self.bytes = value
                                    self.bytes.value_namespace = name_space
                                    self.bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "packets"):
                                    self.packets = value
                                    self.packets.value_namespace = name_space
                                    self.packets.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                (self.bfd_no_reply is not None and self.bfd_no_reply.has_data()) or
                                (self.transmit_bfd_good is not None and self.transmit_bfd_good.has_data()) or
                                (self.transmit_drop is not None and self.transmit_drop.has_data()) or
                                (self.transmit_good is not None and self.transmit_good.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.bfd_no_reply is not None and self.bfd_no_reply.has_operation()) or
                                (self.transmit_bfd_good is not None and self.transmit_bfd_good.has_operation()) or
                                (self.transmit_drop is not None and self.transmit_drop.has_operation()) or
                                (self.transmit_good is not None and self.transmit_good.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "working-rep-sent" + path_buffer

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

                            if (child_yang_name == "bfd-no-reply"):
                                if (self.bfd_no_reply is None):
                                    self.bfd_no_reply = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.BfdNoReply()
                                    self.bfd_no_reply.parent = self
                                    self._children_name_map["bfd_no_reply"] = "bfd-no-reply"
                                return self.bfd_no_reply

                            if (child_yang_name == "transmit-bfd-good"):
                                if (self.transmit_bfd_good is None):
                                    self.transmit_bfd_good = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitBfdGood()
                                    self.transmit_bfd_good.parent = self
                                    self._children_name_map["transmit_bfd_good"] = "transmit-bfd-good"
                                return self.transmit_bfd_good

                            if (child_yang_name == "transmit-drop"):
                                if (self.transmit_drop is None):
                                    self.transmit_drop = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitDrop()
                                    self.transmit_drop.parent = self
                                    self._children_name_map["transmit_drop"] = "transmit-drop"
                                return self.transmit_drop

                            if (child_yang_name == "transmit-good"):
                                if (self.transmit_good is None):
                                    self.transmit_good = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitGood()
                                    self.transmit_good.parent = self
                                    self._children_name_map["transmit_good"] = "transmit-good"
                                return self.transmit_good

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "bfd-no-reply" or name == "transmit-bfd-good" or name == "transmit-drop" or name == "transmit-good"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class ProtectReqSent(Entity):
                        """
                        Protect Request Packet transmit counts
                        
                        .. attribute:: bfd_no_reply
                        
                        	No Reply action for echo reqeust of BFD bootstrap
                        	**type**\:   :py:class:`BfdNoReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.BfdNoReply>`
                        
                        .. attribute:: transmit_bfd_good
                        
                        	Transmit good BFD request packets
                        	**type**\:   :py:class:`TransmitBfdGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitBfdGood>`
                        
                        .. attribute:: transmit_drop
                        
                        	Transmit drop packets
                        	**type**\:   :py:class:`TransmitDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitDrop>`
                        
                        .. attribute:: transmit_good
                        
                        	Transmit good packets
                        	**type**\:   :py:class:`TransmitGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitGood>`
                        
                        

                        """

                        _prefix = 'mpls-oam-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent, self).__init__()

                            self.yang_name = "protect-req-sent"
                            self.yang_parent_name = "packet-statistics"

                            self.bfd_no_reply = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.BfdNoReply()
                            self.bfd_no_reply.parent = self
                            self._children_name_map["bfd_no_reply"] = "bfd-no-reply"
                            self._children_yang_names.add("bfd-no-reply")

                            self.transmit_bfd_good = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitBfdGood()
                            self.transmit_bfd_good.parent = self
                            self._children_name_map["transmit_bfd_good"] = "transmit-bfd-good"
                            self._children_yang_names.add("transmit-bfd-good")

                            self.transmit_drop = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitDrop()
                            self.transmit_drop.parent = self
                            self._children_name_map["transmit_drop"] = "transmit-drop"
                            self._children_yang_names.add("transmit-drop")

                            self.transmit_good = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitGood()
                            self.transmit_good.parent = self
                            self._children_name_map["transmit_good"] = "transmit-good"
                            self._children_yang_names.add("transmit-good")


                        class TransmitGood(Entity):
                            """
                            Transmit good packets
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitGood, self).__init__()

                                self.yang_name = "transmit-good"
                                self.yang_parent_name = "protect-req-sent"

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("bytes",
                                                "packets") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitGood, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitGood, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.bytes.is_set or
                                    self.packets.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.bytes.yfilter != YFilter.not_set or
                                    self.packets.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "transmit-good" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bytes.get_name_leafdata())
                                if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.packets.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bytes" or name == "packets"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "bytes"):
                                    self.bytes = value
                                    self.bytes.value_namespace = name_space
                                    self.bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "packets"):
                                    self.packets = value
                                    self.packets.value_namespace = name_space
                                    self.packets.value_namespace_prefix = name_space_prefix


                        class TransmitDrop(Entity):
                            """
                            Transmit drop packets
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitDrop, self).__init__()

                                self.yang_name = "transmit-drop"
                                self.yang_parent_name = "protect-req-sent"

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("bytes",
                                                "packets") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitDrop, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitDrop, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.bytes.is_set or
                                    self.packets.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.bytes.yfilter != YFilter.not_set or
                                    self.packets.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "transmit-drop" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bytes.get_name_leafdata())
                                if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.packets.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bytes" or name == "packets"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "bytes"):
                                    self.bytes = value
                                    self.bytes.value_namespace = name_space
                                    self.bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "packets"):
                                    self.packets = value
                                    self.packets.value_namespace = name_space
                                    self.packets.value_namespace_prefix = name_space_prefix


                        class TransmitBfdGood(Entity):
                            """
                            Transmit good BFD request packets
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitBfdGood, self).__init__()

                                self.yang_name = "transmit-bfd-good"
                                self.yang_parent_name = "protect-req-sent"

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("bytes",
                                                "packets") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitBfdGood, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitBfdGood, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.bytes.is_set or
                                    self.packets.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.bytes.yfilter != YFilter.not_set or
                                    self.packets.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "transmit-bfd-good" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bytes.get_name_leafdata())
                                if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.packets.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bytes" or name == "packets"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "bytes"):
                                    self.bytes = value
                                    self.bytes.value_namespace = name_space
                                    self.bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "packets"):
                                    self.packets = value
                                    self.packets.value_namespace = name_space
                                    self.packets.value_namespace_prefix = name_space_prefix


                        class BfdNoReply(Entity):
                            """
                            No Reply action for echo reqeust of BFD
                            bootstrap
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.BfdNoReply, self).__init__()

                                self.yang_name = "bfd-no-reply"
                                self.yang_parent_name = "protect-req-sent"

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("bytes",
                                                "packets") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.BfdNoReply, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.BfdNoReply, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.bytes.is_set or
                                    self.packets.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.bytes.yfilter != YFilter.not_set or
                                    self.packets.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "bfd-no-reply" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bytes.get_name_leafdata())
                                if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.packets.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bytes" or name == "packets"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "bytes"):
                                    self.bytes = value
                                    self.bytes.value_namespace = name_space
                                    self.bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "packets"):
                                    self.packets = value
                                    self.packets.value_namespace = name_space
                                    self.packets.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                (self.bfd_no_reply is not None and self.bfd_no_reply.has_data()) or
                                (self.transmit_bfd_good is not None and self.transmit_bfd_good.has_data()) or
                                (self.transmit_drop is not None and self.transmit_drop.has_data()) or
                                (self.transmit_good is not None and self.transmit_good.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.bfd_no_reply is not None and self.bfd_no_reply.has_operation()) or
                                (self.transmit_bfd_good is not None and self.transmit_bfd_good.has_operation()) or
                                (self.transmit_drop is not None and self.transmit_drop.has_operation()) or
                                (self.transmit_good is not None and self.transmit_good.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "protect-req-sent" + path_buffer

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

                            if (child_yang_name == "bfd-no-reply"):
                                if (self.bfd_no_reply is None):
                                    self.bfd_no_reply = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.BfdNoReply()
                                    self.bfd_no_reply.parent = self
                                    self._children_name_map["bfd_no_reply"] = "bfd-no-reply"
                                return self.bfd_no_reply

                            if (child_yang_name == "transmit-bfd-good"):
                                if (self.transmit_bfd_good is None):
                                    self.transmit_bfd_good = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitBfdGood()
                                    self.transmit_bfd_good.parent = self
                                    self._children_name_map["transmit_bfd_good"] = "transmit-bfd-good"
                                return self.transmit_bfd_good

                            if (child_yang_name == "transmit-drop"):
                                if (self.transmit_drop is None):
                                    self.transmit_drop = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitDrop()
                                    self.transmit_drop.parent = self
                                    self._children_name_map["transmit_drop"] = "transmit-drop"
                                return self.transmit_drop

                            if (child_yang_name == "transmit-good"):
                                if (self.transmit_good is None):
                                    self.transmit_good = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitGood()
                                    self.transmit_good.parent = self
                                    self._children_name_map["transmit_good"] = "transmit-good"
                                return self.transmit_good

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "bfd-no-reply" or name == "transmit-bfd-good" or name == "transmit-drop" or name == "transmit-good"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class ProtectRepSent(Entity):
                        """
                        Protect Reply Packet transmit counts
                        
                        .. attribute:: bfd_no_reply
                        
                        	No Reply action for echo reqeust of BFD bootstrap
                        	**type**\:   :py:class:`BfdNoReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.BfdNoReply>`
                        
                        .. attribute:: transmit_bfd_good
                        
                        	Transmit good BFD request packets
                        	**type**\:   :py:class:`TransmitBfdGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitBfdGood>`
                        
                        .. attribute:: transmit_drop
                        
                        	Transmit drop packets
                        	**type**\:   :py:class:`TransmitDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitDrop>`
                        
                        .. attribute:: transmit_good
                        
                        	Transmit good packets
                        	**type**\:   :py:class:`TransmitGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitGood>`
                        
                        

                        """

                        _prefix = 'mpls-oam-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent, self).__init__()

                            self.yang_name = "protect-rep-sent"
                            self.yang_parent_name = "packet-statistics"

                            self.bfd_no_reply = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.BfdNoReply()
                            self.bfd_no_reply.parent = self
                            self._children_name_map["bfd_no_reply"] = "bfd-no-reply"
                            self._children_yang_names.add("bfd-no-reply")

                            self.transmit_bfd_good = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitBfdGood()
                            self.transmit_bfd_good.parent = self
                            self._children_name_map["transmit_bfd_good"] = "transmit-bfd-good"
                            self._children_yang_names.add("transmit-bfd-good")

                            self.transmit_drop = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitDrop()
                            self.transmit_drop.parent = self
                            self._children_name_map["transmit_drop"] = "transmit-drop"
                            self._children_yang_names.add("transmit-drop")

                            self.transmit_good = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitGood()
                            self.transmit_good.parent = self
                            self._children_name_map["transmit_good"] = "transmit-good"
                            self._children_yang_names.add("transmit-good")


                        class TransmitGood(Entity):
                            """
                            Transmit good packets
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitGood, self).__init__()

                                self.yang_name = "transmit-good"
                                self.yang_parent_name = "protect-rep-sent"

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("bytes",
                                                "packets") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitGood, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitGood, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.bytes.is_set or
                                    self.packets.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.bytes.yfilter != YFilter.not_set or
                                    self.packets.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "transmit-good" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bytes.get_name_leafdata())
                                if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.packets.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bytes" or name == "packets"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "bytes"):
                                    self.bytes = value
                                    self.bytes.value_namespace = name_space
                                    self.bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "packets"):
                                    self.packets = value
                                    self.packets.value_namespace = name_space
                                    self.packets.value_namespace_prefix = name_space_prefix


                        class TransmitDrop(Entity):
                            """
                            Transmit drop packets
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitDrop, self).__init__()

                                self.yang_name = "transmit-drop"
                                self.yang_parent_name = "protect-rep-sent"

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("bytes",
                                                "packets") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitDrop, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitDrop, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.bytes.is_set or
                                    self.packets.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.bytes.yfilter != YFilter.not_set or
                                    self.packets.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "transmit-drop" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bytes.get_name_leafdata())
                                if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.packets.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bytes" or name == "packets"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "bytes"):
                                    self.bytes = value
                                    self.bytes.value_namespace = name_space
                                    self.bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "packets"):
                                    self.packets = value
                                    self.packets.value_namespace = name_space
                                    self.packets.value_namespace_prefix = name_space_prefix


                        class TransmitBfdGood(Entity):
                            """
                            Transmit good BFD request packets
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitBfdGood, self).__init__()

                                self.yang_name = "transmit-bfd-good"
                                self.yang_parent_name = "protect-rep-sent"

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("bytes",
                                                "packets") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitBfdGood, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitBfdGood, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.bytes.is_set or
                                    self.packets.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.bytes.yfilter != YFilter.not_set or
                                    self.packets.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "transmit-bfd-good" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bytes.get_name_leafdata())
                                if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.packets.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bytes" or name == "packets"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "bytes"):
                                    self.bytes = value
                                    self.bytes.value_namespace = name_space
                                    self.bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "packets"):
                                    self.packets = value
                                    self.packets.value_namespace = name_space
                                    self.packets.value_namespace_prefix = name_space_prefix


                        class BfdNoReply(Entity):
                            """
                            No Reply action for echo reqeust of BFD
                            bootstrap
                            
                            .. attribute:: bytes
                            
                            	Byte counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: packets
                            
                            	Packet counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls-oam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.BfdNoReply, self).__init__()

                                self.yang_name = "bfd-no-reply"
                                self.yang_parent_name = "protect-rep-sent"

                                self.bytes = YLeaf(YType.uint64, "bytes")

                                self.packets = YLeaf(YType.uint64, "packets")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("bytes",
                                                "packets") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.BfdNoReply, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.BfdNoReply, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.bytes.is_set or
                                    self.packets.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.bytes.yfilter != YFilter.not_set or
                                    self.packets.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "bfd-no-reply" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bytes.get_name_leafdata())
                                if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.packets.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bytes" or name == "packets"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "bytes"):
                                    self.bytes = value
                                    self.bytes.value_namespace = name_space
                                    self.bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "packets"):
                                    self.packets = value
                                    self.packets.value_namespace = name_space
                                    self.packets.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                (self.bfd_no_reply is not None and self.bfd_no_reply.has_data()) or
                                (self.transmit_bfd_good is not None and self.transmit_bfd_good.has_data()) or
                                (self.transmit_drop is not None and self.transmit_drop.has_data()) or
                                (self.transmit_good is not None and self.transmit_good.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.bfd_no_reply is not None and self.bfd_no_reply.has_operation()) or
                                (self.transmit_bfd_good is not None and self.transmit_bfd_good.has_operation()) or
                                (self.transmit_drop is not None and self.transmit_drop.has_operation()) or
                                (self.transmit_good is not None and self.transmit_good.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "protect-rep-sent" + path_buffer

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

                            if (child_yang_name == "bfd-no-reply"):
                                if (self.bfd_no_reply is None):
                                    self.bfd_no_reply = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.BfdNoReply()
                                    self.bfd_no_reply.parent = self
                                    self._children_name_map["bfd_no_reply"] = "bfd-no-reply"
                                return self.bfd_no_reply

                            if (child_yang_name == "transmit-bfd-good"):
                                if (self.transmit_bfd_good is None):
                                    self.transmit_bfd_good = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitBfdGood()
                                    self.transmit_bfd_good.parent = self
                                    self._children_name_map["transmit_bfd_good"] = "transmit-bfd-good"
                                return self.transmit_bfd_good

                            if (child_yang_name == "transmit-drop"):
                                if (self.transmit_drop is None):
                                    self.transmit_drop = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitDrop()
                                    self.transmit_drop.parent = self
                                    self._children_name_map["transmit_drop"] = "transmit-drop"
                                return self.transmit_drop

                            if (child_yang_name == "transmit-good"):
                                if (self.transmit_good is None):
                                    self.transmit_good = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitGood()
                                    self.transmit_good.parent = self
                                    self._children_name_map["transmit_good"] = "transmit-good"
                                return self.transmit_good

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "bfd-no-reply" or name == "transmit-bfd-good" or name == "transmit-drop" or name == "transmit-good"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            (self.protect_rep_sent is not None and self.protect_rep_sent.has_data()) or
                            (self.protect_req_sent is not None and self.protect_req_sent.has_data()) or
                            (self.received is not None and self.received.has_data()) or
                            (self.sent is not None and self.sent.has_data()) or
                            (self.working_rep_sent is not None and self.working_rep_sent.has_data()) or
                            (self.working_req_sent is not None and self.working_req_sent.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.protect_rep_sent is not None and self.protect_rep_sent.has_operation()) or
                            (self.protect_req_sent is not None and self.protect_req_sent.has_operation()) or
                            (self.received is not None and self.received.has_operation()) or
                            (self.sent is not None and self.sent.has_operation()) or
                            (self.working_rep_sent is not None and self.working_rep_sent.has_operation()) or
                            (self.working_req_sent is not None and self.working_req_sent.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "packet-statistics" + path_buffer

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

                        if (child_yang_name == "protect-rep-sent"):
                            if (self.protect_rep_sent is None):
                                self.protect_rep_sent = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent()
                                self.protect_rep_sent.parent = self
                                self._children_name_map["protect_rep_sent"] = "protect-rep-sent"
                            return self.protect_rep_sent

                        if (child_yang_name == "protect-req-sent"):
                            if (self.protect_req_sent is None):
                                self.protect_req_sent = MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent()
                                self.protect_req_sent.parent = self
                                self._children_name_map["protect_req_sent"] = "protect-req-sent"
                            return self.protect_req_sent

                        if (child_yang_name == "received"):
                            if (self.received is None):
                                self.received = MplsOam.Interface.Details.Detail.PacketStatistics.Received()
                                self.received.parent = self
                                self._children_name_map["received"] = "received"
                            return self.received

                        if (child_yang_name == "sent"):
                            if (self.sent is None):
                                self.sent = MplsOam.Interface.Details.Detail.PacketStatistics.Sent()
                                self.sent.parent = self
                                self._children_name_map["sent"] = "sent"
                            return self.sent

                        if (child_yang_name == "working-rep-sent"):
                            if (self.working_rep_sent is None):
                                self.working_rep_sent = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent()
                                self.working_rep_sent.parent = self
                                self._children_name_map["working_rep_sent"] = "working-rep-sent"
                            return self.working_rep_sent

                        if (child_yang_name == "working-req-sent"):
                            if (self.working_req_sent is None):
                                self.working_req_sent = MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent()
                                self.working_req_sent.parent = self
                                self._children_name_map["working_req_sent"] = "working-req-sent"
                            return self.working_req_sent

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "protect-rep-sent" or name == "protect-req-sent" or name == "received" or name == "sent" or name == "working-rep-sent" or name == "working-req-sent"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.interface_name.is_set or
                        (self.interface_brief is not None and self.interface_brief.has_data()) or
                        (self.packet_statistics is not None and self.packet_statistics.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.interface_name.yfilter != YFilter.not_set or
                        (self.interface_brief is not None and self.interface_brief.has_operation()) or
                        (self.packet_statistics is not None and self.packet_statistics.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "detail" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/interface/details/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "interface-brief"):
                        if (self.interface_brief is None):
                            self.interface_brief = MplsOam.Interface.Details.Detail.InterfaceBrief()
                            self.interface_brief.parent = self
                            self._children_name_map["interface_brief"] = "interface-brief"
                        return self.interface_brief

                    if (child_yang_name == "packet-statistics"):
                        if (self.packet_statistics is None):
                            self.packet_statistics = MplsOam.Interface.Details.Detail.PacketStatistics()
                            self.packet_statistics.parent = self
                            self._children_name_map["packet_statistics"] = "packet-statistics"
                        return self.packet_statistics

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface-brief" or name == "packet-statistics" or name == "interface-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "interface-name"):
                        self.interface_name = value
                        self.interface_name.value_namespace = name_space
                        self.interface_name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.detail:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.detail:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "details" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/interface/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "detail"):
                    for c in self.detail:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = MplsOam.Interface.Details.Detail()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.detail.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "detail"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                (self.briefs is not None and self.briefs.has_data()) or
                (self.details is not None and self.details.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.briefs is not None and self.briefs.has_operation()) or
                (self.details is not None and self.details.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "interface" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "briefs"):
                if (self.briefs is None):
                    self.briefs = MplsOam.Interface.Briefs()
                    self.briefs.parent = self
                    self._children_name_map["briefs"] = "briefs"
                return self.briefs

            if (child_yang_name == "details"):
                if (self.details is None):
                    self.details = MplsOam.Interface.Details()
                    self.details.parent = self
                    self._children_name_map["details"] = "details"
                return self.details

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "briefs" or name == "details"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Packet(Entity):
        """
        LSPV packet counters operational data
        
        .. attribute:: protect_rep_sent
        
        	Protect Reply Packet transmit counts
        	**type**\:   :py:class:`ProtectRepSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.ProtectRepSent>`
        
        .. attribute:: protect_req_sent
        
        	Protect Request Packet transmit counts
        	**type**\:   :py:class:`ProtectReqSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.ProtectReqSent>`
        
        .. attribute:: received
        
        	Packet reception counts
        	**type**\:   :py:class:`Received <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received>`
        
        .. attribute:: sent
        
        	Packet transmit counts
        	**type**\:   :py:class:`Sent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Sent>`
        
        .. attribute:: working_rep_sent
        
        	Working Reply Packet transmit counts
        	**type**\:   :py:class:`WorkingRepSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.WorkingRepSent>`
        
        .. attribute:: working_req_sent
        
        	Working Request Packet transmit counts
        	**type**\:   :py:class:`WorkingReqSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.WorkingReqSent>`
        
        

        """

        _prefix = 'mpls-oam-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(MplsOam.Packet, self).__init__()

            self.yang_name = "packet"
            self.yang_parent_name = "mpls-oam"

            self.protect_rep_sent = MplsOam.Packet.ProtectRepSent()
            self.protect_rep_sent.parent = self
            self._children_name_map["protect_rep_sent"] = "protect-rep-sent"
            self._children_yang_names.add("protect-rep-sent")

            self.protect_req_sent = MplsOam.Packet.ProtectReqSent()
            self.protect_req_sent.parent = self
            self._children_name_map["protect_req_sent"] = "protect-req-sent"
            self._children_yang_names.add("protect-req-sent")

            self.received = MplsOam.Packet.Received()
            self.received.parent = self
            self._children_name_map["received"] = "received"
            self._children_yang_names.add("received")

            self.sent = MplsOam.Packet.Sent()
            self.sent.parent = self
            self._children_name_map["sent"] = "sent"
            self._children_yang_names.add("sent")

            self.working_rep_sent = MplsOam.Packet.WorkingRepSent()
            self.working_rep_sent.parent = self
            self._children_name_map["working_rep_sent"] = "working-rep-sent"
            self._children_yang_names.add("working-rep-sent")

            self.working_req_sent = MplsOam.Packet.WorkingReqSent()
            self.working_req_sent.parent = self
            self._children_name_map["working_req_sent"] = "working-req-sent"
            self._children_yang_names.add("working-req-sent")


        class Received(Entity):
            """
            Packet reception counts
            
            .. attribute:: protect_protocol_received_good_reply
            
            	Protect Protocol Received good reply
            	**type**\:   :py:class:`ProtectProtocolReceivedGoodReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ProtectProtocolReceivedGoodReply>`
            
            .. attribute:: protect_protocol_received_good_request
            
            	Protect Protocol Received good request
            	**type**\:   :py:class:`ProtectProtocolReceivedGoodRequest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ProtectProtocolReceivedGoodRequest>`
            
            .. attribute:: received_error_general
            
            	General error
            	**type**\:   :py:class:`ReceivedErrorGeneral <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedErrorGeneral>`
            
            .. attribute:: received_error_ip_header
            
            	IP header error
            	**type**\:   :py:class:`ReceivedErrorIpHeader <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedErrorIpHeader>`
            
            .. attribute:: received_error_no_interface
            
            	Error no Interfaces
            	**type**\:   :py:class:`ReceivedErrorNoInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedErrorNoInterface>`
            
            .. attribute:: received_error_no_memory
            
            	Error no memory
            	**type**\:   :py:class:`ReceivedErrorNoMemory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedErrorNoMemory>`
            
            .. attribute:: received_error_queue_full
            
            	Dropped queue full
            	**type**\:   :py:class:`ReceivedErrorQueueFull <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedErrorQueueFull>`
            
            .. attribute:: received_error_runt
            
            	RUNT error
            	**type**\:   :py:class:`ReceivedErrorRunt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedErrorRunt>`
            
            .. attribute:: received_error_udp_header
            
            	UDP header error
            	**type**\:   :py:class:`ReceivedErrorUdpHeader <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedErrorUdpHeader>`
            
            .. attribute:: received_good_bfd_reply
            
            	Received Reply with BFD TLV
            	**type**\:   :py:class:`ReceivedGoodBfdReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedGoodBfdReply>`
            
            .. attribute:: received_good_bfd_request
            
            	Received Reqeust with BFD TLV
            	**type**\:   :py:class:`ReceivedGoodBfdRequest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedGoodBfdRequest>`
            
            .. attribute:: received_good_reply
            
            	Received good reply
            	**type**\:   :py:class:`ReceivedGoodReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedGoodReply>`
            
            .. attribute:: received_good_request
            
            	Received good request
            	**type**\:   :py:class:`ReceivedGoodRequest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedGoodRequest>`
            
            .. attribute:: received_unknown
            
            	Received unknown packets
            	**type**\:   :py:class:`ReceivedUnknown <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Received.ReceivedUnknown>`
            
            

            """

            _prefix = 'mpls-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsOam.Packet.Received, self).__init__()

                self.yang_name = "received"
                self.yang_parent_name = "packet"

                self.protect_protocol_received_good_reply = MplsOam.Packet.Received.ProtectProtocolReceivedGoodReply()
                self.protect_protocol_received_good_reply.parent = self
                self._children_name_map["protect_protocol_received_good_reply"] = "protect-protocol-received-good-reply"
                self._children_yang_names.add("protect-protocol-received-good-reply")

                self.protect_protocol_received_good_request = MplsOam.Packet.Received.ProtectProtocolReceivedGoodRequest()
                self.protect_protocol_received_good_request.parent = self
                self._children_name_map["protect_protocol_received_good_request"] = "protect-protocol-received-good-request"
                self._children_yang_names.add("protect-protocol-received-good-request")

                self.received_error_general = MplsOam.Packet.Received.ReceivedErrorGeneral()
                self.received_error_general.parent = self
                self._children_name_map["received_error_general"] = "received-error-general"
                self._children_yang_names.add("received-error-general")

                self.received_error_ip_header = MplsOam.Packet.Received.ReceivedErrorIpHeader()
                self.received_error_ip_header.parent = self
                self._children_name_map["received_error_ip_header"] = "received-error-ip-header"
                self._children_yang_names.add("received-error-ip-header")

                self.received_error_no_interface = MplsOam.Packet.Received.ReceivedErrorNoInterface()
                self.received_error_no_interface.parent = self
                self._children_name_map["received_error_no_interface"] = "received-error-no-interface"
                self._children_yang_names.add("received-error-no-interface")

                self.received_error_no_memory = MplsOam.Packet.Received.ReceivedErrorNoMemory()
                self.received_error_no_memory.parent = self
                self._children_name_map["received_error_no_memory"] = "received-error-no-memory"
                self._children_yang_names.add("received-error-no-memory")

                self.received_error_queue_full = MplsOam.Packet.Received.ReceivedErrorQueueFull()
                self.received_error_queue_full.parent = self
                self._children_name_map["received_error_queue_full"] = "received-error-queue-full"
                self._children_yang_names.add("received-error-queue-full")

                self.received_error_runt = MplsOam.Packet.Received.ReceivedErrorRunt()
                self.received_error_runt.parent = self
                self._children_name_map["received_error_runt"] = "received-error-runt"
                self._children_yang_names.add("received-error-runt")

                self.received_error_udp_header = MplsOam.Packet.Received.ReceivedErrorUdpHeader()
                self.received_error_udp_header.parent = self
                self._children_name_map["received_error_udp_header"] = "received-error-udp-header"
                self._children_yang_names.add("received-error-udp-header")

                self.received_good_bfd_reply = MplsOam.Packet.Received.ReceivedGoodBfdReply()
                self.received_good_bfd_reply.parent = self
                self._children_name_map["received_good_bfd_reply"] = "received-good-bfd-reply"
                self._children_yang_names.add("received-good-bfd-reply")

                self.received_good_bfd_request = MplsOam.Packet.Received.ReceivedGoodBfdRequest()
                self.received_good_bfd_request.parent = self
                self._children_name_map["received_good_bfd_request"] = "received-good-bfd-request"
                self._children_yang_names.add("received-good-bfd-request")

                self.received_good_reply = MplsOam.Packet.Received.ReceivedGoodReply()
                self.received_good_reply.parent = self
                self._children_name_map["received_good_reply"] = "received-good-reply"
                self._children_yang_names.add("received-good-reply")

                self.received_good_request = MplsOam.Packet.Received.ReceivedGoodRequest()
                self.received_good_request.parent = self
                self._children_name_map["received_good_request"] = "received-good-request"
                self._children_yang_names.add("received-good-request")

                self.received_unknown = MplsOam.Packet.Received.ReceivedUnknown()
                self.received_unknown.parent = self
                self._children_name_map["received_unknown"] = "received-unknown"
                self._children_yang_names.add("received-unknown")


            class ReceivedGoodRequest(Entity):
                """
                Received good request
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.Received.ReceivedGoodRequest, self).__init__()

                    self.yang_name = "received-good-request"
                    self.yang_parent_name = "received"

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bytes",
                                    "packets") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsOam.Packet.Received.ReceivedGoodRequest, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsOam.Packet.Received.ReceivedGoodRequest, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.bytes.is_set or
                        self.packets.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bytes.yfilter != YFilter.not_set or
                        self.packets.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "received-good-request" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/received/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bytes.get_name_leafdata())
                    if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.packets.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bytes" or name == "packets"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bytes"):
                        self.bytes = value
                        self.bytes.value_namespace = name_space
                        self.bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "packets"):
                        self.packets = value
                        self.packets.value_namespace = name_space
                        self.packets.value_namespace_prefix = name_space_prefix


            class ReceivedGoodReply(Entity):
                """
                Received good reply
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.Received.ReceivedGoodReply, self).__init__()

                    self.yang_name = "received-good-reply"
                    self.yang_parent_name = "received"

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bytes",
                                    "packets") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsOam.Packet.Received.ReceivedGoodReply, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsOam.Packet.Received.ReceivedGoodReply, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.bytes.is_set or
                        self.packets.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bytes.yfilter != YFilter.not_set or
                        self.packets.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "received-good-reply" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/received/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bytes.get_name_leafdata())
                    if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.packets.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bytes" or name == "packets"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bytes"):
                        self.bytes = value
                        self.bytes.value_namespace = name_space
                        self.bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "packets"):
                        self.packets = value
                        self.packets.value_namespace = name_space
                        self.packets.value_namespace_prefix = name_space_prefix


            class ReceivedUnknown(Entity):
                """
                Received unknown packets
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.Received.ReceivedUnknown, self).__init__()

                    self.yang_name = "received-unknown"
                    self.yang_parent_name = "received"

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bytes",
                                    "packets") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsOam.Packet.Received.ReceivedUnknown, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsOam.Packet.Received.ReceivedUnknown, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.bytes.is_set or
                        self.packets.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bytes.yfilter != YFilter.not_set or
                        self.packets.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "received-unknown" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/received/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bytes.get_name_leafdata())
                    if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.packets.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bytes" or name == "packets"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bytes"):
                        self.bytes = value
                        self.bytes.value_namespace = name_space
                        self.bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "packets"):
                        self.packets = value
                        self.packets.value_namespace = name_space
                        self.packets.value_namespace_prefix = name_space_prefix


            class ReceivedErrorIpHeader(Entity):
                """
                IP header error
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.Received.ReceivedErrorIpHeader, self).__init__()

                    self.yang_name = "received-error-ip-header"
                    self.yang_parent_name = "received"

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bytes",
                                    "packets") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsOam.Packet.Received.ReceivedErrorIpHeader, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsOam.Packet.Received.ReceivedErrorIpHeader, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.bytes.is_set or
                        self.packets.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bytes.yfilter != YFilter.not_set or
                        self.packets.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "received-error-ip-header" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/received/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bytes.get_name_leafdata())
                    if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.packets.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bytes" or name == "packets"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bytes"):
                        self.bytes = value
                        self.bytes.value_namespace = name_space
                        self.bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "packets"):
                        self.packets = value
                        self.packets.value_namespace = name_space
                        self.packets.value_namespace_prefix = name_space_prefix


            class ReceivedErrorUdpHeader(Entity):
                """
                UDP header error
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.Received.ReceivedErrorUdpHeader, self).__init__()

                    self.yang_name = "received-error-udp-header"
                    self.yang_parent_name = "received"

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bytes",
                                    "packets") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsOam.Packet.Received.ReceivedErrorUdpHeader, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsOam.Packet.Received.ReceivedErrorUdpHeader, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.bytes.is_set or
                        self.packets.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bytes.yfilter != YFilter.not_set or
                        self.packets.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "received-error-udp-header" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/received/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bytes.get_name_leafdata())
                    if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.packets.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bytes" or name == "packets"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bytes"):
                        self.bytes = value
                        self.bytes.value_namespace = name_space
                        self.bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "packets"):
                        self.packets = value
                        self.packets.value_namespace = name_space
                        self.packets.value_namespace_prefix = name_space_prefix


            class ReceivedErrorRunt(Entity):
                """
                RUNT error
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.Received.ReceivedErrorRunt, self).__init__()

                    self.yang_name = "received-error-runt"
                    self.yang_parent_name = "received"

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bytes",
                                    "packets") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsOam.Packet.Received.ReceivedErrorRunt, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsOam.Packet.Received.ReceivedErrorRunt, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.bytes.is_set or
                        self.packets.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bytes.yfilter != YFilter.not_set or
                        self.packets.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "received-error-runt" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/received/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bytes.get_name_leafdata())
                    if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.packets.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bytes" or name == "packets"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bytes"):
                        self.bytes = value
                        self.bytes.value_namespace = name_space
                        self.bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "packets"):
                        self.packets = value
                        self.packets.value_namespace = name_space
                        self.packets.value_namespace_prefix = name_space_prefix


            class ReceivedErrorQueueFull(Entity):
                """
                Dropped queue full
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.Received.ReceivedErrorQueueFull, self).__init__()

                    self.yang_name = "received-error-queue-full"
                    self.yang_parent_name = "received"

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bytes",
                                    "packets") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsOam.Packet.Received.ReceivedErrorQueueFull, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsOam.Packet.Received.ReceivedErrorQueueFull, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.bytes.is_set or
                        self.packets.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bytes.yfilter != YFilter.not_set or
                        self.packets.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "received-error-queue-full" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/received/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bytes.get_name_leafdata())
                    if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.packets.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bytes" or name == "packets"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bytes"):
                        self.bytes = value
                        self.bytes.value_namespace = name_space
                        self.bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "packets"):
                        self.packets = value
                        self.packets.value_namespace = name_space
                        self.packets.value_namespace_prefix = name_space_prefix


            class ReceivedErrorGeneral(Entity):
                """
                General error
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.Received.ReceivedErrorGeneral, self).__init__()

                    self.yang_name = "received-error-general"
                    self.yang_parent_name = "received"

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bytes",
                                    "packets") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsOam.Packet.Received.ReceivedErrorGeneral, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsOam.Packet.Received.ReceivedErrorGeneral, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.bytes.is_set or
                        self.packets.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bytes.yfilter != YFilter.not_set or
                        self.packets.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "received-error-general" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/received/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bytes.get_name_leafdata())
                    if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.packets.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bytes" or name == "packets"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bytes"):
                        self.bytes = value
                        self.bytes.value_namespace = name_space
                        self.bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "packets"):
                        self.packets = value
                        self.packets.value_namespace = name_space
                        self.packets.value_namespace_prefix = name_space_prefix


            class ReceivedErrorNoInterface(Entity):
                """
                Error no Interfaces
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.Received.ReceivedErrorNoInterface, self).__init__()

                    self.yang_name = "received-error-no-interface"
                    self.yang_parent_name = "received"

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bytes",
                                    "packets") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsOam.Packet.Received.ReceivedErrorNoInterface, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsOam.Packet.Received.ReceivedErrorNoInterface, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.bytes.is_set or
                        self.packets.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bytes.yfilter != YFilter.not_set or
                        self.packets.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "received-error-no-interface" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/received/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bytes.get_name_leafdata())
                    if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.packets.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bytes" or name == "packets"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bytes"):
                        self.bytes = value
                        self.bytes.value_namespace = name_space
                        self.bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "packets"):
                        self.packets = value
                        self.packets.value_namespace = name_space
                        self.packets.value_namespace_prefix = name_space_prefix


            class ReceivedErrorNoMemory(Entity):
                """
                Error no memory
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.Received.ReceivedErrorNoMemory, self).__init__()

                    self.yang_name = "received-error-no-memory"
                    self.yang_parent_name = "received"

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bytes",
                                    "packets") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsOam.Packet.Received.ReceivedErrorNoMemory, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsOam.Packet.Received.ReceivedErrorNoMemory, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.bytes.is_set or
                        self.packets.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bytes.yfilter != YFilter.not_set or
                        self.packets.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "received-error-no-memory" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/received/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bytes.get_name_leafdata())
                    if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.packets.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bytes" or name == "packets"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bytes"):
                        self.bytes = value
                        self.bytes.value_namespace = name_space
                        self.bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "packets"):
                        self.packets = value
                        self.packets.value_namespace = name_space
                        self.packets.value_namespace_prefix = name_space_prefix


            class ProtectProtocolReceivedGoodRequest(Entity):
                """
                Protect Protocol Received good request
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.Received.ProtectProtocolReceivedGoodRequest, self).__init__()

                    self.yang_name = "protect-protocol-received-good-request"
                    self.yang_parent_name = "received"

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bytes",
                                    "packets") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsOam.Packet.Received.ProtectProtocolReceivedGoodRequest, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsOam.Packet.Received.ProtectProtocolReceivedGoodRequest, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.bytes.is_set or
                        self.packets.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bytes.yfilter != YFilter.not_set or
                        self.packets.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "protect-protocol-received-good-request" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/received/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bytes.get_name_leafdata())
                    if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.packets.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bytes" or name == "packets"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bytes"):
                        self.bytes = value
                        self.bytes.value_namespace = name_space
                        self.bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "packets"):
                        self.packets = value
                        self.packets.value_namespace = name_space
                        self.packets.value_namespace_prefix = name_space_prefix


            class ProtectProtocolReceivedGoodReply(Entity):
                """
                Protect Protocol Received good reply
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.Received.ProtectProtocolReceivedGoodReply, self).__init__()

                    self.yang_name = "protect-protocol-received-good-reply"
                    self.yang_parent_name = "received"

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bytes",
                                    "packets") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsOam.Packet.Received.ProtectProtocolReceivedGoodReply, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsOam.Packet.Received.ProtectProtocolReceivedGoodReply, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.bytes.is_set or
                        self.packets.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bytes.yfilter != YFilter.not_set or
                        self.packets.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "protect-protocol-received-good-reply" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/received/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bytes.get_name_leafdata())
                    if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.packets.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bytes" or name == "packets"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bytes"):
                        self.bytes = value
                        self.bytes.value_namespace = name_space
                        self.bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "packets"):
                        self.packets = value
                        self.packets.value_namespace = name_space
                        self.packets.value_namespace_prefix = name_space_prefix


            class ReceivedGoodBfdRequest(Entity):
                """
                Received Reqeust with BFD TLV
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.Received.ReceivedGoodBfdRequest, self).__init__()

                    self.yang_name = "received-good-bfd-request"
                    self.yang_parent_name = "received"

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bytes",
                                    "packets") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsOam.Packet.Received.ReceivedGoodBfdRequest, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsOam.Packet.Received.ReceivedGoodBfdRequest, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.bytes.is_set or
                        self.packets.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bytes.yfilter != YFilter.not_set or
                        self.packets.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "received-good-bfd-request" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/received/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bytes.get_name_leafdata())
                    if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.packets.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bytes" or name == "packets"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bytes"):
                        self.bytes = value
                        self.bytes.value_namespace = name_space
                        self.bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "packets"):
                        self.packets = value
                        self.packets.value_namespace = name_space
                        self.packets.value_namespace_prefix = name_space_prefix


            class ReceivedGoodBfdReply(Entity):
                """
                Received Reply with BFD TLV
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.Received.ReceivedGoodBfdReply, self).__init__()

                    self.yang_name = "received-good-bfd-reply"
                    self.yang_parent_name = "received"

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bytes",
                                    "packets") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsOam.Packet.Received.ReceivedGoodBfdReply, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsOam.Packet.Received.ReceivedGoodBfdReply, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.bytes.is_set or
                        self.packets.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bytes.yfilter != YFilter.not_set or
                        self.packets.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "received-good-bfd-reply" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/received/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bytes.get_name_leafdata())
                    if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.packets.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bytes" or name == "packets"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bytes"):
                        self.bytes = value
                        self.bytes.value_namespace = name_space
                        self.bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "packets"):
                        self.packets = value
                        self.packets.value_namespace = name_space
                        self.packets.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    (self.protect_protocol_received_good_reply is not None and self.protect_protocol_received_good_reply.has_data()) or
                    (self.protect_protocol_received_good_request is not None and self.protect_protocol_received_good_request.has_data()) or
                    (self.received_error_general is not None and self.received_error_general.has_data()) or
                    (self.received_error_ip_header is not None and self.received_error_ip_header.has_data()) or
                    (self.received_error_no_interface is not None and self.received_error_no_interface.has_data()) or
                    (self.received_error_no_memory is not None and self.received_error_no_memory.has_data()) or
                    (self.received_error_queue_full is not None and self.received_error_queue_full.has_data()) or
                    (self.received_error_runt is not None and self.received_error_runt.has_data()) or
                    (self.received_error_udp_header is not None and self.received_error_udp_header.has_data()) or
                    (self.received_good_bfd_reply is not None and self.received_good_bfd_reply.has_data()) or
                    (self.received_good_bfd_request is not None and self.received_good_bfd_request.has_data()) or
                    (self.received_good_reply is not None and self.received_good_reply.has_data()) or
                    (self.received_good_request is not None and self.received_good_request.has_data()) or
                    (self.received_unknown is not None and self.received_unknown.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.protect_protocol_received_good_reply is not None and self.protect_protocol_received_good_reply.has_operation()) or
                    (self.protect_protocol_received_good_request is not None and self.protect_protocol_received_good_request.has_operation()) or
                    (self.received_error_general is not None and self.received_error_general.has_operation()) or
                    (self.received_error_ip_header is not None and self.received_error_ip_header.has_operation()) or
                    (self.received_error_no_interface is not None and self.received_error_no_interface.has_operation()) or
                    (self.received_error_no_memory is not None and self.received_error_no_memory.has_operation()) or
                    (self.received_error_queue_full is not None and self.received_error_queue_full.has_operation()) or
                    (self.received_error_runt is not None and self.received_error_runt.has_operation()) or
                    (self.received_error_udp_header is not None and self.received_error_udp_header.has_operation()) or
                    (self.received_good_bfd_reply is not None and self.received_good_bfd_reply.has_operation()) or
                    (self.received_good_bfd_request is not None and self.received_good_bfd_request.has_operation()) or
                    (self.received_good_reply is not None and self.received_good_reply.has_operation()) or
                    (self.received_good_request is not None and self.received_good_request.has_operation()) or
                    (self.received_unknown is not None and self.received_unknown.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "received" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "protect-protocol-received-good-reply"):
                    if (self.protect_protocol_received_good_reply is None):
                        self.protect_protocol_received_good_reply = MplsOam.Packet.Received.ProtectProtocolReceivedGoodReply()
                        self.protect_protocol_received_good_reply.parent = self
                        self._children_name_map["protect_protocol_received_good_reply"] = "protect-protocol-received-good-reply"
                    return self.protect_protocol_received_good_reply

                if (child_yang_name == "protect-protocol-received-good-request"):
                    if (self.protect_protocol_received_good_request is None):
                        self.protect_protocol_received_good_request = MplsOam.Packet.Received.ProtectProtocolReceivedGoodRequest()
                        self.protect_protocol_received_good_request.parent = self
                        self._children_name_map["protect_protocol_received_good_request"] = "protect-protocol-received-good-request"
                    return self.protect_protocol_received_good_request

                if (child_yang_name == "received-error-general"):
                    if (self.received_error_general is None):
                        self.received_error_general = MplsOam.Packet.Received.ReceivedErrorGeneral()
                        self.received_error_general.parent = self
                        self._children_name_map["received_error_general"] = "received-error-general"
                    return self.received_error_general

                if (child_yang_name == "received-error-ip-header"):
                    if (self.received_error_ip_header is None):
                        self.received_error_ip_header = MplsOam.Packet.Received.ReceivedErrorIpHeader()
                        self.received_error_ip_header.parent = self
                        self._children_name_map["received_error_ip_header"] = "received-error-ip-header"
                    return self.received_error_ip_header

                if (child_yang_name == "received-error-no-interface"):
                    if (self.received_error_no_interface is None):
                        self.received_error_no_interface = MplsOam.Packet.Received.ReceivedErrorNoInterface()
                        self.received_error_no_interface.parent = self
                        self._children_name_map["received_error_no_interface"] = "received-error-no-interface"
                    return self.received_error_no_interface

                if (child_yang_name == "received-error-no-memory"):
                    if (self.received_error_no_memory is None):
                        self.received_error_no_memory = MplsOam.Packet.Received.ReceivedErrorNoMemory()
                        self.received_error_no_memory.parent = self
                        self._children_name_map["received_error_no_memory"] = "received-error-no-memory"
                    return self.received_error_no_memory

                if (child_yang_name == "received-error-queue-full"):
                    if (self.received_error_queue_full is None):
                        self.received_error_queue_full = MplsOam.Packet.Received.ReceivedErrorQueueFull()
                        self.received_error_queue_full.parent = self
                        self._children_name_map["received_error_queue_full"] = "received-error-queue-full"
                    return self.received_error_queue_full

                if (child_yang_name == "received-error-runt"):
                    if (self.received_error_runt is None):
                        self.received_error_runt = MplsOam.Packet.Received.ReceivedErrorRunt()
                        self.received_error_runt.parent = self
                        self._children_name_map["received_error_runt"] = "received-error-runt"
                    return self.received_error_runt

                if (child_yang_name == "received-error-udp-header"):
                    if (self.received_error_udp_header is None):
                        self.received_error_udp_header = MplsOam.Packet.Received.ReceivedErrorUdpHeader()
                        self.received_error_udp_header.parent = self
                        self._children_name_map["received_error_udp_header"] = "received-error-udp-header"
                    return self.received_error_udp_header

                if (child_yang_name == "received-good-bfd-reply"):
                    if (self.received_good_bfd_reply is None):
                        self.received_good_bfd_reply = MplsOam.Packet.Received.ReceivedGoodBfdReply()
                        self.received_good_bfd_reply.parent = self
                        self._children_name_map["received_good_bfd_reply"] = "received-good-bfd-reply"
                    return self.received_good_bfd_reply

                if (child_yang_name == "received-good-bfd-request"):
                    if (self.received_good_bfd_request is None):
                        self.received_good_bfd_request = MplsOam.Packet.Received.ReceivedGoodBfdRequest()
                        self.received_good_bfd_request.parent = self
                        self._children_name_map["received_good_bfd_request"] = "received-good-bfd-request"
                    return self.received_good_bfd_request

                if (child_yang_name == "received-good-reply"):
                    if (self.received_good_reply is None):
                        self.received_good_reply = MplsOam.Packet.Received.ReceivedGoodReply()
                        self.received_good_reply.parent = self
                        self._children_name_map["received_good_reply"] = "received-good-reply"
                    return self.received_good_reply

                if (child_yang_name == "received-good-request"):
                    if (self.received_good_request is None):
                        self.received_good_request = MplsOam.Packet.Received.ReceivedGoodRequest()
                        self.received_good_request.parent = self
                        self._children_name_map["received_good_request"] = "received-good-request"
                    return self.received_good_request

                if (child_yang_name == "received-unknown"):
                    if (self.received_unknown is None):
                        self.received_unknown = MplsOam.Packet.Received.ReceivedUnknown()
                        self.received_unknown.parent = self
                        self._children_name_map["received_unknown"] = "received-unknown"
                    return self.received_unknown

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "protect-protocol-received-good-reply" or name == "protect-protocol-received-good-request" or name == "received-error-general" or name == "received-error-ip-header" or name == "received-error-no-interface" or name == "received-error-no-memory" or name == "received-error-queue-full" or name == "received-error-runt" or name == "received-error-udp-header" or name == "received-good-bfd-reply" or name == "received-good-bfd-request" or name == "received-good-reply" or name == "received-good-request" or name == "received-unknown"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Sent(Entity):
            """
            Packet transmit counts
            
            .. attribute:: bfd_no_reply
            
            	No Reply action for echo reqeust of BFD bootstrap
            	**type**\:   :py:class:`BfdNoReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Sent.BfdNoReply>`
            
            .. attribute:: transmit_bfd_good
            
            	Transmit good BFD request packets
            	**type**\:   :py:class:`TransmitBfdGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Sent.TransmitBfdGood>`
            
            .. attribute:: transmit_drop
            
            	Transmit drop packets
            	**type**\:   :py:class:`TransmitDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Sent.TransmitDrop>`
            
            .. attribute:: transmit_good
            
            	Transmit good packets
            	**type**\:   :py:class:`TransmitGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.Sent.TransmitGood>`
            
            

            """

            _prefix = 'mpls-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsOam.Packet.Sent, self).__init__()

                self.yang_name = "sent"
                self.yang_parent_name = "packet"

                self.bfd_no_reply = MplsOam.Packet.Sent.BfdNoReply()
                self.bfd_no_reply.parent = self
                self._children_name_map["bfd_no_reply"] = "bfd-no-reply"
                self._children_yang_names.add("bfd-no-reply")

                self.transmit_bfd_good = MplsOam.Packet.Sent.TransmitBfdGood()
                self.transmit_bfd_good.parent = self
                self._children_name_map["transmit_bfd_good"] = "transmit-bfd-good"
                self._children_yang_names.add("transmit-bfd-good")

                self.transmit_drop = MplsOam.Packet.Sent.TransmitDrop()
                self.transmit_drop.parent = self
                self._children_name_map["transmit_drop"] = "transmit-drop"
                self._children_yang_names.add("transmit-drop")

                self.transmit_good = MplsOam.Packet.Sent.TransmitGood()
                self.transmit_good.parent = self
                self._children_name_map["transmit_good"] = "transmit-good"
                self._children_yang_names.add("transmit-good")


            class TransmitGood(Entity):
                """
                Transmit good packets
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.Sent.TransmitGood, self).__init__()

                    self.yang_name = "transmit-good"
                    self.yang_parent_name = "sent"

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bytes",
                                    "packets") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsOam.Packet.Sent.TransmitGood, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsOam.Packet.Sent.TransmitGood, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.bytes.is_set or
                        self.packets.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bytes.yfilter != YFilter.not_set or
                        self.packets.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "transmit-good" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/sent/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bytes.get_name_leafdata())
                    if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.packets.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bytes" or name == "packets"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bytes"):
                        self.bytes = value
                        self.bytes.value_namespace = name_space
                        self.bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "packets"):
                        self.packets = value
                        self.packets.value_namespace = name_space
                        self.packets.value_namespace_prefix = name_space_prefix


            class TransmitDrop(Entity):
                """
                Transmit drop packets
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.Sent.TransmitDrop, self).__init__()

                    self.yang_name = "transmit-drop"
                    self.yang_parent_name = "sent"

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bytes",
                                    "packets") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsOam.Packet.Sent.TransmitDrop, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsOam.Packet.Sent.TransmitDrop, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.bytes.is_set or
                        self.packets.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bytes.yfilter != YFilter.not_set or
                        self.packets.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "transmit-drop" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/sent/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bytes.get_name_leafdata())
                    if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.packets.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bytes" or name == "packets"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bytes"):
                        self.bytes = value
                        self.bytes.value_namespace = name_space
                        self.bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "packets"):
                        self.packets = value
                        self.packets.value_namespace = name_space
                        self.packets.value_namespace_prefix = name_space_prefix


            class TransmitBfdGood(Entity):
                """
                Transmit good BFD request packets
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.Sent.TransmitBfdGood, self).__init__()

                    self.yang_name = "transmit-bfd-good"
                    self.yang_parent_name = "sent"

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bytes",
                                    "packets") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsOam.Packet.Sent.TransmitBfdGood, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsOam.Packet.Sent.TransmitBfdGood, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.bytes.is_set or
                        self.packets.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bytes.yfilter != YFilter.not_set or
                        self.packets.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "transmit-bfd-good" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/sent/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bytes.get_name_leafdata())
                    if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.packets.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bytes" or name == "packets"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bytes"):
                        self.bytes = value
                        self.bytes.value_namespace = name_space
                        self.bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "packets"):
                        self.packets = value
                        self.packets.value_namespace = name_space
                        self.packets.value_namespace_prefix = name_space_prefix


            class BfdNoReply(Entity):
                """
                No Reply action for echo reqeust of BFD
                bootstrap
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.Sent.BfdNoReply, self).__init__()

                    self.yang_name = "bfd-no-reply"
                    self.yang_parent_name = "sent"

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bytes",
                                    "packets") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsOam.Packet.Sent.BfdNoReply, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsOam.Packet.Sent.BfdNoReply, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.bytes.is_set or
                        self.packets.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bytes.yfilter != YFilter.not_set or
                        self.packets.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "bfd-no-reply" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/sent/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bytes.get_name_leafdata())
                    if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.packets.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bytes" or name == "packets"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bytes"):
                        self.bytes = value
                        self.bytes.value_namespace = name_space
                        self.bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "packets"):
                        self.packets = value
                        self.packets.value_namespace = name_space
                        self.packets.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    (self.bfd_no_reply is not None and self.bfd_no_reply.has_data()) or
                    (self.transmit_bfd_good is not None and self.transmit_bfd_good.has_data()) or
                    (self.transmit_drop is not None and self.transmit_drop.has_data()) or
                    (self.transmit_good is not None and self.transmit_good.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.bfd_no_reply is not None and self.bfd_no_reply.has_operation()) or
                    (self.transmit_bfd_good is not None and self.transmit_bfd_good.has_operation()) or
                    (self.transmit_drop is not None and self.transmit_drop.has_operation()) or
                    (self.transmit_good is not None and self.transmit_good.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "sent" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "bfd-no-reply"):
                    if (self.bfd_no_reply is None):
                        self.bfd_no_reply = MplsOam.Packet.Sent.BfdNoReply()
                        self.bfd_no_reply.parent = self
                        self._children_name_map["bfd_no_reply"] = "bfd-no-reply"
                    return self.bfd_no_reply

                if (child_yang_name == "transmit-bfd-good"):
                    if (self.transmit_bfd_good is None):
                        self.transmit_bfd_good = MplsOam.Packet.Sent.TransmitBfdGood()
                        self.transmit_bfd_good.parent = self
                        self._children_name_map["transmit_bfd_good"] = "transmit-bfd-good"
                    return self.transmit_bfd_good

                if (child_yang_name == "transmit-drop"):
                    if (self.transmit_drop is None):
                        self.transmit_drop = MplsOam.Packet.Sent.TransmitDrop()
                        self.transmit_drop.parent = self
                        self._children_name_map["transmit_drop"] = "transmit-drop"
                    return self.transmit_drop

                if (child_yang_name == "transmit-good"):
                    if (self.transmit_good is None):
                        self.transmit_good = MplsOam.Packet.Sent.TransmitGood()
                        self.transmit_good.parent = self
                        self._children_name_map["transmit_good"] = "transmit-good"
                    return self.transmit_good

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "bfd-no-reply" or name == "transmit-bfd-good" or name == "transmit-drop" or name == "transmit-good"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class WorkingReqSent(Entity):
            """
            Working Request Packet transmit counts
            
            .. attribute:: bfd_no_reply
            
            	No Reply action for echo reqeust of BFD bootstrap
            	**type**\:   :py:class:`BfdNoReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.WorkingReqSent.BfdNoReply>`
            
            .. attribute:: transmit_bfd_good
            
            	Transmit good BFD request packets
            	**type**\:   :py:class:`TransmitBfdGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.WorkingReqSent.TransmitBfdGood>`
            
            .. attribute:: transmit_drop
            
            	Transmit drop packets
            	**type**\:   :py:class:`TransmitDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.WorkingReqSent.TransmitDrop>`
            
            .. attribute:: transmit_good
            
            	Transmit good packets
            	**type**\:   :py:class:`TransmitGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.WorkingReqSent.TransmitGood>`
            
            

            """

            _prefix = 'mpls-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsOam.Packet.WorkingReqSent, self).__init__()

                self.yang_name = "working-req-sent"
                self.yang_parent_name = "packet"

                self.bfd_no_reply = MplsOam.Packet.WorkingReqSent.BfdNoReply()
                self.bfd_no_reply.parent = self
                self._children_name_map["bfd_no_reply"] = "bfd-no-reply"
                self._children_yang_names.add("bfd-no-reply")

                self.transmit_bfd_good = MplsOam.Packet.WorkingReqSent.TransmitBfdGood()
                self.transmit_bfd_good.parent = self
                self._children_name_map["transmit_bfd_good"] = "transmit-bfd-good"
                self._children_yang_names.add("transmit-bfd-good")

                self.transmit_drop = MplsOam.Packet.WorkingReqSent.TransmitDrop()
                self.transmit_drop.parent = self
                self._children_name_map["transmit_drop"] = "transmit-drop"
                self._children_yang_names.add("transmit-drop")

                self.transmit_good = MplsOam.Packet.WorkingReqSent.TransmitGood()
                self.transmit_good.parent = self
                self._children_name_map["transmit_good"] = "transmit-good"
                self._children_yang_names.add("transmit-good")


            class TransmitGood(Entity):
                """
                Transmit good packets
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.WorkingReqSent.TransmitGood, self).__init__()

                    self.yang_name = "transmit-good"
                    self.yang_parent_name = "working-req-sent"

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bytes",
                                    "packets") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsOam.Packet.WorkingReqSent.TransmitGood, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsOam.Packet.WorkingReqSent.TransmitGood, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.bytes.is_set or
                        self.packets.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bytes.yfilter != YFilter.not_set or
                        self.packets.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "transmit-good" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/working-req-sent/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bytes.get_name_leafdata())
                    if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.packets.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bytes" or name == "packets"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bytes"):
                        self.bytes = value
                        self.bytes.value_namespace = name_space
                        self.bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "packets"):
                        self.packets = value
                        self.packets.value_namespace = name_space
                        self.packets.value_namespace_prefix = name_space_prefix


            class TransmitDrop(Entity):
                """
                Transmit drop packets
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.WorkingReqSent.TransmitDrop, self).__init__()

                    self.yang_name = "transmit-drop"
                    self.yang_parent_name = "working-req-sent"

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bytes",
                                    "packets") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsOam.Packet.WorkingReqSent.TransmitDrop, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsOam.Packet.WorkingReqSent.TransmitDrop, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.bytes.is_set or
                        self.packets.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bytes.yfilter != YFilter.not_set or
                        self.packets.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "transmit-drop" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/working-req-sent/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bytes.get_name_leafdata())
                    if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.packets.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bytes" or name == "packets"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bytes"):
                        self.bytes = value
                        self.bytes.value_namespace = name_space
                        self.bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "packets"):
                        self.packets = value
                        self.packets.value_namespace = name_space
                        self.packets.value_namespace_prefix = name_space_prefix


            class TransmitBfdGood(Entity):
                """
                Transmit good BFD request packets
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.WorkingReqSent.TransmitBfdGood, self).__init__()

                    self.yang_name = "transmit-bfd-good"
                    self.yang_parent_name = "working-req-sent"

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bytes",
                                    "packets") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsOam.Packet.WorkingReqSent.TransmitBfdGood, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsOam.Packet.WorkingReqSent.TransmitBfdGood, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.bytes.is_set or
                        self.packets.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bytes.yfilter != YFilter.not_set or
                        self.packets.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "transmit-bfd-good" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/working-req-sent/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bytes.get_name_leafdata())
                    if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.packets.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bytes" or name == "packets"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bytes"):
                        self.bytes = value
                        self.bytes.value_namespace = name_space
                        self.bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "packets"):
                        self.packets = value
                        self.packets.value_namespace = name_space
                        self.packets.value_namespace_prefix = name_space_prefix


            class BfdNoReply(Entity):
                """
                No Reply action for echo reqeust of BFD
                bootstrap
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.WorkingReqSent.BfdNoReply, self).__init__()

                    self.yang_name = "bfd-no-reply"
                    self.yang_parent_name = "working-req-sent"

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bytes",
                                    "packets") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsOam.Packet.WorkingReqSent.BfdNoReply, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsOam.Packet.WorkingReqSent.BfdNoReply, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.bytes.is_set or
                        self.packets.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bytes.yfilter != YFilter.not_set or
                        self.packets.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "bfd-no-reply" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/working-req-sent/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bytes.get_name_leafdata())
                    if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.packets.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bytes" or name == "packets"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bytes"):
                        self.bytes = value
                        self.bytes.value_namespace = name_space
                        self.bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "packets"):
                        self.packets = value
                        self.packets.value_namespace = name_space
                        self.packets.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    (self.bfd_no_reply is not None and self.bfd_no_reply.has_data()) or
                    (self.transmit_bfd_good is not None and self.transmit_bfd_good.has_data()) or
                    (self.transmit_drop is not None and self.transmit_drop.has_data()) or
                    (self.transmit_good is not None and self.transmit_good.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.bfd_no_reply is not None and self.bfd_no_reply.has_operation()) or
                    (self.transmit_bfd_good is not None and self.transmit_bfd_good.has_operation()) or
                    (self.transmit_drop is not None and self.transmit_drop.has_operation()) or
                    (self.transmit_good is not None and self.transmit_good.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "working-req-sent" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "bfd-no-reply"):
                    if (self.bfd_no_reply is None):
                        self.bfd_no_reply = MplsOam.Packet.WorkingReqSent.BfdNoReply()
                        self.bfd_no_reply.parent = self
                        self._children_name_map["bfd_no_reply"] = "bfd-no-reply"
                    return self.bfd_no_reply

                if (child_yang_name == "transmit-bfd-good"):
                    if (self.transmit_bfd_good is None):
                        self.transmit_bfd_good = MplsOam.Packet.WorkingReqSent.TransmitBfdGood()
                        self.transmit_bfd_good.parent = self
                        self._children_name_map["transmit_bfd_good"] = "transmit-bfd-good"
                    return self.transmit_bfd_good

                if (child_yang_name == "transmit-drop"):
                    if (self.transmit_drop is None):
                        self.transmit_drop = MplsOam.Packet.WorkingReqSent.TransmitDrop()
                        self.transmit_drop.parent = self
                        self._children_name_map["transmit_drop"] = "transmit-drop"
                    return self.transmit_drop

                if (child_yang_name == "transmit-good"):
                    if (self.transmit_good is None):
                        self.transmit_good = MplsOam.Packet.WorkingReqSent.TransmitGood()
                        self.transmit_good.parent = self
                        self._children_name_map["transmit_good"] = "transmit-good"
                    return self.transmit_good

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "bfd-no-reply" or name == "transmit-bfd-good" or name == "transmit-drop" or name == "transmit-good"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class WorkingRepSent(Entity):
            """
            Working Reply Packet transmit counts
            
            .. attribute:: bfd_no_reply
            
            	No Reply action for echo reqeust of BFD bootstrap
            	**type**\:   :py:class:`BfdNoReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.WorkingRepSent.BfdNoReply>`
            
            .. attribute:: transmit_bfd_good
            
            	Transmit good BFD request packets
            	**type**\:   :py:class:`TransmitBfdGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.WorkingRepSent.TransmitBfdGood>`
            
            .. attribute:: transmit_drop
            
            	Transmit drop packets
            	**type**\:   :py:class:`TransmitDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.WorkingRepSent.TransmitDrop>`
            
            .. attribute:: transmit_good
            
            	Transmit good packets
            	**type**\:   :py:class:`TransmitGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.WorkingRepSent.TransmitGood>`
            
            

            """

            _prefix = 'mpls-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsOam.Packet.WorkingRepSent, self).__init__()

                self.yang_name = "working-rep-sent"
                self.yang_parent_name = "packet"

                self.bfd_no_reply = MplsOam.Packet.WorkingRepSent.BfdNoReply()
                self.bfd_no_reply.parent = self
                self._children_name_map["bfd_no_reply"] = "bfd-no-reply"
                self._children_yang_names.add("bfd-no-reply")

                self.transmit_bfd_good = MplsOam.Packet.WorkingRepSent.TransmitBfdGood()
                self.transmit_bfd_good.parent = self
                self._children_name_map["transmit_bfd_good"] = "transmit-bfd-good"
                self._children_yang_names.add("transmit-bfd-good")

                self.transmit_drop = MplsOam.Packet.WorkingRepSent.TransmitDrop()
                self.transmit_drop.parent = self
                self._children_name_map["transmit_drop"] = "transmit-drop"
                self._children_yang_names.add("transmit-drop")

                self.transmit_good = MplsOam.Packet.WorkingRepSent.TransmitGood()
                self.transmit_good.parent = self
                self._children_name_map["transmit_good"] = "transmit-good"
                self._children_yang_names.add("transmit-good")


            class TransmitGood(Entity):
                """
                Transmit good packets
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.WorkingRepSent.TransmitGood, self).__init__()

                    self.yang_name = "transmit-good"
                    self.yang_parent_name = "working-rep-sent"

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bytes",
                                    "packets") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsOam.Packet.WorkingRepSent.TransmitGood, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsOam.Packet.WorkingRepSent.TransmitGood, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.bytes.is_set or
                        self.packets.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bytes.yfilter != YFilter.not_set or
                        self.packets.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "transmit-good" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/working-rep-sent/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bytes.get_name_leafdata())
                    if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.packets.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bytes" or name == "packets"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bytes"):
                        self.bytes = value
                        self.bytes.value_namespace = name_space
                        self.bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "packets"):
                        self.packets = value
                        self.packets.value_namespace = name_space
                        self.packets.value_namespace_prefix = name_space_prefix


            class TransmitDrop(Entity):
                """
                Transmit drop packets
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.WorkingRepSent.TransmitDrop, self).__init__()

                    self.yang_name = "transmit-drop"
                    self.yang_parent_name = "working-rep-sent"

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bytes",
                                    "packets") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsOam.Packet.WorkingRepSent.TransmitDrop, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsOam.Packet.WorkingRepSent.TransmitDrop, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.bytes.is_set or
                        self.packets.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bytes.yfilter != YFilter.not_set or
                        self.packets.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "transmit-drop" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/working-rep-sent/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bytes.get_name_leafdata())
                    if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.packets.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bytes" or name == "packets"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bytes"):
                        self.bytes = value
                        self.bytes.value_namespace = name_space
                        self.bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "packets"):
                        self.packets = value
                        self.packets.value_namespace = name_space
                        self.packets.value_namespace_prefix = name_space_prefix


            class TransmitBfdGood(Entity):
                """
                Transmit good BFD request packets
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.WorkingRepSent.TransmitBfdGood, self).__init__()

                    self.yang_name = "transmit-bfd-good"
                    self.yang_parent_name = "working-rep-sent"

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bytes",
                                    "packets") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsOam.Packet.WorkingRepSent.TransmitBfdGood, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsOam.Packet.WorkingRepSent.TransmitBfdGood, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.bytes.is_set or
                        self.packets.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bytes.yfilter != YFilter.not_set or
                        self.packets.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "transmit-bfd-good" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/working-rep-sent/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bytes.get_name_leafdata())
                    if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.packets.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bytes" or name == "packets"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bytes"):
                        self.bytes = value
                        self.bytes.value_namespace = name_space
                        self.bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "packets"):
                        self.packets = value
                        self.packets.value_namespace = name_space
                        self.packets.value_namespace_prefix = name_space_prefix


            class BfdNoReply(Entity):
                """
                No Reply action for echo reqeust of BFD
                bootstrap
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.WorkingRepSent.BfdNoReply, self).__init__()

                    self.yang_name = "bfd-no-reply"
                    self.yang_parent_name = "working-rep-sent"

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bytes",
                                    "packets") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsOam.Packet.WorkingRepSent.BfdNoReply, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsOam.Packet.WorkingRepSent.BfdNoReply, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.bytes.is_set or
                        self.packets.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bytes.yfilter != YFilter.not_set or
                        self.packets.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "bfd-no-reply" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/working-rep-sent/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bytes.get_name_leafdata())
                    if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.packets.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bytes" or name == "packets"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bytes"):
                        self.bytes = value
                        self.bytes.value_namespace = name_space
                        self.bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "packets"):
                        self.packets = value
                        self.packets.value_namespace = name_space
                        self.packets.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    (self.bfd_no_reply is not None and self.bfd_no_reply.has_data()) or
                    (self.transmit_bfd_good is not None and self.transmit_bfd_good.has_data()) or
                    (self.transmit_drop is not None and self.transmit_drop.has_data()) or
                    (self.transmit_good is not None and self.transmit_good.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.bfd_no_reply is not None and self.bfd_no_reply.has_operation()) or
                    (self.transmit_bfd_good is not None and self.transmit_bfd_good.has_operation()) or
                    (self.transmit_drop is not None and self.transmit_drop.has_operation()) or
                    (self.transmit_good is not None and self.transmit_good.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "working-rep-sent" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "bfd-no-reply"):
                    if (self.bfd_no_reply is None):
                        self.bfd_no_reply = MplsOam.Packet.WorkingRepSent.BfdNoReply()
                        self.bfd_no_reply.parent = self
                        self._children_name_map["bfd_no_reply"] = "bfd-no-reply"
                    return self.bfd_no_reply

                if (child_yang_name == "transmit-bfd-good"):
                    if (self.transmit_bfd_good is None):
                        self.transmit_bfd_good = MplsOam.Packet.WorkingRepSent.TransmitBfdGood()
                        self.transmit_bfd_good.parent = self
                        self._children_name_map["transmit_bfd_good"] = "transmit-bfd-good"
                    return self.transmit_bfd_good

                if (child_yang_name == "transmit-drop"):
                    if (self.transmit_drop is None):
                        self.transmit_drop = MplsOam.Packet.WorkingRepSent.TransmitDrop()
                        self.transmit_drop.parent = self
                        self._children_name_map["transmit_drop"] = "transmit-drop"
                    return self.transmit_drop

                if (child_yang_name == "transmit-good"):
                    if (self.transmit_good is None):
                        self.transmit_good = MplsOam.Packet.WorkingRepSent.TransmitGood()
                        self.transmit_good.parent = self
                        self._children_name_map["transmit_good"] = "transmit-good"
                    return self.transmit_good

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "bfd-no-reply" or name == "transmit-bfd-good" or name == "transmit-drop" or name == "transmit-good"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class ProtectReqSent(Entity):
            """
            Protect Request Packet transmit counts
            
            .. attribute:: bfd_no_reply
            
            	No Reply action for echo reqeust of BFD bootstrap
            	**type**\:   :py:class:`BfdNoReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.ProtectReqSent.BfdNoReply>`
            
            .. attribute:: transmit_bfd_good
            
            	Transmit good BFD request packets
            	**type**\:   :py:class:`TransmitBfdGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.ProtectReqSent.TransmitBfdGood>`
            
            .. attribute:: transmit_drop
            
            	Transmit drop packets
            	**type**\:   :py:class:`TransmitDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.ProtectReqSent.TransmitDrop>`
            
            .. attribute:: transmit_good
            
            	Transmit good packets
            	**type**\:   :py:class:`TransmitGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.ProtectReqSent.TransmitGood>`
            
            

            """

            _prefix = 'mpls-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsOam.Packet.ProtectReqSent, self).__init__()

                self.yang_name = "protect-req-sent"
                self.yang_parent_name = "packet"

                self.bfd_no_reply = MplsOam.Packet.ProtectReqSent.BfdNoReply()
                self.bfd_no_reply.parent = self
                self._children_name_map["bfd_no_reply"] = "bfd-no-reply"
                self._children_yang_names.add("bfd-no-reply")

                self.transmit_bfd_good = MplsOam.Packet.ProtectReqSent.TransmitBfdGood()
                self.transmit_bfd_good.parent = self
                self._children_name_map["transmit_bfd_good"] = "transmit-bfd-good"
                self._children_yang_names.add("transmit-bfd-good")

                self.transmit_drop = MplsOam.Packet.ProtectReqSent.TransmitDrop()
                self.transmit_drop.parent = self
                self._children_name_map["transmit_drop"] = "transmit-drop"
                self._children_yang_names.add("transmit-drop")

                self.transmit_good = MplsOam.Packet.ProtectReqSent.TransmitGood()
                self.transmit_good.parent = self
                self._children_name_map["transmit_good"] = "transmit-good"
                self._children_yang_names.add("transmit-good")


            class TransmitGood(Entity):
                """
                Transmit good packets
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.ProtectReqSent.TransmitGood, self).__init__()

                    self.yang_name = "transmit-good"
                    self.yang_parent_name = "protect-req-sent"

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bytes",
                                    "packets") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsOam.Packet.ProtectReqSent.TransmitGood, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsOam.Packet.ProtectReqSent.TransmitGood, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.bytes.is_set or
                        self.packets.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bytes.yfilter != YFilter.not_set or
                        self.packets.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "transmit-good" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/protect-req-sent/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bytes.get_name_leafdata())
                    if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.packets.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bytes" or name == "packets"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bytes"):
                        self.bytes = value
                        self.bytes.value_namespace = name_space
                        self.bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "packets"):
                        self.packets = value
                        self.packets.value_namespace = name_space
                        self.packets.value_namespace_prefix = name_space_prefix


            class TransmitDrop(Entity):
                """
                Transmit drop packets
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.ProtectReqSent.TransmitDrop, self).__init__()

                    self.yang_name = "transmit-drop"
                    self.yang_parent_name = "protect-req-sent"

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bytes",
                                    "packets") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsOam.Packet.ProtectReqSent.TransmitDrop, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsOam.Packet.ProtectReqSent.TransmitDrop, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.bytes.is_set or
                        self.packets.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bytes.yfilter != YFilter.not_set or
                        self.packets.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "transmit-drop" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/protect-req-sent/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bytes.get_name_leafdata())
                    if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.packets.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bytes" or name == "packets"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bytes"):
                        self.bytes = value
                        self.bytes.value_namespace = name_space
                        self.bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "packets"):
                        self.packets = value
                        self.packets.value_namespace = name_space
                        self.packets.value_namespace_prefix = name_space_prefix


            class TransmitBfdGood(Entity):
                """
                Transmit good BFD request packets
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.ProtectReqSent.TransmitBfdGood, self).__init__()

                    self.yang_name = "transmit-bfd-good"
                    self.yang_parent_name = "protect-req-sent"

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bytes",
                                    "packets") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsOam.Packet.ProtectReqSent.TransmitBfdGood, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsOam.Packet.ProtectReqSent.TransmitBfdGood, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.bytes.is_set or
                        self.packets.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bytes.yfilter != YFilter.not_set or
                        self.packets.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "transmit-bfd-good" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/protect-req-sent/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bytes.get_name_leafdata())
                    if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.packets.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bytes" or name == "packets"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bytes"):
                        self.bytes = value
                        self.bytes.value_namespace = name_space
                        self.bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "packets"):
                        self.packets = value
                        self.packets.value_namespace = name_space
                        self.packets.value_namespace_prefix = name_space_prefix


            class BfdNoReply(Entity):
                """
                No Reply action for echo reqeust of BFD
                bootstrap
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.ProtectReqSent.BfdNoReply, self).__init__()

                    self.yang_name = "bfd-no-reply"
                    self.yang_parent_name = "protect-req-sent"

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bytes",
                                    "packets") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsOam.Packet.ProtectReqSent.BfdNoReply, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsOam.Packet.ProtectReqSent.BfdNoReply, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.bytes.is_set or
                        self.packets.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bytes.yfilter != YFilter.not_set or
                        self.packets.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "bfd-no-reply" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/protect-req-sent/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bytes.get_name_leafdata())
                    if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.packets.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bytes" or name == "packets"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bytes"):
                        self.bytes = value
                        self.bytes.value_namespace = name_space
                        self.bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "packets"):
                        self.packets = value
                        self.packets.value_namespace = name_space
                        self.packets.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    (self.bfd_no_reply is not None and self.bfd_no_reply.has_data()) or
                    (self.transmit_bfd_good is not None and self.transmit_bfd_good.has_data()) or
                    (self.transmit_drop is not None and self.transmit_drop.has_data()) or
                    (self.transmit_good is not None and self.transmit_good.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.bfd_no_reply is not None and self.bfd_no_reply.has_operation()) or
                    (self.transmit_bfd_good is not None and self.transmit_bfd_good.has_operation()) or
                    (self.transmit_drop is not None and self.transmit_drop.has_operation()) or
                    (self.transmit_good is not None and self.transmit_good.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "protect-req-sent" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "bfd-no-reply"):
                    if (self.bfd_no_reply is None):
                        self.bfd_no_reply = MplsOam.Packet.ProtectReqSent.BfdNoReply()
                        self.bfd_no_reply.parent = self
                        self._children_name_map["bfd_no_reply"] = "bfd-no-reply"
                    return self.bfd_no_reply

                if (child_yang_name == "transmit-bfd-good"):
                    if (self.transmit_bfd_good is None):
                        self.transmit_bfd_good = MplsOam.Packet.ProtectReqSent.TransmitBfdGood()
                        self.transmit_bfd_good.parent = self
                        self._children_name_map["transmit_bfd_good"] = "transmit-bfd-good"
                    return self.transmit_bfd_good

                if (child_yang_name == "transmit-drop"):
                    if (self.transmit_drop is None):
                        self.transmit_drop = MplsOam.Packet.ProtectReqSent.TransmitDrop()
                        self.transmit_drop.parent = self
                        self._children_name_map["transmit_drop"] = "transmit-drop"
                    return self.transmit_drop

                if (child_yang_name == "transmit-good"):
                    if (self.transmit_good is None):
                        self.transmit_good = MplsOam.Packet.ProtectReqSent.TransmitGood()
                        self.transmit_good.parent = self
                        self._children_name_map["transmit_good"] = "transmit-good"
                    return self.transmit_good

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "bfd-no-reply" or name == "transmit-bfd-good" or name == "transmit-drop" or name == "transmit-good"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class ProtectRepSent(Entity):
            """
            Protect Reply Packet transmit counts
            
            .. attribute:: bfd_no_reply
            
            	No Reply action for echo reqeust of BFD bootstrap
            	**type**\:   :py:class:`BfdNoReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.ProtectRepSent.BfdNoReply>`
            
            .. attribute:: transmit_bfd_good
            
            	Transmit good BFD request packets
            	**type**\:   :py:class:`TransmitBfdGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.ProtectRepSent.TransmitBfdGood>`
            
            .. attribute:: transmit_drop
            
            	Transmit drop packets
            	**type**\:   :py:class:`TransmitDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.ProtectRepSent.TransmitDrop>`
            
            .. attribute:: transmit_good
            
            	Transmit good packets
            	**type**\:   :py:class:`TransmitGood <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Packet.ProtectRepSent.TransmitGood>`
            
            

            """

            _prefix = 'mpls-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsOam.Packet.ProtectRepSent, self).__init__()

                self.yang_name = "protect-rep-sent"
                self.yang_parent_name = "packet"

                self.bfd_no_reply = MplsOam.Packet.ProtectRepSent.BfdNoReply()
                self.bfd_no_reply.parent = self
                self._children_name_map["bfd_no_reply"] = "bfd-no-reply"
                self._children_yang_names.add("bfd-no-reply")

                self.transmit_bfd_good = MplsOam.Packet.ProtectRepSent.TransmitBfdGood()
                self.transmit_bfd_good.parent = self
                self._children_name_map["transmit_bfd_good"] = "transmit-bfd-good"
                self._children_yang_names.add("transmit-bfd-good")

                self.transmit_drop = MplsOam.Packet.ProtectRepSent.TransmitDrop()
                self.transmit_drop.parent = self
                self._children_name_map["transmit_drop"] = "transmit-drop"
                self._children_yang_names.add("transmit-drop")

                self.transmit_good = MplsOam.Packet.ProtectRepSent.TransmitGood()
                self.transmit_good.parent = self
                self._children_name_map["transmit_good"] = "transmit-good"
                self._children_yang_names.add("transmit-good")


            class TransmitGood(Entity):
                """
                Transmit good packets
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.ProtectRepSent.TransmitGood, self).__init__()

                    self.yang_name = "transmit-good"
                    self.yang_parent_name = "protect-rep-sent"

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bytes",
                                    "packets") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsOam.Packet.ProtectRepSent.TransmitGood, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsOam.Packet.ProtectRepSent.TransmitGood, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.bytes.is_set or
                        self.packets.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bytes.yfilter != YFilter.not_set or
                        self.packets.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "transmit-good" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/protect-rep-sent/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bytes.get_name_leafdata())
                    if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.packets.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bytes" or name == "packets"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bytes"):
                        self.bytes = value
                        self.bytes.value_namespace = name_space
                        self.bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "packets"):
                        self.packets = value
                        self.packets.value_namespace = name_space
                        self.packets.value_namespace_prefix = name_space_prefix


            class TransmitDrop(Entity):
                """
                Transmit drop packets
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.ProtectRepSent.TransmitDrop, self).__init__()

                    self.yang_name = "transmit-drop"
                    self.yang_parent_name = "protect-rep-sent"

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bytes",
                                    "packets") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsOam.Packet.ProtectRepSent.TransmitDrop, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsOam.Packet.ProtectRepSent.TransmitDrop, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.bytes.is_set or
                        self.packets.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bytes.yfilter != YFilter.not_set or
                        self.packets.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "transmit-drop" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/protect-rep-sent/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bytes.get_name_leafdata())
                    if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.packets.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bytes" or name == "packets"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bytes"):
                        self.bytes = value
                        self.bytes.value_namespace = name_space
                        self.bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "packets"):
                        self.packets = value
                        self.packets.value_namespace = name_space
                        self.packets.value_namespace_prefix = name_space_prefix


            class TransmitBfdGood(Entity):
                """
                Transmit good BFD request packets
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.ProtectRepSent.TransmitBfdGood, self).__init__()

                    self.yang_name = "transmit-bfd-good"
                    self.yang_parent_name = "protect-rep-sent"

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bytes",
                                    "packets") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsOam.Packet.ProtectRepSent.TransmitBfdGood, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsOam.Packet.ProtectRepSent.TransmitBfdGood, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.bytes.is_set or
                        self.packets.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bytes.yfilter != YFilter.not_set or
                        self.packets.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "transmit-bfd-good" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/protect-rep-sent/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bytes.get_name_leafdata())
                    if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.packets.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bytes" or name == "packets"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bytes"):
                        self.bytes = value
                        self.bytes.value_namespace = name_space
                        self.bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "packets"):
                        self.packets = value
                        self.packets.value_namespace = name_space
                        self.packets.value_namespace_prefix = name_space_prefix


            class BfdNoReply(Entity):
                """
                No Reply action for echo reqeust of BFD
                bootstrap
                
                .. attribute:: bytes
                
                	Byte counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets
                
                	Packet counter
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Packet.ProtectRepSent.BfdNoReply, self).__init__()

                    self.yang_name = "bfd-no-reply"
                    self.yang_parent_name = "protect-rep-sent"

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.packets = YLeaf(YType.uint64, "packets")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bytes",
                                    "packets") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsOam.Packet.ProtectRepSent.BfdNoReply, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsOam.Packet.ProtectRepSent.BfdNoReply, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.bytes.is_set or
                        self.packets.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bytes.yfilter != YFilter.not_set or
                        self.packets.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "bfd-no-reply" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/protect-rep-sent/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bytes.get_name_leafdata())
                    if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.packets.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bytes" or name == "packets"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bytes"):
                        self.bytes = value
                        self.bytes.value_namespace = name_space
                        self.bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "packets"):
                        self.packets = value
                        self.packets.value_namespace = name_space
                        self.packets.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    (self.bfd_no_reply is not None and self.bfd_no_reply.has_data()) or
                    (self.transmit_bfd_good is not None and self.transmit_bfd_good.has_data()) or
                    (self.transmit_drop is not None and self.transmit_drop.has_data()) or
                    (self.transmit_good is not None and self.transmit_good.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.bfd_no_reply is not None and self.bfd_no_reply.has_operation()) or
                    (self.transmit_bfd_good is not None and self.transmit_bfd_good.has_operation()) or
                    (self.transmit_drop is not None and self.transmit_drop.has_operation()) or
                    (self.transmit_good is not None and self.transmit_good.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "protect-rep-sent" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/packet/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "bfd-no-reply"):
                    if (self.bfd_no_reply is None):
                        self.bfd_no_reply = MplsOam.Packet.ProtectRepSent.BfdNoReply()
                        self.bfd_no_reply.parent = self
                        self._children_name_map["bfd_no_reply"] = "bfd-no-reply"
                    return self.bfd_no_reply

                if (child_yang_name == "transmit-bfd-good"):
                    if (self.transmit_bfd_good is None):
                        self.transmit_bfd_good = MplsOam.Packet.ProtectRepSent.TransmitBfdGood()
                        self.transmit_bfd_good.parent = self
                        self._children_name_map["transmit_bfd_good"] = "transmit-bfd-good"
                    return self.transmit_bfd_good

                if (child_yang_name == "transmit-drop"):
                    if (self.transmit_drop is None):
                        self.transmit_drop = MplsOam.Packet.ProtectRepSent.TransmitDrop()
                        self.transmit_drop.parent = self
                        self._children_name_map["transmit_drop"] = "transmit-drop"
                    return self.transmit_drop

                if (child_yang_name == "transmit-good"):
                    if (self.transmit_good is None):
                        self.transmit_good = MplsOam.Packet.ProtectRepSent.TransmitGood()
                        self.transmit_good.parent = self
                        self._children_name_map["transmit_good"] = "transmit-good"
                    return self.transmit_good

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "bfd-no-reply" or name == "transmit-bfd-good" or name == "transmit-drop" or name == "transmit-good"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                (self.protect_rep_sent is not None and self.protect_rep_sent.has_data()) or
                (self.protect_req_sent is not None and self.protect_req_sent.has_data()) or
                (self.received is not None and self.received.has_data()) or
                (self.sent is not None and self.sent.has_data()) or
                (self.working_rep_sent is not None and self.working_rep_sent.has_data()) or
                (self.working_req_sent is not None and self.working_req_sent.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.protect_rep_sent is not None and self.protect_rep_sent.has_operation()) or
                (self.protect_req_sent is not None and self.protect_req_sent.has_operation()) or
                (self.received is not None and self.received.has_operation()) or
                (self.sent is not None and self.sent.has_operation()) or
                (self.working_rep_sent is not None and self.working_rep_sent.has_operation()) or
                (self.working_req_sent is not None and self.working_req_sent.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "packet" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "protect-rep-sent"):
                if (self.protect_rep_sent is None):
                    self.protect_rep_sent = MplsOam.Packet.ProtectRepSent()
                    self.protect_rep_sent.parent = self
                    self._children_name_map["protect_rep_sent"] = "protect-rep-sent"
                return self.protect_rep_sent

            if (child_yang_name == "protect-req-sent"):
                if (self.protect_req_sent is None):
                    self.protect_req_sent = MplsOam.Packet.ProtectReqSent()
                    self.protect_req_sent.parent = self
                    self._children_name_map["protect_req_sent"] = "protect-req-sent"
                return self.protect_req_sent

            if (child_yang_name == "received"):
                if (self.received is None):
                    self.received = MplsOam.Packet.Received()
                    self.received.parent = self
                    self._children_name_map["received"] = "received"
                return self.received

            if (child_yang_name == "sent"):
                if (self.sent is None):
                    self.sent = MplsOam.Packet.Sent()
                    self.sent.parent = self
                    self._children_name_map["sent"] = "sent"
                return self.sent

            if (child_yang_name == "working-rep-sent"):
                if (self.working_rep_sent is None):
                    self.working_rep_sent = MplsOam.Packet.WorkingRepSent()
                    self.working_rep_sent.parent = self
                    self._children_name_map["working_rep_sent"] = "working-rep-sent"
                return self.working_rep_sent

            if (child_yang_name == "working-req-sent"):
                if (self.working_req_sent is None):
                    self.working_req_sent = MplsOam.Packet.WorkingReqSent()
                    self.working_req_sent.parent = self
                    self._children_name_map["working_req_sent"] = "working-req-sent"
                return self.working_req_sent

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "protect-rep-sent" or name == "protect-req-sent" or name == "received" or name == "sent" or name == "working-rep-sent" or name == "working-req-sent"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Global_(Entity):
        """
        LSPV global counters operational data
        
        .. attribute:: collaborator_statistics
        
        	Collaborator statistics
        	**type**\:   :py:class:`CollaboratorStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Global_.CollaboratorStatistics>`
        
        .. attribute:: message_statistics
        
        	Message statistics
        	**type**\:   :py:class:`MessageStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Global_.MessageStatistics>`
        
        .. attribute:: total_clients
        
        	Number of clients
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'mpls-oam-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(MplsOam.Global_, self).__init__()

            self.yang_name = "global"
            self.yang_parent_name = "mpls-oam"

            self.total_clients = YLeaf(YType.uint32, "total-clients")

            self.collaborator_statistics = MplsOam.Global_.CollaboratorStatistics()
            self.collaborator_statistics.parent = self
            self._children_name_map["collaborator_statistics"] = "collaborator-statistics"
            self._children_yang_names.add("collaborator-statistics")

            self.message_statistics = MplsOam.Global_.MessageStatistics()
            self.message_statistics.parent = self
            self._children_name_map["message_statistics"] = "message-statistics"
            self._children_yang_names.add("message-statistics")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("total_clients") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(MplsOam.Global_, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsOam.Global_, self).__setattr__(name, value)


        class MessageStatistics(Entity):
            """
            Message statistics
            
            .. attribute:: echo_cancel_messages
            
            	Message echo cancel count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: echo_submit_messages
            
            	Message echo submit count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: get_config_messages
            
            	Message get configiuration count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: get_response_messages
            
            	Message get response count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: get_result_messages
            
            	Message get results count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: property_block_messages
            
            	Message property block count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: property_request_messages
            
            	Message property request count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: property_response_messages
            
            	Message property response count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: register_messages
            
            	Message register count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: thread_request_messages
            
            	Message thread request count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: unregister_messages
            
            	Message unregister count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'mpls-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsOam.Global_.MessageStatistics, self).__init__()

                self.yang_name = "message-statistics"
                self.yang_parent_name = "global"

                self.echo_cancel_messages = YLeaf(YType.uint32, "echo-cancel-messages")

                self.echo_submit_messages = YLeaf(YType.uint32, "echo-submit-messages")

                self.get_config_messages = YLeaf(YType.uint32, "get-config-messages")

                self.get_response_messages = YLeaf(YType.uint32, "get-response-messages")

                self.get_result_messages = YLeaf(YType.uint32, "get-result-messages")

                self.property_block_messages = YLeaf(YType.uint32, "property-block-messages")

                self.property_request_messages = YLeaf(YType.uint32, "property-request-messages")

                self.property_response_messages = YLeaf(YType.uint32, "property-response-messages")

                self.register_messages = YLeaf(YType.uint32, "register-messages")

                self.thread_request_messages = YLeaf(YType.uint32, "thread-request-messages")

                self.unregister_messages = YLeaf(YType.uint32, "unregister-messages")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("echo_cancel_messages",
                                "echo_submit_messages",
                                "get_config_messages",
                                "get_response_messages",
                                "get_result_messages",
                                "property_block_messages",
                                "property_request_messages",
                                "property_response_messages",
                                "register_messages",
                                "thread_request_messages",
                                "unregister_messages") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsOam.Global_.MessageStatistics, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsOam.Global_.MessageStatistics, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.echo_cancel_messages.is_set or
                    self.echo_submit_messages.is_set or
                    self.get_config_messages.is_set or
                    self.get_response_messages.is_set or
                    self.get_result_messages.is_set or
                    self.property_block_messages.is_set or
                    self.property_request_messages.is_set or
                    self.property_response_messages.is_set or
                    self.register_messages.is_set or
                    self.thread_request_messages.is_set or
                    self.unregister_messages.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.echo_cancel_messages.yfilter != YFilter.not_set or
                    self.echo_submit_messages.yfilter != YFilter.not_set or
                    self.get_config_messages.yfilter != YFilter.not_set or
                    self.get_response_messages.yfilter != YFilter.not_set or
                    self.get_result_messages.yfilter != YFilter.not_set or
                    self.property_block_messages.yfilter != YFilter.not_set or
                    self.property_request_messages.yfilter != YFilter.not_set or
                    self.property_response_messages.yfilter != YFilter.not_set or
                    self.register_messages.yfilter != YFilter.not_set or
                    self.thread_request_messages.yfilter != YFilter.not_set or
                    self.unregister_messages.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "message-statistics" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/global/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.echo_cancel_messages.is_set or self.echo_cancel_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.echo_cancel_messages.get_name_leafdata())
                if (self.echo_submit_messages.is_set or self.echo_submit_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.echo_submit_messages.get_name_leafdata())
                if (self.get_config_messages.is_set or self.get_config_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.get_config_messages.get_name_leafdata())
                if (self.get_response_messages.is_set or self.get_response_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.get_response_messages.get_name_leafdata())
                if (self.get_result_messages.is_set or self.get_result_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.get_result_messages.get_name_leafdata())
                if (self.property_block_messages.is_set or self.property_block_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.property_block_messages.get_name_leafdata())
                if (self.property_request_messages.is_set or self.property_request_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.property_request_messages.get_name_leafdata())
                if (self.property_response_messages.is_set or self.property_response_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.property_response_messages.get_name_leafdata())
                if (self.register_messages.is_set or self.register_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.register_messages.get_name_leafdata())
                if (self.thread_request_messages.is_set or self.thread_request_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.thread_request_messages.get_name_leafdata())
                if (self.unregister_messages.is_set or self.unregister_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.unregister_messages.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "echo-cancel-messages" or name == "echo-submit-messages" or name == "get-config-messages" or name == "get-response-messages" or name == "get-result-messages" or name == "property-block-messages" or name == "property-request-messages" or name == "property-response-messages" or name == "register-messages" or name == "thread-request-messages" or name == "unregister-messages"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "echo-cancel-messages"):
                    self.echo_cancel_messages = value
                    self.echo_cancel_messages.value_namespace = name_space
                    self.echo_cancel_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "echo-submit-messages"):
                    self.echo_submit_messages = value
                    self.echo_submit_messages.value_namespace = name_space
                    self.echo_submit_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "get-config-messages"):
                    self.get_config_messages = value
                    self.get_config_messages.value_namespace = name_space
                    self.get_config_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "get-response-messages"):
                    self.get_response_messages = value
                    self.get_response_messages.value_namespace = name_space
                    self.get_response_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "get-result-messages"):
                    self.get_result_messages = value
                    self.get_result_messages.value_namespace = name_space
                    self.get_result_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "property-block-messages"):
                    self.property_block_messages = value
                    self.property_block_messages.value_namespace = name_space
                    self.property_block_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "property-request-messages"):
                    self.property_request_messages = value
                    self.property_request_messages.value_namespace = name_space
                    self.property_request_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "property-response-messages"):
                    self.property_response_messages = value
                    self.property_response_messages.value_namespace = name_space
                    self.property_response_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "register-messages"):
                    self.register_messages = value
                    self.register_messages.value_namespace = name_space
                    self.register_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "thread-request-messages"):
                    self.thread_request_messages = value
                    self.thread_request_messages.value_namespace = name_space
                    self.thread_request_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "unregister-messages"):
                    self.unregister_messages = value
                    self.unregister_messages.value_namespace = name_space
                    self.unregister_messages.value_namespace_prefix = name_space_prefix


        class CollaboratorStatistics(Entity):
            """
            Collaborator statistics
            
            .. attribute:: collaborator_i_parm
            
            	Collaborator IPARM counts
            	**type**\:   :py:class:`CollaboratorIParm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Global_.CollaboratorStatistics.CollaboratorIParm>`
            
            .. attribute:: collaborator_im
            
            	Collaborator IM counts
            	**type**\:   :py:class:`CollaboratorIm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Global_.CollaboratorStatistics.CollaboratorIm>`
            
            .. attribute:: collaborator_net_io
            
            	Collaborator NetIO counts
            	**type**\:   :py:class:`CollaboratorNetIo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Global_.CollaboratorStatistics.CollaboratorNetIo>`
            
            .. attribute:: collaborator_rib
            
            	Collaborator RIB counts
            	**type**\:   :py:class:`CollaboratorRib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper.MplsOam.Global_.CollaboratorStatistics.CollaboratorRib>`
            
            

            """

            _prefix = 'mpls-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsOam.Global_.CollaboratorStatistics, self).__init__()

                self.yang_name = "collaborator-statistics"
                self.yang_parent_name = "global"

                self.collaborator_i_parm = MplsOam.Global_.CollaboratorStatistics.CollaboratorIParm()
                self.collaborator_i_parm.parent = self
                self._children_name_map["collaborator_i_parm"] = "collaborator-i-parm"
                self._children_yang_names.add("collaborator-i-parm")

                self.collaborator_im = MplsOam.Global_.CollaboratorStatistics.CollaboratorIm()
                self.collaborator_im.parent = self
                self._children_name_map["collaborator_im"] = "collaborator-im"
                self._children_yang_names.add("collaborator-im")

                self.collaborator_net_io = MplsOam.Global_.CollaboratorStatistics.CollaboratorNetIo()
                self.collaborator_net_io.parent = self
                self._children_name_map["collaborator_net_io"] = "collaborator-net-io"
                self._children_yang_names.add("collaborator-net-io")

                self.collaborator_rib = MplsOam.Global_.CollaboratorStatistics.CollaboratorRib()
                self.collaborator_rib.parent = self
                self._children_name_map["collaborator_rib"] = "collaborator-rib"
                self._children_yang_names.add("collaborator-rib")


            class CollaboratorIParm(Entity):
                """
                Collaborator IPARM counts
                
                .. attribute:: downs
                
                	Collaborator down counter
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: ups
                
                	Collaborator up counter
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Global_.CollaboratorStatistics.CollaboratorIParm, self).__init__()

                    self.yang_name = "collaborator-i-parm"
                    self.yang_parent_name = "collaborator-statistics"

                    self.downs = YLeaf(YType.uint32, "downs")

                    self.ups = YLeaf(YType.uint32, "ups")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("downs",
                                    "ups") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsOam.Global_.CollaboratorStatistics.CollaboratorIParm, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsOam.Global_.CollaboratorStatistics.CollaboratorIParm, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.downs.is_set or
                        self.ups.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.downs.yfilter != YFilter.not_set or
                        self.ups.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "collaborator-i-parm" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/global/collaborator-statistics/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.downs.is_set or self.downs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.downs.get_name_leafdata())
                    if (self.ups.is_set or self.ups.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ups.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "downs" or name == "ups"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "downs"):
                        self.downs = value
                        self.downs.value_namespace = name_space
                        self.downs.value_namespace_prefix = name_space_prefix
                    if(value_path == "ups"):
                        self.ups = value
                        self.ups.value_namespace = name_space
                        self.ups.value_namespace_prefix = name_space_prefix


            class CollaboratorIm(Entity):
                """
                Collaborator IM counts
                
                .. attribute:: downs
                
                	Collaborator down counter
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: ups
                
                	Collaborator up counter
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Global_.CollaboratorStatistics.CollaboratorIm, self).__init__()

                    self.yang_name = "collaborator-im"
                    self.yang_parent_name = "collaborator-statistics"

                    self.downs = YLeaf(YType.uint32, "downs")

                    self.ups = YLeaf(YType.uint32, "ups")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("downs",
                                    "ups") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsOam.Global_.CollaboratorStatistics.CollaboratorIm, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsOam.Global_.CollaboratorStatistics.CollaboratorIm, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.downs.is_set or
                        self.ups.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.downs.yfilter != YFilter.not_set or
                        self.ups.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "collaborator-im" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/global/collaborator-statistics/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.downs.is_set or self.downs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.downs.get_name_leafdata())
                    if (self.ups.is_set or self.ups.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ups.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "downs" or name == "ups"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "downs"):
                        self.downs = value
                        self.downs.value_namespace = name_space
                        self.downs.value_namespace_prefix = name_space_prefix
                    if(value_path == "ups"):
                        self.ups = value
                        self.ups.value_namespace = name_space
                        self.ups.value_namespace_prefix = name_space_prefix


            class CollaboratorNetIo(Entity):
                """
                Collaborator NetIO counts
                
                .. attribute:: downs
                
                	Collaborator down counter
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: ups
                
                	Collaborator up counter
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Global_.CollaboratorStatistics.CollaboratorNetIo, self).__init__()

                    self.yang_name = "collaborator-net-io"
                    self.yang_parent_name = "collaborator-statistics"

                    self.downs = YLeaf(YType.uint32, "downs")

                    self.ups = YLeaf(YType.uint32, "ups")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("downs",
                                    "ups") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsOam.Global_.CollaboratorStatistics.CollaboratorNetIo, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsOam.Global_.CollaboratorStatistics.CollaboratorNetIo, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.downs.is_set or
                        self.ups.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.downs.yfilter != YFilter.not_set or
                        self.ups.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "collaborator-net-io" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/global/collaborator-statistics/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.downs.is_set or self.downs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.downs.get_name_leafdata())
                    if (self.ups.is_set or self.ups.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ups.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "downs" or name == "ups"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "downs"):
                        self.downs = value
                        self.downs.value_namespace = name_space
                        self.downs.value_namespace_prefix = name_space_prefix
                    if(value_path == "ups"):
                        self.ups = value
                        self.ups.value_namespace = name_space
                        self.ups.value_namespace_prefix = name_space_prefix


            class CollaboratorRib(Entity):
                """
                Collaborator RIB counts
                
                .. attribute:: downs
                
                	Collaborator down counter
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: ups
                
                	Collaborator up counter
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'mpls-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsOam.Global_.CollaboratorStatistics.CollaboratorRib, self).__init__()

                    self.yang_name = "collaborator-rib"
                    self.yang_parent_name = "collaborator-statistics"

                    self.downs = YLeaf(YType.uint32, "downs")

                    self.ups = YLeaf(YType.uint32, "ups")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("downs",
                                    "ups") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsOam.Global_.CollaboratorStatistics.CollaboratorRib, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsOam.Global_.CollaboratorStatistics.CollaboratorRib, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.downs.is_set or
                        self.ups.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.downs.yfilter != YFilter.not_set or
                        self.ups.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "collaborator-rib" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/global/collaborator-statistics/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.downs.is_set or self.downs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.downs.get_name_leafdata())
                    if (self.ups.is_set or self.ups.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ups.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "downs" or name == "ups"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "downs"):
                        self.downs = value
                        self.downs.value_namespace = name_space
                        self.downs.value_namespace_prefix = name_space_prefix
                    if(value_path == "ups"):
                        self.ups = value
                        self.ups.value_namespace = name_space
                        self.ups.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    (self.collaborator_i_parm is not None and self.collaborator_i_parm.has_data()) or
                    (self.collaborator_im is not None and self.collaborator_im.has_data()) or
                    (self.collaborator_net_io is not None and self.collaborator_net_io.has_data()) or
                    (self.collaborator_rib is not None and self.collaborator_rib.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.collaborator_i_parm is not None and self.collaborator_i_parm.has_operation()) or
                    (self.collaborator_im is not None and self.collaborator_im.has_operation()) or
                    (self.collaborator_net_io is not None and self.collaborator_net_io.has_operation()) or
                    (self.collaborator_rib is not None and self.collaborator_rib.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "collaborator-statistics" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/global/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "collaborator-i-parm"):
                    if (self.collaborator_i_parm is None):
                        self.collaborator_i_parm = MplsOam.Global_.CollaboratorStatistics.CollaboratorIParm()
                        self.collaborator_i_parm.parent = self
                        self._children_name_map["collaborator_i_parm"] = "collaborator-i-parm"
                    return self.collaborator_i_parm

                if (child_yang_name == "collaborator-im"):
                    if (self.collaborator_im is None):
                        self.collaborator_im = MplsOam.Global_.CollaboratorStatistics.CollaboratorIm()
                        self.collaborator_im.parent = self
                        self._children_name_map["collaborator_im"] = "collaborator-im"
                    return self.collaborator_im

                if (child_yang_name == "collaborator-net-io"):
                    if (self.collaborator_net_io is None):
                        self.collaborator_net_io = MplsOam.Global_.CollaboratorStatistics.CollaboratorNetIo()
                        self.collaborator_net_io.parent = self
                        self._children_name_map["collaborator_net_io"] = "collaborator-net-io"
                    return self.collaborator_net_io

                if (child_yang_name == "collaborator-rib"):
                    if (self.collaborator_rib is None):
                        self.collaborator_rib = MplsOam.Global_.CollaboratorStatistics.CollaboratorRib()
                        self.collaborator_rib.parent = self
                        self._children_name_map["collaborator_rib"] = "collaborator-rib"
                    return self.collaborator_rib

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "collaborator-i-parm" or name == "collaborator-im" or name == "collaborator-net-io" or name == "collaborator-rib"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                self.total_clients.is_set or
                (self.collaborator_statistics is not None and self.collaborator_statistics.has_data()) or
                (self.message_statistics is not None and self.message_statistics.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.total_clients.yfilter != YFilter.not_set or
                (self.collaborator_statistics is not None and self.collaborator_statistics.has_operation()) or
                (self.message_statistics is not None and self.message_statistics.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "global" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.total_clients.is_set or self.total_clients.yfilter != YFilter.not_set):
                leaf_name_data.append(self.total_clients.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "collaborator-statistics"):
                if (self.collaborator_statistics is None):
                    self.collaborator_statistics = MplsOam.Global_.CollaboratorStatistics()
                    self.collaborator_statistics.parent = self
                    self._children_name_map["collaborator_statistics"] = "collaborator-statistics"
                return self.collaborator_statistics

            if (child_yang_name == "message-statistics"):
                if (self.message_statistics is None):
                    self.message_statistics = MplsOam.Global_.MessageStatistics()
                    self.message_statistics.parent = self
                    self._children_name_map["message_statistics"] = "message-statistics"
                return self.message_statistics

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "collaborator-statistics" or name == "message-statistics" or name == "total-clients"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "total-clients"):
                self.total_clients = value
                self.total_clients.value_namespace = name_space
                self.total_clients.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            (self.global_ is not None and self.global_.has_data()) or
            (self.interface is not None and self.interface.has_data()) or
            (self.packet is not None and self.packet.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.global_ is not None and self.global_.has_operation()) or
            (self.interface is not None and self.interface.has_operation()) or
            (self.packet is not None and self.packet.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-mpls-oam-oper:mpls-oam" + path_buffer

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

        if (child_yang_name == "global"):
            if (self.global_ is None):
                self.global_ = MplsOam.Global_()
                self.global_.parent = self
                self._children_name_map["global_"] = "global"
            return self.global_

        if (child_yang_name == "interface"):
            if (self.interface is None):
                self.interface = MplsOam.Interface()
                self.interface.parent = self
                self._children_name_map["interface"] = "interface"
            return self.interface

        if (child_yang_name == "packet"):
            if (self.packet is None):
                self.packet = MplsOam.Packet()
                self.packet.parent = self
                self._children_name_map["packet"] = "packet"
            return self.packet

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "global" or name == "interface" or name == "packet"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = MplsOam()
        return self._top_entity


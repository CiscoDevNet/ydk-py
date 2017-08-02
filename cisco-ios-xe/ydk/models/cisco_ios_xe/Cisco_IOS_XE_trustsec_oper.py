""" Cisco_IOS_XE_trustsec_oper 

This module contains a collection of YANG definitions
for monitoring of Cisco Trustsec operational information on
Role based permissions, IP\-SGT bindings and SXP connections.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class CtsOdmBindingSource(Enum):
    """
    CtsOdmBindingSource

    Binding Source enumeration

    .. data:: default = 0

    	Default Security Group Tag binding value in this device

    	for the given IP-Address

    .. data:: from_vlan = 1

    	Security Group Tag binding value in this device for the given

    	IP-Address is learned from a VLAN

    .. data:: from_cli = 2

    	Security Group Tag binding value in this device

    	for the given

    	IP-Address is configure from CLI (Command Line Inteface)

    .. data:: from_l3if = 3

    	Security Group Tag binding value in this device

    	for the given IP-Address is learned from a L3 (Layer 3) interface

    .. data:: from_cfp = 4

    	Security Group Tag binding value in this device

    	for the given IP-Address is learned via SXP

    	binding exchange protocol

    .. data:: from_ip_arp = 5

    	Security Group Tag binding value in this

    	device for the given

    	IP-Address is learned via IP-ARP protocol

    .. data:: from_local = 6

    	Security Group Tag binding value in this device

    	for the given IP-Address is learned locally

    .. data:: from_sgt_caching = 7

    	Security Group Tag binding value in this device

    	for the given IP-Address is learned via Security Group Tag

    	caching from datapath.

    .. data:: from_cli_hi = 8

    	Security Group Tag binding value in this device

    	for the given IP-Address is configured from CLI-high priority.

    """

    default = Enum.YLeaf(0, "default")

    from_vlan = Enum.YLeaf(1, "from-vlan")

    from_cli = Enum.YLeaf(2, "from-cli")

    from_l3if = Enum.YLeaf(3, "from-l3if")

    from_cfp = Enum.YLeaf(4, "from-cfp")

    from_ip_arp = Enum.YLeaf(5, "from-ip-arp")

    from_local = Enum.YLeaf(6, "from-local")

    from_sgt_caching = Enum.YLeaf(7, "from-sgt-caching")

    from_cli_hi = Enum.YLeaf(8, "from-cli-hi")


class SxpConMode(Enum):
    """
    SxpConMode

    SXP Connection mode

    .. data:: con_mode_invalid = 0

    	SXP Connection mode is Invalid

    .. data:: con_mode_speaker = 1

    	SXP Connection mode is Speaker

    .. data:: con_mode_listener = 2

    	SXP Connection mode is Listener

    .. data:: con_mode_both = 3

    	SXP Connection mode is Both (Speaker and Listener)

    """

    con_mode_invalid = Enum.YLeaf(0, "con-mode-invalid")

    con_mode_speaker = Enum.YLeaf(1, "con-mode-speaker")

    con_mode_listener = Enum.YLeaf(2, "con-mode-listener")

    con_mode_both = Enum.YLeaf(3, "con-mode-both")


class SxpConState(Enum):
    """
    SxpConState

    SXP Connection state

    .. data:: state_off = 0

    	SXP Connection state is OFF

    .. data:: state_pending_on = 1

    	SXP Connection state is Pending-On

    .. data:: state_on = 2

    	SXP Connection state is ON

    .. data:: state_delete_hold_down = 3

    	SXP Connection state is Delete-Hold-Down

    .. data:: state_not_applicable = 4

    	SXP Connection state is Not-Applicable

    """

    state_off = Enum.YLeaf(0, "state-off")

    state_pending_on = Enum.YLeaf(1, "state-pending-on")

    state_on = Enum.YLeaf(2, "state-on")

    state_delete_hold_down = Enum.YLeaf(3, "state-delete-hold-down")

    state_not_applicable = Enum.YLeaf(4, "state-not-applicable")



class TrustsecState(Entity):
    """
    This is top level container for Cisco Trusted Security
    solution operational data.
    It can have Security Group Tag binding information for
    the given IP\-Address, Role based permissions between a
    Source Security Group Tag and a Destination Security
    Group, SXP Connection information for a given peer
    IP\-Address in this device
    
    .. attribute:: cts_rolebased_policies
    
    	Role based permissions between a Source Security Group and a Destination Security Group are configured by the administrator in the Identity Services Engine or in the Device
    	**type**\:   :py:class:`CtsRolebasedPolicies <ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper.TrustsecState.CtsRolebasedPolicies>`
    
    .. attribute:: cts_rolebased_sgtmaps
    
    	Security Group Tag value corresponding to an IP\-Address  in the given VRF instance in this device
    	**type**\:   :py:class:`CtsRolebasedSgtmaps <ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper.TrustsecState.CtsRolebasedSgtmaps>`
    
    .. attribute:: cts_sxp_connections
    
    	Trustsec SXP connection is used between Cisco devices to propagate Security Group Tags from one device to  another device. One of the device will be in Speaker  mode or Listener mode or both the devices can be in both the connection modes
    	**type**\:   :py:class:`CtsSxpConnections <ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper.TrustsecState.CtsSxpConnections>`
    
    

    """

    _prefix = 'trustsec-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(TrustsecState, self).__init__()
        self._top_entity = None

        self.yang_name = "trustsec-state"
        self.yang_parent_name = "Cisco-IOS-XE-trustsec-oper"

        self.cts_rolebased_policies = TrustsecState.CtsRolebasedPolicies()
        self.cts_rolebased_policies.parent = self
        self._children_name_map["cts_rolebased_policies"] = "cts-rolebased-policies"
        self._children_yang_names.add("cts-rolebased-policies")

        self.cts_rolebased_sgtmaps = TrustsecState.CtsRolebasedSgtmaps()
        self.cts_rolebased_sgtmaps.parent = self
        self._children_name_map["cts_rolebased_sgtmaps"] = "cts-rolebased-sgtmaps"
        self._children_yang_names.add("cts-rolebased-sgtmaps")

        self.cts_sxp_connections = TrustsecState.CtsSxpConnections()
        self.cts_sxp_connections.parent = self
        self._children_name_map["cts_sxp_connections"] = "cts-sxp-connections"
        self._children_yang_names.add("cts-sxp-connections")


    class CtsRolebasedSgtmaps(Entity):
        """
        Security Group Tag value corresponding to an IP\-Address 
        in the given VRF instance in this device
        
        .. attribute:: cts_rolebased_sgtmap
        
        	Security Group Tag is assigned for an IP\-Address based on the user permissions and authorization  level as configured by the network administrator in Identity Service Engine server or in the device locally
        	**type**\: list of    :py:class:`CtsRolebasedSgtmap <ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper.TrustsecState.CtsRolebasedSgtmaps.CtsRolebasedSgtmap>`
        
        

        """

        _prefix = 'trustsec-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            super(TrustsecState.CtsRolebasedSgtmaps, self).__init__()

            self.yang_name = "cts-rolebased-sgtmaps"
            self.yang_parent_name = "trustsec-state"

            self.cts_rolebased_sgtmap = YList(self)

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
                        super(TrustsecState.CtsRolebasedSgtmaps, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(TrustsecState.CtsRolebasedSgtmaps, self).__setattr__(name, value)


        class CtsRolebasedSgtmap(Entity):
            """
            Security Group Tag is assigned for an IP\-Address
            based on the user permissions and authorization 
            level as configured by the network administrator
            in Identity Service Engine server or in the device locally
            
            .. attribute:: ip  <key>
            
            	IP\-Prefix information to find its corresponding Secure Group Tag. Only IPv4 prefix information is supported currently to get the Security Group Tag binding in this device
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
            
            
            ----
            .. attribute:: vrf_name  <key>
            
            	VRF\-Name to find the Security Group Tag for the corresponding IP\-Address in this VRF instance. Only default VRF is supported currently which is indicated by (empty string)
            	**type**\:  str
            
            .. attribute:: sgt
            
            	Security Group Tag value corresponding to the given IP\-Address
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: source
            
            	Source information via which the Security Group Tag binding was learned in this device
            	**type**\:   :py:class:`CtsOdmBindingSource <ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper.CtsOdmBindingSource>`
            
            

            """

            _prefix = 'trustsec-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(TrustsecState.CtsRolebasedSgtmaps.CtsRolebasedSgtmap, self).__init__()

                self.yang_name = "cts-rolebased-sgtmap"
                self.yang_parent_name = "cts-rolebased-sgtmaps"

                self.ip = YLeaf(YType.str, "ip")

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.sgt = YLeaf(YType.int32, "sgt")

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
                    if name in ("ip",
                                "vrf_name",
                                "sgt",
                                "source") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(TrustsecState.CtsRolebasedSgtmaps.CtsRolebasedSgtmap, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(TrustsecState.CtsRolebasedSgtmaps.CtsRolebasedSgtmap, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ip.is_set or
                    self.vrf_name.is_set or
                    self.sgt.is_set or
                    self.source.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ip.yfilter != YFilter.not_set or
                    self.vrf_name.yfilter != YFilter.not_set or
                    self.sgt.yfilter != YFilter.not_set or
                    self.source.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cts-rolebased-sgtmap" + "[ip='" + self.ip.get() + "']" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XE-trustsec-oper:trustsec-state/cts-rolebased-sgtmaps/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ip.is_set or self.ip.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ip.get_name_leafdata())
                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_name.get_name_leafdata())
                if (self.sgt.is_set or self.sgt.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sgt.get_name_leafdata())
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
                if(name == "ip" or name == "vrf-name" or name == "sgt" or name == "source"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ip"):
                    self.ip = value
                    self.ip.value_namespace = name_space
                    self.ip.value_namespace_prefix = name_space_prefix
                if(value_path == "vrf-name"):
                    self.vrf_name = value
                    self.vrf_name.value_namespace = name_space
                    self.vrf_name.value_namespace_prefix = name_space_prefix
                if(value_path == "sgt"):
                    self.sgt = value
                    self.sgt.value_namespace = name_space
                    self.sgt.value_namespace_prefix = name_space_prefix
                if(value_path == "source"):
                    self.source = value
                    self.source.value_namespace = name_space
                    self.source.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cts_rolebased_sgtmap:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cts_rolebased_sgtmap:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cts-rolebased-sgtmaps" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XE-trustsec-oper:trustsec-state/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cts-rolebased-sgtmap"):
                for c in self.cts_rolebased_sgtmap:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = TrustsecState.CtsRolebasedSgtmaps.CtsRolebasedSgtmap()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cts_rolebased_sgtmap.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cts-rolebased-sgtmap"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class CtsRolebasedPolicies(Entity):
        """
        Role based permissions between a Source Security Group
        and a Destination Security Group are configured by the
        administrator in the Identity Services Engine or in the Device
        
        .. attribute:: cts_rolebased_policy
        
        	Role based permissions between a Source Security Group and a Destination Security Group can be retrieved from the device using a Security Group Tag and Destination Group Tag value
        	**type**\: list of    :py:class:`CtsRolebasedPolicy <ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper.TrustsecState.CtsRolebasedPolicies.CtsRolebasedPolicy>`
        
        

        """

        _prefix = 'trustsec-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            super(TrustsecState.CtsRolebasedPolicies, self).__init__()

            self.yang_name = "cts-rolebased-policies"
            self.yang_parent_name = "trustsec-state"

            self.cts_rolebased_policy = YList(self)

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
                        super(TrustsecState.CtsRolebasedPolicies, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(TrustsecState.CtsRolebasedPolicies, self).__setattr__(name, value)


        class CtsRolebasedPolicy(Entity):
            """
            Role based permissions between a Source Security Group
            and a Destination Security Group can be retrieved from
            the device using a Security Group Tag and Destination
            Group Tag value
            
            .. attribute:: src_sgt  <key>
            
            	Source Security Group Tag number. This value must be in the inclusive range of \-1 to 65519
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: dst_sgt  <key>
            
            	Destination Security Tag number. This value must be in the inclusive range of \-1 to 65519
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: hardware_deny_count
            
            	Number of packets that have been denied in the hardware forwarding path of the device by the Role based permissions between a Source Security Group and a Destination Security Group
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: hardware_monitor_count
            
            	Number of packets that have been monitored in the hardware forwarding path of the device by the Role based permissions between a Source Security Group and a Destination Security Group
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: hardware_permit_count
            
            	Number of packets that have been permitted in the hardware forwarding path of the device by the Role based permissions between a Source Security Group and a Destination Security Group
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: last_updated_time
            
            	Indicates the time when the Role based permissions between a Source Security Group and a Destination Security Group was modified or updated last. The value will be represented as date and time  corresponding to the local time zone of the Identify Services Engine when the Role based  permissions was modified or updated last
            	**type**\:  str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            .. attribute:: monitor_mode
            
            	Indicates the monitor mode status between the Source Security Group and Destination Security Group is currently enabled or disabled. This will be TRUE if monitor mode is enabled and FALSE if it is disabled
            	**type**\:  bool
            
            .. attribute:: num_of_sgacl
            
            	Number of Security Group Access Control Lists that are currently applied between the Source Security Group and the Destination Security Group. This should match the number of Security Group Access Control List names in sgacl\-name
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: policy_life_time
            
            	Duration of the Role based permissions that are applied between a Source Security Group and a Destination Security Group. The duration is represented in seconds
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: sgacl_name
            
            	List of Security Group Access Control List names separated by semi\-colon(;)
            	**type**\:  str
            
            .. attribute:: software_deny_count
            
            	Number of packets that have been denied in the  software forwarding path of the device by the Role based permissions between a Source Security Group and a Destination Security Group
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: software_monitor_count
            
            	Number of packets that have been monitored in the software forwarding path of the device by the Role based permissions between a Source Security Group and a Destination Security Group
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: software_permit_count
            
            	Number of packets that have been permitted in the software forwarding path of the device by the Role based permissions between a Source Security Group and a Destination Security Group
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: total_deny_count
            
            	Total number of packets that have been denied by the Role based permissions between a Source Security Group and a Destination Security Group. This corresponds to total packets denied in both hardware and software forwarding paths of the device
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: total_permit_count
            
            	Total number of packets that have been permitted by the Role based permissions between a Source Security Group and a Destination Security Group. This corresponds to total packets allowed in both hardware and software forwarding paths of the device
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'trustsec-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(TrustsecState.CtsRolebasedPolicies.CtsRolebasedPolicy, self).__init__()

                self.yang_name = "cts-rolebased-policy"
                self.yang_parent_name = "cts-rolebased-policies"

                self.src_sgt = YLeaf(YType.int32, "src-sgt")

                self.dst_sgt = YLeaf(YType.int32, "dst-sgt")

                self.hardware_deny_count = YLeaf(YType.uint64, "hardware-deny-count")

                self.hardware_monitor_count = YLeaf(YType.uint64, "hardware-monitor-count")

                self.hardware_permit_count = YLeaf(YType.uint64, "hardware-permit-count")

                self.last_updated_time = YLeaf(YType.str, "last-updated-time")

                self.monitor_mode = YLeaf(YType.boolean, "monitor-mode")

                self.num_of_sgacl = YLeaf(YType.uint32, "num-of-sgacl")

                self.policy_life_time = YLeaf(YType.uint64, "policy-life-time")

                self.sgacl_name = YLeaf(YType.str, "sgacl-name")

                self.software_deny_count = YLeaf(YType.uint64, "software-deny-count")

                self.software_monitor_count = YLeaf(YType.uint64, "software-monitor-count")

                self.software_permit_count = YLeaf(YType.uint64, "software-permit-count")

                self.total_deny_count = YLeaf(YType.uint64, "total-deny-count")

                self.total_permit_count = YLeaf(YType.uint64, "total-permit-count")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("src_sgt",
                                "dst_sgt",
                                "hardware_deny_count",
                                "hardware_monitor_count",
                                "hardware_permit_count",
                                "last_updated_time",
                                "monitor_mode",
                                "num_of_sgacl",
                                "policy_life_time",
                                "sgacl_name",
                                "software_deny_count",
                                "software_monitor_count",
                                "software_permit_count",
                                "total_deny_count",
                                "total_permit_count") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(TrustsecState.CtsRolebasedPolicies.CtsRolebasedPolicy, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(TrustsecState.CtsRolebasedPolicies.CtsRolebasedPolicy, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.src_sgt.is_set or
                    self.dst_sgt.is_set or
                    self.hardware_deny_count.is_set or
                    self.hardware_monitor_count.is_set or
                    self.hardware_permit_count.is_set or
                    self.last_updated_time.is_set or
                    self.monitor_mode.is_set or
                    self.num_of_sgacl.is_set or
                    self.policy_life_time.is_set or
                    self.sgacl_name.is_set or
                    self.software_deny_count.is_set or
                    self.software_monitor_count.is_set or
                    self.software_permit_count.is_set or
                    self.total_deny_count.is_set or
                    self.total_permit_count.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.src_sgt.yfilter != YFilter.not_set or
                    self.dst_sgt.yfilter != YFilter.not_set or
                    self.hardware_deny_count.yfilter != YFilter.not_set or
                    self.hardware_monitor_count.yfilter != YFilter.not_set or
                    self.hardware_permit_count.yfilter != YFilter.not_set or
                    self.last_updated_time.yfilter != YFilter.not_set or
                    self.monitor_mode.yfilter != YFilter.not_set or
                    self.num_of_sgacl.yfilter != YFilter.not_set or
                    self.policy_life_time.yfilter != YFilter.not_set or
                    self.sgacl_name.yfilter != YFilter.not_set or
                    self.software_deny_count.yfilter != YFilter.not_set or
                    self.software_monitor_count.yfilter != YFilter.not_set or
                    self.software_permit_count.yfilter != YFilter.not_set or
                    self.total_deny_count.yfilter != YFilter.not_set or
                    self.total_permit_count.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cts-rolebased-policy" + "[src-sgt='" + self.src_sgt.get() + "']" + "[dst-sgt='" + self.dst_sgt.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XE-trustsec-oper:trustsec-state/cts-rolebased-policies/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.src_sgt.is_set or self.src_sgt.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.src_sgt.get_name_leafdata())
                if (self.dst_sgt.is_set or self.dst_sgt.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dst_sgt.get_name_leafdata())
                if (self.hardware_deny_count.is_set or self.hardware_deny_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hardware_deny_count.get_name_leafdata())
                if (self.hardware_monitor_count.is_set or self.hardware_monitor_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hardware_monitor_count.get_name_leafdata())
                if (self.hardware_permit_count.is_set or self.hardware_permit_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hardware_permit_count.get_name_leafdata())
                if (self.last_updated_time.is_set or self.last_updated_time.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.last_updated_time.get_name_leafdata())
                if (self.monitor_mode.is_set or self.monitor_mode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.monitor_mode.get_name_leafdata())
                if (self.num_of_sgacl.is_set or self.num_of_sgacl.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.num_of_sgacl.get_name_leafdata())
                if (self.policy_life_time.is_set or self.policy_life_time.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.policy_life_time.get_name_leafdata())
                if (self.sgacl_name.is_set or self.sgacl_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sgacl_name.get_name_leafdata())
                if (self.software_deny_count.is_set or self.software_deny_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.software_deny_count.get_name_leafdata())
                if (self.software_monitor_count.is_set or self.software_monitor_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.software_monitor_count.get_name_leafdata())
                if (self.software_permit_count.is_set or self.software_permit_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.software_permit_count.get_name_leafdata())
                if (self.total_deny_count.is_set or self.total_deny_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.total_deny_count.get_name_leafdata())
                if (self.total_permit_count.is_set or self.total_permit_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.total_permit_count.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "src-sgt" or name == "dst-sgt" or name == "hardware-deny-count" or name == "hardware-monitor-count" or name == "hardware-permit-count" or name == "last-updated-time" or name == "monitor-mode" or name == "num-of-sgacl" or name == "policy-life-time" or name == "sgacl-name" or name == "software-deny-count" or name == "software-monitor-count" or name == "software-permit-count" or name == "total-deny-count" or name == "total-permit-count"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "src-sgt"):
                    self.src_sgt = value
                    self.src_sgt.value_namespace = name_space
                    self.src_sgt.value_namespace_prefix = name_space_prefix
                if(value_path == "dst-sgt"):
                    self.dst_sgt = value
                    self.dst_sgt.value_namespace = name_space
                    self.dst_sgt.value_namespace_prefix = name_space_prefix
                if(value_path == "hardware-deny-count"):
                    self.hardware_deny_count = value
                    self.hardware_deny_count.value_namespace = name_space
                    self.hardware_deny_count.value_namespace_prefix = name_space_prefix
                if(value_path == "hardware-monitor-count"):
                    self.hardware_monitor_count = value
                    self.hardware_monitor_count.value_namespace = name_space
                    self.hardware_monitor_count.value_namespace_prefix = name_space_prefix
                if(value_path == "hardware-permit-count"):
                    self.hardware_permit_count = value
                    self.hardware_permit_count.value_namespace = name_space
                    self.hardware_permit_count.value_namespace_prefix = name_space_prefix
                if(value_path == "last-updated-time"):
                    self.last_updated_time = value
                    self.last_updated_time.value_namespace = name_space
                    self.last_updated_time.value_namespace_prefix = name_space_prefix
                if(value_path == "monitor-mode"):
                    self.monitor_mode = value
                    self.monitor_mode.value_namespace = name_space
                    self.monitor_mode.value_namespace_prefix = name_space_prefix
                if(value_path == "num-of-sgacl"):
                    self.num_of_sgacl = value
                    self.num_of_sgacl.value_namespace = name_space
                    self.num_of_sgacl.value_namespace_prefix = name_space_prefix
                if(value_path == "policy-life-time"):
                    self.policy_life_time = value
                    self.policy_life_time.value_namespace = name_space
                    self.policy_life_time.value_namespace_prefix = name_space_prefix
                if(value_path == "sgacl-name"):
                    self.sgacl_name = value
                    self.sgacl_name.value_namespace = name_space
                    self.sgacl_name.value_namespace_prefix = name_space_prefix
                if(value_path == "software-deny-count"):
                    self.software_deny_count = value
                    self.software_deny_count.value_namespace = name_space
                    self.software_deny_count.value_namespace_prefix = name_space_prefix
                if(value_path == "software-monitor-count"):
                    self.software_monitor_count = value
                    self.software_monitor_count.value_namespace = name_space
                    self.software_monitor_count.value_namespace_prefix = name_space_prefix
                if(value_path == "software-permit-count"):
                    self.software_permit_count = value
                    self.software_permit_count.value_namespace = name_space
                    self.software_permit_count.value_namespace_prefix = name_space_prefix
                if(value_path == "total-deny-count"):
                    self.total_deny_count = value
                    self.total_deny_count.value_namespace = name_space
                    self.total_deny_count.value_namespace_prefix = name_space_prefix
                if(value_path == "total-permit-count"):
                    self.total_permit_count = value
                    self.total_permit_count.value_namespace = name_space
                    self.total_permit_count.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cts_rolebased_policy:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cts_rolebased_policy:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cts-rolebased-policies" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XE-trustsec-oper:trustsec-state/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cts-rolebased-policy"):
                for c in self.cts_rolebased_policy:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = TrustsecState.CtsRolebasedPolicies.CtsRolebasedPolicy()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cts_rolebased_policy.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cts-rolebased-policy"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class CtsSxpConnections(Entity):
        """
        Trustsec SXP connection is used between Cisco devices
        to propagate Security Group Tags from one device to 
        another device. One of the device will be in Speaker 
        mode or Listener mode or both the devices can be in
        both the connection modes
        
        .. attribute:: cts_sxp_connection
        
        	Trustsec SXP connection information from a device can be retrieved with the SXP connection peer IP address. Only IPv4 address as Peer IP and default VRF instance in device is supported currently
        	**type**\: list of    :py:class:`CtsSxpConnection <ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper.TrustsecState.CtsSxpConnections.CtsSxpConnection>`
        
        

        """

        _prefix = 'trustsec-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            super(TrustsecState.CtsSxpConnections, self).__init__()

            self.yang_name = "cts-sxp-connections"
            self.yang_parent_name = "trustsec-state"

            self.cts_sxp_connection = YList(self)

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
                        super(TrustsecState.CtsSxpConnections, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(TrustsecState.CtsSxpConnections, self).__setattr__(name, value)


        class CtsSxpConnection(Entity):
            """
            Trustsec SXP connection information from a device
            can be retrieved with the SXP connection peer IP
            address. Only IPv4 address as Peer IP and default
            VRF instance in device is supported currently
            
            .. attribute:: peer_ip  <key>
            
            	IP\-Address information of the peer of an SXP connection in this device. Only IPv4 address is currently supported
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: vrf_name  <key>
            
            	vrf\-name string of the VRF instance in this device, to which the peer of an SXP connection belongs to. Only default VRF is supported currently which is indicated by empty string
            	**type**\:  str
            
            .. attribute:: listener_duration
            
            	Duration of the SXP listener of the SXP connection in this device. This information is valid Only if the local mode of the SXP connection is Listener
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: listener_state
            
            	SXP listener state information of the SXP  connection in this device. This information is valid only if the local mode of the SXP connection in the device is Listener
            	**type**\:   :py:class:`SxpConState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper.SxpConState>`
            
            .. attribute:: local_mode
            
            	SXP connection mode of this device for the SXP connection with the given peer
            	**type**\:   :py:class:`SxpConMode <ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper.SxpConMode>`
            
            .. attribute:: source_ip
            
            	Source IP\-Address of the SXP connection in this device for the given peer IP\-Address
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: speaker_duration
            
            	Duration of the SXP speaker of the SXP connection in this device. This information is valid only if the local mode of the SXP connection is Speaker
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: speaker_state
            
            	SXP speaker state information of the SXP connection in this device. This information is valid only if the local mode of the SXP connection in this device is Speaker
            	**type**\:   :py:class:`SxpConState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper.SxpConState>`
            
            

            """

            _prefix = 'trustsec-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(TrustsecState.CtsSxpConnections.CtsSxpConnection, self).__init__()

                self.yang_name = "cts-sxp-connection"
                self.yang_parent_name = "cts-sxp-connections"

                self.peer_ip = YLeaf(YType.str, "peer-ip")

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.listener_duration = YLeaf(YType.uint64, "listener-duration")

                self.listener_state = YLeaf(YType.enumeration, "listener-state")

                self.local_mode = YLeaf(YType.enumeration, "local-mode")

                self.source_ip = YLeaf(YType.str, "source-ip")

                self.speaker_duration = YLeaf(YType.uint64, "speaker-duration")

                self.speaker_state = YLeaf(YType.enumeration, "speaker-state")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("peer_ip",
                                "vrf_name",
                                "listener_duration",
                                "listener_state",
                                "local_mode",
                                "source_ip",
                                "speaker_duration",
                                "speaker_state") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(TrustsecState.CtsSxpConnections.CtsSxpConnection, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(TrustsecState.CtsSxpConnections.CtsSxpConnection, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.peer_ip.is_set or
                    self.vrf_name.is_set or
                    self.listener_duration.is_set or
                    self.listener_state.is_set or
                    self.local_mode.is_set or
                    self.source_ip.is_set or
                    self.speaker_duration.is_set or
                    self.speaker_state.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.peer_ip.yfilter != YFilter.not_set or
                    self.vrf_name.yfilter != YFilter.not_set or
                    self.listener_duration.yfilter != YFilter.not_set or
                    self.listener_state.yfilter != YFilter.not_set or
                    self.local_mode.yfilter != YFilter.not_set or
                    self.source_ip.yfilter != YFilter.not_set or
                    self.speaker_duration.yfilter != YFilter.not_set or
                    self.speaker_state.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cts-sxp-connection" + "[peer-ip='" + self.peer_ip.get() + "']" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XE-trustsec-oper:trustsec-state/cts-sxp-connections/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.peer_ip.is_set or self.peer_ip.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.peer_ip.get_name_leafdata())
                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_name.get_name_leafdata())
                if (self.listener_duration.is_set or self.listener_duration.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.listener_duration.get_name_leafdata())
                if (self.listener_state.is_set or self.listener_state.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.listener_state.get_name_leafdata())
                if (self.local_mode.is_set or self.local_mode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.local_mode.get_name_leafdata())
                if (self.source_ip.is_set or self.source_ip.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.source_ip.get_name_leafdata())
                if (self.speaker_duration.is_set or self.speaker_duration.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.speaker_duration.get_name_leafdata())
                if (self.speaker_state.is_set or self.speaker_state.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.speaker_state.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "peer-ip" or name == "vrf-name" or name == "listener-duration" or name == "listener-state" or name == "local-mode" or name == "source-ip" or name == "speaker-duration" or name == "speaker-state"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "peer-ip"):
                    self.peer_ip = value
                    self.peer_ip.value_namespace = name_space
                    self.peer_ip.value_namespace_prefix = name_space_prefix
                if(value_path == "vrf-name"):
                    self.vrf_name = value
                    self.vrf_name.value_namespace = name_space
                    self.vrf_name.value_namespace_prefix = name_space_prefix
                if(value_path == "listener-duration"):
                    self.listener_duration = value
                    self.listener_duration.value_namespace = name_space
                    self.listener_duration.value_namespace_prefix = name_space_prefix
                if(value_path == "listener-state"):
                    self.listener_state = value
                    self.listener_state.value_namespace = name_space
                    self.listener_state.value_namespace_prefix = name_space_prefix
                if(value_path == "local-mode"):
                    self.local_mode = value
                    self.local_mode.value_namespace = name_space
                    self.local_mode.value_namespace_prefix = name_space_prefix
                if(value_path == "source-ip"):
                    self.source_ip = value
                    self.source_ip.value_namespace = name_space
                    self.source_ip.value_namespace_prefix = name_space_prefix
                if(value_path == "speaker-duration"):
                    self.speaker_duration = value
                    self.speaker_duration.value_namespace = name_space
                    self.speaker_duration.value_namespace_prefix = name_space_prefix
                if(value_path == "speaker-state"):
                    self.speaker_state = value
                    self.speaker_state.value_namespace = name_space
                    self.speaker_state.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cts_sxp_connection:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cts_sxp_connection:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cts-sxp-connections" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XE-trustsec-oper:trustsec-state/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cts-sxp-connection"):
                for c in self.cts_sxp_connection:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = TrustsecState.CtsSxpConnections.CtsSxpConnection()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cts_sxp_connection.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cts-sxp-connection"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.cts_rolebased_policies is not None and self.cts_rolebased_policies.has_data()) or
            (self.cts_rolebased_sgtmaps is not None and self.cts_rolebased_sgtmaps.has_data()) or
            (self.cts_sxp_connections is not None and self.cts_sxp_connections.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cts_rolebased_policies is not None and self.cts_rolebased_policies.has_operation()) or
            (self.cts_rolebased_sgtmaps is not None and self.cts_rolebased_sgtmaps.has_operation()) or
            (self.cts_sxp_connections is not None and self.cts_sxp_connections.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XE-trustsec-oper:trustsec-state" + path_buffer

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

        if (child_yang_name == "cts-rolebased-policies"):
            if (self.cts_rolebased_policies is None):
                self.cts_rolebased_policies = TrustsecState.CtsRolebasedPolicies()
                self.cts_rolebased_policies.parent = self
                self._children_name_map["cts_rolebased_policies"] = "cts-rolebased-policies"
            return self.cts_rolebased_policies

        if (child_yang_name == "cts-rolebased-sgtmaps"):
            if (self.cts_rolebased_sgtmaps is None):
                self.cts_rolebased_sgtmaps = TrustsecState.CtsRolebasedSgtmaps()
                self.cts_rolebased_sgtmaps.parent = self
                self._children_name_map["cts_rolebased_sgtmaps"] = "cts-rolebased-sgtmaps"
            return self.cts_rolebased_sgtmaps

        if (child_yang_name == "cts-sxp-connections"):
            if (self.cts_sxp_connections is None):
                self.cts_sxp_connections = TrustsecState.CtsSxpConnections()
                self.cts_sxp_connections.parent = self
                self._children_name_map["cts_sxp_connections"] = "cts-sxp-connections"
            return self.cts_sxp_connections

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cts-rolebased-policies" or name == "cts-rolebased-sgtmaps" or name == "cts-sxp-connections"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = TrustsecState()
        return self._top_entity


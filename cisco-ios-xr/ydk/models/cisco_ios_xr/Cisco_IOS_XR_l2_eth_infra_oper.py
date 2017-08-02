""" Cisco_IOS_XR_l2_eth_infra_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR l2\-eth\-infra package operational data.

This module contains definitions
for the following management objects\:
  mac\-accounting\: MAC accounting operational data
  vlan\: vlan
  ethernet\-encapsulation\: ethernet encapsulation

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class EfpPayloadEtype(Enum):
    """
    EfpPayloadEtype

    Payload ethertype match

    .. data:: payload_ethertype_any = 0

    	Any

    .. data:: payload_ethertype_ip = 1

    	IP

    .. data:: payload_ethertype_pppoe = 2

    	PPPoE

    """

    payload_ethertype_any = Enum.YLeaf(0, "payload-ethertype-any")

    payload_ethertype_ip = Enum.YLeaf(1, "payload-ethertype-ip")

    payload_ethertype_pppoe = Enum.YLeaf(2, "payload-ethertype-pppoe")


class EfpTagEtype(Enum):
    """
    EfpTagEtype

    Tag ethertype

    .. data:: untagged = 0

    	Untagged

    .. data:: dot1q = 33024

    	Dot1Q

    .. data:: dot1ad = 34984

    	Dot1ad

    """

    untagged = Enum.YLeaf(0, "untagged")

    dot1q = Enum.YLeaf(33024, "dot1q")

    dot1ad = Enum.YLeaf(34984, "dot1ad")


class EfpTagPriority(Enum):
    """
    EfpTagPriority

    Priority

    .. data:: priority0 = 0

    	Priority 0

    .. data:: priority1 = 1

    	Priority 1

    .. data:: priority2 = 2

    	Priority 2

    .. data:: priority3 = 3

    	Priority 3

    .. data:: priority4 = 4

    	Priority 4

    .. data:: priority5 = 5

    	Priority 5

    .. data:: priority6 = 6

    	Priority 6

    .. data:: priority7 = 7

    	Priority 7

    .. data:: priority_any = 8

    	Any priority

    """

    priority0 = Enum.YLeaf(0, "priority0")

    priority1 = Enum.YLeaf(1, "priority1")

    priority2 = Enum.YLeaf(2, "priority2")

    priority3 = Enum.YLeaf(3, "priority3")

    priority4 = Enum.YLeaf(4, "priority4")

    priority5 = Enum.YLeaf(5, "priority5")

    priority6 = Enum.YLeaf(6, "priority6")

    priority7 = Enum.YLeaf(7, "priority7")

    priority_any = Enum.YLeaf(8, "priority-any")


class EthCapsUcastMacMode(Enum):
    """
    EthCapsUcastMacMode

    Eth caps ucast mac mode

    .. data:: reserved = 0

    	Reserved

    .. data:: permit = 1

    	Permit

    """

    reserved = Enum.YLeaf(0, "reserved")

    permit = Enum.YLeaf(1, "permit")


class EthFiltering(Enum):
    """
    EthFiltering

    Ethernet frame filtering

    .. data:: no_filtering = 0

    	No IEEE 802.1Q/802.1ad/MAC relay multicast MAC

    	address filtering

    .. data:: dot1q_filtering = 1

    	IEEE 802.1q C-VLAN filtering

    .. data:: dot1ad_filtering = 2

    	IEEE 802.1ad S-VLAN filtering

    .. data:: two_port_mac_relay_filtering = 3

    	IEEE 802.1aj 2-Port MAC relay filtering

    """

    no_filtering = Enum.YLeaf(0, "no-filtering")

    dot1q_filtering = Enum.YLeaf(1, "dot1q-filtering")

    dot1ad_filtering = Enum.YLeaf(2, "dot1ad-filtering")

    two_port_mac_relay_filtering = Enum.YLeaf(3, "two-port-mac-relay-filtering")


class ImStateEnum(Enum):
    """
    ImStateEnum

    Im state enum

    .. data:: im_state_not_ready = 0

    	im state not ready

    .. data:: im_state_admin_down = 1

    	im state admin down

    .. data:: im_state_down = 2

    	im state down

    .. data:: im_state_up = 3

    	im state up

    .. data:: im_state_shutdown = 4

    	im state shutdown

    .. data:: im_state_err_disable = 5

    	im state err disable

    .. data:: im_state_down_immediate = 6

    	im state down immediate

    .. data:: im_state_down_immediate_admin = 7

    	im state down immediate admin

    .. data:: im_state_down_graceful = 8

    	im state down graceful

    .. data:: im_state_begin_shutdown = 9

    	im state begin shutdown

    .. data:: im_state_end_shutdown = 10

    	im state end shutdown

    .. data:: im_state_begin_error_disable = 11

    	im state begin error disable

    .. data:: im_state_end_error_disable = 12

    	im state end error disable

    .. data:: im_state_begin_down_graceful = 13

    	im state begin down graceful

    .. data:: im_state_reset = 14

    	im state reset

    .. data:: im_state_operational = 15

    	im state operational

    .. data:: im_state_not_operational = 16

    	im state not operational

    .. data:: im_state_unknown = 17

    	im state unknown

    .. data:: im_state_last = 18

    	im state last

    """

    im_state_not_ready = Enum.YLeaf(0, "im-state-not-ready")

    im_state_admin_down = Enum.YLeaf(1, "im-state-admin-down")

    im_state_down = Enum.YLeaf(2, "im-state-down")

    im_state_up = Enum.YLeaf(3, "im-state-up")

    im_state_shutdown = Enum.YLeaf(4, "im-state-shutdown")

    im_state_err_disable = Enum.YLeaf(5, "im-state-err-disable")

    im_state_down_immediate = Enum.YLeaf(6, "im-state-down-immediate")

    im_state_down_immediate_admin = Enum.YLeaf(7, "im-state-down-immediate-admin")

    im_state_down_graceful = Enum.YLeaf(8, "im-state-down-graceful")

    im_state_begin_shutdown = Enum.YLeaf(9, "im-state-begin-shutdown")

    im_state_end_shutdown = Enum.YLeaf(10, "im-state-end-shutdown")

    im_state_begin_error_disable = Enum.YLeaf(11, "im-state-begin-error-disable")

    im_state_end_error_disable = Enum.YLeaf(12, "im-state-end-error-disable")

    im_state_begin_down_graceful = Enum.YLeaf(13, "im-state-begin-down-graceful")

    im_state_reset = Enum.YLeaf(14, "im-state-reset")

    im_state_operational = Enum.YLeaf(15, "im-state-operational")

    im_state_not_operational = Enum.YLeaf(16, "im-state-not-operational")

    im_state_unknown = Enum.YLeaf(17, "im-state-unknown")

    im_state_last = Enum.YLeaf(18, "im-state-last")


class VlanEncaps(Enum):
    """
    VlanEncaps

    VLAN encapsulation

    .. data:: no_encapsulation = 0

    	No encapsulation

    .. data:: dot1q = 1

    	IEEE 802.1Q encapsulation

    .. data:: qinq = 2

    	Double 802.1Q encapsulation

    .. data:: qin_any = 3

    	Double 802.1Q wildcarded encapsulation

    .. data:: dot1q_native = 4

    	IEEE 802.1Q native VLAN encapsulation

    .. data:: dot1ad = 5

    	IEEE 802.1ad encapsulation

    .. data:: dot1ad_native = 6

    	IEEE 802.1ad native VLAN encapsulation

    .. data:: service_instance = 7

    	Ethernet Service Instance

    .. data:: dot1ad_dot1q = 8

    	IEEE 802.1ad 802.1Q encapsulation

    .. data:: dot1ad_any = 9

    	IEEE 802.1ad wildcard 802.1Q encapsulation

    """

    no_encapsulation = Enum.YLeaf(0, "no-encapsulation")

    dot1q = Enum.YLeaf(1, "dot1q")

    qinq = Enum.YLeaf(2, "qinq")

    qin_any = Enum.YLeaf(3, "qin-any")

    dot1q_native = Enum.YLeaf(4, "dot1q-native")

    dot1ad = Enum.YLeaf(5, "dot1ad")

    dot1ad_native = Enum.YLeaf(6, "dot1ad-native")

    service_instance = Enum.YLeaf(7, "service-instance")

    dot1ad_dot1q = Enum.YLeaf(8, "dot1ad-dot1q")

    dot1ad_any = Enum.YLeaf(9, "dot1ad-any")


class VlanQinqOuterEtype(Enum):
    """
    VlanQinqOuterEtype

    QinQ Outer Tag Ethertype

    .. data:: ether_type8100 = 33024

    	Dot1Q (0x8100)

    .. data:: ether_type9100 = 37120

    	0x9100

    .. data:: ether_type9200 = 37376

    	0x9200

    """

    ether_type8100 = Enum.YLeaf(33024, "ether-type8100")

    ether_type9100 = Enum.YLeaf(37120, "ether-type9100")

    ether_type9200 = Enum.YLeaf(37376, "ether-type9200")


class VlanService(Enum):
    """
    VlanService

    Layer 2 vs. Layer 3 Terminated Service

    .. data:: vlan_service_l2 = 1

    	Layer 2 Transport Service

    .. data:: vlan_service_l3 = 2

    	Layer 3 Terminated Service

    """

    vlan_service_l2 = Enum.YLeaf(1, "vlan-service-l2")

    vlan_service_l3 = Enum.YLeaf(2, "vlan-service-l3")



class MacAccounting(Entity):
    """
    MAC accounting operational data
    
    .. attribute:: interfaces
    
    	MAC accounting interface table in MIB lexicographic order
    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.MacAccounting.Interfaces>`
    
    

    """

    _prefix = 'l2-eth-infra-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(MacAccounting, self).__init__()
        self._top_entity = None

        self.yang_name = "mac-accounting"
        self.yang_parent_name = "Cisco-IOS-XR-l2-eth-infra-oper"

        self.interfaces = MacAccounting.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._children_yang_names.add("interfaces")


    class Interfaces(Entity):
        """
        MAC accounting interface table in MIB
        lexicographic order
        
        .. attribute:: interface
        
        	Operational data and statistics for an interface configured with MAC accounting enabled
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.MacAccounting.Interfaces.Interface>`
        
        

        """

        _prefix = 'l2-eth-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(MacAccounting.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "mac-accounting"

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
                        super(MacAccounting.Interfaces, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MacAccounting.Interfaces, self).__setattr__(name, value)


        class Interface(Entity):
            """
            Operational data and statistics for an
            interface configured with MAC accounting
            enabled
            
            .. attribute:: interface_name  <key>
            
            	The interface name
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: egress_statistic
            
            	Egress MAC accounting statistics
            	**type**\: list of    :py:class:`EgressStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.MacAccounting.Interfaces.Interface.EgressStatistic>`
            
            .. attribute:: ingress_statistic
            
            	Ingress MAC accounting statistics
            	**type**\: list of    :py:class:`IngressStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.MacAccounting.Interfaces.Interface.IngressStatistic>`
            
            .. attribute:: state
            
            	MAC accounting state for the interface
            	**type**\:   :py:class:`State <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.MacAccounting.Interfaces.Interface.State>`
            
            

            """

            _prefix = 'l2-eth-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(MacAccounting.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.state = MacAccounting.Interfaces.Interface.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._children_yang_names.add("state")

                self.egress_statistic = YList(self)
                self.ingress_statistic = YList(self)

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
                            super(MacAccounting.Interfaces.Interface, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MacAccounting.Interfaces.Interface, self).__setattr__(name, value)


            class State(Entity):
                """
                MAC accounting state for the interface
                
                .. attribute:: is_egress_enabled
                
                	MAC accounting on on egress
                	**type**\:  bool
                
                .. attribute:: is_ingress_enabled
                
                	MAC accounting on on ingress
                	**type**\:  bool
                
                .. attribute:: number_available_egress
                
                	MAC accounting entries available on egress
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: number_available_ingress
                
                	MAC accounting entries available on ingress
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: number_available_on_node
                
                	MAC accountng entries available across the node
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'l2-eth-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MacAccounting.Interfaces.Interface.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "interface"

                    self.is_egress_enabled = YLeaf(YType.boolean, "is-egress-enabled")

                    self.is_ingress_enabled = YLeaf(YType.boolean, "is-ingress-enabled")

                    self.number_available_egress = YLeaf(YType.uint32, "number-available-egress")

                    self.number_available_ingress = YLeaf(YType.uint32, "number-available-ingress")

                    self.number_available_on_node = YLeaf(YType.uint32, "number-available-on-node")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("is_egress_enabled",
                                    "is_ingress_enabled",
                                    "number_available_egress",
                                    "number_available_ingress",
                                    "number_available_on_node") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MacAccounting.Interfaces.Interface.State, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MacAccounting.Interfaces.Interface.State, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.is_egress_enabled.is_set or
                        self.is_ingress_enabled.is_set or
                        self.number_available_egress.is_set or
                        self.number_available_ingress.is_set or
                        self.number_available_on_node.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.is_egress_enabled.yfilter != YFilter.not_set or
                        self.is_ingress_enabled.yfilter != YFilter.not_set or
                        self.number_available_egress.yfilter != YFilter.not_set or
                        self.number_available_ingress.yfilter != YFilter.not_set or
                        self.number_available_on_node.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "state" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.is_egress_enabled.is_set or self.is_egress_enabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_egress_enabled.get_name_leafdata())
                    if (self.is_ingress_enabled.is_set or self.is_ingress_enabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_ingress_enabled.get_name_leafdata())
                    if (self.number_available_egress.is_set or self.number_available_egress.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.number_available_egress.get_name_leafdata())
                    if (self.number_available_ingress.is_set or self.number_available_ingress.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.number_available_ingress.get_name_leafdata())
                    if (self.number_available_on_node.is_set or self.number_available_on_node.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.number_available_on_node.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "is-egress-enabled" or name == "is-ingress-enabled" or name == "number-available-egress" or name == "number-available-ingress" or name == "number-available-on-node"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "is-egress-enabled"):
                        self.is_egress_enabled = value
                        self.is_egress_enabled.value_namespace = name_space
                        self.is_egress_enabled.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-ingress-enabled"):
                        self.is_ingress_enabled = value
                        self.is_ingress_enabled.value_namespace = name_space
                        self.is_ingress_enabled.value_namespace_prefix = name_space_prefix
                    if(value_path == "number-available-egress"):
                        self.number_available_egress = value
                        self.number_available_egress.value_namespace = name_space
                        self.number_available_egress.value_namespace_prefix = name_space_prefix
                    if(value_path == "number-available-ingress"):
                        self.number_available_ingress = value
                        self.number_available_ingress.value_namespace = name_space
                        self.number_available_ingress.value_namespace_prefix = name_space_prefix
                    if(value_path == "number-available-on-node"):
                        self.number_available_on_node = value
                        self.number_available_on_node.value_namespace = name_space
                        self.number_available_on_node.value_namespace_prefix = name_space_prefix


            class IngressStatistic(Entity):
                """
                Ingress MAC accounting statistics
                
                .. attribute:: bytes
                
                	Number of bytes counted
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: mac_address
                
                	48bit MAC address
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: packets
                
                	Number of packets counted
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'l2-eth-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MacAccounting.Interfaces.Interface.IngressStatistic, self).__init__()

                    self.yang_name = "ingress-statistic"
                    self.yang_parent_name = "interface"

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.mac_address = YLeaf(YType.str, "mac-address")

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
                                    "mac_address",
                                    "packets") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MacAccounting.Interfaces.Interface.IngressStatistic, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MacAccounting.Interfaces.Interface.IngressStatistic, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.bytes.is_set or
                        self.mac_address.is_set or
                        self.packets.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bytes.yfilter != YFilter.not_set or
                        self.mac_address.yfilter != YFilter.not_set or
                        self.packets.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ingress-statistic" + path_buffer

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
                    if (self.mac_address.is_set or self.mac_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mac_address.get_name_leafdata())
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
                    if(name == "bytes" or name == "mac-address" or name == "packets"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bytes"):
                        self.bytes = value
                        self.bytes.value_namespace = name_space
                        self.bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "mac-address"):
                        self.mac_address = value
                        self.mac_address.value_namespace = name_space
                        self.mac_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "packets"):
                        self.packets = value
                        self.packets.value_namespace = name_space
                        self.packets.value_namespace_prefix = name_space_prefix


            class EgressStatistic(Entity):
                """
                Egress MAC accounting statistics
                
                .. attribute:: bytes
                
                	Number of bytes counted
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: mac_address
                
                	48bit MAC address
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: packets
                
                	Number of packets counted
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'l2-eth-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MacAccounting.Interfaces.Interface.EgressStatistic, self).__init__()

                    self.yang_name = "egress-statistic"
                    self.yang_parent_name = "interface"

                    self.bytes = YLeaf(YType.uint64, "bytes")

                    self.mac_address = YLeaf(YType.str, "mac-address")

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
                                    "mac_address",
                                    "packets") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MacAccounting.Interfaces.Interface.EgressStatistic, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MacAccounting.Interfaces.Interface.EgressStatistic, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.bytes.is_set or
                        self.mac_address.is_set or
                        self.packets.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bytes.yfilter != YFilter.not_set or
                        self.mac_address.yfilter != YFilter.not_set or
                        self.packets.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "egress-statistic" + path_buffer

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
                    if (self.mac_address.is_set or self.mac_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mac_address.get_name_leafdata())
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
                    if(name == "bytes" or name == "mac-address" or name == "packets"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bytes"):
                        self.bytes = value
                        self.bytes.value_namespace = name_space
                        self.bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "mac-address"):
                        self.mac_address = value
                        self.mac_address.value_namespace = name_space
                        self.mac_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "packets"):
                        self.packets = value
                        self.packets.value_namespace = name_space
                        self.packets.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.egress_statistic:
                    if (c.has_data()):
                        return True
                for c in self.ingress_statistic:
                    if (c.has_data()):
                        return True
                return (
                    self.interface_name.is_set or
                    (self.state is not None and self.state.has_data()))

            def has_operation(self):
                for c in self.egress_statistic:
                    if (c.has_operation()):
                        return True
                for c in self.ingress_statistic:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.interface_name.yfilter != YFilter.not_set or
                    (self.state is not None and self.state.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-l2-eth-infra-oper:mac-accounting/interfaces/%s" % self.get_segment_path()
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

                if (child_yang_name == "egress-statistic"):
                    for c in self.egress_statistic:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = MacAccounting.Interfaces.Interface.EgressStatistic()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.egress_statistic.append(c)
                    return c

                if (child_yang_name == "ingress-statistic"):
                    for c in self.ingress_statistic:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = MacAccounting.Interfaces.Interface.IngressStatistic()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.ingress_statistic.append(c)
                    return c

                if (child_yang_name == "state"):
                    if (self.state is None):
                        self.state = MacAccounting.Interfaces.Interface.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                    return self.state

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "egress-statistic" or name == "ingress-statistic" or name == "state" or name == "interface-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "interface-name"):
                    self.interface_name = value
                    self.interface_name.value_namespace = name_space
                    self.interface_name.value_namespace_prefix = name_space_prefix

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
                path_buffer = "Cisco-IOS-XR-l2-eth-infra-oper:mac-accounting/%s" % self.get_segment_path()
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
                c = MacAccounting.Interfaces.Interface()
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
        return (self.interfaces is not None and self.interfaces.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.interfaces is not None and self.interfaces.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-l2-eth-infra-oper:mac-accounting" + path_buffer

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
                self.interfaces = MacAccounting.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
            return self.interfaces

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "interfaces"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = MacAccounting()
        return self._top_entity

class Vlan(Entity):
    """
    vlan
    
    .. attribute:: nodes
    
    	Per node VLAN operational data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes>`
    
    

    """

    _prefix = 'l2-eth-infra-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Vlan, self).__init__()
        self._top_entity = None

        self.yang_name = "vlan"
        self.yang_parent_name = "Cisco-IOS-XR-l2-eth-infra-oper"

        self.nodes = Vlan.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        Per node VLAN operational data
        
        .. attribute:: node
        
        	The VLAN operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node>`
        
        

        """

        _prefix = 'l2-eth-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Vlan.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "vlan"

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
                        super(Vlan.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Vlan.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            The VLAN operational data for a particular node
            
            .. attribute:: node_id  <key>
            
            	The identifier for the node
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: interfaces
            
            	VLAN interface table (specific to this node)
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Interfaces>`
            
            .. attribute:: tag_allocations
            
            	VLAN tag allocation table (specific to this node)
            	**type**\:   :py:class:`TagAllocations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.TagAllocations>`
            
            .. attribute:: trunks
            
            	VLAN trunk table (specific to this node)
            	**type**\:   :py:class:`Trunks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Trunks>`
            
            

            """

            _prefix = 'l2-eth-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Vlan.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_id = YLeaf(YType.str, "node-id")

                self.interfaces = Vlan.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._children_yang_names.add("interfaces")

                self.tag_allocations = Vlan.Nodes.Node.TagAllocations()
                self.tag_allocations.parent = self
                self._children_name_map["tag_allocations"] = "tag-allocations"
                self._children_yang_names.add("tag-allocations")

                self.trunks = Vlan.Nodes.Node.Trunks()
                self.trunks.parent = self
                self._children_name_map["trunks"] = "trunks"
                self._children_yang_names.add("trunks")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("node_id") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Vlan.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Vlan.Nodes.Node, self).__setattr__(name, value)


            class Trunks(Entity):
                """
                VLAN trunk table (specific to this node)
                
                .. attribute:: trunk
                
                	Operational data for trunk interfaces configured with VLANs
                	**type**\: list of    :py:class:`Trunk <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Trunks.Trunk>`
                
                

                """

                _prefix = 'l2-eth-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Vlan.Nodes.Node.Trunks, self).__init__()

                    self.yang_name = "trunks"
                    self.yang_parent_name = "node"

                    self.trunk = YList(self)

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
                                super(Vlan.Nodes.Node.Trunks, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Vlan.Nodes.Node.Trunks, self).__setattr__(name, value)


                class Trunk(Entity):
                    """
                    Operational data for trunk interfaces
                    configured with VLANs
                    
                    .. attribute:: interface  <key>
                    
                    	The interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: dot1ad_count
                    
                    	Number of subinterfaces with 802.1ad outer tag
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_xr
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: layer2_sub_interfaces
                    
                    	Layer 2 Transport Subinterfaces
                    	**type**\:   :py:class:`Layer2SubInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces>`
                    
                    .. attribute:: layer3_sub_interfaces
                    
                    	Layer 3 Terminated Subinterfaces
                    	**type**\:   :py:class:`Layer3SubInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces>`
                    
                    .. attribute:: mac_filtering
                    
                    	IEEE 802.1Q/802.1ad multicast MAC address filtering
                    	**type**\:   :py:class:`EthFiltering <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EthFiltering>`
                    
                    .. attribute:: mtu
                    
                    	L2 MTU
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: qinq_outer_ether_type
                    
                    	QinQ Outer Tag Ether Type
                    	**type**\:   :py:class:`VlanQinqOuterEtype <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.VlanQinqOuterEtype>`
                    
                    .. attribute:: state
                    
                    	Interface state
                    	**type**\:   :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.ImStateEnum>`
                    
                    .. attribute:: untagged_interface
                    
                    	Interface/Sub\-interface handling untagged frames
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    

                    """

                    _prefix = 'l2-eth-infra-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Vlan.Nodes.Node.Trunks.Trunk, self).__init__()

                        self.yang_name = "trunk"
                        self.yang_parent_name = "trunks"

                        self.interface = YLeaf(YType.str, "interface")

                        self.dot1ad_count = YLeaf(YType.uint32, "dot1ad-count")

                        self.interface_xr = YLeaf(YType.str, "interface-xr")

                        self.mac_filtering = YLeaf(YType.enumeration, "mac-filtering")

                        self.mtu = YLeaf(YType.uint16, "mtu")

                        self.qinq_outer_ether_type = YLeaf(YType.enumeration, "qinq-outer-ether-type")

                        self.state = YLeaf(YType.enumeration, "state")

                        self.untagged_interface = YLeaf(YType.str, "untagged-interface")

                        self.layer2_sub_interfaces = Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces()
                        self.layer2_sub_interfaces.parent = self
                        self._children_name_map["layer2_sub_interfaces"] = "layer2-sub-interfaces"
                        self._children_yang_names.add("layer2-sub-interfaces")

                        self.layer3_sub_interfaces = Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces()
                        self.layer3_sub_interfaces.parent = self
                        self._children_name_map["layer3_sub_interfaces"] = "layer3-sub-interfaces"
                        self._children_yang_names.add("layer3-sub-interfaces")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface",
                                        "dot1ad_count",
                                        "interface_xr",
                                        "mac_filtering",
                                        "mtu",
                                        "qinq_outer_ether_type",
                                        "state",
                                        "untagged_interface") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Vlan.Nodes.Node.Trunks.Trunk, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Vlan.Nodes.Node.Trunks.Trunk, self).__setattr__(name, value)


                    class Layer2SubInterfaces(Entity):
                        """
                        Layer 2 Transport Subinterfaces
                        
                        .. attribute:: dot1q_count
                        
                        	Number of single tagged subinterfaces
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: qin_any_count
                        
                        	Number of double tagged subinterfaces with wildcarded inner tag
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: qin_q_count
                        
                        	Number of double tagged subinterfaces with explicit inner tag
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: state_counters
                        
                        	Numbers of subinterfaces up, down or administratively shut down
                        	**type**\:   :py:class:`StateCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces.StateCounters>`
                        
                        .. attribute:: total_count
                        
                        	Total number of Layer 2 subinterfaces configured
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: untagged_count
                        
                        	Number of subinterfaces without VLAN tag configuration
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'l2-eth-infra-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces, self).__init__()

                            self.yang_name = "layer2-sub-interfaces"
                            self.yang_parent_name = "trunk"

                            self.dot1q_count = YLeaf(YType.uint32, "dot1q-count")

                            self.qin_any_count = YLeaf(YType.uint32, "qin-any-count")

                            self.qin_q_count = YLeaf(YType.uint32, "qin-q-count")

                            self.total_count = YLeaf(YType.uint32, "total-count")

                            self.untagged_count = YLeaf(YType.uint32, "untagged-count")

                            self.state_counters = Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces.StateCounters()
                            self.state_counters.parent = self
                            self._children_name_map["state_counters"] = "state-counters"
                            self._children_yang_names.add("state-counters")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("dot1q_count",
                                            "qin_any_count",
                                            "qin_q_count",
                                            "total_count",
                                            "untagged_count") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces, self).__setattr__(name, value)


                        class StateCounters(Entity):
                            """
                            Numbers of subinterfaces up, down or
                            administratively shut down
                            
                            .. attribute:: admin_down
                            
                            	Number of subinterfaces which are administrativelyshutdown
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: down
                            
                            	Number of subinterfaces which are down
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: up
                            
                            	Number of subinterfaces which are up
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'l2-eth-infra-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces.StateCounters, self).__init__()

                                self.yang_name = "state-counters"
                                self.yang_parent_name = "layer2-sub-interfaces"

                                self.admin_down = YLeaf(YType.uint32, "admin-down")

                                self.down = YLeaf(YType.uint32, "down")

                                self.up = YLeaf(YType.uint32, "up")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("admin_down",
                                                "down",
                                                "up") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces.StateCounters, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces.StateCounters, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.admin_down.is_set or
                                    self.down.is_set or
                                    self.up.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.admin_down.yfilter != YFilter.not_set or
                                    self.down.yfilter != YFilter.not_set or
                                    self.up.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "state-counters" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.admin_down.is_set or self.admin_down.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.admin_down.get_name_leafdata())
                                if (self.down.is_set or self.down.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.down.get_name_leafdata())
                                if (self.up.is_set or self.up.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.up.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "admin-down" or name == "down" or name == "up"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "admin-down"):
                                    self.admin_down = value
                                    self.admin_down.value_namespace = name_space
                                    self.admin_down.value_namespace_prefix = name_space_prefix
                                if(value_path == "down"):
                                    self.down = value
                                    self.down.value_namespace = name_space
                                    self.down.value_namespace_prefix = name_space_prefix
                                if(value_path == "up"):
                                    self.up = value
                                    self.up.value_namespace = name_space
                                    self.up.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.dot1q_count.is_set or
                                self.qin_any_count.is_set or
                                self.qin_q_count.is_set or
                                self.total_count.is_set or
                                self.untagged_count.is_set or
                                (self.state_counters is not None and self.state_counters.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.dot1q_count.yfilter != YFilter.not_set or
                                self.qin_any_count.yfilter != YFilter.not_set or
                                self.qin_q_count.yfilter != YFilter.not_set or
                                self.total_count.yfilter != YFilter.not_set or
                                self.untagged_count.yfilter != YFilter.not_set or
                                (self.state_counters is not None and self.state_counters.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "layer2-sub-interfaces" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.dot1q_count.is_set or self.dot1q_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dot1q_count.get_name_leafdata())
                            if (self.qin_any_count.is_set or self.qin_any_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.qin_any_count.get_name_leafdata())
                            if (self.qin_q_count.is_set or self.qin_q_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.qin_q_count.get_name_leafdata())
                            if (self.total_count.is_set or self.total_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.total_count.get_name_leafdata())
                            if (self.untagged_count.is_set or self.untagged_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.untagged_count.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "state-counters"):
                                if (self.state_counters is None):
                                    self.state_counters = Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces.StateCounters()
                                    self.state_counters.parent = self
                                    self._children_name_map["state_counters"] = "state-counters"
                                return self.state_counters

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "state-counters" or name == "dot1q-count" or name == "qin-any-count" or name == "qin-q-count" or name == "total-count" or name == "untagged-count"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "dot1q-count"):
                                self.dot1q_count = value
                                self.dot1q_count.value_namespace = name_space
                                self.dot1q_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "qin-any-count"):
                                self.qin_any_count = value
                                self.qin_any_count.value_namespace = name_space
                                self.qin_any_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "qin-q-count"):
                                self.qin_q_count = value
                                self.qin_q_count.value_namespace = name_space
                                self.qin_q_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "total-count"):
                                self.total_count = value
                                self.total_count.value_namespace = name_space
                                self.total_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "untagged-count"):
                                self.untagged_count = value
                                self.untagged_count.value_namespace = name_space
                                self.untagged_count.value_namespace_prefix = name_space_prefix


                    class Layer3SubInterfaces(Entity):
                        """
                        Layer 3 Terminated Subinterfaces
                        
                        .. attribute:: dot1q_count
                        
                        	Number of single tagged subinterfaces
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: native_vlan
                        
                        	Native VLAN ID configured on trunk
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: qin_q_count
                        
                        	Number of double tagged subinterfaces
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: state_counters
                        
                        	Numbers of subinterfaces up, down or administratively shut down
                        	**type**\:   :py:class:`StateCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces.StateCounters>`
                        
                        .. attribute:: total_count
                        
                        	Total number of Layer 3 subinterfaces configured
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: untagged_count
                        
                        	Number of subinterfaces without VLAN tag configuration
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'l2-eth-infra-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces, self).__init__()

                            self.yang_name = "layer3-sub-interfaces"
                            self.yang_parent_name = "trunk"

                            self.dot1q_count = YLeaf(YType.uint32, "dot1q-count")

                            self.native_vlan = YLeaf(YType.uint16, "native-vlan")

                            self.qin_q_count = YLeaf(YType.uint32, "qin-q-count")

                            self.total_count = YLeaf(YType.uint32, "total-count")

                            self.untagged_count = YLeaf(YType.uint32, "untagged-count")

                            self.state_counters = Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces.StateCounters()
                            self.state_counters.parent = self
                            self._children_name_map["state_counters"] = "state-counters"
                            self._children_yang_names.add("state-counters")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("dot1q_count",
                                            "native_vlan",
                                            "qin_q_count",
                                            "total_count",
                                            "untagged_count") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces, self).__setattr__(name, value)


                        class StateCounters(Entity):
                            """
                            Numbers of subinterfaces up, down or
                            administratively shut down
                            
                            .. attribute:: admin_down
                            
                            	Number of subinterfaces which are administrativelyshutdown
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: down
                            
                            	Number of subinterfaces which are down
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: up
                            
                            	Number of subinterfaces which are up
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'l2-eth-infra-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces.StateCounters, self).__init__()

                                self.yang_name = "state-counters"
                                self.yang_parent_name = "layer3-sub-interfaces"

                                self.admin_down = YLeaf(YType.uint32, "admin-down")

                                self.down = YLeaf(YType.uint32, "down")

                                self.up = YLeaf(YType.uint32, "up")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("admin_down",
                                                "down",
                                                "up") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces.StateCounters, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces.StateCounters, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.admin_down.is_set or
                                    self.down.is_set or
                                    self.up.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.admin_down.yfilter != YFilter.not_set or
                                    self.down.yfilter != YFilter.not_set or
                                    self.up.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "state-counters" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.admin_down.is_set or self.admin_down.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.admin_down.get_name_leafdata())
                                if (self.down.is_set or self.down.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.down.get_name_leafdata())
                                if (self.up.is_set or self.up.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.up.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "admin-down" or name == "down" or name == "up"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "admin-down"):
                                    self.admin_down = value
                                    self.admin_down.value_namespace = name_space
                                    self.admin_down.value_namespace_prefix = name_space_prefix
                                if(value_path == "down"):
                                    self.down = value
                                    self.down.value_namespace = name_space
                                    self.down.value_namespace_prefix = name_space_prefix
                                if(value_path == "up"):
                                    self.up = value
                                    self.up.value_namespace = name_space
                                    self.up.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.dot1q_count.is_set or
                                self.native_vlan.is_set or
                                self.qin_q_count.is_set or
                                self.total_count.is_set or
                                self.untagged_count.is_set or
                                (self.state_counters is not None and self.state_counters.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.dot1q_count.yfilter != YFilter.not_set or
                                self.native_vlan.yfilter != YFilter.not_set or
                                self.qin_q_count.yfilter != YFilter.not_set or
                                self.total_count.yfilter != YFilter.not_set or
                                self.untagged_count.yfilter != YFilter.not_set or
                                (self.state_counters is not None and self.state_counters.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "layer3-sub-interfaces" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.dot1q_count.is_set or self.dot1q_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dot1q_count.get_name_leafdata())
                            if (self.native_vlan.is_set or self.native_vlan.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.native_vlan.get_name_leafdata())
                            if (self.qin_q_count.is_set or self.qin_q_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.qin_q_count.get_name_leafdata())
                            if (self.total_count.is_set or self.total_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.total_count.get_name_leafdata())
                            if (self.untagged_count.is_set or self.untagged_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.untagged_count.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "state-counters"):
                                if (self.state_counters is None):
                                    self.state_counters = Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces.StateCounters()
                                    self.state_counters.parent = self
                                    self._children_name_map["state_counters"] = "state-counters"
                                return self.state_counters

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "state-counters" or name == "dot1q-count" or name == "native-vlan" or name == "qin-q-count" or name == "total-count" or name == "untagged-count"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "dot1q-count"):
                                self.dot1q_count = value
                                self.dot1q_count.value_namespace = name_space
                                self.dot1q_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "native-vlan"):
                                self.native_vlan = value
                                self.native_vlan.value_namespace = name_space
                                self.native_vlan.value_namespace_prefix = name_space_prefix
                            if(value_path == "qin-q-count"):
                                self.qin_q_count = value
                                self.qin_q_count.value_namespace = name_space
                                self.qin_q_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "total-count"):
                                self.total_count = value
                                self.total_count.value_namespace = name_space
                                self.total_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "untagged-count"):
                                self.untagged_count = value
                                self.untagged_count.value_namespace = name_space
                                self.untagged_count.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.interface.is_set or
                            self.dot1ad_count.is_set or
                            self.interface_xr.is_set or
                            self.mac_filtering.is_set or
                            self.mtu.is_set or
                            self.qinq_outer_ether_type.is_set or
                            self.state.is_set or
                            self.untagged_interface.is_set or
                            (self.layer2_sub_interfaces is not None and self.layer2_sub_interfaces.has_data()) or
                            (self.layer3_sub_interfaces is not None and self.layer3_sub_interfaces.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface.yfilter != YFilter.not_set or
                            self.dot1ad_count.yfilter != YFilter.not_set or
                            self.interface_xr.yfilter != YFilter.not_set or
                            self.mac_filtering.yfilter != YFilter.not_set or
                            self.mtu.yfilter != YFilter.not_set or
                            self.qinq_outer_ether_type.yfilter != YFilter.not_set or
                            self.state.yfilter != YFilter.not_set or
                            self.untagged_interface.yfilter != YFilter.not_set or
                            (self.layer2_sub_interfaces is not None and self.layer2_sub_interfaces.has_operation()) or
                            (self.layer3_sub_interfaces is not None and self.layer3_sub_interfaces.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "trunk" + "[interface='" + self.interface.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface.get_name_leafdata())
                        if (self.dot1ad_count.is_set or self.dot1ad_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dot1ad_count.get_name_leafdata())
                        if (self.interface_xr.is_set or self.interface_xr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_xr.get_name_leafdata())
                        if (self.mac_filtering.is_set or self.mac_filtering.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mac_filtering.get_name_leafdata())
                        if (self.mtu.is_set or self.mtu.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mtu.get_name_leafdata())
                        if (self.qinq_outer_ether_type.is_set or self.qinq_outer_ether_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.qinq_outer_ether_type.get_name_leafdata())
                        if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.state.get_name_leafdata())
                        if (self.untagged_interface.is_set or self.untagged_interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.untagged_interface.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "layer2-sub-interfaces"):
                            if (self.layer2_sub_interfaces is None):
                                self.layer2_sub_interfaces = Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces()
                                self.layer2_sub_interfaces.parent = self
                                self._children_name_map["layer2_sub_interfaces"] = "layer2-sub-interfaces"
                            return self.layer2_sub_interfaces

                        if (child_yang_name == "layer3-sub-interfaces"):
                            if (self.layer3_sub_interfaces is None):
                                self.layer3_sub_interfaces = Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces()
                                self.layer3_sub_interfaces.parent = self
                                self._children_name_map["layer3_sub_interfaces"] = "layer3-sub-interfaces"
                            return self.layer3_sub_interfaces

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "layer2-sub-interfaces" or name == "layer3-sub-interfaces" or name == "interface" or name == "dot1ad-count" or name == "interface-xr" or name == "mac-filtering" or name == "mtu" or name == "qinq-outer-ether-type" or name == "state" or name == "untagged-interface"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface"):
                            self.interface = value
                            self.interface.value_namespace = name_space
                            self.interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "dot1ad-count"):
                            self.dot1ad_count = value
                            self.dot1ad_count.value_namespace = name_space
                            self.dot1ad_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-xr"):
                            self.interface_xr = value
                            self.interface_xr.value_namespace = name_space
                            self.interface_xr.value_namespace_prefix = name_space_prefix
                        if(value_path == "mac-filtering"):
                            self.mac_filtering = value
                            self.mac_filtering.value_namespace = name_space
                            self.mac_filtering.value_namespace_prefix = name_space_prefix
                        if(value_path == "mtu"):
                            self.mtu = value
                            self.mtu.value_namespace = name_space
                            self.mtu.value_namespace_prefix = name_space_prefix
                        if(value_path == "qinq-outer-ether-type"):
                            self.qinq_outer_ether_type = value
                            self.qinq_outer_ether_type.value_namespace = name_space
                            self.qinq_outer_ether_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "state"):
                            self.state = value
                            self.state.value_namespace = name_space
                            self.state.value_namespace_prefix = name_space_prefix
                        if(value_path == "untagged-interface"):
                            self.untagged_interface = value
                            self.untagged_interface.value_namespace = name_space
                            self.untagged_interface.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.trunk:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.trunk:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "trunks" + path_buffer

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

                    if (child_yang_name == "trunk"):
                        for c in self.trunk:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Vlan.Nodes.Node.Trunks.Trunk()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.trunk.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "trunk"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Interfaces(Entity):
                """
                VLAN interface table (specific to this node)
                
                .. attribute:: interface
                
                	Operational data for a sub\-interface configured with VLANs
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'l2-eth-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Vlan.Nodes.Node.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "node"

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
                                super(Vlan.Nodes.Node.Interfaces, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Vlan.Nodes.Node.Interfaces, self).__setattr__(name, value)


                class Interface(Entity):
                    """
                    Operational data for a sub\-interface
                    configured with VLANs
                    
                    .. attribute:: interface  <key>
                    
                    	The interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: encapsulation_details
                    
                    	Encapsulation type and tag stack
                    	**type**\:   :py:class:`EncapsulationDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails>`
                    
                    .. attribute:: interface_xr
                    
                    	Interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: mtu
                    
                    	L2 MTU
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: parent_interface
                    
                    	Parent interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: service
                    
                    	Service type
                    	**type**\:   :py:class:`VlanService <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.VlanService>`
                    
                    .. attribute:: state
                    
                    	Interface state
                    	**type**\:   :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.ImStateEnum>`
                    
                    .. attribute:: switched_mtu
                    
                    	L2 switched MTU
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'l2-eth-infra-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Vlan.Nodes.Node.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"

                        self.interface = YLeaf(YType.str, "interface")

                        self.interface_xr = YLeaf(YType.str, "interface-xr")

                        self.mtu = YLeaf(YType.uint16, "mtu")

                        self.parent_interface = YLeaf(YType.str, "parent-interface")

                        self.service = YLeaf(YType.enumeration, "service")

                        self.state = YLeaf(YType.enumeration, "state")

                        self.switched_mtu = YLeaf(YType.uint16, "switched-mtu")

                        self.encapsulation_details = Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails()
                        self.encapsulation_details.parent = self
                        self._children_name_map["encapsulation_details"] = "encapsulation-details"
                        self._children_yang_names.add("encapsulation-details")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface",
                                        "interface_xr",
                                        "mtu",
                                        "parent_interface",
                                        "service",
                                        "state",
                                        "switched_mtu") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Vlan.Nodes.Node.Interfaces.Interface, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Vlan.Nodes.Node.Interfaces.Interface, self).__setattr__(name, value)


                    class EncapsulationDetails(Entity):
                        """
                        Encapsulation type and tag stack
                        
                        .. attribute:: dot1ad_dot1q_stack
                        
                        	802.1ad 802.1Q stack value
                        	**type**\:   :py:class:`Dot1AdDot1QStack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Dot1AdDot1QStack>`
                        
                        .. attribute:: dot1ad_native_tag
                        
                        	802.1ad native tag value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: dot1ad_outer_tag
                        
                        	802.1ad Outer tag value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: dot1ad_tag
                        
                        	802.1ad tag value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: native_tag
                        
                        	Native tag value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: outer_tag
                        
                        	Outer tag value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: service_instance_details
                        
                        	Service Instance encapsulation
                        	**type**\:   :py:class:`ServiceInstanceDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails>`
                        
                        .. attribute:: stack
                        
                        	Stack value
                        	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Stack>`
                        
                        .. attribute:: tag
                        
                        	Tag value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: vlan_encapsulation
                        
                        	VLANEncapsulation
                        	**type**\:   :py:class:`VlanEncaps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.VlanEncaps>`
                        
                        

                        """

                        _prefix = 'l2-eth-infra-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails, self).__init__()

                            self.yang_name = "encapsulation-details"
                            self.yang_parent_name = "interface"

                            self.dot1ad_native_tag = YLeaf(YType.uint16, "dot1ad-native-tag")

                            self.dot1ad_outer_tag = YLeaf(YType.uint16, "dot1ad-outer-tag")

                            self.dot1ad_tag = YLeaf(YType.uint16, "dot1ad-tag")

                            self.native_tag = YLeaf(YType.uint16, "native-tag")

                            self.outer_tag = YLeaf(YType.uint16, "outer-tag")

                            self.tag = YLeaf(YType.uint16, "tag")

                            self.vlan_encapsulation = YLeaf(YType.enumeration, "vlan-encapsulation")

                            self.dot1ad_dot1q_stack = Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Dot1AdDot1QStack()
                            self.dot1ad_dot1q_stack.parent = self
                            self._children_name_map["dot1ad_dot1q_stack"] = "dot1ad-dot1q-stack"
                            self._children_yang_names.add("dot1ad-dot1q-stack")

                            self.service_instance_details = Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails()
                            self.service_instance_details.parent = self
                            self._children_name_map["service_instance_details"] = "service-instance-details"
                            self._children_yang_names.add("service-instance-details")

                            self.stack = Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Stack()
                            self.stack.parent = self
                            self._children_name_map["stack"] = "stack"
                            self._children_yang_names.add("stack")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("dot1ad_native_tag",
                                            "dot1ad_outer_tag",
                                            "dot1ad_tag",
                                            "native_tag",
                                            "outer_tag",
                                            "tag",
                                            "vlan_encapsulation") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails, self).__setattr__(name, value)


                        class Stack(Entity):
                            """
                            Stack value
                            
                            .. attribute:: outer_tag
                            
                            	Outer tag value
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: second_tag
                            
                            	Second tag value
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'l2-eth-infra-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Stack, self).__init__()

                                self.yang_name = "stack"
                                self.yang_parent_name = "encapsulation-details"

                                self.outer_tag = YLeaf(YType.uint16, "outer-tag")

                                self.second_tag = YLeaf(YType.uint16, "second-tag")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("outer_tag",
                                                "second_tag") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Stack, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Stack, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.outer_tag.is_set or
                                    self.second_tag.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.outer_tag.yfilter != YFilter.not_set or
                                    self.second_tag.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "stack" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.outer_tag.is_set or self.outer_tag.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.outer_tag.get_name_leafdata())
                                if (self.second_tag.is_set or self.second_tag.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.second_tag.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "outer-tag" or name == "second-tag"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "outer-tag"):
                                    self.outer_tag = value
                                    self.outer_tag.value_namespace = name_space
                                    self.outer_tag.value_namespace_prefix = name_space_prefix
                                if(value_path == "second-tag"):
                                    self.second_tag = value
                                    self.second_tag.value_namespace = name_space
                                    self.second_tag.value_namespace_prefix = name_space_prefix


                        class ServiceInstanceDetails(Entity):
                            """
                            Service Instance encapsulation
                            
                            .. attribute:: destination_mac_match
                            
                            	The destination MAC address to match on ingress
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: is_exact_match
                            
                            	Whether the packet must match the encapsulation exactly, with no further inner tags
                            	**type**\:  bool
                            
                            .. attribute:: is_native_preserving
                            
                            	Whether the native VLAN is customer\-tag preserving
                            	**type**\:  bool
                            
                            .. attribute:: is_native_vlan
                            
                            	Whether this represents the native VLAN on the port
                            	**type**\:  bool
                            
                            .. attribute:: local_traffic_stack
                            
                            	VLAN tags for locally\-sourced traffic
                            	**type**\:   :py:class:`LocalTrafficStack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack>`
                            
                            .. attribute:: payload_ethertype
                            
                            	Payload Ethertype to match
                            	**type**\:   :py:class:`EfpPayloadEtype <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpPayloadEtype>`
                            
                            .. attribute:: pushe
                            
                            	VLAN tags pushed on egress
                            	**type**\: list of    :py:class:`Pushe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.Pushe>`
                            
                            .. attribute:: source_mac_match
                            
                            	The source MAC address to match on ingress
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: tags_popped
                            
                            	Number of tags popped on ingress
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: tags_to_match
                            
                            	Tags to match on ingress packets
                            	**type**\: list of    :py:class:`TagsToMatch <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch>`
                            
                            

                            """

                            _prefix = 'l2-eth-infra-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails, self).__init__()

                                self.yang_name = "service-instance-details"
                                self.yang_parent_name = "encapsulation-details"

                                self.destination_mac_match = YLeaf(YType.str, "destination-mac-match")

                                self.is_exact_match = YLeaf(YType.boolean, "is-exact-match")

                                self.is_native_preserving = YLeaf(YType.boolean, "is-native-preserving")

                                self.is_native_vlan = YLeaf(YType.boolean, "is-native-vlan")

                                self.payload_ethertype = YLeaf(YType.enumeration, "payload-ethertype")

                                self.source_mac_match = YLeaf(YType.str, "source-mac-match")

                                self.tags_popped = YLeaf(YType.uint16, "tags-popped")

                                self.local_traffic_stack = Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack()
                                self.local_traffic_stack.parent = self
                                self._children_name_map["local_traffic_stack"] = "local-traffic-stack"
                                self._children_yang_names.add("local-traffic-stack")

                                self.pushe = YList(self)
                                self.tags_to_match = YList(self)

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("destination_mac_match",
                                                "is_exact_match",
                                                "is_native_preserving",
                                                "is_native_vlan",
                                                "payload_ethertype",
                                                "source_mac_match",
                                                "tags_popped") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails, self).__setattr__(name, value)


                            class LocalTrafficStack(Entity):
                                """
                                VLAN tags for locally\-sourced traffic
                                
                                .. attribute:: local_traffic_tag
                                
                                	VLAN tags for locally\-sourced traffic
                                	**type**\: list of    :py:class:`LocalTrafficTag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack.LocalTrafficTag>`
                                
                                

                                """

                                _prefix = 'l2-eth-infra-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack, self).__init__()

                                    self.yang_name = "local-traffic-stack"
                                    self.yang_parent_name = "service-instance-details"

                                    self.local_traffic_tag = YList(self)

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
                                                super(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack, self).__setattr__(name, value)


                                class LocalTrafficTag(Entity):
                                    """
                                    VLAN tags for locally\-sourced traffic
                                    
                                    .. attribute:: ethertype
                                    
                                    	Ethertype of tag
                                    	**type**\:   :py:class:`EfpTagEtype <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpTagEtype>`
                                    
                                    .. attribute:: vlan_id
                                    
                                    	VLAN Id
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'l2-eth-infra-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack.LocalTrafficTag, self).__init__()

                                        self.yang_name = "local-traffic-tag"
                                        self.yang_parent_name = "local-traffic-stack"

                                        self.ethertype = YLeaf(YType.enumeration, "ethertype")

                                        self.vlan_id = YLeaf(YType.uint16, "vlan-id")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("ethertype",
                                                        "vlan_id") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack.LocalTrafficTag, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack.LocalTrafficTag, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.ethertype.is_set or
                                            self.vlan_id.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.ethertype.yfilter != YFilter.not_set or
                                            self.vlan_id.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "local-traffic-tag" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.ethertype.is_set or self.ethertype.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.ethertype.get_name_leafdata())
                                        if (self.vlan_id.is_set or self.vlan_id.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.vlan_id.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "ethertype" or name == "vlan-id"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "ethertype"):
                                            self.ethertype = value
                                            self.ethertype.value_namespace = name_space
                                            self.ethertype.value_namespace_prefix = name_space_prefix
                                        if(value_path == "vlan-id"):
                                            self.vlan_id = value
                                            self.vlan_id.value_namespace = name_space
                                            self.vlan_id.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.local_traffic_tag:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.local_traffic_tag:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "local-traffic-stack" + path_buffer

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

                                    if (child_yang_name == "local-traffic-tag"):
                                        for c in self.local_traffic_tag:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack.LocalTrafficTag()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.local_traffic_tag.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "local-traffic-tag"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass


                            class TagsToMatch(Entity):
                                """
                                Tags to match on ingress packets
                                
                                .. attribute:: ethertype
                                
                                	Ethertype of tag to match
                                	**type**\:   :py:class:`EfpTagEtype <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpTagEtype>`
                                
                                .. attribute:: priority
                                
                                	Priority to match
                                	**type**\:   :py:class:`EfpTagPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpTagPriority>`
                                
                                .. attribute:: vlan_range
                                
                                	VLAN Ids to match
                                	**type**\: list of    :py:class:`VlanRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch.VlanRange>`
                                
                                

                                """

                                _prefix = 'l2-eth-infra-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch, self).__init__()

                                    self.yang_name = "tags-to-match"
                                    self.yang_parent_name = "service-instance-details"

                                    self.ethertype = YLeaf(YType.enumeration, "ethertype")

                                    self.priority = YLeaf(YType.enumeration, "priority")

                                    self.vlan_range = YList(self)

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("ethertype",
                                                    "priority") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch, self).__setattr__(name, value)


                                class VlanRange(Entity):
                                    """
                                    VLAN Ids to match
                                    
                                    .. attribute:: vlan_id_high
                                    
                                    	VLAN ID High
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: vlan_id_low
                                    
                                    	VLAN ID Low
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'l2-eth-infra-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch.VlanRange, self).__init__()

                                        self.yang_name = "vlan-range"
                                        self.yang_parent_name = "tags-to-match"

                                        self.vlan_id_high = YLeaf(YType.uint16, "vlan-id-high")

                                        self.vlan_id_low = YLeaf(YType.uint16, "vlan-id-low")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("vlan_id_high",
                                                        "vlan_id_low") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch.VlanRange, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch.VlanRange, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.vlan_id_high.is_set or
                                            self.vlan_id_low.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.vlan_id_high.yfilter != YFilter.not_set or
                                            self.vlan_id_low.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "vlan-range" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.vlan_id_high.is_set or self.vlan_id_high.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.vlan_id_high.get_name_leafdata())
                                        if (self.vlan_id_low.is_set or self.vlan_id_low.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.vlan_id_low.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "vlan-id-high" or name == "vlan-id-low"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "vlan-id-high"):
                                            self.vlan_id_high = value
                                            self.vlan_id_high.value_namespace = name_space
                                            self.vlan_id_high.value_namespace_prefix = name_space_prefix
                                        if(value_path == "vlan-id-low"):
                                            self.vlan_id_low = value
                                            self.vlan_id_low.value_namespace = name_space
                                            self.vlan_id_low.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.vlan_range:
                                        if (c.has_data()):
                                            return True
                                    return (
                                        self.ethertype.is_set or
                                        self.priority.is_set)

                                def has_operation(self):
                                    for c in self.vlan_range:
                                        if (c.has_operation()):
                                            return True
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.ethertype.yfilter != YFilter.not_set or
                                        self.priority.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "tags-to-match" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.ethertype.is_set or self.ethertype.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.ethertype.get_name_leafdata())
                                    if (self.priority.is_set or self.priority.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.priority.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "vlan-range"):
                                        for c in self.vlan_range:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch.VlanRange()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.vlan_range.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "vlan-range" or name == "ethertype" or name == "priority"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "ethertype"):
                                        self.ethertype = value
                                        self.ethertype.value_namespace = name_space
                                        self.ethertype.value_namespace_prefix = name_space_prefix
                                    if(value_path == "priority"):
                                        self.priority = value
                                        self.priority.value_namespace = name_space
                                        self.priority.value_namespace_prefix = name_space_prefix


                            class Pushe(Entity):
                                """
                                VLAN tags pushed on egress
                                
                                .. attribute:: ethertype
                                
                                	Ethertype of tag
                                	**type**\:   :py:class:`EfpTagEtype <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpTagEtype>`
                                
                                .. attribute:: vlan_id
                                
                                	VLAN Id
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'l2-eth-infra-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.Pushe, self).__init__()

                                    self.yang_name = "pushe"
                                    self.yang_parent_name = "service-instance-details"

                                    self.ethertype = YLeaf(YType.enumeration, "ethertype")

                                    self.vlan_id = YLeaf(YType.uint16, "vlan-id")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("ethertype",
                                                    "vlan_id") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.Pushe, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.Pushe, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.ethertype.is_set or
                                        self.vlan_id.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.ethertype.yfilter != YFilter.not_set or
                                        self.vlan_id.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "pushe" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.ethertype.is_set or self.ethertype.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.ethertype.get_name_leafdata())
                                    if (self.vlan_id.is_set or self.vlan_id.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.vlan_id.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "ethertype" or name == "vlan-id"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "ethertype"):
                                        self.ethertype = value
                                        self.ethertype.value_namespace = name_space
                                        self.ethertype.value_namespace_prefix = name_space_prefix
                                    if(value_path == "vlan-id"):
                                        self.vlan_id = value
                                        self.vlan_id.value_namespace = name_space
                                        self.vlan_id.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.pushe:
                                    if (c.has_data()):
                                        return True
                                for c in self.tags_to_match:
                                    if (c.has_data()):
                                        return True
                                return (
                                    self.destination_mac_match.is_set or
                                    self.is_exact_match.is_set or
                                    self.is_native_preserving.is_set or
                                    self.is_native_vlan.is_set or
                                    self.payload_ethertype.is_set or
                                    self.source_mac_match.is_set or
                                    self.tags_popped.is_set or
                                    (self.local_traffic_stack is not None and self.local_traffic_stack.has_data()))

                            def has_operation(self):
                                for c in self.pushe:
                                    if (c.has_operation()):
                                        return True
                                for c in self.tags_to_match:
                                    if (c.has_operation()):
                                        return True
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.destination_mac_match.yfilter != YFilter.not_set or
                                    self.is_exact_match.yfilter != YFilter.not_set or
                                    self.is_native_preserving.yfilter != YFilter.not_set or
                                    self.is_native_vlan.yfilter != YFilter.not_set or
                                    self.payload_ethertype.yfilter != YFilter.not_set or
                                    self.source_mac_match.yfilter != YFilter.not_set or
                                    self.tags_popped.yfilter != YFilter.not_set or
                                    (self.local_traffic_stack is not None and self.local_traffic_stack.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "service-instance-details" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.destination_mac_match.is_set or self.destination_mac_match.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.destination_mac_match.get_name_leafdata())
                                if (self.is_exact_match.is_set or self.is_exact_match.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.is_exact_match.get_name_leafdata())
                                if (self.is_native_preserving.is_set or self.is_native_preserving.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.is_native_preserving.get_name_leafdata())
                                if (self.is_native_vlan.is_set or self.is_native_vlan.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.is_native_vlan.get_name_leafdata())
                                if (self.payload_ethertype.is_set or self.payload_ethertype.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.payload_ethertype.get_name_leafdata())
                                if (self.source_mac_match.is_set or self.source_mac_match.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.source_mac_match.get_name_leafdata())
                                if (self.tags_popped.is_set or self.tags_popped.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.tags_popped.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "local-traffic-stack"):
                                    if (self.local_traffic_stack is None):
                                        self.local_traffic_stack = Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack()
                                        self.local_traffic_stack.parent = self
                                        self._children_name_map["local_traffic_stack"] = "local-traffic-stack"
                                    return self.local_traffic_stack

                                if (child_yang_name == "pushe"):
                                    for c in self.pushe:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.Pushe()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.pushe.append(c)
                                    return c

                                if (child_yang_name == "tags-to-match"):
                                    for c in self.tags_to_match:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.tags_to_match.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "local-traffic-stack" or name == "pushe" or name == "tags-to-match" or name == "destination-mac-match" or name == "is-exact-match" or name == "is-native-preserving" or name == "is-native-vlan" or name == "payload-ethertype" or name == "source-mac-match" or name == "tags-popped"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "destination-mac-match"):
                                    self.destination_mac_match = value
                                    self.destination_mac_match.value_namespace = name_space
                                    self.destination_mac_match.value_namespace_prefix = name_space_prefix
                                if(value_path == "is-exact-match"):
                                    self.is_exact_match = value
                                    self.is_exact_match.value_namespace = name_space
                                    self.is_exact_match.value_namespace_prefix = name_space_prefix
                                if(value_path == "is-native-preserving"):
                                    self.is_native_preserving = value
                                    self.is_native_preserving.value_namespace = name_space
                                    self.is_native_preserving.value_namespace_prefix = name_space_prefix
                                if(value_path == "is-native-vlan"):
                                    self.is_native_vlan = value
                                    self.is_native_vlan.value_namespace = name_space
                                    self.is_native_vlan.value_namespace_prefix = name_space_prefix
                                if(value_path == "payload-ethertype"):
                                    self.payload_ethertype = value
                                    self.payload_ethertype.value_namespace = name_space
                                    self.payload_ethertype.value_namespace_prefix = name_space_prefix
                                if(value_path == "source-mac-match"):
                                    self.source_mac_match = value
                                    self.source_mac_match.value_namespace = name_space
                                    self.source_mac_match.value_namespace_prefix = name_space_prefix
                                if(value_path == "tags-popped"):
                                    self.tags_popped = value
                                    self.tags_popped.value_namespace = name_space
                                    self.tags_popped.value_namespace_prefix = name_space_prefix


                        class Dot1AdDot1QStack(Entity):
                            """
                            802.1ad 802.1Q stack value
                            
                            .. attribute:: outer_tag
                            
                            	Outer tag value
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: second_tag
                            
                            	Second tag value
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'l2-eth-infra-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Dot1AdDot1QStack, self).__init__()

                                self.yang_name = "dot1ad-dot1q-stack"
                                self.yang_parent_name = "encapsulation-details"

                                self.outer_tag = YLeaf(YType.uint16, "outer-tag")

                                self.second_tag = YLeaf(YType.uint16, "second-tag")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("outer_tag",
                                                "second_tag") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Dot1AdDot1QStack, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Dot1AdDot1QStack, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.outer_tag.is_set or
                                    self.second_tag.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.outer_tag.yfilter != YFilter.not_set or
                                    self.second_tag.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "dot1ad-dot1q-stack" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.outer_tag.is_set or self.outer_tag.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.outer_tag.get_name_leafdata())
                                if (self.second_tag.is_set or self.second_tag.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.second_tag.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "outer-tag" or name == "second-tag"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "outer-tag"):
                                    self.outer_tag = value
                                    self.outer_tag.value_namespace = name_space
                                    self.outer_tag.value_namespace_prefix = name_space_prefix
                                if(value_path == "second-tag"):
                                    self.second_tag = value
                                    self.second_tag.value_namespace = name_space
                                    self.second_tag.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.dot1ad_native_tag.is_set or
                                self.dot1ad_outer_tag.is_set or
                                self.dot1ad_tag.is_set or
                                self.native_tag.is_set or
                                self.outer_tag.is_set or
                                self.tag.is_set or
                                self.vlan_encapsulation.is_set or
                                (self.dot1ad_dot1q_stack is not None and self.dot1ad_dot1q_stack.has_data()) or
                                (self.service_instance_details is not None and self.service_instance_details.has_data()) or
                                (self.stack is not None and self.stack.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.dot1ad_native_tag.yfilter != YFilter.not_set or
                                self.dot1ad_outer_tag.yfilter != YFilter.not_set or
                                self.dot1ad_tag.yfilter != YFilter.not_set or
                                self.native_tag.yfilter != YFilter.not_set or
                                self.outer_tag.yfilter != YFilter.not_set or
                                self.tag.yfilter != YFilter.not_set or
                                self.vlan_encapsulation.yfilter != YFilter.not_set or
                                (self.dot1ad_dot1q_stack is not None and self.dot1ad_dot1q_stack.has_operation()) or
                                (self.service_instance_details is not None and self.service_instance_details.has_operation()) or
                                (self.stack is not None and self.stack.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "encapsulation-details" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.dot1ad_native_tag.is_set or self.dot1ad_native_tag.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dot1ad_native_tag.get_name_leafdata())
                            if (self.dot1ad_outer_tag.is_set or self.dot1ad_outer_tag.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dot1ad_outer_tag.get_name_leafdata())
                            if (self.dot1ad_tag.is_set or self.dot1ad_tag.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dot1ad_tag.get_name_leafdata())
                            if (self.native_tag.is_set or self.native_tag.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.native_tag.get_name_leafdata())
                            if (self.outer_tag.is_set or self.outer_tag.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.outer_tag.get_name_leafdata())
                            if (self.tag.is_set or self.tag.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.tag.get_name_leafdata())
                            if (self.vlan_encapsulation.is_set or self.vlan_encapsulation.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.vlan_encapsulation.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "dot1ad-dot1q-stack"):
                                if (self.dot1ad_dot1q_stack is None):
                                    self.dot1ad_dot1q_stack = Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Dot1AdDot1QStack()
                                    self.dot1ad_dot1q_stack.parent = self
                                    self._children_name_map["dot1ad_dot1q_stack"] = "dot1ad-dot1q-stack"
                                return self.dot1ad_dot1q_stack

                            if (child_yang_name == "service-instance-details"):
                                if (self.service_instance_details is None):
                                    self.service_instance_details = Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails()
                                    self.service_instance_details.parent = self
                                    self._children_name_map["service_instance_details"] = "service-instance-details"
                                return self.service_instance_details

                            if (child_yang_name == "stack"):
                                if (self.stack is None):
                                    self.stack = Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Stack()
                                    self.stack.parent = self
                                    self._children_name_map["stack"] = "stack"
                                return self.stack

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "dot1ad-dot1q-stack" or name == "service-instance-details" or name == "stack" or name == "dot1ad-native-tag" or name == "dot1ad-outer-tag" or name == "dot1ad-tag" or name == "native-tag" or name == "outer-tag" or name == "tag" or name == "vlan-encapsulation"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "dot1ad-native-tag"):
                                self.dot1ad_native_tag = value
                                self.dot1ad_native_tag.value_namespace = name_space
                                self.dot1ad_native_tag.value_namespace_prefix = name_space_prefix
                            if(value_path == "dot1ad-outer-tag"):
                                self.dot1ad_outer_tag = value
                                self.dot1ad_outer_tag.value_namespace = name_space
                                self.dot1ad_outer_tag.value_namespace_prefix = name_space_prefix
                            if(value_path == "dot1ad-tag"):
                                self.dot1ad_tag = value
                                self.dot1ad_tag.value_namespace = name_space
                                self.dot1ad_tag.value_namespace_prefix = name_space_prefix
                            if(value_path == "native-tag"):
                                self.native_tag = value
                                self.native_tag.value_namespace = name_space
                                self.native_tag.value_namespace_prefix = name_space_prefix
                            if(value_path == "outer-tag"):
                                self.outer_tag = value
                                self.outer_tag.value_namespace = name_space
                                self.outer_tag.value_namespace_prefix = name_space_prefix
                            if(value_path == "tag"):
                                self.tag = value
                                self.tag.value_namespace = name_space
                                self.tag.value_namespace_prefix = name_space_prefix
                            if(value_path == "vlan-encapsulation"):
                                self.vlan_encapsulation = value
                                self.vlan_encapsulation.value_namespace = name_space
                                self.vlan_encapsulation.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.interface.is_set or
                            self.interface_xr.is_set or
                            self.mtu.is_set or
                            self.parent_interface.is_set or
                            self.service.is_set or
                            self.state.is_set or
                            self.switched_mtu.is_set or
                            (self.encapsulation_details is not None and self.encapsulation_details.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface.yfilter != YFilter.not_set or
                            self.interface_xr.yfilter != YFilter.not_set or
                            self.mtu.yfilter != YFilter.not_set or
                            self.parent_interface.yfilter != YFilter.not_set or
                            self.service.yfilter != YFilter.not_set or
                            self.state.yfilter != YFilter.not_set or
                            self.switched_mtu.yfilter != YFilter.not_set or
                            (self.encapsulation_details is not None and self.encapsulation_details.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface" + "[interface='" + self.interface.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface.get_name_leafdata())
                        if (self.interface_xr.is_set or self.interface_xr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_xr.get_name_leafdata())
                        if (self.mtu.is_set or self.mtu.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mtu.get_name_leafdata())
                        if (self.parent_interface.is_set or self.parent_interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.parent_interface.get_name_leafdata())
                        if (self.service.is_set or self.service.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.service.get_name_leafdata())
                        if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.state.get_name_leafdata())
                        if (self.switched_mtu.is_set or self.switched_mtu.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.switched_mtu.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "encapsulation-details"):
                            if (self.encapsulation_details is None):
                                self.encapsulation_details = Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails()
                                self.encapsulation_details.parent = self
                                self._children_name_map["encapsulation_details"] = "encapsulation-details"
                            return self.encapsulation_details

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "encapsulation-details" or name == "interface" or name == "interface-xr" or name == "mtu" or name == "parent-interface" or name == "service" or name == "state" or name == "switched-mtu"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface"):
                            self.interface = value
                            self.interface.value_namespace = name_space
                            self.interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-xr"):
                            self.interface_xr = value
                            self.interface_xr.value_namespace = name_space
                            self.interface_xr.value_namespace_prefix = name_space_prefix
                        if(value_path == "mtu"):
                            self.mtu = value
                            self.mtu.value_namespace = name_space
                            self.mtu.value_namespace_prefix = name_space_prefix
                        if(value_path == "parent-interface"):
                            self.parent_interface = value
                            self.parent_interface.value_namespace = name_space
                            self.parent_interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "service"):
                            self.service = value
                            self.service.value_namespace = name_space
                            self.service.value_namespace_prefix = name_space_prefix
                        if(value_path == "state"):
                            self.state = value
                            self.state.value_namespace = name_space
                            self.state.value_namespace_prefix = name_space_prefix
                        if(value_path == "switched-mtu"):
                            self.switched_mtu = value
                            self.switched_mtu.value_namespace = name_space
                            self.switched_mtu.value_namespace_prefix = name_space_prefix

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

                    if (child_yang_name == "interface"):
                        for c in self.interface:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Vlan.Nodes.Node.Interfaces.Interface()
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


            class TagAllocations(Entity):
                """
                VLAN tag allocation table (specific to this
                node)
                
                .. attribute:: tag_allocation
                
                	Operational data for a sub\-interface configured with VLANs
                	**type**\: list of    :py:class:`TagAllocation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.TagAllocations.TagAllocation>`
                
                

                """

                _prefix = 'l2-eth-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Vlan.Nodes.Node.TagAllocations, self).__init__()

                    self.yang_name = "tag-allocations"
                    self.yang_parent_name = "node"

                    self.tag_allocation = YList(self)

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
                                super(Vlan.Nodes.Node.TagAllocations, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Vlan.Nodes.Node.TagAllocations, self).__setattr__(name, value)


                class TagAllocation(Entity):
                    """
                    Operational data for a sub\-interface
                    configured with VLANs
                    
                    .. attribute:: encapsulation_details
                    
                    	Encapsulation type and tag stack
                    	**type**\:   :py:class:`EncapsulationDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails>`
                    
                    .. attribute:: first_tag
                    
                    	The first (outermost) tag
                    	**type**\:  int
                    
                    	**range:** 1..4094
                    
                    .. attribute:: interface
                    
                    	The interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: interface_xr
                    
                    	Interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: mtu
                    
                    	L2 MTU
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: parent_interface
                    
                    	Parent interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: second_tag
                    
                    	The second tag
                    	**type**\: one of the below types:
                    
                    	**type**\:   :py:class:`VlanTagOrAny <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_datatypes.VlanTagOrAny>`
                    
                    
                    ----
                    	**type**\:  int
                    
                    	**range:** 1..4096
                    
                    
                    ----
                    .. attribute:: service
                    
                    	Service type
                    	**type**\:   :py:class:`VlanService <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.VlanService>`
                    
                    .. attribute:: state
                    
                    	Interface state
                    	**type**\:   :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.ImStateEnum>`
                    
                    .. attribute:: switched_mtu
                    
                    	L2 switched MTU
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'l2-eth-infra-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Vlan.Nodes.Node.TagAllocations.TagAllocation, self).__init__()

                        self.yang_name = "tag-allocation"
                        self.yang_parent_name = "tag-allocations"

                        self.first_tag = YLeaf(YType.uint32, "first-tag")

                        self.interface = YLeaf(YType.str, "interface")

                        self.interface_xr = YLeaf(YType.str, "interface-xr")

                        self.mtu = YLeaf(YType.uint16, "mtu")

                        self.parent_interface = YLeaf(YType.str, "parent-interface")

                        self.second_tag = YLeaf(YType.str, "second-tag")

                        self.service = YLeaf(YType.enumeration, "service")

                        self.state = YLeaf(YType.enumeration, "state")

                        self.switched_mtu = YLeaf(YType.uint16, "switched-mtu")

                        self.encapsulation_details = Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails()
                        self.encapsulation_details.parent = self
                        self._children_name_map["encapsulation_details"] = "encapsulation-details"
                        self._children_yang_names.add("encapsulation-details")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("first_tag",
                                        "interface",
                                        "interface_xr",
                                        "mtu",
                                        "parent_interface",
                                        "second_tag",
                                        "service",
                                        "state",
                                        "switched_mtu") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Vlan.Nodes.Node.TagAllocations.TagAllocation, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Vlan.Nodes.Node.TagAllocations.TagAllocation, self).__setattr__(name, value)


                    class EncapsulationDetails(Entity):
                        """
                        Encapsulation type and tag stack
                        
                        .. attribute:: dot1ad_dot1q_stack
                        
                        	802.1ad 802.1Q stack value
                        	**type**\:   :py:class:`Dot1AdDot1QStack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Dot1AdDot1QStack>`
                        
                        .. attribute:: dot1ad_native_tag
                        
                        	802.1ad native tag value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: dot1ad_outer_tag
                        
                        	802.1ad Outer tag value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: dot1ad_tag
                        
                        	802.1ad tag value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: native_tag
                        
                        	Native tag value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: outer_tag
                        
                        	Outer tag value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: service_instance_details
                        
                        	Service Instance encapsulation
                        	**type**\:   :py:class:`ServiceInstanceDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails>`
                        
                        .. attribute:: stack
                        
                        	Stack value
                        	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Stack>`
                        
                        .. attribute:: tag
                        
                        	Tag value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: vlan_encapsulation
                        
                        	VLANEncapsulation
                        	**type**\:   :py:class:`VlanEncaps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.VlanEncaps>`
                        
                        

                        """

                        _prefix = 'l2-eth-infra-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails, self).__init__()

                            self.yang_name = "encapsulation-details"
                            self.yang_parent_name = "tag-allocation"

                            self.dot1ad_native_tag = YLeaf(YType.uint16, "dot1ad-native-tag")

                            self.dot1ad_outer_tag = YLeaf(YType.uint16, "dot1ad-outer-tag")

                            self.dot1ad_tag = YLeaf(YType.uint16, "dot1ad-tag")

                            self.native_tag = YLeaf(YType.uint16, "native-tag")

                            self.outer_tag = YLeaf(YType.uint16, "outer-tag")

                            self.tag = YLeaf(YType.uint16, "tag")

                            self.vlan_encapsulation = YLeaf(YType.enumeration, "vlan-encapsulation")

                            self.dot1ad_dot1q_stack = Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Dot1AdDot1QStack()
                            self.dot1ad_dot1q_stack.parent = self
                            self._children_name_map["dot1ad_dot1q_stack"] = "dot1ad-dot1q-stack"
                            self._children_yang_names.add("dot1ad-dot1q-stack")

                            self.service_instance_details = Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails()
                            self.service_instance_details.parent = self
                            self._children_name_map["service_instance_details"] = "service-instance-details"
                            self._children_yang_names.add("service-instance-details")

                            self.stack = Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Stack()
                            self.stack.parent = self
                            self._children_name_map["stack"] = "stack"
                            self._children_yang_names.add("stack")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("dot1ad_native_tag",
                                            "dot1ad_outer_tag",
                                            "dot1ad_tag",
                                            "native_tag",
                                            "outer_tag",
                                            "tag",
                                            "vlan_encapsulation") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails, self).__setattr__(name, value)


                        class Stack(Entity):
                            """
                            Stack value
                            
                            .. attribute:: outer_tag
                            
                            	Outer tag value
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: second_tag
                            
                            	Second tag value
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'l2-eth-infra-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Stack, self).__init__()

                                self.yang_name = "stack"
                                self.yang_parent_name = "encapsulation-details"

                                self.outer_tag = YLeaf(YType.uint16, "outer-tag")

                                self.second_tag = YLeaf(YType.uint16, "second-tag")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("outer_tag",
                                                "second_tag") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Stack, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Stack, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.outer_tag.is_set or
                                    self.second_tag.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.outer_tag.yfilter != YFilter.not_set or
                                    self.second_tag.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "stack" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.outer_tag.is_set or self.outer_tag.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.outer_tag.get_name_leafdata())
                                if (self.second_tag.is_set or self.second_tag.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.second_tag.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "outer-tag" or name == "second-tag"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "outer-tag"):
                                    self.outer_tag = value
                                    self.outer_tag.value_namespace = name_space
                                    self.outer_tag.value_namespace_prefix = name_space_prefix
                                if(value_path == "second-tag"):
                                    self.second_tag = value
                                    self.second_tag.value_namespace = name_space
                                    self.second_tag.value_namespace_prefix = name_space_prefix


                        class ServiceInstanceDetails(Entity):
                            """
                            Service Instance encapsulation
                            
                            .. attribute:: destination_mac_match
                            
                            	The destination MAC address to match on ingress
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: is_exact_match
                            
                            	Whether the packet must match the encapsulation exactly, with no further inner tags
                            	**type**\:  bool
                            
                            .. attribute:: is_native_preserving
                            
                            	Whether the native VLAN is customer\-tag preserving
                            	**type**\:  bool
                            
                            .. attribute:: is_native_vlan
                            
                            	Whether this represents the native VLAN on the port
                            	**type**\:  bool
                            
                            .. attribute:: local_traffic_stack
                            
                            	VLAN tags for locally\-sourced traffic
                            	**type**\:   :py:class:`LocalTrafficStack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack>`
                            
                            .. attribute:: payload_ethertype
                            
                            	Payload Ethertype to match
                            	**type**\:   :py:class:`EfpPayloadEtype <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpPayloadEtype>`
                            
                            .. attribute:: pushe
                            
                            	VLAN tags pushed on egress
                            	**type**\: list of    :py:class:`Pushe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.Pushe>`
                            
                            .. attribute:: source_mac_match
                            
                            	The source MAC address to match on ingress
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: tags_popped
                            
                            	Number of tags popped on ingress
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: tags_to_match
                            
                            	Tags to match on ingress packets
                            	**type**\: list of    :py:class:`TagsToMatch <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch>`
                            
                            

                            """

                            _prefix = 'l2-eth-infra-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails, self).__init__()

                                self.yang_name = "service-instance-details"
                                self.yang_parent_name = "encapsulation-details"

                                self.destination_mac_match = YLeaf(YType.str, "destination-mac-match")

                                self.is_exact_match = YLeaf(YType.boolean, "is-exact-match")

                                self.is_native_preserving = YLeaf(YType.boolean, "is-native-preserving")

                                self.is_native_vlan = YLeaf(YType.boolean, "is-native-vlan")

                                self.payload_ethertype = YLeaf(YType.enumeration, "payload-ethertype")

                                self.source_mac_match = YLeaf(YType.str, "source-mac-match")

                                self.tags_popped = YLeaf(YType.uint16, "tags-popped")

                                self.local_traffic_stack = Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack()
                                self.local_traffic_stack.parent = self
                                self._children_name_map["local_traffic_stack"] = "local-traffic-stack"
                                self._children_yang_names.add("local-traffic-stack")

                                self.pushe = YList(self)
                                self.tags_to_match = YList(self)

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("destination_mac_match",
                                                "is_exact_match",
                                                "is_native_preserving",
                                                "is_native_vlan",
                                                "payload_ethertype",
                                                "source_mac_match",
                                                "tags_popped") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails, self).__setattr__(name, value)


                            class LocalTrafficStack(Entity):
                                """
                                VLAN tags for locally\-sourced traffic
                                
                                .. attribute:: local_traffic_tag
                                
                                	VLAN tags for locally\-sourced traffic
                                	**type**\: list of    :py:class:`LocalTrafficTag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack.LocalTrafficTag>`
                                
                                

                                """

                                _prefix = 'l2-eth-infra-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack, self).__init__()

                                    self.yang_name = "local-traffic-stack"
                                    self.yang_parent_name = "service-instance-details"

                                    self.local_traffic_tag = YList(self)

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
                                                super(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack, self).__setattr__(name, value)


                                class LocalTrafficTag(Entity):
                                    """
                                    VLAN tags for locally\-sourced traffic
                                    
                                    .. attribute:: ethertype
                                    
                                    	Ethertype of tag
                                    	**type**\:   :py:class:`EfpTagEtype <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpTagEtype>`
                                    
                                    .. attribute:: vlan_id
                                    
                                    	VLAN Id
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'l2-eth-infra-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack.LocalTrafficTag, self).__init__()

                                        self.yang_name = "local-traffic-tag"
                                        self.yang_parent_name = "local-traffic-stack"

                                        self.ethertype = YLeaf(YType.enumeration, "ethertype")

                                        self.vlan_id = YLeaf(YType.uint16, "vlan-id")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("ethertype",
                                                        "vlan_id") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack.LocalTrafficTag, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack.LocalTrafficTag, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.ethertype.is_set or
                                            self.vlan_id.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.ethertype.yfilter != YFilter.not_set or
                                            self.vlan_id.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "local-traffic-tag" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.ethertype.is_set or self.ethertype.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.ethertype.get_name_leafdata())
                                        if (self.vlan_id.is_set or self.vlan_id.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.vlan_id.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "ethertype" or name == "vlan-id"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "ethertype"):
                                            self.ethertype = value
                                            self.ethertype.value_namespace = name_space
                                            self.ethertype.value_namespace_prefix = name_space_prefix
                                        if(value_path == "vlan-id"):
                                            self.vlan_id = value
                                            self.vlan_id.value_namespace = name_space
                                            self.vlan_id.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.local_traffic_tag:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.local_traffic_tag:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "local-traffic-stack" + path_buffer

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

                                    if (child_yang_name == "local-traffic-tag"):
                                        for c in self.local_traffic_tag:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack.LocalTrafficTag()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.local_traffic_tag.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "local-traffic-tag"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass


                            class TagsToMatch(Entity):
                                """
                                Tags to match on ingress packets
                                
                                .. attribute:: ethertype
                                
                                	Ethertype of tag to match
                                	**type**\:   :py:class:`EfpTagEtype <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpTagEtype>`
                                
                                .. attribute:: priority
                                
                                	Priority to match
                                	**type**\:   :py:class:`EfpTagPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpTagPriority>`
                                
                                .. attribute:: vlan_range
                                
                                	VLAN Ids to match
                                	**type**\: list of    :py:class:`VlanRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch.VlanRange>`
                                
                                

                                """

                                _prefix = 'l2-eth-infra-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch, self).__init__()

                                    self.yang_name = "tags-to-match"
                                    self.yang_parent_name = "service-instance-details"

                                    self.ethertype = YLeaf(YType.enumeration, "ethertype")

                                    self.priority = YLeaf(YType.enumeration, "priority")

                                    self.vlan_range = YList(self)

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("ethertype",
                                                    "priority") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch, self).__setattr__(name, value)


                                class VlanRange(Entity):
                                    """
                                    VLAN Ids to match
                                    
                                    .. attribute:: vlan_id_high
                                    
                                    	VLAN ID High
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: vlan_id_low
                                    
                                    	VLAN ID Low
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'l2-eth-infra-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch.VlanRange, self).__init__()

                                        self.yang_name = "vlan-range"
                                        self.yang_parent_name = "tags-to-match"

                                        self.vlan_id_high = YLeaf(YType.uint16, "vlan-id-high")

                                        self.vlan_id_low = YLeaf(YType.uint16, "vlan-id-low")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("vlan_id_high",
                                                        "vlan_id_low") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch.VlanRange, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch.VlanRange, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.vlan_id_high.is_set or
                                            self.vlan_id_low.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.vlan_id_high.yfilter != YFilter.not_set or
                                            self.vlan_id_low.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "vlan-range" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.vlan_id_high.is_set or self.vlan_id_high.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.vlan_id_high.get_name_leafdata())
                                        if (self.vlan_id_low.is_set or self.vlan_id_low.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.vlan_id_low.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "vlan-id-high" or name == "vlan-id-low"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "vlan-id-high"):
                                            self.vlan_id_high = value
                                            self.vlan_id_high.value_namespace = name_space
                                            self.vlan_id_high.value_namespace_prefix = name_space_prefix
                                        if(value_path == "vlan-id-low"):
                                            self.vlan_id_low = value
                                            self.vlan_id_low.value_namespace = name_space
                                            self.vlan_id_low.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.vlan_range:
                                        if (c.has_data()):
                                            return True
                                    return (
                                        self.ethertype.is_set or
                                        self.priority.is_set)

                                def has_operation(self):
                                    for c in self.vlan_range:
                                        if (c.has_operation()):
                                            return True
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.ethertype.yfilter != YFilter.not_set or
                                        self.priority.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "tags-to-match" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.ethertype.is_set or self.ethertype.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.ethertype.get_name_leafdata())
                                    if (self.priority.is_set or self.priority.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.priority.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "vlan-range"):
                                        for c in self.vlan_range:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch.VlanRange()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.vlan_range.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "vlan-range" or name == "ethertype" or name == "priority"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "ethertype"):
                                        self.ethertype = value
                                        self.ethertype.value_namespace = name_space
                                        self.ethertype.value_namespace_prefix = name_space_prefix
                                    if(value_path == "priority"):
                                        self.priority = value
                                        self.priority.value_namespace = name_space
                                        self.priority.value_namespace_prefix = name_space_prefix


                            class Pushe(Entity):
                                """
                                VLAN tags pushed on egress
                                
                                .. attribute:: ethertype
                                
                                	Ethertype of tag
                                	**type**\:   :py:class:`EfpTagEtype <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EfpTagEtype>`
                                
                                .. attribute:: vlan_id
                                
                                	VLAN Id
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'l2-eth-infra-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.Pushe, self).__init__()

                                    self.yang_name = "pushe"
                                    self.yang_parent_name = "service-instance-details"

                                    self.ethertype = YLeaf(YType.enumeration, "ethertype")

                                    self.vlan_id = YLeaf(YType.uint16, "vlan-id")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("ethertype",
                                                    "vlan_id") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.Pushe, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.Pushe, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.ethertype.is_set or
                                        self.vlan_id.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.ethertype.yfilter != YFilter.not_set or
                                        self.vlan_id.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "pushe" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.ethertype.is_set or self.ethertype.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.ethertype.get_name_leafdata())
                                    if (self.vlan_id.is_set or self.vlan_id.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.vlan_id.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "ethertype" or name == "vlan-id"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "ethertype"):
                                        self.ethertype = value
                                        self.ethertype.value_namespace = name_space
                                        self.ethertype.value_namespace_prefix = name_space_prefix
                                    if(value_path == "vlan-id"):
                                        self.vlan_id = value
                                        self.vlan_id.value_namespace = name_space
                                        self.vlan_id.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.pushe:
                                    if (c.has_data()):
                                        return True
                                for c in self.tags_to_match:
                                    if (c.has_data()):
                                        return True
                                return (
                                    self.destination_mac_match.is_set or
                                    self.is_exact_match.is_set or
                                    self.is_native_preserving.is_set or
                                    self.is_native_vlan.is_set or
                                    self.payload_ethertype.is_set or
                                    self.source_mac_match.is_set or
                                    self.tags_popped.is_set or
                                    (self.local_traffic_stack is not None and self.local_traffic_stack.has_data()))

                            def has_operation(self):
                                for c in self.pushe:
                                    if (c.has_operation()):
                                        return True
                                for c in self.tags_to_match:
                                    if (c.has_operation()):
                                        return True
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.destination_mac_match.yfilter != YFilter.not_set or
                                    self.is_exact_match.yfilter != YFilter.not_set or
                                    self.is_native_preserving.yfilter != YFilter.not_set or
                                    self.is_native_vlan.yfilter != YFilter.not_set or
                                    self.payload_ethertype.yfilter != YFilter.not_set or
                                    self.source_mac_match.yfilter != YFilter.not_set or
                                    self.tags_popped.yfilter != YFilter.not_set or
                                    (self.local_traffic_stack is not None and self.local_traffic_stack.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "service-instance-details" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.destination_mac_match.is_set or self.destination_mac_match.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.destination_mac_match.get_name_leafdata())
                                if (self.is_exact_match.is_set or self.is_exact_match.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.is_exact_match.get_name_leafdata())
                                if (self.is_native_preserving.is_set or self.is_native_preserving.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.is_native_preserving.get_name_leafdata())
                                if (self.is_native_vlan.is_set or self.is_native_vlan.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.is_native_vlan.get_name_leafdata())
                                if (self.payload_ethertype.is_set or self.payload_ethertype.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.payload_ethertype.get_name_leafdata())
                                if (self.source_mac_match.is_set or self.source_mac_match.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.source_mac_match.get_name_leafdata())
                                if (self.tags_popped.is_set or self.tags_popped.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.tags_popped.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "local-traffic-stack"):
                                    if (self.local_traffic_stack is None):
                                        self.local_traffic_stack = Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack()
                                        self.local_traffic_stack.parent = self
                                        self._children_name_map["local_traffic_stack"] = "local-traffic-stack"
                                    return self.local_traffic_stack

                                if (child_yang_name == "pushe"):
                                    for c in self.pushe:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.Pushe()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.pushe.append(c)
                                    return c

                                if (child_yang_name == "tags-to-match"):
                                    for c in self.tags_to_match:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.tags_to_match.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "local-traffic-stack" or name == "pushe" or name == "tags-to-match" or name == "destination-mac-match" or name == "is-exact-match" or name == "is-native-preserving" or name == "is-native-vlan" or name == "payload-ethertype" or name == "source-mac-match" or name == "tags-popped"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "destination-mac-match"):
                                    self.destination_mac_match = value
                                    self.destination_mac_match.value_namespace = name_space
                                    self.destination_mac_match.value_namespace_prefix = name_space_prefix
                                if(value_path == "is-exact-match"):
                                    self.is_exact_match = value
                                    self.is_exact_match.value_namespace = name_space
                                    self.is_exact_match.value_namespace_prefix = name_space_prefix
                                if(value_path == "is-native-preserving"):
                                    self.is_native_preserving = value
                                    self.is_native_preserving.value_namespace = name_space
                                    self.is_native_preserving.value_namespace_prefix = name_space_prefix
                                if(value_path == "is-native-vlan"):
                                    self.is_native_vlan = value
                                    self.is_native_vlan.value_namespace = name_space
                                    self.is_native_vlan.value_namespace_prefix = name_space_prefix
                                if(value_path == "payload-ethertype"):
                                    self.payload_ethertype = value
                                    self.payload_ethertype.value_namespace = name_space
                                    self.payload_ethertype.value_namespace_prefix = name_space_prefix
                                if(value_path == "source-mac-match"):
                                    self.source_mac_match = value
                                    self.source_mac_match.value_namespace = name_space
                                    self.source_mac_match.value_namespace_prefix = name_space_prefix
                                if(value_path == "tags-popped"):
                                    self.tags_popped = value
                                    self.tags_popped.value_namespace = name_space
                                    self.tags_popped.value_namespace_prefix = name_space_prefix


                        class Dot1AdDot1QStack(Entity):
                            """
                            802.1ad 802.1Q stack value
                            
                            .. attribute:: outer_tag
                            
                            	Outer tag value
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: second_tag
                            
                            	Second tag value
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'l2-eth-infra-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Dot1AdDot1QStack, self).__init__()

                                self.yang_name = "dot1ad-dot1q-stack"
                                self.yang_parent_name = "encapsulation-details"

                                self.outer_tag = YLeaf(YType.uint16, "outer-tag")

                                self.second_tag = YLeaf(YType.uint16, "second-tag")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("outer_tag",
                                                "second_tag") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Dot1AdDot1QStack, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Dot1AdDot1QStack, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.outer_tag.is_set or
                                    self.second_tag.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.outer_tag.yfilter != YFilter.not_set or
                                    self.second_tag.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "dot1ad-dot1q-stack" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.outer_tag.is_set or self.outer_tag.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.outer_tag.get_name_leafdata())
                                if (self.second_tag.is_set or self.second_tag.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.second_tag.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "outer-tag" or name == "second-tag"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "outer-tag"):
                                    self.outer_tag = value
                                    self.outer_tag.value_namespace = name_space
                                    self.outer_tag.value_namespace_prefix = name_space_prefix
                                if(value_path == "second-tag"):
                                    self.second_tag = value
                                    self.second_tag.value_namespace = name_space
                                    self.second_tag.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.dot1ad_native_tag.is_set or
                                self.dot1ad_outer_tag.is_set or
                                self.dot1ad_tag.is_set or
                                self.native_tag.is_set or
                                self.outer_tag.is_set or
                                self.tag.is_set or
                                self.vlan_encapsulation.is_set or
                                (self.dot1ad_dot1q_stack is not None and self.dot1ad_dot1q_stack.has_data()) or
                                (self.service_instance_details is not None and self.service_instance_details.has_data()) or
                                (self.stack is not None and self.stack.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.dot1ad_native_tag.yfilter != YFilter.not_set or
                                self.dot1ad_outer_tag.yfilter != YFilter.not_set or
                                self.dot1ad_tag.yfilter != YFilter.not_set or
                                self.native_tag.yfilter != YFilter.not_set or
                                self.outer_tag.yfilter != YFilter.not_set or
                                self.tag.yfilter != YFilter.not_set or
                                self.vlan_encapsulation.yfilter != YFilter.not_set or
                                (self.dot1ad_dot1q_stack is not None and self.dot1ad_dot1q_stack.has_operation()) or
                                (self.service_instance_details is not None and self.service_instance_details.has_operation()) or
                                (self.stack is not None and self.stack.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "encapsulation-details" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.dot1ad_native_tag.is_set or self.dot1ad_native_tag.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dot1ad_native_tag.get_name_leafdata())
                            if (self.dot1ad_outer_tag.is_set or self.dot1ad_outer_tag.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dot1ad_outer_tag.get_name_leafdata())
                            if (self.dot1ad_tag.is_set or self.dot1ad_tag.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dot1ad_tag.get_name_leafdata())
                            if (self.native_tag.is_set or self.native_tag.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.native_tag.get_name_leafdata())
                            if (self.outer_tag.is_set or self.outer_tag.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.outer_tag.get_name_leafdata())
                            if (self.tag.is_set or self.tag.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.tag.get_name_leafdata())
                            if (self.vlan_encapsulation.is_set or self.vlan_encapsulation.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.vlan_encapsulation.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "dot1ad-dot1q-stack"):
                                if (self.dot1ad_dot1q_stack is None):
                                    self.dot1ad_dot1q_stack = Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Dot1AdDot1QStack()
                                    self.dot1ad_dot1q_stack.parent = self
                                    self._children_name_map["dot1ad_dot1q_stack"] = "dot1ad-dot1q-stack"
                                return self.dot1ad_dot1q_stack

                            if (child_yang_name == "service-instance-details"):
                                if (self.service_instance_details is None):
                                    self.service_instance_details = Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails()
                                    self.service_instance_details.parent = self
                                    self._children_name_map["service_instance_details"] = "service-instance-details"
                                return self.service_instance_details

                            if (child_yang_name == "stack"):
                                if (self.stack is None):
                                    self.stack = Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Stack()
                                    self.stack.parent = self
                                    self._children_name_map["stack"] = "stack"
                                return self.stack

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "dot1ad-dot1q-stack" or name == "service-instance-details" or name == "stack" or name == "dot1ad-native-tag" or name == "dot1ad-outer-tag" or name == "dot1ad-tag" or name == "native-tag" or name == "outer-tag" or name == "tag" or name == "vlan-encapsulation"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "dot1ad-native-tag"):
                                self.dot1ad_native_tag = value
                                self.dot1ad_native_tag.value_namespace = name_space
                                self.dot1ad_native_tag.value_namespace_prefix = name_space_prefix
                            if(value_path == "dot1ad-outer-tag"):
                                self.dot1ad_outer_tag = value
                                self.dot1ad_outer_tag.value_namespace = name_space
                                self.dot1ad_outer_tag.value_namespace_prefix = name_space_prefix
                            if(value_path == "dot1ad-tag"):
                                self.dot1ad_tag = value
                                self.dot1ad_tag.value_namespace = name_space
                                self.dot1ad_tag.value_namespace_prefix = name_space_prefix
                            if(value_path == "native-tag"):
                                self.native_tag = value
                                self.native_tag.value_namespace = name_space
                                self.native_tag.value_namespace_prefix = name_space_prefix
                            if(value_path == "outer-tag"):
                                self.outer_tag = value
                                self.outer_tag.value_namespace = name_space
                                self.outer_tag.value_namespace_prefix = name_space_prefix
                            if(value_path == "tag"):
                                self.tag = value
                                self.tag.value_namespace = name_space
                                self.tag.value_namespace_prefix = name_space_prefix
                            if(value_path == "vlan-encapsulation"):
                                self.vlan_encapsulation = value
                                self.vlan_encapsulation.value_namespace = name_space
                                self.vlan_encapsulation.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.first_tag.is_set or
                            self.interface.is_set or
                            self.interface_xr.is_set or
                            self.mtu.is_set or
                            self.parent_interface.is_set or
                            self.second_tag.is_set or
                            self.service.is_set or
                            self.state.is_set or
                            self.switched_mtu.is_set or
                            (self.encapsulation_details is not None and self.encapsulation_details.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.first_tag.yfilter != YFilter.not_set or
                            self.interface.yfilter != YFilter.not_set or
                            self.interface_xr.yfilter != YFilter.not_set or
                            self.mtu.yfilter != YFilter.not_set or
                            self.parent_interface.yfilter != YFilter.not_set or
                            self.second_tag.yfilter != YFilter.not_set or
                            self.service.yfilter != YFilter.not_set or
                            self.state.yfilter != YFilter.not_set or
                            self.switched_mtu.yfilter != YFilter.not_set or
                            (self.encapsulation_details is not None and self.encapsulation_details.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "tag-allocation" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.first_tag.is_set or self.first_tag.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.first_tag.get_name_leafdata())
                        if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface.get_name_leafdata())
                        if (self.interface_xr.is_set or self.interface_xr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_xr.get_name_leafdata())
                        if (self.mtu.is_set or self.mtu.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mtu.get_name_leafdata())
                        if (self.parent_interface.is_set or self.parent_interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.parent_interface.get_name_leafdata())
                        if (self.second_tag.is_set or self.second_tag.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.second_tag.get_name_leafdata())
                        if (self.service.is_set or self.service.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.service.get_name_leafdata())
                        if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.state.get_name_leafdata())
                        if (self.switched_mtu.is_set or self.switched_mtu.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.switched_mtu.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "encapsulation-details"):
                            if (self.encapsulation_details is None):
                                self.encapsulation_details = Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails()
                                self.encapsulation_details.parent = self
                                self._children_name_map["encapsulation_details"] = "encapsulation-details"
                            return self.encapsulation_details

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "encapsulation-details" or name == "first-tag" or name == "interface" or name == "interface-xr" or name == "mtu" or name == "parent-interface" or name == "second-tag" or name == "service" or name == "state" or name == "switched-mtu"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "first-tag"):
                            self.first_tag = value
                            self.first_tag.value_namespace = name_space
                            self.first_tag.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface"):
                            self.interface = value
                            self.interface.value_namespace = name_space
                            self.interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-xr"):
                            self.interface_xr = value
                            self.interface_xr.value_namespace = name_space
                            self.interface_xr.value_namespace_prefix = name_space_prefix
                        if(value_path == "mtu"):
                            self.mtu = value
                            self.mtu.value_namespace = name_space
                            self.mtu.value_namespace_prefix = name_space_prefix
                        if(value_path == "parent-interface"):
                            self.parent_interface = value
                            self.parent_interface.value_namespace = name_space
                            self.parent_interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "second-tag"):
                            self.second_tag = value
                            self.second_tag.value_namespace = name_space
                            self.second_tag.value_namespace_prefix = name_space_prefix
                        if(value_path == "service"):
                            self.service = value
                            self.service.value_namespace = name_space
                            self.service.value_namespace_prefix = name_space_prefix
                        if(value_path == "state"):
                            self.state = value
                            self.state.value_namespace = name_space
                            self.state.value_namespace_prefix = name_space_prefix
                        if(value_path == "switched-mtu"):
                            self.switched_mtu = value
                            self.switched_mtu.value_namespace = name_space
                            self.switched_mtu.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.tag_allocation:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.tag_allocation:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "tag-allocations" + path_buffer

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

                    if (child_yang_name == "tag-allocation"):
                        for c in self.tag_allocation:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Vlan.Nodes.Node.TagAllocations.TagAllocation()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.tag_allocation.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "tag-allocation"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.node_id.is_set or
                    (self.interfaces is not None and self.interfaces.has_data()) or
                    (self.tag_allocations is not None and self.tag_allocations.has_data()) or
                    (self.trunks is not None and self.trunks.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_id.yfilter != YFilter.not_set or
                    (self.interfaces is not None and self.interfaces.has_operation()) or
                    (self.tag_allocations is not None and self.tag_allocations.has_operation()) or
                    (self.trunks is not None and self.trunks.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-id='" + self.node_id.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-l2-eth-infra-oper:vlan/nodes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.node_id.is_set or self.node_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.node_id.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "interfaces"):
                    if (self.interfaces is None):
                        self.interfaces = Vlan.Nodes.Node.Interfaces()
                        self.interfaces.parent = self
                        self._children_name_map["interfaces"] = "interfaces"
                    return self.interfaces

                if (child_yang_name == "tag-allocations"):
                    if (self.tag_allocations is None):
                        self.tag_allocations = Vlan.Nodes.Node.TagAllocations()
                        self.tag_allocations.parent = self
                        self._children_name_map["tag_allocations"] = "tag-allocations"
                    return self.tag_allocations

                if (child_yang_name == "trunks"):
                    if (self.trunks is None):
                        self.trunks = Vlan.Nodes.Node.Trunks()
                        self.trunks.parent = self
                        self._children_name_map["trunks"] = "trunks"
                    return self.trunks

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "interfaces" or name == "tag-allocations" or name == "trunks" or name == "node-id"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "node-id"):
                    self.node_id = value
                    self.node_id.value_namespace = name_space
                    self.node_id.value_namespace_prefix = name_space_prefix

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
            path_buffer = "nodes" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-l2-eth-infra-oper:vlan/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

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
                c = Vlan.Nodes.Node()
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

    def has_data(self):
        return (self.nodes is not None and self.nodes.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.nodes is not None and self.nodes.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-l2-eth-infra-oper:vlan" + path_buffer

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

        if (child_yang_name == "nodes"):
            if (self.nodes is None):
                self.nodes = Vlan.Nodes()
                self.nodes.parent = self
                self._children_name_map["nodes"] = "nodes"
            return self.nodes

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "nodes"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Vlan()
        return self._top_entity

class EthernetEncapsulation(Entity):
    """
    ethernet encapsulation
    
    .. attribute:: nodes
    
    	Per node Ethernet encapsulation operational data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EthernetEncapsulation.Nodes>`
    
    

    """

    _prefix = 'l2-eth-infra-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(EthernetEncapsulation, self).__init__()
        self._top_entity = None

        self.yang_name = "ethernet-encapsulation"
        self.yang_parent_name = "Cisco-IOS-XR-l2-eth-infra-oper"

        self.nodes = EthernetEncapsulation.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        Per node Ethernet encapsulation operational data
        
        .. attribute:: node
        
        	The Ethernet encaps operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EthernetEncapsulation.Nodes.Node>`
        
        

        """

        _prefix = 'l2-eth-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(EthernetEncapsulation.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "ethernet-encapsulation"

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
                        super(EthernetEncapsulation.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(EthernetEncapsulation.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            The Ethernet encaps operational data for a
            particular node
            
            .. attribute:: node_name  <key>
            
            	The identifier for the node
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: unicast_mac_filters
            
            	Unicast MAC filter table (specific to this node)
            	**type**\:   :py:class:`UnicastMacFilters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EthernetEncapsulation.Nodes.Node.UnicastMacFilters>`
            
            

            """

            _prefix = 'l2-eth-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(EthernetEncapsulation.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.unicast_mac_filters = EthernetEncapsulation.Nodes.Node.UnicastMacFilters()
                self.unicast_mac_filters.parent = self
                self._children_name_map["unicast_mac_filters"] = "unicast-mac-filters"
                self._children_yang_names.add("unicast-mac-filters")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("node_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(EthernetEncapsulation.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(EthernetEncapsulation.Nodes.Node, self).__setattr__(name, value)


            class UnicastMacFilters(Entity):
                """
                Unicast MAC filter table (specific to this
                node)
                
                .. attribute:: unicast_mac_filter
                
                	Operational data for interface with MAC filters configured
                	**type**\: list of    :py:class:`UnicastMacFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EthernetEncapsulation.Nodes.Node.UnicastMacFilters.UnicastMacFilter>`
                
                

                """

                _prefix = 'l2-eth-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(EthernetEncapsulation.Nodes.Node.UnicastMacFilters, self).__init__()

                    self.yang_name = "unicast-mac-filters"
                    self.yang_parent_name = "node"

                    self.unicast_mac_filter = YList(self)

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
                                super(EthernetEncapsulation.Nodes.Node.UnicastMacFilters, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(EthernetEncapsulation.Nodes.Node.UnicastMacFilters, self).__setattr__(name, value)


                class UnicastMacFilter(Entity):
                    """
                    Operational data for interface with MAC
                    filters configured
                    
                    .. attribute:: interface_name  <key>
                    
                    	The interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: unicast_filter
                    
                    	Unicast MAC filter information
                    	**type**\: list of    :py:class:`UnicastFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EthernetEncapsulation.Nodes.Node.UnicastMacFilters.UnicastMacFilter.UnicastFilter>`
                    
                    

                    """

                    _prefix = 'l2-eth-infra-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(EthernetEncapsulation.Nodes.Node.UnicastMacFilters.UnicastMacFilter, self).__init__()

                        self.yang_name = "unicast-mac-filter"
                        self.yang_parent_name = "unicast-mac-filters"

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.unicast_filter = YList(self)

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
                                    super(EthernetEncapsulation.Nodes.Node.UnicastMacFilters.UnicastMacFilter, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(EthernetEncapsulation.Nodes.Node.UnicastMacFilters.UnicastMacFilter, self).__setattr__(name, value)


                    class UnicastFilter(Entity):
                        """
                        Unicast MAC filter information
                        
                        .. attribute:: mac_address
                        
                        	MAC address
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: mode
                        
                        	Unicast MAC mode
                        	**type**\:   :py:class:`EthCapsUcastMacMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper.EthCapsUcastMacMode>`
                        
                        

                        """

                        _prefix = 'l2-eth-infra-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(EthernetEncapsulation.Nodes.Node.UnicastMacFilters.UnicastMacFilter.UnicastFilter, self).__init__()

                            self.yang_name = "unicast-filter"
                            self.yang_parent_name = "unicast-mac-filter"

                            self.mac_address = YLeaf(YType.str, "mac-address")

                            self.mode = YLeaf(YType.enumeration, "mode")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("mac_address",
                                            "mode") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(EthernetEncapsulation.Nodes.Node.UnicastMacFilters.UnicastMacFilter.UnicastFilter, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(EthernetEncapsulation.Nodes.Node.UnicastMacFilters.UnicastMacFilter.UnicastFilter, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.mac_address.is_set or
                                self.mode.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.mac_address.yfilter != YFilter.not_set or
                                self.mode.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "unicast-filter" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.mac_address.is_set or self.mac_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mac_address.get_name_leafdata())
                            if (self.mode.is_set or self.mode.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mode.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "mac-address" or name == "mode"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "mac-address"):
                                self.mac_address = value
                                self.mac_address.value_namespace = name_space
                                self.mac_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "mode"):
                                self.mode = value
                                self.mode.value_namespace = name_space
                                self.mode.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.unicast_filter:
                            if (c.has_data()):
                                return True
                        return self.interface_name.is_set

                    def has_operation(self):
                        for c in self.unicast_filter:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "unicast-mac-filter" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
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

                        if (child_yang_name == "unicast-filter"):
                            for c in self.unicast_filter:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = EthernetEncapsulation.Nodes.Node.UnicastMacFilters.UnicastMacFilter.UnicastFilter()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.unicast_filter.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "unicast-filter" or name == "interface-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.unicast_mac_filter:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.unicast_mac_filter:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "unicast-mac-filters" + path_buffer

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

                    if (child_yang_name == "unicast-mac-filter"):
                        for c in self.unicast_mac_filter:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = EthernetEncapsulation.Nodes.Node.UnicastMacFilters.UnicastMacFilter()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.unicast_mac_filter.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "unicast-mac-filter"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.unicast_mac_filters is not None and self.unicast_mac_filters.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.unicast_mac_filters is not None and self.unicast_mac_filters.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-l2-eth-infra-oper:ethernet-encapsulation/nodes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.node_name.is_set or self.node_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.node_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "unicast-mac-filters"):
                    if (self.unicast_mac_filters is None):
                        self.unicast_mac_filters = EthernetEncapsulation.Nodes.Node.UnicastMacFilters()
                        self.unicast_mac_filters.parent = self
                        self._children_name_map["unicast_mac_filters"] = "unicast-mac-filters"
                    return self.unicast_mac_filters

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "unicast-mac-filters" or name == "node-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "node-name"):
                    self.node_name = value
                    self.node_name.value_namespace = name_space
                    self.node_name.value_namespace_prefix = name_space_prefix

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
            path_buffer = "nodes" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-l2-eth-infra-oper:ethernet-encapsulation/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

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
                c = EthernetEncapsulation.Nodes.Node()
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

    def has_data(self):
        return (self.nodes is not None and self.nodes.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.nodes is not None and self.nodes.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-l2-eth-infra-oper:ethernet-encapsulation" + path_buffer

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

        if (child_yang_name == "nodes"):
            if (self.nodes is None):
                self.nodes = EthernetEncapsulation.Nodes()
                self.nodes.parent = self
                self._children_name_map["nodes"] = "nodes"
            return self.nodes

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "nodes"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = EthernetEncapsulation()
        return self._top_entity


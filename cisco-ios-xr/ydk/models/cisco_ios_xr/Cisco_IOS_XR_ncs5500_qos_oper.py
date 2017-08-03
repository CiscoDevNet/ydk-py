""" Cisco_IOS_XR_ncs5500_qos_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ncs5500\-qos package operational data.

This module contains definitions
for the following management objects\:
  platform\-qos\: DNX QoS EA operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class DnxQoseaShowAction(Enum):
    """
    DnxQoseaShowAction

    Policer action type

    .. data:: action_none = 0

    	None

    .. data:: action_transmit = 1

    	Transmit

    .. data:: action_drop = 2

    	Drop

    .. data:: action_mark = 3

    	Mark

    """

    action_none = Enum.YLeaf(0, "action-none")

    action_transmit = Enum.YLeaf(1, "action-transmit")

    action_drop = Enum.YLeaf(2, "action-drop")

    action_mark = Enum.YLeaf(3, "action-mark")


class DnxQoseaShowHpLevel(Enum):
    """
    DnxQoseaShowHpLevel

    Priority level

    .. data:: high_priority_level1 = 0

    	High priority queue level 1

    .. data:: high_priority_level2 = 1

    	High priority queue level 2

    .. data:: high_priority_level3 = 2

    	High priority queue level 3

    .. data:: high_priority_level4 = 3

    	High priority queue level 4

    .. data:: high_priority_level5 = 4

    	High priority queue level 5

    .. data:: high_priority_level6 = 5

    	High priority queue level 6

    .. data:: high_priority_level7 = 6

    	High priority queue level 7

    .. data:: unknown = 7

    	Unknown

    """

    high_priority_level1 = Enum.YLeaf(0, "high-priority-level1")

    high_priority_level2 = Enum.YLeaf(1, "high-priority-level2")

    high_priority_level3 = Enum.YLeaf(2, "high-priority-level3")

    high_priority_level4 = Enum.YLeaf(3, "high-priority-level4")

    high_priority_level5 = Enum.YLeaf(4, "high-priority-level5")

    high_priority_level6 = Enum.YLeaf(5, "high-priority-level6")

    high_priority_level7 = Enum.YLeaf(6, "high-priority-level7")

    unknown = Enum.YLeaf(7, "unknown")


class DnxQoseaShowIntfStatus(Enum):
    """
    DnxQoseaShowIntfStatus

    Intf Status

    .. data:: state_unknown = 0

    	State is unknown

    .. data:: state_down = 1

    	State is Down

    """

    state_unknown = Enum.YLeaf(0, "state-unknown")

    state_down = Enum.YLeaf(1, "state-down")


class DnxQoseaShowLevel(Enum):
    """
    DnxQoseaShowLevel

    Level type

    .. data:: level1 = 0

    	QoS level1 class

    .. data:: level2 = 1

    	QoS level2 class

    .. data:: level3 = 2

    	QoS level3 class

    .. data:: level4 = 3

    	QoS level4 class

    .. data:: level5 = 4

    	QoS level5 class

    """

    level1 = Enum.YLeaf(0, "level1")

    level2 = Enum.YLeaf(1, "level2")

    level3 = Enum.YLeaf(2, "level3")

    level4 = Enum.YLeaf(3, "level4")

    level5 = Enum.YLeaf(4, "level5")


class DnxQoseaShowMark(Enum):
    """
    DnxQoseaShowMark

    Mark type

    .. data:: mark_none = 0

    	None

    .. data:: dscp = 1

    	DSCP

    .. data:: precedence = 2

    	Precedence

    .. data:: mpls_topmost = 3

    	MPLS topmost

    .. data:: mpls_imposition = 4

    	MPLS imposition

    .. data:: qos_group = 5

    	Qos group

    .. data:: discard_class = 6

    	Discard class

    .. data:: cos = 7

    	COS

    .. data:: inner_cos = 8

    	Inner COS

    .. data:: un_supported9 = 9

    	Unsupported type 9

    .. data:: un_supported10 = 10

    	Unsupported type 10

    .. data:: dscp_tunnel = 11

    	DSCP tunnel

    .. data:: precedence_tunnel = 12

    	Precedence tunnel

    .. data:: dei = 13

    	DEI

    .. data:: dei_imposition = 14

    	DEI Imposition

    """

    mark_none = Enum.YLeaf(0, "mark-none")

    dscp = Enum.YLeaf(1, "dscp")

    precedence = Enum.YLeaf(2, "precedence")

    mpls_topmost = Enum.YLeaf(3, "mpls-topmost")

    mpls_imposition = Enum.YLeaf(4, "mpls-imposition")

    qos_group = Enum.YLeaf(5, "qos-group")

    discard_class = Enum.YLeaf(6, "discard-class")

    cos = Enum.YLeaf(7, "cos")

    inner_cos = Enum.YLeaf(8, "inner-cos")

    un_supported9 = Enum.YLeaf(9, "un-supported9")

    un_supported10 = Enum.YLeaf(10, "un-supported10")

    dscp_tunnel = Enum.YLeaf(11, "dscp-tunnel")

    precedence_tunnel = Enum.YLeaf(12, "precedence-tunnel")

    dei = Enum.YLeaf(13, "dei")

    dei_imposition = Enum.YLeaf(14, "dei-imposition")


class DnxQoseaShowPolicyStatus(Enum):
    """
    DnxQoseaShowPolicyStatus

    Status

    .. data:: no_error = 0

    	No errors

    .. data:: policy_in_reset = 1

    	QoS policy is reset

    """

    no_error = Enum.YLeaf(0, "no-error")

    policy_in_reset = Enum.YLeaf(1, "policy-in-reset")


class DnxQoseaShowQueue(Enum):
    """
    DnxQoseaShowQueue

    Priority Queue Type

    .. data:: low_priority_default_queue = 0

    	Low priority default queue

    .. data:: low_priority_queue = 1

    	Low priority queue

    .. data:: high_priority_queue = 2

    	High priority queue

    .. data:: unknown_queue_type = 3

    	Queue priority unknown

    """

    low_priority_default_queue = Enum.YLeaf(0, "low-priority-default-queue")

    low_priority_queue = Enum.YLeaf(1, "low-priority-queue")

    high_priority_queue = Enum.YLeaf(2, "high-priority-queue")

    unknown_queue_type = Enum.YLeaf(3, "unknown-queue-type")


class DnxQoseaShowWred(Enum):
    """
    DnxQoseaShowWred

    WRED type

    .. data:: wred_cos = 0

    	WRED based on COS

    .. data:: wred_dscp = 1

    	WRED based on DSCP

    .. data:: wred_precedence = 2

    	WRED based on Precedence

    .. data:: wred_discard_class = 3

    	WRED based on discard class

    .. data:: wred_mpls_exp = 4

    	WRED based on MPLS EXP

    .. data:: red_with_user_min_max = 5

    	RED with user defined min and max

    .. data:: red_with_default_min_max = 6

    	RED with default min and max

    .. data:: wred_invalid = 7

    	Invalid

    """

    wred_cos = Enum.YLeaf(0, "wred-cos")

    wred_dscp = Enum.YLeaf(1, "wred-dscp")

    wred_precedence = Enum.YLeaf(2, "wred-precedence")

    wred_discard_class = Enum.YLeaf(3, "wred-discard-class")

    wred_mpls_exp = Enum.YLeaf(4, "wred-mpls-exp")

    red_with_user_min_max = Enum.YLeaf(5, "red-with-user-min-max")

    red_with_default_min_max = Enum.YLeaf(6, "red-with-default-min-max")

    wred_invalid = Enum.YLeaf(7, "wred-invalid")


class PolicyParamUnit(Enum):
    """
    PolicyParamUnit

    Policy param unit

    .. data:: policy_param_unit_invalid = 0

    	policy param unit invalid

    .. data:: policy_param_unit_bytes = 1

    	policy param unit bytes

    .. data:: policy_param_unit_kbytes = 2

    	policy param unit kbytes

    .. data:: policy_param_unit_mbytes = 3

    	policy param unit mbytes

    .. data:: policy_param_unit_gbytes = 4

    	policy param unit gbytes

    .. data:: policy_param_unit_bitsps = 5

    	policy param unit bitsps

    .. data:: policy_param_unit_kbitsps = 6

    	policy param unit kbitsps

    .. data:: policy_param_unit_mbitsps = 7

    	policy param unit mbitsps

    .. data:: policy_param_unit_gbitsps = 8

    	policy param unit gbitsps

    .. data:: policy_param_unit_cells_ps = 9

    	policy param unit cells ps

    .. data:: policy_param_unit_packets_ps = 10

    	policy param unit packets ps

    .. data:: policy_param_unit_us = 11

    	policy param unit us

    .. data:: policy_param_unit_ms = 12

    	policy param unit ms

    .. data:: policy_param_unit_seconds = 13

    	policy param unit seconds

    .. data:: policy_param_unit_packets = 14

    	policy param unit packets

    .. data:: policy_param_unit_cells = 15

    	policy param unit cells

    .. data:: policy_param_unit_percent = 16

    	policy param unit percent

    .. data:: policy_param_unit_per_thousand = 17

    	policy param unit per thousand

    .. data:: policy_param_unit_per_million = 18

    	policy param unit per million

    .. data:: policy_param_unit_hz = 19

    	policy param unit hz

    .. data:: policy_param_unit_khz = 20

    	policy param unit khz

    .. data:: policy_param_unit_mhz = 21

    	policy param unit mhz

    .. data:: policy_param_unit_ratio = 22

    	policy param unit ratio

    .. data:: policy_param_unit_max = 23

    	policy param unit max

    """

    policy_param_unit_invalid = Enum.YLeaf(0, "policy-param-unit-invalid")

    policy_param_unit_bytes = Enum.YLeaf(1, "policy-param-unit-bytes")

    policy_param_unit_kbytes = Enum.YLeaf(2, "policy-param-unit-kbytes")

    policy_param_unit_mbytes = Enum.YLeaf(3, "policy-param-unit-mbytes")

    policy_param_unit_gbytes = Enum.YLeaf(4, "policy-param-unit-gbytes")

    policy_param_unit_bitsps = Enum.YLeaf(5, "policy-param-unit-bitsps")

    policy_param_unit_kbitsps = Enum.YLeaf(6, "policy-param-unit-kbitsps")

    policy_param_unit_mbitsps = Enum.YLeaf(7, "policy-param-unit-mbitsps")

    policy_param_unit_gbitsps = Enum.YLeaf(8, "policy-param-unit-gbitsps")

    policy_param_unit_cells_ps = Enum.YLeaf(9, "policy-param-unit-cells-ps")

    policy_param_unit_packets_ps = Enum.YLeaf(10, "policy-param-unit-packets-ps")

    policy_param_unit_us = Enum.YLeaf(11, "policy-param-unit-us")

    policy_param_unit_ms = Enum.YLeaf(12, "policy-param-unit-ms")

    policy_param_unit_seconds = Enum.YLeaf(13, "policy-param-unit-seconds")

    policy_param_unit_packets = Enum.YLeaf(14, "policy-param-unit-packets")

    policy_param_unit_cells = Enum.YLeaf(15, "policy-param-unit-cells")

    policy_param_unit_percent = Enum.YLeaf(16, "policy-param-unit-percent")

    policy_param_unit_per_thousand = Enum.YLeaf(17, "policy-param-unit-per-thousand")

    policy_param_unit_per_million = Enum.YLeaf(18, "policy-param-unit-per-million")

    policy_param_unit_hz = Enum.YLeaf(19, "policy-param-unit-hz")

    policy_param_unit_khz = Enum.YLeaf(20, "policy-param-unit-khz")

    policy_param_unit_mhz = Enum.YLeaf(21, "policy-param-unit-mhz")

    policy_param_unit_ratio = Enum.YLeaf(22, "policy-param-unit-ratio")

    policy_param_unit_max = Enum.YLeaf(23, "policy-param-unit-max")


class QosPolicyAccountEnum(Enum):
    """
    QosPolicyAccountEnum

    Qos policy account enum

    .. data:: qos_serv_policy_no_ac_count_pref = 0

    	qos serv policy no ac count pref

    .. data:: qos_serv_policy_ac_count_l2 = 1

    	qos serv policy ac count l2

    .. data:: qos_serv_policy_no_ac_count_l2 = 2

    	qos serv policy no ac count l2

    .. data:: qos_serv_policy_ac_count_user_def = 3

    	qos serv policy ac count user def

    .. data:: qos_serv_policy_ac_count_l1 = 4

    	qos serv policy ac count l1

    """

    qos_serv_policy_no_ac_count_pref = Enum.YLeaf(0, "qos-serv-policy-no-ac-count-pref")

    qos_serv_policy_ac_count_l2 = Enum.YLeaf(1, "qos-serv-policy-ac-count-l2")

    qos_serv_policy_no_ac_count_l2 = Enum.YLeaf(2, "qos-serv-policy-no-ac-count-l2")

    qos_serv_policy_ac_count_user_def = Enum.YLeaf(3, "qos-serv-policy-ac-count-user-def")

    qos_serv_policy_ac_count_l1 = Enum.YLeaf(4, "qos-serv-policy-ac-count-l1")



class PlatformQos(Entity):
    """
    DNX QoS EA operational data
    
    .. attribute:: nodes
    
    	List of nodes with platform specific QoS configuration
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes>`
    
    

    """

    _prefix = 'ncs5500-qos-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(PlatformQos, self).__init__()
        self._top_entity = None

        self.yang_name = "platform-qos"
        self.yang_parent_name = "Cisco-IOS-XR-ncs5500-qos-oper"

        self.nodes = PlatformQos.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        List of nodes with platform specific QoS
        configuration
        
        .. attribute:: node
        
        	Node with platform specific QoS configuration
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node>`
        
        

        """

        _prefix = 'ncs5500-qos-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(PlatformQos.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "platform-qos"

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
                        super(PlatformQos.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(PlatformQos.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            Node with platform specific QoS configuration
            
            .. attribute:: node_name  <key>
            
            	Node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: bundle_interfaces
            
            	QoS list of bundle interfaces
            	**type**\:   :py:class:`BundleInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces>`
            
            .. attribute:: interfaces
            
            	QoS list of interfaces
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces>`
            
            .. attribute:: remote_interfaces
            
            	QoS list of remote interfaces
            	**type**\:   :py:class:`RemoteInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.RemoteInterfaces>`
            
            

            """

            _prefix = 'ncs5500-qos-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(PlatformQos.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.bundle_interfaces = PlatformQos.Nodes.Node.BundleInterfaces()
                self.bundle_interfaces.parent = self
                self._children_name_map["bundle_interfaces"] = "bundle-interfaces"
                self._children_yang_names.add("bundle-interfaces")

                self.interfaces = PlatformQos.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._children_yang_names.add("interfaces")

                self.remote_interfaces = PlatformQos.Nodes.Node.RemoteInterfaces()
                self.remote_interfaces.parent = self
                self._children_name_map["remote_interfaces"] = "remote-interfaces"
                self._children_yang_names.add("remote-interfaces")

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
                            super(PlatformQos.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(PlatformQos.Nodes.Node, self).__setattr__(name, value)


            class BundleInterfaces(Entity):
                """
                QoS list of bundle interfaces
                
                .. attribute:: bundle_interface
                
                	QoS interface names
                	**type**\: list of    :py:class:`BundleInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface>`
                
                

                """

                _prefix = 'ncs5500-qos-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PlatformQos.Nodes.Node.BundleInterfaces, self).__init__()

                    self.yang_name = "bundle-interfaces"
                    self.yang_parent_name = "node"

                    self.bundle_interface = YList(self)

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
                                super(PlatformQos.Nodes.Node.BundleInterfaces, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PlatformQos.Nodes.Node.BundleInterfaces, self).__setattr__(name, value)


                class BundleInterface(Entity):
                    """
                    QoS interface names
                    
                    .. attribute:: interface_name  <key>
                    
                    	Bundle interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: classes
                    
                    	QoS list of class names
                    	**type**\:   :py:class:`Classes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes>`
                    
                    .. attribute:: member_interfaces
                    
                    	QoS list of member interfaces
                    	**type**\:   :py:class:`MemberInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces>`
                    
                    .. attribute:: npu_id
                    
                    	NPU ID
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: policy_details
                    
                    	Policy Details
                    	**type**\:   :py:class:`PolicyDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.PolicyDetails>`
                    
                    .. attribute:: qos_direction
                    
                    	The interface direction on which QoS is applied to
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'ncs5500-qos-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface, self).__init__()

                        self.yang_name = "bundle-interface"
                        self.yang_parent_name = "bundle-interfaces"

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.npu_id = YLeaf(YType.int32, "npu-id")

                        self.qos_direction = YLeaf(YType.str, "qos-direction")

                        self.classes = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes()
                        self.classes.parent = self
                        self._children_name_map["classes"] = "classes"
                        self._children_yang_names.add("classes")

                        self.member_interfaces = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces()
                        self.member_interfaces.parent = self
                        self._children_name_map["member_interfaces"] = "member-interfaces"
                        self._children_yang_names.add("member-interfaces")

                        self.policy_details = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.PolicyDetails()
                        self.policy_details.parent = self
                        self._children_name_map["policy_details"] = "policy-details"
                        self._children_yang_names.add("policy-details")

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
                                        "npu_id",
                                        "qos_direction") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface, self).__setattr__(name, value)


                    class MemberInterfaces(Entity):
                        """
                        QoS list of member interfaces
                        
                        .. attribute:: member_interface
                        
                        	QoS interface names
                        	**type**\: list of    :py:class:`MemberInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface>`
                        
                        

                        """

                        _prefix = 'ncs5500-qos-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces, self).__init__()

                            self.yang_name = "member-interfaces"
                            self.yang_parent_name = "bundle-interface"

                            self.member_interface = YList(self)

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
                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces, self).__setattr__(name, value)


                        class MemberInterface(Entity):
                            """
                            QoS interface names
                            
                            .. attribute:: interface_name  <key>
                            
                            	Member interface
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: classes
                            
                            	QoS list of class names
                            	**type**\:   :py:class:`Classes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes>`
                            
                            .. attribute:: policy_details
                            
                            	Policy Details
                            	**type**\:   :py:class:`PolicyDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.PolicyDetails>`
                            
                            

                            """

                            _prefix = 'ncs5500-qos-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface, self).__init__()

                                self.yang_name = "member-interface"
                                self.yang_parent_name = "member-interfaces"

                                self.interface_name = YLeaf(YType.str, "interface-name")

                                self.classes = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes()
                                self.classes.parent = self
                                self._children_name_map["classes"] = "classes"
                                self._children_yang_names.add("classes")

                                self.policy_details = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.PolicyDetails()
                                self.policy_details.parent = self
                                self._children_name_map["policy_details"] = "policy-details"
                                self._children_yang_names.add("policy-details")

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
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface, self).__setattr__(name, value)


                            class PolicyDetails(Entity):
                                """
                                Policy Details
                                
                                .. attribute:: interface_bandwidth_kbps
                                
                                	Interface Bandwidth (in kbps)
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: kbit/s
                                
                                .. attribute:: interface_handle
                                
                                	InterfaceHandle
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: interface_status
                                
                                	Interface Status
                                	**type**\:   :py:class:`DnxQoseaShowIntfStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowIntfStatus>`
                                
                                .. attribute:: npu_id
                                
                                	NPU ID
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: policy_name
                                
                                	Policy name
                                	**type**\:  str
                                
                                	**length:** 0..64
                                
                                .. attribute:: policy_status
                                
                                	Policy Status
                                	**type**\:   :py:class:`DnxQoseaShowPolicyStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowPolicyStatus>`
                                
                                .. attribute:: stats_accounting_type
                                
                                	QoS Statistics Accounting Type
                                	**type**\:   :py:class:`QosPolicyAccountEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.QosPolicyAccountEnum>`
                                
                                .. attribute:: total_number_of_classes
                                
                                	Number of Classes
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: voq_base_address
                                
                                	VOQ base address
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: voq_stats_handle
                                
                                	VOQ stats handle
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.PolicyDetails, self).__init__()

                                    self.yang_name = "policy-details"
                                    self.yang_parent_name = "member-interface"

                                    self.interface_bandwidth_kbps = YLeaf(YType.uint32, "interface-bandwidth-kbps")

                                    self.interface_handle = YLeaf(YType.uint32, "interface-handle")

                                    self.interface_status = YLeaf(YType.enumeration, "interface-status")

                                    self.npu_id = YLeaf(YType.uint32, "npu-id")

                                    self.policy_name = YLeaf(YType.str, "policy-name")

                                    self.policy_status = YLeaf(YType.enumeration, "policy-status")

                                    self.stats_accounting_type = YLeaf(YType.enumeration, "stats-accounting-type")

                                    self.total_number_of_classes = YLeaf(YType.uint16, "total-number-of-classes")

                                    self.voq_base_address = YLeaf(YType.uint32, "voq-base-address")

                                    self.voq_stats_handle = YLeaf(YType.uint64, "voq-stats-handle")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("interface_bandwidth_kbps",
                                                    "interface_handle",
                                                    "interface_status",
                                                    "npu_id",
                                                    "policy_name",
                                                    "policy_status",
                                                    "stats_accounting_type",
                                                    "total_number_of_classes",
                                                    "voq_base_address",
                                                    "voq_stats_handle") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.PolicyDetails, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.PolicyDetails, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.interface_bandwidth_kbps.is_set or
                                        self.interface_handle.is_set or
                                        self.interface_status.is_set or
                                        self.npu_id.is_set or
                                        self.policy_name.is_set or
                                        self.policy_status.is_set or
                                        self.stats_accounting_type.is_set or
                                        self.total_number_of_classes.is_set or
                                        self.voq_base_address.is_set or
                                        self.voq_stats_handle.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.interface_bandwidth_kbps.yfilter != YFilter.not_set or
                                        self.interface_handle.yfilter != YFilter.not_set or
                                        self.interface_status.yfilter != YFilter.not_set or
                                        self.npu_id.yfilter != YFilter.not_set or
                                        self.policy_name.yfilter != YFilter.not_set or
                                        self.policy_status.yfilter != YFilter.not_set or
                                        self.stats_accounting_type.yfilter != YFilter.not_set or
                                        self.total_number_of_classes.yfilter != YFilter.not_set or
                                        self.voq_base_address.yfilter != YFilter.not_set or
                                        self.voq_stats_handle.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "policy-details" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.interface_bandwidth_kbps.is_set or self.interface_bandwidth_kbps.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.interface_bandwidth_kbps.get_name_leafdata())
                                    if (self.interface_handle.is_set or self.interface_handle.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.interface_handle.get_name_leafdata())
                                    if (self.interface_status.is_set or self.interface_status.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.interface_status.get_name_leafdata())
                                    if (self.npu_id.is_set or self.npu_id.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.npu_id.get_name_leafdata())
                                    if (self.policy_name.is_set or self.policy_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.policy_name.get_name_leafdata())
                                    if (self.policy_status.is_set or self.policy_status.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.policy_status.get_name_leafdata())
                                    if (self.stats_accounting_type.is_set or self.stats_accounting_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.stats_accounting_type.get_name_leafdata())
                                    if (self.total_number_of_classes.is_set or self.total_number_of_classes.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.total_number_of_classes.get_name_leafdata())
                                    if (self.voq_base_address.is_set or self.voq_base_address.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.voq_base_address.get_name_leafdata())
                                    if (self.voq_stats_handle.is_set or self.voq_stats_handle.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.voq_stats_handle.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "interface-bandwidth-kbps" or name == "interface-handle" or name == "interface-status" or name == "npu-id" or name == "policy-name" or name == "policy-status" or name == "stats-accounting-type" or name == "total-number-of-classes" or name == "voq-base-address" or name == "voq-stats-handle"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "interface-bandwidth-kbps"):
                                        self.interface_bandwidth_kbps = value
                                        self.interface_bandwidth_kbps.value_namespace = name_space
                                        self.interface_bandwidth_kbps.value_namespace_prefix = name_space_prefix
                                    if(value_path == "interface-handle"):
                                        self.interface_handle = value
                                        self.interface_handle.value_namespace = name_space
                                        self.interface_handle.value_namespace_prefix = name_space_prefix
                                    if(value_path == "interface-status"):
                                        self.interface_status = value
                                        self.interface_status.value_namespace = name_space
                                        self.interface_status.value_namespace_prefix = name_space_prefix
                                    if(value_path == "npu-id"):
                                        self.npu_id = value
                                        self.npu_id.value_namespace = name_space
                                        self.npu_id.value_namespace_prefix = name_space_prefix
                                    if(value_path == "policy-name"):
                                        self.policy_name = value
                                        self.policy_name.value_namespace = name_space
                                        self.policy_name.value_namespace_prefix = name_space_prefix
                                    if(value_path == "policy-status"):
                                        self.policy_status = value
                                        self.policy_status.value_namespace = name_space
                                        self.policy_status.value_namespace_prefix = name_space_prefix
                                    if(value_path == "stats-accounting-type"):
                                        self.stats_accounting_type = value
                                        self.stats_accounting_type.value_namespace = name_space
                                        self.stats_accounting_type.value_namespace_prefix = name_space_prefix
                                    if(value_path == "total-number-of-classes"):
                                        self.total_number_of_classes = value
                                        self.total_number_of_classes.value_namespace = name_space
                                        self.total_number_of_classes.value_namespace_prefix = name_space_prefix
                                    if(value_path == "voq-base-address"):
                                        self.voq_base_address = value
                                        self.voq_base_address.value_namespace = name_space
                                        self.voq_base_address.value_namespace_prefix = name_space_prefix
                                    if(value_path == "voq-stats-handle"):
                                        self.voq_stats_handle = value
                                        self.voq_stats_handle.value_namespace = name_space
                                        self.voq_stats_handle.value_namespace_prefix = name_space_prefix


                            class Classes(Entity):
                                """
                                QoS list of class names
                                
                                .. attribute:: class_
                                
                                	QoS policy class
                                	**type**\: list of    :py:class:`Class_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes, self).__init__()

                                    self.yang_name = "classes"
                                    self.yang_parent_name = "member-interface"

                                    self.class_ = YList(self)

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
                                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes, self).__setattr__(name, value)


                                class Class_(Entity):
                                    """
                                    QoS policy class
                                    
                                    .. attribute:: level_one_class_name  <key>
                                    
                                    	QoS policy class name at level 1
                                    	**type**\:  str
                                    
                                    .. attribute:: class_level
                                    
                                    	Class level
                                    	**type**\:   :py:class:`DnxQoseaShowLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowLevel>`
                                    
                                    .. attribute:: common_mark
                                    
                                    	Common mark
                                    	**type**\: list of    :py:class:`CommonMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.CommonMark>`
                                    
                                    .. attribute:: config_excess_bandwidth_percent
                                    
                                    	Configured excess bandwidth percentage
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**units**\: percentage
                                    
                                    .. attribute:: config_excess_bandwidth_unit
                                    
                                    	Configured excess bandwidth unit
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: config_max_rate
                                    
                                    	Configured maximum rate
                                    	**type**\:   :py:class:`ConfigMaxRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigMaxRate>`
                                    
                                    .. attribute:: config_min_rate
                                    
                                    	Configured minimum rate
                                    	**type**\:   :py:class:`ConfigMinRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigMinRate>`
                                    
                                    .. attribute:: config_policer_average_rate
                                    
                                    	Configured policer average rate
                                    	**type**\:   :py:class:`ConfigPolicerAverageRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerAverageRate>`
                                    
                                    .. attribute:: config_policer_conform_burst
                                    
                                    	Configured policer conform burst
                                    	**type**\:   :py:class:`ConfigPolicerConformBurst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerConformBurst>`
                                    
                                    .. attribute:: config_policer_excess_burst
                                    
                                    	Configured policer excess burst
                                    	**type**\:   :py:class:`ConfigPolicerExcessBurst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerExcessBurst>`
                                    
                                    .. attribute:: config_policer_peak_rate
                                    
                                    	Config policer peak rate
                                    	**type**\:   :py:class:`ConfigPolicerPeakRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerPeakRate>`
                                    
                                    .. attribute:: config_queue_limit
                                    
                                    	Configured queue limit
                                    	**type**\:   :py:class:`ConfigQueueLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigQueueLimit>`
                                    
                                    .. attribute:: conform_action
                                    
                                    	Conform action
                                    	**type**\:   :py:class:`ConformAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConformAction>`
                                    
                                    .. attribute:: egress_queue_id
                                    
                                    	Egress Queue ID
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: exceed_action
                                    
                                    	Exceed action
                                    	**type**\:   :py:class:`ExceedAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ExceedAction>`
                                    
                                    .. attribute:: hardware_excess_bandwidth_weight
                                    
                                    	Hardware excess bandwidth weight
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: hardware_max_rate_kbps
                                    
                                    	Hardware maximum rate in kbps
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**units**\: kbit/s
                                    
                                    .. attribute:: hardware_min_rate_kbps
                                    
                                    	Hardware minimum rate in kbps
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**units**\: kbit/s
                                    
                                    .. attribute:: hardware_policer_average_rate_kbps
                                    
                                    	Hardware policer average in kbps
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**units**\: kbit/s
                                    
                                    .. attribute:: hardware_policer_conform_burst_bytes
                                    
                                    	Hardware policer conform burst
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: hardware_policer_excess_burst_bytes
                                    
                                    	Hardware policer excess burst
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: hardware_policer_peak_rate_kbps
                                    
                                    	Hardware policer peak rate
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: hardware_queue_limit_bytes
                                    
                                    	Hardware queue limit in bytes
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: hardware_queue_limit_microseconds
                                    
                                    	Hardware queue limit in microseconds
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: microsecond
                                    
                                    .. attribute:: ip_mark
                                    
                                    	IP mark
                                    	**type**\: list of    :py:class:`IpMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.IpMark>`
                                    
                                    .. attribute:: level_two_class_name
                                    
                                    	QoS policy child class name at level 2
                                    	**type**\:  str
                                    
                                    .. attribute:: mpls_mark
                                    
                                    	MPLS mark
                                    	**type**\: list of    :py:class:`MplsMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.MplsMark>`
                                    
                                    .. attribute:: network_min_bandwidth_kbps
                                    
                                    	Network minimum Bandwith
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: policer_bucket_id
                                    
                                    	PolicerBucketID
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: policer_stats_handle
                                    
                                    	PolicerStatsHandle
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: priority_level
                                    
                                    	Priority level
                                    	**type**\:   :py:class:`DnxQoseaShowHpLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowHpLevel>`
                                    
                                    .. attribute:: queue_type
                                    
                                    	Queue type
                                    	**type**\:   :py:class:`DnxQoseaShowQueue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowQueue>`
                                    
                                    .. attribute:: violate_action
                                    
                                    	Violate action
                                    	**type**\:   :py:class:`ViolateAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ViolateAction>`
                                    
                                    .. attribute:: wred
                                    
                                    	WRED parameters
                                    	**type**\: list of    :py:class:`Wred <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_, self).__init__()

                                        self.yang_name = "class"
                                        self.yang_parent_name = "classes"

                                        self.level_one_class_name = YLeaf(YType.str, "level-one-class-name")

                                        self.class_level = YLeaf(YType.enumeration, "class-level")

                                        self.config_excess_bandwidth_percent = YLeaf(YType.uint32, "config-excess-bandwidth-percent")

                                        self.config_excess_bandwidth_unit = YLeaf(YType.uint32, "config-excess-bandwidth-unit")

                                        self.egress_queue_id = YLeaf(YType.int32, "egress-queue-id")

                                        self.hardware_excess_bandwidth_weight = YLeaf(YType.uint32, "hardware-excess-bandwidth-weight")

                                        self.hardware_max_rate_kbps = YLeaf(YType.uint32, "hardware-max-rate-kbps")

                                        self.hardware_min_rate_kbps = YLeaf(YType.uint32, "hardware-min-rate-kbps")

                                        self.hardware_policer_average_rate_kbps = YLeaf(YType.uint32, "hardware-policer-average-rate-kbps")

                                        self.hardware_policer_conform_burst_bytes = YLeaf(YType.uint32, "hardware-policer-conform-burst-bytes")

                                        self.hardware_policer_excess_burst_bytes = YLeaf(YType.uint32, "hardware-policer-excess-burst-bytes")

                                        self.hardware_policer_peak_rate_kbps = YLeaf(YType.uint32, "hardware-policer-peak-rate-kbps")

                                        self.hardware_queue_limit_bytes = YLeaf(YType.uint64, "hardware-queue-limit-bytes")

                                        self.hardware_queue_limit_microseconds = YLeaf(YType.uint64, "hardware-queue-limit-microseconds")

                                        self.level_two_class_name = YLeaf(YType.str, "level-two-class-name")

                                        self.network_min_bandwidth_kbps = YLeaf(YType.uint32, "network-min-bandwidth-kbps")

                                        self.policer_bucket_id = YLeaf(YType.uint32, "policer-bucket-id")

                                        self.policer_stats_handle = YLeaf(YType.uint64, "policer-stats-handle")

                                        self.priority_level = YLeaf(YType.enumeration, "priority-level")

                                        self.queue_type = YLeaf(YType.enumeration, "queue-type")

                                        self.config_max_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigMaxRate()
                                        self.config_max_rate.parent = self
                                        self._children_name_map["config_max_rate"] = "config-max-rate"
                                        self._children_yang_names.add("config-max-rate")

                                        self.config_min_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigMinRate()
                                        self.config_min_rate.parent = self
                                        self._children_name_map["config_min_rate"] = "config-min-rate"
                                        self._children_yang_names.add("config-min-rate")

                                        self.config_policer_average_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerAverageRate()
                                        self.config_policer_average_rate.parent = self
                                        self._children_name_map["config_policer_average_rate"] = "config-policer-average-rate"
                                        self._children_yang_names.add("config-policer-average-rate")

                                        self.config_policer_conform_burst = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerConformBurst()
                                        self.config_policer_conform_burst.parent = self
                                        self._children_name_map["config_policer_conform_burst"] = "config-policer-conform-burst"
                                        self._children_yang_names.add("config-policer-conform-burst")

                                        self.config_policer_excess_burst = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerExcessBurst()
                                        self.config_policer_excess_burst.parent = self
                                        self._children_name_map["config_policer_excess_burst"] = "config-policer-excess-burst"
                                        self._children_yang_names.add("config-policer-excess-burst")

                                        self.config_policer_peak_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerPeakRate()
                                        self.config_policer_peak_rate.parent = self
                                        self._children_name_map["config_policer_peak_rate"] = "config-policer-peak-rate"
                                        self._children_yang_names.add("config-policer-peak-rate")

                                        self.config_queue_limit = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigQueueLimit()
                                        self.config_queue_limit.parent = self
                                        self._children_name_map["config_queue_limit"] = "config-queue-limit"
                                        self._children_yang_names.add("config-queue-limit")

                                        self.conform_action = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConformAction()
                                        self.conform_action.parent = self
                                        self._children_name_map["conform_action"] = "conform-action"
                                        self._children_yang_names.add("conform-action")

                                        self.exceed_action = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ExceedAction()
                                        self.exceed_action.parent = self
                                        self._children_name_map["exceed_action"] = "exceed-action"
                                        self._children_yang_names.add("exceed-action")

                                        self.violate_action = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ViolateAction()
                                        self.violate_action.parent = self
                                        self._children_name_map["violate_action"] = "violate-action"
                                        self._children_yang_names.add("violate-action")

                                        self.common_mark = YList(self)
                                        self.ip_mark = YList(self)
                                        self.mpls_mark = YList(self)
                                        self.wred = YList(self)

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("level_one_class_name",
                                                        "class_level",
                                                        "config_excess_bandwidth_percent",
                                                        "config_excess_bandwidth_unit",
                                                        "egress_queue_id",
                                                        "hardware_excess_bandwidth_weight",
                                                        "hardware_max_rate_kbps",
                                                        "hardware_min_rate_kbps",
                                                        "hardware_policer_average_rate_kbps",
                                                        "hardware_policer_conform_burst_bytes",
                                                        "hardware_policer_excess_burst_bytes",
                                                        "hardware_policer_peak_rate_kbps",
                                                        "hardware_queue_limit_bytes",
                                                        "hardware_queue_limit_microseconds",
                                                        "level_two_class_name",
                                                        "network_min_bandwidth_kbps",
                                                        "policer_bucket_id",
                                                        "policer_stats_handle",
                                                        "priority_level",
                                                        "queue_type") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_, self).__setattr__(name, value)


                                    class ConfigMaxRate(Entity):
                                        """
                                        Configured maximum rate
                                        
                                        .. attribute:: policy_unit
                                        
                                        	Policy unit
                                        	**type**\:   :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                        
                                        .. attribute:: policy_value
                                        
                                        	Policy value
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigMaxRate, self).__init__()

                                            self.yang_name = "config-max-rate"
                                            self.yang_parent_name = "class"

                                            self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                            self.policy_value = YLeaf(YType.uint32, "policy-value")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("policy_unit",
                                                            "policy_value") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigMaxRate, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigMaxRate, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.policy_unit.is_set or
                                                self.policy_value.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.policy_unit.yfilter != YFilter.not_set or
                                                self.policy_value.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "config-max-rate" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.policy_unit.is_set or self.policy_unit.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.policy_unit.get_name_leafdata())
                                            if (self.policy_value.is_set or self.policy_value.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.policy_value.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "policy-unit" or name == "policy-value"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "policy-unit"):
                                                self.policy_unit = value
                                                self.policy_unit.value_namespace = name_space
                                                self.policy_unit.value_namespace_prefix = name_space_prefix
                                            if(value_path == "policy-value"):
                                                self.policy_value = value
                                                self.policy_value.value_namespace = name_space
                                                self.policy_value.value_namespace_prefix = name_space_prefix


                                    class ConfigMinRate(Entity):
                                        """
                                        Configured minimum rate
                                        
                                        .. attribute:: policy_unit
                                        
                                        	Policy unit
                                        	**type**\:   :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                        
                                        .. attribute:: policy_value
                                        
                                        	Policy value
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigMinRate, self).__init__()

                                            self.yang_name = "config-min-rate"
                                            self.yang_parent_name = "class"

                                            self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                            self.policy_value = YLeaf(YType.uint32, "policy-value")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("policy_unit",
                                                            "policy_value") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigMinRate, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigMinRate, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.policy_unit.is_set or
                                                self.policy_value.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.policy_unit.yfilter != YFilter.not_set or
                                                self.policy_value.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "config-min-rate" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.policy_unit.is_set or self.policy_unit.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.policy_unit.get_name_leafdata())
                                            if (self.policy_value.is_set or self.policy_value.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.policy_value.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "policy-unit" or name == "policy-value"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "policy-unit"):
                                                self.policy_unit = value
                                                self.policy_unit.value_namespace = name_space
                                                self.policy_unit.value_namespace_prefix = name_space_prefix
                                            if(value_path == "policy-value"):
                                                self.policy_value = value
                                                self.policy_value.value_namespace = name_space
                                                self.policy_value.value_namespace_prefix = name_space_prefix


                                    class ConfigQueueLimit(Entity):
                                        """
                                        Configured queue limit
                                        
                                        .. attribute:: policy_unit
                                        
                                        	Policy unit
                                        	**type**\:   :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                        
                                        .. attribute:: policy_value
                                        
                                        	Policy value
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigQueueLimit, self).__init__()

                                            self.yang_name = "config-queue-limit"
                                            self.yang_parent_name = "class"

                                            self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                            self.policy_value = YLeaf(YType.uint32, "policy-value")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("policy_unit",
                                                            "policy_value") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigQueueLimit, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigQueueLimit, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.policy_unit.is_set or
                                                self.policy_value.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.policy_unit.yfilter != YFilter.not_set or
                                                self.policy_value.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "config-queue-limit" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.policy_unit.is_set or self.policy_unit.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.policy_unit.get_name_leafdata())
                                            if (self.policy_value.is_set or self.policy_value.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.policy_value.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "policy-unit" or name == "policy-value"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "policy-unit"):
                                                self.policy_unit = value
                                                self.policy_unit.value_namespace = name_space
                                                self.policy_unit.value_namespace_prefix = name_space_prefix
                                            if(value_path == "policy-value"):
                                                self.policy_value = value
                                                self.policy_value.value_namespace = name_space
                                                self.policy_value.value_namespace_prefix = name_space_prefix


                                    class ConfigPolicerAverageRate(Entity):
                                        """
                                        Configured policer average rate
                                        
                                        .. attribute:: policy_unit
                                        
                                        	Policy unit
                                        	**type**\:   :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                        
                                        .. attribute:: policy_value
                                        
                                        	Policy value
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerAverageRate, self).__init__()

                                            self.yang_name = "config-policer-average-rate"
                                            self.yang_parent_name = "class"

                                            self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                            self.policy_value = YLeaf(YType.uint32, "policy-value")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("policy_unit",
                                                            "policy_value") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerAverageRate, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerAverageRate, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.policy_unit.is_set or
                                                self.policy_value.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.policy_unit.yfilter != YFilter.not_set or
                                                self.policy_value.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "config-policer-average-rate" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.policy_unit.is_set or self.policy_unit.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.policy_unit.get_name_leafdata())
                                            if (self.policy_value.is_set or self.policy_value.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.policy_value.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "policy-unit" or name == "policy-value"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "policy-unit"):
                                                self.policy_unit = value
                                                self.policy_unit.value_namespace = name_space
                                                self.policy_unit.value_namespace_prefix = name_space_prefix
                                            if(value_path == "policy-value"):
                                                self.policy_value = value
                                                self.policy_value.value_namespace = name_space
                                                self.policy_value.value_namespace_prefix = name_space_prefix


                                    class ConfigPolicerPeakRate(Entity):
                                        """
                                        Config policer peak rate
                                        
                                        .. attribute:: policy_unit
                                        
                                        	Policy unit
                                        	**type**\:   :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                        
                                        .. attribute:: policy_value
                                        
                                        	Policy value
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerPeakRate, self).__init__()

                                            self.yang_name = "config-policer-peak-rate"
                                            self.yang_parent_name = "class"

                                            self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                            self.policy_value = YLeaf(YType.uint32, "policy-value")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("policy_unit",
                                                            "policy_value") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerPeakRate, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerPeakRate, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.policy_unit.is_set or
                                                self.policy_value.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.policy_unit.yfilter != YFilter.not_set or
                                                self.policy_value.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "config-policer-peak-rate" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.policy_unit.is_set or self.policy_unit.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.policy_unit.get_name_leafdata())
                                            if (self.policy_value.is_set or self.policy_value.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.policy_value.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "policy-unit" or name == "policy-value"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "policy-unit"):
                                                self.policy_unit = value
                                                self.policy_unit.value_namespace = name_space
                                                self.policy_unit.value_namespace_prefix = name_space_prefix
                                            if(value_path == "policy-value"):
                                                self.policy_value = value
                                                self.policy_value.value_namespace = name_space
                                                self.policy_value.value_namespace_prefix = name_space_prefix


                                    class ConfigPolicerConformBurst(Entity):
                                        """
                                        Configured policer conform burst
                                        
                                        .. attribute:: policy_unit
                                        
                                        	Policy unit
                                        	**type**\:   :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                        
                                        .. attribute:: policy_value
                                        
                                        	Policy value
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerConformBurst, self).__init__()

                                            self.yang_name = "config-policer-conform-burst"
                                            self.yang_parent_name = "class"

                                            self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                            self.policy_value = YLeaf(YType.uint32, "policy-value")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("policy_unit",
                                                            "policy_value") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerConformBurst, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerConformBurst, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.policy_unit.is_set or
                                                self.policy_value.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.policy_unit.yfilter != YFilter.not_set or
                                                self.policy_value.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "config-policer-conform-burst" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.policy_unit.is_set or self.policy_unit.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.policy_unit.get_name_leafdata())
                                            if (self.policy_value.is_set or self.policy_value.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.policy_value.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "policy-unit" or name == "policy-value"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "policy-unit"):
                                                self.policy_unit = value
                                                self.policy_unit.value_namespace = name_space
                                                self.policy_unit.value_namespace_prefix = name_space_prefix
                                            if(value_path == "policy-value"):
                                                self.policy_value = value
                                                self.policy_value.value_namespace = name_space
                                                self.policy_value.value_namespace_prefix = name_space_prefix


                                    class ConfigPolicerExcessBurst(Entity):
                                        """
                                        Configured policer excess burst
                                        
                                        .. attribute:: policy_unit
                                        
                                        	Policy unit
                                        	**type**\:   :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                        
                                        .. attribute:: policy_value
                                        
                                        	Policy value
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerExcessBurst, self).__init__()

                                            self.yang_name = "config-policer-excess-burst"
                                            self.yang_parent_name = "class"

                                            self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                            self.policy_value = YLeaf(YType.uint32, "policy-value")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("policy_unit",
                                                            "policy_value") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerExcessBurst, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerExcessBurst, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.policy_unit.is_set or
                                                self.policy_value.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.policy_unit.yfilter != YFilter.not_set or
                                                self.policy_value.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "config-policer-excess-burst" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.policy_unit.is_set or self.policy_unit.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.policy_unit.get_name_leafdata())
                                            if (self.policy_value.is_set or self.policy_value.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.policy_value.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "policy-unit" or name == "policy-value"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "policy-unit"):
                                                self.policy_unit = value
                                                self.policy_unit.value_namespace = name_space
                                                self.policy_unit.value_namespace_prefix = name_space_prefix
                                            if(value_path == "policy-value"):
                                                self.policy_value = value
                                                self.policy_value.value_namespace = name_space
                                                self.policy_value.value_namespace_prefix = name_space_prefix


                                    class ConformAction(Entity):
                                        """
                                        Conform action
                                        
                                        .. attribute:: action_type
                                        
                                        	Policer action type
                                        	**type**\:   :py:class:`DnxQoseaShowAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowAction>`
                                        
                                        .. attribute:: mark
                                        
                                        	Action mark
                                        	**type**\: list of    :py:class:`Mark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConformAction.Mark>`
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConformAction, self).__init__()

                                            self.yang_name = "conform-action"
                                            self.yang_parent_name = "class"

                                            self.action_type = YLeaf(YType.enumeration, "action-type")

                                            self.mark = YList(self)

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
                                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConformAction, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConformAction, self).__setattr__(name, value)


                                        class Mark(Entity):
                                            """
                                            Action mark
                                            
                                            .. attribute:: mark_type
                                            
                                            	Mark type
                                            	**type**\:   :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                            
                                            .. attribute:: mark_value
                                            
                                            	Mark value
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            

                                            """

                                            _prefix = 'ncs5500-qos-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConformAction.Mark, self).__init__()

                                                self.yang_name = "mark"
                                                self.yang_parent_name = "conform-action"

                                                self.mark_type = YLeaf(YType.enumeration, "mark-type")

                                                self.mark_value = YLeaf(YType.uint16, "mark-value")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("mark_type",
                                                                "mark_value") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConformAction.Mark, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConformAction.Mark, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.mark_type.is_set or
                                                    self.mark_value.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.mark_type.yfilter != YFilter.not_set or
                                                    self.mark_value.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "mark" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.mark_type.is_set or self.mark_type.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.mark_type.get_name_leafdata())
                                                if (self.mark_value.is_set or self.mark_value.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.mark_value.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "mark-type" or name == "mark-value"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "mark-type"):
                                                    self.mark_type = value
                                                    self.mark_type.value_namespace = name_space
                                                    self.mark_type.value_namespace_prefix = name_space_prefix
                                                if(value_path == "mark-value"):
                                                    self.mark_value = value
                                                    self.mark_value.value_namespace = name_space
                                                    self.mark_value.value_namespace_prefix = name_space_prefix

                                        def has_data(self):
                                            for c in self.mark:
                                                if (c.has_data()):
                                                    return True
                                            return self.action_type.is_set

                                        def has_operation(self):
                                            for c in self.mark:
                                                if (c.has_operation()):
                                                    return True
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.action_type.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "conform-action" + path_buffer

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

                                            if (child_yang_name == "mark"):
                                                for c in self.mark:
                                                    segment = c.get_segment_path()
                                                    if (segment_path == segment):
                                                        return c
                                                c = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConformAction.Mark()
                                                c.parent = self
                                                local_reference_key = "ydk::seg::%s" % segment_path
                                                self._local_refs[local_reference_key] = c
                                                self.mark.append(c)
                                                return c

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "mark" or name == "action-type"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "action-type"):
                                                self.action_type = value
                                                self.action_type.value_namespace = name_space
                                                self.action_type.value_namespace_prefix = name_space_prefix


                                    class ExceedAction(Entity):
                                        """
                                        Exceed action
                                        
                                        .. attribute:: action_type
                                        
                                        	Policer action type
                                        	**type**\:   :py:class:`DnxQoseaShowAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowAction>`
                                        
                                        .. attribute:: mark
                                        
                                        	Action mark
                                        	**type**\: list of    :py:class:`Mark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ExceedAction.Mark>`
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ExceedAction, self).__init__()

                                            self.yang_name = "exceed-action"
                                            self.yang_parent_name = "class"

                                            self.action_type = YLeaf(YType.enumeration, "action-type")

                                            self.mark = YList(self)

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
                                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ExceedAction, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ExceedAction, self).__setattr__(name, value)


                                        class Mark(Entity):
                                            """
                                            Action mark
                                            
                                            .. attribute:: mark_type
                                            
                                            	Mark type
                                            	**type**\:   :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                            
                                            .. attribute:: mark_value
                                            
                                            	Mark value
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            

                                            """

                                            _prefix = 'ncs5500-qos-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ExceedAction.Mark, self).__init__()

                                                self.yang_name = "mark"
                                                self.yang_parent_name = "exceed-action"

                                                self.mark_type = YLeaf(YType.enumeration, "mark-type")

                                                self.mark_value = YLeaf(YType.uint16, "mark-value")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("mark_type",
                                                                "mark_value") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ExceedAction.Mark, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ExceedAction.Mark, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.mark_type.is_set or
                                                    self.mark_value.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.mark_type.yfilter != YFilter.not_set or
                                                    self.mark_value.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "mark" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.mark_type.is_set or self.mark_type.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.mark_type.get_name_leafdata())
                                                if (self.mark_value.is_set or self.mark_value.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.mark_value.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "mark-type" or name == "mark-value"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "mark-type"):
                                                    self.mark_type = value
                                                    self.mark_type.value_namespace = name_space
                                                    self.mark_type.value_namespace_prefix = name_space_prefix
                                                if(value_path == "mark-value"):
                                                    self.mark_value = value
                                                    self.mark_value.value_namespace = name_space
                                                    self.mark_value.value_namespace_prefix = name_space_prefix

                                        def has_data(self):
                                            for c in self.mark:
                                                if (c.has_data()):
                                                    return True
                                            return self.action_type.is_set

                                        def has_operation(self):
                                            for c in self.mark:
                                                if (c.has_operation()):
                                                    return True
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.action_type.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "exceed-action" + path_buffer

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

                                            if (child_yang_name == "mark"):
                                                for c in self.mark:
                                                    segment = c.get_segment_path()
                                                    if (segment_path == segment):
                                                        return c
                                                c = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ExceedAction.Mark()
                                                c.parent = self
                                                local_reference_key = "ydk::seg::%s" % segment_path
                                                self._local_refs[local_reference_key] = c
                                                self.mark.append(c)
                                                return c

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "mark" or name == "action-type"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "action-type"):
                                                self.action_type = value
                                                self.action_type.value_namespace = name_space
                                                self.action_type.value_namespace_prefix = name_space_prefix


                                    class ViolateAction(Entity):
                                        """
                                        Violate action
                                        
                                        .. attribute:: action_type
                                        
                                        	Policer action type
                                        	**type**\:   :py:class:`DnxQoseaShowAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowAction>`
                                        
                                        .. attribute:: mark
                                        
                                        	Action mark
                                        	**type**\: list of    :py:class:`Mark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ViolateAction.Mark>`
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ViolateAction, self).__init__()

                                            self.yang_name = "violate-action"
                                            self.yang_parent_name = "class"

                                            self.action_type = YLeaf(YType.enumeration, "action-type")

                                            self.mark = YList(self)

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
                                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ViolateAction, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ViolateAction, self).__setattr__(name, value)


                                        class Mark(Entity):
                                            """
                                            Action mark
                                            
                                            .. attribute:: mark_type
                                            
                                            	Mark type
                                            	**type**\:   :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                            
                                            .. attribute:: mark_value
                                            
                                            	Mark value
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            

                                            """

                                            _prefix = 'ncs5500-qos-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ViolateAction.Mark, self).__init__()

                                                self.yang_name = "mark"
                                                self.yang_parent_name = "violate-action"

                                                self.mark_type = YLeaf(YType.enumeration, "mark-type")

                                                self.mark_value = YLeaf(YType.uint16, "mark-value")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("mark_type",
                                                                "mark_value") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ViolateAction.Mark, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ViolateAction.Mark, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.mark_type.is_set or
                                                    self.mark_value.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.mark_type.yfilter != YFilter.not_set or
                                                    self.mark_value.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "mark" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.mark_type.is_set or self.mark_type.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.mark_type.get_name_leafdata())
                                                if (self.mark_value.is_set or self.mark_value.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.mark_value.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "mark-type" or name == "mark-value"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "mark-type"):
                                                    self.mark_type = value
                                                    self.mark_type.value_namespace = name_space
                                                    self.mark_type.value_namespace_prefix = name_space_prefix
                                                if(value_path == "mark-value"):
                                                    self.mark_value = value
                                                    self.mark_value.value_namespace = name_space
                                                    self.mark_value.value_namespace_prefix = name_space_prefix

                                        def has_data(self):
                                            for c in self.mark:
                                                if (c.has_data()):
                                                    return True
                                            return self.action_type.is_set

                                        def has_operation(self):
                                            for c in self.mark:
                                                if (c.has_operation()):
                                                    return True
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.action_type.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "violate-action" + path_buffer

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

                                            if (child_yang_name == "mark"):
                                                for c in self.mark:
                                                    segment = c.get_segment_path()
                                                    if (segment_path == segment):
                                                        return c
                                                c = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ViolateAction.Mark()
                                                c.parent = self
                                                local_reference_key = "ydk::seg::%s" % segment_path
                                                self._local_refs[local_reference_key] = c
                                                self.mark.append(c)
                                                return c

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "mark" or name == "action-type"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "action-type"):
                                                self.action_type = value
                                                self.action_type.value_namespace = name_space
                                                self.action_type.value_namespace_prefix = name_space_prefix


                                    class IpMark(Entity):
                                        """
                                        IP mark
                                        
                                        .. attribute:: mark_type
                                        
                                        	Mark type
                                        	**type**\:   :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                        
                                        .. attribute:: mark_value
                                        
                                        	Mark value
                                        	**type**\:  int
                                        
                                        	**range:** 0..65535
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.IpMark, self).__init__()

                                            self.yang_name = "ip-mark"
                                            self.yang_parent_name = "class"

                                            self.mark_type = YLeaf(YType.enumeration, "mark-type")

                                            self.mark_value = YLeaf(YType.uint16, "mark-value")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("mark_type",
                                                            "mark_value") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.IpMark, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.IpMark, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.mark_type.is_set or
                                                self.mark_value.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.mark_type.yfilter != YFilter.not_set or
                                                self.mark_value.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "ip-mark" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.mark_type.is_set or self.mark_type.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.mark_type.get_name_leafdata())
                                            if (self.mark_value.is_set or self.mark_value.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.mark_value.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "mark-type" or name == "mark-value"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "mark-type"):
                                                self.mark_type = value
                                                self.mark_type.value_namespace = name_space
                                                self.mark_type.value_namespace_prefix = name_space_prefix
                                            if(value_path == "mark-value"):
                                                self.mark_value = value
                                                self.mark_value.value_namespace = name_space
                                                self.mark_value.value_namespace_prefix = name_space_prefix


                                    class CommonMark(Entity):
                                        """
                                        Common mark
                                        
                                        .. attribute:: mark_type
                                        
                                        	Mark type
                                        	**type**\:   :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                        
                                        .. attribute:: mark_value
                                        
                                        	Mark value
                                        	**type**\:  int
                                        
                                        	**range:** 0..65535
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.CommonMark, self).__init__()

                                            self.yang_name = "common-mark"
                                            self.yang_parent_name = "class"

                                            self.mark_type = YLeaf(YType.enumeration, "mark-type")

                                            self.mark_value = YLeaf(YType.uint16, "mark-value")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("mark_type",
                                                            "mark_value") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.CommonMark, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.CommonMark, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.mark_type.is_set or
                                                self.mark_value.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.mark_type.yfilter != YFilter.not_set or
                                                self.mark_value.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "common-mark" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.mark_type.is_set or self.mark_type.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.mark_type.get_name_leafdata())
                                            if (self.mark_value.is_set or self.mark_value.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.mark_value.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "mark-type" or name == "mark-value"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "mark-type"):
                                                self.mark_type = value
                                                self.mark_type.value_namespace = name_space
                                                self.mark_type.value_namespace_prefix = name_space_prefix
                                            if(value_path == "mark-value"):
                                                self.mark_value = value
                                                self.mark_value.value_namespace = name_space
                                                self.mark_value.value_namespace_prefix = name_space_prefix


                                    class MplsMark(Entity):
                                        """
                                        MPLS mark
                                        
                                        .. attribute:: mark_type
                                        
                                        	Mark type
                                        	**type**\:   :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                        
                                        .. attribute:: mark_value
                                        
                                        	Mark value
                                        	**type**\:  int
                                        
                                        	**range:** 0..65535
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.MplsMark, self).__init__()

                                            self.yang_name = "mpls-mark"
                                            self.yang_parent_name = "class"

                                            self.mark_type = YLeaf(YType.enumeration, "mark-type")

                                            self.mark_value = YLeaf(YType.uint16, "mark-value")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("mark_type",
                                                            "mark_value") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.MplsMark, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.MplsMark, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.mark_type.is_set or
                                                self.mark_value.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.mark_type.yfilter != YFilter.not_set or
                                                self.mark_value.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "mpls-mark" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.mark_type.is_set or self.mark_type.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.mark_type.get_name_leafdata())
                                            if (self.mark_value.is_set or self.mark_value.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.mark_value.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "mark-type" or name == "mark-value"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "mark-type"):
                                                self.mark_type = value
                                                self.mark_type.value_namespace = name_space
                                                self.mark_type.value_namespace_prefix = name_space_prefix
                                            if(value_path == "mark-value"):
                                                self.mark_value = value
                                                self.mark_value.value_namespace = name_space
                                                self.mark_value.value_namespace_prefix = name_space_prefix


                                    class Wred(Entity):
                                        """
                                        WRED parameters
                                        
                                        .. attribute:: config_max_threshold
                                        
                                        	Configured maximum threshold
                                        	**type**\:   :py:class:`ConfigMaxThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.ConfigMaxThreshold>`
                                        
                                        .. attribute:: config_min_threshold
                                        
                                        	Configured minimum threshold
                                        	**type**\:   :py:class:`ConfigMinThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.ConfigMinThreshold>`
                                        
                                        .. attribute:: first_segment
                                        
                                        	First segment
                                        	**type**\:  int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: hardware_max_threshold_bytes
                                        
                                        	Hardware maximum threshold
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: hardware_min_threshold_bytes
                                        
                                        	Hardware minimum threshold
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: segment_size
                                        
                                        	Segment size
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: wred_match_type
                                        
                                        	WREDMatchType
                                        	**type**\:   :py:class:`DnxQoseaShowWred <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowWred>`
                                        
                                        .. attribute:: wred_match_value
                                        
                                        	WRED match values
                                        	**type**\:   :py:class:`WredMatchValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.WredMatchValue>`
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred, self).__init__()

                                            self.yang_name = "wred"
                                            self.yang_parent_name = "class"

                                            self.first_segment = YLeaf(YType.uint16, "first-segment")

                                            self.hardware_max_threshold_bytes = YLeaf(YType.uint32, "hardware-max-threshold-bytes")

                                            self.hardware_min_threshold_bytes = YLeaf(YType.uint32, "hardware-min-threshold-bytes")

                                            self.segment_size = YLeaf(YType.uint32, "segment-size")

                                            self.wred_match_type = YLeaf(YType.enumeration, "wred-match-type")

                                            self.config_max_threshold = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.ConfigMaxThreshold()
                                            self.config_max_threshold.parent = self
                                            self._children_name_map["config_max_threshold"] = "config-max-threshold"
                                            self._children_yang_names.add("config-max-threshold")

                                            self.config_min_threshold = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.ConfigMinThreshold()
                                            self.config_min_threshold.parent = self
                                            self._children_name_map["config_min_threshold"] = "config-min-threshold"
                                            self._children_yang_names.add("config-min-threshold")

                                            self.wred_match_value = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.WredMatchValue()
                                            self.wred_match_value.parent = self
                                            self._children_name_map["wred_match_value"] = "wred-match-value"
                                            self._children_yang_names.add("wred-match-value")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("first_segment",
                                                            "hardware_max_threshold_bytes",
                                                            "hardware_min_threshold_bytes",
                                                            "segment_size",
                                                            "wred_match_type") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred, self).__setattr__(name, value)


                                        class WredMatchValue(Entity):
                                            """
                                            WRED match values
                                            
                                            .. attribute:: dnx_qosea_show_red_match_value
                                            
                                            	dnx qosea show red match value
                                            	**type**\: list of    :py:class:`DnxQoseaShowRedMatchValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.WredMatchValue.DnxQoseaShowRedMatchValue>`
                                            
                                            

                                            """

                                            _prefix = 'ncs5500-qos-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.WredMatchValue, self).__init__()

                                                self.yang_name = "wred-match-value"
                                                self.yang_parent_name = "wred"

                                                self.dnx_qosea_show_red_match_value = YList(self)

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
                                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.WredMatchValue, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.WredMatchValue, self).__setattr__(name, value)


                                            class DnxQoseaShowRedMatchValue(Entity):
                                                """
                                                dnx qosea show red match value
                                                
                                                .. attribute:: range_end
                                                
                                                	End value of a range
                                                	**type**\:  int
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: range_start
                                                
                                                	Start value of a range
                                                	**type**\:  int
                                                
                                                	**range:** 0..255
                                                
                                                

                                                """

                                                _prefix = 'ncs5500-qos-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.WredMatchValue.DnxQoseaShowRedMatchValue, self).__init__()

                                                    self.yang_name = "dnx-qosea-show-red-match-value"
                                                    self.yang_parent_name = "wred-match-value"

                                                    self.range_end = YLeaf(YType.uint8, "range-end")

                                                    self.range_start = YLeaf(YType.uint8, "range-start")

                                                def __setattr__(self, name, value):
                                                    self._check_monkey_patching_error(name, value)
                                                    with _handle_type_error():
                                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                "Please use list append or extend method."
                                                                                .format(value))
                                                        if isinstance(value, Enum.YLeaf):
                                                            value = value.name
                                                        if name in ("range_end",
                                                                    "range_start") and name in self.__dict__:
                                                            if isinstance(value, YLeaf):
                                                                self.__dict__[name].set(value.get())
                                                            elif isinstance(value, YLeafList):
                                                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.WredMatchValue.DnxQoseaShowRedMatchValue, self).__setattr__(name, value)
                                                            else:
                                                                self.__dict__[name].set(value)
                                                        else:
                                                            if hasattr(value, "parent") and name != "parent":
                                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                    value.parent = self
                                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                    value.parent = self
                                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.WredMatchValue.DnxQoseaShowRedMatchValue, self).__setattr__(name, value)

                                                def has_data(self):
                                                    return (
                                                        self.range_end.is_set or
                                                        self.range_start.is_set)

                                                def has_operation(self):
                                                    return (
                                                        self.yfilter != YFilter.not_set or
                                                        self.range_end.yfilter != YFilter.not_set or
                                                        self.range_start.yfilter != YFilter.not_set)

                                                def get_segment_path(self):
                                                    path_buffer = ""
                                                    path_buffer = "dnx-qosea-show-red-match-value" + path_buffer

                                                    return path_buffer

                                                def get_entity_path(self, ancestor):
                                                    path_buffer = ""
                                                    if (ancestor is None):
                                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                    else:
                                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                    leaf_name_data = LeafDataList()
                                                    if (self.range_end.is_set or self.range_end.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.range_end.get_name_leafdata())
                                                    if (self.range_start.is_set or self.range_start.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.range_start.get_name_leafdata())

                                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                                    return entity_path

                                                def get_child_by_name(self, child_yang_name, segment_path):
                                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                    if child is not None:
                                                        return child

                                                    return None

                                                def has_leaf_or_child_of_name(self, name):
                                                    if(name == "range-end" or name == "range-start"):
                                                        return True
                                                    return False

                                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                                    if(value_path == "range-end"):
                                                        self.range_end = value
                                                        self.range_end.value_namespace = name_space
                                                        self.range_end.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "range-start"):
                                                        self.range_start = value
                                                        self.range_start.value_namespace = name_space
                                                        self.range_start.value_namespace_prefix = name_space_prefix

                                            def has_data(self):
                                                for c in self.dnx_qosea_show_red_match_value:
                                                    if (c.has_data()):
                                                        return True
                                                return False

                                            def has_operation(self):
                                                for c in self.dnx_qosea_show_red_match_value:
                                                    if (c.has_operation()):
                                                        return True
                                                return self.yfilter != YFilter.not_set

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "wred-match-value" + path_buffer

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

                                                if (child_yang_name == "dnx-qosea-show-red-match-value"):
                                                    for c in self.dnx_qosea_show_red_match_value:
                                                        segment = c.get_segment_path()
                                                        if (segment_path == segment):
                                                            return c
                                                    c = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.WredMatchValue.DnxQoseaShowRedMatchValue()
                                                    c.parent = self
                                                    local_reference_key = "ydk::seg::%s" % segment_path
                                                    self._local_refs[local_reference_key] = c
                                                    self.dnx_qosea_show_red_match_value.append(c)
                                                    return c

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "dnx-qosea-show-red-match-value"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                pass


                                        class ConfigMinThreshold(Entity):
                                            """
                                            Configured minimum threshold
                                            
                                            .. attribute:: policy_unit
                                            
                                            	Policy unit
                                            	**type**\:   :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                            
                                            .. attribute:: policy_value
                                            
                                            	Policy value
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'ncs5500-qos-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.ConfigMinThreshold, self).__init__()

                                                self.yang_name = "config-min-threshold"
                                                self.yang_parent_name = "wred"

                                                self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                                self.policy_value = YLeaf(YType.uint32, "policy-value")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("policy_unit",
                                                                "policy_value") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.ConfigMinThreshold, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.ConfigMinThreshold, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.policy_unit.is_set or
                                                    self.policy_value.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.policy_unit.yfilter != YFilter.not_set or
                                                    self.policy_value.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "config-min-threshold" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.policy_unit.is_set or self.policy_unit.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.policy_unit.get_name_leafdata())
                                                if (self.policy_value.is_set or self.policy_value.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.policy_value.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "policy-unit" or name == "policy-value"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "policy-unit"):
                                                    self.policy_unit = value
                                                    self.policy_unit.value_namespace = name_space
                                                    self.policy_unit.value_namespace_prefix = name_space_prefix
                                                if(value_path == "policy-value"):
                                                    self.policy_value = value
                                                    self.policy_value.value_namespace = name_space
                                                    self.policy_value.value_namespace_prefix = name_space_prefix


                                        class ConfigMaxThreshold(Entity):
                                            """
                                            Configured maximum threshold
                                            
                                            .. attribute:: policy_unit
                                            
                                            	Policy unit
                                            	**type**\:   :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                            
                                            .. attribute:: policy_value
                                            
                                            	Policy value
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'ncs5500-qos-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.ConfigMaxThreshold, self).__init__()

                                                self.yang_name = "config-max-threshold"
                                                self.yang_parent_name = "wred"

                                                self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                                self.policy_value = YLeaf(YType.uint32, "policy-value")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("policy_unit",
                                                                "policy_value") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.ConfigMaxThreshold, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.ConfigMaxThreshold, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.policy_unit.is_set or
                                                    self.policy_value.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.policy_unit.yfilter != YFilter.not_set or
                                                    self.policy_value.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "config-max-threshold" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.policy_unit.is_set or self.policy_unit.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.policy_unit.get_name_leafdata())
                                                if (self.policy_value.is_set or self.policy_value.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.policy_value.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "policy-unit" or name == "policy-value"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "policy-unit"):
                                                    self.policy_unit = value
                                                    self.policy_unit.value_namespace = name_space
                                                    self.policy_unit.value_namespace_prefix = name_space_prefix
                                                if(value_path == "policy-value"):
                                                    self.policy_value = value
                                                    self.policy_value.value_namespace = name_space
                                                    self.policy_value.value_namespace_prefix = name_space_prefix

                                        def has_data(self):
                                            return (
                                                self.first_segment.is_set or
                                                self.hardware_max_threshold_bytes.is_set or
                                                self.hardware_min_threshold_bytes.is_set or
                                                self.segment_size.is_set or
                                                self.wred_match_type.is_set or
                                                (self.config_max_threshold is not None and self.config_max_threshold.has_data()) or
                                                (self.config_min_threshold is not None and self.config_min_threshold.has_data()) or
                                                (self.wred_match_value is not None and self.wred_match_value.has_data()))

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.first_segment.yfilter != YFilter.not_set or
                                                self.hardware_max_threshold_bytes.yfilter != YFilter.not_set or
                                                self.hardware_min_threshold_bytes.yfilter != YFilter.not_set or
                                                self.segment_size.yfilter != YFilter.not_set or
                                                self.wred_match_type.yfilter != YFilter.not_set or
                                                (self.config_max_threshold is not None and self.config_max_threshold.has_operation()) or
                                                (self.config_min_threshold is not None and self.config_min_threshold.has_operation()) or
                                                (self.wred_match_value is not None and self.wred_match_value.has_operation()))

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "wred" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.first_segment.is_set or self.first_segment.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.first_segment.get_name_leafdata())
                                            if (self.hardware_max_threshold_bytes.is_set or self.hardware_max_threshold_bytes.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.hardware_max_threshold_bytes.get_name_leafdata())
                                            if (self.hardware_min_threshold_bytes.is_set or self.hardware_min_threshold_bytes.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.hardware_min_threshold_bytes.get_name_leafdata())
                                            if (self.segment_size.is_set or self.segment_size.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.segment_size.get_name_leafdata())
                                            if (self.wred_match_type.is_set or self.wred_match_type.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.wred_match_type.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            if (child_yang_name == "config-max-threshold"):
                                                if (self.config_max_threshold is None):
                                                    self.config_max_threshold = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.ConfigMaxThreshold()
                                                    self.config_max_threshold.parent = self
                                                    self._children_name_map["config_max_threshold"] = "config-max-threshold"
                                                return self.config_max_threshold

                                            if (child_yang_name == "config-min-threshold"):
                                                if (self.config_min_threshold is None):
                                                    self.config_min_threshold = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.ConfigMinThreshold()
                                                    self.config_min_threshold.parent = self
                                                    self._children_name_map["config_min_threshold"] = "config-min-threshold"
                                                return self.config_min_threshold

                                            if (child_yang_name == "wred-match-value"):
                                                if (self.wred_match_value is None):
                                                    self.wred_match_value = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.WredMatchValue()
                                                    self.wred_match_value.parent = self
                                                    self._children_name_map["wred_match_value"] = "wred-match-value"
                                                return self.wred_match_value

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "config-max-threshold" or name == "config-min-threshold" or name == "wred-match-value" or name == "first-segment" or name == "hardware-max-threshold-bytes" or name == "hardware-min-threshold-bytes" or name == "segment-size" or name == "wred-match-type"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "first-segment"):
                                                self.first_segment = value
                                                self.first_segment.value_namespace = name_space
                                                self.first_segment.value_namespace_prefix = name_space_prefix
                                            if(value_path == "hardware-max-threshold-bytes"):
                                                self.hardware_max_threshold_bytes = value
                                                self.hardware_max_threshold_bytes.value_namespace = name_space
                                                self.hardware_max_threshold_bytes.value_namespace_prefix = name_space_prefix
                                            if(value_path == "hardware-min-threshold-bytes"):
                                                self.hardware_min_threshold_bytes = value
                                                self.hardware_min_threshold_bytes.value_namespace = name_space
                                                self.hardware_min_threshold_bytes.value_namespace_prefix = name_space_prefix
                                            if(value_path == "segment-size"):
                                                self.segment_size = value
                                                self.segment_size.value_namespace = name_space
                                                self.segment_size.value_namespace_prefix = name_space_prefix
                                            if(value_path == "wred-match-type"):
                                                self.wred_match_type = value
                                                self.wred_match_type.value_namespace = name_space
                                                self.wred_match_type.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        for c in self.common_mark:
                                            if (c.has_data()):
                                                return True
                                        for c in self.ip_mark:
                                            if (c.has_data()):
                                                return True
                                        for c in self.mpls_mark:
                                            if (c.has_data()):
                                                return True
                                        for c in self.wred:
                                            if (c.has_data()):
                                                return True
                                        return (
                                            self.level_one_class_name.is_set or
                                            self.class_level.is_set or
                                            self.config_excess_bandwidth_percent.is_set or
                                            self.config_excess_bandwidth_unit.is_set or
                                            self.egress_queue_id.is_set or
                                            self.hardware_excess_bandwidth_weight.is_set or
                                            self.hardware_max_rate_kbps.is_set or
                                            self.hardware_min_rate_kbps.is_set or
                                            self.hardware_policer_average_rate_kbps.is_set or
                                            self.hardware_policer_conform_burst_bytes.is_set or
                                            self.hardware_policer_excess_burst_bytes.is_set or
                                            self.hardware_policer_peak_rate_kbps.is_set or
                                            self.hardware_queue_limit_bytes.is_set or
                                            self.hardware_queue_limit_microseconds.is_set or
                                            self.level_two_class_name.is_set or
                                            self.network_min_bandwidth_kbps.is_set or
                                            self.policer_bucket_id.is_set or
                                            self.policer_stats_handle.is_set or
                                            self.priority_level.is_set or
                                            self.queue_type.is_set or
                                            (self.config_max_rate is not None and self.config_max_rate.has_data()) or
                                            (self.config_min_rate is not None and self.config_min_rate.has_data()) or
                                            (self.config_policer_average_rate is not None and self.config_policer_average_rate.has_data()) or
                                            (self.config_policer_conform_burst is not None and self.config_policer_conform_burst.has_data()) or
                                            (self.config_policer_excess_burst is not None and self.config_policer_excess_burst.has_data()) or
                                            (self.config_policer_peak_rate is not None and self.config_policer_peak_rate.has_data()) or
                                            (self.config_queue_limit is not None and self.config_queue_limit.has_data()) or
                                            (self.conform_action is not None and self.conform_action.has_data()) or
                                            (self.exceed_action is not None and self.exceed_action.has_data()) or
                                            (self.violate_action is not None and self.violate_action.has_data()))

                                    def has_operation(self):
                                        for c in self.common_mark:
                                            if (c.has_operation()):
                                                return True
                                        for c in self.ip_mark:
                                            if (c.has_operation()):
                                                return True
                                        for c in self.mpls_mark:
                                            if (c.has_operation()):
                                                return True
                                        for c in self.wred:
                                            if (c.has_operation()):
                                                return True
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.level_one_class_name.yfilter != YFilter.not_set or
                                            self.class_level.yfilter != YFilter.not_set or
                                            self.config_excess_bandwidth_percent.yfilter != YFilter.not_set or
                                            self.config_excess_bandwidth_unit.yfilter != YFilter.not_set or
                                            self.egress_queue_id.yfilter != YFilter.not_set or
                                            self.hardware_excess_bandwidth_weight.yfilter != YFilter.not_set or
                                            self.hardware_max_rate_kbps.yfilter != YFilter.not_set or
                                            self.hardware_min_rate_kbps.yfilter != YFilter.not_set or
                                            self.hardware_policer_average_rate_kbps.yfilter != YFilter.not_set or
                                            self.hardware_policer_conform_burst_bytes.yfilter != YFilter.not_set or
                                            self.hardware_policer_excess_burst_bytes.yfilter != YFilter.not_set or
                                            self.hardware_policer_peak_rate_kbps.yfilter != YFilter.not_set or
                                            self.hardware_queue_limit_bytes.yfilter != YFilter.not_set or
                                            self.hardware_queue_limit_microseconds.yfilter != YFilter.not_set or
                                            self.level_two_class_name.yfilter != YFilter.not_set or
                                            self.network_min_bandwidth_kbps.yfilter != YFilter.not_set or
                                            self.policer_bucket_id.yfilter != YFilter.not_set or
                                            self.policer_stats_handle.yfilter != YFilter.not_set or
                                            self.priority_level.yfilter != YFilter.not_set or
                                            self.queue_type.yfilter != YFilter.not_set or
                                            (self.config_max_rate is not None and self.config_max_rate.has_operation()) or
                                            (self.config_min_rate is not None and self.config_min_rate.has_operation()) or
                                            (self.config_policer_average_rate is not None and self.config_policer_average_rate.has_operation()) or
                                            (self.config_policer_conform_burst is not None and self.config_policer_conform_burst.has_operation()) or
                                            (self.config_policer_excess_burst is not None and self.config_policer_excess_burst.has_operation()) or
                                            (self.config_policer_peak_rate is not None and self.config_policer_peak_rate.has_operation()) or
                                            (self.config_queue_limit is not None and self.config_queue_limit.has_operation()) or
                                            (self.conform_action is not None and self.conform_action.has_operation()) or
                                            (self.exceed_action is not None and self.exceed_action.has_operation()) or
                                            (self.violate_action is not None and self.violate_action.has_operation()))

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "class" + "[level-one-class-name='" + self.level_one_class_name.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.level_one_class_name.is_set or self.level_one_class_name.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.level_one_class_name.get_name_leafdata())
                                        if (self.class_level.is_set or self.class_level.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.class_level.get_name_leafdata())
                                        if (self.config_excess_bandwidth_percent.is_set or self.config_excess_bandwidth_percent.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.config_excess_bandwidth_percent.get_name_leafdata())
                                        if (self.config_excess_bandwidth_unit.is_set or self.config_excess_bandwidth_unit.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.config_excess_bandwidth_unit.get_name_leafdata())
                                        if (self.egress_queue_id.is_set or self.egress_queue_id.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.egress_queue_id.get_name_leafdata())
                                        if (self.hardware_excess_bandwidth_weight.is_set or self.hardware_excess_bandwidth_weight.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.hardware_excess_bandwidth_weight.get_name_leafdata())
                                        if (self.hardware_max_rate_kbps.is_set or self.hardware_max_rate_kbps.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.hardware_max_rate_kbps.get_name_leafdata())
                                        if (self.hardware_min_rate_kbps.is_set or self.hardware_min_rate_kbps.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.hardware_min_rate_kbps.get_name_leafdata())
                                        if (self.hardware_policer_average_rate_kbps.is_set or self.hardware_policer_average_rate_kbps.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.hardware_policer_average_rate_kbps.get_name_leafdata())
                                        if (self.hardware_policer_conform_burst_bytes.is_set or self.hardware_policer_conform_burst_bytes.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.hardware_policer_conform_burst_bytes.get_name_leafdata())
                                        if (self.hardware_policer_excess_burst_bytes.is_set or self.hardware_policer_excess_burst_bytes.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.hardware_policer_excess_burst_bytes.get_name_leafdata())
                                        if (self.hardware_policer_peak_rate_kbps.is_set or self.hardware_policer_peak_rate_kbps.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.hardware_policer_peak_rate_kbps.get_name_leafdata())
                                        if (self.hardware_queue_limit_bytes.is_set or self.hardware_queue_limit_bytes.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.hardware_queue_limit_bytes.get_name_leafdata())
                                        if (self.hardware_queue_limit_microseconds.is_set or self.hardware_queue_limit_microseconds.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.hardware_queue_limit_microseconds.get_name_leafdata())
                                        if (self.level_two_class_name.is_set or self.level_two_class_name.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.level_two_class_name.get_name_leafdata())
                                        if (self.network_min_bandwidth_kbps.is_set or self.network_min_bandwidth_kbps.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.network_min_bandwidth_kbps.get_name_leafdata())
                                        if (self.policer_bucket_id.is_set or self.policer_bucket_id.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.policer_bucket_id.get_name_leafdata())
                                        if (self.policer_stats_handle.is_set or self.policer_stats_handle.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.policer_stats_handle.get_name_leafdata())
                                        if (self.priority_level.is_set or self.priority_level.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.priority_level.get_name_leafdata())
                                        if (self.queue_type.is_set or self.queue_type.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.queue_type.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "common-mark"):
                                            for c in self.common_mark:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.CommonMark()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.common_mark.append(c)
                                            return c

                                        if (child_yang_name == "config-max-rate"):
                                            if (self.config_max_rate is None):
                                                self.config_max_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigMaxRate()
                                                self.config_max_rate.parent = self
                                                self._children_name_map["config_max_rate"] = "config-max-rate"
                                            return self.config_max_rate

                                        if (child_yang_name == "config-min-rate"):
                                            if (self.config_min_rate is None):
                                                self.config_min_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigMinRate()
                                                self.config_min_rate.parent = self
                                                self._children_name_map["config_min_rate"] = "config-min-rate"
                                            return self.config_min_rate

                                        if (child_yang_name == "config-policer-average-rate"):
                                            if (self.config_policer_average_rate is None):
                                                self.config_policer_average_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerAverageRate()
                                                self.config_policer_average_rate.parent = self
                                                self._children_name_map["config_policer_average_rate"] = "config-policer-average-rate"
                                            return self.config_policer_average_rate

                                        if (child_yang_name == "config-policer-conform-burst"):
                                            if (self.config_policer_conform_burst is None):
                                                self.config_policer_conform_burst = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerConformBurst()
                                                self.config_policer_conform_burst.parent = self
                                                self._children_name_map["config_policer_conform_burst"] = "config-policer-conform-burst"
                                            return self.config_policer_conform_burst

                                        if (child_yang_name == "config-policer-excess-burst"):
                                            if (self.config_policer_excess_burst is None):
                                                self.config_policer_excess_burst = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerExcessBurst()
                                                self.config_policer_excess_burst.parent = self
                                                self._children_name_map["config_policer_excess_burst"] = "config-policer-excess-burst"
                                            return self.config_policer_excess_burst

                                        if (child_yang_name == "config-policer-peak-rate"):
                                            if (self.config_policer_peak_rate is None):
                                                self.config_policer_peak_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerPeakRate()
                                                self.config_policer_peak_rate.parent = self
                                                self._children_name_map["config_policer_peak_rate"] = "config-policer-peak-rate"
                                            return self.config_policer_peak_rate

                                        if (child_yang_name == "config-queue-limit"):
                                            if (self.config_queue_limit is None):
                                                self.config_queue_limit = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigQueueLimit()
                                                self.config_queue_limit.parent = self
                                                self._children_name_map["config_queue_limit"] = "config-queue-limit"
                                            return self.config_queue_limit

                                        if (child_yang_name == "conform-action"):
                                            if (self.conform_action is None):
                                                self.conform_action = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConformAction()
                                                self.conform_action.parent = self
                                                self._children_name_map["conform_action"] = "conform-action"
                                            return self.conform_action

                                        if (child_yang_name == "exceed-action"):
                                            if (self.exceed_action is None):
                                                self.exceed_action = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ExceedAction()
                                                self.exceed_action.parent = self
                                                self._children_name_map["exceed_action"] = "exceed-action"
                                            return self.exceed_action

                                        if (child_yang_name == "ip-mark"):
                                            for c in self.ip_mark:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.IpMark()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.ip_mark.append(c)
                                            return c

                                        if (child_yang_name == "mpls-mark"):
                                            for c in self.mpls_mark:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.MplsMark()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.mpls_mark.append(c)
                                            return c

                                        if (child_yang_name == "violate-action"):
                                            if (self.violate_action is None):
                                                self.violate_action = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ViolateAction()
                                                self.violate_action.parent = self
                                                self._children_name_map["violate_action"] = "violate-action"
                                            return self.violate_action

                                        if (child_yang_name == "wred"):
                                            for c in self.wred:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.wred.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "common-mark" or name == "config-max-rate" or name == "config-min-rate" or name == "config-policer-average-rate" or name == "config-policer-conform-burst" or name == "config-policer-excess-burst" or name == "config-policer-peak-rate" or name == "config-queue-limit" or name == "conform-action" or name == "exceed-action" or name == "ip-mark" or name == "mpls-mark" or name == "violate-action" or name == "wred" or name == "level-one-class-name" or name == "class-level" or name == "config-excess-bandwidth-percent" or name == "config-excess-bandwidth-unit" or name == "egress-queue-id" or name == "hardware-excess-bandwidth-weight" or name == "hardware-max-rate-kbps" or name == "hardware-min-rate-kbps" or name == "hardware-policer-average-rate-kbps" or name == "hardware-policer-conform-burst-bytes" or name == "hardware-policer-excess-burst-bytes" or name == "hardware-policer-peak-rate-kbps" or name == "hardware-queue-limit-bytes" or name == "hardware-queue-limit-microseconds" or name == "level-two-class-name" or name == "network-min-bandwidth-kbps" or name == "policer-bucket-id" or name == "policer-stats-handle" or name == "priority-level" or name == "queue-type"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "level-one-class-name"):
                                            self.level_one_class_name = value
                                            self.level_one_class_name.value_namespace = name_space
                                            self.level_one_class_name.value_namespace_prefix = name_space_prefix
                                        if(value_path == "class-level"):
                                            self.class_level = value
                                            self.class_level.value_namespace = name_space
                                            self.class_level.value_namespace_prefix = name_space_prefix
                                        if(value_path == "config-excess-bandwidth-percent"):
                                            self.config_excess_bandwidth_percent = value
                                            self.config_excess_bandwidth_percent.value_namespace = name_space
                                            self.config_excess_bandwidth_percent.value_namespace_prefix = name_space_prefix
                                        if(value_path == "config-excess-bandwidth-unit"):
                                            self.config_excess_bandwidth_unit = value
                                            self.config_excess_bandwidth_unit.value_namespace = name_space
                                            self.config_excess_bandwidth_unit.value_namespace_prefix = name_space_prefix
                                        if(value_path == "egress-queue-id"):
                                            self.egress_queue_id = value
                                            self.egress_queue_id.value_namespace = name_space
                                            self.egress_queue_id.value_namespace_prefix = name_space_prefix
                                        if(value_path == "hardware-excess-bandwidth-weight"):
                                            self.hardware_excess_bandwidth_weight = value
                                            self.hardware_excess_bandwidth_weight.value_namespace = name_space
                                            self.hardware_excess_bandwidth_weight.value_namespace_prefix = name_space_prefix
                                        if(value_path == "hardware-max-rate-kbps"):
                                            self.hardware_max_rate_kbps = value
                                            self.hardware_max_rate_kbps.value_namespace = name_space
                                            self.hardware_max_rate_kbps.value_namespace_prefix = name_space_prefix
                                        if(value_path == "hardware-min-rate-kbps"):
                                            self.hardware_min_rate_kbps = value
                                            self.hardware_min_rate_kbps.value_namespace = name_space
                                            self.hardware_min_rate_kbps.value_namespace_prefix = name_space_prefix
                                        if(value_path == "hardware-policer-average-rate-kbps"):
                                            self.hardware_policer_average_rate_kbps = value
                                            self.hardware_policer_average_rate_kbps.value_namespace = name_space
                                            self.hardware_policer_average_rate_kbps.value_namespace_prefix = name_space_prefix
                                        if(value_path == "hardware-policer-conform-burst-bytes"):
                                            self.hardware_policer_conform_burst_bytes = value
                                            self.hardware_policer_conform_burst_bytes.value_namespace = name_space
                                            self.hardware_policer_conform_burst_bytes.value_namespace_prefix = name_space_prefix
                                        if(value_path == "hardware-policer-excess-burst-bytes"):
                                            self.hardware_policer_excess_burst_bytes = value
                                            self.hardware_policer_excess_burst_bytes.value_namespace = name_space
                                            self.hardware_policer_excess_burst_bytes.value_namespace_prefix = name_space_prefix
                                        if(value_path == "hardware-policer-peak-rate-kbps"):
                                            self.hardware_policer_peak_rate_kbps = value
                                            self.hardware_policer_peak_rate_kbps.value_namespace = name_space
                                            self.hardware_policer_peak_rate_kbps.value_namespace_prefix = name_space_prefix
                                        if(value_path == "hardware-queue-limit-bytes"):
                                            self.hardware_queue_limit_bytes = value
                                            self.hardware_queue_limit_bytes.value_namespace = name_space
                                            self.hardware_queue_limit_bytes.value_namespace_prefix = name_space_prefix
                                        if(value_path == "hardware-queue-limit-microseconds"):
                                            self.hardware_queue_limit_microseconds = value
                                            self.hardware_queue_limit_microseconds.value_namespace = name_space
                                            self.hardware_queue_limit_microseconds.value_namespace_prefix = name_space_prefix
                                        if(value_path == "level-two-class-name"):
                                            self.level_two_class_name = value
                                            self.level_two_class_name.value_namespace = name_space
                                            self.level_two_class_name.value_namespace_prefix = name_space_prefix
                                        if(value_path == "network-min-bandwidth-kbps"):
                                            self.network_min_bandwidth_kbps = value
                                            self.network_min_bandwidth_kbps.value_namespace = name_space
                                            self.network_min_bandwidth_kbps.value_namespace_prefix = name_space_prefix
                                        if(value_path == "policer-bucket-id"):
                                            self.policer_bucket_id = value
                                            self.policer_bucket_id.value_namespace = name_space
                                            self.policer_bucket_id.value_namespace_prefix = name_space_prefix
                                        if(value_path == "policer-stats-handle"):
                                            self.policer_stats_handle = value
                                            self.policer_stats_handle.value_namespace = name_space
                                            self.policer_stats_handle.value_namespace_prefix = name_space_prefix
                                        if(value_path == "priority-level"):
                                            self.priority_level = value
                                            self.priority_level.value_namespace = name_space
                                            self.priority_level.value_namespace_prefix = name_space_prefix
                                        if(value_path == "queue-type"):
                                            self.queue_type = value
                                            self.queue_type.value_namespace = name_space
                                            self.queue_type.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.class_:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.class_:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "classes" + path_buffer

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

                                    if (child_yang_name == "class"):
                                        for c in self.class_:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.class_.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "class"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass

                            def has_data(self):
                                return (
                                    self.interface_name.is_set or
                                    (self.classes is not None and self.classes.has_data()) or
                                    (self.policy_details is not None and self.policy_details.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.interface_name.yfilter != YFilter.not_set or
                                    (self.classes is not None and self.classes.has_operation()) or
                                    (self.policy_details is not None and self.policy_details.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "member-interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

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

                                if (child_yang_name == "classes"):
                                    if (self.classes is None):
                                        self.classes = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes()
                                        self.classes.parent = self
                                        self._children_name_map["classes"] = "classes"
                                    return self.classes

                                if (child_yang_name == "policy-details"):
                                    if (self.policy_details is None):
                                        self.policy_details = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.PolicyDetails()
                                        self.policy_details.parent = self
                                        self._children_name_map["policy_details"] = "policy-details"
                                    return self.policy_details

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "classes" or name == "policy-details" or name == "interface-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "interface-name"):
                                    self.interface_name = value
                                    self.interface_name.value_namespace = name_space
                                    self.interface_name.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.member_interface:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.member_interface:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "member-interfaces" + path_buffer

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

                            if (child_yang_name == "member-interface"):
                                for c in self.member_interface:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.member_interface.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "member-interface"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class PolicyDetails(Entity):
                        """
                        Policy Details
                        
                        .. attribute:: interface_bandwidth_kbps
                        
                        	Interface Bandwidth (in kbps)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: kbit/s
                        
                        .. attribute:: interface_handle
                        
                        	InterfaceHandle
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: interface_status
                        
                        	Interface Status
                        	**type**\:   :py:class:`DnxQoseaShowIntfStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowIntfStatus>`
                        
                        .. attribute:: npu_id
                        
                        	NPU ID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: policy_name
                        
                        	Policy name
                        	**type**\:  str
                        
                        	**length:** 0..64
                        
                        .. attribute:: policy_status
                        
                        	Policy Status
                        	**type**\:   :py:class:`DnxQoseaShowPolicyStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowPolicyStatus>`
                        
                        .. attribute:: stats_accounting_type
                        
                        	QoS Statistics Accounting Type
                        	**type**\:   :py:class:`QosPolicyAccountEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.QosPolicyAccountEnum>`
                        
                        .. attribute:: total_number_of_classes
                        
                        	Number of Classes
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: voq_base_address
                        
                        	VOQ base address
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: voq_stats_handle
                        
                        	VOQ stats handle
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'ncs5500-qos-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.PolicyDetails, self).__init__()

                            self.yang_name = "policy-details"
                            self.yang_parent_name = "bundle-interface"

                            self.interface_bandwidth_kbps = YLeaf(YType.uint32, "interface-bandwidth-kbps")

                            self.interface_handle = YLeaf(YType.uint32, "interface-handle")

                            self.interface_status = YLeaf(YType.enumeration, "interface-status")

                            self.npu_id = YLeaf(YType.uint32, "npu-id")

                            self.policy_name = YLeaf(YType.str, "policy-name")

                            self.policy_status = YLeaf(YType.enumeration, "policy-status")

                            self.stats_accounting_type = YLeaf(YType.enumeration, "stats-accounting-type")

                            self.total_number_of_classes = YLeaf(YType.uint16, "total-number-of-classes")

                            self.voq_base_address = YLeaf(YType.uint32, "voq-base-address")

                            self.voq_stats_handle = YLeaf(YType.uint64, "voq-stats-handle")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("interface_bandwidth_kbps",
                                            "interface_handle",
                                            "interface_status",
                                            "npu_id",
                                            "policy_name",
                                            "policy_status",
                                            "stats_accounting_type",
                                            "total_number_of_classes",
                                            "voq_base_address",
                                            "voq_stats_handle") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.PolicyDetails, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.PolicyDetails, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.interface_bandwidth_kbps.is_set or
                                self.interface_handle.is_set or
                                self.interface_status.is_set or
                                self.npu_id.is_set or
                                self.policy_name.is_set or
                                self.policy_status.is_set or
                                self.stats_accounting_type.is_set or
                                self.total_number_of_classes.is_set or
                                self.voq_base_address.is_set or
                                self.voq_stats_handle.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.interface_bandwidth_kbps.yfilter != YFilter.not_set or
                                self.interface_handle.yfilter != YFilter.not_set or
                                self.interface_status.yfilter != YFilter.not_set or
                                self.npu_id.yfilter != YFilter.not_set or
                                self.policy_name.yfilter != YFilter.not_set or
                                self.policy_status.yfilter != YFilter.not_set or
                                self.stats_accounting_type.yfilter != YFilter.not_set or
                                self.total_number_of_classes.yfilter != YFilter.not_set or
                                self.voq_base_address.yfilter != YFilter.not_set or
                                self.voq_stats_handle.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "policy-details" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.interface_bandwidth_kbps.is_set or self.interface_bandwidth_kbps.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface_bandwidth_kbps.get_name_leafdata())
                            if (self.interface_handle.is_set or self.interface_handle.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface_handle.get_name_leafdata())
                            if (self.interface_status.is_set or self.interface_status.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface_status.get_name_leafdata())
                            if (self.npu_id.is_set or self.npu_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.npu_id.get_name_leafdata())
                            if (self.policy_name.is_set or self.policy_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.policy_name.get_name_leafdata())
                            if (self.policy_status.is_set or self.policy_status.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.policy_status.get_name_leafdata())
                            if (self.stats_accounting_type.is_set or self.stats_accounting_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.stats_accounting_type.get_name_leafdata())
                            if (self.total_number_of_classes.is_set or self.total_number_of_classes.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.total_number_of_classes.get_name_leafdata())
                            if (self.voq_base_address.is_set or self.voq_base_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.voq_base_address.get_name_leafdata())
                            if (self.voq_stats_handle.is_set or self.voq_stats_handle.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.voq_stats_handle.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "interface-bandwidth-kbps" or name == "interface-handle" or name == "interface-status" or name == "npu-id" or name == "policy-name" or name == "policy-status" or name == "stats-accounting-type" or name == "total-number-of-classes" or name == "voq-base-address" or name == "voq-stats-handle"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "interface-bandwidth-kbps"):
                                self.interface_bandwidth_kbps = value
                                self.interface_bandwidth_kbps.value_namespace = name_space
                                self.interface_bandwidth_kbps.value_namespace_prefix = name_space_prefix
                            if(value_path == "interface-handle"):
                                self.interface_handle = value
                                self.interface_handle.value_namespace = name_space
                                self.interface_handle.value_namespace_prefix = name_space_prefix
                            if(value_path == "interface-status"):
                                self.interface_status = value
                                self.interface_status.value_namespace = name_space
                                self.interface_status.value_namespace_prefix = name_space_prefix
                            if(value_path == "npu-id"):
                                self.npu_id = value
                                self.npu_id.value_namespace = name_space
                                self.npu_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "policy-name"):
                                self.policy_name = value
                                self.policy_name.value_namespace = name_space
                                self.policy_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "policy-status"):
                                self.policy_status = value
                                self.policy_status.value_namespace = name_space
                                self.policy_status.value_namespace_prefix = name_space_prefix
                            if(value_path == "stats-accounting-type"):
                                self.stats_accounting_type = value
                                self.stats_accounting_type.value_namespace = name_space
                                self.stats_accounting_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "total-number-of-classes"):
                                self.total_number_of_classes = value
                                self.total_number_of_classes.value_namespace = name_space
                                self.total_number_of_classes.value_namespace_prefix = name_space_prefix
                            if(value_path == "voq-base-address"):
                                self.voq_base_address = value
                                self.voq_base_address.value_namespace = name_space
                                self.voq_base_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "voq-stats-handle"):
                                self.voq_stats_handle = value
                                self.voq_stats_handle.value_namespace = name_space
                                self.voq_stats_handle.value_namespace_prefix = name_space_prefix


                    class Classes(Entity):
                        """
                        QoS list of class names
                        
                        .. attribute:: class_
                        
                        	QoS policy class
                        	**type**\: list of    :py:class:`Class_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_>`
                        
                        

                        """

                        _prefix = 'ncs5500-qos-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes, self).__init__()

                            self.yang_name = "classes"
                            self.yang_parent_name = "bundle-interface"

                            self.class_ = YList(self)

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
                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes, self).__setattr__(name, value)


                        class Class_(Entity):
                            """
                            QoS policy class
                            
                            .. attribute:: level_one_class_name  <key>
                            
                            	QoS policy class name at level 1
                            	**type**\:  str
                            
                            .. attribute:: class_level
                            
                            	Class level
                            	**type**\:   :py:class:`DnxQoseaShowLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowLevel>`
                            
                            .. attribute:: common_mark
                            
                            	Common mark
                            	**type**\: list of    :py:class:`CommonMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.CommonMark>`
                            
                            .. attribute:: config_excess_bandwidth_percent
                            
                            	Configured excess bandwidth percentage
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: percentage
                            
                            .. attribute:: config_excess_bandwidth_unit
                            
                            	Configured excess bandwidth unit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: config_max_rate
                            
                            	Configured maximum rate
                            	**type**\:   :py:class:`ConfigMaxRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigMaxRate>`
                            
                            .. attribute:: config_min_rate
                            
                            	Configured minimum rate
                            	**type**\:   :py:class:`ConfigMinRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigMinRate>`
                            
                            .. attribute:: config_policer_average_rate
                            
                            	Configured policer average rate
                            	**type**\:   :py:class:`ConfigPolicerAverageRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerAverageRate>`
                            
                            .. attribute:: config_policer_conform_burst
                            
                            	Configured policer conform burst
                            	**type**\:   :py:class:`ConfigPolicerConformBurst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerConformBurst>`
                            
                            .. attribute:: config_policer_excess_burst
                            
                            	Configured policer excess burst
                            	**type**\:   :py:class:`ConfigPolicerExcessBurst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerExcessBurst>`
                            
                            .. attribute:: config_policer_peak_rate
                            
                            	Config policer peak rate
                            	**type**\:   :py:class:`ConfigPolicerPeakRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerPeakRate>`
                            
                            .. attribute:: config_queue_limit
                            
                            	Configured queue limit
                            	**type**\:   :py:class:`ConfigQueueLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigQueueLimit>`
                            
                            .. attribute:: conform_action
                            
                            	Conform action
                            	**type**\:   :py:class:`ConformAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConformAction>`
                            
                            .. attribute:: egress_queue_id
                            
                            	Egress Queue ID
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: exceed_action
                            
                            	Exceed action
                            	**type**\:   :py:class:`ExceedAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ExceedAction>`
                            
                            .. attribute:: hardware_excess_bandwidth_weight
                            
                            	Hardware excess bandwidth weight
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hardware_max_rate_kbps
                            
                            	Hardware maximum rate in kbps
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: kbit/s
                            
                            .. attribute:: hardware_min_rate_kbps
                            
                            	Hardware minimum rate in kbps
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: kbit/s
                            
                            .. attribute:: hardware_policer_average_rate_kbps
                            
                            	Hardware policer average in kbps
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: kbit/s
                            
                            .. attribute:: hardware_policer_conform_burst_bytes
                            
                            	Hardware policer conform burst
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hardware_policer_excess_burst_bytes
                            
                            	Hardware policer excess burst
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hardware_policer_peak_rate_kbps
                            
                            	Hardware policer peak rate
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hardware_queue_limit_bytes
                            
                            	Hardware queue limit in bytes
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: hardware_queue_limit_microseconds
                            
                            	Hardware queue limit in microseconds
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: microsecond
                            
                            .. attribute:: ip_mark
                            
                            	IP mark
                            	**type**\: list of    :py:class:`IpMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.IpMark>`
                            
                            .. attribute:: level_two_class_name
                            
                            	QoS policy child class name at level 2
                            	**type**\:  str
                            
                            .. attribute:: mpls_mark
                            
                            	MPLS mark
                            	**type**\: list of    :py:class:`MplsMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.MplsMark>`
                            
                            .. attribute:: network_min_bandwidth_kbps
                            
                            	Network minimum Bandwith
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: policer_bucket_id
                            
                            	PolicerBucketID
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: policer_stats_handle
                            
                            	PolicerStatsHandle
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: priority_level
                            
                            	Priority level
                            	**type**\:   :py:class:`DnxQoseaShowHpLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowHpLevel>`
                            
                            .. attribute:: queue_type
                            
                            	Queue type
                            	**type**\:   :py:class:`DnxQoseaShowQueue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowQueue>`
                            
                            .. attribute:: violate_action
                            
                            	Violate action
                            	**type**\:   :py:class:`ViolateAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ViolateAction>`
                            
                            .. attribute:: wred
                            
                            	WRED parameters
                            	**type**\: list of    :py:class:`Wred <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred>`
                            
                            

                            """

                            _prefix = 'ncs5500-qos-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_, self).__init__()

                                self.yang_name = "class"
                                self.yang_parent_name = "classes"

                                self.level_one_class_name = YLeaf(YType.str, "level-one-class-name")

                                self.class_level = YLeaf(YType.enumeration, "class-level")

                                self.config_excess_bandwidth_percent = YLeaf(YType.uint32, "config-excess-bandwidth-percent")

                                self.config_excess_bandwidth_unit = YLeaf(YType.uint32, "config-excess-bandwidth-unit")

                                self.egress_queue_id = YLeaf(YType.int32, "egress-queue-id")

                                self.hardware_excess_bandwidth_weight = YLeaf(YType.uint32, "hardware-excess-bandwidth-weight")

                                self.hardware_max_rate_kbps = YLeaf(YType.uint32, "hardware-max-rate-kbps")

                                self.hardware_min_rate_kbps = YLeaf(YType.uint32, "hardware-min-rate-kbps")

                                self.hardware_policer_average_rate_kbps = YLeaf(YType.uint32, "hardware-policer-average-rate-kbps")

                                self.hardware_policer_conform_burst_bytes = YLeaf(YType.uint32, "hardware-policer-conform-burst-bytes")

                                self.hardware_policer_excess_burst_bytes = YLeaf(YType.uint32, "hardware-policer-excess-burst-bytes")

                                self.hardware_policer_peak_rate_kbps = YLeaf(YType.uint32, "hardware-policer-peak-rate-kbps")

                                self.hardware_queue_limit_bytes = YLeaf(YType.uint64, "hardware-queue-limit-bytes")

                                self.hardware_queue_limit_microseconds = YLeaf(YType.uint64, "hardware-queue-limit-microseconds")

                                self.level_two_class_name = YLeaf(YType.str, "level-two-class-name")

                                self.network_min_bandwidth_kbps = YLeaf(YType.uint32, "network-min-bandwidth-kbps")

                                self.policer_bucket_id = YLeaf(YType.uint32, "policer-bucket-id")

                                self.policer_stats_handle = YLeaf(YType.uint64, "policer-stats-handle")

                                self.priority_level = YLeaf(YType.enumeration, "priority-level")

                                self.queue_type = YLeaf(YType.enumeration, "queue-type")

                                self.config_max_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigMaxRate()
                                self.config_max_rate.parent = self
                                self._children_name_map["config_max_rate"] = "config-max-rate"
                                self._children_yang_names.add("config-max-rate")

                                self.config_min_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigMinRate()
                                self.config_min_rate.parent = self
                                self._children_name_map["config_min_rate"] = "config-min-rate"
                                self._children_yang_names.add("config-min-rate")

                                self.config_policer_average_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerAverageRate()
                                self.config_policer_average_rate.parent = self
                                self._children_name_map["config_policer_average_rate"] = "config-policer-average-rate"
                                self._children_yang_names.add("config-policer-average-rate")

                                self.config_policer_conform_burst = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerConformBurst()
                                self.config_policer_conform_burst.parent = self
                                self._children_name_map["config_policer_conform_burst"] = "config-policer-conform-burst"
                                self._children_yang_names.add("config-policer-conform-burst")

                                self.config_policer_excess_burst = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerExcessBurst()
                                self.config_policer_excess_burst.parent = self
                                self._children_name_map["config_policer_excess_burst"] = "config-policer-excess-burst"
                                self._children_yang_names.add("config-policer-excess-burst")

                                self.config_policer_peak_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerPeakRate()
                                self.config_policer_peak_rate.parent = self
                                self._children_name_map["config_policer_peak_rate"] = "config-policer-peak-rate"
                                self._children_yang_names.add("config-policer-peak-rate")

                                self.config_queue_limit = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigQueueLimit()
                                self.config_queue_limit.parent = self
                                self._children_name_map["config_queue_limit"] = "config-queue-limit"
                                self._children_yang_names.add("config-queue-limit")

                                self.conform_action = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConformAction()
                                self.conform_action.parent = self
                                self._children_name_map["conform_action"] = "conform-action"
                                self._children_yang_names.add("conform-action")

                                self.exceed_action = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ExceedAction()
                                self.exceed_action.parent = self
                                self._children_name_map["exceed_action"] = "exceed-action"
                                self._children_yang_names.add("exceed-action")

                                self.violate_action = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ViolateAction()
                                self.violate_action.parent = self
                                self._children_name_map["violate_action"] = "violate-action"
                                self._children_yang_names.add("violate-action")

                                self.common_mark = YList(self)
                                self.ip_mark = YList(self)
                                self.mpls_mark = YList(self)
                                self.wred = YList(self)

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("level_one_class_name",
                                                "class_level",
                                                "config_excess_bandwidth_percent",
                                                "config_excess_bandwidth_unit",
                                                "egress_queue_id",
                                                "hardware_excess_bandwidth_weight",
                                                "hardware_max_rate_kbps",
                                                "hardware_min_rate_kbps",
                                                "hardware_policer_average_rate_kbps",
                                                "hardware_policer_conform_burst_bytes",
                                                "hardware_policer_excess_burst_bytes",
                                                "hardware_policer_peak_rate_kbps",
                                                "hardware_queue_limit_bytes",
                                                "hardware_queue_limit_microseconds",
                                                "level_two_class_name",
                                                "network_min_bandwidth_kbps",
                                                "policer_bucket_id",
                                                "policer_stats_handle",
                                                "priority_level",
                                                "queue_type") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_, self).__setattr__(name, value)


                            class ConfigMaxRate(Entity):
                                """
                                Configured maximum rate
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:   :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigMaxRate, self).__init__()

                                    self.yang_name = "config-max-rate"
                                    self.yang_parent_name = "class"

                                    self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                    self.policy_value = YLeaf(YType.uint32, "policy-value")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("policy_unit",
                                                    "policy_value") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigMaxRate, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigMaxRate, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.policy_unit.is_set or
                                        self.policy_value.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.policy_unit.yfilter != YFilter.not_set or
                                        self.policy_value.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "config-max-rate" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.policy_unit.is_set or self.policy_unit.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.policy_unit.get_name_leafdata())
                                    if (self.policy_value.is_set or self.policy_value.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.policy_value.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "policy-unit" or name == "policy-value"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "policy-unit"):
                                        self.policy_unit = value
                                        self.policy_unit.value_namespace = name_space
                                        self.policy_unit.value_namespace_prefix = name_space_prefix
                                    if(value_path == "policy-value"):
                                        self.policy_value = value
                                        self.policy_value.value_namespace = name_space
                                        self.policy_value.value_namespace_prefix = name_space_prefix


                            class ConfigMinRate(Entity):
                                """
                                Configured minimum rate
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:   :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigMinRate, self).__init__()

                                    self.yang_name = "config-min-rate"
                                    self.yang_parent_name = "class"

                                    self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                    self.policy_value = YLeaf(YType.uint32, "policy-value")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("policy_unit",
                                                    "policy_value") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigMinRate, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigMinRate, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.policy_unit.is_set or
                                        self.policy_value.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.policy_unit.yfilter != YFilter.not_set or
                                        self.policy_value.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "config-min-rate" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.policy_unit.is_set or self.policy_unit.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.policy_unit.get_name_leafdata())
                                    if (self.policy_value.is_set or self.policy_value.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.policy_value.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "policy-unit" or name == "policy-value"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "policy-unit"):
                                        self.policy_unit = value
                                        self.policy_unit.value_namespace = name_space
                                        self.policy_unit.value_namespace_prefix = name_space_prefix
                                    if(value_path == "policy-value"):
                                        self.policy_value = value
                                        self.policy_value.value_namespace = name_space
                                        self.policy_value.value_namespace_prefix = name_space_prefix


                            class ConfigQueueLimit(Entity):
                                """
                                Configured queue limit
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:   :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigQueueLimit, self).__init__()

                                    self.yang_name = "config-queue-limit"
                                    self.yang_parent_name = "class"

                                    self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                    self.policy_value = YLeaf(YType.uint32, "policy-value")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("policy_unit",
                                                    "policy_value") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigQueueLimit, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigQueueLimit, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.policy_unit.is_set or
                                        self.policy_value.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.policy_unit.yfilter != YFilter.not_set or
                                        self.policy_value.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "config-queue-limit" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.policy_unit.is_set or self.policy_unit.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.policy_unit.get_name_leafdata())
                                    if (self.policy_value.is_set or self.policy_value.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.policy_value.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "policy-unit" or name == "policy-value"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "policy-unit"):
                                        self.policy_unit = value
                                        self.policy_unit.value_namespace = name_space
                                        self.policy_unit.value_namespace_prefix = name_space_prefix
                                    if(value_path == "policy-value"):
                                        self.policy_value = value
                                        self.policy_value.value_namespace = name_space
                                        self.policy_value.value_namespace_prefix = name_space_prefix


                            class ConfigPolicerAverageRate(Entity):
                                """
                                Configured policer average rate
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:   :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerAverageRate, self).__init__()

                                    self.yang_name = "config-policer-average-rate"
                                    self.yang_parent_name = "class"

                                    self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                    self.policy_value = YLeaf(YType.uint32, "policy-value")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("policy_unit",
                                                    "policy_value") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerAverageRate, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerAverageRate, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.policy_unit.is_set or
                                        self.policy_value.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.policy_unit.yfilter != YFilter.not_set or
                                        self.policy_value.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "config-policer-average-rate" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.policy_unit.is_set or self.policy_unit.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.policy_unit.get_name_leafdata())
                                    if (self.policy_value.is_set or self.policy_value.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.policy_value.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "policy-unit" or name == "policy-value"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "policy-unit"):
                                        self.policy_unit = value
                                        self.policy_unit.value_namespace = name_space
                                        self.policy_unit.value_namespace_prefix = name_space_prefix
                                    if(value_path == "policy-value"):
                                        self.policy_value = value
                                        self.policy_value.value_namespace = name_space
                                        self.policy_value.value_namespace_prefix = name_space_prefix


                            class ConfigPolicerPeakRate(Entity):
                                """
                                Config policer peak rate
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:   :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerPeakRate, self).__init__()

                                    self.yang_name = "config-policer-peak-rate"
                                    self.yang_parent_name = "class"

                                    self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                    self.policy_value = YLeaf(YType.uint32, "policy-value")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("policy_unit",
                                                    "policy_value") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerPeakRate, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerPeakRate, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.policy_unit.is_set or
                                        self.policy_value.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.policy_unit.yfilter != YFilter.not_set or
                                        self.policy_value.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "config-policer-peak-rate" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.policy_unit.is_set or self.policy_unit.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.policy_unit.get_name_leafdata())
                                    if (self.policy_value.is_set or self.policy_value.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.policy_value.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "policy-unit" or name == "policy-value"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "policy-unit"):
                                        self.policy_unit = value
                                        self.policy_unit.value_namespace = name_space
                                        self.policy_unit.value_namespace_prefix = name_space_prefix
                                    if(value_path == "policy-value"):
                                        self.policy_value = value
                                        self.policy_value.value_namespace = name_space
                                        self.policy_value.value_namespace_prefix = name_space_prefix


                            class ConfigPolicerConformBurst(Entity):
                                """
                                Configured policer conform burst
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:   :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerConformBurst, self).__init__()

                                    self.yang_name = "config-policer-conform-burst"
                                    self.yang_parent_name = "class"

                                    self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                    self.policy_value = YLeaf(YType.uint32, "policy-value")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("policy_unit",
                                                    "policy_value") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerConformBurst, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerConformBurst, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.policy_unit.is_set or
                                        self.policy_value.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.policy_unit.yfilter != YFilter.not_set or
                                        self.policy_value.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "config-policer-conform-burst" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.policy_unit.is_set or self.policy_unit.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.policy_unit.get_name_leafdata())
                                    if (self.policy_value.is_set or self.policy_value.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.policy_value.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "policy-unit" or name == "policy-value"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "policy-unit"):
                                        self.policy_unit = value
                                        self.policy_unit.value_namespace = name_space
                                        self.policy_unit.value_namespace_prefix = name_space_prefix
                                    if(value_path == "policy-value"):
                                        self.policy_value = value
                                        self.policy_value.value_namespace = name_space
                                        self.policy_value.value_namespace_prefix = name_space_prefix


                            class ConfigPolicerExcessBurst(Entity):
                                """
                                Configured policer excess burst
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:   :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerExcessBurst, self).__init__()

                                    self.yang_name = "config-policer-excess-burst"
                                    self.yang_parent_name = "class"

                                    self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                    self.policy_value = YLeaf(YType.uint32, "policy-value")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("policy_unit",
                                                    "policy_value") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerExcessBurst, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerExcessBurst, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.policy_unit.is_set or
                                        self.policy_value.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.policy_unit.yfilter != YFilter.not_set or
                                        self.policy_value.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "config-policer-excess-burst" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.policy_unit.is_set or self.policy_unit.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.policy_unit.get_name_leafdata())
                                    if (self.policy_value.is_set or self.policy_value.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.policy_value.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "policy-unit" or name == "policy-value"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "policy-unit"):
                                        self.policy_unit = value
                                        self.policy_unit.value_namespace = name_space
                                        self.policy_unit.value_namespace_prefix = name_space_prefix
                                    if(value_path == "policy-value"):
                                        self.policy_value = value
                                        self.policy_value.value_namespace = name_space
                                        self.policy_value.value_namespace_prefix = name_space_prefix


                            class ConformAction(Entity):
                                """
                                Conform action
                                
                                .. attribute:: action_type
                                
                                	Policer action type
                                	**type**\:   :py:class:`DnxQoseaShowAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowAction>`
                                
                                .. attribute:: mark
                                
                                	Action mark
                                	**type**\: list of    :py:class:`Mark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConformAction.Mark>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConformAction, self).__init__()

                                    self.yang_name = "conform-action"
                                    self.yang_parent_name = "class"

                                    self.action_type = YLeaf(YType.enumeration, "action-type")

                                    self.mark = YList(self)

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
                                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConformAction, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConformAction, self).__setattr__(name, value)


                                class Mark(Entity):
                                    """
                                    Action mark
                                    
                                    .. attribute:: mark_type
                                    
                                    	Mark type
                                    	**type**\:   :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                    
                                    .. attribute:: mark_value
                                    
                                    	Mark value
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConformAction.Mark, self).__init__()

                                        self.yang_name = "mark"
                                        self.yang_parent_name = "conform-action"

                                        self.mark_type = YLeaf(YType.enumeration, "mark-type")

                                        self.mark_value = YLeaf(YType.uint16, "mark-value")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("mark_type",
                                                        "mark_value") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConformAction.Mark, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConformAction.Mark, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.mark_type.is_set or
                                            self.mark_value.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.mark_type.yfilter != YFilter.not_set or
                                            self.mark_value.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "mark" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.mark_type.is_set or self.mark_type.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.mark_type.get_name_leafdata())
                                        if (self.mark_value.is_set or self.mark_value.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.mark_value.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "mark-type" or name == "mark-value"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "mark-type"):
                                            self.mark_type = value
                                            self.mark_type.value_namespace = name_space
                                            self.mark_type.value_namespace_prefix = name_space_prefix
                                        if(value_path == "mark-value"):
                                            self.mark_value = value
                                            self.mark_value.value_namespace = name_space
                                            self.mark_value.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.mark:
                                        if (c.has_data()):
                                            return True
                                    return self.action_type.is_set

                                def has_operation(self):
                                    for c in self.mark:
                                        if (c.has_operation()):
                                            return True
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.action_type.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "conform-action" + path_buffer

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

                                    if (child_yang_name == "mark"):
                                        for c in self.mark:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConformAction.Mark()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.mark.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "mark" or name == "action-type"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "action-type"):
                                        self.action_type = value
                                        self.action_type.value_namespace = name_space
                                        self.action_type.value_namespace_prefix = name_space_prefix


                            class ExceedAction(Entity):
                                """
                                Exceed action
                                
                                .. attribute:: action_type
                                
                                	Policer action type
                                	**type**\:   :py:class:`DnxQoseaShowAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowAction>`
                                
                                .. attribute:: mark
                                
                                	Action mark
                                	**type**\: list of    :py:class:`Mark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ExceedAction.Mark>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ExceedAction, self).__init__()

                                    self.yang_name = "exceed-action"
                                    self.yang_parent_name = "class"

                                    self.action_type = YLeaf(YType.enumeration, "action-type")

                                    self.mark = YList(self)

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
                                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ExceedAction, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ExceedAction, self).__setattr__(name, value)


                                class Mark(Entity):
                                    """
                                    Action mark
                                    
                                    .. attribute:: mark_type
                                    
                                    	Mark type
                                    	**type**\:   :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                    
                                    .. attribute:: mark_value
                                    
                                    	Mark value
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ExceedAction.Mark, self).__init__()

                                        self.yang_name = "mark"
                                        self.yang_parent_name = "exceed-action"

                                        self.mark_type = YLeaf(YType.enumeration, "mark-type")

                                        self.mark_value = YLeaf(YType.uint16, "mark-value")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("mark_type",
                                                        "mark_value") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ExceedAction.Mark, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ExceedAction.Mark, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.mark_type.is_set or
                                            self.mark_value.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.mark_type.yfilter != YFilter.not_set or
                                            self.mark_value.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "mark" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.mark_type.is_set or self.mark_type.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.mark_type.get_name_leafdata())
                                        if (self.mark_value.is_set or self.mark_value.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.mark_value.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "mark-type" or name == "mark-value"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "mark-type"):
                                            self.mark_type = value
                                            self.mark_type.value_namespace = name_space
                                            self.mark_type.value_namespace_prefix = name_space_prefix
                                        if(value_path == "mark-value"):
                                            self.mark_value = value
                                            self.mark_value.value_namespace = name_space
                                            self.mark_value.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.mark:
                                        if (c.has_data()):
                                            return True
                                    return self.action_type.is_set

                                def has_operation(self):
                                    for c in self.mark:
                                        if (c.has_operation()):
                                            return True
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.action_type.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "exceed-action" + path_buffer

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

                                    if (child_yang_name == "mark"):
                                        for c in self.mark:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ExceedAction.Mark()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.mark.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "mark" or name == "action-type"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "action-type"):
                                        self.action_type = value
                                        self.action_type.value_namespace = name_space
                                        self.action_type.value_namespace_prefix = name_space_prefix


                            class ViolateAction(Entity):
                                """
                                Violate action
                                
                                .. attribute:: action_type
                                
                                	Policer action type
                                	**type**\:   :py:class:`DnxQoseaShowAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowAction>`
                                
                                .. attribute:: mark
                                
                                	Action mark
                                	**type**\: list of    :py:class:`Mark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ViolateAction.Mark>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ViolateAction, self).__init__()

                                    self.yang_name = "violate-action"
                                    self.yang_parent_name = "class"

                                    self.action_type = YLeaf(YType.enumeration, "action-type")

                                    self.mark = YList(self)

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
                                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ViolateAction, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ViolateAction, self).__setattr__(name, value)


                                class Mark(Entity):
                                    """
                                    Action mark
                                    
                                    .. attribute:: mark_type
                                    
                                    	Mark type
                                    	**type**\:   :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                    
                                    .. attribute:: mark_value
                                    
                                    	Mark value
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ViolateAction.Mark, self).__init__()

                                        self.yang_name = "mark"
                                        self.yang_parent_name = "violate-action"

                                        self.mark_type = YLeaf(YType.enumeration, "mark-type")

                                        self.mark_value = YLeaf(YType.uint16, "mark-value")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("mark_type",
                                                        "mark_value") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ViolateAction.Mark, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ViolateAction.Mark, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.mark_type.is_set or
                                            self.mark_value.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.mark_type.yfilter != YFilter.not_set or
                                            self.mark_value.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "mark" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.mark_type.is_set or self.mark_type.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.mark_type.get_name_leafdata())
                                        if (self.mark_value.is_set or self.mark_value.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.mark_value.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "mark-type" or name == "mark-value"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "mark-type"):
                                            self.mark_type = value
                                            self.mark_type.value_namespace = name_space
                                            self.mark_type.value_namespace_prefix = name_space_prefix
                                        if(value_path == "mark-value"):
                                            self.mark_value = value
                                            self.mark_value.value_namespace = name_space
                                            self.mark_value.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.mark:
                                        if (c.has_data()):
                                            return True
                                    return self.action_type.is_set

                                def has_operation(self):
                                    for c in self.mark:
                                        if (c.has_operation()):
                                            return True
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.action_type.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "violate-action" + path_buffer

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

                                    if (child_yang_name == "mark"):
                                        for c in self.mark:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ViolateAction.Mark()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.mark.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "mark" or name == "action-type"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "action-type"):
                                        self.action_type = value
                                        self.action_type.value_namespace = name_space
                                        self.action_type.value_namespace_prefix = name_space_prefix


                            class IpMark(Entity):
                                """
                                IP mark
                                
                                .. attribute:: mark_type
                                
                                	Mark type
                                	**type**\:   :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                
                                .. attribute:: mark_value
                                
                                	Mark value
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.IpMark, self).__init__()

                                    self.yang_name = "ip-mark"
                                    self.yang_parent_name = "class"

                                    self.mark_type = YLeaf(YType.enumeration, "mark-type")

                                    self.mark_value = YLeaf(YType.uint16, "mark-value")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("mark_type",
                                                    "mark_value") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.IpMark, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.IpMark, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.mark_type.is_set or
                                        self.mark_value.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.mark_type.yfilter != YFilter.not_set or
                                        self.mark_value.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "ip-mark" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.mark_type.is_set or self.mark_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.mark_type.get_name_leafdata())
                                    if (self.mark_value.is_set or self.mark_value.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.mark_value.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "mark-type" or name == "mark-value"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "mark-type"):
                                        self.mark_type = value
                                        self.mark_type.value_namespace = name_space
                                        self.mark_type.value_namespace_prefix = name_space_prefix
                                    if(value_path == "mark-value"):
                                        self.mark_value = value
                                        self.mark_value.value_namespace = name_space
                                        self.mark_value.value_namespace_prefix = name_space_prefix


                            class CommonMark(Entity):
                                """
                                Common mark
                                
                                .. attribute:: mark_type
                                
                                	Mark type
                                	**type**\:   :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                
                                .. attribute:: mark_value
                                
                                	Mark value
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.CommonMark, self).__init__()

                                    self.yang_name = "common-mark"
                                    self.yang_parent_name = "class"

                                    self.mark_type = YLeaf(YType.enumeration, "mark-type")

                                    self.mark_value = YLeaf(YType.uint16, "mark-value")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("mark_type",
                                                    "mark_value") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.CommonMark, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.CommonMark, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.mark_type.is_set or
                                        self.mark_value.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.mark_type.yfilter != YFilter.not_set or
                                        self.mark_value.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "common-mark" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.mark_type.is_set or self.mark_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.mark_type.get_name_leafdata())
                                    if (self.mark_value.is_set or self.mark_value.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.mark_value.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "mark-type" or name == "mark-value"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "mark-type"):
                                        self.mark_type = value
                                        self.mark_type.value_namespace = name_space
                                        self.mark_type.value_namespace_prefix = name_space_prefix
                                    if(value_path == "mark-value"):
                                        self.mark_value = value
                                        self.mark_value.value_namespace = name_space
                                        self.mark_value.value_namespace_prefix = name_space_prefix


                            class MplsMark(Entity):
                                """
                                MPLS mark
                                
                                .. attribute:: mark_type
                                
                                	Mark type
                                	**type**\:   :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                
                                .. attribute:: mark_value
                                
                                	Mark value
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.MplsMark, self).__init__()

                                    self.yang_name = "mpls-mark"
                                    self.yang_parent_name = "class"

                                    self.mark_type = YLeaf(YType.enumeration, "mark-type")

                                    self.mark_value = YLeaf(YType.uint16, "mark-value")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("mark_type",
                                                    "mark_value") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.MplsMark, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.MplsMark, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.mark_type.is_set or
                                        self.mark_value.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.mark_type.yfilter != YFilter.not_set or
                                        self.mark_value.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "mpls-mark" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.mark_type.is_set or self.mark_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.mark_type.get_name_leafdata())
                                    if (self.mark_value.is_set or self.mark_value.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.mark_value.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "mark-type" or name == "mark-value"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "mark-type"):
                                        self.mark_type = value
                                        self.mark_type.value_namespace = name_space
                                        self.mark_type.value_namespace_prefix = name_space_prefix
                                    if(value_path == "mark-value"):
                                        self.mark_value = value
                                        self.mark_value.value_namespace = name_space
                                        self.mark_value.value_namespace_prefix = name_space_prefix


                            class Wred(Entity):
                                """
                                WRED parameters
                                
                                .. attribute:: config_max_threshold
                                
                                	Configured maximum threshold
                                	**type**\:   :py:class:`ConfigMaxThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.ConfigMaxThreshold>`
                                
                                .. attribute:: config_min_threshold
                                
                                	Configured minimum threshold
                                	**type**\:   :py:class:`ConfigMinThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.ConfigMinThreshold>`
                                
                                .. attribute:: first_segment
                                
                                	First segment
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: hardware_max_threshold_bytes
                                
                                	Hardware maximum threshold
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: hardware_min_threshold_bytes
                                
                                	Hardware minimum threshold
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: segment_size
                                
                                	Segment size
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: wred_match_type
                                
                                	WREDMatchType
                                	**type**\:   :py:class:`DnxQoseaShowWred <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowWred>`
                                
                                .. attribute:: wred_match_value
                                
                                	WRED match values
                                	**type**\:   :py:class:`WredMatchValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.WredMatchValue>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred, self).__init__()

                                    self.yang_name = "wred"
                                    self.yang_parent_name = "class"

                                    self.first_segment = YLeaf(YType.uint16, "first-segment")

                                    self.hardware_max_threshold_bytes = YLeaf(YType.uint32, "hardware-max-threshold-bytes")

                                    self.hardware_min_threshold_bytes = YLeaf(YType.uint32, "hardware-min-threshold-bytes")

                                    self.segment_size = YLeaf(YType.uint32, "segment-size")

                                    self.wred_match_type = YLeaf(YType.enumeration, "wred-match-type")

                                    self.config_max_threshold = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.ConfigMaxThreshold()
                                    self.config_max_threshold.parent = self
                                    self._children_name_map["config_max_threshold"] = "config-max-threshold"
                                    self._children_yang_names.add("config-max-threshold")

                                    self.config_min_threshold = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.ConfigMinThreshold()
                                    self.config_min_threshold.parent = self
                                    self._children_name_map["config_min_threshold"] = "config-min-threshold"
                                    self._children_yang_names.add("config-min-threshold")

                                    self.wred_match_value = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.WredMatchValue()
                                    self.wred_match_value.parent = self
                                    self._children_name_map["wred_match_value"] = "wred-match-value"
                                    self._children_yang_names.add("wred-match-value")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("first_segment",
                                                    "hardware_max_threshold_bytes",
                                                    "hardware_min_threshold_bytes",
                                                    "segment_size",
                                                    "wred_match_type") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred, self).__setattr__(name, value)


                                class WredMatchValue(Entity):
                                    """
                                    WRED match values
                                    
                                    .. attribute:: dnx_qosea_show_red_match_value
                                    
                                    	dnx qosea show red match value
                                    	**type**\: list of    :py:class:`DnxQoseaShowRedMatchValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.WredMatchValue.DnxQoseaShowRedMatchValue>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.WredMatchValue, self).__init__()

                                        self.yang_name = "wred-match-value"
                                        self.yang_parent_name = "wred"

                                        self.dnx_qosea_show_red_match_value = YList(self)

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
                                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.WredMatchValue, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.WredMatchValue, self).__setattr__(name, value)


                                    class DnxQoseaShowRedMatchValue(Entity):
                                        """
                                        dnx qosea show red match value
                                        
                                        .. attribute:: range_end
                                        
                                        	End value of a range
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: range_start
                                        
                                        	Start value of a range
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.WredMatchValue.DnxQoseaShowRedMatchValue, self).__init__()

                                            self.yang_name = "dnx-qosea-show-red-match-value"
                                            self.yang_parent_name = "wred-match-value"

                                            self.range_end = YLeaf(YType.uint8, "range-end")

                                            self.range_start = YLeaf(YType.uint8, "range-start")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("range_end",
                                                            "range_start") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.WredMatchValue.DnxQoseaShowRedMatchValue, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.WredMatchValue.DnxQoseaShowRedMatchValue, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.range_end.is_set or
                                                self.range_start.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.range_end.yfilter != YFilter.not_set or
                                                self.range_start.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "dnx-qosea-show-red-match-value" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.range_end.is_set or self.range_end.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.range_end.get_name_leafdata())
                                            if (self.range_start.is_set or self.range_start.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.range_start.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "range-end" or name == "range-start"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "range-end"):
                                                self.range_end = value
                                                self.range_end.value_namespace = name_space
                                                self.range_end.value_namespace_prefix = name_space_prefix
                                            if(value_path == "range-start"):
                                                self.range_start = value
                                                self.range_start.value_namespace = name_space
                                                self.range_start.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        for c in self.dnx_qosea_show_red_match_value:
                                            if (c.has_data()):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for c in self.dnx_qosea_show_red_match_value:
                                            if (c.has_operation()):
                                                return True
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "wred-match-value" + path_buffer

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

                                        if (child_yang_name == "dnx-qosea-show-red-match-value"):
                                            for c in self.dnx_qosea_show_red_match_value:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.WredMatchValue.DnxQoseaShowRedMatchValue()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.dnx_qosea_show_red_match_value.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "dnx-qosea-show-red-match-value"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass


                                class ConfigMinThreshold(Entity):
                                    """
                                    Configured minimum threshold
                                    
                                    .. attribute:: policy_unit
                                    
                                    	Policy unit
                                    	**type**\:   :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                    
                                    .. attribute:: policy_value
                                    
                                    	Policy value
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.ConfigMinThreshold, self).__init__()

                                        self.yang_name = "config-min-threshold"
                                        self.yang_parent_name = "wred"

                                        self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                        self.policy_value = YLeaf(YType.uint32, "policy-value")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("policy_unit",
                                                        "policy_value") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.ConfigMinThreshold, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.ConfigMinThreshold, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.policy_unit.is_set or
                                            self.policy_value.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.policy_unit.yfilter != YFilter.not_set or
                                            self.policy_value.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "config-min-threshold" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.policy_unit.is_set or self.policy_unit.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.policy_unit.get_name_leafdata())
                                        if (self.policy_value.is_set or self.policy_value.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.policy_value.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "policy-unit" or name == "policy-value"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "policy-unit"):
                                            self.policy_unit = value
                                            self.policy_unit.value_namespace = name_space
                                            self.policy_unit.value_namespace_prefix = name_space_prefix
                                        if(value_path == "policy-value"):
                                            self.policy_value = value
                                            self.policy_value.value_namespace = name_space
                                            self.policy_value.value_namespace_prefix = name_space_prefix


                                class ConfigMaxThreshold(Entity):
                                    """
                                    Configured maximum threshold
                                    
                                    .. attribute:: policy_unit
                                    
                                    	Policy unit
                                    	**type**\:   :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                    
                                    .. attribute:: policy_value
                                    
                                    	Policy value
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.ConfigMaxThreshold, self).__init__()

                                        self.yang_name = "config-max-threshold"
                                        self.yang_parent_name = "wred"

                                        self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                        self.policy_value = YLeaf(YType.uint32, "policy-value")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("policy_unit",
                                                        "policy_value") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.ConfigMaxThreshold, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.ConfigMaxThreshold, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.policy_unit.is_set or
                                            self.policy_value.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.policy_unit.yfilter != YFilter.not_set or
                                            self.policy_value.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "config-max-threshold" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.policy_unit.is_set or self.policy_unit.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.policy_unit.get_name_leafdata())
                                        if (self.policy_value.is_set or self.policy_value.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.policy_value.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "policy-unit" or name == "policy-value"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "policy-unit"):
                                            self.policy_unit = value
                                            self.policy_unit.value_namespace = name_space
                                            self.policy_unit.value_namespace_prefix = name_space_prefix
                                        if(value_path == "policy-value"):
                                            self.policy_value = value
                                            self.policy_value.value_namespace = name_space
                                            self.policy_value.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    return (
                                        self.first_segment.is_set or
                                        self.hardware_max_threshold_bytes.is_set or
                                        self.hardware_min_threshold_bytes.is_set or
                                        self.segment_size.is_set or
                                        self.wred_match_type.is_set or
                                        (self.config_max_threshold is not None and self.config_max_threshold.has_data()) or
                                        (self.config_min_threshold is not None and self.config_min_threshold.has_data()) or
                                        (self.wred_match_value is not None and self.wred_match_value.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.first_segment.yfilter != YFilter.not_set or
                                        self.hardware_max_threshold_bytes.yfilter != YFilter.not_set or
                                        self.hardware_min_threshold_bytes.yfilter != YFilter.not_set or
                                        self.segment_size.yfilter != YFilter.not_set or
                                        self.wred_match_type.yfilter != YFilter.not_set or
                                        (self.config_max_threshold is not None and self.config_max_threshold.has_operation()) or
                                        (self.config_min_threshold is not None and self.config_min_threshold.has_operation()) or
                                        (self.wred_match_value is not None and self.wred_match_value.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "wred" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.first_segment.is_set or self.first_segment.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.first_segment.get_name_leafdata())
                                    if (self.hardware_max_threshold_bytes.is_set or self.hardware_max_threshold_bytes.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.hardware_max_threshold_bytes.get_name_leafdata())
                                    if (self.hardware_min_threshold_bytes.is_set or self.hardware_min_threshold_bytes.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.hardware_min_threshold_bytes.get_name_leafdata())
                                    if (self.segment_size.is_set or self.segment_size.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.segment_size.get_name_leafdata())
                                    if (self.wred_match_type.is_set or self.wred_match_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.wred_match_type.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "config-max-threshold"):
                                        if (self.config_max_threshold is None):
                                            self.config_max_threshold = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.ConfigMaxThreshold()
                                            self.config_max_threshold.parent = self
                                            self._children_name_map["config_max_threshold"] = "config-max-threshold"
                                        return self.config_max_threshold

                                    if (child_yang_name == "config-min-threshold"):
                                        if (self.config_min_threshold is None):
                                            self.config_min_threshold = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.ConfigMinThreshold()
                                            self.config_min_threshold.parent = self
                                            self._children_name_map["config_min_threshold"] = "config-min-threshold"
                                        return self.config_min_threshold

                                    if (child_yang_name == "wred-match-value"):
                                        if (self.wred_match_value is None):
                                            self.wred_match_value = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.WredMatchValue()
                                            self.wred_match_value.parent = self
                                            self._children_name_map["wred_match_value"] = "wred-match-value"
                                        return self.wred_match_value

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "config-max-threshold" or name == "config-min-threshold" or name == "wred-match-value" or name == "first-segment" or name == "hardware-max-threshold-bytes" or name == "hardware-min-threshold-bytes" or name == "segment-size" or name == "wred-match-type"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "first-segment"):
                                        self.first_segment = value
                                        self.first_segment.value_namespace = name_space
                                        self.first_segment.value_namespace_prefix = name_space_prefix
                                    if(value_path == "hardware-max-threshold-bytes"):
                                        self.hardware_max_threshold_bytes = value
                                        self.hardware_max_threshold_bytes.value_namespace = name_space
                                        self.hardware_max_threshold_bytes.value_namespace_prefix = name_space_prefix
                                    if(value_path == "hardware-min-threshold-bytes"):
                                        self.hardware_min_threshold_bytes = value
                                        self.hardware_min_threshold_bytes.value_namespace = name_space
                                        self.hardware_min_threshold_bytes.value_namespace_prefix = name_space_prefix
                                    if(value_path == "segment-size"):
                                        self.segment_size = value
                                        self.segment_size.value_namespace = name_space
                                        self.segment_size.value_namespace_prefix = name_space_prefix
                                    if(value_path == "wred-match-type"):
                                        self.wred_match_type = value
                                        self.wred_match_type.value_namespace = name_space
                                        self.wred_match_type.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.common_mark:
                                    if (c.has_data()):
                                        return True
                                for c in self.ip_mark:
                                    if (c.has_data()):
                                        return True
                                for c in self.mpls_mark:
                                    if (c.has_data()):
                                        return True
                                for c in self.wred:
                                    if (c.has_data()):
                                        return True
                                return (
                                    self.level_one_class_name.is_set or
                                    self.class_level.is_set or
                                    self.config_excess_bandwidth_percent.is_set or
                                    self.config_excess_bandwidth_unit.is_set or
                                    self.egress_queue_id.is_set or
                                    self.hardware_excess_bandwidth_weight.is_set or
                                    self.hardware_max_rate_kbps.is_set or
                                    self.hardware_min_rate_kbps.is_set or
                                    self.hardware_policer_average_rate_kbps.is_set or
                                    self.hardware_policer_conform_burst_bytes.is_set or
                                    self.hardware_policer_excess_burst_bytes.is_set or
                                    self.hardware_policer_peak_rate_kbps.is_set or
                                    self.hardware_queue_limit_bytes.is_set or
                                    self.hardware_queue_limit_microseconds.is_set or
                                    self.level_two_class_name.is_set or
                                    self.network_min_bandwidth_kbps.is_set or
                                    self.policer_bucket_id.is_set or
                                    self.policer_stats_handle.is_set or
                                    self.priority_level.is_set or
                                    self.queue_type.is_set or
                                    (self.config_max_rate is not None and self.config_max_rate.has_data()) or
                                    (self.config_min_rate is not None and self.config_min_rate.has_data()) or
                                    (self.config_policer_average_rate is not None and self.config_policer_average_rate.has_data()) or
                                    (self.config_policer_conform_burst is not None and self.config_policer_conform_burst.has_data()) or
                                    (self.config_policer_excess_burst is not None and self.config_policer_excess_burst.has_data()) or
                                    (self.config_policer_peak_rate is not None and self.config_policer_peak_rate.has_data()) or
                                    (self.config_queue_limit is not None and self.config_queue_limit.has_data()) or
                                    (self.conform_action is not None and self.conform_action.has_data()) or
                                    (self.exceed_action is not None and self.exceed_action.has_data()) or
                                    (self.violate_action is not None and self.violate_action.has_data()))

                            def has_operation(self):
                                for c in self.common_mark:
                                    if (c.has_operation()):
                                        return True
                                for c in self.ip_mark:
                                    if (c.has_operation()):
                                        return True
                                for c in self.mpls_mark:
                                    if (c.has_operation()):
                                        return True
                                for c in self.wred:
                                    if (c.has_operation()):
                                        return True
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.level_one_class_name.yfilter != YFilter.not_set or
                                    self.class_level.yfilter != YFilter.not_set or
                                    self.config_excess_bandwidth_percent.yfilter != YFilter.not_set or
                                    self.config_excess_bandwidth_unit.yfilter != YFilter.not_set or
                                    self.egress_queue_id.yfilter != YFilter.not_set or
                                    self.hardware_excess_bandwidth_weight.yfilter != YFilter.not_set or
                                    self.hardware_max_rate_kbps.yfilter != YFilter.not_set or
                                    self.hardware_min_rate_kbps.yfilter != YFilter.not_set or
                                    self.hardware_policer_average_rate_kbps.yfilter != YFilter.not_set or
                                    self.hardware_policer_conform_burst_bytes.yfilter != YFilter.not_set or
                                    self.hardware_policer_excess_burst_bytes.yfilter != YFilter.not_set or
                                    self.hardware_policer_peak_rate_kbps.yfilter != YFilter.not_set or
                                    self.hardware_queue_limit_bytes.yfilter != YFilter.not_set or
                                    self.hardware_queue_limit_microseconds.yfilter != YFilter.not_set or
                                    self.level_two_class_name.yfilter != YFilter.not_set or
                                    self.network_min_bandwidth_kbps.yfilter != YFilter.not_set or
                                    self.policer_bucket_id.yfilter != YFilter.not_set or
                                    self.policer_stats_handle.yfilter != YFilter.not_set or
                                    self.priority_level.yfilter != YFilter.not_set or
                                    self.queue_type.yfilter != YFilter.not_set or
                                    (self.config_max_rate is not None and self.config_max_rate.has_operation()) or
                                    (self.config_min_rate is not None and self.config_min_rate.has_operation()) or
                                    (self.config_policer_average_rate is not None and self.config_policer_average_rate.has_operation()) or
                                    (self.config_policer_conform_burst is not None and self.config_policer_conform_burst.has_operation()) or
                                    (self.config_policer_excess_burst is not None and self.config_policer_excess_burst.has_operation()) or
                                    (self.config_policer_peak_rate is not None and self.config_policer_peak_rate.has_operation()) or
                                    (self.config_queue_limit is not None and self.config_queue_limit.has_operation()) or
                                    (self.conform_action is not None and self.conform_action.has_operation()) or
                                    (self.exceed_action is not None and self.exceed_action.has_operation()) or
                                    (self.violate_action is not None and self.violate_action.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "class" + "[level-one-class-name='" + self.level_one_class_name.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.level_one_class_name.is_set or self.level_one_class_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.level_one_class_name.get_name_leafdata())
                                if (self.class_level.is_set or self.class_level.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.class_level.get_name_leafdata())
                                if (self.config_excess_bandwidth_percent.is_set or self.config_excess_bandwidth_percent.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.config_excess_bandwidth_percent.get_name_leafdata())
                                if (self.config_excess_bandwidth_unit.is_set or self.config_excess_bandwidth_unit.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.config_excess_bandwidth_unit.get_name_leafdata())
                                if (self.egress_queue_id.is_set or self.egress_queue_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.egress_queue_id.get_name_leafdata())
                                if (self.hardware_excess_bandwidth_weight.is_set or self.hardware_excess_bandwidth_weight.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.hardware_excess_bandwidth_weight.get_name_leafdata())
                                if (self.hardware_max_rate_kbps.is_set or self.hardware_max_rate_kbps.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.hardware_max_rate_kbps.get_name_leafdata())
                                if (self.hardware_min_rate_kbps.is_set or self.hardware_min_rate_kbps.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.hardware_min_rate_kbps.get_name_leafdata())
                                if (self.hardware_policer_average_rate_kbps.is_set or self.hardware_policer_average_rate_kbps.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.hardware_policer_average_rate_kbps.get_name_leafdata())
                                if (self.hardware_policer_conform_burst_bytes.is_set or self.hardware_policer_conform_burst_bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.hardware_policer_conform_burst_bytes.get_name_leafdata())
                                if (self.hardware_policer_excess_burst_bytes.is_set or self.hardware_policer_excess_burst_bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.hardware_policer_excess_burst_bytes.get_name_leafdata())
                                if (self.hardware_policer_peak_rate_kbps.is_set or self.hardware_policer_peak_rate_kbps.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.hardware_policer_peak_rate_kbps.get_name_leafdata())
                                if (self.hardware_queue_limit_bytes.is_set or self.hardware_queue_limit_bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.hardware_queue_limit_bytes.get_name_leafdata())
                                if (self.hardware_queue_limit_microseconds.is_set or self.hardware_queue_limit_microseconds.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.hardware_queue_limit_microseconds.get_name_leafdata())
                                if (self.level_two_class_name.is_set or self.level_two_class_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.level_two_class_name.get_name_leafdata())
                                if (self.network_min_bandwidth_kbps.is_set or self.network_min_bandwidth_kbps.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.network_min_bandwidth_kbps.get_name_leafdata())
                                if (self.policer_bucket_id.is_set or self.policer_bucket_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.policer_bucket_id.get_name_leafdata())
                                if (self.policer_stats_handle.is_set or self.policer_stats_handle.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.policer_stats_handle.get_name_leafdata())
                                if (self.priority_level.is_set or self.priority_level.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.priority_level.get_name_leafdata())
                                if (self.queue_type.is_set or self.queue_type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.queue_type.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "common-mark"):
                                    for c in self.common_mark:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.CommonMark()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.common_mark.append(c)
                                    return c

                                if (child_yang_name == "config-max-rate"):
                                    if (self.config_max_rate is None):
                                        self.config_max_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigMaxRate()
                                        self.config_max_rate.parent = self
                                        self._children_name_map["config_max_rate"] = "config-max-rate"
                                    return self.config_max_rate

                                if (child_yang_name == "config-min-rate"):
                                    if (self.config_min_rate is None):
                                        self.config_min_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigMinRate()
                                        self.config_min_rate.parent = self
                                        self._children_name_map["config_min_rate"] = "config-min-rate"
                                    return self.config_min_rate

                                if (child_yang_name == "config-policer-average-rate"):
                                    if (self.config_policer_average_rate is None):
                                        self.config_policer_average_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerAverageRate()
                                        self.config_policer_average_rate.parent = self
                                        self._children_name_map["config_policer_average_rate"] = "config-policer-average-rate"
                                    return self.config_policer_average_rate

                                if (child_yang_name == "config-policer-conform-burst"):
                                    if (self.config_policer_conform_burst is None):
                                        self.config_policer_conform_burst = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerConformBurst()
                                        self.config_policer_conform_burst.parent = self
                                        self._children_name_map["config_policer_conform_burst"] = "config-policer-conform-burst"
                                    return self.config_policer_conform_burst

                                if (child_yang_name == "config-policer-excess-burst"):
                                    if (self.config_policer_excess_burst is None):
                                        self.config_policer_excess_burst = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerExcessBurst()
                                        self.config_policer_excess_burst.parent = self
                                        self._children_name_map["config_policer_excess_burst"] = "config-policer-excess-burst"
                                    return self.config_policer_excess_burst

                                if (child_yang_name == "config-policer-peak-rate"):
                                    if (self.config_policer_peak_rate is None):
                                        self.config_policer_peak_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerPeakRate()
                                        self.config_policer_peak_rate.parent = self
                                        self._children_name_map["config_policer_peak_rate"] = "config-policer-peak-rate"
                                    return self.config_policer_peak_rate

                                if (child_yang_name == "config-queue-limit"):
                                    if (self.config_queue_limit is None):
                                        self.config_queue_limit = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigQueueLimit()
                                        self.config_queue_limit.parent = self
                                        self._children_name_map["config_queue_limit"] = "config-queue-limit"
                                    return self.config_queue_limit

                                if (child_yang_name == "conform-action"):
                                    if (self.conform_action is None):
                                        self.conform_action = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConformAction()
                                        self.conform_action.parent = self
                                        self._children_name_map["conform_action"] = "conform-action"
                                    return self.conform_action

                                if (child_yang_name == "exceed-action"):
                                    if (self.exceed_action is None):
                                        self.exceed_action = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ExceedAction()
                                        self.exceed_action.parent = self
                                        self._children_name_map["exceed_action"] = "exceed-action"
                                    return self.exceed_action

                                if (child_yang_name == "ip-mark"):
                                    for c in self.ip_mark:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.IpMark()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.ip_mark.append(c)
                                    return c

                                if (child_yang_name == "mpls-mark"):
                                    for c in self.mpls_mark:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.MplsMark()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.mpls_mark.append(c)
                                    return c

                                if (child_yang_name == "violate-action"):
                                    if (self.violate_action is None):
                                        self.violate_action = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ViolateAction()
                                        self.violate_action.parent = self
                                        self._children_name_map["violate_action"] = "violate-action"
                                    return self.violate_action

                                if (child_yang_name == "wred"):
                                    for c in self.wred:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.wred.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "common-mark" or name == "config-max-rate" or name == "config-min-rate" or name == "config-policer-average-rate" or name == "config-policer-conform-burst" or name == "config-policer-excess-burst" or name == "config-policer-peak-rate" or name == "config-queue-limit" or name == "conform-action" or name == "exceed-action" or name == "ip-mark" or name == "mpls-mark" or name == "violate-action" or name == "wred" or name == "level-one-class-name" or name == "class-level" or name == "config-excess-bandwidth-percent" or name == "config-excess-bandwidth-unit" or name == "egress-queue-id" or name == "hardware-excess-bandwidth-weight" or name == "hardware-max-rate-kbps" or name == "hardware-min-rate-kbps" or name == "hardware-policer-average-rate-kbps" or name == "hardware-policer-conform-burst-bytes" or name == "hardware-policer-excess-burst-bytes" or name == "hardware-policer-peak-rate-kbps" or name == "hardware-queue-limit-bytes" or name == "hardware-queue-limit-microseconds" or name == "level-two-class-name" or name == "network-min-bandwidth-kbps" or name == "policer-bucket-id" or name == "policer-stats-handle" or name == "priority-level" or name == "queue-type"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "level-one-class-name"):
                                    self.level_one_class_name = value
                                    self.level_one_class_name.value_namespace = name_space
                                    self.level_one_class_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "class-level"):
                                    self.class_level = value
                                    self.class_level.value_namespace = name_space
                                    self.class_level.value_namespace_prefix = name_space_prefix
                                if(value_path == "config-excess-bandwidth-percent"):
                                    self.config_excess_bandwidth_percent = value
                                    self.config_excess_bandwidth_percent.value_namespace = name_space
                                    self.config_excess_bandwidth_percent.value_namespace_prefix = name_space_prefix
                                if(value_path == "config-excess-bandwidth-unit"):
                                    self.config_excess_bandwidth_unit = value
                                    self.config_excess_bandwidth_unit.value_namespace = name_space
                                    self.config_excess_bandwidth_unit.value_namespace_prefix = name_space_prefix
                                if(value_path == "egress-queue-id"):
                                    self.egress_queue_id = value
                                    self.egress_queue_id.value_namespace = name_space
                                    self.egress_queue_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "hardware-excess-bandwidth-weight"):
                                    self.hardware_excess_bandwidth_weight = value
                                    self.hardware_excess_bandwidth_weight.value_namespace = name_space
                                    self.hardware_excess_bandwidth_weight.value_namespace_prefix = name_space_prefix
                                if(value_path == "hardware-max-rate-kbps"):
                                    self.hardware_max_rate_kbps = value
                                    self.hardware_max_rate_kbps.value_namespace = name_space
                                    self.hardware_max_rate_kbps.value_namespace_prefix = name_space_prefix
                                if(value_path == "hardware-min-rate-kbps"):
                                    self.hardware_min_rate_kbps = value
                                    self.hardware_min_rate_kbps.value_namespace = name_space
                                    self.hardware_min_rate_kbps.value_namespace_prefix = name_space_prefix
                                if(value_path == "hardware-policer-average-rate-kbps"):
                                    self.hardware_policer_average_rate_kbps = value
                                    self.hardware_policer_average_rate_kbps.value_namespace = name_space
                                    self.hardware_policer_average_rate_kbps.value_namespace_prefix = name_space_prefix
                                if(value_path == "hardware-policer-conform-burst-bytes"):
                                    self.hardware_policer_conform_burst_bytes = value
                                    self.hardware_policer_conform_burst_bytes.value_namespace = name_space
                                    self.hardware_policer_conform_burst_bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "hardware-policer-excess-burst-bytes"):
                                    self.hardware_policer_excess_burst_bytes = value
                                    self.hardware_policer_excess_burst_bytes.value_namespace = name_space
                                    self.hardware_policer_excess_burst_bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "hardware-policer-peak-rate-kbps"):
                                    self.hardware_policer_peak_rate_kbps = value
                                    self.hardware_policer_peak_rate_kbps.value_namespace = name_space
                                    self.hardware_policer_peak_rate_kbps.value_namespace_prefix = name_space_prefix
                                if(value_path == "hardware-queue-limit-bytes"):
                                    self.hardware_queue_limit_bytes = value
                                    self.hardware_queue_limit_bytes.value_namespace = name_space
                                    self.hardware_queue_limit_bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "hardware-queue-limit-microseconds"):
                                    self.hardware_queue_limit_microseconds = value
                                    self.hardware_queue_limit_microseconds.value_namespace = name_space
                                    self.hardware_queue_limit_microseconds.value_namespace_prefix = name_space_prefix
                                if(value_path == "level-two-class-name"):
                                    self.level_two_class_name = value
                                    self.level_two_class_name.value_namespace = name_space
                                    self.level_two_class_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "network-min-bandwidth-kbps"):
                                    self.network_min_bandwidth_kbps = value
                                    self.network_min_bandwidth_kbps.value_namespace = name_space
                                    self.network_min_bandwidth_kbps.value_namespace_prefix = name_space_prefix
                                if(value_path == "policer-bucket-id"):
                                    self.policer_bucket_id = value
                                    self.policer_bucket_id.value_namespace = name_space
                                    self.policer_bucket_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "policer-stats-handle"):
                                    self.policer_stats_handle = value
                                    self.policer_stats_handle.value_namespace = name_space
                                    self.policer_stats_handle.value_namespace_prefix = name_space_prefix
                                if(value_path == "priority-level"):
                                    self.priority_level = value
                                    self.priority_level.value_namespace = name_space
                                    self.priority_level.value_namespace_prefix = name_space_prefix
                                if(value_path == "queue-type"):
                                    self.queue_type = value
                                    self.queue_type.value_namespace = name_space
                                    self.queue_type.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.class_:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.class_:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "classes" + path_buffer

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

                            if (child_yang_name == "class"):
                                for c in self.class_:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.class_.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "class"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.interface_name.is_set or
                            self.npu_id.is_set or
                            self.qos_direction.is_set or
                            (self.classes is not None and self.classes.has_data()) or
                            (self.member_interfaces is not None and self.member_interfaces.has_data()) or
                            (self.policy_details is not None and self.policy_details.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.npu_id.yfilter != YFilter.not_set or
                            self.qos_direction.yfilter != YFilter.not_set or
                            (self.classes is not None and self.classes.has_operation()) or
                            (self.member_interfaces is not None and self.member_interfaces.has_operation()) or
                            (self.policy_details is not None and self.policy_details.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "bundle-interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

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
                        if (self.npu_id.is_set or self.npu_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.npu_id.get_name_leafdata())
                        if (self.qos_direction.is_set or self.qos_direction.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.qos_direction.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "classes"):
                            if (self.classes is None):
                                self.classes = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes()
                                self.classes.parent = self
                                self._children_name_map["classes"] = "classes"
                            return self.classes

                        if (child_yang_name == "member-interfaces"):
                            if (self.member_interfaces is None):
                                self.member_interfaces = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces()
                                self.member_interfaces.parent = self
                                self._children_name_map["member_interfaces"] = "member-interfaces"
                            return self.member_interfaces

                        if (child_yang_name == "policy-details"):
                            if (self.policy_details is None):
                                self.policy_details = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.PolicyDetails()
                                self.policy_details.parent = self
                                self._children_name_map["policy_details"] = "policy-details"
                            return self.policy_details

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "classes" or name == "member-interfaces" or name == "policy-details" or name == "interface-name" or name == "npu-id" or name == "qos-direction"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "npu-id"):
                            self.npu_id = value
                            self.npu_id.value_namespace = name_space
                            self.npu_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "qos-direction"):
                            self.qos_direction = value
                            self.qos_direction.value_namespace = name_space
                            self.qos_direction.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.bundle_interface:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.bundle_interface:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "bundle-interfaces" + path_buffer

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

                    if (child_yang_name == "bundle-interface"):
                        for c in self.bundle_interface:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.bundle_interface.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bundle-interface"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Interfaces(Entity):
                """
                QoS list of interfaces
                
                .. attribute:: interface
                
                	QoS interface names
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'ncs5500-qos-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PlatformQos.Nodes.Node.Interfaces, self).__init__()

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
                                super(PlatformQos.Nodes.Node.Interfaces, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PlatformQos.Nodes.Node.Interfaces, self).__setattr__(name, value)


                class Interface(Entity):
                    """
                    QoS interface names
                    
                    .. attribute:: interface_name  <key>
                    
                    	The name of the interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: classes
                    
                    	QoS list of class names
                    	**type**\:   :py:class:`Classes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes>`
                    
                    .. attribute:: policy_details
                    
                    	Policy Details
                    	**type**\:   :py:class:`PolicyDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.PolicyDetails>`
                    
                    .. attribute:: qos_direction
                    
                    	The interface direction on which QoS is applied to
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'ncs5500-qos-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PlatformQos.Nodes.Node.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.qos_direction = YLeaf(YType.str, "qos-direction")

                        self.classes = PlatformQos.Nodes.Node.Interfaces.Interface.Classes()
                        self.classes.parent = self
                        self._children_name_map["classes"] = "classes"
                        self._children_yang_names.add("classes")

                        self.policy_details = PlatformQos.Nodes.Node.Interfaces.Interface.PolicyDetails()
                        self.policy_details.parent = self
                        self._children_name_map["policy_details"] = "policy-details"
                        self._children_yang_names.add("policy-details")

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
                                        "qos_direction") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PlatformQos.Nodes.Node.Interfaces.Interface, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PlatformQos.Nodes.Node.Interfaces.Interface, self).__setattr__(name, value)


                    class PolicyDetails(Entity):
                        """
                        Policy Details
                        
                        .. attribute:: interface_bandwidth_kbps
                        
                        	Interface Bandwidth (in kbps)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: kbit/s
                        
                        .. attribute:: interface_handle
                        
                        	InterfaceHandle
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: interface_status
                        
                        	Interface Status
                        	**type**\:   :py:class:`DnxQoseaShowIntfStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowIntfStatus>`
                        
                        .. attribute:: npu_id
                        
                        	NPU ID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: policy_name
                        
                        	Policy name
                        	**type**\:  str
                        
                        	**length:** 0..64
                        
                        .. attribute:: policy_status
                        
                        	Policy Status
                        	**type**\:   :py:class:`DnxQoseaShowPolicyStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowPolicyStatus>`
                        
                        .. attribute:: stats_accounting_type
                        
                        	QoS Statistics Accounting Type
                        	**type**\:   :py:class:`QosPolicyAccountEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.QosPolicyAccountEnum>`
                        
                        .. attribute:: total_number_of_classes
                        
                        	Number of Classes
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: voq_base_address
                        
                        	VOQ base address
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: voq_stats_handle
                        
                        	VOQ stats handle
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'ncs5500-qos-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PlatformQos.Nodes.Node.Interfaces.Interface.PolicyDetails, self).__init__()

                            self.yang_name = "policy-details"
                            self.yang_parent_name = "interface"

                            self.interface_bandwidth_kbps = YLeaf(YType.uint32, "interface-bandwidth-kbps")

                            self.interface_handle = YLeaf(YType.uint32, "interface-handle")

                            self.interface_status = YLeaf(YType.enumeration, "interface-status")

                            self.npu_id = YLeaf(YType.uint32, "npu-id")

                            self.policy_name = YLeaf(YType.str, "policy-name")

                            self.policy_status = YLeaf(YType.enumeration, "policy-status")

                            self.stats_accounting_type = YLeaf(YType.enumeration, "stats-accounting-type")

                            self.total_number_of_classes = YLeaf(YType.uint16, "total-number-of-classes")

                            self.voq_base_address = YLeaf(YType.uint32, "voq-base-address")

                            self.voq_stats_handle = YLeaf(YType.uint64, "voq-stats-handle")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("interface_bandwidth_kbps",
                                            "interface_handle",
                                            "interface_status",
                                            "npu_id",
                                            "policy_name",
                                            "policy_status",
                                            "stats_accounting_type",
                                            "total_number_of_classes",
                                            "voq_base_address",
                                            "voq_stats_handle") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PlatformQos.Nodes.Node.Interfaces.Interface.PolicyDetails, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.PolicyDetails, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.interface_bandwidth_kbps.is_set or
                                self.interface_handle.is_set or
                                self.interface_status.is_set or
                                self.npu_id.is_set or
                                self.policy_name.is_set or
                                self.policy_status.is_set or
                                self.stats_accounting_type.is_set or
                                self.total_number_of_classes.is_set or
                                self.voq_base_address.is_set or
                                self.voq_stats_handle.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.interface_bandwidth_kbps.yfilter != YFilter.not_set or
                                self.interface_handle.yfilter != YFilter.not_set or
                                self.interface_status.yfilter != YFilter.not_set or
                                self.npu_id.yfilter != YFilter.not_set or
                                self.policy_name.yfilter != YFilter.not_set or
                                self.policy_status.yfilter != YFilter.not_set or
                                self.stats_accounting_type.yfilter != YFilter.not_set or
                                self.total_number_of_classes.yfilter != YFilter.not_set or
                                self.voq_base_address.yfilter != YFilter.not_set or
                                self.voq_stats_handle.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "policy-details" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.interface_bandwidth_kbps.is_set or self.interface_bandwidth_kbps.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface_bandwidth_kbps.get_name_leafdata())
                            if (self.interface_handle.is_set or self.interface_handle.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface_handle.get_name_leafdata())
                            if (self.interface_status.is_set or self.interface_status.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface_status.get_name_leafdata())
                            if (self.npu_id.is_set or self.npu_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.npu_id.get_name_leafdata())
                            if (self.policy_name.is_set or self.policy_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.policy_name.get_name_leafdata())
                            if (self.policy_status.is_set or self.policy_status.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.policy_status.get_name_leafdata())
                            if (self.stats_accounting_type.is_set or self.stats_accounting_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.stats_accounting_type.get_name_leafdata())
                            if (self.total_number_of_classes.is_set or self.total_number_of_classes.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.total_number_of_classes.get_name_leafdata())
                            if (self.voq_base_address.is_set or self.voq_base_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.voq_base_address.get_name_leafdata())
                            if (self.voq_stats_handle.is_set or self.voq_stats_handle.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.voq_stats_handle.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "interface-bandwidth-kbps" or name == "interface-handle" or name == "interface-status" or name == "npu-id" or name == "policy-name" or name == "policy-status" or name == "stats-accounting-type" or name == "total-number-of-classes" or name == "voq-base-address" or name == "voq-stats-handle"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "interface-bandwidth-kbps"):
                                self.interface_bandwidth_kbps = value
                                self.interface_bandwidth_kbps.value_namespace = name_space
                                self.interface_bandwidth_kbps.value_namespace_prefix = name_space_prefix
                            if(value_path == "interface-handle"):
                                self.interface_handle = value
                                self.interface_handle.value_namespace = name_space
                                self.interface_handle.value_namespace_prefix = name_space_prefix
                            if(value_path == "interface-status"):
                                self.interface_status = value
                                self.interface_status.value_namespace = name_space
                                self.interface_status.value_namespace_prefix = name_space_prefix
                            if(value_path == "npu-id"):
                                self.npu_id = value
                                self.npu_id.value_namespace = name_space
                                self.npu_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "policy-name"):
                                self.policy_name = value
                                self.policy_name.value_namespace = name_space
                                self.policy_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "policy-status"):
                                self.policy_status = value
                                self.policy_status.value_namespace = name_space
                                self.policy_status.value_namespace_prefix = name_space_prefix
                            if(value_path == "stats-accounting-type"):
                                self.stats_accounting_type = value
                                self.stats_accounting_type.value_namespace = name_space
                                self.stats_accounting_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "total-number-of-classes"):
                                self.total_number_of_classes = value
                                self.total_number_of_classes.value_namespace = name_space
                                self.total_number_of_classes.value_namespace_prefix = name_space_prefix
                            if(value_path == "voq-base-address"):
                                self.voq_base_address = value
                                self.voq_base_address.value_namespace = name_space
                                self.voq_base_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "voq-stats-handle"):
                                self.voq_stats_handle = value
                                self.voq_stats_handle.value_namespace = name_space
                                self.voq_stats_handle.value_namespace_prefix = name_space_prefix


                    class Classes(Entity):
                        """
                        QoS list of class names
                        
                        .. attribute:: class_
                        
                        	QoS policy class
                        	**type**\: list of    :py:class:`Class_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_>`
                        
                        

                        """

                        _prefix = 'ncs5500-qos-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes, self).__init__()

                            self.yang_name = "classes"
                            self.yang_parent_name = "interface"

                            self.class_ = YList(self)

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
                                        super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes, self).__setattr__(name, value)


                        class Class_(Entity):
                            """
                            QoS policy class
                            
                            .. attribute:: level_one_class_name  <key>
                            
                            	QoS policy class name at level 1
                            	**type**\:  str
                            
                            .. attribute:: class_level
                            
                            	Class level
                            	**type**\:   :py:class:`DnxQoseaShowLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowLevel>`
                            
                            .. attribute:: common_mark
                            
                            	Common mark
                            	**type**\: list of    :py:class:`CommonMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.CommonMark>`
                            
                            .. attribute:: config_excess_bandwidth_percent
                            
                            	Configured excess bandwidth percentage
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: percentage
                            
                            .. attribute:: config_excess_bandwidth_unit
                            
                            	Configured excess bandwidth unit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: config_max_rate
                            
                            	Configured maximum rate
                            	**type**\:   :py:class:`ConfigMaxRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigMaxRate>`
                            
                            .. attribute:: config_min_rate
                            
                            	Configured minimum rate
                            	**type**\:   :py:class:`ConfigMinRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigMinRate>`
                            
                            .. attribute:: config_policer_average_rate
                            
                            	Configured policer average rate
                            	**type**\:   :py:class:`ConfigPolicerAverageRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerAverageRate>`
                            
                            .. attribute:: config_policer_conform_burst
                            
                            	Configured policer conform burst
                            	**type**\:   :py:class:`ConfigPolicerConformBurst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerConformBurst>`
                            
                            .. attribute:: config_policer_excess_burst
                            
                            	Configured policer excess burst
                            	**type**\:   :py:class:`ConfigPolicerExcessBurst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerExcessBurst>`
                            
                            .. attribute:: config_policer_peak_rate
                            
                            	Config policer peak rate
                            	**type**\:   :py:class:`ConfigPolicerPeakRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerPeakRate>`
                            
                            .. attribute:: config_queue_limit
                            
                            	Configured queue limit
                            	**type**\:   :py:class:`ConfigQueueLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigQueueLimit>`
                            
                            .. attribute:: conform_action
                            
                            	Conform action
                            	**type**\:   :py:class:`ConformAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConformAction>`
                            
                            .. attribute:: egress_queue_id
                            
                            	Egress Queue ID
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: exceed_action
                            
                            	Exceed action
                            	**type**\:   :py:class:`ExceedAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ExceedAction>`
                            
                            .. attribute:: hardware_excess_bandwidth_weight
                            
                            	Hardware excess bandwidth weight
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hardware_max_rate_kbps
                            
                            	Hardware maximum rate in kbps
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: kbit/s
                            
                            .. attribute:: hardware_min_rate_kbps
                            
                            	Hardware minimum rate in kbps
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: kbit/s
                            
                            .. attribute:: hardware_policer_average_rate_kbps
                            
                            	Hardware policer average in kbps
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: kbit/s
                            
                            .. attribute:: hardware_policer_conform_burst_bytes
                            
                            	Hardware policer conform burst
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hardware_policer_excess_burst_bytes
                            
                            	Hardware policer excess burst
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hardware_policer_peak_rate_kbps
                            
                            	Hardware policer peak rate
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hardware_queue_limit_bytes
                            
                            	Hardware queue limit in bytes
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: hardware_queue_limit_microseconds
                            
                            	Hardware queue limit in microseconds
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: microsecond
                            
                            .. attribute:: ip_mark
                            
                            	IP mark
                            	**type**\: list of    :py:class:`IpMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.IpMark>`
                            
                            .. attribute:: level_two_class_name
                            
                            	QoS policy child class name at level 2
                            	**type**\:  str
                            
                            .. attribute:: mpls_mark
                            
                            	MPLS mark
                            	**type**\: list of    :py:class:`MplsMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.MplsMark>`
                            
                            .. attribute:: network_min_bandwidth_kbps
                            
                            	Network minimum Bandwith
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: policer_bucket_id
                            
                            	PolicerBucketID
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: policer_stats_handle
                            
                            	PolicerStatsHandle
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: priority_level
                            
                            	Priority level
                            	**type**\:   :py:class:`DnxQoseaShowHpLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowHpLevel>`
                            
                            .. attribute:: queue_type
                            
                            	Queue type
                            	**type**\:   :py:class:`DnxQoseaShowQueue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowQueue>`
                            
                            .. attribute:: violate_action
                            
                            	Violate action
                            	**type**\:   :py:class:`ViolateAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ViolateAction>`
                            
                            .. attribute:: wred
                            
                            	WRED parameters
                            	**type**\: list of    :py:class:`Wred <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred>`
                            
                            

                            """

                            _prefix = 'ncs5500-qos-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_, self).__init__()

                                self.yang_name = "class"
                                self.yang_parent_name = "classes"

                                self.level_one_class_name = YLeaf(YType.str, "level-one-class-name")

                                self.class_level = YLeaf(YType.enumeration, "class-level")

                                self.config_excess_bandwidth_percent = YLeaf(YType.uint32, "config-excess-bandwidth-percent")

                                self.config_excess_bandwidth_unit = YLeaf(YType.uint32, "config-excess-bandwidth-unit")

                                self.egress_queue_id = YLeaf(YType.int32, "egress-queue-id")

                                self.hardware_excess_bandwidth_weight = YLeaf(YType.uint32, "hardware-excess-bandwidth-weight")

                                self.hardware_max_rate_kbps = YLeaf(YType.uint32, "hardware-max-rate-kbps")

                                self.hardware_min_rate_kbps = YLeaf(YType.uint32, "hardware-min-rate-kbps")

                                self.hardware_policer_average_rate_kbps = YLeaf(YType.uint32, "hardware-policer-average-rate-kbps")

                                self.hardware_policer_conform_burst_bytes = YLeaf(YType.uint32, "hardware-policer-conform-burst-bytes")

                                self.hardware_policer_excess_burst_bytes = YLeaf(YType.uint32, "hardware-policer-excess-burst-bytes")

                                self.hardware_policer_peak_rate_kbps = YLeaf(YType.uint32, "hardware-policer-peak-rate-kbps")

                                self.hardware_queue_limit_bytes = YLeaf(YType.uint64, "hardware-queue-limit-bytes")

                                self.hardware_queue_limit_microseconds = YLeaf(YType.uint64, "hardware-queue-limit-microseconds")

                                self.level_two_class_name = YLeaf(YType.str, "level-two-class-name")

                                self.network_min_bandwidth_kbps = YLeaf(YType.uint32, "network-min-bandwidth-kbps")

                                self.policer_bucket_id = YLeaf(YType.uint32, "policer-bucket-id")

                                self.policer_stats_handle = YLeaf(YType.uint64, "policer-stats-handle")

                                self.priority_level = YLeaf(YType.enumeration, "priority-level")

                                self.queue_type = YLeaf(YType.enumeration, "queue-type")

                                self.config_max_rate = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigMaxRate()
                                self.config_max_rate.parent = self
                                self._children_name_map["config_max_rate"] = "config-max-rate"
                                self._children_yang_names.add("config-max-rate")

                                self.config_min_rate = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigMinRate()
                                self.config_min_rate.parent = self
                                self._children_name_map["config_min_rate"] = "config-min-rate"
                                self._children_yang_names.add("config-min-rate")

                                self.config_policer_average_rate = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerAverageRate()
                                self.config_policer_average_rate.parent = self
                                self._children_name_map["config_policer_average_rate"] = "config-policer-average-rate"
                                self._children_yang_names.add("config-policer-average-rate")

                                self.config_policer_conform_burst = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerConformBurst()
                                self.config_policer_conform_burst.parent = self
                                self._children_name_map["config_policer_conform_burst"] = "config-policer-conform-burst"
                                self._children_yang_names.add("config-policer-conform-burst")

                                self.config_policer_excess_burst = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerExcessBurst()
                                self.config_policer_excess_burst.parent = self
                                self._children_name_map["config_policer_excess_burst"] = "config-policer-excess-burst"
                                self._children_yang_names.add("config-policer-excess-burst")

                                self.config_policer_peak_rate = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerPeakRate()
                                self.config_policer_peak_rate.parent = self
                                self._children_name_map["config_policer_peak_rate"] = "config-policer-peak-rate"
                                self._children_yang_names.add("config-policer-peak-rate")

                                self.config_queue_limit = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigQueueLimit()
                                self.config_queue_limit.parent = self
                                self._children_name_map["config_queue_limit"] = "config-queue-limit"
                                self._children_yang_names.add("config-queue-limit")

                                self.conform_action = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConformAction()
                                self.conform_action.parent = self
                                self._children_name_map["conform_action"] = "conform-action"
                                self._children_yang_names.add("conform-action")

                                self.exceed_action = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ExceedAction()
                                self.exceed_action.parent = self
                                self._children_name_map["exceed_action"] = "exceed-action"
                                self._children_yang_names.add("exceed-action")

                                self.violate_action = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ViolateAction()
                                self.violate_action.parent = self
                                self._children_name_map["violate_action"] = "violate-action"
                                self._children_yang_names.add("violate-action")

                                self.common_mark = YList(self)
                                self.ip_mark = YList(self)
                                self.mpls_mark = YList(self)
                                self.wred = YList(self)

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("level_one_class_name",
                                                "class_level",
                                                "config_excess_bandwidth_percent",
                                                "config_excess_bandwidth_unit",
                                                "egress_queue_id",
                                                "hardware_excess_bandwidth_weight",
                                                "hardware_max_rate_kbps",
                                                "hardware_min_rate_kbps",
                                                "hardware_policer_average_rate_kbps",
                                                "hardware_policer_conform_burst_bytes",
                                                "hardware_policer_excess_burst_bytes",
                                                "hardware_policer_peak_rate_kbps",
                                                "hardware_queue_limit_bytes",
                                                "hardware_queue_limit_microseconds",
                                                "level_two_class_name",
                                                "network_min_bandwidth_kbps",
                                                "policer_bucket_id",
                                                "policer_stats_handle",
                                                "priority_level",
                                                "queue_type") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_, self).__setattr__(name, value)


                            class ConfigMaxRate(Entity):
                                """
                                Configured maximum rate
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:   :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigMaxRate, self).__init__()

                                    self.yang_name = "config-max-rate"
                                    self.yang_parent_name = "class"

                                    self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                    self.policy_value = YLeaf(YType.uint32, "policy-value")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("policy_unit",
                                                    "policy_value") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigMaxRate, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigMaxRate, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.policy_unit.is_set or
                                        self.policy_value.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.policy_unit.yfilter != YFilter.not_set or
                                        self.policy_value.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "config-max-rate" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.policy_unit.is_set or self.policy_unit.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.policy_unit.get_name_leafdata())
                                    if (self.policy_value.is_set or self.policy_value.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.policy_value.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "policy-unit" or name == "policy-value"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "policy-unit"):
                                        self.policy_unit = value
                                        self.policy_unit.value_namespace = name_space
                                        self.policy_unit.value_namespace_prefix = name_space_prefix
                                    if(value_path == "policy-value"):
                                        self.policy_value = value
                                        self.policy_value.value_namespace = name_space
                                        self.policy_value.value_namespace_prefix = name_space_prefix


                            class ConfigMinRate(Entity):
                                """
                                Configured minimum rate
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:   :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigMinRate, self).__init__()

                                    self.yang_name = "config-min-rate"
                                    self.yang_parent_name = "class"

                                    self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                    self.policy_value = YLeaf(YType.uint32, "policy-value")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("policy_unit",
                                                    "policy_value") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigMinRate, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigMinRate, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.policy_unit.is_set or
                                        self.policy_value.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.policy_unit.yfilter != YFilter.not_set or
                                        self.policy_value.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "config-min-rate" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.policy_unit.is_set or self.policy_unit.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.policy_unit.get_name_leafdata())
                                    if (self.policy_value.is_set or self.policy_value.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.policy_value.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "policy-unit" or name == "policy-value"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "policy-unit"):
                                        self.policy_unit = value
                                        self.policy_unit.value_namespace = name_space
                                        self.policy_unit.value_namespace_prefix = name_space_prefix
                                    if(value_path == "policy-value"):
                                        self.policy_value = value
                                        self.policy_value.value_namespace = name_space
                                        self.policy_value.value_namespace_prefix = name_space_prefix


                            class ConfigQueueLimit(Entity):
                                """
                                Configured queue limit
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:   :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigQueueLimit, self).__init__()

                                    self.yang_name = "config-queue-limit"
                                    self.yang_parent_name = "class"

                                    self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                    self.policy_value = YLeaf(YType.uint32, "policy-value")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("policy_unit",
                                                    "policy_value") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigQueueLimit, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigQueueLimit, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.policy_unit.is_set or
                                        self.policy_value.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.policy_unit.yfilter != YFilter.not_set or
                                        self.policy_value.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "config-queue-limit" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.policy_unit.is_set or self.policy_unit.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.policy_unit.get_name_leafdata())
                                    if (self.policy_value.is_set or self.policy_value.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.policy_value.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "policy-unit" or name == "policy-value"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "policy-unit"):
                                        self.policy_unit = value
                                        self.policy_unit.value_namespace = name_space
                                        self.policy_unit.value_namespace_prefix = name_space_prefix
                                    if(value_path == "policy-value"):
                                        self.policy_value = value
                                        self.policy_value.value_namespace = name_space
                                        self.policy_value.value_namespace_prefix = name_space_prefix


                            class ConfigPolicerAverageRate(Entity):
                                """
                                Configured policer average rate
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:   :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerAverageRate, self).__init__()

                                    self.yang_name = "config-policer-average-rate"
                                    self.yang_parent_name = "class"

                                    self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                    self.policy_value = YLeaf(YType.uint32, "policy-value")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("policy_unit",
                                                    "policy_value") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerAverageRate, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerAverageRate, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.policy_unit.is_set or
                                        self.policy_value.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.policy_unit.yfilter != YFilter.not_set or
                                        self.policy_value.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "config-policer-average-rate" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.policy_unit.is_set or self.policy_unit.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.policy_unit.get_name_leafdata())
                                    if (self.policy_value.is_set or self.policy_value.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.policy_value.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "policy-unit" or name == "policy-value"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "policy-unit"):
                                        self.policy_unit = value
                                        self.policy_unit.value_namespace = name_space
                                        self.policy_unit.value_namespace_prefix = name_space_prefix
                                    if(value_path == "policy-value"):
                                        self.policy_value = value
                                        self.policy_value.value_namespace = name_space
                                        self.policy_value.value_namespace_prefix = name_space_prefix


                            class ConfigPolicerPeakRate(Entity):
                                """
                                Config policer peak rate
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:   :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerPeakRate, self).__init__()

                                    self.yang_name = "config-policer-peak-rate"
                                    self.yang_parent_name = "class"

                                    self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                    self.policy_value = YLeaf(YType.uint32, "policy-value")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("policy_unit",
                                                    "policy_value") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerPeakRate, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerPeakRate, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.policy_unit.is_set or
                                        self.policy_value.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.policy_unit.yfilter != YFilter.not_set or
                                        self.policy_value.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "config-policer-peak-rate" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.policy_unit.is_set or self.policy_unit.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.policy_unit.get_name_leafdata())
                                    if (self.policy_value.is_set or self.policy_value.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.policy_value.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "policy-unit" or name == "policy-value"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "policy-unit"):
                                        self.policy_unit = value
                                        self.policy_unit.value_namespace = name_space
                                        self.policy_unit.value_namespace_prefix = name_space_prefix
                                    if(value_path == "policy-value"):
                                        self.policy_value = value
                                        self.policy_value.value_namespace = name_space
                                        self.policy_value.value_namespace_prefix = name_space_prefix


                            class ConfigPolicerConformBurst(Entity):
                                """
                                Configured policer conform burst
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:   :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerConformBurst, self).__init__()

                                    self.yang_name = "config-policer-conform-burst"
                                    self.yang_parent_name = "class"

                                    self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                    self.policy_value = YLeaf(YType.uint32, "policy-value")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("policy_unit",
                                                    "policy_value") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerConformBurst, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerConformBurst, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.policy_unit.is_set or
                                        self.policy_value.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.policy_unit.yfilter != YFilter.not_set or
                                        self.policy_value.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "config-policer-conform-burst" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.policy_unit.is_set or self.policy_unit.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.policy_unit.get_name_leafdata())
                                    if (self.policy_value.is_set or self.policy_value.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.policy_value.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "policy-unit" or name == "policy-value"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "policy-unit"):
                                        self.policy_unit = value
                                        self.policy_unit.value_namespace = name_space
                                        self.policy_unit.value_namespace_prefix = name_space_prefix
                                    if(value_path == "policy-value"):
                                        self.policy_value = value
                                        self.policy_value.value_namespace = name_space
                                        self.policy_value.value_namespace_prefix = name_space_prefix


                            class ConfigPolicerExcessBurst(Entity):
                                """
                                Configured policer excess burst
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:   :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerExcessBurst, self).__init__()

                                    self.yang_name = "config-policer-excess-burst"
                                    self.yang_parent_name = "class"

                                    self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                    self.policy_value = YLeaf(YType.uint32, "policy-value")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("policy_unit",
                                                    "policy_value") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerExcessBurst, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerExcessBurst, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.policy_unit.is_set or
                                        self.policy_value.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.policy_unit.yfilter != YFilter.not_set or
                                        self.policy_value.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "config-policer-excess-burst" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.policy_unit.is_set or self.policy_unit.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.policy_unit.get_name_leafdata())
                                    if (self.policy_value.is_set or self.policy_value.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.policy_value.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "policy-unit" or name == "policy-value"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "policy-unit"):
                                        self.policy_unit = value
                                        self.policy_unit.value_namespace = name_space
                                        self.policy_unit.value_namespace_prefix = name_space_prefix
                                    if(value_path == "policy-value"):
                                        self.policy_value = value
                                        self.policy_value.value_namespace = name_space
                                        self.policy_value.value_namespace_prefix = name_space_prefix


                            class ConformAction(Entity):
                                """
                                Conform action
                                
                                .. attribute:: action_type
                                
                                	Policer action type
                                	**type**\:   :py:class:`DnxQoseaShowAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowAction>`
                                
                                .. attribute:: mark
                                
                                	Action mark
                                	**type**\: list of    :py:class:`Mark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConformAction.Mark>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConformAction, self).__init__()

                                    self.yang_name = "conform-action"
                                    self.yang_parent_name = "class"

                                    self.action_type = YLeaf(YType.enumeration, "action-type")

                                    self.mark = YList(self)

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
                                                super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConformAction, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConformAction, self).__setattr__(name, value)


                                class Mark(Entity):
                                    """
                                    Action mark
                                    
                                    .. attribute:: mark_type
                                    
                                    	Mark type
                                    	**type**\:   :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                    
                                    .. attribute:: mark_value
                                    
                                    	Mark value
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConformAction.Mark, self).__init__()

                                        self.yang_name = "mark"
                                        self.yang_parent_name = "conform-action"

                                        self.mark_type = YLeaf(YType.enumeration, "mark-type")

                                        self.mark_value = YLeaf(YType.uint16, "mark-value")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("mark_type",
                                                        "mark_value") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConformAction.Mark, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConformAction.Mark, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.mark_type.is_set or
                                            self.mark_value.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.mark_type.yfilter != YFilter.not_set or
                                            self.mark_value.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "mark" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.mark_type.is_set or self.mark_type.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.mark_type.get_name_leafdata())
                                        if (self.mark_value.is_set or self.mark_value.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.mark_value.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "mark-type" or name == "mark-value"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "mark-type"):
                                            self.mark_type = value
                                            self.mark_type.value_namespace = name_space
                                            self.mark_type.value_namespace_prefix = name_space_prefix
                                        if(value_path == "mark-value"):
                                            self.mark_value = value
                                            self.mark_value.value_namespace = name_space
                                            self.mark_value.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.mark:
                                        if (c.has_data()):
                                            return True
                                    return self.action_type.is_set

                                def has_operation(self):
                                    for c in self.mark:
                                        if (c.has_operation()):
                                            return True
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.action_type.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "conform-action" + path_buffer

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

                                    if (child_yang_name == "mark"):
                                        for c in self.mark:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConformAction.Mark()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.mark.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "mark" or name == "action-type"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "action-type"):
                                        self.action_type = value
                                        self.action_type.value_namespace = name_space
                                        self.action_type.value_namespace_prefix = name_space_prefix


                            class ExceedAction(Entity):
                                """
                                Exceed action
                                
                                .. attribute:: action_type
                                
                                	Policer action type
                                	**type**\:   :py:class:`DnxQoseaShowAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowAction>`
                                
                                .. attribute:: mark
                                
                                	Action mark
                                	**type**\: list of    :py:class:`Mark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ExceedAction.Mark>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ExceedAction, self).__init__()

                                    self.yang_name = "exceed-action"
                                    self.yang_parent_name = "class"

                                    self.action_type = YLeaf(YType.enumeration, "action-type")

                                    self.mark = YList(self)

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
                                                super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ExceedAction, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ExceedAction, self).__setattr__(name, value)


                                class Mark(Entity):
                                    """
                                    Action mark
                                    
                                    .. attribute:: mark_type
                                    
                                    	Mark type
                                    	**type**\:   :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                    
                                    .. attribute:: mark_value
                                    
                                    	Mark value
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ExceedAction.Mark, self).__init__()

                                        self.yang_name = "mark"
                                        self.yang_parent_name = "exceed-action"

                                        self.mark_type = YLeaf(YType.enumeration, "mark-type")

                                        self.mark_value = YLeaf(YType.uint16, "mark-value")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("mark_type",
                                                        "mark_value") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ExceedAction.Mark, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ExceedAction.Mark, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.mark_type.is_set or
                                            self.mark_value.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.mark_type.yfilter != YFilter.not_set or
                                            self.mark_value.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "mark" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.mark_type.is_set or self.mark_type.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.mark_type.get_name_leafdata())
                                        if (self.mark_value.is_set or self.mark_value.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.mark_value.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "mark-type" or name == "mark-value"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "mark-type"):
                                            self.mark_type = value
                                            self.mark_type.value_namespace = name_space
                                            self.mark_type.value_namespace_prefix = name_space_prefix
                                        if(value_path == "mark-value"):
                                            self.mark_value = value
                                            self.mark_value.value_namespace = name_space
                                            self.mark_value.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.mark:
                                        if (c.has_data()):
                                            return True
                                    return self.action_type.is_set

                                def has_operation(self):
                                    for c in self.mark:
                                        if (c.has_operation()):
                                            return True
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.action_type.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "exceed-action" + path_buffer

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

                                    if (child_yang_name == "mark"):
                                        for c in self.mark:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ExceedAction.Mark()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.mark.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "mark" or name == "action-type"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "action-type"):
                                        self.action_type = value
                                        self.action_type.value_namespace = name_space
                                        self.action_type.value_namespace_prefix = name_space_prefix


                            class ViolateAction(Entity):
                                """
                                Violate action
                                
                                .. attribute:: action_type
                                
                                	Policer action type
                                	**type**\:   :py:class:`DnxQoseaShowAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowAction>`
                                
                                .. attribute:: mark
                                
                                	Action mark
                                	**type**\: list of    :py:class:`Mark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ViolateAction.Mark>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ViolateAction, self).__init__()

                                    self.yang_name = "violate-action"
                                    self.yang_parent_name = "class"

                                    self.action_type = YLeaf(YType.enumeration, "action-type")

                                    self.mark = YList(self)

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
                                                super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ViolateAction, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ViolateAction, self).__setattr__(name, value)


                                class Mark(Entity):
                                    """
                                    Action mark
                                    
                                    .. attribute:: mark_type
                                    
                                    	Mark type
                                    	**type**\:   :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                    
                                    .. attribute:: mark_value
                                    
                                    	Mark value
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ViolateAction.Mark, self).__init__()

                                        self.yang_name = "mark"
                                        self.yang_parent_name = "violate-action"

                                        self.mark_type = YLeaf(YType.enumeration, "mark-type")

                                        self.mark_value = YLeaf(YType.uint16, "mark-value")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("mark_type",
                                                        "mark_value") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ViolateAction.Mark, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ViolateAction.Mark, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.mark_type.is_set or
                                            self.mark_value.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.mark_type.yfilter != YFilter.not_set or
                                            self.mark_value.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "mark" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.mark_type.is_set or self.mark_type.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.mark_type.get_name_leafdata())
                                        if (self.mark_value.is_set or self.mark_value.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.mark_value.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "mark-type" or name == "mark-value"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "mark-type"):
                                            self.mark_type = value
                                            self.mark_type.value_namespace = name_space
                                            self.mark_type.value_namespace_prefix = name_space_prefix
                                        if(value_path == "mark-value"):
                                            self.mark_value = value
                                            self.mark_value.value_namespace = name_space
                                            self.mark_value.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.mark:
                                        if (c.has_data()):
                                            return True
                                    return self.action_type.is_set

                                def has_operation(self):
                                    for c in self.mark:
                                        if (c.has_operation()):
                                            return True
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.action_type.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "violate-action" + path_buffer

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

                                    if (child_yang_name == "mark"):
                                        for c in self.mark:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ViolateAction.Mark()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.mark.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "mark" or name == "action-type"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "action-type"):
                                        self.action_type = value
                                        self.action_type.value_namespace = name_space
                                        self.action_type.value_namespace_prefix = name_space_prefix


                            class IpMark(Entity):
                                """
                                IP mark
                                
                                .. attribute:: mark_type
                                
                                	Mark type
                                	**type**\:   :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                
                                .. attribute:: mark_value
                                
                                	Mark value
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.IpMark, self).__init__()

                                    self.yang_name = "ip-mark"
                                    self.yang_parent_name = "class"

                                    self.mark_type = YLeaf(YType.enumeration, "mark-type")

                                    self.mark_value = YLeaf(YType.uint16, "mark-value")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("mark_type",
                                                    "mark_value") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.IpMark, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.IpMark, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.mark_type.is_set or
                                        self.mark_value.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.mark_type.yfilter != YFilter.not_set or
                                        self.mark_value.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "ip-mark" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.mark_type.is_set or self.mark_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.mark_type.get_name_leafdata())
                                    if (self.mark_value.is_set or self.mark_value.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.mark_value.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "mark-type" or name == "mark-value"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "mark-type"):
                                        self.mark_type = value
                                        self.mark_type.value_namespace = name_space
                                        self.mark_type.value_namespace_prefix = name_space_prefix
                                    if(value_path == "mark-value"):
                                        self.mark_value = value
                                        self.mark_value.value_namespace = name_space
                                        self.mark_value.value_namespace_prefix = name_space_prefix


                            class CommonMark(Entity):
                                """
                                Common mark
                                
                                .. attribute:: mark_type
                                
                                	Mark type
                                	**type**\:   :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                
                                .. attribute:: mark_value
                                
                                	Mark value
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.CommonMark, self).__init__()

                                    self.yang_name = "common-mark"
                                    self.yang_parent_name = "class"

                                    self.mark_type = YLeaf(YType.enumeration, "mark-type")

                                    self.mark_value = YLeaf(YType.uint16, "mark-value")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("mark_type",
                                                    "mark_value") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.CommonMark, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.CommonMark, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.mark_type.is_set or
                                        self.mark_value.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.mark_type.yfilter != YFilter.not_set or
                                        self.mark_value.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "common-mark" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.mark_type.is_set or self.mark_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.mark_type.get_name_leafdata())
                                    if (self.mark_value.is_set or self.mark_value.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.mark_value.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "mark-type" or name == "mark-value"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "mark-type"):
                                        self.mark_type = value
                                        self.mark_type.value_namespace = name_space
                                        self.mark_type.value_namespace_prefix = name_space_prefix
                                    if(value_path == "mark-value"):
                                        self.mark_value = value
                                        self.mark_value.value_namespace = name_space
                                        self.mark_value.value_namespace_prefix = name_space_prefix


                            class MplsMark(Entity):
                                """
                                MPLS mark
                                
                                .. attribute:: mark_type
                                
                                	Mark type
                                	**type**\:   :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                
                                .. attribute:: mark_value
                                
                                	Mark value
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.MplsMark, self).__init__()

                                    self.yang_name = "mpls-mark"
                                    self.yang_parent_name = "class"

                                    self.mark_type = YLeaf(YType.enumeration, "mark-type")

                                    self.mark_value = YLeaf(YType.uint16, "mark-value")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("mark_type",
                                                    "mark_value") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.MplsMark, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.MplsMark, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.mark_type.is_set or
                                        self.mark_value.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.mark_type.yfilter != YFilter.not_set or
                                        self.mark_value.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "mpls-mark" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.mark_type.is_set or self.mark_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.mark_type.get_name_leafdata())
                                    if (self.mark_value.is_set or self.mark_value.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.mark_value.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "mark-type" or name == "mark-value"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "mark-type"):
                                        self.mark_type = value
                                        self.mark_type.value_namespace = name_space
                                        self.mark_type.value_namespace_prefix = name_space_prefix
                                    if(value_path == "mark-value"):
                                        self.mark_value = value
                                        self.mark_value.value_namespace = name_space
                                        self.mark_value.value_namespace_prefix = name_space_prefix


                            class Wred(Entity):
                                """
                                WRED parameters
                                
                                .. attribute:: config_max_threshold
                                
                                	Configured maximum threshold
                                	**type**\:   :py:class:`ConfigMaxThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.ConfigMaxThreshold>`
                                
                                .. attribute:: config_min_threshold
                                
                                	Configured minimum threshold
                                	**type**\:   :py:class:`ConfigMinThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.ConfigMinThreshold>`
                                
                                .. attribute:: first_segment
                                
                                	First segment
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: hardware_max_threshold_bytes
                                
                                	Hardware maximum threshold
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: hardware_min_threshold_bytes
                                
                                	Hardware minimum threshold
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: segment_size
                                
                                	Segment size
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: wred_match_type
                                
                                	WREDMatchType
                                	**type**\:   :py:class:`DnxQoseaShowWred <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowWred>`
                                
                                .. attribute:: wred_match_value
                                
                                	WRED match values
                                	**type**\:   :py:class:`WredMatchValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.WredMatchValue>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred, self).__init__()

                                    self.yang_name = "wred"
                                    self.yang_parent_name = "class"

                                    self.first_segment = YLeaf(YType.uint16, "first-segment")

                                    self.hardware_max_threshold_bytes = YLeaf(YType.uint32, "hardware-max-threshold-bytes")

                                    self.hardware_min_threshold_bytes = YLeaf(YType.uint32, "hardware-min-threshold-bytes")

                                    self.segment_size = YLeaf(YType.uint32, "segment-size")

                                    self.wred_match_type = YLeaf(YType.enumeration, "wred-match-type")

                                    self.config_max_threshold = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.ConfigMaxThreshold()
                                    self.config_max_threshold.parent = self
                                    self._children_name_map["config_max_threshold"] = "config-max-threshold"
                                    self._children_yang_names.add("config-max-threshold")

                                    self.config_min_threshold = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.ConfigMinThreshold()
                                    self.config_min_threshold.parent = self
                                    self._children_name_map["config_min_threshold"] = "config-min-threshold"
                                    self._children_yang_names.add("config-min-threshold")

                                    self.wred_match_value = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.WredMatchValue()
                                    self.wred_match_value.parent = self
                                    self._children_name_map["wred_match_value"] = "wred-match-value"
                                    self._children_yang_names.add("wred-match-value")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("first_segment",
                                                    "hardware_max_threshold_bytes",
                                                    "hardware_min_threshold_bytes",
                                                    "segment_size",
                                                    "wred_match_type") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred, self).__setattr__(name, value)


                                class WredMatchValue(Entity):
                                    """
                                    WRED match values
                                    
                                    .. attribute:: dnx_qosea_show_red_match_value
                                    
                                    	dnx qosea show red match value
                                    	**type**\: list of    :py:class:`DnxQoseaShowRedMatchValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.WredMatchValue.DnxQoseaShowRedMatchValue>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.WredMatchValue, self).__init__()

                                        self.yang_name = "wred-match-value"
                                        self.yang_parent_name = "wred"

                                        self.dnx_qosea_show_red_match_value = YList(self)

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
                                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.WredMatchValue, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.WredMatchValue, self).__setattr__(name, value)


                                    class DnxQoseaShowRedMatchValue(Entity):
                                        """
                                        dnx qosea show red match value
                                        
                                        .. attribute:: range_end
                                        
                                        	End value of a range
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: range_start
                                        
                                        	Start value of a range
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.WredMatchValue.DnxQoseaShowRedMatchValue, self).__init__()

                                            self.yang_name = "dnx-qosea-show-red-match-value"
                                            self.yang_parent_name = "wred-match-value"

                                            self.range_end = YLeaf(YType.uint8, "range-end")

                                            self.range_start = YLeaf(YType.uint8, "range-start")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("range_end",
                                                            "range_start") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.WredMatchValue.DnxQoseaShowRedMatchValue, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.WredMatchValue.DnxQoseaShowRedMatchValue, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.range_end.is_set or
                                                self.range_start.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.range_end.yfilter != YFilter.not_set or
                                                self.range_start.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "dnx-qosea-show-red-match-value" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.range_end.is_set or self.range_end.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.range_end.get_name_leafdata())
                                            if (self.range_start.is_set or self.range_start.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.range_start.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "range-end" or name == "range-start"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "range-end"):
                                                self.range_end = value
                                                self.range_end.value_namespace = name_space
                                                self.range_end.value_namespace_prefix = name_space_prefix
                                            if(value_path == "range-start"):
                                                self.range_start = value
                                                self.range_start.value_namespace = name_space
                                                self.range_start.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        for c in self.dnx_qosea_show_red_match_value:
                                            if (c.has_data()):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for c in self.dnx_qosea_show_red_match_value:
                                            if (c.has_operation()):
                                                return True
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "wred-match-value" + path_buffer

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

                                        if (child_yang_name == "dnx-qosea-show-red-match-value"):
                                            for c in self.dnx_qosea_show_red_match_value:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.WredMatchValue.DnxQoseaShowRedMatchValue()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.dnx_qosea_show_red_match_value.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "dnx-qosea-show-red-match-value"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass


                                class ConfigMinThreshold(Entity):
                                    """
                                    Configured minimum threshold
                                    
                                    .. attribute:: policy_unit
                                    
                                    	Policy unit
                                    	**type**\:   :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                    
                                    .. attribute:: policy_value
                                    
                                    	Policy value
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.ConfigMinThreshold, self).__init__()

                                        self.yang_name = "config-min-threshold"
                                        self.yang_parent_name = "wred"

                                        self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                        self.policy_value = YLeaf(YType.uint32, "policy-value")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("policy_unit",
                                                        "policy_value") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.ConfigMinThreshold, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.ConfigMinThreshold, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.policy_unit.is_set or
                                            self.policy_value.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.policy_unit.yfilter != YFilter.not_set or
                                            self.policy_value.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "config-min-threshold" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.policy_unit.is_set or self.policy_unit.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.policy_unit.get_name_leafdata())
                                        if (self.policy_value.is_set or self.policy_value.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.policy_value.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "policy-unit" or name == "policy-value"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "policy-unit"):
                                            self.policy_unit = value
                                            self.policy_unit.value_namespace = name_space
                                            self.policy_unit.value_namespace_prefix = name_space_prefix
                                        if(value_path == "policy-value"):
                                            self.policy_value = value
                                            self.policy_value.value_namespace = name_space
                                            self.policy_value.value_namespace_prefix = name_space_prefix


                                class ConfigMaxThreshold(Entity):
                                    """
                                    Configured maximum threshold
                                    
                                    .. attribute:: policy_unit
                                    
                                    	Policy unit
                                    	**type**\:   :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                    
                                    .. attribute:: policy_value
                                    
                                    	Policy value
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.ConfigMaxThreshold, self).__init__()

                                        self.yang_name = "config-max-threshold"
                                        self.yang_parent_name = "wred"

                                        self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                        self.policy_value = YLeaf(YType.uint32, "policy-value")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("policy_unit",
                                                        "policy_value") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.ConfigMaxThreshold, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.ConfigMaxThreshold, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.policy_unit.is_set or
                                            self.policy_value.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.policy_unit.yfilter != YFilter.not_set or
                                            self.policy_value.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "config-max-threshold" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.policy_unit.is_set or self.policy_unit.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.policy_unit.get_name_leafdata())
                                        if (self.policy_value.is_set or self.policy_value.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.policy_value.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "policy-unit" or name == "policy-value"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "policy-unit"):
                                            self.policy_unit = value
                                            self.policy_unit.value_namespace = name_space
                                            self.policy_unit.value_namespace_prefix = name_space_prefix
                                        if(value_path == "policy-value"):
                                            self.policy_value = value
                                            self.policy_value.value_namespace = name_space
                                            self.policy_value.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    return (
                                        self.first_segment.is_set or
                                        self.hardware_max_threshold_bytes.is_set or
                                        self.hardware_min_threshold_bytes.is_set or
                                        self.segment_size.is_set or
                                        self.wred_match_type.is_set or
                                        (self.config_max_threshold is not None and self.config_max_threshold.has_data()) or
                                        (self.config_min_threshold is not None and self.config_min_threshold.has_data()) or
                                        (self.wred_match_value is not None and self.wred_match_value.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.first_segment.yfilter != YFilter.not_set or
                                        self.hardware_max_threshold_bytes.yfilter != YFilter.not_set or
                                        self.hardware_min_threshold_bytes.yfilter != YFilter.not_set or
                                        self.segment_size.yfilter != YFilter.not_set or
                                        self.wred_match_type.yfilter != YFilter.not_set or
                                        (self.config_max_threshold is not None and self.config_max_threshold.has_operation()) or
                                        (self.config_min_threshold is not None and self.config_min_threshold.has_operation()) or
                                        (self.wred_match_value is not None and self.wred_match_value.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "wred" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.first_segment.is_set or self.first_segment.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.first_segment.get_name_leafdata())
                                    if (self.hardware_max_threshold_bytes.is_set or self.hardware_max_threshold_bytes.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.hardware_max_threshold_bytes.get_name_leafdata())
                                    if (self.hardware_min_threshold_bytes.is_set or self.hardware_min_threshold_bytes.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.hardware_min_threshold_bytes.get_name_leafdata())
                                    if (self.segment_size.is_set or self.segment_size.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.segment_size.get_name_leafdata())
                                    if (self.wred_match_type.is_set or self.wred_match_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.wred_match_type.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "config-max-threshold"):
                                        if (self.config_max_threshold is None):
                                            self.config_max_threshold = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.ConfigMaxThreshold()
                                            self.config_max_threshold.parent = self
                                            self._children_name_map["config_max_threshold"] = "config-max-threshold"
                                        return self.config_max_threshold

                                    if (child_yang_name == "config-min-threshold"):
                                        if (self.config_min_threshold is None):
                                            self.config_min_threshold = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.ConfigMinThreshold()
                                            self.config_min_threshold.parent = self
                                            self._children_name_map["config_min_threshold"] = "config-min-threshold"
                                        return self.config_min_threshold

                                    if (child_yang_name == "wred-match-value"):
                                        if (self.wred_match_value is None):
                                            self.wred_match_value = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.WredMatchValue()
                                            self.wred_match_value.parent = self
                                            self._children_name_map["wred_match_value"] = "wred-match-value"
                                        return self.wred_match_value

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "config-max-threshold" or name == "config-min-threshold" or name == "wred-match-value" or name == "first-segment" or name == "hardware-max-threshold-bytes" or name == "hardware-min-threshold-bytes" or name == "segment-size" or name == "wred-match-type"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "first-segment"):
                                        self.first_segment = value
                                        self.first_segment.value_namespace = name_space
                                        self.first_segment.value_namespace_prefix = name_space_prefix
                                    if(value_path == "hardware-max-threshold-bytes"):
                                        self.hardware_max_threshold_bytes = value
                                        self.hardware_max_threshold_bytes.value_namespace = name_space
                                        self.hardware_max_threshold_bytes.value_namespace_prefix = name_space_prefix
                                    if(value_path == "hardware-min-threshold-bytes"):
                                        self.hardware_min_threshold_bytes = value
                                        self.hardware_min_threshold_bytes.value_namespace = name_space
                                        self.hardware_min_threshold_bytes.value_namespace_prefix = name_space_prefix
                                    if(value_path == "segment-size"):
                                        self.segment_size = value
                                        self.segment_size.value_namespace = name_space
                                        self.segment_size.value_namespace_prefix = name_space_prefix
                                    if(value_path == "wred-match-type"):
                                        self.wred_match_type = value
                                        self.wred_match_type.value_namespace = name_space
                                        self.wred_match_type.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.common_mark:
                                    if (c.has_data()):
                                        return True
                                for c in self.ip_mark:
                                    if (c.has_data()):
                                        return True
                                for c in self.mpls_mark:
                                    if (c.has_data()):
                                        return True
                                for c in self.wred:
                                    if (c.has_data()):
                                        return True
                                return (
                                    self.level_one_class_name.is_set or
                                    self.class_level.is_set or
                                    self.config_excess_bandwidth_percent.is_set or
                                    self.config_excess_bandwidth_unit.is_set or
                                    self.egress_queue_id.is_set or
                                    self.hardware_excess_bandwidth_weight.is_set or
                                    self.hardware_max_rate_kbps.is_set or
                                    self.hardware_min_rate_kbps.is_set or
                                    self.hardware_policer_average_rate_kbps.is_set or
                                    self.hardware_policer_conform_burst_bytes.is_set or
                                    self.hardware_policer_excess_burst_bytes.is_set or
                                    self.hardware_policer_peak_rate_kbps.is_set or
                                    self.hardware_queue_limit_bytes.is_set or
                                    self.hardware_queue_limit_microseconds.is_set or
                                    self.level_two_class_name.is_set or
                                    self.network_min_bandwidth_kbps.is_set or
                                    self.policer_bucket_id.is_set or
                                    self.policer_stats_handle.is_set or
                                    self.priority_level.is_set or
                                    self.queue_type.is_set or
                                    (self.config_max_rate is not None and self.config_max_rate.has_data()) or
                                    (self.config_min_rate is not None and self.config_min_rate.has_data()) or
                                    (self.config_policer_average_rate is not None and self.config_policer_average_rate.has_data()) or
                                    (self.config_policer_conform_burst is not None and self.config_policer_conform_burst.has_data()) or
                                    (self.config_policer_excess_burst is not None and self.config_policer_excess_burst.has_data()) or
                                    (self.config_policer_peak_rate is not None and self.config_policer_peak_rate.has_data()) or
                                    (self.config_queue_limit is not None and self.config_queue_limit.has_data()) or
                                    (self.conform_action is not None and self.conform_action.has_data()) or
                                    (self.exceed_action is not None and self.exceed_action.has_data()) or
                                    (self.violate_action is not None and self.violate_action.has_data()))

                            def has_operation(self):
                                for c in self.common_mark:
                                    if (c.has_operation()):
                                        return True
                                for c in self.ip_mark:
                                    if (c.has_operation()):
                                        return True
                                for c in self.mpls_mark:
                                    if (c.has_operation()):
                                        return True
                                for c in self.wred:
                                    if (c.has_operation()):
                                        return True
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.level_one_class_name.yfilter != YFilter.not_set or
                                    self.class_level.yfilter != YFilter.not_set or
                                    self.config_excess_bandwidth_percent.yfilter != YFilter.not_set or
                                    self.config_excess_bandwidth_unit.yfilter != YFilter.not_set or
                                    self.egress_queue_id.yfilter != YFilter.not_set or
                                    self.hardware_excess_bandwidth_weight.yfilter != YFilter.not_set or
                                    self.hardware_max_rate_kbps.yfilter != YFilter.not_set or
                                    self.hardware_min_rate_kbps.yfilter != YFilter.not_set or
                                    self.hardware_policer_average_rate_kbps.yfilter != YFilter.not_set or
                                    self.hardware_policer_conform_burst_bytes.yfilter != YFilter.not_set or
                                    self.hardware_policer_excess_burst_bytes.yfilter != YFilter.not_set or
                                    self.hardware_policer_peak_rate_kbps.yfilter != YFilter.not_set or
                                    self.hardware_queue_limit_bytes.yfilter != YFilter.not_set or
                                    self.hardware_queue_limit_microseconds.yfilter != YFilter.not_set or
                                    self.level_two_class_name.yfilter != YFilter.not_set or
                                    self.network_min_bandwidth_kbps.yfilter != YFilter.not_set or
                                    self.policer_bucket_id.yfilter != YFilter.not_set or
                                    self.policer_stats_handle.yfilter != YFilter.not_set or
                                    self.priority_level.yfilter != YFilter.not_set or
                                    self.queue_type.yfilter != YFilter.not_set or
                                    (self.config_max_rate is not None and self.config_max_rate.has_operation()) or
                                    (self.config_min_rate is not None and self.config_min_rate.has_operation()) or
                                    (self.config_policer_average_rate is not None and self.config_policer_average_rate.has_operation()) or
                                    (self.config_policer_conform_burst is not None and self.config_policer_conform_burst.has_operation()) or
                                    (self.config_policer_excess_burst is not None and self.config_policer_excess_burst.has_operation()) or
                                    (self.config_policer_peak_rate is not None and self.config_policer_peak_rate.has_operation()) or
                                    (self.config_queue_limit is not None and self.config_queue_limit.has_operation()) or
                                    (self.conform_action is not None and self.conform_action.has_operation()) or
                                    (self.exceed_action is not None and self.exceed_action.has_operation()) or
                                    (self.violate_action is not None and self.violate_action.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "class" + "[level-one-class-name='" + self.level_one_class_name.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.level_one_class_name.is_set or self.level_one_class_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.level_one_class_name.get_name_leafdata())
                                if (self.class_level.is_set or self.class_level.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.class_level.get_name_leafdata())
                                if (self.config_excess_bandwidth_percent.is_set or self.config_excess_bandwidth_percent.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.config_excess_bandwidth_percent.get_name_leafdata())
                                if (self.config_excess_bandwidth_unit.is_set or self.config_excess_bandwidth_unit.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.config_excess_bandwidth_unit.get_name_leafdata())
                                if (self.egress_queue_id.is_set or self.egress_queue_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.egress_queue_id.get_name_leafdata())
                                if (self.hardware_excess_bandwidth_weight.is_set or self.hardware_excess_bandwidth_weight.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.hardware_excess_bandwidth_weight.get_name_leafdata())
                                if (self.hardware_max_rate_kbps.is_set or self.hardware_max_rate_kbps.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.hardware_max_rate_kbps.get_name_leafdata())
                                if (self.hardware_min_rate_kbps.is_set or self.hardware_min_rate_kbps.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.hardware_min_rate_kbps.get_name_leafdata())
                                if (self.hardware_policer_average_rate_kbps.is_set or self.hardware_policer_average_rate_kbps.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.hardware_policer_average_rate_kbps.get_name_leafdata())
                                if (self.hardware_policer_conform_burst_bytes.is_set or self.hardware_policer_conform_burst_bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.hardware_policer_conform_burst_bytes.get_name_leafdata())
                                if (self.hardware_policer_excess_burst_bytes.is_set or self.hardware_policer_excess_burst_bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.hardware_policer_excess_burst_bytes.get_name_leafdata())
                                if (self.hardware_policer_peak_rate_kbps.is_set or self.hardware_policer_peak_rate_kbps.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.hardware_policer_peak_rate_kbps.get_name_leafdata())
                                if (self.hardware_queue_limit_bytes.is_set or self.hardware_queue_limit_bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.hardware_queue_limit_bytes.get_name_leafdata())
                                if (self.hardware_queue_limit_microseconds.is_set or self.hardware_queue_limit_microseconds.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.hardware_queue_limit_microseconds.get_name_leafdata())
                                if (self.level_two_class_name.is_set or self.level_two_class_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.level_two_class_name.get_name_leafdata())
                                if (self.network_min_bandwidth_kbps.is_set or self.network_min_bandwidth_kbps.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.network_min_bandwidth_kbps.get_name_leafdata())
                                if (self.policer_bucket_id.is_set or self.policer_bucket_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.policer_bucket_id.get_name_leafdata())
                                if (self.policer_stats_handle.is_set or self.policer_stats_handle.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.policer_stats_handle.get_name_leafdata())
                                if (self.priority_level.is_set or self.priority_level.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.priority_level.get_name_leafdata())
                                if (self.queue_type.is_set or self.queue_type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.queue_type.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "common-mark"):
                                    for c in self.common_mark:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.CommonMark()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.common_mark.append(c)
                                    return c

                                if (child_yang_name == "config-max-rate"):
                                    if (self.config_max_rate is None):
                                        self.config_max_rate = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigMaxRate()
                                        self.config_max_rate.parent = self
                                        self._children_name_map["config_max_rate"] = "config-max-rate"
                                    return self.config_max_rate

                                if (child_yang_name == "config-min-rate"):
                                    if (self.config_min_rate is None):
                                        self.config_min_rate = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigMinRate()
                                        self.config_min_rate.parent = self
                                        self._children_name_map["config_min_rate"] = "config-min-rate"
                                    return self.config_min_rate

                                if (child_yang_name == "config-policer-average-rate"):
                                    if (self.config_policer_average_rate is None):
                                        self.config_policer_average_rate = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerAverageRate()
                                        self.config_policer_average_rate.parent = self
                                        self._children_name_map["config_policer_average_rate"] = "config-policer-average-rate"
                                    return self.config_policer_average_rate

                                if (child_yang_name == "config-policer-conform-burst"):
                                    if (self.config_policer_conform_burst is None):
                                        self.config_policer_conform_burst = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerConformBurst()
                                        self.config_policer_conform_burst.parent = self
                                        self._children_name_map["config_policer_conform_burst"] = "config-policer-conform-burst"
                                    return self.config_policer_conform_burst

                                if (child_yang_name == "config-policer-excess-burst"):
                                    if (self.config_policer_excess_burst is None):
                                        self.config_policer_excess_burst = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerExcessBurst()
                                        self.config_policer_excess_burst.parent = self
                                        self._children_name_map["config_policer_excess_burst"] = "config-policer-excess-burst"
                                    return self.config_policer_excess_burst

                                if (child_yang_name == "config-policer-peak-rate"):
                                    if (self.config_policer_peak_rate is None):
                                        self.config_policer_peak_rate = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerPeakRate()
                                        self.config_policer_peak_rate.parent = self
                                        self._children_name_map["config_policer_peak_rate"] = "config-policer-peak-rate"
                                    return self.config_policer_peak_rate

                                if (child_yang_name == "config-queue-limit"):
                                    if (self.config_queue_limit is None):
                                        self.config_queue_limit = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigQueueLimit()
                                        self.config_queue_limit.parent = self
                                        self._children_name_map["config_queue_limit"] = "config-queue-limit"
                                    return self.config_queue_limit

                                if (child_yang_name == "conform-action"):
                                    if (self.conform_action is None):
                                        self.conform_action = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConformAction()
                                        self.conform_action.parent = self
                                        self._children_name_map["conform_action"] = "conform-action"
                                    return self.conform_action

                                if (child_yang_name == "exceed-action"):
                                    if (self.exceed_action is None):
                                        self.exceed_action = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ExceedAction()
                                        self.exceed_action.parent = self
                                        self._children_name_map["exceed_action"] = "exceed-action"
                                    return self.exceed_action

                                if (child_yang_name == "ip-mark"):
                                    for c in self.ip_mark:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.IpMark()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.ip_mark.append(c)
                                    return c

                                if (child_yang_name == "mpls-mark"):
                                    for c in self.mpls_mark:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.MplsMark()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.mpls_mark.append(c)
                                    return c

                                if (child_yang_name == "violate-action"):
                                    if (self.violate_action is None):
                                        self.violate_action = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ViolateAction()
                                        self.violate_action.parent = self
                                        self._children_name_map["violate_action"] = "violate-action"
                                    return self.violate_action

                                if (child_yang_name == "wred"):
                                    for c in self.wred:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.wred.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "common-mark" or name == "config-max-rate" or name == "config-min-rate" or name == "config-policer-average-rate" or name == "config-policer-conform-burst" or name == "config-policer-excess-burst" or name == "config-policer-peak-rate" or name == "config-queue-limit" or name == "conform-action" or name == "exceed-action" or name == "ip-mark" or name == "mpls-mark" or name == "violate-action" or name == "wred" or name == "level-one-class-name" or name == "class-level" or name == "config-excess-bandwidth-percent" or name == "config-excess-bandwidth-unit" or name == "egress-queue-id" or name == "hardware-excess-bandwidth-weight" or name == "hardware-max-rate-kbps" or name == "hardware-min-rate-kbps" or name == "hardware-policer-average-rate-kbps" or name == "hardware-policer-conform-burst-bytes" or name == "hardware-policer-excess-burst-bytes" or name == "hardware-policer-peak-rate-kbps" or name == "hardware-queue-limit-bytes" or name == "hardware-queue-limit-microseconds" or name == "level-two-class-name" or name == "network-min-bandwidth-kbps" or name == "policer-bucket-id" or name == "policer-stats-handle" or name == "priority-level" or name == "queue-type"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "level-one-class-name"):
                                    self.level_one_class_name = value
                                    self.level_one_class_name.value_namespace = name_space
                                    self.level_one_class_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "class-level"):
                                    self.class_level = value
                                    self.class_level.value_namespace = name_space
                                    self.class_level.value_namespace_prefix = name_space_prefix
                                if(value_path == "config-excess-bandwidth-percent"):
                                    self.config_excess_bandwidth_percent = value
                                    self.config_excess_bandwidth_percent.value_namespace = name_space
                                    self.config_excess_bandwidth_percent.value_namespace_prefix = name_space_prefix
                                if(value_path == "config-excess-bandwidth-unit"):
                                    self.config_excess_bandwidth_unit = value
                                    self.config_excess_bandwidth_unit.value_namespace = name_space
                                    self.config_excess_bandwidth_unit.value_namespace_prefix = name_space_prefix
                                if(value_path == "egress-queue-id"):
                                    self.egress_queue_id = value
                                    self.egress_queue_id.value_namespace = name_space
                                    self.egress_queue_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "hardware-excess-bandwidth-weight"):
                                    self.hardware_excess_bandwidth_weight = value
                                    self.hardware_excess_bandwidth_weight.value_namespace = name_space
                                    self.hardware_excess_bandwidth_weight.value_namespace_prefix = name_space_prefix
                                if(value_path == "hardware-max-rate-kbps"):
                                    self.hardware_max_rate_kbps = value
                                    self.hardware_max_rate_kbps.value_namespace = name_space
                                    self.hardware_max_rate_kbps.value_namespace_prefix = name_space_prefix
                                if(value_path == "hardware-min-rate-kbps"):
                                    self.hardware_min_rate_kbps = value
                                    self.hardware_min_rate_kbps.value_namespace = name_space
                                    self.hardware_min_rate_kbps.value_namespace_prefix = name_space_prefix
                                if(value_path == "hardware-policer-average-rate-kbps"):
                                    self.hardware_policer_average_rate_kbps = value
                                    self.hardware_policer_average_rate_kbps.value_namespace = name_space
                                    self.hardware_policer_average_rate_kbps.value_namespace_prefix = name_space_prefix
                                if(value_path == "hardware-policer-conform-burst-bytes"):
                                    self.hardware_policer_conform_burst_bytes = value
                                    self.hardware_policer_conform_burst_bytes.value_namespace = name_space
                                    self.hardware_policer_conform_burst_bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "hardware-policer-excess-burst-bytes"):
                                    self.hardware_policer_excess_burst_bytes = value
                                    self.hardware_policer_excess_burst_bytes.value_namespace = name_space
                                    self.hardware_policer_excess_burst_bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "hardware-policer-peak-rate-kbps"):
                                    self.hardware_policer_peak_rate_kbps = value
                                    self.hardware_policer_peak_rate_kbps.value_namespace = name_space
                                    self.hardware_policer_peak_rate_kbps.value_namespace_prefix = name_space_prefix
                                if(value_path == "hardware-queue-limit-bytes"):
                                    self.hardware_queue_limit_bytes = value
                                    self.hardware_queue_limit_bytes.value_namespace = name_space
                                    self.hardware_queue_limit_bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "hardware-queue-limit-microseconds"):
                                    self.hardware_queue_limit_microseconds = value
                                    self.hardware_queue_limit_microseconds.value_namespace = name_space
                                    self.hardware_queue_limit_microseconds.value_namespace_prefix = name_space_prefix
                                if(value_path == "level-two-class-name"):
                                    self.level_two_class_name = value
                                    self.level_two_class_name.value_namespace = name_space
                                    self.level_two_class_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "network-min-bandwidth-kbps"):
                                    self.network_min_bandwidth_kbps = value
                                    self.network_min_bandwidth_kbps.value_namespace = name_space
                                    self.network_min_bandwidth_kbps.value_namespace_prefix = name_space_prefix
                                if(value_path == "policer-bucket-id"):
                                    self.policer_bucket_id = value
                                    self.policer_bucket_id.value_namespace = name_space
                                    self.policer_bucket_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "policer-stats-handle"):
                                    self.policer_stats_handle = value
                                    self.policer_stats_handle.value_namespace = name_space
                                    self.policer_stats_handle.value_namespace_prefix = name_space_prefix
                                if(value_path == "priority-level"):
                                    self.priority_level = value
                                    self.priority_level.value_namespace = name_space
                                    self.priority_level.value_namespace_prefix = name_space_prefix
                                if(value_path == "queue-type"):
                                    self.queue_type = value
                                    self.queue_type.value_namespace = name_space
                                    self.queue_type.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.class_:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.class_:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "classes" + path_buffer

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

                            if (child_yang_name == "class"):
                                for c in self.class_:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.class_.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "class"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.interface_name.is_set or
                            self.qos_direction.is_set or
                            (self.classes is not None and self.classes.has_data()) or
                            (self.policy_details is not None and self.policy_details.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.qos_direction.yfilter != YFilter.not_set or
                            (self.classes is not None and self.classes.has_operation()) or
                            (self.policy_details is not None and self.policy_details.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

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
                        if (self.qos_direction.is_set or self.qos_direction.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.qos_direction.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "classes"):
                            if (self.classes is None):
                                self.classes = PlatformQos.Nodes.Node.Interfaces.Interface.Classes()
                                self.classes.parent = self
                                self._children_name_map["classes"] = "classes"
                            return self.classes

                        if (child_yang_name == "policy-details"):
                            if (self.policy_details is None):
                                self.policy_details = PlatformQos.Nodes.Node.Interfaces.Interface.PolicyDetails()
                                self.policy_details.parent = self
                                self._children_name_map["policy_details"] = "policy-details"
                            return self.policy_details

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "classes" or name == "policy-details" or name == "interface-name" or name == "qos-direction"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "qos-direction"):
                            self.qos_direction = value
                            self.qos_direction.value_namespace = name_space
                            self.qos_direction.value_namespace_prefix = name_space_prefix

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
                        c = PlatformQos.Nodes.Node.Interfaces.Interface()
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


            class RemoteInterfaces(Entity):
                """
                QoS list of remote interfaces
                
                .. attribute:: remote_interface
                
                	QoS remote interface names
                	**type**\: list of    :py:class:`RemoteInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface>`
                
                

                """

                _prefix = 'ncs5500-qos-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PlatformQos.Nodes.Node.RemoteInterfaces, self).__init__()

                    self.yang_name = "remote-interfaces"
                    self.yang_parent_name = "node"

                    self.remote_interface = YList(self)

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
                                super(PlatformQos.Nodes.Node.RemoteInterfaces, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PlatformQos.Nodes.Node.RemoteInterfaces, self).__setattr__(name, value)


                class RemoteInterface(Entity):
                    """
                    QoS remote interface names
                    
                    .. attribute:: interface_name  <key>
                    
                    	The name of the remote interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: interface_handle
                    
                    	Interface Handle
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_classes
                    
                    	Number of Classes
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_virtual_output_queues
                    
                    	Number of Virtual Output Queues
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: policy_name
                    
                    	Policy Name
                    	**type**\:  str
                    
                    	**length:** 0..64
                    
                    .. attribute:: remote_class
                    
                    	Remote Class array
                    	**type**\: list of    :py:class:`RemoteClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass>`
                    
                    .. attribute:: virtual_output_queue_statistics_handle
                    
                    	Virtual output queue statistics handle
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'ncs5500-qos-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface, self).__init__()

                        self.yang_name = "remote-interface"
                        self.yang_parent_name = "remote-interfaces"

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.interface_handle = YLeaf(YType.uint32, "interface-handle")

                        self.number_of_classes = YLeaf(YType.uint32, "number-of-classes")

                        self.number_of_virtual_output_queues = YLeaf(YType.uint32, "number-of-virtual-output-queues")

                        self.policy_name = YLeaf(YType.str, "policy-name")

                        self.virtual_output_queue_statistics_handle = YLeaf(YType.uint64, "virtual-output-queue-statistics-handle")

                        self.remote_class = YList(self)

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
                                        "interface_handle",
                                        "number_of_classes",
                                        "number_of_virtual_output_queues",
                                        "policy_name",
                                        "virtual_output_queue_statistics_handle") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface, self).__setattr__(name, value)


                    class RemoteClass(Entity):
                        """
                        Remote Class array
                        
                        .. attribute:: class_id
                        
                        	Class ID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: class_name
                        
                        	Class Name
                        	**type**\:  str
                        
                        	**length:** 0..64
                        
                        .. attribute:: cos_q
                        
                        	Class of Service Queue
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hardware_queue_limit
                        
                        	Hardware queue limit in bytes
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: byte
                        
                        .. attribute:: hw_wred
                        
                        	Hardware WRED profiles
                        	**type**\: list of    :py:class:`HwWred <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass.HwWred>`
                        
                        .. attribute:: queue_limit
                        
                        	Default/Configured queue limit in bytes
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: byte
                        
                        .. attribute:: wred
                        
                        	Default/Configured WRED profiles
                        	**type**\: list of    :py:class:`Wred <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass.Wred>`
                        
                        

                        """

                        _prefix = 'ncs5500-qos-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass, self).__init__()

                            self.yang_name = "remote-class"
                            self.yang_parent_name = "remote-interface"

                            self.class_id = YLeaf(YType.uint32, "class-id")

                            self.class_name = YLeaf(YType.str, "class-name")

                            self.cos_q = YLeaf(YType.uint32, "cos-q")

                            self.hardware_queue_limit = YLeaf(YType.uint32, "hardware-queue-limit")

                            self.queue_limit = YLeaf(YType.uint32, "queue-limit")

                            self.hw_wred = YList(self)
                            self.wred = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("class_id",
                                            "class_name",
                                            "cos_q",
                                            "hardware_queue_limit",
                                            "queue_limit") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass, self).__setattr__(name, value)


                        class Wred(Entity):
                            """
                            Default/Configured WRED profiles
                            
                            .. attribute:: drop_probability
                            
                            	Drop Probability
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: max_threshold
                            
                            	Maximum Threshold
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: min_threshold
                            
                            	Minimum Threshold
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ncs5500-qos-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass.Wred, self).__init__()

                                self.yang_name = "wred"
                                self.yang_parent_name = "remote-class"

                                self.drop_probability = YLeaf(YType.uint32, "drop-probability")

                                self.max_threshold = YLeaf(YType.uint32, "max-threshold")

                                self.min_threshold = YLeaf(YType.uint32, "min-threshold")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("drop_probability",
                                                "max_threshold",
                                                "min_threshold") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass.Wred, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass.Wred, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.drop_probability.is_set or
                                    self.max_threshold.is_set or
                                    self.min_threshold.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.drop_probability.yfilter != YFilter.not_set or
                                    self.max_threshold.yfilter != YFilter.not_set or
                                    self.min_threshold.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "wred" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.drop_probability.is_set or self.drop_probability.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.drop_probability.get_name_leafdata())
                                if (self.max_threshold.is_set or self.max_threshold.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.max_threshold.get_name_leafdata())
                                if (self.min_threshold.is_set or self.min_threshold.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.min_threshold.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "drop-probability" or name == "max-threshold" or name == "min-threshold"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "drop-probability"):
                                    self.drop_probability = value
                                    self.drop_probability.value_namespace = name_space
                                    self.drop_probability.value_namespace_prefix = name_space_prefix
                                if(value_path == "max-threshold"):
                                    self.max_threshold = value
                                    self.max_threshold.value_namespace = name_space
                                    self.max_threshold.value_namespace_prefix = name_space_prefix
                                if(value_path == "min-threshold"):
                                    self.min_threshold = value
                                    self.min_threshold.value_namespace = name_space
                                    self.min_threshold.value_namespace_prefix = name_space_prefix


                        class HwWred(Entity):
                            """
                            Hardware WRED profiles
                            
                            .. attribute:: drop_probability
                            
                            	Drop Probability
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: max_threshold
                            
                            	Maximum Threshold
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: min_threshold
                            
                            	Minimum Threshold
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ncs5500-qos-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass.HwWred, self).__init__()

                                self.yang_name = "hw-wred"
                                self.yang_parent_name = "remote-class"

                                self.drop_probability = YLeaf(YType.uint32, "drop-probability")

                                self.max_threshold = YLeaf(YType.uint32, "max-threshold")

                                self.min_threshold = YLeaf(YType.uint32, "min-threshold")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("drop_probability",
                                                "max_threshold",
                                                "min_threshold") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass.HwWred, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass.HwWred, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.drop_probability.is_set or
                                    self.max_threshold.is_set or
                                    self.min_threshold.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.drop_probability.yfilter != YFilter.not_set or
                                    self.max_threshold.yfilter != YFilter.not_set or
                                    self.min_threshold.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "hw-wred" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.drop_probability.is_set or self.drop_probability.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.drop_probability.get_name_leafdata())
                                if (self.max_threshold.is_set or self.max_threshold.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.max_threshold.get_name_leafdata())
                                if (self.min_threshold.is_set or self.min_threshold.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.min_threshold.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "drop-probability" or name == "max-threshold" or name == "min-threshold"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "drop-probability"):
                                    self.drop_probability = value
                                    self.drop_probability.value_namespace = name_space
                                    self.drop_probability.value_namespace_prefix = name_space_prefix
                                if(value_path == "max-threshold"):
                                    self.max_threshold = value
                                    self.max_threshold.value_namespace = name_space
                                    self.max_threshold.value_namespace_prefix = name_space_prefix
                                if(value_path == "min-threshold"):
                                    self.min_threshold = value
                                    self.min_threshold.value_namespace = name_space
                                    self.min_threshold.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.hw_wred:
                                if (c.has_data()):
                                    return True
                            for c in self.wred:
                                if (c.has_data()):
                                    return True
                            return (
                                self.class_id.is_set or
                                self.class_name.is_set or
                                self.cos_q.is_set or
                                self.hardware_queue_limit.is_set or
                                self.queue_limit.is_set)

                        def has_operation(self):
                            for c in self.hw_wred:
                                if (c.has_operation()):
                                    return True
                            for c in self.wred:
                                if (c.has_operation()):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.class_id.yfilter != YFilter.not_set or
                                self.class_name.yfilter != YFilter.not_set or
                                self.cos_q.yfilter != YFilter.not_set or
                                self.hardware_queue_limit.yfilter != YFilter.not_set or
                                self.queue_limit.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "remote-class" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.class_id.is_set or self.class_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.class_id.get_name_leafdata())
                            if (self.class_name.is_set or self.class_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.class_name.get_name_leafdata())
                            if (self.cos_q.is_set or self.cos_q.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.cos_q.get_name_leafdata())
                            if (self.hardware_queue_limit.is_set or self.hardware_queue_limit.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.hardware_queue_limit.get_name_leafdata())
                            if (self.queue_limit.is_set or self.queue_limit.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.queue_limit.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "hw-wred"):
                                for c in self.hw_wred:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass.HwWred()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.hw_wred.append(c)
                                return c

                            if (child_yang_name == "wred"):
                                for c in self.wred:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass.Wred()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.wred.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "hw-wred" or name == "wred" or name == "class-id" or name == "class-name" or name == "cos-q" or name == "hardware-queue-limit" or name == "queue-limit"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "class-id"):
                                self.class_id = value
                                self.class_id.value_namespace = name_space
                                self.class_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "class-name"):
                                self.class_name = value
                                self.class_name.value_namespace = name_space
                                self.class_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "cos-q"):
                                self.cos_q = value
                                self.cos_q.value_namespace = name_space
                                self.cos_q.value_namespace_prefix = name_space_prefix
                            if(value_path == "hardware-queue-limit"):
                                self.hardware_queue_limit = value
                                self.hardware_queue_limit.value_namespace = name_space
                                self.hardware_queue_limit.value_namespace_prefix = name_space_prefix
                            if(value_path == "queue-limit"):
                                self.queue_limit = value
                                self.queue_limit.value_namespace = name_space
                                self.queue_limit.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.remote_class:
                            if (c.has_data()):
                                return True
                        return (
                            self.interface_name.is_set or
                            self.interface_handle.is_set or
                            self.number_of_classes.is_set or
                            self.number_of_virtual_output_queues.is_set or
                            self.policy_name.is_set or
                            self.virtual_output_queue_statistics_handle.is_set)

                    def has_operation(self):
                        for c in self.remote_class:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.interface_handle.yfilter != YFilter.not_set or
                            self.number_of_classes.yfilter != YFilter.not_set or
                            self.number_of_virtual_output_queues.yfilter != YFilter.not_set or
                            self.policy_name.yfilter != YFilter.not_set or
                            self.virtual_output_queue_statistics_handle.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "remote-interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

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
                        if (self.interface_handle.is_set or self.interface_handle.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_handle.get_name_leafdata())
                        if (self.number_of_classes.is_set or self.number_of_classes.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.number_of_classes.get_name_leafdata())
                        if (self.number_of_virtual_output_queues.is_set or self.number_of_virtual_output_queues.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.number_of_virtual_output_queues.get_name_leafdata())
                        if (self.policy_name.is_set or self.policy_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.policy_name.get_name_leafdata())
                        if (self.virtual_output_queue_statistics_handle.is_set or self.virtual_output_queue_statistics_handle.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.virtual_output_queue_statistics_handle.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "remote-class"):
                            for c in self.remote_class:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.remote_class.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "remote-class" or name == "interface-name" or name == "interface-handle" or name == "number-of-classes" or name == "number-of-virtual-output-queues" or name == "policy-name" or name == "virtual-output-queue-statistics-handle"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-handle"):
                            self.interface_handle = value
                            self.interface_handle.value_namespace = name_space
                            self.interface_handle.value_namespace_prefix = name_space_prefix
                        if(value_path == "number-of-classes"):
                            self.number_of_classes = value
                            self.number_of_classes.value_namespace = name_space
                            self.number_of_classes.value_namespace_prefix = name_space_prefix
                        if(value_path == "number-of-virtual-output-queues"):
                            self.number_of_virtual_output_queues = value
                            self.number_of_virtual_output_queues.value_namespace = name_space
                            self.number_of_virtual_output_queues.value_namespace_prefix = name_space_prefix
                        if(value_path == "policy-name"):
                            self.policy_name = value
                            self.policy_name.value_namespace = name_space
                            self.policy_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "virtual-output-queue-statistics-handle"):
                            self.virtual_output_queue_statistics_handle = value
                            self.virtual_output_queue_statistics_handle.value_namespace = name_space
                            self.virtual_output_queue_statistics_handle.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.remote_interface:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.remote_interface:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "remote-interfaces" + path_buffer

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

                    if (child_yang_name == "remote-interface"):
                        for c in self.remote_interface:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.remote_interface.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "remote-interface"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.bundle_interfaces is not None and self.bundle_interfaces.has_data()) or
                    (self.interfaces is not None and self.interfaces.has_data()) or
                    (self.remote_interfaces is not None and self.remote_interfaces.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.bundle_interfaces is not None and self.bundle_interfaces.has_operation()) or
                    (self.interfaces is not None and self.interfaces.has_operation()) or
                    (self.remote_interfaces is not None and self.remote_interfaces.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ncs5500-qos-oper:platform-qos/nodes/%s" % self.get_segment_path()
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

                if (child_yang_name == "bundle-interfaces"):
                    if (self.bundle_interfaces is None):
                        self.bundle_interfaces = PlatformQos.Nodes.Node.BundleInterfaces()
                        self.bundle_interfaces.parent = self
                        self._children_name_map["bundle_interfaces"] = "bundle-interfaces"
                    return self.bundle_interfaces

                if (child_yang_name == "interfaces"):
                    if (self.interfaces is None):
                        self.interfaces = PlatformQos.Nodes.Node.Interfaces()
                        self.interfaces.parent = self
                        self._children_name_map["interfaces"] = "interfaces"
                    return self.interfaces

                if (child_yang_name == "remote-interfaces"):
                    if (self.remote_interfaces is None):
                        self.remote_interfaces = PlatformQos.Nodes.Node.RemoteInterfaces()
                        self.remote_interfaces.parent = self
                        self._children_name_map["remote_interfaces"] = "remote-interfaces"
                    return self.remote_interfaces

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "bundle-interfaces" or name == "interfaces" or name == "remote-interfaces" or name == "node-name"):
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
                path_buffer = "Cisco-IOS-XR-ncs5500-qos-oper:platform-qos/%s" % self.get_segment_path()
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
                c = PlatformQos.Nodes.Node()
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
        path_buffer = "Cisco-IOS-XR-ncs5500-qos-oper:platform-qos" + path_buffer

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
                self.nodes = PlatformQos.Nodes()
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
        self._top_entity = PlatformQos()
        return self._top_entity


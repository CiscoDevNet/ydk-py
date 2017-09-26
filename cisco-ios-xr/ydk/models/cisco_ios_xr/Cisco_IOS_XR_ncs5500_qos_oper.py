""" Cisco_IOS_XR_ncs5500_qos_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ncs5500\-qos package operational data.

This module contains definitions
for the following management objects\:
  platform\-qos\: DNX QoS EA operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
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
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"nodes" : ("nodes", PlatformQos.Nodes)}
        self._child_list_classes = {}

        self.nodes = PlatformQos.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-ncs5500-qos-oper:platform-qos"


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
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"node" : ("node", PlatformQos.Nodes.Node)}

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-ncs5500-qos-oper:platform-qos/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(PlatformQos.Nodes, [], name, value)


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
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"bundle-interfaces" : ("bundle_interfaces", PlatformQos.Nodes.Node.BundleInterfaces), "interfaces" : ("interfaces", PlatformQos.Nodes.Node.Interfaces), "remote-interfaces" : ("remote_interfaces", PlatformQos.Nodes.Node.RemoteInterfaces)}
                self._child_list_classes = {}

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
                self._segment_path = lambda: "node" + "[node-name='" + self.node_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ncs5500-qos-oper:platform-qos/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(PlatformQos.Nodes.Node, ['node_name'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"bundle-interface" : ("bundle_interface", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface)}

                    self.bundle_interface = YList(self)
                    self._segment_path = lambda: "bundle-interfaces"

                def __setattr__(self, name, value):
                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces, [], name, value)


                class BundleInterface(Entity):
                    """
                    QoS interface names
                    
                    .. attribute:: interface_name  <key>
                    
                    	Bundle interface name
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"classes" : ("classes", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes), "member-interfaces" : ("member_interfaces", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces), "policy-details" : ("policy_details", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.PolicyDetails)}
                        self._child_list_classes = {}

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
                        self._segment_path = lambda: "bundle-interface" + "[interface-name='" + self.interface_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface, ['interface_name', 'npu_id', 'qos_direction'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"class" : ("class_", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_)}

                            self.class_ = YList(self)
                            self._segment_path = lambda: "classes"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes, [], name, value)


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
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"config-max-rate" : ("config_max_rate", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigMaxRate), "config-min-rate" : ("config_min_rate", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigMinRate), "config-policer-average-rate" : ("config_policer_average_rate", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerAverageRate), "config-policer-conform-burst" : ("config_policer_conform_burst", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerConformBurst), "config-policer-excess-burst" : ("config_policer_excess_burst", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerExcessBurst), "config-policer-peak-rate" : ("config_policer_peak_rate", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerPeakRate), "config-queue-limit" : ("config_queue_limit", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigQueueLimit), "conform-action" : ("conform_action", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConformAction), "exceed-action" : ("exceed_action", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ExceedAction), "violate-action" : ("violate_action", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ViolateAction)}
                                self._child_list_classes = {"common-mark" : ("common_mark", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.CommonMark), "ip-mark" : ("ip_mark", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.IpMark), "mpls-mark" : ("mpls_mark", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.MplsMark), "wred" : ("wred", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred)}

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
                                self._segment_path = lambda: "class" + "[level-one-class-name='" + self.level_one_class_name.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_, ['level_one_class_name', 'class_level', 'config_excess_bandwidth_percent', 'config_excess_bandwidth_unit', 'egress_queue_id', 'hardware_excess_bandwidth_weight', 'hardware_max_rate_kbps', 'hardware_min_rate_kbps', 'hardware_policer_average_rate_kbps', 'hardware_policer_conform_burst_bytes', 'hardware_policer_excess_burst_bytes', 'hardware_policer_peak_rate_kbps', 'hardware_queue_limit_bytes', 'hardware_queue_limit_microseconds', 'level_two_class_name', 'network_min_bandwidth_kbps', 'policer_bucket_id', 'policer_stats_handle', 'priority_level', 'queue_type'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.mark_type = YLeaf(YType.enumeration, "mark-type")

                                    self.mark_value = YLeaf(YType.uint16, "mark-value")
                                    self._segment_path = lambda: "common-mark"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.CommonMark, ['mark_type', 'mark_value'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                    self.policy_value = YLeaf(YType.uint32, "policy-value")
                                    self._segment_path = lambda: "config-max-rate"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigMaxRate, ['policy_unit', 'policy_value'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                    self.policy_value = YLeaf(YType.uint32, "policy-value")
                                    self._segment_path = lambda: "config-min-rate"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigMinRate, ['policy_unit', 'policy_value'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                    self.policy_value = YLeaf(YType.uint32, "policy-value")
                                    self._segment_path = lambda: "config-policer-average-rate"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerAverageRate, ['policy_unit', 'policy_value'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                    self.policy_value = YLeaf(YType.uint32, "policy-value")
                                    self._segment_path = lambda: "config-policer-conform-burst"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerConformBurst, ['policy_unit', 'policy_value'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                    self.policy_value = YLeaf(YType.uint32, "policy-value")
                                    self._segment_path = lambda: "config-policer-excess-burst"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerExcessBurst, ['policy_unit', 'policy_value'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                    self.policy_value = YLeaf(YType.uint32, "policy-value")
                                    self._segment_path = lambda: "config-policer-peak-rate"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerPeakRate, ['policy_unit', 'policy_value'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                    self.policy_value = YLeaf(YType.uint32, "policy-value")
                                    self._segment_path = lambda: "config-queue-limit"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigQueueLimit, ['policy_unit', 'policy_value'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"mark" : ("mark", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConformAction.Mark)}

                                    self.action_type = YLeaf(YType.enumeration, "action-type")

                                    self.mark = YList(self)
                                    self._segment_path = lambda: "conform-action"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConformAction, ['action_type'], name, value)


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
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.mark_type = YLeaf(YType.enumeration, "mark-type")

                                        self.mark_value = YLeaf(YType.uint16, "mark-value")
                                        self._segment_path = lambda: "mark"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConformAction.Mark, ['mark_type', 'mark_value'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"mark" : ("mark", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ExceedAction.Mark)}

                                    self.action_type = YLeaf(YType.enumeration, "action-type")

                                    self.mark = YList(self)
                                    self._segment_path = lambda: "exceed-action"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ExceedAction, ['action_type'], name, value)


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
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.mark_type = YLeaf(YType.enumeration, "mark-type")

                                        self.mark_value = YLeaf(YType.uint16, "mark-value")
                                        self._segment_path = lambda: "mark"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ExceedAction.Mark, ['mark_type', 'mark_value'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.mark_type = YLeaf(YType.enumeration, "mark-type")

                                    self.mark_value = YLeaf(YType.uint16, "mark-value")
                                    self._segment_path = lambda: "ip-mark"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.IpMark, ['mark_type', 'mark_value'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.mark_type = YLeaf(YType.enumeration, "mark-type")

                                    self.mark_value = YLeaf(YType.uint16, "mark-value")
                                    self._segment_path = lambda: "mpls-mark"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.MplsMark, ['mark_type', 'mark_value'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"mark" : ("mark", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ViolateAction.Mark)}

                                    self.action_type = YLeaf(YType.enumeration, "action-type")

                                    self.mark = YList(self)
                                    self._segment_path = lambda: "violate-action"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ViolateAction, ['action_type'], name, value)


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
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.mark_type = YLeaf(YType.enumeration, "mark-type")

                                        self.mark_value = YLeaf(YType.uint16, "mark-value")
                                        self._segment_path = lambda: "mark"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ViolateAction.Mark, ['mark_type', 'mark_value'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"config-max-threshold" : ("config_max_threshold", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.ConfigMaxThreshold), "config-min-threshold" : ("config_min_threshold", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.ConfigMinThreshold), "wred-match-value" : ("wred_match_value", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.WredMatchValue)}
                                    self._child_list_classes = {}

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
                                    self._segment_path = lambda: "wred"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred, ['first_segment', 'hardware_max_threshold_bytes', 'hardware_min_threshold_bytes', 'segment_size', 'wred_match_type'], name, value)


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
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                        self.policy_value = YLeaf(YType.uint32, "policy-value")
                                        self._segment_path = lambda: "config-max-threshold"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.ConfigMaxThreshold, ['policy_unit', 'policy_value'], name, value)


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
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                        self.policy_value = YLeaf(YType.uint32, "policy-value")
                                        self._segment_path = lambda: "config-min-threshold"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.ConfigMinThreshold, ['policy_unit', 'policy_value'], name, value)


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
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"dnx-qosea-show-red-match-value" : ("dnx_qosea_show_red_match_value", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.WredMatchValue.DnxQoseaShowRedMatchValue)}

                                        self.dnx_qosea_show_red_match_value = YList(self)
                                        self._segment_path = lambda: "wred-match-value"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.WredMatchValue, [], name, value)


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
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.range_end = YLeaf(YType.uint8, "range-end")

                                            self.range_start = YLeaf(YType.uint8, "range-start")
                                            self._segment_path = lambda: "dnx-qosea-show-red-match-value"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.WredMatchValue.DnxQoseaShowRedMatchValue, ['range_end', 'range_start'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"member-interface" : ("member_interface", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface)}

                            self.member_interface = YList(self)
                            self._segment_path = lambda: "member-interfaces"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces, [], name, value)


                        class MemberInterface(Entity):
                            """
                            QoS interface names
                            
                            .. attribute:: interface_name  <key>
                            
                            	Member interface
                            	**type**\:  str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
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
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"classes" : ("classes", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes), "policy-details" : ("policy_details", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.PolicyDetails)}
                                self._child_list_classes = {}

                                self.interface_name = YLeaf(YType.str, "interface-name")

                                self.classes = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes()
                                self.classes.parent = self
                                self._children_name_map["classes"] = "classes"
                                self._children_yang_names.add("classes")

                                self.policy_details = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.PolicyDetails()
                                self.policy_details.parent = self
                                self._children_name_map["policy_details"] = "policy-details"
                                self._children_yang_names.add("policy-details")
                                self._segment_path = lambda: "member-interface" + "[interface-name='" + self.interface_name.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface, ['interface_name'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"class" : ("class_", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_)}

                                    self.class_ = YList(self)
                                    self._segment_path = lambda: "classes"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes, [], name, value)


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
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"config-max-rate" : ("config_max_rate", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigMaxRate), "config-min-rate" : ("config_min_rate", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigMinRate), "config-policer-average-rate" : ("config_policer_average_rate", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerAverageRate), "config-policer-conform-burst" : ("config_policer_conform_burst", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerConformBurst), "config-policer-excess-burst" : ("config_policer_excess_burst", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerExcessBurst), "config-policer-peak-rate" : ("config_policer_peak_rate", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerPeakRate), "config-queue-limit" : ("config_queue_limit", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigQueueLimit), "conform-action" : ("conform_action", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConformAction), "exceed-action" : ("exceed_action", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ExceedAction), "violate-action" : ("violate_action", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ViolateAction)}
                                        self._child_list_classes = {"common-mark" : ("common_mark", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.CommonMark), "ip-mark" : ("ip_mark", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.IpMark), "mpls-mark" : ("mpls_mark", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.MplsMark), "wred" : ("wred", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred)}

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
                                        self._segment_path = lambda: "class" + "[level-one-class-name='" + self.level_one_class_name.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_, ['level_one_class_name', 'class_level', 'config_excess_bandwidth_percent', 'config_excess_bandwidth_unit', 'egress_queue_id', 'hardware_excess_bandwidth_weight', 'hardware_max_rate_kbps', 'hardware_min_rate_kbps', 'hardware_policer_average_rate_kbps', 'hardware_policer_conform_burst_bytes', 'hardware_policer_excess_burst_bytes', 'hardware_policer_peak_rate_kbps', 'hardware_queue_limit_bytes', 'hardware_queue_limit_microseconds', 'level_two_class_name', 'network_min_bandwidth_kbps', 'policer_bucket_id', 'policer_stats_handle', 'priority_level', 'queue_type'], name, value)


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
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.mark_type = YLeaf(YType.enumeration, "mark-type")

                                            self.mark_value = YLeaf(YType.uint16, "mark-value")
                                            self._segment_path = lambda: "common-mark"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.CommonMark, ['mark_type', 'mark_value'], name, value)


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
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                            self.policy_value = YLeaf(YType.uint32, "policy-value")
                                            self._segment_path = lambda: "config-max-rate"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigMaxRate, ['policy_unit', 'policy_value'], name, value)


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
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                            self.policy_value = YLeaf(YType.uint32, "policy-value")
                                            self._segment_path = lambda: "config-min-rate"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigMinRate, ['policy_unit', 'policy_value'], name, value)


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
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                            self.policy_value = YLeaf(YType.uint32, "policy-value")
                                            self._segment_path = lambda: "config-policer-average-rate"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerAverageRate, ['policy_unit', 'policy_value'], name, value)


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
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                            self.policy_value = YLeaf(YType.uint32, "policy-value")
                                            self._segment_path = lambda: "config-policer-conform-burst"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerConformBurst, ['policy_unit', 'policy_value'], name, value)


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
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                            self.policy_value = YLeaf(YType.uint32, "policy-value")
                                            self._segment_path = lambda: "config-policer-excess-burst"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerExcessBurst, ['policy_unit', 'policy_value'], name, value)


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
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                            self.policy_value = YLeaf(YType.uint32, "policy-value")
                                            self._segment_path = lambda: "config-policer-peak-rate"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerPeakRate, ['policy_unit', 'policy_value'], name, value)


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
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                            self.policy_value = YLeaf(YType.uint32, "policy-value")
                                            self._segment_path = lambda: "config-queue-limit"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigQueueLimit, ['policy_unit', 'policy_value'], name, value)


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
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {"mark" : ("mark", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConformAction.Mark)}

                                            self.action_type = YLeaf(YType.enumeration, "action-type")

                                            self.mark = YList(self)
                                            self._segment_path = lambda: "conform-action"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConformAction, ['action_type'], name, value)


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
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.mark_type = YLeaf(YType.enumeration, "mark-type")

                                                self.mark_value = YLeaf(YType.uint16, "mark-value")
                                                self._segment_path = lambda: "mark"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConformAction.Mark, ['mark_type', 'mark_value'], name, value)


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
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {"mark" : ("mark", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ExceedAction.Mark)}

                                            self.action_type = YLeaf(YType.enumeration, "action-type")

                                            self.mark = YList(self)
                                            self._segment_path = lambda: "exceed-action"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ExceedAction, ['action_type'], name, value)


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
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.mark_type = YLeaf(YType.enumeration, "mark-type")

                                                self.mark_value = YLeaf(YType.uint16, "mark-value")
                                                self._segment_path = lambda: "mark"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ExceedAction.Mark, ['mark_type', 'mark_value'], name, value)


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
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.mark_type = YLeaf(YType.enumeration, "mark-type")

                                            self.mark_value = YLeaf(YType.uint16, "mark-value")
                                            self._segment_path = lambda: "ip-mark"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.IpMark, ['mark_type', 'mark_value'], name, value)


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
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.mark_type = YLeaf(YType.enumeration, "mark-type")

                                            self.mark_value = YLeaf(YType.uint16, "mark-value")
                                            self._segment_path = lambda: "mpls-mark"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.MplsMark, ['mark_type', 'mark_value'], name, value)


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
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {"mark" : ("mark", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ViolateAction.Mark)}

                                            self.action_type = YLeaf(YType.enumeration, "action-type")

                                            self.mark = YList(self)
                                            self._segment_path = lambda: "violate-action"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ViolateAction, ['action_type'], name, value)


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
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.mark_type = YLeaf(YType.enumeration, "mark-type")

                                                self.mark_value = YLeaf(YType.uint16, "mark-value")
                                                self._segment_path = lambda: "mark"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ViolateAction.Mark, ['mark_type', 'mark_value'], name, value)


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
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {"config-max-threshold" : ("config_max_threshold", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.ConfigMaxThreshold), "config-min-threshold" : ("config_min_threshold", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.ConfigMinThreshold), "wred-match-value" : ("wred_match_value", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.WredMatchValue)}
                                            self._child_list_classes = {}

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
                                            self._segment_path = lambda: "wred"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred, ['first_segment', 'hardware_max_threshold_bytes', 'hardware_min_threshold_bytes', 'segment_size', 'wred_match_type'], name, value)


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
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                                self.policy_value = YLeaf(YType.uint32, "policy-value")
                                                self._segment_path = lambda: "config-max-threshold"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.ConfigMaxThreshold, ['policy_unit', 'policy_value'], name, value)


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
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                                self.policy_value = YLeaf(YType.uint32, "policy-value")
                                                self._segment_path = lambda: "config-min-threshold"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.ConfigMinThreshold, ['policy_unit', 'policy_value'], name, value)


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
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {"dnx-qosea-show-red-match-value" : ("dnx_qosea_show_red_match_value", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.WredMatchValue.DnxQoseaShowRedMatchValue)}

                                                self.dnx_qosea_show_red_match_value = YList(self)
                                                self._segment_path = lambda: "wred-match-value"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.WredMatchValue, [], name, value)


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
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.range_end = YLeaf(YType.uint8, "range-end")

                                                    self.range_start = YLeaf(YType.uint8, "range-start")
                                                    self._segment_path = lambda: "dnx-qosea-show-red-match-value"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.WredMatchValue.DnxQoseaShowRedMatchValue, ['range_end', 'range_start'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

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
                                    self._segment_path = lambda: "policy-details"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.PolicyDetails, ['interface_bandwidth_kbps', 'interface_handle', 'interface_status', 'npu_id', 'policy_name', 'policy_status', 'stats_accounting_type', 'total_number_of_classes', 'voq_base_address', 'voq_stats_handle'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

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
                            self._segment_path = lambda: "policy-details"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.PolicyDetails, ['interface_bandwidth_kbps', 'interface_handle', 'interface_status', 'npu_id', 'policy_name', 'policy_status', 'stats_accounting_type', 'total_number_of_classes', 'voq_base_address', 'voq_stats_handle'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"interface" : ("interface", PlatformQos.Nodes.Node.Interfaces.Interface)}

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"

                def __setattr__(self, name, value):
                    self._perform_setattr(PlatformQos.Nodes.Node.Interfaces, [], name, value)


                class Interface(Entity):
                    """
                    QoS interface names
                    
                    .. attribute:: interface_name  <key>
                    
                    	The name of the interface
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"classes" : ("classes", PlatformQos.Nodes.Node.Interfaces.Interface.Classes), "policy-details" : ("policy_details", PlatformQos.Nodes.Node.Interfaces.Interface.PolicyDetails)}
                        self._child_list_classes = {}

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
                        self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface, ['interface_name', 'qos_direction'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"class" : ("class_", PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_)}

                            self.class_ = YList(self)
                            self._segment_path = lambda: "classes"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Classes, [], name, value)


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
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"config-max-rate" : ("config_max_rate", PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigMaxRate), "config-min-rate" : ("config_min_rate", PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigMinRate), "config-policer-average-rate" : ("config_policer_average_rate", PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerAverageRate), "config-policer-conform-burst" : ("config_policer_conform_burst", PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerConformBurst), "config-policer-excess-burst" : ("config_policer_excess_burst", PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerExcessBurst), "config-policer-peak-rate" : ("config_policer_peak_rate", PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerPeakRate), "config-queue-limit" : ("config_queue_limit", PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigQueueLimit), "conform-action" : ("conform_action", PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConformAction), "exceed-action" : ("exceed_action", PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ExceedAction), "violate-action" : ("violate_action", PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ViolateAction)}
                                self._child_list_classes = {"common-mark" : ("common_mark", PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.CommonMark), "ip-mark" : ("ip_mark", PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.IpMark), "mpls-mark" : ("mpls_mark", PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.MplsMark), "wred" : ("wred", PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred)}

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
                                self._segment_path = lambda: "class" + "[level-one-class-name='" + self.level_one_class_name.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_, ['level_one_class_name', 'class_level', 'config_excess_bandwidth_percent', 'config_excess_bandwidth_unit', 'egress_queue_id', 'hardware_excess_bandwidth_weight', 'hardware_max_rate_kbps', 'hardware_min_rate_kbps', 'hardware_policer_average_rate_kbps', 'hardware_policer_conform_burst_bytes', 'hardware_policer_excess_burst_bytes', 'hardware_policer_peak_rate_kbps', 'hardware_queue_limit_bytes', 'hardware_queue_limit_microseconds', 'level_two_class_name', 'network_min_bandwidth_kbps', 'policer_bucket_id', 'policer_stats_handle', 'priority_level', 'queue_type'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.mark_type = YLeaf(YType.enumeration, "mark-type")

                                    self.mark_value = YLeaf(YType.uint16, "mark-value")
                                    self._segment_path = lambda: "common-mark"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.CommonMark, ['mark_type', 'mark_value'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                    self.policy_value = YLeaf(YType.uint32, "policy-value")
                                    self._segment_path = lambda: "config-max-rate"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigMaxRate, ['policy_unit', 'policy_value'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                    self.policy_value = YLeaf(YType.uint32, "policy-value")
                                    self._segment_path = lambda: "config-min-rate"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigMinRate, ['policy_unit', 'policy_value'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                    self.policy_value = YLeaf(YType.uint32, "policy-value")
                                    self._segment_path = lambda: "config-policer-average-rate"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerAverageRate, ['policy_unit', 'policy_value'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                    self.policy_value = YLeaf(YType.uint32, "policy-value")
                                    self._segment_path = lambda: "config-policer-conform-burst"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerConformBurst, ['policy_unit', 'policy_value'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                    self.policy_value = YLeaf(YType.uint32, "policy-value")
                                    self._segment_path = lambda: "config-policer-excess-burst"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerExcessBurst, ['policy_unit', 'policy_value'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                    self.policy_value = YLeaf(YType.uint32, "policy-value")
                                    self._segment_path = lambda: "config-policer-peak-rate"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerPeakRate, ['policy_unit', 'policy_value'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                    self.policy_value = YLeaf(YType.uint32, "policy-value")
                                    self._segment_path = lambda: "config-queue-limit"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigQueueLimit, ['policy_unit', 'policy_value'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"mark" : ("mark", PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConformAction.Mark)}

                                    self.action_type = YLeaf(YType.enumeration, "action-type")

                                    self.mark = YList(self)
                                    self._segment_path = lambda: "conform-action"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConformAction, ['action_type'], name, value)


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
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.mark_type = YLeaf(YType.enumeration, "mark-type")

                                        self.mark_value = YLeaf(YType.uint16, "mark-value")
                                        self._segment_path = lambda: "mark"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConformAction.Mark, ['mark_type', 'mark_value'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"mark" : ("mark", PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ExceedAction.Mark)}

                                    self.action_type = YLeaf(YType.enumeration, "action-type")

                                    self.mark = YList(self)
                                    self._segment_path = lambda: "exceed-action"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ExceedAction, ['action_type'], name, value)


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
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.mark_type = YLeaf(YType.enumeration, "mark-type")

                                        self.mark_value = YLeaf(YType.uint16, "mark-value")
                                        self._segment_path = lambda: "mark"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ExceedAction.Mark, ['mark_type', 'mark_value'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.mark_type = YLeaf(YType.enumeration, "mark-type")

                                    self.mark_value = YLeaf(YType.uint16, "mark-value")
                                    self._segment_path = lambda: "ip-mark"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.IpMark, ['mark_type', 'mark_value'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.mark_type = YLeaf(YType.enumeration, "mark-type")

                                    self.mark_value = YLeaf(YType.uint16, "mark-value")
                                    self._segment_path = lambda: "mpls-mark"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.MplsMark, ['mark_type', 'mark_value'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"mark" : ("mark", PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ViolateAction.Mark)}

                                    self.action_type = YLeaf(YType.enumeration, "action-type")

                                    self.mark = YList(self)
                                    self._segment_path = lambda: "violate-action"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ViolateAction, ['action_type'], name, value)


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
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.mark_type = YLeaf(YType.enumeration, "mark-type")

                                        self.mark_value = YLeaf(YType.uint16, "mark-value")
                                        self._segment_path = lambda: "mark"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ViolateAction.Mark, ['mark_type', 'mark_value'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"config-max-threshold" : ("config_max_threshold", PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.ConfigMaxThreshold), "config-min-threshold" : ("config_min_threshold", PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.ConfigMinThreshold), "wred-match-value" : ("wred_match_value", PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.WredMatchValue)}
                                    self._child_list_classes = {}

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
                                    self._segment_path = lambda: "wred"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred, ['first_segment', 'hardware_max_threshold_bytes', 'hardware_min_threshold_bytes', 'segment_size', 'wred_match_type'], name, value)


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
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                        self.policy_value = YLeaf(YType.uint32, "policy-value")
                                        self._segment_path = lambda: "config-max-threshold"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.ConfigMaxThreshold, ['policy_unit', 'policy_value'], name, value)


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
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.policy_unit = YLeaf(YType.enumeration, "policy-unit")

                                        self.policy_value = YLeaf(YType.uint32, "policy-value")
                                        self._segment_path = lambda: "config-min-threshold"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.ConfigMinThreshold, ['policy_unit', 'policy_value'], name, value)


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
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"dnx-qosea-show-red-match-value" : ("dnx_qosea_show_red_match_value", PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.WredMatchValue.DnxQoseaShowRedMatchValue)}

                                        self.dnx_qosea_show_red_match_value = YList(self)
                                        self._segment_path = lambda: "wred-match-value"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.WredMatchValue, [], name, value)


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
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.range_end = YLeaf(YType.uint8, "range-end")

                                            self.range_start = YLeaf(YType.uint8, "range-start")
                                            self._segment_path = lambda: "dnx-qosea-show-red-match-value"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.WredMatchValue.DnxQoseaShowRedMatchValue, ['range_end', 'range_start'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

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
                            self._segment_path = lambda: "policy-details"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.PolicyDetails, ['interface_bandwidth_kbps', 'interface_handle', 'interface_status', 'npu_id', 'policy_name', 'policy_status', 'stats_accounting_type', 'total_number_of_classes', 'voq_base_address', 'voq_stats_handle'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"remote-interface" : ("remote_interface", PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface)}

                    self.remote_interface = YList(self)
                    self._segment_path = lambda: "remote-interfaces"

                def __setattr__(self, name, value):
                    self._perform_setattr(PlatformQos.Nodes.Node.RemoteInterfaces, [], name, value)


                class RemoteInterface(Entity):
                    """
                    QoS remote interface names
                    
                    .. attribute:: interface_name  <key>
                    
                    	The name of the remote interface
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"remote-class" : ("remote_class", PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass)}

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.interface_handle = YLeaf(YType.uint32, "interface-handle")

                        self.number_of_classes = YLeaf(YType.uint32, "number-of-classes")

                        self.number_of_virtual_output_queues = YLeaf(YType.uint32, "number-of-virtual-output-queues")

                        self.policy_name = YLeaf(YType.str, "policy-name")

                        self.virtual_output_queue_statistics_handle = YLeaf(YType.uint64, "virtual-output-queue-statistics-handle")

                        self.remote_class = YList(self)
                        self._segment_path = lambda: "remote-interface" + "[interface-name='" + self.interface_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface, ['interface_name', 'interface_handle', 'number_of_classes', 'number_of_virtual_output_queues', 'policy_name', 'virtual_output_queue_statistics_handle'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"hw-wred" : ("hw_wred", PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass.HwWred), "wred" : ("wred", PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass.Wred)}

                            self.class_id = YLeaf(YType.uint32, "class-id")

                            self.class_name = YLeaf(YType.str, "class-name")

                            self.cos_q = YLeaf(YType.uint32, "cos-q")

                            self.hardware_queue_limit = YLeaf(YType.uint32, "hardware-queue-limit")

                            self.queue_limit = YLeaf(YType.uint32, "queue-limit")

                            self.hw_wred = YList(self)
                            self.wred = YList(self)
                            self._segment_path = lambda: "remote-class"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass, ['class_id', 'class_name', 'cos_q', 'hardware_queue_limit', 'queue_limit'], name, value)


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
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.drop_probability = YLeaf(YType.uint32, "drop-probability")

                                self.max_threshold = YLeaf(YType.uint32, "max-threshold")

                                self.min_threshold = YLeaf(YType.uint32, "min-threshold")
                                self._segment_path = lambda: "hw-wred"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass.HwWred, ['drop_probability', 'max_threshold', 'min_threshold'], name, value)


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
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.drop_probability = YLeaf(YType.uint32, "drop-probability")

                                self.max_threshold = YLeaf(YType.uint32, "max-threshold")

                                self.min_threshold = YLeaf(YType.uint32, "min-threshold")
                                self._segment_path = lambda: "wred"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass.Wred, ['drop_probability', 'max_threshold', 'min_threshold'], name, value)

    def clone_ptr(self):
        self._top_entity = PlatformQos()
        return self._top_entity


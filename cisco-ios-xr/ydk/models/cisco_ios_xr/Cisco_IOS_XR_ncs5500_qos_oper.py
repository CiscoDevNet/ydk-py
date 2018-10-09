""" Cisco_IOS_XR_ncs5500_qos_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ncs5500\-qos package operational data.

This module contains definitions
for the following management objects\:
  platform\-qos\: DNX QoS EA operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class DnxQoseaShowAction(Enum):
    """
    DnxQoseaShowAction (Enum Class)

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
    DnxQoseaShowHpLevel (Enum Class)

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
    DnxQoseaShowIntfStatus (Enum Class)

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
    DnxQoseaShowLevel (Enum Class)

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
    DnxQoseaShowMark (Enum Class)

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

    .. data:: un_supported11 = 11

    	Unsupported type 11

    .. data:: dscp_tunnel = 12

    	DSCP tunnel

    .. data:: precedence_tunnel = 13

    	Precedence tunnel

    .. data:: dei = 14

    	DEI

    .. data:: dei_imposition = 15

    	DEI Imposition

    .. data:: un_supported16 = 16

    	Unsupported type 16

    .. data:: un_supported17 = 17

    	Unsupported type 17

    .. data:: traffic_class = 18

    	Traffic class

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

    un_supported11 = Enum.YLeaf(11, "un-supported11")

    dscp_tunnel = Enum.YLeaf(12, "dscp-tunnel")

    precedence_tunnel = Enum.YLeaf(13, "precedence-tunnel")

    dei = Enum.YLeaf(14, "dei")

    dei_imposition = Enum.YLeaf(15, "dei-imposition")

    un_supported16 = Enum.YLeaf(16, "un-supported16")

    un_supported17 = Enum.YLeaf(17, "un-supported17")

    traffic_class = Enum.YLeaf(18, "traffic-class")


class DnxQoseaShowPolicyStatus(Enum):
    """
    DnxQoseaShowPolicyStatus (Enum Class)

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
    DnxQoseaShowQueue (Enum Class)

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
    DnxQoseaShowWred (Enum Class)

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
    PolicyParamUnit (Enum Class)

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
    QosPolicyAccountEnum (Enum Class)

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
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes>`
    
    

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
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", PlatformQos.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = PlatformQos.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-ncs5500-qos-oper:platform-qos"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(PlatformQos, [], name, value)


    class Nodes(Entity):
        """
        List of nodes with platform specific QoS
        configuration
        
        .. attribute:: node
        
        	Node with platform specific QoS configuration
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node>`
        
        

        """

        _prefix = 'ncs5500-qos-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(PlatformQos.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "platform-qos"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", PlatformQos.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-ncs5500-qos-oper:platform-qos/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PlatformQos.Nodes, [], name, value)


        class Node(Entity):
            """
            Node with platform specific QoS configuration
            
            .. attribute:: node_name  (key)
            
            	Node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: bundle_interfaces
            
            	QoS list of bundle interfaces
            	**type**\:  :py:class:`BundleInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces>`
            
            .. attribute:: interfaces
            
            	QoS list of interfaces
            	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces>`
            
            .. attribute:: qos_interfaces
            
            	QoS list of interfaces
            	**type**\:  :py:class:`QosInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces>`
            
            .. attribute:: bundle_interface_singles
            
            	QoS list of bundle interfaces
            	**type**\:  :py:class:`BundleInterfaceSingles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles>`
            
            .. attribute:: remote_interfaces
            
            	QoS list of remote interfaces
            	**type**\:  :py:class:`RemoteInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.RemoteInterfaces>`
            
            

            """

            _prefix = 'ncs5500-qos-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(PlatformQos.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("bundle-interfaces", ("bundle_interfaces", PlatformQos.Nodes.Node.BundleInterfaces)), ("interfaces", ("interfaces", PlatformQos.Nodes.Node.Interfaces)), ("qos-interfaces", ("qos_interfaces", PlatformQos.Nodes.Node.QosInterfaces)), ("bundle-interface-singles", ("bundle_interface_singles", PlatformQos.Nodes.Node.BundleInterfaceSingles)), ("remote-interfaces", ("remote_interfaces", PlatformQos.Nodes.Node.RemoteInterfaces))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.bundle_interfaces = PlatformQos.Nodes.Node.BundleInterfaces()
                self.bundle_interfaces.parent = self
                self._children_name_map["bundle_interfaces"] = "bundle-interfaces"

                self.interfaces = PlatformQos.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"

                self.qos_interfaces = PlatformQos.Nodes.Node.QosInterfaces()
                self.qos_interfaces.parent = self
                self._children_name_map["qos_interfaces"] = "qos-interfaces"

                self.bundle_interface_singles = PlatformQos.Nodes.Node.BundleInterfaceSingles()
                self.bundle_interface_singles.parent = self
                self._children_name_map["bundle_interface_singles"] = "bundle-interface-singles"

                self.remote_interfaces = PlatformQos.Nodes.Node.RemoteInterfaces()
                self.remote_interfaces.parent = self
                self._children_name_map["remote_interfaces"] = "remote-interfaces"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ncs5500-qos-oper:platform-qos/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PlatformQos.Nodes.Node, ['node_name'], name, value)


            class BundleInterfaces(Entity):
                """
                QoS list of bundle interfaces
                
                .. attribute:: bundle_interface
                
                	QoS interface names
                	**type**\: list of  		 :py:class:`BundleInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface>`
                
                

                """

                _prefix = 'ncs5500-qos-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PlatformQos.Nodes.Node.BundleInterfaces, self).__init__()

                    self.yang_name = "bundle-interfaces"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("bundle-interface", ("bundle_interface", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface))])
                    self._leafs = OrderedDict()

                    self.bundle_interface = YList(self)
                    self._segment_path = lambda: "bundle-interfaces"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces, [], name, value)


                class BundleInterface(Entity):
                    """
                    QoS interface names
                    
                    .. attribute:: interface_name
                    
                    	Bundle interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: npu_id
                    
                    	NPU ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: qos_direction
                    
                    	The interface direction on which QoS is applied to
                    	**type**\: str
                    
                    .. attribute:: policy_details
                    
                    	Policy Details
                    	**type**\:  :py:class:`PolicyDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.PolicyDetails>`
                    
                    .. attribute:: member_interfaces
                    
                    	QoS list of member interfaces
                    	**type**\:  :py:class:`MemberInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces>`
                    
                    .. attribute:: class_table
                    
                    	QoS list of class names
                    	**type**\:  :py:class:`ClassTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable>`
                    
                    

                    """

                    _prefix = 'ncs5500-qos-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface, self).__init__()

                        self.yang_name = "bundle-interface"
                        self.yang_parent_name = "bundle-interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("policy-details", ("policy_details", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.PolicyDetails)), ("member-interfaces", ("member_interfaces", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces)), ("class-table", ("class_table", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('npu_id', (YLeaf(YType.uint32, 'npu-id'), ['int'])),
                            ('qos_direction', (YLeaf(YType.str, 'qos-direction'), ['str'])),
                        ])
                        self.interface_name = None
                        self.npu_id = None
                        self.qos_direction = None

                        self.policy_details = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.PolicyDetails()
                        self.policy_details.parent = self
                        self._children_name_map["policy_details"] = "policy-details"

                        self.member_interfaces = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces()
                        self.member_interfaces.parent = self
                        self._children_name_map["member_interfaces"] = "member-interfaces"

                        self.class_table = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable()
                        self.class_table.parent = self
                        self._children_name_map["class_table"] = "class-table"
                        self._segment_path = lambda: "bundle-interface"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface, ['interface_name', 'npu_id', 'qos_direction'], name, value)


                    class PolicyDetails(Entity):
                        """
                        Policy Details
                        
                        .. attribute:: npu_id
                        
                        	NPU ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: interface_handle
                        
                        	InterfaceHandle
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: interface_bandwidth_kbps
                        
                        	Interface Bandwidth (in kbps)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: kbit/s
                        
                        .. attribute:: policy_name
                        
                        	Policy name
                        	**type**\: str
                        
                        	**length:** 0..64
                        
                        .. attribute:: total_number_of_classes
                        
                        	Number of Classes
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: voq_base_address
                        
                        	VOQ base address
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: voq_stats_handle
                        
                        	VOQ stats handle
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: stats_accounting_type
                        
                        	QoS Statistics Accounting Type
                        	**type**\:  :py:class:`QosPolicyAccountEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.QosPolicyAccountEnum>`
                        
                        .. attribute:: policy_status
                        
                        	Policy Status
                        	**type**\:  :py:class:`DnxQoseaShowPolicyStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowPolicyStatus>`
                        
                        .. attribute:: interface_status
                        
                        	Interface Status
                        	**type**\:  :py:class:`DnxQoseaShowIntfStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowIntfStatus>`
                        
                        

                        """

                        _prefix = 'ncs5500-qos-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.PolicyDetails, self).__init__()

                            self.yang_name = "policy-details"
                            self.yang_parent_name = "bundle-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('npu_id', (YLeaf(YType.uint32, 'npu-id'), ['int'])),
                                ('interface_handle', (YLeaf(YType.uint32, 'interface-handle'), ['int'])),
                                ('interface_bandwidth_kbps', (YLeaf(YType.uint32, 'interface-bandwidth-kbps'), ['int'])),
                                ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                ('total_number_of_classes', (YLeaf(YType.uint16, 'total-number-of-classes'), ['int'])),
                                ('voq_base_address', (YLeaf(YType.uint32, 'voq-base-address'), ['int'])),
                                ('voq_stats_handle', (YLeaf(YType.uint64, 'voq-stats-handle'), ['int'])),
                                ('stats_accounting_type', (YLeaf(YType.enumeration, 'stats-accounting-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'QosPolicyAccountEnum', '')])),
                                ('policy_status', (YLeaf(YType.enumeration, 'policy-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowPolicyStatus', '')])),
                                ('interface_status', (YLeaf(YType.enumeration, 'interface-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowIntfStatus', '')])),
                            ])
                            self.npu_id = None
                            self.interface_handle = None
                            self.interface_bandwidth_kbps = None
                            self.policy_name = None
                            self.total_number_of_classes = None
                            self.voq_base_address = None
                            self.voq_stats_handle = None
                            self.stats_accounting_type = None
                            self.policy_status = None
                            self.interface_status = None
                            self._segment_path = lambda: "policy-details"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.PolicyDetails, [u'npu_id', u'interface_handle', u'interface_bandwidth_kbps', u'policy_name', u'total_number_of_classes', u'voq_base_address', u'voq_stats_handle', u'stats_accounting_type', u'policy_status', u'interface_status'], name, value)


                    class MemberInterfaces(Entity):
                        """
                        QoS list of member interfaces
                        
                        .. attribute:: member_interface
                        
                        	QoS interface names
                        	**type**\: list of  		 :py:class:`MemberInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface>`
                        
                        

                        """

                        _prefix = 'ncs5500-qos-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces, self).__init__()

                            self.yang_name = "member-interfaces"
                            self.yang_parent_name = "bundle-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("member-interface", ("member_interface", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface))])
                            self._leafs = OrderedDict()

                            self.member_interface = YList(self)
                            self._segment_path = lambda: "member-interfaces"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces, [], name, value)


                        class MemberInterface(Entity):
                            """
                            QoS interface names
                            
                            .. attribute:: interface_name  (key)
                            
                            	Member interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: policy_details
                            
                            	Policy Details
                            	**type**\:  :py:class:`PolicyDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.PolicyDetails>`
                            
                            .. attribute:: class_table
                            
                            	QoS list of class names
                            	**type**\:  :py:class:`ClassTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable>`
                            
                            

                            """

                            _prefix = 'ncs5500-qos-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface, self).__init__()

                                self.yang_name = "member-interface"
                                self.yang_parent_name = "member-interfaces"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['interface_name']
                                self._child_classes = OrderedDict([("policy-details", ("policy_details", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.PolicyDetails)), ("class-table", ("class_table", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable))])
                                self._leafs = OrderedDict([
                                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ])
                                self.interface_name = None

                                self.policy_details = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.PolicyDetails()
                                self.policy_details.parent = self
                                self._children_name_map["policy_details"] = "policy-details"

                                self.class_table = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable()
                                self.class_table.parent = self
                                self._children_name_map["class_table"] = "class-table"
                                self._segment_path = lambda: "member-interface" + "[interface-name='" + str(self.interface_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface, ['interface_name'], name, value)


                            class PolicyDetails(Entity):
                                """
                                Policy Details
                                
                                .. attribute:: npu_id
                                
                                	NPU ID
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: interface_handle
                                
                                	InterfaceHandle
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: interface_bandwidth_kbps
                                
                                	Interface Bandwidth (in kbps)
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: kbit/s
                                
                                .. attribute:: policy_name
                                
                                	Policy name
                                	**type**\: str
                                
                                	**length:** 0..64
                                
                                .. attribute:: total_number_of_classes
                                
                                	Number of Classes
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: voq_base_address
                                
                                	VOQ base address
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: voq_stats_handle
                                
                                	VOQ stats handle
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: stats_accounting_type
                                
                                	QoS Statistics Accounting Type
                                	**type**\:  :py:class:`QosPolicyAccountEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.QosPolicyAccountEnum>`
                                
                                .. attribute:: policy_status
                                
                                	Policy Status
                                	**type**\:  :py:class:`DnxQoseaShowPolicyStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowPolicyStatus>`
                                
                                .. attribute:: interface_status
                                
                                	Interface Status
                                	**type**\:  :py:class:`DnxQoseaShowIntfStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowIntfStatus>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.PolicyDetails, self).__init__()

                                    self.yang_name = "policy-details"
                                    self.yang_parent_name = "member-interface"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('npu_id', (YLeaf(YType.uint32, 'npu-id'), ['int'])),
                                        ('interface_handle', (YLeaf(YType.uint32, 'interface-handle'), ['int'])),
                                        ('interface_bandwidth_kbps', (YLeaf(YType.uint32, 'interface-bandwidth-kbps'), ['int'])),
                                        ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                        ('total_number_of_classes', (YLeaf(YType.uint16, 'total-number-of-classes'), ['int'])),
                                        ('voq_base_address', (YLeaf(YType.uint32, 'voq-base-address'), ['int'])),
                                        ('voq_stats_handle', (YLeaf(YType.uint64, 'voq-stats-handle'), ['int'])),
                                        ('stats_accounting_type', (YLeaf(YType.enumeration, 'stats-accounting-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'QosPolicyAccountEnum', '')])),
                                        ('policy_status', (YLeaf(YType.enumeration, 'policy-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowPolicyStatus', '')])),
                                        ('interface_status', (YLeaf(YType.enumeration, 'interface-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowIntfStatus', '')])),
                                    ])
                                    self.npu_id = None
                                    self.interface_handle = None
                                    self.interface_bandwidth_kbps = None
                                    self.policy_name = None
                                    self.total_number_of_classes = None
                                    self.voq_base_address = None
                                    self.voq_stats_handle = None
                                    self.stats_accounting_type = None
                                    self.policy_status = None
                                    self.interface_status = None
                                    self._segment_path = lambda: "policy-details"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.PolicyDetails, [u'npu_id', u'interface_handle', u'interface_bandwidth_kbps', u'policy_name', u'total_number_of_classes', u'voq_base_address', u'voq_stats_handle', u'stats_accounting_type', u'policy_status', u'interface_status'], name, value)


                            class ClassTable(Entity):
                                """
                                QoS list of class names
                                
                                .. attribute:: class_
                                
                                	QoS policy class
                                	**type**\: list of  		 :py:class:`Class <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable, self).__init__()

                                    self.yang_name = "class-table"
                                    self.yang_parent_name = "member-interface"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("class", ("class_", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class))])
                                    self._leafs = OrderedDict()

                                    self.class_ = YList(self)
                                    self._segment_path = lambda: "class-table"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable, [], name, value)


                                class Class(Entity):
                                    """
                                    QoS policy class
                                    
                                    .. attribute:: level_one_class_name  (key)
                                    
                                    	QoS policy class name at level 1
                                    	**type**\: str
                                    
                                    .. attribute:: level_two_class_name
                                    
                                    	QoS policy child class name at level 2
                                    	**type**\: str
                                    
                                    .. attribute:: config_max_rate
                                    
                                    	Configured maximum rate
                                    	**type**\:  :py:class:`ConfigMaxRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigMaxRate>`
                                    
                                    .. attribute:: config_min_rate
                                    
                                    	Configured minimum rate
                                    	**type**\:  :py:class:`ConfigMinRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigMinRate>`
                                    
                                    .. attribute:: config_queue_limit
                                    
                                    	Configured queue limit
                                    	**type**\:  :py:class:`ConfigQueueLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigQueueLimit>`
                                    
                                    .. attribute:: config_policer_average_rate
                                    
                                    	Configured policer average rate
                                    	**type**\:  :py:class:`ConfigPolicerAverageRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigPolicerAverageRate>`
                                    
                                    .. attribute:: config_policer_peak_rate
                                    
                                    	Config policer peak rate
                                    	**type**\:  :py:class:`ConfigPolicerPeakRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigPolicerPeakRate>`
                                    
                                    .. attribute:: config_policer_conform_burst
                                    
                                    	Configured policer conform burst
                                    	**type**\:  :py:class:`ConfigPolicerConformBurst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigPolicerConformBurst>`
                                    
                                    .. attribute:: config_policer_excess_burst
                                    
                                    	Configured policer excess burst
                                    	**type**\:  :py:class:`ConfigPolicerExcessBurst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigPolicerExcessBurst>`
                                    
                                    .. attribute:: conform_action
                                    
                                    	Conform action
                                    	**type**\:  :py:class:`ConformAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ConformAction>`
                                    
                                    .. attribute:: exceed_action
                                    
                                    	Exceed action
                                    	**type**\:  :py:class:`ExceedAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ExceedAction>`
                                    
                                    .. attribute:: violate_action
                                    
                                    	Violate action
                                    	**type**\:  :py:class:`ViolateAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ViolateAction>`
                                    
                                    .. attribute:: class_level
                                    
                                    	Class level
                                    	**type**\:  :py:class:`DnxQoseaShowLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowLevel>`
                                    
                                    .. attribute:: egress_queue_id
                                    
                                    	Egress Queue ID
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: queue_type
                                    
                                    	Queue type
                                    	**type**\:  :py:class:`DnxQoseaShowQueue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowQueue>`
                                    
                                    .. attribute:: priority_level
                                    
                                    	Priority level
                                    	**type**\:  :py:class:`DnxQoseaShowHpLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowHpLevel>`
                                    
                                    .. attribute:: hardware_max_rate_kbps
                                    
                                    	Hardware maximum rate in kbps
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**units**\: kbit/s
                                    
                                    .. attribute:: hardware_min_rate_kbps
                                    
                                    	Hardware minimum rate in kbps
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**units**\: kbit/s
                                    
                                    .. attribute:: config_excess_bandwidth_percent
                                    
                                    	Configured excess bandwidth percentage
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**units**\: percentage
                                    
                                    .. attribute:: config_excess_bandwidth_unit
                                    
                                    	Configured excess bandwidth unit
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: hardware_excess_bandwidth_weight
                                    
                                    	Hardware excess bandwidth weight
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: network_min_bandwidth_kbps
                                    
                                    	Network minimum Bandwith
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: hardware_queue_limit_bytes
                                    
                                    	Hardware queue limit in bytes
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: hardware_queue_limit_microseconds
                                    
                                    	Hardware queue limit in microseconds
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: microsecond
                                    
                                    .. attribute:: policer_bucket_id
                                    
                                    	PolicerBucketID
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: policer_stats_handle
                                    
                                    	PolicerStatsHandle
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: hardware_policer_average_rate_kbps
                                    
                                    	Hardware policer average in kbps
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**units**\: kbit/s
                                    
                                    .. attribute:: hardware_policer_peak_rate_kbps
                                    
                                    	Hardware policer peak rate
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: hardware_policer_conform_burst_bytes
                                    
                                    	Hardware policer conform burst
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: hardware_policer_excess_burst_bytes
                                    
                                    	Hardware policer excess burst
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: ip_mark
                                    
                                    	IP mark
                                    	**type**\: list of  		 :py:class:`IpMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.IpMark>`
                                    
                                    .. attribute:: common_mark
                                    
                                    	Common mark
                                    	**type**\: list of  		 :py:class:`CommonMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.CommonMark>`
                                    
                                    .. attribute:: mpls_mark
                                    
                                    	MPLS mark
                                    	**type**\: list of  		 :py:class:`MplsMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.MplsMark>`
                                    
                                    .. attribute:: wred
                                    
                                    	WRED parameters
                                    	**type**\: list of  		 :py:class:`Wred <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.Wred>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class, self).__init__()

                                        self.yang_name = "class"
                                        self.yang_parent_name = "class-table"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['level_one_class_name']
                                        self._child_classes = OrderedDict([("config-max-rate", ("config_max_rate", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigMaxRate)), ("config-min-rate", ("config_min_rate", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigMinRate)), ("config-queue-limit", ("config_queue_limit", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigQueueLimit)), ("config-policer-average-rate", ("config_policer_average_rate", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigPolicerAverageRate)), ("config-policer-peak-rate", ("config_policer_peak_rate", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigPolicerPeakRate)), ("config-policer-conform-burst", ("config_policer_conform_burst", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigPolicerConformBurst)), ("config-policer-excess-burst", ("config_policer_excess_burst", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigPolicerExcessBurst)), ("conform-action", ("conform_action", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ConformAction)), ("exceed-action", ("exceed_action", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ExceedAction)), ("violate-action", ("violate_action", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ViolateAction)), ("ip-mark", ("ip_mark", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.IpMark)), ("common-mark", ("common_mark", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.CommonMark)), ("mpls-mark", ("mpls_mark", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.MplsMark)), ("wred", ("wred", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.Wred))])
                                        self._leafs = OrderedDict([
                                            ('level_one_class_name', (YLeaf(YType.str, 'level-one-class-name'), ['str'])),
                                            ('level_two_class_name', (YLeaf(YType.str, 'level-two-class-name'), ['str'])),
                                            ('class_level', (YLeaf(YType.enumeration, 'class-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowLevel', '')])),
                                            ('egress_queue_id', (YLeaf(YType.int32, 'egress-queue-id'), ['int'])),
                                            ('queue_type', (YLeaf(YType.enumeration, 'queue-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowQueue', '')])),
                                            ('priority_level', (YLeaf(YType.enumeration, 'priority-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowHpLevel', '')])),
                                            ('hardware_max_rate_kbps', (YLeaf(YType.uint32, 'hardware-max-rate-kbps'), ['int'])),
                                            ('hardware_min_rate_kbps', (YLeaf(YType.uint32, 'hardware-min-rate-kbps'), ['int'])),
                                            ('config_excess_bandwidth_percent', (YLeaf(YType.uint32, 'config-excess-bandwidth-percent'), ['int'])),
                                            ('config_excess_bandwidth_unit', (YLeaf(YType.uint32, 'config-excess-bandwidth-unit'), ['int'])),
                                            ('hardware_excess_bandwidth_weight', (YLeaf(YType.uint32, 'hardware-excess-bandwidth-weight'), ['int'])),
                                            ('network_min_bandwidth_kbps', (YLeaf(YType.uint32, 'network-min-bandwidth-kbps'), ['int'])),
                                            ('hardware_queue_limit_bytes', (YLeaf(YType.uint64, 'hardware-queue-limit-bytes'), ['int'])),
                                            ('hardware_queue_limit_microseconds', (YLeaf(YType.uint64, 'hardware-queue-limit-microseconds'), ['int'])),
                                            ('policer_bucket_id', (YLeaf(YType.uint32, 'policer-bucket-id'), ['int'])),
                                            ('policer_stats_handle', (YLeaf(YType.uint64, 'policer-stats-handle'), ['int'])),
                                            ('hardware_policer_average_rate_kbps', (YLeaf(YType.uint32, 'hardware-policer-average-rate-kbps'), ['int'])),
                                            ('hardware_policer_peak_rate_kbps', (YLeaf(YType.uint32, 'hardware-policer-peak-rate-kbps'), ['int'])),
                                            ('hardware_policer_conform_burst_bytes', (YLeaf(YType.uint32, 'hardware-policer-conform-burst-bytes'), ['int'])),
                                            ('hardware_policer_excess_burst_bytes', (YLeaf(YType.uint32, 'hardware-policer-excess-burst-bytes'), ['int'])),
                                        ])
                                        self.level_one_class_name = None
                                        self.level_two_class_name = None
                                        self.class_level = None
                                        self.egress_queue_id = None
                                        self.queue_type = None
                                        self.priority_level = None
                                        self.hardware_max_rate_kbps = None
                                        self.hardware_min_rate_kbps = None
                                        self.config_excess_bandwidth_percent = None
                                        self.config_excess_bandwidth_unit = None
                                        self.hardware_excess_bandwidth_weight = None
                                        self.network_min_bandwidth_kbps = None
                                        self.hardware_queue_limit_bytes = None
                                        self.hardware_queue_limit_microseconds = None
                                        self.policer_bucket_id = None
                                        self.policer_stats_handle = None
                                        self.hardware_policer_average_rate_kbps = None
                                        self.hardware_policer_peak_rate_kbps = None
                                        self.hardware_policer_conform_burst_bytes = None
                                        self.hardware_policer_excess_burst_bytes = None

                                        self.config_max_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigMaxRate()
                                        self.config_max_rate.parent = self
                                        self._children_name_map["config_max_rate"] = "config-max-rate"

                                        self.config_min_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigMinRate()
                                        self.config_min_rate.parent = self
                                        self._children_name_map["config_min_rate"] = "config-min-rate"

                                        self.config_queue_limit = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigQueueLimit()
                                        self.config_queue_limit.parent = self
                                        self._children_name_map["config_queue_limit"] = "config-queue-limit"

                                        self.config_policer_average_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigPolicerAverageRate()
                                        self.config_policer_average_rate.parent = self
                                        self._children_name_map["config_policer_average_rate"] = "config-policer-average-rate"

                                        self.config_policer_peak_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigPolicerPeakRate()
                                        self.config_policer_peak_rate.parent = self
                                        self._children_name_map["config_policer_peak_rate"] = "config-policer-peak-rate"

                                        self.config_policer_conform_burst = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigPolicerConformBurst()
                                        self.config_policer_conform_burst.parent = self
                                        self._children_name_map["config_policer_conform_burst"] = "config-policer-conform-burst"

                                        self.config_policer_excess_burst = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigPolicerExcessBurst()
                                        self.config_policer_excess_burst.parent = self
                                        self._children_name_map["config_policer_excess_burst"] = "config-policer-excess-burst"

                                        self.conform_action = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ConformAction()
                                        self.conform_action.parent = self
                                        self._children_name_map["conform_action"] = "conform-action"

                                        self.exceed_action = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ExceedAction()
                                        self.exceed_action.parent = self
                                        self._children_name_map["exceed_action"] = "exceed-action"

                                        self.violate_action = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ViolateAction()
                                        self.violate_action.parent = self
                                        self._children_name_map["violate_action"] = "violate-action"

                                        self.ip_mark = YList(self)
                                        self.common_mark = YList(self)
                                        self.mpls_mark = YList(self)
                                        self.wred = YList(self)
                                        self._segment_path = lambda: "class" + "[level-one-class-name='" + str(self.level_one_class_name) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class, ['level_one_class_name', 'level_two_class_name', u'class_level', u'egress_queue_id', u'queue_type', u'priority_level', u'hardware_max_rate_kbps', u'hardware_min_rate_kbps', u'config_excess_bandwidth_percent', u'config_excess_bandwidth_unit', u'hardware_excess_bandwidth_weight', u'network_min_bandwidth_kbps', u'hardware_queue_limit_bytes', u'hardware_queue_limit_microseconds', u'policer_bucket_id', u'policer_stats_handle', u'hardware_policer_average_rate_kbps', u'hardware_policer_peak_rate_kbps', u'hardware_policer_conform_burst_bytes', u'hardware_policer_excess_burst_bytes'], name, value)


                                    class ConfigMaxRate(Entity):
                                        """
                                        Configured maximum rate
                                        
                                        .. attribute:: policy_value
                                        
                                        	Policy value
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: policy_unit
                                        
                                        	Policy unit
                                        	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigMaxRate, self).__init__()

                                            self.yang_name = "config-max-rate"
                                            self.yang_parent_name = "class"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                                ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                            ])
                                            self.policy_value = None
                                            self.policy_unit = None
                                            self._segment_path = lambda: "config-max-rate"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigMaxRate, [u'policy_value', u'policy_unit'], name, value)


                                    class ConfigMinRate(Entity):
                                        """
                                        Configured minimum rate
                                        
                                        .. attribute:: policy_value
                                        
                                        	Policy value
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: policy_unit
                                        
                                        	Policy unit
                                        	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigMinRate, self).__init__()

                                            self.yang_name = "config-min-rate"
                                            self.yang_parent_name = "class"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                                ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                            ])
                                            self.policy_value = None
                                            self.policy_unit = None
                                            self._segment_path = lambda: "config-min-rate"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigMinRate, [u'policy_value', u'policy_unit'], name, value)


                                    class ConfigQueueLimit(Entity):
                                        """
                                        Configured queue limit
                                        
                                        .. attribute:: policy_value
                                        
                                        	Policy value
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: policy_unit
                                        
                                        	Policy unit
                                        	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigQueueLimit, self).__init__()

                                            self.yang_name = "config-queue-limit"
                                            self.yang_parent_name = "class"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                                ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                            ])
                                            self.policy_value = None
                                            self.policy_unit = None
                                            self._segment_path = lambda: "config-queue-limit"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigQueueLimit, [u'policy_value', u'policy_unit'], name, value)


                                    class ConfigPolicerAverageRate(Entity):
                                        """
                                        Configured policer average rate
                                        
                                        .. attribute:: policy_value
                                        
                                        	Policy value
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: policy_unit
                                        
                                        	Policy unit
                                        	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigPolicerAverageRate, self).__init__()

                                            self.yang_name = "config-policer-average-rate"
                                            self.yang_parent_name = "class"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                                ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                            ])
                                            self.policy_value = None
                                            self.policy_unit = None
                                            self._segment_path = lambda: "config-policer-average-rate"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigPolicerAverageRate, [u'policy_value', u'policy_unit'], name, value)


                                    class ConfigPolicerPeakRate(Entity):
                                        """
                                        Config policer peak rate
                                        
                                        .. attribute:: policy_value
                                        
                                        	Policy value
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: policy_unit
                                        
                                        	Policy unit
                                        	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigPolicerPeakRate, self).__init__()

                                            self.yang_name = "config-policer-peak-rate"
                                            self.yang_parent_name = "class"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                                ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                            ])
                                            self.policy_value = None
                                            self.policy_unit = None
                                            self._segment_path = lambda: "config-policer-peak-rate"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigPolicerPeakRate, [u'policy_value', u'policy_unit'], name, value)


                                    class ConfigPolicerConformBurst(Entity):
                                        """
                                        Configured policer conform burst
                                        
                                        .. attribute:: policy_value
                                        
                                        	Policy value
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: policy_unit
                                        
                                        	Policy unit
                                        	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigPolicerConformBurst, self).__init__()

                                            self.yang_name = "config-policer-conform-burst"
                                            self.yang_parent_name = "class"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                                ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                            ])
                                            self.policy_value = None
                                            self.policy_unit = None
                                            self._segment_path = lambda: "config-policer-conform-burst"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigPolicerConformBurst, [u'policy_value', u'policy_unit'], name, value)


                                    class ConfigPolicerExcessBurst(Entity):
                                        """
                                        Configured policer excess burst
                                        
                                        .. attribute:: policy_value
                                        
                                        	Policy value
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: policy_unit
                                        
                                        	Policy unit
                                        	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigPolicerExcessBurst, self).__init__()

                                            self.yang_name = "config-policer-excess-burst"
                                            self.yang_parent_name = "class"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                                ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                            ])
                                            self.policy_value = None
                                            self.policy_unit = None
                                            self._segment_path = lambda: "config-policer-excess-burst"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigPolicerExcessBurst, [u'policy_value', u'policy_unit'], name, value)


                                    class ConformAction(Entity):
                                        """
                                        Conform action
                                        
                                        .. attribute:: action_type
                                        
                                        	Policer action type
                                        	**type**\:  :py:class:`DnxQoseaShowAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowAction>`
                                        
                                        .. attribute:: mark
                                        
                                        	Action mark
                                        	**type**\: list of  		 :py:class:`Mark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ConformAction.Mark>`
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ConformAction, self).__init__()

                                            self.yang_name = "conform-action"
                                            self.yang_parent_name = "class"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("mark", ("mark", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ConformAction.Mark))])
                                            self._leafs = OrderedDict([
                                                ('action_type', (YLeaf(YType.enumeration, 'action-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowAction', '')])),
                                            ])
                                            self.action_type = None

                                            self.mark = YList(self)
                                            self._segment_path = lambda: "conform-action"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ConformAction, [u'action_type'], name, value)


                                        class Mark(Entity):
                                            """
                                            Action mark
                                            
                                            .. attribute:: mark_type
                                            
                                            	Mark type
                                            	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                            
                                            .. attribute:: mark_value
                                            
                                            	Mark value
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            

                                            """

                                            _prefix = 'ncs5500-qos-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ConformAction.Mark, self).__init__()

                                                self.yang_name = "mark"
                                                self.yang_parent_name = "conform-action"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                                    ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                                ])
                                                self.mark_type = None
                                                self.mark_value = None
                                                self._segment_path = lambda: "mark"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ConformAction.Mark, [u'mark_type', u'mark_value'], name, value)


                                    class ExceedAction(Entity):
                                        """
                                        Exceed action
                                        
                                        .. attribute:: action_type
                                        
                                        	Policer action type
                                        	**type**\:  :py:class:`DnxQoseaShowAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowAction>`
                                        
                                        .. attribute:: mark
                                        
                                        	Action mark
                                        	**type**\: list of  		 :py:class:`Mark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ExceedAction.Mark>`
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ExceedAction, self).__init__()

                                            self.yang_name = "exceed-action"
                                            self.yang_parent_name = "class"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("mark", ("mark", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ExceedAction.Mark))])
                                            self._leafs = OrderedDict([
                                                ('action_type', (YLeaf(YType.enumeration, 'action-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowAction', '')])),
                                            ])
                                            self.action_type = None

                                            self.mark = YList(self)
                                            self._segment_path = lambda: "exceed-action"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ExceedAction, [u'action_type'], name, value)


                                        class Mark(Entity):
                                            """
                                            Action mark
                                            
                                            .. attribute:: mark_type
                                            
                                            	Mark type
                                            	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                            
                                            .. attribute:: mark_value
                                            
                                            	Mark value
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            

                                            """

                                            _prefix = 'ncs5500-qos-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ExceedAction.Mark, self).__init__()

                                                self.yang_name = "mark"
                                                self.yang_parent_name = "exceed-action"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                                    ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                                ])
                                                self.mark_type = None
                                                self.mark_value = None
                                                self._segment_path = lambda: "mark"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ExceedAction.Mark, [u'mark_type', u'mark_value'], name, value)


                                    class ViolateAction(Entity):
                                        """
                                        Violate action
                                        
                                        .. attribute:: action_type
                                        
                                        	Policer action type
                                        	**type**\:  :py:class:`DnxQoseaShowAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowAction>`
                                        
                                        .. attribute:: mark
                                        
                                        	Action mark
                                        	**type**\: list of  		 :py:class:`Mark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ViolateAction.Mark>`
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ViolateAction, self).__init__()

                                            self.yang_name = "violate-action"
                                            self.yang_parent_name = "class"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("mark", ("mark", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ViolateAction.Mark))])
                                            self._leafs = OrderedDict([
                                                ('action_type', (YLeaf(YType.enumeration, 'action-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowAction', '')])),
                                            ])
                                            self.action_type = None

                                            self.mark = YList(self)
                                            self._segment_path = lambda: "violate-action"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ViolateAction, [u'action_type'], name, value)


                                        class Mark(Entity):
                                            """
                                            Action mark
                                            
                                            .. attribute:: mark_type
                                            
                                            	Mark type
                                            	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                            
                                            .. attribute:: mark_value
                                            
                                            	Mark value
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            

                                            """

                                            _prefix = 'ncs5500-qos-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ViolateAction.Mark, self).__init__()

                                                self.yang_name = "mark"
                                                self.yang_parent_name = "violate-action"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                                    ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                                ])
                                                self.mark_type = None
                                                self.mark_value = None
                                                self._segment_path = lambda: "mark"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.ViolateAction.Mark, [u'mark_type', u'mark_value'], name, value)


                                    class IpMark(Entity):
                                        """
                                        IP mark
                                        
                                        .. attribute:: mark_type
                                        
                                        	Mark type
                                        	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                        
                                        .. attribute:: mark_value
                                        
                                        	Mark value
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.IpMark, self).__init__()

                                            self.yang_name = "ip-mark"
                                            self.yang_parent_name = "class"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                                ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                            ])
                                            self.mark_type = None
                                            self.mark_value = None
                                            self._segment_path = lambda: "ip-mark"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.IpMark, [u'mark_type', u'mark_value'], name, value)


                                    class CommonMark(Entity):
                                        """
                                        Common mark
                                        
                                        .. attribute:: mark_type
                                        
                                        	Mark type
                                        	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                        
                                        .. attribute:: mark_value
                                        
                                        	Mark value
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.CommonMark, self).__init__()

                                            self.yang_name = "common-mark"
                                            self.yang_parent_name = "class"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                                ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                            ])
                                            self.mark_type = None
                                            self.mark_value = None
                                            self._segment_path = lambda: "common-mark"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.CommonMark, [u'mark_type', u'mark_value'], name, value)


                                    class MplsMark(Entity):
                                        """
                                        MPLS mark
                                        
                                        .. attribute:: mark_type
                                        
                                        	Mark type
                                        	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                        
                                        .. attribute:: mark_value
                                        
                                        	Mark value
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.MplsMark, self).__init__()

                                            self.yang_name = "mpls-mark"
                                            self.yang_parent_name = "class"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                                ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                            ])
                                            self.mark_type = None
                                            self.mark_value = None
                                            self._segment_path = lambda: "mpls-mark"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.MplsMark, [u'mark_type', u'mark_value'], name, value)


                                    class Wred(Entity):
                                        """
                                        WRED parameters
                                        
                                        .. attribute:: wred_match_value
                                        
                                        	WRED match values
                                        	**type**\:  :py:class:`WredMatchValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.Wred.WredMatchValue>`
                                        
                                        .. attribute:: config_min_threshold
                                        
                                        	Configured minimum threshold
                                        	**type**\:  :py:class:`ConfigMinThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.Wred.ConfigMinThreshold>`
                                        
                                        .. attribute:: config_max_threshold
                                        
                                        	Configured maximum threshold
                                        	**type**\:  :py:class:`ConfigMaxThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.Wred.ConfigMaxThreshold>`
                                        
                                        .. attribute:: wred_match_type
                                        
                                        	WREDMatchType
                                        	**type**\:  :py:class:`DnxQoseaShowWred <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowWred>`
                                        
                                        .. attribute:: hardware_min_threshold_bytes
                                        
                                        	Hardware minimum threshold
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: hardware_max_threshold_bytes
                                        
                                        	Hardware maximum threshold
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: first_segment
                                        
                                        	First segment
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: segment_size
                                        
                                        	Segment size
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.Wred, self).__init__()

                                            self.yang_name = "wred"
                                            self.yang_parent_name = "class"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("wred-match-value", ("wred_match_value", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.Wred.WredMatchValue)), ("config-min-threshold", ("config_min_threshold", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.Wred.ConfigMinThreshold)), ("config-max-threshold", ("config_max_threshold", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.Wred.ConfigMaxThreshold))])
                                            self._leafs = OrderedDict([
                                                ('wred_match_type', (YLeaf(YType.enumeration, 'wred-match-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowWred', '')])),
                                                ('hardware_min_threshold_bytes', (YLeaf(YType.uint32, 'hardware-min-threshold-bytes'), ['int'])),
                                                ('hardware_max_threshold_bytes', (YLeaf(YType.uint32, 'hardware-max-threshold-bytes'), ['int'])),
                                                ('first_segment', (YLeaf(YType.uint16, 'first-segment'), ['int'])),
                                                ('segment_size', (YLeaf(YType.uint32, 'segment-size'), ['int'])),
                                            ])
                                            self.wred_match_type = None
                                            self.hardware_min_threshold_bytes = None
                                            self.hardware_max_threshold_bytes = None
                                            self.first_segment = None
                                            self.segment_size = None

                                            self.wred_match_value = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.Wred.WredMatchValue()
                                            self.wred_match_value.parent = self
                                            self._children_name_map["wred_match_value"] = "wred-match-value"

                                            self.config_min_threshold = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.Wred.ConfigMinThreshold()
                                            self.config_min_threshold.parent = self
                                            self._children_name_map["config_min_threshold"] = "config-min-threshold"

                                            self.config_max_threshold = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.Wred.ConfigMaxThreshold()
                                            self.config_max_threshold.parent = self
                                            self._children_name_map["config_max_threshold"] = "config-max-threshold"
                                            self._segment_path = lambda: "wred"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.Wred, [u'wred_match_type', u'hardware_min_threshold_bytes', u'hardware_max_threshold_bytes', u'first_segment', u'segment_size'], name, value)


                                        class WredMatchValue(Entity):
                                            """
                                            WRED match values
                                            
                                            .. attribute:: dnx_qosea_show_red_match_value
                                            
                                            	dnx qosea show red match value
                                            	**type**\: list of  		 :py:class:`DnxQoseaShowRedMatchValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue>`
                                            
                                            

                                            """

                                            _prefix = 'ncs5500-qos-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.Wred.WredMatchValue, self).__init__()

                                                self.yang_name = "wred-match-value"
                                                self.yang_parent_name = "wred"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("dnx-qosea-show-red-match-value", ("dnx_qosea_show_red_match_value", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue))])
                                                self._leafs = OrderedDict()

                                                self.dnx_qosea_show_red_match_value = YList(self)
                                                self._segment_path = lambda: "wred-match-value"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.Wred.WredMatchValue, [], name, value)


                                            class DnxQoseaShowRedMatchValue(Entity):
                                                """
                                                dnx qosea show red match value
                                                
                                                .. attribute:: range_start
                                                
                                                	Start value of a range
                                                	**type**\: int
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: range_end
                                                
                                                	End value of a range
                                                	**type**\: int
                                                
                                                	**range:** 0..255
                                                
                                                

                                                """

                                                _prefix = 'ncs5500-qos-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue, self).__init__()

                                                    self.yang_name = "dnx-qosea-show-red-match-value"
                                                    self.yang_parent_name = "wred-match-value"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('range_start', (YLeaf(YType.uint8, 'range-start'), ['int'])),
                                                        ('range_end', (YLeaf(YType.uint8, 'range-end'), ['int'])),
                                                    ])
                                                    self.range_start = None
                                                    self.range_end = None
                                                    self._segment_path = lambda: "dnx-qosea-show-red-match-value"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue, [u'range_start', u'range_end'], name, value)


                                        class ConfigMinThreshold(Entity):
                                            """
                                            Configured minimum threshold
                                            
                                            .. attribute:: policy_value
                                            
                                            	Policy value
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: policy_unit
                                            
                                            	Policy unit
                                            	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                            
                                            

                                            """

                                            _prefix = 'ncs5500-qos-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.Wred.ConfigMinThreshold, self).__init__()

                                                self.yang_name = "config-min-threshold"
                                                self.yang_parent_name = "wred"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                                    ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                                ])
                                                self.policy_value = None
                                                self.policy_unit = None
                                                self._segment_path = lambda: "config-min-threshold"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.Wred.ConfigMinThreshold, [u'policy_value', u'policy_unit'], name, value)


                                        class ConfigMaxThreshold(Entity):
                                            """
                                            Configured maximum threshold
                                            
                                            .. attribute:: policy_value
                                            
                                            	Policy value
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: policy_unit
                                            
                                            	Policy unit
                                            	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                            
                                            

                                            """

                                            _prefix = 'ncs5500-qos-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.Wred.ConfigMaxThreshold, self).__init__()

                                                self.yang_name = "config-max-threshold"
                                                self.yang_parent_name = "wred"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                                    ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                                ])
                                                self.policy_value = None
                                                self.policy_unit = None
                                                self._segment_path = lambda: "config-max-threshold"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.ClassTable.Class.Wred.ConfigMaxThreshold, [u'policy_value', u'policy_unit'], name, value)


                    class ClassTable(Entity):
                        """
                        QoS list of class names
                        
                        .. attribute:: class_
                        
                        	QoS policy class
                        	**type**\: list of  		 :py:class:`Class <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class>`
                        
                        

                        """

                        _prefix = 'ncs5500-qos-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable, self).__init__()

                            self.yang_name = "class-table"
                            self.yang_parent_name = "bundle-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("class", ("class_", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class))])
                            self._leafs = OrderedDict()

                            self.class_ = YList(self)
                            self._segment_path = lambda: "class-table"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable, [], name, value)


                        class Class(Entity):
                            """
                            QoS policy class
                            
                            .. attribute:: level_one_class_name  (key)
                            
                            	QoS policy class name at level 1
                            	**type**\: str
                            
                            .. attribute:: level_two_class_name
                            
                            	QoS policy child class name at level 2
                            	**type**\: str
                            
                            .. attribute:: config_max_rate
                            
                            	Configured maximum rate
                            	**type**\:  :py:class:`ConfigMaxRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ConfigMaxRate>`
                            
                            .. attribute:: config_min_rate
                            
                            	Configured minimum rate
                            	**type**\:  :py:class:`ConfigMinRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ConfigMinRate>`
                            
                            .. attribute:: config_queue_limit
                            
                            	Configured queue limit
                            	**type**\:  :py:class:`ConfigQueueLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ConfigQueueLimit>`
                            
                            .. attribute:: config_policer_average_rate
                            
                            	Configured policer average rate
                            	**type**\:  :py:class:`ConfigPolicerAverageRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ConfigPolicerAverageRate>`
                            
                            .. attribute:: config_policer_peak_rate
                            
                            	Config policer peak rate
                            	**type**\:  :py:class:`ConfigPolicerPeakRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ConfigPolicerPeakRate>`
                            
                            .. attribute:: config_policer_conform_burst
                            
                            	Configured policer conform burst
                            	**type**\:  :py:class:`ConfigPolicerConformBurst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ConfigPolicerConformBurst>`
                            
                            .. attribute:: config_policer_excess_burst
                            
                            	Configured policer excess burst
                            	**type**\:  :py:class:`ConfigPolicerExcessBurst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ConfigPolicerExcessBurst>`
                            
                            .. attribute:: conform_action
                            
                            	Conform action
                            	**type**\:  :py:class:`ConformAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ConformAction>`
                            
                            .. attribute:: exceed_action
                            
                            	Exceed action
                            	**type**\:  :py:class:`ExceedAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ExceedAction>`
                            
                            .. attribute:: violate_action
                            
                            	Violate action
                            	**type**\:  :py:class:`ViolateAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ViolateAction>`
                            
                            .. attribute:: class_level
                            
                            	Class level
                            	**type**\:  :py:class:`DnxQoseaShowLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowLevel>`
                            
                            .. attribute:: egress_queue_id
                            
                            	Egress Queue ID
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: queue_type
                            
                            	Queue type
                            	**type**\:  :py:class:`DnxQoseaShowQueue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowQueue>`
                            
                            .. attribute:: priority_level
                            
                            	Priority level
                            	**type**\:  :py:class:`DnxQoseaShowHpLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowHpLevel>`
                            
                            .. attribute:: hardware_max_rate_kbps
                            
                            	Hardware maximum rate in kbps
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: kbit/s
                            
                            .. attribute:: hardware_min_rate_kbps
                            
                            	Hardware minimum rate in kbps
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: kbit/s
                            
                            .. attribute:: config_excess_bandwidth_percent
                            
                            	Configured excess bandwidth percentage
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: percentage
                            
                            .. attribute:: config_excess_bandwidth_unit
                            
                            	Configured excess bandwidth unit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hardware_excess_bandwidth_weight
                            
                            	Hardware excess bandwidth weight
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: network_min_bandwidth_kbps
                            
                            	Network minimum Bandwith
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hardware_queue_limit_bytes
                            
                            	Hardware queue limit in bytes
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: hardware_queue_limit_microseconds
                            
                            	Hardware queue limit in microseconds
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: microsecond
                            
                            .. attribute:: policer_bucket_id
                            
                            	PolicerBucketID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: policer_stats_handle
                            
                            	PolicerStatsHandle
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: hardware_policer_average_rate_kbps
                            
                            	Hardware policer average in kbps
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: kbit/s
                            
                            .. attribute:: hardware_policer_peak_rate_kbps
                            
                            	Hardware policer peak rate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hardware_policer_conform_burst_bytes
                            
                            	Hardware policer conform burst
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hardware_policer_excess_burst_bytes
                            
                            	Hardware policer excess burst
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ip_mark
                            
                            	IP mark
                            	**type**\: list of  		 :py:class:`IpMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.IpMark>`
                            
                            .. attribute:: common_mark
                            
                            	Common mark
                            	**type**\: list of  		 :py:class:`CommonMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.CommonMark>`
                            
                            .. attribute:: mpls_mark
                            
                            	MPLS mark
                            	**type**\: list of  		 :py:class:`MplsMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.MplsMark>`
                            
                            .. attribute:: wred
                            
                            	WRED parameters
                            	**type**\: list of  		 :py:class:`Wred <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.Wred>`
                            
                            

                            """

                            _prefix = 'ncs5500-qos-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class, self).__init__()

                                self.yang_name = "class"
                                self.yang_parent_name = "class-table"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['level_one_class_name']
                                self._child_classes = OrderedDict([("config-max-rate", ("config_max_rate", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ConfigMaxRate)), ("config-min-rate", ("config_min_rate", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ConfigMinRate)), ("config-queue-limit", ("config_queue_limit", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ConfigQueueLimit)), ("config-policer-average-rate", ("config_policer_average_rate", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ConfigPolicerAverageRate)), ("config-policer-peak-rate", ("config_policer_peak_rate", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ConfigPolicerPeakRate)), ("config-policer-conform-burst", ("config_policer_conform_burst", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ConfigPolicerConformBurst)), ("config-policer-excess-burst", ("config_policer_excess_burst", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ConfigPolicerExcessBurst)), ("conform-action", ("conform_action", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ConformAction)), ("exceed-action", ("exceed_action", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ExceedAction)), ("violate-action", ("violate_action", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ViolateAction)), ("ip-mark", ("ip_mark", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.IpMark)), ("common-mark", ("common_mark", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.CommonMark)), ("mpls-mark", ("mpls_mark", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.MplsMark)), ("wred", ("wred", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.Wred))])
                                self._leafs = OrderedDict([
                                    ('level_one_class_name', (YLeaf(YType.str, 'level-one-class-name'), ['str'])),
                                    ('level_two_class_name', (YLeaf(YType.str, 'level-two-class-name'), ['str'])),
                                    ('class_level', (YLeaf(YType.enumeration, 'class-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowLevel', '')])),
                                    ('egress_queue_id', (YLeaf(YType.int32, 'egress-queue-id'), ['int'])),
                                    ('queue_type', (YLeaf(YType.enumeration, 'queue-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowQueue', '')])),
                                    ('priority_level', (YLeaf(YType.enumeration, 'priority-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowHpLevel', '')])),
                                    ('hardware_max_rate_kbps', (YLeaf(YType.uint32, 'hardware-max-rate-kbps'), ['int'])),
                                    ('hardware_min_rate_kbps', (YLeaf(YType.uint32, 'hardware-min-rate-kbps'), ['int'])),
                                    ('config_excess_bandwidth_percent', (YLeaf(YType.uint32, 'config-excess-bandwidth-percent'), ['int'])),
                                    ('config_excess_bandwidth_unit', (YLeaf(YType.uint32, 'config-excess-bandwidth-unit'), ['int'])),
                                    ('hardware_excess_bandwidth_weight', (YLeaf(YType.uint32, 'hardware-excess-bandwidth-weight'), ['int'])),
                                    ('network_min_bandwidth_kbps', (YLeaf(YType.uint32, 'network-min-bandwidth-kbps'), ['int'])),
                                    ('hardware_queue_limit_bytes', (YLeaf(YType.uint64, 'hardware-queue-limit-bytes'), ['int'])),
                                    ('hardware_queue_limit_microseconds', (YLeaf(YType.uint64, 'hardware-queue-limit-microseconds'), ['int'])),
                                    ('policer_bucket_id', (YLeaf(YType.uint32, 'policer-bucket-id'), ['int'])),
                                    ('policer_stats_handle', (YLeaf(YType.uint64, 'policer-stats-handle'), ['int'])),
                                    ('hardware_policer_average_rate_kbps', (YLeaf(YType.uint32, 'hardware-policer-average-rate-kbps'), ['int'])),
                                    ('hardware_policer_peak_rate_kbps', (YLeaf(YType.uint32, 'hardware-policer-peak-rate-kbps'), ['int'])),
                                    ('hardware_policer_conform_burst_bytes', (YLeaf(YType.uint32, 'hardware-policer-conform-burst-bytes'), ['int'])),
                                    ('hardware_policer_excess_burst_bytes', (YLeaf(YType.uint32, 'hardware-policer-excess-burst-bytes'), ['int'])),
                                ])
                                self.level_one_class_name = None
                                self.level_two_class_name = None
                                self.class_level = None
                                self.egress_queue_id = None
                                self.queue_type = None
                                self.priority_level = None
                                self.hardware_max_rate_kbps = None
                                self.hardware_min_rate_kbps = None
                                self.config_excess_bandwidth_percent = None
                                self.config_excess_bandwidth_unit = None
                                self.hardware_excess_bandwidth_weight = None
                                self.network_min_bandwidth_kbps = None
                                self.hardware_queue_limit_bytes = None
                                self.hardware_queue_limit_microseconds = None
                                self.policer_bucket_id = None
                                self.policer_stats_handle = None
                                self.hardware_policer_average_rate_kbps = None
                                self.hardware_policer_peak_rate_kbps = None
                                self.hardware_policer_conform_burst_bytes = None
                                self.hardware_policer_excess_burst_bytes = None

                                self.config_max_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ConfigMaxRate()
                                self.config_max_rate.parent = self
                                self._children_name_map["config_max_rate"] = "config-max-rate"

                                self.config_min_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ConfigMinRate()
                                self.config_min_rate.parent = self
                                self._children_name_map["config_min_rate"] = "config-min-rate"

                                self.config_queue_limit = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ConfigQueueLimit()
                                self.config_queue_limit.parent = self
                                self._children_name_map["config_queue_limit"] = "config-queue-limit"

                                self.config_policer_average_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ConfigPolicerAverageRate()
                                self.config_policer_average_rate.parent = self
                                self._children_name_map["config_policer_average_rate"] = "config-policer-average-rate"

                                self.config_policer_peak_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ConfigPolicerPeakRate()
                                self.config_policer_peak_rate.parent = self
                                self._children_name_map["config_policer_peak_rate"] = "config-policer-peak-rate"

                                self.config_policer_conform_burst = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ConfigPolicerConformBurst()
                                self.config_policer_conform_burst.parent = self
                                self._children_name_map["config_policer_conform_burst"] = "config-policer-conform-burst"

                                self.config_policer_excess_burst = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ConfigPolicerExcessBurst()
                                self.config_policer_excess_burst.parent = self
                                self._children_name_map["config_policer_excess_burst"] = "config-policer-excess-burst"

                                self.conform_action = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ConformAction()
                                self.conform_action.parent = self
                                self._children_name_map["conform_action"] = "conform-action"

                                self.exceed_action = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ExceedAction()
                                self.exceed_action.parent = self
                                self._children_name_map["exceed_action"] = "exceed-action"

                                self.violate_action = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ViolateAction()
                                self.violate_action.parent = self
                                self._children_name_map["violate_action"] = "violate-action"

                                self.ip_mark = YList(self)
                                self.common_mark = YList(self)
                                self.mpls_mark = YList(self)
                                self.wred = YList(self)
                                self._segment_path = lambda: "class" + "[level-one-class-name='" + str(self.level_one_class_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class, ['level_one_class_name', 'level_two_class_name', u'class_level', u'egress_queue_id', u'queue_type', u'priority_level', u'hardware_max_rate_kbps', u'hardware_min_rate_kbps', u'config_excess_bandwidth_percent', u'config_excess_bandwidth_unit', u'hardware_excess_bandwidth_weight', u'network_min_bandwidth_kbps', u'hardware_queue_limit_bytes', u'hardware_queue_limit_microseconds', u'policer_bucket_id', u'policer_stats_handle', u'hardware_policer_average_rate_kbps', u'hardware_policer_peak_rate_kbps', u'hardware_policer_conform_burst_bytes', u'hardware_policer_excess_burst_bytes'], name, value)


                            class ConfigMaxRate(Entity):
                                """
                                Configured maximum rate
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ConfigMaxRate, self).__init__()

                                    self.yang_name = "config-max-rate"
                                    self.yang_parent_name = "class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                        ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                    ])
                                    self.policy_value = None
                                    self.policy_unit = None
                                    self._segment_path = lambda: "config-max-rate"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ConfigMaxRate, [u'policy_value', u'policy_unit'], name, value)


                            class ConfigMinRate(Entity):
                                """
                                Configured minimum rate
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ConfigMinRate, self).__init__()

                                    self.yang_name = "config-min-rate"
                                    self.yang_parent_name = "class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                        ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                    ])
                                    self.policy_value = None
                                    self.policy_unit = None
                                    self._segment_path = lambda: "config-min-rate"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ConfigMinRate, [u'policy_value', u'policy_unit'], name, value)


                            class ConfigQueueLimit(Entity):
                                """
                                Configured queue limit
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ConfigQueueLimit, self).__init__()

                                    self.yang_name = "config-queue-limit"
                                    self.yang_parent_name = "class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                        ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                    ])
                                    self.policy_value = None
                                    self.policy_unit = None
                                    self._segment_path = lambda: "config-queue-limit"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ConfigQueueLimit, [u'policy_value', u'policy_unit'], name, value)


                            class ConfigPolicerAverageRate(Entity):
                                """
                                Configured policer average rate
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ConfigPolicerAverageRate, self).__init__()

                                    self.yang_name = "config-policer-average-rate"
                                    self.yang_parent_name = "class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                        ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                    ])
                                    self.policy_value = None
                                    self.policy_unit = None
                                    self._segment_path = lambda: "config-policer-average-rate"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ConfigPolicerAverageRate, [u'policy_value', u'policy_unit'], name, value)


                            class ConfigPolicerPeakRate(Entity):
                                """
                                Config policer peak rate
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ConfigPolicerPeakRate, self).__init__()

                                    self.yang_name = "config-policer-peak-rate"
                                    self.yang_parent_name = "class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                        ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                    ])
                                    self.policy_value = None
                                    self.policy_unit = None
                                    self._segment_path = lambda: "config-policer-peak-rate"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ConfigPolicerPeakRate, [u'policy_value', u'policy_unit'], name, value)


                            class ConfigPolicerConformBurst(Entity):
                                """
                                Configured policer conform burst
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ConfigPolicerConformBurst, self).__init__()

                                    self.yang_name = "config-policer-conform-burst"
                                    self.yang_parent_name = "class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                        ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                    ])
                                    self.policy_value = None
                                    self.policy_unit = None
                                    self._segment_path = lambda: "config-policer-conform-burst"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ConfigPolicerConformBurst, [u'policy_value', u'policy_unit'], name, value)


                            class ConfigPolicerExcessBurst(Entity):
                                """
                                Configured policer excess burst
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ConfigPolicerExcessBurst, self).__init__()

                                    self.yang_name = "config-policer-excess-burst"
                                    self.yang_parent_name = "class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                        ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                    ])
                                    self.policy_value = None
                                    self.policy_unit = None
                                    self._segment_path = lambda: "config-policer-excess-burst"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ConfigPolicerExcessBurst, [u'policy_value', u'policy_unit'], name, value)


                            class ConformAction(Entity):
                                """
                                Conform action
                                
                                .. attribute:: action_type
                                
                                	Policer action type
                                	**type**\:  :py:class:`DnxQoseaShowAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowAction>`
                                
                                .. attribute:: mark
                                
                                	Action mark
                                	**type**\: list of  		 :py:class:`Mark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ConformAction.Mark>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ConformAction, self).__init__()

                                    self.yang_name = "conform-action"
                                    self.yang_parent_name = "class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("mark", ("mark", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ConformAction.Mark))])
                                    self._leafs = OrderedDict([
                                        ('action_type', (YLeaf(YType.enumeration, 'action-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowAction', '')])),
                                    ])
                                    self.action_type = None

                                    self.mark = YList(self)
                                    self._segment_path = lambda: "conform-action"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ConformAction, [u'action_type'], name, value)


                                class Mark(Entity):
                                    """
                                    Action mark
                                    
                                    .. attribute:: mark_type
                                    
                                    	Mark type
                                    	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                    
                                    .. attribute:: mark_value
                                    
                                    	Mark value
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ConformAction.Mark, self).__init__()

                                        self.yang_name = "mark"
                                        self.yang_parent_name = "conform-action"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                            ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                        ])
                                        self.mark_type = None
                                        self.mark_value = None
                                        self._segment_path = lambda: "mark"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ConformAction.Mark, [u'mark_type', u'mark_value'], name, value)


                            class ExceedAction(Entity):
                                """
                                Exceed action
                                
                                .. attribute:: action_type
                                
                                	Policer action type
                                	**type**\:  :py:class:`DnxQoseaShowAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowAction>`
                                
                                .. attribute:: mark
                                
                                	Action mark
                                	**type**\: list of  		 :py:class:`Mark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ExceedAction.Mark>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ExceedAction, self).__init__()

                                    self.yang_name = "exceed-action"
                                    self.yang_parent_name = "class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("mark", ("mark", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ExceedAction.Mark))])
                                    self._leafs = OrderedDict([
                                        ('action_type', (YLeaf(YType.enumeration, 'action-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowAction', '')])),
                                    ])
                                    self.action_type = None

                                    self.mark = YList(self)
                                    self._segment_path = lambda: "exceed-action"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ExceedAction, [u'action_type'], name, value)


                                class Mark(Entity):
                                    """
                                    Action mark
                                    
                                    .. attribute:: mark_type
                                    
                                    	Mark type
                                    	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                    
                                    .. attribute:: mark_value
                                    
                                    	Mark value
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ExceedAction.Mark, self).__init__()

                                        self.yang_name = "mark"
                                        self.yang_parent_name = "exceed-action"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                            ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                        ])
                                        self.mark_type = None
                                        self.mark_value = None
                                        self._segment_path = lambda: "mark"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ExceedAction.Mark, [u'mark_type', u'mark_value'], name, value)


                            class ViolateAction(Entity):
                                """
                                Violate action
                                
                                .. attribute:: action_type
                                
                                	Policer action type
                                	**type**\:  :py:class:`DnxQoseaShowAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowAction>`
                                
                                .. attribute:: mark
                                
                                	Action mark
                                	**type**\: list of  		 :py:class:`Mark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ViolateAction.Mark>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ViolateAction, self).__init__()

                                    self.yang_name = "violate-action"
                                    self.yang_parent_name = "class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("mark", ("mark", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ViolateAction.Mark))])
                                    self._leafs = OrderedDict([
                                        ('action_type', (YLeaf(YType.enumeration, 'action-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowAction', '')])),
                                    ])
                                    self.action_type = None

                                    self.mark = YList(self)
                                    self._segment_path = lambda: "violate-action"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ViolateAction, [u'action_type'], name, value)


                                class Mark(Entity):
                                    """
                                    Action mark
                                    
                                    .. attribute:: mark_type
                                    
                                    	Mark type
                                    	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                    
                                    .. attribute:: mark_value
                                    
                                    	Mark value
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ViolateAction.Mark, self).__init__()

                                        self.yang_name = "mark"
                                        self.yang_parent_name = "violate-action"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                            ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                        ])
                                        self.mark_type = None
                                        self.mark_value = None
                                        self._segment_path = lambda: "mark"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.ViolateAction.Mark, [u'mark_type', u'mark_value'], name, value)


                            class IpMark(Entity):
                                """
                                IP mark
                                
                                .. attribute:: mark_type
                                
                                	Mark type
                                	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                
                                .. attribute:: mark_value
                                
                                	Mark value
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.IpMark, self).__init__()

                                    self.yang_name = "ip-mark"
                                    self.yang_parent_name = "class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                        ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                    ])
                                    self.mark_type = None
                                    self.mark_value = None
                                    self._segment_path = lambda: "ip-mark"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.IpMark, [u'mark_type', u'mark_value'], name, value)


                            class CommonMark(Entity):
                                """
                                Common mark
                                
                                .. attribute:: mark_type
                                
                                	Mark type
                                	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                
                                .. attribute:: mark_value
                                
                                	Mark value
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.CommonMark, self).__init__()

                                    self.yang_name = "common-mark"
                                    self.yang_parent_name = "class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                        ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                    ])
                                    self.mark_type = None
                                    self.mark_value = None
                                    self._segment_path = lambda: "common-mark"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.CommonMark, [u'mark_type', u'mark_value'], name, value)


                            class MplsMark(Entity):
                                """
                                MPLS mark
                                
                                .. attribute:: mark_type
                                
                                	Mark type
                                	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                
                                .. attribute:: mark_value
                                
                                	Mark value
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.MplsMark, self).__init__()

                                    self.yang_name = "mpls-mark"
                                    self.yang_parent_name = "class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                        ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                    ])
                                    self.mark_type = None
                                    self.mark_value = None
                                    self._segment_path = lambda: "mpls-mark"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.MplsMark, [u'mark_type', u'mark_value'], name, value)


                            class Wred(Entity):
                                """
                                WRED parameters
                                
                                .. attribute:: wred_match_value
                                
                                	WRED match values
                                	**type**\:  :py:class:`WredMatchValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.Wred.WredMatchValue>`
                                
                                .. attribute:: config_min_threshold
                                
                                	Configured minimum threshold
                                	**type**\:  :py:class:`ConfigMinThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.Wred.ConfigMinThreshold>`
                                
                                .. attribute:: config_max_threshold
                                
                                	Configured maximum threshold
                                	**type**\:  :py:class:`ConfigMaxThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.Wred.ConfigMaxThreshold>`
                                
                                .. attribute:: wred_match_type
                                
                                	WREDMatchType
                                	**type**\:  :py:class:`DnxQoseaShowWred <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowWred>`
                                
                                .. attribute:: hardware_min_threshold_bytes
                                
                                	Hardware minimum threshold
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: hardware_max_threshold_bytes
                                
                                	Hardware maximum threshold
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: first_segment
                                
                                	First segment
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: segment_size
                                
                                	Segment size
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.Wred, self).__init__()

                                    self.yang_name = "wred"
                                    self.yang_parent_name = "class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("wred-match-value", ("wred_match_value", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.Wred.WredMatchValue)), ("config-min-threshold", ("config_min_threshold", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.Wred.ConfigMinThreshold)), ("config-max-threshold", ("config_max_threshold", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.Wred.ConfigMaxThreshold))])
                                    self._leafs = OrderedDict([
                                        ('wred_match_type', (YLeaf(YType.enumeration, 'wred-match-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowWred', '')])),
                                        ('hardware_min_threshold_bytes', (YLeaf(YType.uint32, 'hardware-min-threshold-bytes'), ['int'])),
                                        ('hardware_max_threshold_bytes', (YLeaf(YType.uint32, 'hardware-max-threshold-bytes'), ['int'])),
                                        ('first_segment', (YLeaf(YType.uint16, 'first-segment'), ['int'])),
                                        ('segment_size', (YLeaf(YType.uint32, 'segment-size'), ['int'])),
                                    ])
                                    self.wred_match_type = None
                                    self.hardware_min_threshold_bytes = None
                                    self.hardware_max_threshold_bytes = None
                                    self.first_segment = None
                                    self.segment_size = None

                                    self.wred_match_value = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.Wred.WredMatchValue()
                                    self.wred_match_value.parent = self
                                    self._children_name_map["wred_match_value"] = "wred-match-value"

                                    self.config_min_threshold = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.Wred.ConfigMinThreshold()
                                    self.config_min_threshold.parent = self
                                    self._children_name_map["config_min_threshold"] = "config-min-threshold"

                                    self.config_max_threshold = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.Wred.ConfigMaxThreshold()
                                    self.config_max_threshold.parent = self
                                    self._children_name_map["config_max_threshold"] = "config-max-threshold"
                                    self._segment_path = lambda: "wred"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.Wred, [u'wred_match_type', u'hardware_min_threshold_bytes', u'hardware_max_threshold_bytes', u'first_segment', u'segment_size'], name, value)


                                class WredMatchValue(Entity):
                                    """
                                    WRED match values
                                    
                                    .. attribute:: dnx_qosea_show_red_match_value
                                    
                                    	dnx qosea show red match value
                                    	**type**\: list of  		 :py:class:`DnxQoseaShowRedMatchValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.Wred.WredMatchValue, self).__init__()

                                        self.yang_name = "wred-match-value"
                                        self.yang_parent_name = "wred"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("dnx-qosea-show-red-match-value", ("dnx_qosea_show_red_match_value", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue))])
                                        self._leafs = OrderedDict()

                                        self.dnx_qosea_show_red_match_value = YList(self)
                                        self._segment_path = lambda: "wred-match-value"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.Wred.WredMatchValue, [], name, value)


                                    class DnxQoseaShowRedMatchValue(Entity):
                                        """
                                        dnx qosea show red match value
                                        
                                        .. attribute:: range_start
                                        
                                        	Start value of a range
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: range_end
                                        
                                        	End value of a range
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue, self).__init__()

                                            self.yang_name = "dnx-qosea-show-red-match-value"
                                            self.yang_parent_name = "wred-match-value"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('range_start', (YLeaf(YType.uint8, 'range-start'), ['int'])),
                                                ('range_end', (YLeaf(YType.uint8, 'range-end'), ['int'])),
                                            ])
                                            self.range_start = None
                                            self.range_end = None
                                            self._segment_path = lambda: "dnx-qosea-show-red-match-value"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue, [u'range_start', u'range_end'], name, value)


                                class ConfigMinThreshold(Entity):
                                    """
                                    Configured minimum threshold
                                    
                                    .. attribute:: policy_value
                                    
                                    	Policy value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: policy_unit
                                    
                                    	Policy unit
                                    	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.Wred.ConfigMinThreshold, self).__init__()

                                        self.yang_name = "config-min-threshold"
                                        self.yang_parent_name = "wred"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                            ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                        ])
                                        self.policy_value = None
                                        self.policy_unit = None
                                        self._segment_path = lambda: "config-min-threshold"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.Wred.ConfigMinThreshold, [u'policy_value', u'policy_unit'], name, value)


                                class ConfigMaxThreshold(Entity):
                                    """
                                    Configured maximum threshold
                                    
                                    .. attribute:: policy_value
                                    
                                    	Policy value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: policy_unit
                                    
                                    	Policy unit
                                    	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.Wred.ConfigMaxThreshold, self).__init__()

                                        self.yang_name = "config-max-threshold"
                                        self.yang_parent_name = "wred"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                            ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                        ])
                                        self.policy_value = None
                                        self.policy_unit = None
                                        self._segment_path = lambda: "config-max-threshold"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.ClassTable.Class.Wred.ConfigMaxThreshold, [u'policy_value', u'policy_unit'], name, value)


            class Interfaces(Entity):
                """
                QoS list of interfaces
                
                .. attribute:: interface
                
                	QoS interface names
                	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'ncs5500-qos-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PlatformQos.Nodes.Node.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface", ("interface", PlatformQos.Nodes.Node.Interfaces.Interface))])
                    self._leafs = OrderedDict()

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PlatformQos.Nodes.Node.Interfaces, [], name, value)


                class Interface(Entity):
                    """
                    QoS interface names
                    
                    .. attribute:: interface_name  (key)
                    
                    	The name of the interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: policy_details
                    
                    	Policy Details
                    	**type**\:  :py:class:`PolicyDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.PolicyDetails>`
                    
                    .. attribute:: output
                    
                    	QoS policy direction egress
                    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output>`
                    
                    .. attribute:: class_table
                    
                    	QoS list of class names
                    	**type**\:  :py:class:`ClassTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable>`
                    
                    

                    """

                    _prefix = 'ncs5500-qos-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PlatformQos.Nodes.Node.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([("policy-details", ("policy_details", PlatformQos.Nodes.Node.Interfaces.Interface.PolicyDetails)), ("output", ("output", PlatformQos.Nodes.Node.Interfaces.Interface.Output)), ("class-table", ("class_table", PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ])
                        self.interface_name = None

                        self.policy_details = PlatformQos.Nodes.Node.Interfaces.Interface.PolicyDetails()
                        self.policy_details.parent = self
                        self._children_name_map["policy_details"] = "policy-details"

                        self.output = PlatformQos.Nodes.Node.Interfaces.Interface.Output()
                        self.output.parent = self
                        self._children_name_map["output"] = "output"

                        self.class_table = PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable()
                        self.class_table.parent = self
                        self._children_name_map["class_table"] = "class-table"
                        self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface, ['interface_name'], name, value)


                    class PolicyDetails(Entity):
                        """
                        Policy Details
                        
                        .. attribute:: npu_id
                        
                        	NPU ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: interface_handle
                        
                        	InterfaceHandle
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: interface_bandwidth_kbps
                        
                        	Interface Bandwidth (in kbps)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: kbit/s
                        
                        .. attribute:: policy_name
                        
                        	Policy name
                        	**type**\: str
                        
                        	**length:** 0..64
                        
                        .. attribute:: total_number_of_classes
                        
                        	Number of Classes
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: voq_base_address
                        
                        	VOQ base address
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: voq_stats_handle
                        
                        	VOQ stats handle
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: stats_accounting_type
                        
                        	QoS Statistics Accounting Type
                        	**type**\:  :py:class:`QosPolicyAccountEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.QosPolicyAccountEnum>`
                        
                        .. attribute:: policy_status
                        
                        	Policy Status
                        	**type**\:  :py:class:`DnxQoseaShowPolicyStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowPolicyStatus>`
                        
                        .. attribute:: interface_status
                        
                        	Interface Status
                        	**type**\:  :py:class:`DnxQoseaShowIntfStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowIntfStatus>`
                        
                        

                        """

                        _prefix = 'ncs5500-qos-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PlatformQos.Nodes.Node.Interfaces.Interface.PolicyDetails, self).__init__()

                            self.yang_name = "policy-details"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('npu_id', (YLeaf(YType.uint32, 'npu-id'), ['int'])),
                                ('interface_handle', (YLeaf(YType.uint32, 'interface-handle'), ['int'])),
                                ('interface_bandwidth_kbps', (YLeaf(YType.uint32, 'interface-bandwidth-kbps'), ['int'])),
                                ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                ('total_number_of_classes', (YLeaf(YType.uint16, 'total-number-of-classes'), ['int'])),
                                ('voq_base_address', (YLeaf(YType.uint32, 'voq-base-address'), ['int'])),
                                ('voq_stats_handle', (YLeaf(YType.uint64, 'voq-stats-handle'), ['int'])),
                                ('stats_accounting_type', (YLeaf(YType.enumeration, 'stats-accounting-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'QosPolicyAccountEnum', '')])),
                                ('policy_status', (YLeaf(YType.enumeration, 'policy-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowPolicyStatus', '')])),
                                ('interface_status', (YLeaf(YType.enumeration, 'interface-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowIntfStatus', '')])),
                            ])
                            self.npu_id = None
                            self.interface_handle = None
                            self.interface_bandwidth_kbps = None
                            self.policy_name = None
                            self.total_number_of_classes = None
                            self.voq_base_address = None
                            self.voq_stats_handle = None
                            self.stats_accounting_type = None
                            self.policy_status = None
                            self.interface_status = None
                            self._segment_path = lambda: "policy-details"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.PolicyDetails, [u'npu_id', u'interface_handle', u'interface_bandwidth_kbps', u'policy_name', u'total_number_of_classes', u'voq_base_address', u'voq_stats_handle', u'stats_accounting_type', u'policy_status', u'interface_status'], name, value)


                    class Output(Entity):
                        """
                        QoS policy direction egress
                        
                        .. attribute:: qos_class_table
                        
                        	QoS list of class names
                        	**type**\:  :py:class:`QosClassTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable>`
                        
                        

                        """

                        _prefix = 'ncs5500-qos-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PlatformQos.Nodes.Node.Interfaces.Interface.Output, self).__init__()

                            self.yang_name = "output"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("qos-class-table", ("qos_class_table", PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable))])
                            self._leafs = OrderedDict()

                            self.qos_class_table = PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable()
                            self.qos_class_table.parent = self
                            self._children_name_map["qos_class_table"] = "qos-class-table"
                            self._segment_path = lambda: "output"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output, [], name, value)


                        class QosClassTable(Entity):
                            """
                            QoS list of class names
                            
                            .. attribute:: class_
                            
                            	QoS policy class
                            	**type**\: list of  		 :py:class:`Class <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class>`
                            
                            

                            """

                            _prefix = 'ncs5500-qos-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable, self).__init__()

                                self.yang_name = "qos-class-table"
                                self.yang_parent_name = "output"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("class", ("class_", PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class))])
                                self._leafs = OrderedDict()

                                self.class_ = YList(self)
                                self._segment_path = lambda: "qos-class-table"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable, [], name, value)


                            class Class(Entity):
                                """
                                QoS policy class
                                
                                .. attribute:: level_one_class_name  (key)
                                
                                	QoS policy class name at level 1
                                	**type**\: str
                                
                                .. attribute:: level_two_class_name
                                
                                	QoS policy child class name at level 2
                                	**type**\: str
                                
                                .. attribute:: config_max_rate
                                
                                	Configured maximum rate
                                	**type**\:  :py:class:`ConfigMaxRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ConfigMaxRate>`
                                
                                .. attribute:: config_min_rate
                                
                                	Configured minimum rate
                                	**type**\:  :py:class:`ConfigMinRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ConfigMinRate>`
                                
                                .. attribute:: config_queue_limit
                                
                                	Configured queue limit
                                	**type**\:  :py:class:`ConfigQueueLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ConfigQueueLimit>`
                                
                                .. attribute:: config_policer_average_rate
                                
                                	Configured policer average rate
                                	**type**\:  :py:class:`ConfigPolicerAverageRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ConfigPolicerAverageRate>`
                                
                                .. attribute:: config_policer_peak_rate
                                
                                	Config policer peak rate
                                	**type**\:  :py:class:`ConfigPolicerPeakRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ConfigPolicerPeakRate>`
                                
                                .. attribute:: config_policer_conform_burst
                                
                                	Configured policer conform burst
                                	**type**\:  :py:class:`ConfigPolicerConformBurst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ConfigPolicerConformBurst>`
                                
                                .. attribute:: config_policer_excess_burst
                                
                                	Configured policer excess burst
                                	**type**\:  :py:class:`ConfigPolicerExcessBurst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ConfigPolicerExcessBurst>`
                                
                                .. attribute:: conform_action
                                
                                	Conform action
                                	**type**\:  :py:class:`ConformAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ConformAction>`
                                
                                .. attribute:: exceed_action
                                
                                	Exceed action
                                	**type**\:  :py:class:`ExceedAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ExceedAction>`
                                
                                .. attribute:: violate_action
                                
                                	Violate action
                                	**type**\:  :py:class:`ViolateAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ViolateAction>`
                                
                                .. attribute:: class_level
                                
                                	Class level
                                	**type**\:  :py:class:`DnxQoseaShowLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowLevel>`
                                
                                .. attribute:: egress_queue_id
                                
                                	Egress Queue ID
                                	**type**\: int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: queue_type
                                
                                	Queue type
                                	**type**\:  :py:class:`DnxQoseaShowQueue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowQueue>`
                                
                                .. attribute:: priority_level
                                
                                	Priority level
                                	**type**\:  :py:class:`DnxQoseaShowHpLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowHpLevel>`
                                
                                .. attribute:: hardware_max_rate_kbps
                                
                                	Hardware maximum rate in kbps
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: kbit/s
                                
                                .. attribute:: hardware_min_rate_kbps
                                
                                	Hardware minimum rate in kbps
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: kbit/s
                                
                                .. attribute:: config_excess_bandwidth_percent
                                
                                	Configured excess bandwidth percentage
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: percentage
                                
                                .. attribute:: config_excess_bandwidth_unit
                                
                                	Configured excess bandwidth unit
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: hardware_excess_bandwidth_weight
                                
                                	Hardware excess bandwidth weight
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: network_min_bandwidth_kbps
                                
                                	Network minimum Bandwith
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: hardware_queue_limit_bytes
                                
                                	Hardware queue limit in bytes
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: byte
                                
                                .. attribute:: hardware_queue_limit_microseconds
                                
                                	Hardware queue limit in microseconds
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: microsecond
                                
                                .. attribute:: policer_bucket_id
                                
                                	PolicerBucketID
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: policer_stats_handle
                                
                                	PolicerStatsHandle
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: hardware_policer_average_rate_kbps
                                
                                	Hardware policer average in kbps
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: kbit/s
                                
                                .. attribute:: hardware_policer_peak_rate_kbps
                                
                                	Hardware policer peak rate
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: hardware_policer_conform_burst_bytes
                                
                                	Hardware policer conform burst
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: hardware_policer_excess_burst_bytes
                                
                                	Hardware policer excess burst
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ip_mark
                                
                                	IP mark
                                	**type**\: list of  		 :py:class:`IpMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.IpMark>`
                                
                                .. attribute:: common_mark
                                
                                	Common mark
                                	**type**\: list of  		 :py:class:`CommonMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.CommonMark>`
                                
                                .. attribute:: mpls_mark
                                
                                	MPLS mark
                                	**type**\: list of  		 :py:class:`MplsMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.MplsMark>`
                                
                                .. attribute:: wred
                                
                                	WRED parameters
                                	**type**\: list of  		 :py:class:`Wred <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.Wred>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class, self).__init__()

                                    self.yang_name = "class"
                                    self.yang_parent_name = "qos-class-table"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['level_one_class_name']
                                    self._child_classes = OrderedDict([("config-max-rate", ("config_max_rate", PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ConfigMaxRate)), ("config-min-rate", ("config_min_rate", PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ConfigMinRate)), ("config-queue-limit", ("config_queue_limit", PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ConfigQueueLimit)), ("config-policer-average-rate", ("config_policer_average_rate", PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ConfigPolicerAverageRate)), ("config-policer-peak-rate", ("config_policer_peak_rate", PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ConfigPolicerPeakRate)), ("config-policer-conform-burst", ("config_policer_conform_burst", PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ConfigPolicerConformBurst)), ("config-policer-excess-burst", ("config_policer_excess_burst", PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ConfigPolicerExcessBurst)), ("conform-action", ("conform_action", PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ConformAction)), ("exceed-action", ("exceed_action", PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ExceedAction)), ("violate-action", ("violate_action", PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ViolateAction)), ("ip-mark", ("ip_mark", PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.IpMark)), ("common-mark", ("common_mark", PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.CommonMark)), ("mpls-mark", ("mpls_mark", PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.MplsMark)), ("wred", ("wred", PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.Wred))])
                                    self._leafs = OrderedDict([
                                        ('level_one_class_name', (YLeaf(YType.str, 'level-one-class-name'), ['str'])),
                                        ('level_two_class_name', (YLeaf(YType.str, 'level-two-class-name'), ['str'])),
                                        ('class_level', (YLeaf(YType.enumeration, 'class-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowLevel', '')])),
                                        ('egress_queue_id', (YLeaf(YType.int32, 'egress-queue-id'), ['int'])),
                                        ('queue_type', (YLeaf(YType.enumeration, 'queue-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowQueue', '')])),
                                        ('priority_level', (YLeaf(YType.enumeration, 'priority-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowHpLevel', '')])),
                                        ('hardware_max_rate_kbps', (YLeaf(YType.uint32, 'hardware-max-rate-kbps'), ['int'])),
                                        ('hardware_min_rate_kbps', (YLeaf(YType.uint32, 'hardware-min-rate-kbps'), ['int'])),
                                        ('config_excess_bandwidth_percent', (YLeaf(YType.uint32, 'config-excess-bandwidth-percent'), ['int'])),
                                        ('config_excess_bandwidth_unit', (YLeaf(YType.uint32, 'config-excess-bandwidth-unit'), ['int'])),
                                        ('hardware_excess_bandwidth_weight', (YLeaf(YType.uint32, 'hardware-excess-bandwidth-weight'), ['int'])),
                                        ('network_min_bandwidth_kbps', (YLeaf(YType.uint32, 'network-min-bandwidth-kbps'), ['int'])),
                                        ('hardware_queue_limit_bytes', (YLeaf(YType.uint64, 'hardware-queue-limit-bytes'), ['int'])),
                                        ('hardware_queue_limit_microseconds', (YLeaf(YType.uint64, 'hardware-queue-limit-microseconds'), ['int'])),
                                        ('policer_bucket_id', (YLeaf(YType.uint32, 'policer-bucket-id'), ['int'])),
                                        ('policer_stats_handle', (YLeaf(YType.uint64, 'policer-stats-handle'), ['int'])),
                                        ('hardware_policer_average_rate_kbps', (YLeaf(YType.uint32, 'hardware-policer-average-rate-kbps'), ['int'])),
                                        ('hardware_policer_peak_rate_kbps', (YLeaf(YType.uint32, 'hardware-policer-peak-rate-kbps'), ['int'])),
                                        ('hardware_policer_conform_burst_bytes', (YLeaf(YType.uint32, 'hardware-policer-conform-burst-bytes'), ['int'])),
                                        ('hardware_policer_excess_burst_bytes', (YLeaf(YType.uint32, 'hardware-policer-excess-burst-bytes'), ['int'])),
                                    ])
                                    self.level_one_class_name = None
                                    self.level_two_class_name = None
                                    self.class_level = None
                                    self.egress_queue_id = None
                                    self.queue_type = None
                                    self.priority_level = None
                                    self.hardware_max_rate_kbps = None
                                    self.hardware_min_rate_kbps = None
                                    self.config_excess_bandwidth_percent = None
                                    self.config_excess_bandwidth_unit = None
                                    self.hardware_excess_bandwidth_weight = None
                                    self.network_min_bandwidth_kbps = None
                                    self.hardware_queue_limit_bytes = None
                                    self.hardware_queue_limit_microseconds = None
                                    self.policer_bucket_id = None
                                    self.policer_stats_handle = None
                                    self.hardware_policer_average_rate_kbps = None
                                    self.hardware_policer_peak_rate_kbps = None
                                    self.hardware_policer_conform_burst_bytes = None
                                    self.hardware_policer_excess_burst_bytes = None

                                    self.config_max_rate = PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ConfigMaxRate()
                                    self.config_max_rate.parent = self
                                    self._children_name_map["config_max_rate"] = "config-max-rate"

                                    self.config_min_rate = PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ConfigMinRate()
                                    self.config_min_rate.parent = self
                                    self._children_name_map["config_min_rate"] = "config-min-rate"

                                    self.config_queue_limit = PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ConfigQueueLimit()
                                    self.config_queue_limit.parent = self
                                    self._children_name_map["config_queue_limit"] = "config-queue-limit"

                                    self.config_policer_average_rate = PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ConfigPolicerAverageRate()
                                    self.config_policer_average_rate.parent = self
                                    self._children_name_map["config_policer_average_rate"] = "config-policer-average-rate"

                                    self.config_policer_peak_rate = PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ConfigPolicerPeakRate()
                                    self.config_policer_peak_rate.parent = self
                                    self._children_name_map["config_policer_peak_rate"] = "config-policer-peak-rate"

                                    self.config_policer_conform_burst = PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ConfigPolicerConformBurst()
                                    self.config_policer_conform_burst.parent = self
                                    self._children_name_map["config_policer_conform_burst"] = "config-policer-conform-burst"

                                    self.config_policer_excess_burst = PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ConfigPolicerExcessBurst()
                                    self.config_policer_excess_burst.parent = self
                                    self._children_name_map["config_policer_excess_burst"] = "config-policer-excess-burst"

                                    self.conform_action = PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ConformAction()
                                    self.conform_action.parent = self
                                    self._children_name_map["conform_action"] = "conform-action"

                                    self.exceed_action = PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ExceedAction()
                                    self.exceed_action.parent = self
                                    self._children_name_map["exceed_action"] = "exceed-action"

                                    self.violate_action = PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ViolateAction()
                                    self.violate_action.parent = self
                                    self._children_name_map["violate_action"] = "violate-action"

                                    self.ip_mark = YList(self)
                                    self.common_mark = YList(self)
                                    self.mpls_mark = YList(self)
                                    self.wred = YList(self)
                                    self._segment_path = lambda: "class" + "[level-one-class-name='" + str(self.level_one_class_name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class, ['level_one_class_name', 'level_two_class_name', u'class_level', u'egress_queue_id', u'queue_type', u'priority_level', u'hardware_max_rate_kbps', u'hardware_min_rate_kbps', u'config_excess_bandwidth_percent', u'config_excess_bandwidth_unit', u'hardware_excess_bandwidth_weight', u'network_min_bandwidth_kbps', u'hardware_queue_limit_bytes', u'hardware_queue_limit_microseconds', u'policer_bucket_id', u'policer_stats_handle', u'hardware_policer_average_rate_kbps', u'hardware_policer_peak_rate_kbps', u'hardware_policer_conform_burst_bytes', u'hardware_policer_excess_burst_bytes'], name, value)


                                class ConfigMaxRate(Entity):
                                    """
                                    Configured maximum rate
                                    
                                    .. attribute:: policy_value
                                    
                                    	Policy value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: policy_unit
                                    
                                    	Policy unit
                                    	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ConfigMaxRate, self).__init__()

                                        self.yang_name = "config-max-rate"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                            ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                        ])
                                        self.policy_value = None
                                        self.policy_unit = None
                                        self._segment_path = lambda: "config-max-rate"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ConfigMaxRate, [u'policy_value', u'policy_unit'], name, value)


                                class ConfigMinRate(Entity):
                                    """
                                    Configured minimum rate
                                    
                                    .. attribute:: policy_value
                                    
                                    	Policy value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: policy_unit
                                    
                                    	Policy unit
                                    	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ConfigMinRate, self).__init__()

                                        self.yang_name = "config-min-rate"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                            ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                        ])
                                        self.policy_value = None
                                        self.policy_unit = None
                                        self._segment_path = lambda: "config-min-rate"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ConfigMinRate, [u'policy_value', u'policy_unit'], name, value)


                                class ConfigQueueLimit(Entity):
                                    """
                                    Configured queue limit
                                    
                                    .. attribute:: policy_value
                                    
                                    	Policy value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: policy_unit
                                    
                                    	Policy unit
                                    	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ConfigQueueLimit, self).__init__()

                                        self.yang_name = "config-queue-limit"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                            ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                        ])
                                        self.policy_value = None
                                        self.policy_unit = None
                                        self._segment_path = lambda: "config-queue-limit"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ConfigQueueLimit, [u'policy_value', u'policy_unit'], name, value)


                                class ConfigPolicerAverageRate(Entity):
                                    """
                                    Configured policer average rate
                                    
                                    .. attribute:: policy_value
                                    
                                    	Policy value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: policy_unit
                                    
                                    	Policy unit
                                    	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ConfigPolicerAverageRate, self).__init__()

                                        self.yang_name = "config-policer-average-rate"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                            ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                        ])
                                        self.policy_value = None
                                        self.policy_unit = None
                                        self._segment_path = lambda: "config-policer-average-rate"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ConfigPolicerAverageRate, [u'policy_value', u'policy_unit'], name, value)


                                class ConfigPolicerPeakRate(Entity):
                                    """
                                    Config policer peak rate
                                    
                                    .. attribute:: policy_value
                                    
                                    	Policy value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: policy_unit
                                    
                                    	Policy unit
                                    	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ConfigPolicerPeakRate, self).__init__()

                                        self.yang_name = "config-policer-peak-rate"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                            ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                        ])
                                        self.policy_value = None
                                        self.policy_unit = None
                                        self._segment_path = lambda: "config-policer-peak-rate"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ConfigPolicerPeakRate, [u'policy_value', u'policy_unit'], name, value)


                                class ConfigPolicerConformBurst(Entity):
                                    """
                                    Configured policer conform burst
                                    
                                    .. attribute:: policy_value
                                    
                                    	Policy value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: policy_unit
                                    
                                    	Policy unit
                                    	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ConfigPolicerConformBurst, self).__init__()

                                        self.yang_name = "config-policer-conform-burst"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                            ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                        ])
                                        self.policy_value = None
                                        self.policy_unit = None
                                        self._segment_path = lambda: "config-policer-conform-burst"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ConfigPolicerConformBurst, [u'policy_value', u'policy_unit'], name, value)


                                class ConfigPolicerExcessBurst(Entity):
                                    """
                                    Configured policer excess burst
                                    
                                    .. attribute:: policy_value
                                    
                                    	Policy value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: policy_unit
                                    
                                    	Policy unit
                                    	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ConfigPolicerExcessBurst, self).__init__()

                                        self.yang_name = "config-policer-excess-burst"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                            ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                        ])
                                        self.policy_value = None
                                        self.policy_unit = None
                                        self._segment_path = lambda: "config-policer-excess-burst"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ConfigPolicerExcessBurst, [u'policy_value', u'policy_unit'], name, value)


                                class ConformAction(Entity):
                                    """
                                    Conform action
                                    
                                    .. attribute:: action_type
                                    
                                    	Policer action type
                                    	**type**\:  :py:class:`DnxQoseaShowAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowAction>`
                                    
                                    .. attribute:: mark
                                    
                                    	Action mark
                                    	**type**\: list of  		 :py:class:`Mark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ConformAction.Mark>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ConformAction, self).__init__()

                                        self.yang_name = "conform-action"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("mark", ("mark", PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ConformAction.Mark))])
                                        self._leafs = OrderedDict([
                                            ('action_type', (YLeaf(YType.enumeration, 'action-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowAction', '')])),
                                        ])
                                        self.action_type = None

                                        self.mark = YList(self)
                                        self._segment_path = lambda: "conform-action"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ConformAction, [u'action_type'], name, value)


                                    class Mark(Entity):
                                        """
                                        Action mark
                                        
                                        .. attribute:: mark_type
                                        
                                        	Mark type
                                        	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                        
                                        .. attribute:: mark_value
                                        
                                        	Mark value
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ConformAction.Mark, self).__init__()

                                            self.yang_name = "mark"
                                            self.yang_parent_name = "conform-action"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                                ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                            ])
                                            self.mark_type = None
                                            self.mark_value = None
                                            self._segment_path = lambda: "mark"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ConformAction.Mark, [u'mark_type', u'mark_value'], name, value)


                                class ExceedAction(Entity):
                                    """
                                    Exceed action
                                    
                                    .. attribute:: action_type
                                    
                                    	Policer action type
                                    	**type**\:  :py:class:`DnxQoseaShowAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowAction>`
                                    
                                    .. attribute:: mark
                                    
                                    	Action mark
                                    	**type**\: list of  		 :py:class:`Mark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ExceedAction.Mark>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ExceedAction, self).__init__()

                                        self.yang_name = "exceed-action"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("mark", ("mark", PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ExceedAction.Mark))])
                                        self._leafs = OrderedDict([
                                            ('action_type', (YLeaf(YType.enumeration, 'action-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowAction', '')])),
                                        ])
                                        self.action_type = None

                                        self.mark = YList(self)
                                        self._segment_path = lambda: "exceed-action"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ExceedAction, [u'action_type'], name, value)


                                    class Mark(Entity):
                                        """
                                        Action mark
                                        
                                        .. attribute:: mark_type
                                        
                                        	Mark type
                                        	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                        
                                        .. attribute:: mark_value
                                        
                                        	Mark value
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ExceedAction.Mark, self).__init__()

                                            self.yang_name = "mark"
                                            self.yang_parent_name = "exceed-action"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                                ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                            ])
                                            self.mark_type = None
                                            self.mark_value = None
                                            self._segment_path = lambda: "mark"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ExceedAction.Mark, [u'mark_type', u'mark_value'], name, value)


                                class ViolateAction(Entity):
                                    """
                                    Violate action
                                    
                                    .. attribute:: action_type
                                    
                                    	Policer action type
                                    	**type**\:  :py:class:`DnxQoseaShowAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowAction>`
                                    
                                    .. attribute:: mark
                                    
                                    	Action mark
                                    	**type**\: list of  		 :py:class:`Mark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ViolateAction.Mark>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ViolateAction, self).__init__()

                                        self.yang_name = "violate-action"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("mark", ("mark", PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ViolateAction.Mark))])
                                        self._leafs = OrderedDict([
                                            ('action_type', (YLeaf(YType.enumeration, 'action-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowAction', '')])),
                                        ])
                                        self.action_type = None

                                        self.mark = YList(self)
                                        self._segment_path = lambda: "violate-action"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ViolateAction, [u'action_type'], name, value)


                                    class Mark(Entity):
                                        """
                                        Action mark
                                        
                                        .. attribute:: mark_type
                                        
                                        	Mark type
                                        	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                        
                                        .. attribute:: mark_value
                                        
                                        	Mark value
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ViolateAction.Mark, self).__init__()

                                            self.yang_name = "mark"
                                            self.yang_parent_name = "violate-action"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                                ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                            ])
                                            self.mark_type = None
                                            self.mark_value = None
                                            self._segment_path = lambda: "mark"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.ViolateAction.Mark, [u'mark_type', u'mark_value'], name, value)


                                class IpMark(Entity):
                                    """
                                    IP mark
                                    
                                    .. attribute:: mark_type
                                    
                                    	Mark type
                                    	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                    
                                    .. attribute:: mark_value
                                    
                                    	Mark value
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.IpMark, self).__init__()

                                        self.yang_name = "ip-mark"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                            ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                        ])
                                        self.mark_type = None
                                        self.mark_value = None
                                        self._segment_path = lambda: "ip-mark"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.IpMark, [u'mark_type', u'mark_value'], name, value)


                                class CommonMark(Entity):
                                    """
                                    Common mark
                                    
                                    .. attribute:: mark_type
                                    
                                    	Mark type
                                    	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                    
                                    .. attribute:: mark_value
                                    
                                    	Mark value
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.CommonMark, self).__init__()

                                        self.yang_name = "common-mark"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                            ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                        ])
                                        self.mark_type = None
                                        self.mark_value = None
                                        self._segment_path = lambda: "common-mark"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.CommonMark, [u'mark_type', u'mark_value'], name, value)


                                class MplsMark(Entity):
                                    """
                                    MPLS mark
                                    
                                    .. attribute:: mark_type
                                    
                                    	Mark type
                                    	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                    
                                    .. attribute:: mark_value
                                    
                                    	Mark value
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.MplsMark, self).__init__()

                                        self.yang_name = "mpls-mark"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                            ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                        ])
                                        self.mark_type = None
                                        self.mark_value = None
                                        self._segment_path = lambda: "mpls-mark"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.MplsMark, [u'mark_type', u'mark_value'], name, value)


                                class Wred(Entity):
                                    """
                                    WRED parameters
                                    
                                    .. attribute:: wred_match_value
                                    
                                    	WRED match values
                                    	**type**\:  :py:class:`WredMatchValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.Wred.WredMatchValue>`
                                    
                                    .. attribute:: config_min_threshold
                                    
                                    	Configured minimum threshold
                                    	**type**\:  :py:class:`ConfigMinThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.Wred.ConfigMinThreshold>`
                                    
                                    .. attribute:: config_max_threshold
                                    
                                    	Configured maximum threshold
                                    	**type**\:  :py:class:`ConfigMaxThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.Wred.ConfigMaxThreshold>`
                                    
                                    .. attribute:: wred_match_type
                                    
                                    	WREDMatchType
                                    	**type**\:  :py:class:`DnxQoseaShowWred <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowWred>`
                                    
                                    .. attribute:: hardware_min_threshold_bytes
                                    
                                    	Hardware minimum threshold
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: hardware_max_threshold_bytes
                                    
                                    	Hardware maximum threshold
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: first_segment
                                    
                                    	First segment
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: segment_size
                                    
                                    	Segment size
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.Wred, self).__init__()

                                        self.yang_name = "wred"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("wred-match-value", ("wred_match_value", PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.Wred.WredMatchValue)), ("config-min-threshold", ("config_min_threshold", PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.Wred.ConfigMinThreshold)), ("config-max-threshold", ("config_max_threshold", PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.Wred.ConfigMaxThreshold))])
                                        self._leafs = OrderedDict([
                                            ('wred_match_type', (YLeaf(YType.enumeration, 'wred-match-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowWred', '')])),
                                            ('hardware_min_threshold_bytes', (YLeaf(YType.uint32, 'hardware-min-threshold-bytes'), ['int'])),
                                            ('hardware_max_threshold_bytes', (YLeaf(YType.uint32, 'hardware-max-threshold-bytes'), ['int'])),
                                            ('first_segment', (YLeaf(YType.uint16, 'first-segment'), ['int'])),
                                            ('segment_size', (YLeaf(YType.uint32, 'segment-size'), ['int'])),
                                        ])
                                        self.wred_match_type = None
                                        self.hardware_min_threshold_bytes = None
                                        self.hardware_max_threshold_bytes = None
                                        self.first_segment = None
                                        self.segment_size = None

                                        self.wred_match_value = PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.Wred.WredMatchValue()
                                        self.wred_match_value.parent = self
                                        self._children_name_map["wred_match_value"] = "wred-match-value"

                                        self.config_min_threshold = PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.Wred.ConfigMinThreshold()
                                        self.config_min_threshold.parent = self
                                        self._children_name_map["config_min_threshold"] = "config-min-threshold"

                                        self.config_max_threshold = PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.Wred.ConfigMaxThreshold()
                                        self.config_max_threshold.parent = self
                                        self._children_name_map["config_max_threshold"] = "config-max-threshold"
                                        self._segment_path = lambda: "wred"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.Wred, [u'wred_match_type', u'hardware_min_threshold_bytes', u'hardware_max_threshold_bytes', u'first_segment', u'segment_size'], name, value)


                                    class WredMatchValue(Entity):
                                        """
                                        WRED match values
                                        
                                        .. attribute:: dnx_qosea_show_red_match_value
                                        
                                        	dnx qosea show red match value
                                        	**type**\: list of  		 :py:class:`DnxQoseaShowRedMatchValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue>`
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.Wred.WredMatchValue, self).__init__()

                                            self.yang_name = "wred-match-value"
                                            self.yang_parent_name = "wred"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("dnx-qosea-show-red-match-value", ("dnx_qosea_show_red_match_value", PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue))])
                                            self._leafs = OrderedDict()

                                            self.dnx_qosea_show_red_match_value = YList(self)
                                            self._segment_path = lambda: "wred-match-value"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.Wred.WredMatchValue, [], name, value)


                                        class DnxQoseaShowRedMatchValue(Entity):
                                            """
                                            dnx qosea show red match value
                                            
                                            .. attribute:: range_start
                                            
                                            	Start value of a range
                                            	**type**\: int
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: range_end
                                            
                                            	End value of a range
                                            	**type**\: int
                                            
                                            	**range:** 0..255
                                            
                                            

                                            """

                                            _prefix = 'ncs5500-qos-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue, self).__init__()

                                                self.yang_name = "dnx-qosea-show-red-match-value"
                                                self.yang_parent_name = "wred-match-value"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('range_start', (YLeaf(YType.uint8, 'range-start'), ['int'])),
                                                    ('range_end', (YLeaf(YType.uint8, 'range-end'), ['int'])),
                                                ])
                                                self.range_start = None
                                                self.range_end = None
                                                self._segment_path = lambda: "dnx-qosea-show-red-match-value"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue, [u'range_start', u'range_end'], name, value)


                                    class ConfigMinThreshold(Entity):
                                        """
                                        Configured minimum threshold
                                        
                                        .. attribute:: policy_value
                                        
                                        	Policy value
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: policy_unit
                                        
                                        	Policy unit
                                        	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.Wred.ConfigMinThreshold, self).__init__()

                                            self.yang_name = "config-min-threshold"
                                            self.yang_parent_name = "wred"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                                ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                            ])
                                            self.policy_value = None
                                            self.policy_unit = None
                                            self._segment_path = lambda: "config-min-threshold"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.Wred.ConfigMinThreshold, [u'policy_value', u'policy_unit'], name, value)


                                    class ConfigMaxThreshold(Entity):
                                        """
                                        Configured maximum threshold
                                        
                                        .. attribute:: policy_value
                                        
                                        	Policy value
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: policy_unit
                                        
                                        	Policy unit
                                        	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.Wred.ConfigMaxThreshold, self).__init__()

                                            self.yang_name = "config-max-threshold"
                                            self.yang_parent_name = "wred"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                                ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                            ])
                                            self.policy_value = None
                                            self.policy_unit = None
                                            self._segment_path = lambda: "config-max-threshold"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.QosClassTable.Class.Wred.ConfigMaxThreshold, [u'policy_value', u'policy_unit'], name, value)


                    class ClassTable(Entity):
                        """
                        QoS list of class names
                        
                        .. attribute:: class_
                        
                        	QoS policy class
                        	**type**\: list of  		 :py:class:`Class <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class>`
                        
                        

                        """

                        _prefix = 'ncs5500-qos-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable, self).__init__()

                            self.yang_name = "class-table"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("class", ("class_", PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class))])
                            self._leafs = OrderedDict()

                            self.class_ = YList(self)
                            self._segment_path = lambda: "class-table"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable, [], name, value)


                        class Class(Entity):
                            """
                            QoS policy class
                            
                            .. attribute:: level_one_class_name  (key)
                            
                            	QoS policy class name at level 1
                            	**type**\: str
                            
                            .. attribute:: level_two_class_name
                            
                            	QoS policy child class name at level 2
                            	**type**\: str
                            
                            .. attribute:: config_max_rate
                            
                            	Configured maximum rate
                            	**type**\:  :py:class:`ConfigMaxRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ConfigMaxRate>`
                            
                            .. attribute:: config_min_rate
                            
                            	Configured minimum rate
                            	**type**\:  :py:class:`ConfigMinRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ConfigMinRate>`
                            
                            .. attribute:: config_queue_limit
                            
                            	Configured queue limit
                            	**type**\:  :py:class:`ConfigQueueLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ConfigQueueLimit>`
                            
                            .. attribute:: config_policer_average_rate
                            
                            	Configured policer average rate
                            	**type**\:  :py:class:`ConfigPolicerAverageRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ConfigPolicerAverageRate>`
                            
                            .. attribute:: config_policer_peak_rate
                            
                            	Config policer peak rate
                            	**type**\:  :py:class:`ConfigPolicerPeakRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ConfigPolicerPeakRate>`
                            
                            .. attribute:: config_policer_conform_burst
                            
                            	Configured policer conform burst
                            	**type**\:  :py:class:`ConfigPolicerConformBurst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ConfigPolicerConformBurst>`
                            
                            .. attribute:: config_policer_excess_burst
                            
                            	Configured policer excess burst
                            	**type**\:  :py:class:`ConfigPolicerExcessBurst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ConfigPolicerExcessBurst>`
                            
                            .. attribute:: conform_action
                            
                            	Conform action
                            	**type**\:  :py:class:`ConformAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ConformAction>`
                            
                            .. attribute:: exceed_action
                            
                            	Exceed action
                            	**type**\:  :py:class:`ExceedAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ExceedAction>`
                            
                            .. attribute:: violate_action
                            
                            	Violate action
                            	**type**\:  :py:class:`ViolateAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ViolateAction>`
                            
                            .. attribute:: class_level
                            
                            	Class level
                            	**type**\:  :py:class:`DnxQoseaShowLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowLevel>`
                            
                            .. attribute:: egress_queue_id
                            
                            	Egress Queue ID
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: queue_type
                            
                            	Queue type
                            	**type**\:  :py:class:`DnxQoseaShowQueue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowQueue>`
                            
                            .. attribute:: priority_level
                            
                            	Priority level
                            	**type**\:  :py:class:`DnxQoseaShowHpLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowHpLevel>`
                            
                            .. attribute:: hardware_max_rate_kbps
                            
                            	Hardware maximum rate in kbps
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: kbit/s
                            
                            .. attribute:: hardware_min_rate_kbps
                            
                            	Hardware minimum rate in kbps
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: kbit/s
                            
                            .. attribute:: config_excess_bandwidth_percent
                            
                            	Configured excess bandwidth percentage
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: percentage
                            
                            .. attribute:: config_excess_bandwidth_unit
                            
                            	Configured excess bandwidth unit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hardware_excess_bandwidth_weight
                            
                            	Hardware excess bandwidth weight
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: network_min_bandwidth_kbps
                            
                            	Network minimum Bandwith
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hardware_queue_limit_bytes
                            
                            	Hardware queue limit in bytes
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: hardware_queue_limit_microseconds
                            
                            	Hardware queue limit in microseconds
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: microsecond
                            
                            .. attribute:: policer_bucket_id
                            
                            	PolicerBucketID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: policer_stats_handle
                            
                            	PolicerStatsHandle
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: hardware_policer_average_rate_kbps
                            
                            	Hardware policer average in kbps
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: kbit/s
                            
                            .. attribute:: hardware_policer_peak_rate_kbps
                            
                            	Hardware policer peak rate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hardware_policer_conform_burst_bytes
                            
                            	Hardware policer conform burst
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hardware_policer_excess_burst_bytes
                            
                            	Hardware policer excess burst
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ip_mark
                            
                            	IP mark
                            	**type**\: list of  		 :py:class:`IpMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.IpMark>`
                            
                            .. attribute:: common_mark
                            
                            	Common mark
                            	**type**\: list of  		 :py:class:`CommonMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.CommonMark>`
                            
                            .. attribute:: mpls_mark
                            
                            	MPLS mark
                            	**type**\: list of  		 :py:class:`MplsMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.MplsMark>`
                            
                            .. attribute:: wred
                            
                            	WRED parameters
                            	**type**\: list of  		 :py:class:`Wred <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.Wred>`
                            
                            

                            """

                            _prefix = 'ncs5500-qos-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class, self).__init__()

                                self.yang_name = "class"
                                self.yang_parent_name = "class-table"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['level_one_class_name']
                                self._child_classes = OrderedDict([("config-max-rate", ("config_max_rate", PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ConfigMaxRate)), ("config-min-rate", ("config_min_rate", PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ConfigMinRate)), ("config-queue-limit", ("config_queue_limit", PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ConfigQueueLimit)), ("config-policer-average-rate", ("config_policer_average_rate", PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ConfigPolicerAverageRate)), ("config-policer-peak-rate", ("config_policer_peak_rate", PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ConfigPolicerPeakRate)), ("config-policer-conform-burst", ("config_policer_conform_burst", PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ConfigPolicerConformBurst)), ("config-policer-excess-burst", ("config_policer_excess_burst", PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ConfigPolicerExcessBurst)), ("conform-action", ("conform_action", PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ConformAction)), ("exceed-action", ("exceed_action", PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ExceedAction)), ("violate-action", ("violate_action", PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ViolateAction)), ("ip-mark", ("ip_mark", PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.IpMark)), ("common-mark", ("common_mark", PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.CommonMark)), ("mpls-mark", ("mpls_mark", PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.MplsMark)), ("wred", ("wred", PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.Wred))])
                                self._leafs = OrderedDict([
                                    ('level_one_class_name', (YLeaf(YType.str, 'level-one-class-name'), ['str'])),
                                    ('level_two_class_name', (YLeaf(YType.str, 'level-two-class-name'), ['str'])),
                                    ('class_level', (YLeaf(YType.enumeration, 'class-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowLevel', '')])),
                                    ('egress_queue_id', (YLeaf(YType.int32, 'egress-queue-id'), ['int'])),
                                    ('queue_type', (YLeaf(YType.enumeration, 'queue-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowQueue', '')])),
                                    ('priority_level', (YLeaf(YType.enumeration, 'priority-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowHpLevel', '')])),
                                    ('hardware_max_rate_kbps', (YLeaf(YType.uint32, 'hardware-max-rate-kbps'), ['int'])),
                                    ('hardware_min_rate_kbps', (YLeaf(YType.uint32, 'hardware-min-rate-kbps'), ['int'])),
                                    ('config_excess_bandwidth_percent', (YLeaf(YType.uint32, 'config-excess-bandwidth-percent'), ['int'])),
                                    ('config_excess_bandwidth_unit', (YLeaf(YType.uint32, 'config-excess-bandwidth-unit'), ['int'])),
                                    ('hardware_excess_bandwidth_weight', (YLeaf(YType.uint32, 'hardware-excess-bandwidth-weight'), ['int'])),
                                    ('network_min_bandwidth_kbps', (YLeaf(YType.uint32, 'network-min-bandwidth-kbps'), ['int'])),
                                    ('hardware_queue_limit_bytes', (YLeaf(YType.uint64, 'hardware-queue-limit-bytes'), ['int'])),
                                    ('hardware_queue_limit_microseconds', (YLeaf(YType.uint64, 'hardware-queue-limit-microseconds'), ['int'])),
                                    ('policer_bucket_id', (YLeaf(YType.uint32, 'policer-bucket-id'), ['int'])),
                                    ('policer_stats_handle', (YLeaf(YType.uint64, 'policer-stats-handle'), ['int'])),
                                    ('hardware_policer_average_rate_kbps', (YLeaf(YType.uint32, 'hardware-policer-average-rate-kbps'), ['int'])),
                                    ('hardware_policer_peak_rate_kbps', (YLeaf(YType.uint32, 'hardware-policer-peak-rate-kbps'), ['int'])),
                                    ('hardware_policer_conform_burst_bytes', (YLeaf(YType.uint32, 'hardware-policer-conform-burst-bytes'), ['int'])),
                                    ('hardware_policer_excess_burst_bytes', (YLeaf(YType.uint32, 'hardware-policer-excess-burst-bytes'), ['int'])),
                                ])
                                self.level_one_class_name = None
                                self.level_two_class_name = None
                                self.class_level = None
                                self.egress_queue_id = None
                                self.queue_type = None
                                self.priority_level = None
                                self.hardware_max_rate_kbps = None
                                self.hardware_min_rate_kbps = None
                                self.config_excess_bandwidth_percent = None
                                self.config_excess_bandwidth_unit = None
                                self.hardware_excess_bandwidth_weight = None
                                self.network_min_bandwidth_kbps = None
                                self.hardware_queue_limit_bytes = None
                                self.hardware_queue_limit_microseconds = None
                                self.policer_bucket_id = None
                                self.policer_stats_handle = None
                                self.hardware_policer_average_rate_kbps = None
                                self.hardware_policer_peak_rate_kbps = None
                                self.hardware_policer_conform_burst_bytes = None
                                self.hardware_policer_excess_burst_bytes = None

                                self.config_max_rate = PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ConfigMaxRate()
                                self.config_max_rate.parent = self
                                self._children_name_map["config_max_rate"] = "config-max-rate"

                                self.config_min_rate = PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ConfigMinRate()
                                self.config_min_rate.parent = self
                                self._children_name_map["config_min_rate"] = "config-min-rate"

                                self.config_queue_limit = PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ConfigQueueLimit()
                                self.config_queue_limit.parent = self
                                self._children_name_map["config_queue_limit"] = "config-queue-limit"

                                self.config_policer_average_rate = PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ConfigPolicerAverageRate()
                                self.config_policer_average_rate.parent = self
                                self._children_name_map["config_policer_average_rate"] = "config-policer-average-rate"

                                self.config_policer_peak_rate = PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ConfigPolicerPeakRate()
                                self.config_policer_peak_rate.parent = self
                                self._children_name_map["config_policer_peak_rate"] = "config-policer-peak-rate"

                                self.config_policer_conform_burst = PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ConfigPolicerConformBurst()
                                self.config_policer_conform_burst.parent = self
                                self._children_name_map["config_policer_conform_burst"] = "config-policer-conform-burst"

                                self.config_policer_excess_burst = PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ConfigPolicerExcessBurst()
                                self.config_policer_excess_burst.parent = self
                                self._children_name_map["config_policer_excess_burst"] = "config-policer-excess-burst"

                                self.conform_action = PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ConformAction()
                                self.conform_action.parent = self
                                self._children_name_map["conform_action"] = "conform-action"

                                self.exceed_action = PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ExceedAction()
                                self.exceed_action.parent = self
                                self._children_name_map["exceed_action"] = "exceed-action"

                                self.violate_action = PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ViolateAction()
                                self.violate_action.parent = self
                                self._children_name_map["violate_action"] = "violate-action"

                                self.ip_mark = YList(self)
                                self.common_mark = YList(self)
                                self.mpls_mark = YList(self)
                                self.wred = YList(self)
                                self._segment_path = lambda: "class" + "[level-one-class-name='" + str(self.level_one_class_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class, ['level_one_class_name', 'level_two_class_name', u'class_level', u'egress_queue_id', u'queue_type', u'priority_level', u'hardware_max_rate_kbps', u'hardware_min_rate_kbps', u'config_excess_bandwidth_percent', u'config_excess_bandwidth_unit', u'hardware_excess_bandwidth_weight', u'network_min_bandwidth_kbps', u'hardware_queue_limit_bytes', u'hardware_queue_limit_microseconds', u'policer_bucket_id', u'policer_stats_handle', u'hardware_policer_average_rate_kbps', u'hardware_policer_peak_rate_kbps', u'hardware_policer_conform_burst_bytes', u'hardware_policer_excess_burst_bytes'], name, value)


                            class ConfigMaxRate(Entity):
                                """
                                Configured maximum rate
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ConfigMaxRate, self).__init__()

                                    self.yang_name = "config-max-rate"
                                    self.yang_parent_name = "class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                        ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                    ])
                                    self.policy_value = None
                                    self.policy_unit = None
                                    self._segment_path = lambda: "config-max-rate"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ConfigMaxRate, [u'policy_value', u'policy_unit'], name, value)


                            class ConfigMinRate(Entity):
                                """
                                Configured minimum rate
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ConfigMinRate, self).__init__()

                                    self.yang_name = "config-min-rate"
                                    self.yang_parent_name = "class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                        ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                    ])
                                    self.policy_value = None
                                    self.policy_unit = None
                                    self._segment_path = lambda: "config-min-rate"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ConfigMinRate, [u'policy_value', u'policy_unit'], name, value)


                            class ConfigQueueLimit(Entity):
                                """
                                Configured queue limit
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ConfigQueueLimit, self).__init__()

                                    self.yang_name = "config-queue-limit"
                                    self.yang_parent_name = "class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                        ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                    ])
                                    self.policy_value = None
                                    self.policy_unit = None
                                    self._segment_path = lambda: "config-queue-limit"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ConfigQueueLimit, [u'policy_value', u'policy_unit'], name, value)


                            class ConfigPolicerAverageRate(Entity):
                                """
                                Configured policer average rate
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ConfigPolicerAverageRate, self).__init__()

                                    self.yang_name = "config-policer-average-rate"
                                    self.yang_parent_name = "class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                        ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                    ])
                                    self.policy_value = None
                                    self.policy_unit = None
                                    self._segment_path = lambda: "config-policer-average-rate"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ConfigPolicerAverageRate, [u'policy_value', u'policy_unit'], name, value)


                            class ConfigPolicerPeakRate(Entity):
                                """
                                Config policer peak rate
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ConfigPolicerPeakRate, self).__init__()

                                    self.yang_name = "config-policer-peak-rate"
                                    self.yang_parent_name = "class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                        ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                    ])
                                    self.policy_value = None
                                    self.policy_unit = None
                                    self._segment_path = lambda: "config-policer-peak-rate"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ConfigPolicerPeakRate, [u'policy_value', u'policy_unit'], name, value)


                            class ConfigPolicerConformBurst(Entity):
                                """
                                Configured policer conform burst
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ConfigPolicerConformBurst, self).__init__()

                                    self.yang_name = "config-policer-conform-burst"
                                    self.yang_parent_name = "class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                        ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                    ])
                                    self.policy_value = None
                                    self.policy_unit = None
                                    self._segment_path = lambda: "config-policer-conform-burst"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ConfigPolicerConformBurst, [u'policy_value', u'policy_unit'], name, value)


                            class ConfigPolicerExcessBurst(Entity):
                                """
                                Configured policer excess burst
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ConfigPolicerExcessBurst, self).__init__()

                                    self.yang_name = "config-policer-excess-burst"
                                    self.yang_parent_name = "class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                        ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                    ])
                                    self.policy_value = None
                                    self.policy_unit = None
                                    self._segment_path = lambda: "config-policer-excess-burst"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ConfigPolicerExcessBurst, [u'policy_value', u'policy_unit'], name, value)


                            class ConformAction(Entity):
                                """
                                Conform action
                                
                                .. attribute:: action_type
                                
                                	Policer action type
                                	**type**\:  :py:class:`DnxQoseaShowAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowAction>`
                                
                                .. attribute:: mark
                                
                                	Action mark
                                	**type**\: list of  		 :py:class:`Mark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ConformAction.Mark>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ConformAction, self).__init__()

                                    self.yang_name = "conform-action"
                                    self.yang_parent_name = "class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("mark", ("mark", PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ConformAction.Mark))])
                                    self._leafs = OrderedDict([
                                        ('action_type', (YLeaf(YType.enumeration, 'action-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowAction', '')])),
                                    ])
                                    self.action_type = None

                                    self.mark = YList(self)
                                    self._segment_path = lambda: "conform-action"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ConformAction, [u'action_type'], name, value)


                                class Mark(Entity):
                                    """
                                    Action mark
                                    
                                    .. attribute:: mark_type
                                    
                                    	Mark type
                                    	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                    
                                    .. attribute:: mark_value
                                    
                                    	Mark value
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ConformAction.Mark, self).__init__()

                                        self.yang_name = "mark"
                                        self.yang_parent_name = "conform-action"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                            ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                        ])
                                        self.mark_type = None
                                        self.mark_value = None
                                        self._segment_path = lambda: "mark"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ConformAction.Mark, [u'mark_type', u'mark_value'], name, value)


                            class ExceedAction(Entity):
                                """
                                Exceed action
                                
                                .. attribute:: action_type
                                
                                	Policer action type
                                	**type**\:  :py:class:`DnxQoseaShowAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowAction>`
                                
                                .. attribute:: mark
                                
                                	Action mark
                                	**type**\: list of  		 :py:class:`Mark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ExceedAction.Mark>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ExceedAction, self).__init__()

                                    self.yang_name = "exceed-action"
                                    self.yang_parent_name = "class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("mark", ("mark", PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ExceedAction.Mark))])
                                    self._leafs = OrderedDict([
                                        ('action_type', (YLeaf(YType.enumeration, 'action-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowAction', '')])),
                                    ])
                                    self.action_type = None

                                    self.mark = YList(self)
                                    self._segment_path = lambda: "exceed-action"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ExceedAction, [u'action_type'], name, value)


                                class Mark(Entity):
                                    """
                                    Action mark
                                    
                                    .. attribute:: mark_type
                                    
                                    	Mark type
                                    	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                    
                                    .. attribute:: mark_value
                                    
                                    	Mark value
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ExceedAction.Mark, self).__init__()

                                        self.yang_name = "mark"
                                        self.yang_parent_name = "exceed-action"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                            ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                        ])
                                        self.mark_type = None
                                        self.mark_value = None
                                        self._segment_path = lambda: "mark"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ExceedAction.Mark, [u'mark_type', u'mark_value'], name, value)


                            class ViolateAction(Entity):
                                """
                                Violate action
                                
                                .. attribute:: action_type
                                
                                	Policer action type
                                	**type**\:  :py:class:`DnxQoseaShowAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowAction>`
                                
                                .. attribute:: mark
                                
                                	Action mark
                                	**type**\: list of  		 :py:class:`Mark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ViolateAction.Mark>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ViolateAction, self).__init__()

                                    self.yang_name = "violate-action"
                                    self.yang_parent_name = "class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("mark", ("mark", PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ViolateAction.Mark))])
                                    self._leafs = OrderedDict([
                                        ('action_type', (YLeaf(YType.enumeration, 'action-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowAction', '')])),
                                    ])
                                    self.action_type = None

                                    self.mark = YList(self)
                                    self._segment_path = lambda: "violate-action"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ViolateAction, [u'action_type'], name, value)


                                class Mark(Entity):
                                    """
                                    Action mark
                                    
                                    .. attribute:: mark_type
                                    
                                    	Mark type
                                    	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                    
                                    .. attribute:: mark_value
                                    
                                    	Mark value
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ViolateAction.Mark, self).__init__()

                                        self.yang_name = "mark"
                                        self.yang_parent_name = "violate-action"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                            ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                        ])
                                        self.mark_type = None
                                        self.mark_value = None
                                        self._segment_path = lambda: "mark"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.ViolateAction.Mark, [u'mark_type', u'mark_value'], name, value)


                            class IpMark(Entity):
                                """
                                IP mark
                                
                                .. attribute:: mark_type
                                
                                	Mark type
                                	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                
                                .. attribute:: mark_value
                                
                                	Mark value
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.IpMark, self).__init__()

                                    self.yang_name = "ip-mark"
                                    self.yang_parent_name = "class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                        ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                    ])
                                    self.mark_type = None
                                    self.mark_value = None
                                    self._segment_path = lambda: "ip-mark"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.IpMark, [u'mark_type', u'mark_value'], name, value)


                            class CommonMark(Entity):
                                """
                                Common mark
                                
                                .. attribute:: mark_type
                                
                                	Mark type
                                	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                
                                .. attribute:: mark_value
                                
                                	Mark value
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.CommonMark, self).__init__()

                                    self.yang_name = "common-mark"
                                    self.yang_parent_name = "class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                        ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                    ])
                                    self.mark_type = None
                                    self.mark_value = None
                                    self._segment_path = lambda: "common-mark"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.CommonMark, [u'mark_type', u'mark_value'], name, value)


                            class MplsMark(Entity):
                                """
                                MPLS mark
                                
                                .. attribute:: mark_type
                                
                                	Mark type
                                	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                
                                .. attribute:: mark_value
                                
                                	Mark value
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.MplsMark, self).__init__()

                                    self.yang_name = "mpls-mark"
                                    self.yang_parent_name = "class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                        ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                    ])
                                    self.mark_type = None
                                    self.mark_value = None
                                    self._segment_path = lambda: "mpls-mark"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.MplsMark, [u'mark_type', u'mark_value'], name, value)


                            class Wred(Entity):
                                """
                                WRED parameters
                                
                                .. attribute:: wred_match_value
                                
                                	WRED match values
                                	**type**\:  :py:class:`WredMatchValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.Wred.WredMatchValue>`
                                
                                .. attribute:: config_min_threshold
                                
                                	Configured minimum threshold
                                	**type**\:  :py:class:`ConfigMinThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.Wred.ConfigMinThreshold>`
                                
                                .. attribute:: config_max_threshold
                                
                                	Configured maximum threshold
                                	**type**\:  :py:class:`ConfigMaxThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.Wred.ConfigMaxThreshold>`
                                
                                .. attribute:: wred_match_type
                                
                                	WREDMatchType
                                	**type**\:  :py:class:`DnxQoseaShowWred <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowWred>`
                                
                                .. attribute:: hardware_min_threshold_bytes
                                
                                	Hardware minimum threshold
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: hardware_max_threshold_bytes
                                
                                	Hardware maximum threshold
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: first_segment
                                
                                	First segment
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: segment_size
                                
                                	Segment size
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.Wred, self).__init__()

                                    self.yang_name = "wred"
                                    self.yang_parent_name = "class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("wred-match-value", ("wred_match_value", PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.Wred.WredMatchValue)), ("config-min-threshold", ("config_min_threshold", PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.Wred.ConfigMinThreshold)), ("config-max-threshold", ("config_max_threshold", PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.Wred.ConfigMaxThreshold))])
                                    self._leafs = OrderedDict([
                                        ('wred_match_type', (YLeaf(YType.enumeration, 'wred-match-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowWred', '')])),
                                        ('hardware_min_threshold_bytes', (YLeaf(YType.uint32, 'hardware-min-threshold-bytes'), ['int'])),
                                        ('hardware_max_threshold_bytes', (YLeaf(YType.uint32, 'hardware-max-threshold-bytes'), ['int'])),
                                        ('first_segment', (YLeaf(YType.uint16, 'first-segment'), ['int'])),
                                        ('segment_size', (YLeaf(YType.uint32, 'segment-size'), ['int'])),
                                    ])
                                    self.wred_match_type = None
                                    self.hardware_min_threshold_bytes = None
                                    self.hardware_max_threshold_bytes = None
                                    self.first_segment = None
                                    self.segment_size = None

                                    self.wred_match_value = PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.Wred.WredMatchValue()
                                    self.wred_match_value.parent = self
                                    self._children_name_map["wred_match_value"] = "wred-match-value"

                                    self.config_min_threshold = PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.Wred.ConfigMinThreshold()
                                    self.config_min_threshold.parent = self
                                    self._children_name_map["config_min_threshold"] = "config-min-threshold"

                                    self.config_max_threshold = PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.Wred.ConfigMaxThreshold()
                                    self.config_max_threshold.parent = self
                                    self._children_name_map["config_max_threshold"] = "config-max-threshold"
                                    self._segment_path = lambda: "wred"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.Wred, [u'wred_match_type', u'hardware_min_threshold_bytes', u'hardware_max_threshold_bytes', u'first_segment', u'segment_size'], name, value)


                                class WredMatchValue(Entity):
                                    """
                                    WRED match values
                                    
                                    .. attribute:: dnx_qosea_show_red_match_value
                                    
                                    	dnx qosea show red match value
                                    	**type**\: list of  		 :py:class:`DnxQoseaShowRedMatchValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.Wred.WredMatchValue, self).__init__()

                                        self.yang_name = "wred-match-value"
                                        self.yang_parent_name = "wred"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("dnx-qosea-show-red-match-value", ("dnx_qosea_show_red_match_value", PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue))])
                                        self._leafs = OrderedDict()

                                        self.dnx_qosea_show_red_match_value = YList(self)
                                        self._segment_path = lambda: "wred-match-value"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.Wred.WredMatchValue, [], name, value)


                                    class DnxQoseaShowRedMatchValue(Entity):
                                        """
                                        dnx qosea show red match value
                                        
                                        .. attribute:: range_start
                                        
                                        	Start value of a range
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: range_end
                                        
                                        	End value of a range
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue, self).__init__()

                                            self.yang_name = "dnx-qosea-show-red-match-value"
                                            self.yang_parent_name = "wred-match-value"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('range_start', (YLeaf(YType.uint8, 'range-start'), ['int'])),
                                                ('range_end', (YLeaf(YType.uint8, 'range-end'), ['int'])),
                                            ])
                                            self.range_start = None
                                            self.range_end = None
                                            self._segment_path = lambda: "dnx-qosea-show-red-match-value"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue, [u'range_start', u'range_end'], name, value)


                                class ConfigMinThreshold(Entity):
                                    """
                                    Configured minimum threshold
                                    
                                    .. attribute:: policy_value
                                    
                                    	Policy value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: policy_unit
                                    
                                    	Policy unit
                                    	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.Wred.ConfigMinThreshold, self).__init__()

                                        self.yang_name = "config-min-threshold"
                                        self.yang_parent_name = "wred"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                            ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                        ])
                                        self.policy_value = None
                                        self.policy_unit = None
                                        self._segment_path = lambda: "config-min-threshold"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.Wred.ConfigMinThreshold, [u'policy_value', u'policy_unit'], name, value)


                                class ConfigMaxThreshold(Entity):
                                    """
                                    Configured maximum threshold
                                    
                                    .. attribute:: policy_value
                                    
                                    	Policy value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: policy_unit
                                    
                                    	Policy unit
                                    	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.Wred.ConfigMaxThreshold, self).__init__()

                                        self.yang_name = "config-max-threshold"
                                        self.yang_parent_name = "wred"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                            ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                        ])
                                        self.policy_value = None
                                        self.policy_unit = None
                                        self._segment_path = lambda: "config-max-threshold"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.ClassTable.Class.Wred.ConfigMaxThreshold, [u'policy_value', u'policy_unit'], name, value)


            class QosInterfaces(Entity):
                """
                QoS list of interfaces
                
                .. attribute:: qos_interface
                
                	QoS interface names
                	**type**\: list of  		 :py:class:`QosInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface>`
                
                

                """

                _prefix = 'ncs5500-qos-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PlatformQos.Nodes.Node.QosInterfaces, self).__init__()

                    self.yang_name = "qos-interfaces"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("qos-interface", ("qos_interface", PlatformQos.Nodes.Node.QosInterfaces.QosInterface))])
                    self._leafs = OrderedDict()

                    self.qos_interface = YList(self)
                    self._segment_path = lambda: "qos-interfaces"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces, [], name, value)


                class QosInterface(Entity):
                    """
                    QoS interface names
                    
                    .. attribute:: interface_name  (key)
                    
                    	The name of the interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: input
                    
                    	QoS policy direction ingress
                    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input>`
                    
                    .. attribute:: output
                    
                    	QoS policy direction egress
                    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output>`
                    
                    

                    """

                    _prefix = 'ncs5500-qos-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface, self).__init__()

                        self.yang_name = "qos-interface"
                        self.yang_parent_name = "qos-interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([("input", ("input", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input)), ("output", ("output", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ])
                        self.interface_name = None

                        self.input = PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input()
                        self.input.parent = self
                        self._children_name_map["input"] = "input"

                        self.output = PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output()
                        self.output.parent = self
                        self._children_name_map["output"] = "output"
                        self._segment_path = lambda: "qos-interface" + "[interface-name='" + str(self.interface_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface, ['interface_name'], name, value)


                    class Input(Entity):
                        """
                        QoS policy direction ingress
                        
                        .. attribute:: qos_class_table
                        
                        	QoS list of class names
                        	**type**\:  :py:class:`QosClassTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable>`
                        
                        

                        """

                        _prefix = 'ncs5500-qos-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input, self).__init__()

                            self.yang_name = "input"
                            self.yang_parent_name = "qos-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("qos-class-table", ("qos_class_table", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable))])
                            self._leafs = OrderedDict()

                            self.qos_class_table = PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable()
                            self.qos_class_table.parent = self
                            self._children_name_map["qos_class_table"] = "qos-class-table"
                            self._segment_path = lambda: "input"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input, [], name, value)


                        class QosClassTable(Entity):
                            """
                            QoS list of class names
                            
                            .. attribute:: class_
                            
                            	QoS policy class
                            	**type**\: list of  		 :py:class:`Class <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class>`
                            
                            

                            """

                            _prefix = 'ncs5500-qos-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable, self).__init__()

                                self.yang_name = "qos-class-table"
                                self.yang_parent_name = "input"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("class", ("class_", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class))])
                                self._leafs = OrderedDict()

                                self.class_ = YList(self)
                                self._segment_path = lambda: "qos-class-table"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable, [], name, value)


                            class Class(Entity):
                                """
                                QoS policy class
                                
                                .. attribute:: level_one_class_name  (key)
                                
                                	QoS policy class name at level 1
                                	**type**\: str
                                
                                .. attribute:: level_two_class_name
                                
                                	QoS policy child class name at level 2
                                	**type**\: str
                                
                                .. attribute:: config_max_rate
                                
                                	Configured maximum rate
                                	**type**\:  :py:class:`ConfigMaxRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ConfigMaxRate>`
                                
                                .. attribute:: config_min_rate
                                
                                	Configured minimum rate
                                	**type**\:  :py:class:`ConfigMinRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ConfigMinRate>`
                                
                                .. attribute:: config_queue_limit
                                
                                	Configured queue limit
                                	**type**\:  :py:class:`ConfigQueueLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ConfigQueueLimit>`
                                
                                .. attribute:: config_policer_average_rate
                                
                                	Configured policer average rate
                                	**type**\:  :py:class:`ConfigPolicerAverageRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ConfigPolicerAverageRate>`
                                
                                .. attribute:: config_policer_peak_rate
                                
                                	Config policer peak rate
                                	**type**\:  :py:class:`ConfigPolicerPeakRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ConfigPolicerPeakRate>`
                                
                                .. attribute:: config_policer_conform_burst
                                
                                	Configured policer conform burst
                                	**type**\:  :py:class:`ConfigPolicerConformBurst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ConfigPolicerConformBurst>`
                                
                                .. attribute:: config_policer_excess_burst
                                
                                	Configured policer excess burst
                                	**type**\:  :py:class:`ConfigPolicerExcessBurst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ConfigPolicerExcessBurst>`
                                
                                .. attribute:: conform_action
                                
                                	Conform action
                                	**type**\:  :py:class:`ConformAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ConformAction>`
                                
                                .. attribute:: exceed_action
                                
                                	Exceed action
                                	**type**\:  :py:class:`ExceedAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ExceedAction>`
                                
                                .. attribute:: violate_action
                                
                                	Violate action
                                	**type**\:  :py:class:`ViolateAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ViolateAction>`
                                
                                .. attribute:: class_level
                                
                                	Class level
                                	**type**\:  :py:class:`DnxQoseaShowLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowLevel>`
                                
                                .. attribute:: egress_queue_id
                                
                                	Egress Queue ID
                                	**type**\: int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: queue_type
                                
                                	Queue type
                                	**type**\:  :py:class:`DnxQoseaShowQueue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowQueue>`
                                
                                .. attribute:: priority_level
                                
                                	Priority level
                                	**type**\:  :py:class:`DnxQoseaShowHpLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowHpLevel>`
                                
                                .. attribute:: hardware_max_rate_kbps
                                
                                	Hardware maximum rate in kbps
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: kbit/s
                                
                                .. attribute:: hardware_min_rate_kbps
                                
                                	Hardware minimum rate in kbps
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: kbit/s
                                
                                .. attribute:: config_excess_bandwidth_percent
                                
                                	Configured excess bandwidth percentage
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: percentage
                                
                                .. attribute:: config_excess_bandwidth_unit
                                
                                	Configured excess bandwidth unit
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: hardware_excess_bandwidth_weight
                                
                                	Hardware excess bandwidth weight
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: network_min_bandwidth_kbps
                                
                                	Network minimum Bandwith
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: hardware_queue_limit_bytes
                                
                                	Hardware queue limit in bytes
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: byte
                                
                                .. attribute:: hardware_queue_limit_microseconds
                                
                                	Hardware queue limit in microseconds
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: microsecond
                                
                                .. attribute:: policer_bucket_id
                                
                                	PolicerBucketID
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: policer_stats_handle
                                
                                	PolicerStatsHandle
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: hardware_policer_average_rate_kbps
                                
                                	Hardware policer average in kbps
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: kbit/s
                                
                                .. attribute:: hardware_policer_peak_rate_kbps
                                
                                	Hardware policer peak rate
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: hardware_policer_conform_burst_bytes
                                
                                	Hardware policer conform burst
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: hardware_policer_excess_burst_bytes
                                
                                	Hardware policer excess burst
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ip_mark
                                
                                	IP mark
                                	**type**\: list of  		 :py:class:`IpMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.IpMark>`
                                
                                .. attribute:: common_mark
                                
                                	Common mark
                                	**type**\: list of  		 :py:class:`CommonMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.CommonMark>`
                                
                                .. attribute:: mpls_mark
                                
                                	MPLS mark
                                	**type**\: list of  		 :py:class:`MplsMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.MplsMark>`
                                
                                .. attribute:: wred
                                
                                	WRED parameters
                                	**type**\: list of  		 :py:class:`Wred <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.Wred>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class, self).__init__()

                                    self.yang_name = "class"
                                    self.yang_parent_name = "qos-class-table"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['level_one_class_name']
                                    self._child_classes = OrderedDict([("config-max-rate", ("config_max_rate", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ConfigMaxRate)), ("config-min-rate", ("config_min_rate", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ConfigMinRate)), ("config-queue-limit", ("config_queue_limit", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ConfigQueueLimit)), ("config-policer-average-rate", ("config_policer_average_rate", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ConfigPolicerAverageRate)), ("config-policer-peak-rate", ("config_policer_peak_rate", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ConfigPolicerPeakRate)), ("config-policer-conform-burst", ("config_policer_conform_burst", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ConfigPolicerConformBurst)), ("config-policer-excess-burst", ("config_policer_excess_burst", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ConfigPolicerExcessBurst)), ("conform-action", ("conform_action", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ConformAction)), ("exceed-action", ("exceed_action", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ExceedAction)), ("violate-action", ("violate_action", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ViolateAction)), ("ip-mark", ("ip_mark", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.IpMark)), ("common-mark", ("common_mark", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.CommonMark)), ("mpls-mark", ("mpls_mark", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.MplsMark)), ("wred", ("wred", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.Wred))])
                                    self._leafs = OrderedDict([
                                        ('level_one_class_name', (YLeaf(YType.str, 'level-one-class-name'), ['str'])),
                                        ('level_two_class_name', (YLeaf(YType.str, 'level-two-class-name'), ['str'])),
                                        ('class_level', (YLeaf(YType.enumeration, 'class-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowLevel', '')])),
                                        ('egress_queue_id', (YLeaf(YType.int32, 'egress-queue-id'), ['int'])),
                                        ('queue_type', (YLeaf(YType.enumeration, 'queue-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowQueue', '')])),
                                        ('priority_level', (YLeaf(YType.enumeration, 'priority-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowHpLevel', '')])),
                                        ('hardware_max_rate_kbps', (YLeaf(YType.uint32, 'hardware-max-rate-kbps'), ['int'])),
                                        ('hardware_min_rate_kbps', (YLeaf(YType.uint32, 'hardware-min-rate-kbps'), ['int'])),
                                        ('config_excess_bandwidth_percent', (YLeaf(YType.uint32, 'config-excess-bandwidth-percent'), ['int'])),
                                        ('config_excess_bandwidth_unit', (YLeaf(YType.uint32, 'config-excess-bandwidth-unit'), ['int'])),
                                        ('hardware_excess_bandwidth_weight', (YLeaf(YType.uint32, 'hardware-excess-bandwidth-weight'), ['int'])),
                                        ('network_min_bandwidth_kbps', (YLeaf(YType.uint32, 'network-min-bandwidth-kbps'), ['int'])),
                                        ('hardware_queue_limit_bytes', (YLeaf(YType.uint64, 'hardware-queue-limit-bytes'), ['int'])),
                                        ('hardware_queue_limit_microseconds', (YLeaf(YType.uint64, 'hardware-queue-limit-microseconds'), ['int'])),
                                        ('policer_bucket_id', (YLeaf(YType.uint32, 'policer-bucket-id'), ['int'])),
                                        ('policer_stats_handle', (YLeaf(YType.uint64, 'policer-stats-handle'), ['int'])),
                                        ('hardware_policer_average_rate_kbps', (YLeaf(YType.uint32, 'hardware-policer-average-rate-kbps'), ['int'])),
                                        ('hardware_policer_peak_rate_kbps', (YLeaf(YType.uint32, 'hardware-policer-peak-rate-kbps'), ['int'])),
                                        ('hardware_policer_conform_burst_bytes', (YLeaf(YType.uint32, 'hardware-policer-conform-burst-bytes'), ['int'])),
                                        ('hardware_policer_excess_burst_bytes', (YLeaf(YType.uint32, 'hardware-policer-excess-burst-bytes'), ['int'])),
                                    ])
                                    self.level_one_class_name = None
                                    self.level_two_class_name = None
                                    self.class_level = None
                                    self.egress_queue_id = None
                                    self.queue_type = None
                                    self.priority_level = None
                                    self.hardware_max_rate_kbps = None
                                    self.hardware_min_rate_kbps = None
                                    self.config_excess_bandwidth_percent = None
                                    self.config_excess_bandwidth_unit = None
                                    self.hardware_excess_bandwidth_weight = None
                                    self.network_min_bandwidth_kbps = None
                                    self.hardware_queue_limit_bytes = None
                                    self.hardware_queue_limit_microseconds = None
                                    self.policer_bucket_id = None
                                    self.policer_stats_handle = None
                                    self.hardware_policer_average_rate_kbps = None
                                    self.hardware_policer_peak_rate_kbps = None
                                    self.hardware_policer_conform_burst_bytes = None
                                    self.hardware_policer_excess_burst_bytes = None

                                    self.config_max_rate = PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ConfigMaxRate()
                                    self.config_max_rate.parent = self
                                    self._children_name_map["config_max_rate"] = "config-max-rate"

                                    self.config_min_rate = PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ConfigMinRate()
                                    self.config_min_rate.parent = self
                                    self._children_name_map["config_min_rate"] = "config-min-rate"

                                    self.config_queue_limit = PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ConfigQueueLimit()
                                    self.config_queue_limit.parent = self
                                    self._children_name_map["config_queue_limit"] = "config-queue-limit"

                                    self.config_policer_average_rate = PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ConfigPolicerAverageRate()
                                    self.config_policer_average_rate.parent = self
                                    self._children_name_map["config_policer_average_rate"] = "config-policer-average-rate"

                                    self.config_policer_peak_rate = PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ConfigPolicerPeakRate()
                                    self.config_policer_peak_rate.parent = self
                                    self._children_name_map["config_policer_peak_rate"] = "config-policer-peak-rate"

                                    self.config_policer_conform_burst = PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ConfigPolicerConformBurst()
                                    self.config_policer_conform_burst.parent = self
                                    self._children_name_map["config_policer_conform_burst"] = "config-policer-conform-burst"

                                    self.config_policer_excess_burst = PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ConfigPolicerExcessBurst()
                                    self.config_policer_excess_burst.parent = self
                                    self._children_name_map["config_policer_excess_burst"] = "config-policer-excess-burst"

                                    self.conform_action = PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ConformAction()
                                    self.conform_action.parent = self
                                    self._children_name_map["conform_action"] = "conform-action"

                                    self.exceed_action = PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ExceedAction()
                                    self.exceed_action.parent = self
                                    self._children_name_map["exceed_action"] = "exceed-action"

                                    self.violate_action = PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ViolateAction()
                                    self.violate_action.parent = self
                                    self._children_name_map["violate_action"] = "violate-action"

                                    self.ip_mark = YList(self)
                                    self.common_mark = YList(self)
                                    self.mpls_mark = YList(self)
                                    self.wred = YList(self)
                                    self._segment_path = lambda: "class" + "[level-one-class-name='" + str(self.level_one_class_name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class, ['level_one_class_name', 'level_two_class_name', u'class_level', u'egress_queue_id', u'queue_type', u'priority_level', u'hardware_max_rate_kbps', u'hardware_min_rate_kbps', u'config_excess_bandwidth_percent', u'config_excess_bandwidth_unit', u'hardware_excess_bandwidth_weight', u'network_min_bandwidth_kbps', u'hardware_queue_limit_bytes', u'hardware_queue_limit_microseconds', u'policer_bucket_id', u'policer_stats_handle', u'hardware_policer_average_rate_kbps', u'hardware_policer_peak_rate_kbps', u'hardware_policer_conform_burst_bytes', u'hardware_policer_excess_burst_bytes'], name, value)


                                class ConfigMaxRate(Entity):
                                    """
                                    Configured maximum rate
                                    
                                    .. attribute:: policy_value
                                    
                                    	Policy value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: policy_unit
                                    
                                    	Policy unit
                                    	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ConfigMaxRate, self).__init__()

                                        self.yang_name = "config-max-rate"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                            ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                        ])
                                        self.policy_value = None
                                        self.policy_unit = None
                                        self._segment_path = lambda: "config-max-rate"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ConfigMaxRate, [u'policy_value', u'policy_unit'], name, value)


                                class ConfigMinRate(Entity):
                                    """
                                    Configured minimum rate
                                    
                                    .. attribute:: policy_value
                                    
                                    	Policy value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: policy_unit
                                    
                                    	Policy unit
                                    	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ConfigMinRate, self).__init__()

                                        self.yang_name = "config-min-rate"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                            ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                        ])
                                        self.policy_value = None
                                        self.policy_unit = None
                                        self._segment_path = lambda: "config-min-rate"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ConfigMinRate, [u'policy_value', u'policy_unit'], name, value)


                                class ConfigQueueLimit(Entity):
                                    """
                                    Configured queue limit
                                    
                                    .. attribute:: policy_value
                                    
                                    	Policy value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: policy_unit
                                    
                                    	Policy unit
                                    	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ConfigQueueLimit, self).__init__()

                                        self.yang_name = "config-queue-limit"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                            ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                        ])
                                        self.policy_value = None
                                        self.policy_unit = None
                                        self._segment_path = lambda: "config-queue-limit"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ConfigQueueLimit, [u'policy_value', u'policy_unit'], name, value)


                                class ConfigPolicerAverageRate(Entity):
                                    """
                                    Configured policer average rate
                                    
                                    .. attribute:: policy_value
                                    
                                    	Policy value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: policy_unit
                                    
                                    	Policy unit
                                    	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ConfigPolicerAverageRate, self).__init__()

                                        self.yang_name = "config-policer-average-rate"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                            ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                        ])
                                        self.policy_value = None
                                        self.policy_unit = None
                                        self._segment_path = lambda: "config-policer-average-rate"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ConfigPolicerAverageRate, [u'policy_value', u'policy_unit'], name, value)


                                class ConfigPolicerPeakRate(Entity):
                                    """
                                    Config policer peak rate
                                    
                                    .. attribute:: policy_value
                                    
                                    	Policy value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: policy_unit
                                    
                                    	Policy unit
                                    	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ConfigPolicerPeakRate, self).__init__()

                                        self.yang_name = "config-policer-peak-rate"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                            ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                        ])
                                        self.policy_value = None
                                        self.policy_unit = None
                                        self._segment_path = lambda: "config-policer-peak-rate"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ConfigPolicerPeakRate, [u'policy_value', u'policy_unit'], name, value)


                                class ConfigPolicerConformBurst(Entity):
                                    """
                                    Configured policer conform burst
                                    
                                    .. attribute:: policy_value
                                    
                                    	Policy value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: policy_unit
                                    
                                    	Policy unit
                                    	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ConfigPolicerConformBurst, self).__init__()

                                        self.yang_name = "config-policer-conform-burst"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                            ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                        ])
                                        self.policy_value = None
                                        self.policy_unit = None
                                        self._segment_path = lambda: "config-policer-conform-burst"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ConfigPolicerConformBurst, [u'policy_value', u'policy_unit'], name, value)


                                class ConfigPolicerExcessBurst(Entity):
                                    """
                                    Configured policer excess burst
                                    
                                    .. attribute:: policy_value
                                    
                                    	Policy value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: policy_unit
                                    
                                    	Policy unit
                                    	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ConfigPolicerExcessBurst, self).__init__()

                                        self.yang_name = "config-policer-excess-burst"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                            ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                        ])
                                        self.policy_value = None
                                        self.policy_unit = None
                                        self._segment_path = lambda: "config-policer-excess-burst"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ConfigPolicerExcessBurst, [u'policy_value', u'policy_unit'], name, value)


                                class ConformAction(Entity):
                                    """
                                    Conform action
                                    
                                    .. attribute:: action_type
                                    
                                    	Policer action type
                                    	**type**\:  :py:class:`DnxQoseaShowAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowAction>`
                                    
                                    .. attribute:: mark
                                    
                                    	Action mark
                                    	**type**\: list of  		 :py:class:`Mark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ConformAction.Mark>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ConformAction, self).__init__()

                                        self.yang_name = "conform-action"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("mark", ("mark", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ConformAction.Mark))])
                                        self._leafs = OrderedDict([
                                            ('action_type', (YLeaf(YType.enumeration, 'action-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowAction', '')])),
                                        ])
                                        self.action_type = None

                                        self.mark = YList(self)
                                        self._segment_path = lambda: "conform-action"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ConformAction, [u'action_type'], name, value)


                                    class Mark(Entity):
                                        """
                                        Action mark
                                        
                                        .. attribute:: mark_type
                                        
                                        	Mark type
                                        	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                        
                                        .. attribute:: mark_value
                                        
                                        	Mark value
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ConformAction.Mark, self).__init__()

                                            self.yang_name = "mark"
                                            self.yang_parent_name = "conform-action"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                                ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                            ])
                                            self.mark_type = None
                                            self.mark_value = None
                                            self._segment_path = lambda: "mark"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ConformAction.Mark, [u'mark_type', u'mark_value'], name, value)


                                class ExceedAction(Entity):
                                    """
                                    Exceed action
                                    
                                    .. attribute:: action_type
                                    
                                    	Policer action type
                                    	**type**\:  :py:class:`DnxQoseaShowAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowAction>`
                                    
                                    .. attribute:: mark
                                    
                                    	Action mark
                                    	**type**\: list of  		 :py:class:`Mark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ExceedAction.Mark>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ExceedAction, self).__init__()

                                        self.yang_name = "exceed-action"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("mark", ("mark", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ExceedAction.Mark))])
                                        self._leafs = OrderedDict([
                                            ('action_type', (YLeaf(YType.enumeration, 'action-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowAction', '')])),
                                        ])
                                        self.action_type = None

                                        self.mark = YList(self)
                                        self._segment_path = lambda: "exceed-action"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ExceedAction, [u'action_type'], name, value)


                                    class Mark(Entity):
                                        """
                                        Action mark
                                        
                                        .. attribute:: mark_type
                                        
                                        	Mark type
                                        	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                        
                                        .. attribute:: mark_value
                                        
                                        	Mark value
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ExceedAction.Mark, self).__init__()

                                            self.yang_name = "mark"
                                            self.yang_parent_name = "exceed-action"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                                ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                            ])
                                            self.mark_type = None
                                            self.mark_value = None
                                            self._segment_path = lambda: "mark"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ExceedAction.Mark, [u'mark_type', u'mark_value'], name, value)


                                class ViolateAction(Entity):
                                    """
                                    Violate action
                                    
                                    .. attribute:: action_type
                                    
                                    	Policer action type
                                    	**type**\:  :py:class:`DnxQoseaShowAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowAction>`
                                    
                                    .. attribute:: mark
                                    
                                    	Action mark
                                    	**type**\: list of  		 :py:class:`Mark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ViolateAction.Mark>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ViolateAction, self).__init__()

                                        self.yang_name = "violate-action"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("mark", ("mark", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ViolateAction.Mark))])
                                        self._leafs = OrderedDict([
                                            ('action_type', (YLeaf(YType.enumeration, 'action-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowAction', '')])),
                                        ])
                                        self.action_type = None

                                        self.mark = YList(self)
                                        self._segment_path = lambda: "violate-action"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ViolateAction, [u'action_type'], name, value)


                                    class Mark(Entity):
                                        """
                                        Action mark
                                        
                                        .. attribute:: mark_type
                                        
                                        	Mark type
                                        	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                        
                                        .. attribute:: mark_value
                                        
                                        	Mark value
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ViolateAction.Mark, self).__init__()

                                            self.yang_name = "mark"
                                            self.yang_parent_name = "violate-action"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                                ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                            ])
                                            self.mark_type = None
                                            self.mark_value = None
                                            self._segment_path = lambda: "mark"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.ViolateAction.Mark, [u'mark_type', u'mark_value'], name, value)


                                class IpMark(Entity):
                                    """
                                    IP mark
                                    
                                    .. attribute:: mark_type
                                    
                                    	Mark type
                                    	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                    
                                    .. attribute:: mark_value
                                    
                                    	Mark value
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.IpMark, self).__init__()

                                        self.yang_name = "ip-mark"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                            ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                        ])
                                        self.mark_type = None
                                        self.mark_value = None
                                        self._segment_path = lambda: "ip-mark"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.IpMark, [u'mark_type', u'mark_value'], name, value)


                                class CommonMark(Entity):
                                    """
                                    Common mark
                                    
                                    .. attribute:: mark_type
                                    
                                    	Mark type
                                    	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                    
                                    .. attribute:: mark_value
                                    
                                    	Mark value
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.CommonMark, self).__init__()

                                        self.yang_name = "common-mark"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                            ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                        ])
                                        self.mark_type = None
                                        self.mark_value = None
                                        self._segment_path = lambda: "common-mark"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.CommonMark, [u'mark_type', u'mark_value'], name, value)


                                class MplsMark(Entity):
                                    """
                                    MPLS mark
                                    
                                    .. attribute:: mark_type
                                    
                                    	Mark type
                                    	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                    
                                    .. attribute:: mark_value
                                    
                                    	Mark value
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.MplsMark, self).__init__()

                                        self.yang_name = "mpls-mark"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                            ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                        ])
                                        self.mark_type = None
                                        self.mark_value = None
                                        self._segment_path = lambda: "mpls-mark"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.MplsMark, [u'mark_type', u'mark_value'], name, value)


                                class Wred(Entity):
                                    """
                                    WRED parameters
                                    
                                    .. attribute:: wred_match_value
                                    
                                    	WRED match values
                                    	**type**\:  :py:class:`WredMatchValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.Wred.WredMatchValue>`
                                    
                                    .. attribute:: config_min_threshold
                                    
                                    	Configured minimum threshold
                                    	**type**\:  :py:class:`ConfigMinThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.Wred.ConfigMinThreshold>`
                                    
                                    .. attribute:: config_max_threshold
                                    
                                    	Configured maximum threshold
                                    	**type**\:  :py:class:`ConfigMaxThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.Wred.ConfigMaxThreshold>`
                                    
                                    .. attribute:: wred_match_type
                                    
                                    	WREDMatchType
                                    	**type**\:  :py:class:`DnxQoseaShowWred <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowWred>`
                                    
                                    .. attribute:: hardware_min_threshold_bytes
                                    
                                    	Hardware minimum threshold
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: hardware_max_threshold_bytes
                                    
                                    	Hardware maximum threshold
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: first_segment
                                    
                                    	First segment
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: segment_size
                                    
                                    	Segment size
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.Wred, self).__init__()

                                        self.yang_name = "wred"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("wred-match-value", ("wred_match_value", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.Wred.WredMatchValue)), ("config-min-threshold", ("config_min_threshold", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.Wred.ConfigMinThreshold)), ("config-max-threshold", ("config_max_threshold", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.Wred.ConfigMaxThreshold))])
                                        self._leafs = OrderedDict([
                                            ('wred_match_type', (YLeaf(YType.enumeration, 'wred-match-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowWred', '')])),
                                            ('hardware_min_threshold_bytes', (YLeaf(YType.uint32, 'hardware-min-threshold-bytes'), ['int'])),
                                            ('hardware_max_threshold_bytes', (YLeaf(YType.uint32, 'hardware-max-threshold-bytes'), ['int'])),
                                            ('first_segment', (YLeaf(YType.uint16, 'first-segment'), ['int'])),
                                            ('segment_size', (YLeaf(YType.uint32, 'segment-size'), ['int'])),
                                        ])
                                        self.wred_match_type = None
                                        self.hardware_min_threshold_bytes = None
                                        self.hardware_max_threshold_bytes = None
                                        self.first_segment = None
                                        self.segment_size = None

                                        self.wred_match_value = PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.Wred.WredMatchValue()
                                        self.wred_match_value.parent = self
                                        self._children_name_map["wred_match_value"] = "wred-match-value"

                                        self.config_min_threshold = PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.Wred.ConfigMinThreshold()
                                        self.config_min_threshold.parent = self
                                        self._children_name_map["config_min_threshold"] = "config-min-threshold"

                                        self.config_max_threshold = PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.Wred.ConfigMaxThreshold()
                                        self.config_max_threshold.parent = self
                                        self._children_name_map["config_max_threshold"] = "config-max-threshold"
                                        self._segment_path = lambda: "wred"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.Wred, [u'wred_match_type', u'hardware_min_threshold_bytes', u'hardware_max_threshold_bytes', u'first_segment', u'segment_size'], name, value)


                                    class WredMatchValue(Entity):
                                        """
                                        WRED match values
                                        
                                        .. attribute:: dnx_qosea_show_red_match_value
                                        
                                        	dnx qosea show red match value
                                        	**type**\: list of  		 :py:class:`DnxQoseaShowRedMatchValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue>`
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.Wred.WredMatchValue, self).__init__()

                                            self.yang_name = "wred-match-value"
                                            self.yang_parent_name = "wred"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("dnx-qosea-show-red-match-value", ("dnx_qosea_show_red_match_value", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue))])
                                            self._leafs = OrderedDict()

                                            self.dnx_qosea_show_red_match_value = YList(self)
                                            self._segment_path = lambda: "wred-match-value"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.Wred.WredMatchValue, [], name, value)


                                        class DnxQoseaShowRedMatchValue(Entity):
                                            """
                                            dnx qosea show red match value
                                            
                                            .. attribute:: range_start
                                            
                                            	Start value of a range
                                            	**type**\: int
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: range_end
                                            
                                            	End value of a range
                                            	**type**\: int
                                            
                                            	**range:** 0..255
                                            
                                            

                                            """

                                            _prefix = 'ncs5500-qos-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue, self).__init__()

                                                self.yang_name = "dnx-qosea-show-red-match-value"
                                                self.yang_parent_name = "wred-match-value"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('range_start', (YLeaf(YType.uint8, 'range-start'), ['int'])),
                                                    ('range_end', (YLeaf(YType.uint8, 'range-end'), ['int'])),
                                                ])
                                                self.range_start = None
                                                self.range_end = None
                                                self._segment_path = lambda: "dnx-qosea-show-red-match-value"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue, [u'range_start', u'range_end'], name, value)


                                    class ConfigMinThreshold(Entity):
                                        """
                                        Configured minimum threshold
                                        
                                        .. attribute:: policy_value
                                        
                                        	Policy value
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: policy_unit
                                        
                                        	Policy unit
                                        	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.Wred.ConfigMinThreshold, self).__init__()

                                            self.yang_name = "config-min-threshold"
                                            self.yang_parent_name = "wred"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                                ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                            ])
                                            self.policy_value = None
                                            self.policy_unit = None
                                            self._segment_path = lambda: "config-min-threshold"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.Wred.ConfigMinThreshold, [u'policy_value', u'policy_unit'], name, value)


                                    class ConfigMaxThreshold(Entity):
                                        """
                                        Configured maximum threshold
                                        
                                        .. attribute:: policy_value
                                        
                                        	Policy value
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: policy_unit
                                        
                                        	Policy unit
                                        	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.Wred.ConfigMaxThreshold, self).__init__()

                                            self.yang_name = "config-max-threshold"
                                            self.yang_parent_name = "wred"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                                ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                            ])
                                            self.policy_value = None
                                            self.policy_unit = None
                                            self._segment_path = lambda: "config-max-threshold"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Input.QosClassTable.Class.Wred.ConfigMaxThreshold, [u'policy_value', u'policy_unit'], name, value)


                    class Output(Entity):
                        """
                        QoS policy direction egress
                        
                        .. attribute:: qos_class_table
                        
                        	QoS list of class names
                        	**type**\:  :py:class:`QosClassTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable>`
                        
                        

                        """

                        _prefix = 'ncs5500-qos-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output, self).__init__()

                            self.yang_name = "output"
                            self.yang_parent_name = "qos-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("qos-class-table", ("qos_class_table", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable))])
                            self._leafs = OrderedDict()

                            self.qos_class_table = PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable()
                            self.qos_class_table.parent = self
                            self._children_name_map["qos_class_table"] = "qos-class-table"
                            self._segment_path = lambda: "output"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output, [], name, value)


                        class QosClassTable(Entity):
                            """
                            QoS list of class names
                            
                            .. attribute:: class_
                            
                            	QoS policy class
                            	**type**\: list of  		 :py:class:`Class <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class>`
                            
                            

                            """

                            _prefix = 'ncs5500-qos-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable, self).__init__()

                                self.yang_name = "qos-class-table"
                                self.yang_parent_name = "output"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("class", ("class_", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class))])
                                self._leafs = OrderedDict()

                                self.class_ = YList(self)
                                self._segment_path = lambda: "qos-class-table"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable, [], name, value)


                            class Class(Entity):
                                """
                                QoS policy class
                                
                                .. attribute:: level_one_class_name  (key)
                                
                                	QoS policy class name at level 1
                                	**type**\: str
                                
                                .. attribute:: level_two_class_name
                                
                                	QoS policy child class name at level 2
                                	**type**\: str
                                
                                .. attribute:: config_max_rate
                                
                                	Configured maximum rate
                                	**type**\:  :py:class:`ConfigMaxRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ConfigMaxRate>`
                                
                                .. attribute:: config_min_rate
                                
                                	Configured minimum rate
                                	**type**\:  :py:class:`ConfigMinRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ConfigMinRate>`
                                
                                .. attribute:: config_queue_limit
                                
                                	Configured queue limit
                                	**type**\:  :py:class:`ConfigQueueLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ConfigQueueLimit>`
                                
                                .. attribute:: config_policer_average_rate
                                
                                	Configured policer average rate
                                	**type**\:  :py:class:`ConfigPolicerAverageRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ConfigPolicerAverageRate>`
                                
                                .. attribute:: config_policer_peak_rate
                                
                                	Config policer peak rate
                                	**type**\:  :py:class:`ConfigPolicerPeakRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ConfigPolicerPeakRate>`
                                
                                .. attribute:: config_policer_conform_burst
                                
                                	Configured policer conform burst
                                	**type**\:  :py:class:`ConfigPolicerConformBurst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ConfigPolicerConformBurst>`
                                
                                .. attribute:: config_policer_excess_burst
                                
                                	Configured policer excess burst
                                	**type**\:  :py:class:`ConfigPolicerExcessBurst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ConfigPolicerExcessBurst>`
                                
                                .. attribute:: conform_action
                                
                                	Conform action
                                	**type**\:  :py:class:`ConformAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ConformAction>`
                                
                                .. attribute:: exceed_action
                                
                                	Exceed action
                                	**type**\:  :py:class:`ExceedAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ExceedAction>`
                                
                                .. attribute:: violate_action
                                
                                	Violate action
                                	**type**\:  :py:class:`ViolateAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ViolateAction>`
                                
                                .. attribute:: class_level
                                
                                	Class level
                                	**type**\:  :py:class:`DnxQoseaShowLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowLevel>`
                                
                                .. attribute:: egress_queue_id
                                
                                	Egress Queue ID
                                	**type**\: int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: queue_type
                                
                                	Queue type
                                	**type**\:  :py:class:`DnxQoseaShowQueue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowQueue>`
                                
                                .. attribute:: priority_level
                                
                                	Priority level
                                	**type**\:  :py:class:`DnxQoseaShowHpLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowHpLevel>`
                                
                                .. attribute:: hardware_max_rate_kbps
                                
                                	Hardware maximum rate in kbps
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: kbit/s
                                
                                .. attribute:: hardware_min_rate_kbps
                                
                                	Hardware minimum rate in kbps
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: kbit/s
                                
                                .. attribute:: config_excess_bandwidth_percent
                                
                                	Configured excess bandwidth percentage
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: percentage
                                
                                .. attribute:: config_excess_bandwidth_unit
                                
                                	Configured excess bandwidth unit
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: hardware_excess_bandwidth_weight
                                
                                	Hardware excess bandwidth weight
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: network_min_bandwidth_kbps
                                
                                	Network minimum Bandwith
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: hardware_queue_limit_bytes
                                
                                	Hardware queue limit in bytes
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: byte
                                
                                .. attribute:: hardware_queue_limit_microseconds
                                
                                	Hardware queue limit in microseconds
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: microsecond
                                
                                .. attribute:: policer_bucket_id
                                
                                	PolicerBucketID
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: policer_stats_handle
                                
                                	PolicerStatsHandle
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: hardware_policer_average_rate_kbps
                                
                                	Hardware policer average in kbps
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: kbit/s
                                
                                .. attribute:: hardware_policer_peak_rate_kbps
                                
                                	Hardware policer peak rate
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: hardware_policer_conform_burst_bytes
                                
                                	Hardware policer conform burst
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: hardware_policer_excess_burst_bytes
                                
                                	Hardware policer excess burst
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ip_mark
                                
                                	IP mark
                                	**type**\: list of  		 :py:class:`IpMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.IpMark>`
                                
                                .. attribute:: common_mark
                                
                                	Common mark
                                	**type**\: list of  		 :py:class:`CommonMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.CommonMark>`
                                
                                .. attribute:: mpls_mark
                                
                                	MPLS mark
                                	**type**\: list of  		 :py:class:`MplsMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.MplsMark>`
                                
                                .. attribute:: wred
                                
                                	WRED parameters
                                	**type**\: list of  		 :py:class:`Wred <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.Wred>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class, self).__init__()

                                    self.yang_name = "class"
                                    self.yang_parent_name = "qos-class-table"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['level_one_class_name']
                                    self._child_classes = OrderedDict([("config-max-rate", ("config_max_rate", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ConfigMaxRate)), ("config-min-rate", ("config_min_rate", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ConfigMinRate)), ("config-queue-limit", ("config_queue_limit", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ConfigQueueLimit)), ("config-policer-average-rate", ("config_policer_average_rate", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ConfigPolicerAverageRate)), ("config-policer-peak-rate", ("config_policer_peak_rate", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ConfigPolicerPeakRate)), ("config-policer-conform-burst", ("config_policer_conform_burst", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ConfigPolicerConformBurst)), ("config-policer-excess-burst", ("config_policer_excess_burst", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ConfigPolicerExcessBurst)), ("conform-action", ("conform_action", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ConformAction)), ("exceed-action", ("exceed_action", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ExceedAction)), ("violate-action", ("violate_action", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ViolateAction)), ("ip-mark", ("ip_mark", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.IpMark)), ("common-mark", ("common_mark", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.CommonMark)), ("mpls-mark", ("mpls_mark", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.MplsMark)), ("wred", ("wred", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.Wred))])
                                    self._leafs = OrderedDict([
                                        ('level_one_class_name', (YLeaf(YType.str, 'level-one-class-name'), ['str'])),
                                        ('level_two_class_name', (YLeaf(YType.str, 'level-two-class-name'), ['str'])),
                                        ('class_level', (YLeaf(YType.enumeration, 'class-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowLevel', '')])),
                                        ('egress_queue_id', (YLeaf(YType.int32, 'egress-queue-id'), ['int'])),
                                        ('queue_type', (YLeaf(YType.enumeration, 'queue-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowQueue', '')])),
                                        ('priority_level', (YLeaf(YType.enumeration, 'priority-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowHpLevel', '')])),
                                        ('hardware_max_rate_kbps', (YLeaf(YType.uint32, 'hardware-max-rate-kbps'), ['int'])),
                                        ('hardware_min_rate_kbps', (YLeaf(YType.uint32, 'hardware-min-rate-kbps'), ['int'])),
                                        ('config_excess_bandwidth_percent', (YLeaf(YType.uint32, 'config-excess-bandwidth-percent'), ['int'])),
                                        ('config_excess_bandwidth_unit', (YLeaf(YType.uint32, 'config-excess-bandwidth-unit'), ['int'])),
                                        ('hardware_excess_bandwidth_weight', (YLeaf(YType.uint32, 'hardware-excess-bandwidth-weight'), ['int'])),
                                        ('network_min_bandwidth_kbps', (YLeaf(YType.uint32, 'network-min-bandwidth-kbps'), ['int'])),
                                        ('hardware_queue_limit_bytes', (YLeaf(YType.uint64, 'hardware-queue-limit-bytes'), ['int'])),
                                        ('hardware_queue_limit_microseconds', (YLeaf(YType.uint64, 'hardware-queue-limit-microseconds'), ['int'])),
                                        ('policer_bucket_id', (YLeaf(YType.uint32, 'policer-bucket-id'), ['int'])),
                                        ('policer_stats_handle', (YLeaf(YType.uint64, 'policer-stats-handle'), ['int'])),
                                        ('hardware_policer_average_rate_kbps', (YLeaf(YType.uint32, 'hardware-policer-average-rate-kbps'), ['int'])),
                                        ('hardware_policer_peak_rate_kbps', (YLeaf(YType.uint32, 'hardware-policer-peak-rate-kbps'), ['int'])),
                                        ('hardware_policer_conform_burst_bytes', (YLeaf(YType.uint32, 'hardware-policer-conform-burst-bytes'), ['int'])),
                                        ('hardware_policer_excess_burst_bytes', (YLeaf(YType.uint32, 'hardware-policer-excess-burst-bytes'), ['int'])),
                                    ])
                                    self.level_one_class_name = None
                                    self.level_two_class_name = None
                                    self.class_level = None
                                    self.egress_queue_id = None
                                    self.queue_type = None
                                    self.priority_level = None
                                    self.hardware_max_rate_kbps = None
                                    self.hardware_min_rate_kbps = None
                                    self.config_excess_bandwidth_percent = None
                                    self.config_excess_bandwidth_unit = None
                                    self.hardware_excess_bandwidth_weight = None
                                    self.network_min_bandwidth_kbps = None
                                    self.hardware_queue_limit_bytes = None
                                    self.hardware_queue_limit_microseconds = None
                                    self.policer_bucket_id = None
                                    self.policer_stats_handle = None
                                    self.hardware_policer_average_rate_kbps = None
                                    self.hardware_policer_peak_rate_kbps = None
                                    self.hardware_policer_conform_burst_bytes = None
                                    self.hardware_policer_excess_burst_bytes = None

                                    self.config_max_rate = PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ConfigMaxRate()
                                    self.config_max_rate.parent = self
                                    self._children_name_map["config_max_rate"] = "config-max-rate"

                                    self.config_min_rate = PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ConfigMinRate()
                                    self.config_min_rate.parent = self
                                    self._children_name_map["config_min_rate"] = "config-min-rate"

                                    self.config_queue_limit = PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ConfigQueueLimit()
                                    self.config_queue_limit.parent = self
                                    self._children_name_map["config_queue_limit"] = "config-queue-limit"

                                    self.config_policer_average_rate = PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ConfigPolicerAverageRate()
                                    self.config_policer_average_rate.parent = self
                                    self._children_name_map["config_policer_average_rate"] = "config-policer-average-rate"

                                    self.config_policer_peak_rate = PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ConfigPolicerPeakRate()
                                    self.config_policer_peak_rate.parent = self
                                    self._children_name_map["config_policer_peak_rate"] = "config-policer-peak-rate"

                                    self.config_policer_conform_burst = PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ConfigPolicerConformBurst()
                                    self.config_policer_conform_burst.parent = self
                                    self._children_name_map["config_policer_conform_burst"] = "config-policer-conform-burst"

                                    self.config_policer_excess_burst = PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ConfigPolicerExcessBurst()
                                    self.config_policer_excess_burst.parent = self
                                    self._children_name_map["config_policer_excess_burst"] = "config-policer-excess-burst"

                                    self.conform_action = PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ConformAction()
                                    self.conform_action.parent = self
                                    self._children_name_map["conform_action"] = "conform-action"

                                    self.exceed_action = PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ExceedAction()
                                    self.exceed_action.parent = self
                                    self._children_name_map["exceed_action"] = "exceed-action"

                                    self.violate_action = PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ViolateAction()
                                    self.violate_action.parent = self
                                    self._children_name_map["violate_action"] = "violate-action"

                                    self.ip_mark = YList(self)
                                    self.common_mark = YList(self)
                                    self.mpls_mark = YList(self)
                                    self.wred = YList(self)
                                    self._segment_path = lambda: "class" + "[level-one-class-name='" + str(self.level_one_class_name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class, ['level_one_class_name', 'level_two_class_name', u'class_level', u'egress_queue_id', u'queue_type', u'priority_level', u'hardware_max_rate_kbps', u'hardware_min_rate_kbps', u'config_excess_bandwidth_percent', u'config_excess_bandwidth_unit', u'hardware_excess_bandwidth_weight', u'network_min_bandwidth_kbps', u'hardware_queue_limit_bytes', u'hardware_queue_limit_microseconds', u'policer_bucket_id', u'policer_stats_handle', u'hardware_policer_average_rate_kbps', u'hardware_policer_peak_rate_kbps', u'hardware_policer_conform_burst_bytes', u'hardware_policer_excess_burst_bytes'], name, value)


                                class ConfigMaxRate(Entity):
                                    """
                                    Configured maximum rate
                                    
                                    .. attribute:: policy_value
                                    
                                    	Policy value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: policy_unit
                                    
                                    	Policy unit
                                    	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ConfigMaxRate, self).__init__()

                                        self.yang_name = "config-max-rate"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                            ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                        ])
                                        self.policy_value = None
                                        self.policy_unit = None
                                        self._segment_path = lambda: "config-max-rate"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ConfigMaxRate, [u'policy_value', u'policy_unit'], name, value)


                                class ConfigMinRate(Entity):
                                    """
                                    Configured minimum rate
                                    
                                    .. attribute:: policy_value
                                    
                                    	Policy value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: policy_unit
                                    
                                    	Policy unit
                                    	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ConfigMinRate, self).__init__()

                                        self.yang_name = "config-min-rate"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                            ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                        ])
                                        self.policy_value = None
                                        self.policy_unit = None
                                        self._segment_path = lambda: "config-min-rate"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ConfigMinRate, [u'policy_value', u'policy_unit'], name, value)


                                class ConfigQueueLimit(Entity):
                                    """
                                    Configured queue limit
                                    
                                    .. attribute:: policy_value
                                    
                                    	Policy value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: policy_unit
                                    
                                    	Policy unit
                                    	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ConfigQueueLimit, self).__init__()

                                        self.yang_name = "config-queue-limit"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                            ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                        ])
                                        self.policy_value = None
                                        self.policy_unit = None
                                        self._segment_path = lambda: "config-queue-limit"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ConfigQueueLimit, [u'policy_value', u'policy_unit'], name, value)


                                class ConfigPolicerAverageRate(Entity):
                                    """
                                    Configured policer average rate
                                    
                                    .. attribute:: policy_value
                                    
                                    	Policy value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: policy_unit
                                    
                                    	Policy unit
                                    	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ConfigPolicerAverageRate, self).__init__()

                                        self.yang_name = "config-policer-average-rate"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                            ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                        ])
                                        self.policy_value = None
                                        self.policy_unit = None
                                        self._segment_path = lambda: "config-policer-average-rate"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ConfigPolicerAverageRate, [u'policy_value', u'policy_unit'], name, value)


                                class ConfigPolicerPeakRate(Entity):
                                    """
                                    Config policer peak rate
                                    
                                    .. attribute:: policy_value
                                    
                                    	Policy value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: policy_unit
                                    
                                    	Policy unit
                                    	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ConfigPolicerPeakRate, self).__init__()

                                        self.yang_name = "config-policer-peak-rate"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                            ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                        ])
                                        self.policy_value = None
                                        self.policy_unit = None
                                        self._segment_path = lambda: "config-policer-peak-rate"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ConfigPolicerPeakRate, [u'policy_value', u'policy_unit'], name, value)


                                class ConfigPolicerConformBurst(Entity):
                                    """
                                    Configured policer conform burst
                                    
                                    .. attribute:: policy_value
                                    
                                    	Policy value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: policy_unit
                                    
                                    	Policy unit
                                    	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ConfigPolicerConformBurst, self).__init__()

                                        self.yang_name = "config-policer-conform-burst"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                            ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                        ])
                                        self.policy_value = None
                                        self.policy_unit = None
                                        self._segment_path = lambda: "config-policer-conform-burst"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ConfigPolicerConformBurst, [u'policy_value', u'policy_unit'], name, value)


                                class ConfigPolicerExcessBurst(Entity):
                                    """
                                    Configured policer excess burst
                                    
                                    .. attribute:: policy_value
                                    
                                    	Policy value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: policy_unit
                                    
                                    	Policy unit
                                    	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ConfigPolicerExcessBurst, self).__init__()

                                        self.yang_name = "config-policer-excess-burst"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                            ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                        ])
                                        self.policy_value = None
                                        self.policy_unit = None
                                        self._segment_path = lambda: "config-policer-excess-burst"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ConfigPolicerExcessBurst, [u'policy_value', u'policy_unit'], name, value)


                                class ConformAction(Entity):
                                    """
                                    Conform action
                                    
                                    .. attribute:: action_type
                                    
                                    	Policer action type
                                    	**type**\:  :py:class:`DnxQoseaShowAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowAction>`
                                    
                                    .. attribute:: mark
                                    
                                    	Action mark
                                    	**type**\: list of  		 :py:class:`Mark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ConformAction.Mark>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ConformAction, self).__init__()

                                        self.yang_name = "conform-action"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("mark", ("mark", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ConformAction.Mark))])
                                        self._leafs = OrderedDict([
                                            ('action_type', (YLeaf(YType.enumeration, 'action-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowAction', '')])),
                                        ])
                                        self.action_type = None

                                        self.mark = YList(self)
                                        self._segment_path = lambda: "conform-action"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ConformAction, [u'action_type'], name, value)


                                    class Mark(Entity):
                                        """
                                        Action mark
                                        
                                        .. attribute:: mark_type
                                        
                                        	Mark type
                                        	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                        
                                        .. attribute:: mark_value
                                        
                                        	Mark value
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ConformAction.Mark, self).__init__()

                                            self.yang_name = "mark"
                                            self.yang_parent_name = "conform-action"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                                ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                            ])
                                            self.mark_type = None
                                            self.mark_value = None
                                            self._segment_path = lambda: "mark"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ConformAction.Mark, [u'mark_type', u'mark_value'], name, value)


                                class ExceedAction(Entity):
                                    """
                                    Exceed action
                                    
                                    .. attribute:: action_type
                                    
                                    	Policer action type
                                    	**type**\:  :py:class:`DnxQoseaShowAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowAction>`
                                    
                                    .. attribute:: mark
                                    
                                    	Action mark
                                    	**type**\: list of  		 :py:class:`Mark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ExceedAction.Mark>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ExceedAction, self).__init__()

                                        self.yang_name = "exceed-action"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("mark", ("mark", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ExceedAction.Mark))])
                                        self._leafs = OrderedDict([
                                            ('action_type', (YLeaf(YType.enumeration, 'action-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowAction', '')])),
                                        ])
                                        self.action_type = None

                                        self.mark = YList(self)
                                        self._segment_path = lambda: "exceed-action"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ExceedAction, [u'action_type'], name, value)


                                    class Mark(Entity):
                                        """
                                        Action mark
                                        
                                        .. attribute:: mark_type
                                        
                                        	Mark type
                                        	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                        
                                        .. attribute:: mark_value
                                        
                                        	Mark value
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ExceedAction.Mark, self).__init__()

                                            self.yang_name = "mark"
                                            self.yang_parent_name = "exceed-action"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                                ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                            ])
                                            self.mark_type = None
                                            self.mark_value = None
                                            self._segment_path = lambda: "mark"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ExceedAction.Mark, [u'mark_type', u'mark_value'], name, value)


                                class ViolateAction(Entity):
                                    """
                                    Violate action
                                    
                                    .. attribute:: action_type
                                    
                                    	Policer action type
                                    	**type**\:  :py:class:`DnxQoseaShowAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowAction>`
                                    
                                    .. attribute:: mark
                                    
                                    	Action mark
                                    	**type**\: list of  		 :py:class:`Mark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ViolateAction.Mark>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ViolateAction, self).__init__()

                                        self.yang_name = "violate-action"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("mark", ("mark", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ViolateAction.Mark))])
                                        self._leafs = OrderedDict([
                                            ('action_type', (YLeaf(YType.enumeration, 'action-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowAction', '')])),
                                        ])
                                        self.action_type = None

                                        self.mark = YList(self)
                                        self._segment_path = lambda: "violate-action"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ViolateAction, [u'action_type'], name, value)


                                    class Mark(Entity):
                                        """
                                        Action mark
                                        
                                        .. attribute:: mark_type
                                        
                                        	Mark type
                                        	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                        
                                        .. attribute:: mark_value
                                        
                                        	Mark value
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ViolateAction.Mark, self).__init__()

                                            self.yang_name = "mark"
                                            self.yang_parent_name = "violate-action"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                                ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                            ])
                                            self.mark_type = None
                                            self.mark_value = None
                                            self._segment_path = lambda: "mark"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.ViolateAction.Mark, [u'mark_type', u'mark_value'], name, value)


                                class IpMark(Entity):
                                    """
                                    IP mark
                                    
                                    .. attribute:: mark_type
                                    
                                    	Mark type
                                    	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                    
                                    .. attribute:: mark_value
                                    
                                    	Mark value
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.IpMark, self).__init__()

                                        self.yang_name = "ip-mark"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                            ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                        ])
                                        self.mark_type = None
                                        self.mark_value = None
                                        self._segment_path = lambda: "ip-mark"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.IpMark, [u'mark_type', u'mark_value'], name, value)


                                class CommonMark(Entity):
                                    """
                                    Common mark
                                    
                                    .. attribute:: mark_type
                                    
                                    	Mark type
                                    	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                    
                                    .. attribute:: mark_value
                                    
                                    	Mark value
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.CommonMark, self).__init__()

                                        self.yang_name = "common-mark"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                            ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                        ])
                                        self.mark_type = None
                                        self.mark_value = None
                                        self._segment_path = lambda: "common-mark"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.CommonMark, [u'mark_type', u'mark_value'], name, value)


                                class MplsMark(Entity):
                                    """
                                    MPLS mark
                                    
                                    .. attribute:: mark_type
                                    
                                    	Mark type
                                    	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                    
                                    .. attribute:: mark_value
                                    
                                    	Mark value
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.MplsMark, self).__init__()

                                        self.yang_name = "mpls-mark"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                            ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                        ])
                                        self.mark_type = None
                                        self.mark_value = None
                                        self._segment_path = lambda: "mpls-mark"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.MplsMark, [u'mark_type', u'mark_value'], name, value)


                                class Wred(Entity):
                                    """
                                    WRED parameters
                                    
                                    .. attribute:: wred_match_value
                                    
                                    	WRED match values
                                    	**type**\:  :py:class:`WredMatchValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.Wred.WredMatchValue>`
                                    
                                    .. attribute:: config_min_threshold
                                    
                                    	Configured minimum threshold
                                    	**type**\:  :py:class:`ConfigMinThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.Wred.ConfigMinThreshold>`
                                    
                                    .. attribute:: config_max_threshold
                                    
                                    	Configured maximum threshold
                                    	**type**\:  :py:class:`ConfigMaxThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.Wred.ConfigMaxThreshold>`
                                    
                                    .. attribute:: wred_match_type
                                    
                                    	WREDMatchType
                                    	**type**\:  :py:class:`DnxQoseaShowWred <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowWred>`
                                    
                                    .. attribute:: hardware_min_threshold_bytes
                                    
                                    	Hardware minimum threshold
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: hardware_max_threshold_bytes
                                    
                                    	Hardware maximum threshold
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: first_segment
                                    
                                    	First segment
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: segment_size
                                    
                                    	Segment size
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.Wred, self).__init__()

                                        self.yang_name = "wred"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("wred-match-value", ("wred_match_value", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.Wred.WredMatchValue)), ("config-min-threshold", ("config_min_threshold", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.Wred.ConfigMinThreshold)), ("config-max-threshold", ("config_max_threshold", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.Wred.ConfigMaxThreshold))])
                                        self._leafs = OrderedDict([
                                            ('wred_match_type', (YLeaf(YType.enumeration, 'wred-match-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowWred', '')])),
                                            ('hardware_min_threshold_bytes', (YLeaf(YType.uint32, 'hardware-min-threshold-bytes'), ['int'])),
                                            ('hardware_max_threshold_bytes', (YLeaf(YType.uint32, 'hardware-max-threshold-bytes'), ['int'])),
                                            ('first_segment', (YLeaf(YType.uint16, 'first-segment'), ['int'])),
                                            ('segment_size', (YLeaf(YType.uint32, 'segment-size'), ['int'])),
                                        ])
                                        self.wred_match_type = None
                                        self.hardware_min_threshold_bytes = None
                                        self.hardware_max_threshold_bytes = None
                                        self.first_segment = None
                                        self.segment_size = None

                                        self.wred_match_value = PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.Wred.WredMatchValue()
                                        self.wred_match_value.parent = self
                                        self._children_name_map["wred_match_value"] = "wred-match-value"

                                        self.config_min_threshold = PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.Wred.ConfigMinThreshold()
                                        self.config_min_threshold.parent = self
                                        self._children_name_map["config_min_threshold"] = "config-min-threshold"

                                        self.config_max_threshold = PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.Wred.ConfigMaxThreshold()
                                        self.config_max_threshold.parent = self
                                        self._children_name_map["config_max_threshold"] = "config-max-threshold"
                                        self._segment_path = lambda: "wred"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.Wred, [u'wred_match_type', u'hardware_min_threshold_bytes', u'hardware_max_threshold_bytes', u'first_segment', u'segment_size'], name, value)


                                    class WredMatchValue(Entity):
                                        """
                                        WRED match values
                                        
                                        .. attribute:: dnx_qosea_show_red_match_value
                                        
                                        	dnx qosea show red match value
                                        	**type**\: list of  		 :py:class:`DnxQoseaShowRedMatchValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue>`
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.Wred.WredMatchValue, self).__init__()

                                            self.yang_name = "wred-match-value"
                                            self.yang_parent_name = "wred"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("dnx-qosea-show-red-match-value", ("dnx_qosea_show_red_match_value", PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue))])
                                            self._leafs = OrderedDict()

                                            self.dnx_qosea_show_red_match_value = YList(self)
                                            self._segment_path = lambda: "wred-match-value"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.Wred.WredMatchValue, [], name, value)


                                        class DnxQoseaShowRedMatchValue(Entity):
                                            """
                                            dnx qosea show red match value
                                            
                                            .. attribute:: range_start
                                            
                                            	Start value of a range
                                            	**type**\: int
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: range_end
                                            
                                            	End value of a range
                                            	**type**\: int
                                            
                                            	**range:** 0..255
                                            
                                            

                                            """

                                            _prefix = 'ncs5500-qos-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue, self).__init__()

                                                self.yang_name = "dnx-qosea-show-red-match-value"
                                                self.yang_parent_name = "wred-match-value"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('range_start', (YLeaf(YType.uint8, 'range-start'), ['int'])),
                                                    ('range_end', (YLeaf(YType.uint8, 'range-end'), ['int'])),
                                                ])
                                                self.range_start = None
                                                self.range_end = None
                                                self._segment_path = lambda: "dnx-qosea-show-red-match-value"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue, [u'range_start', u'range_end'], name, value)


                                    class ConfigMinThreshold(Entity):
                                        """
                                        Configured minimum threshold
                                        
                                        .. attribute:: policy_value
                                        
                                        	Policy value
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: policy_unit
                                        
                                        	Policy unit
                                        	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.Wred.ConfigMinThreshold, self).__init__()

                                            self.yang_name = "config-min-threshold"
                                            self.yang_parent_name = "wred"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                                ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                            ])
                                            self.policy_value = None
                                            self.policy_unit = None
                                            self._segment_path = lambda: "config-min-threshold"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.Wred.ConfigMinThreshold, [u'policy_value', u'policy_unit'], name, value)


                                    class ConfigMaxThreshold(Entity):
                                        """
                                        Configured maximum threshold
                                        
                                        .. attribute:: policy_value
                                        
                                        	Policy value
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: policy_unit
                                        
                                        	Policy unit
                                        	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.Wred.ConfigMaxThreshold, self).__init__()

                                            self.yang_name = "config-max-threshold"
                                            self.yang_parent_name = "wred"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                                ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                            ])
                                            self.policy_value = None
                                            self.policy_unit = None
                                            self._segment_path = lambda: "config-max-threshold"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.QosInterfaces.QosInterface.Output.QosClassTable.Class.Wred.ConfigMaxThreshold, [u'policy_value', u'policy_unit'], name, value)


            class BundleInterfaceSingles(Entity):
                """
                QoS list of bundle interfaces
                
                .. attribute:: bundle_interface_single
                
                	QoS interface names
                	**type**\: list of  		 :py:class:`BundleInterfaceSingle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle>`
                
                

                """

                _prefix = 'ncs5500-qos-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PlatformQos.Nodes.Node.BundleInterfaceSingles, self).__init__()

                    self.yang_name = "bundle-interface-singles"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("bundle-interface-single", ("bundle_interface_single", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle))])
                    self._leafs = OrderedDict()

                    self.bundle_interface_single = YList(self)
                    self._segment_path = lambda: "bundle-interface-singles"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles, [], name, value)


                class BundleInterfaceSingle(Entity):
                    """
                    QoS interface names
                    
                    .. attribute:: interface_name  (key)
                    
                    	Bundle interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: policy_details
                    
                    	Policy Details
                    	**type**\:  :py:class:`PolicyDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.PolicyDetails>`
                    
                    .. attribute:: member_interfaces
                    
                    	QoS list of member interfaces
                    	**type**\:  :py:class:`MemberInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces>`
                    
                    .. attribute:: class_table
                    
                    	QoS list of class names
                    	**type**\:  :py:class:`ClassTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable>`
                    
                    

                    """

                    _prefix = 'ncs5500-qos-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle, self).__init__()

                        self.yang_name = "bundle-interface-single"
                        self.yang_parent_name = "bundle-interface-singles"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([("policy-details", ("policy_details", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.PolicyDetails)), ("member-interfaces", ("member_interfaces", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces)), ("class-table", ("class_table", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ])
                        self.interface_name = None

                        self.policy_details = PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.PolicyDetails()
                        self.policy_details.parent = self
                        self._children_name_map["policy_details"] = "policy-details"

                        self.member_interfaces = PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces()
                        self.member_interfaces.parent = self
                        self._children_name_map["member_interfaces"] = "member-interfaces"

                        self.class_table = PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable()
                        self.class_table.parent = self
                        self._children_name_map["class_table"] = "class-table"
                        self._segment_path = lambda: "bundle-interface-single" + "[interface-name='" + str(self.interface_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle, ['interface_name'], name, value)


                    class PolicyDetails(Entity):
                        """
                        Policy Details
                        
                        .. attribute:: npu_id
                        
                        	NPU ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: interface_handle
                        
                        	InterfaceHandle
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: interface_bandwidth_kbps
                        
                        	Interface Bandwidth (in kbps)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: kbit/s
                        
                        .. attribute:: policy_name
                        
                        	Policy name
                        	**type**\: str
                        
                        	**length:** 0..64
                        
                        .. attribute:: total_number_of_classes
                        
                        	Number of Classes
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: voq_base_address
                        
                        	VOQ base address
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: voq_stats_handle
                        
                        	VOQ stats handle
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: stats_accounting_type
                        
                        	QoS Statistics Accounting Type
                        	**type**\:  :py:class:`QosPolicyAccountEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.QosPolicyAccountEnum>`
                        
                        .. attribute:: policy_status
                        
                        	Policy Status
                        	**type**\:  :py:class:`DnxQoseaShowPolicyStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowPolicyStatus>`
                        
                        .. attribute:: interface_status
                        
                        	Interface Status
                        	**type**\:  :py:class:`DnxQoseaShowIntfStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowIntfStatus>`
                        
                        

                        """

                        _prefix = 'ncs5500-qos-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.PolicyDetails, self).__init__()

                            self.yang_name = "policy-details"
                            self.yang_parent_name = "bundle-interface-single"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('npu_id', (YLeaf(YType.uint32, 'npu-id'), ['int'])),
                                ('interface_handle', (YLeaf(YType.uint32, 'interface-handle'), ['int'])),
                                ('interface_bandwidth_kbps', (YLeaf(YType.uint32, 'interface-bandwidth-kbps'), ['int'])),
                                ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                ('total_number_of_classes', (YLeaf(YType.uint16, 'total-number-of-classes'), ['int'])),
                                ('voq_base_address', (YLeaf(YType.uint32, 'voq-base-address'), ['int'])),
                                ('voq_stats_handle', (YLeaf(YType.uint64, 'voq-stats-handle'), ['int'])),
                                ('stats_accounting_type', (YLeaf(YType.enumeration, 'stats-accounting-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'QosPolicyAccountEnum', '')])),
                                ('policy_status', (YLeaf(YType.enumeration, 'policy-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowPolicyStatus', '')])),
                                ('interface_status', (YLeaf(YType.enumeration, 'interface-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowIntfStatus', '')])),
                            ])
                            self.npu_id = None
                            self.interface_handle = None
                            self.interface_bandwidth_kbps = None
                            self.policy_name = None
                            self.total_number_of_classes = None
                            self.voq_base_address = None
                            self.voq_stats_handle = None
                            self.stats_accounting_type = None
                            self.policy_status = None
                            self.interface_status = None
                            self._segment_path = lambda: "policy-details"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.PolicyDetails, [u'npu_id', u'interface_handle', u'interface_bandwidth_kbps', u'policy_name', u'total_number_of_classes', u'voq_base_address', u'voq_stats_handle', u'stats_accounting_type', u'policy_status', u'interface_status'], name, value)


                    class MemberInterfaces(Entity):
                        """
                        QoS list of member interfaces
                        
                        .. attribute:: member_interface
                        
                        	QoS interface names
                        	**type**\: list of  		 :py:class:`MemberInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface>`
                        
                        

                        """

                        _prefix = 'ncs5500-qos-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces, self).__init__()

                            self.yang_name = "member-interfaces"
                            self.yang_parent_name = "bundle-interface-single"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("member-interface", ("member_interface", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface))])
                            self._leafs = OrderedDict()

                            self.member_interface = YList(self)
                            self._segment_path = lambda: "member-interfaces"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces, [], name, value)


                        class MemberInterface(Entity):
                            """
                            QoS interface names
                            
                            .. attribute:: interface_name  (key)
                            
                            	Member interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: policy_details
                            
                            	Policy Details
                            	**type**\:  :py:class:`PolicyDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.PolicyDetails>`
                            
                            .. attribute:: class_table
                            
                            	QoS list of class names
                            	**type**\:  :py:class:`ClassTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable>`
                            
                            

                            """

                            _prefix = 'ncs5500-qos-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface, self).__init__()

                                self.yang_name = "member-interface"
                                self.yang_parent_name = "member-interfaces"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['interface_name']
                                self._child_classes = OrderedDict([("policy-details", ("policy_details", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.PolicyDetails)), ("class-table", ("class_table", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable))])
                                self._leafs = OrderedDict([
                                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ])
                                self.interface_name = None

                                self.policy_details = PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.PolicyDetails()
                                self.policy_details.parent = self
                                self._children_name_map["policy_details"] = "policy-details"

                                self.class_table = PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable()
                                self.class_table.parent = self
                                self._children_name_map["class_table"] = "class-table"
                                self._segment_path = lambda: "member-interface" + "[interface-name='" + str(self.interface_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface, ['interface_name'], name, value)


                            class PolicyDetails(Entity):
                                """
                                Policy Details
                                
                                .. attribute:: npu_id
                                
                                	NPU ID
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: interface_handle
                                
                                	InterfaceHandle
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: interface_bandwidth_kbps
                                
                                	Interface Bandwidth (in kbps)
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: kbit/s
                                
                                .. attribute:: policy_name
                                
                                	Policy name
                                	**type**\: str
                                
                                	**length:** 0..64
                                
                                .. attribute:: total_number_of_classes
                                
                                	Number of Classes
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: voq_base_address
                                
                                	VOQ base address
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: voq_stats_handle
                                
                                	VOQ stats handle
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: stats_accounting_type
                                
                                	QoS Statistics Accounting Type
                                	**type**\:  :py:class:`QosPolicyAccountEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.QosPolicyAccountEnum>`
                                
                                .. attribute:: policy_status
                                
                                	Policy Status
                                	**type**\:  :py:class:`DnxQoseaShowPolicyStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowPolicyStatus>`
                                
                                .. attribute:: interface_status
                                
                                	Interface Status
                                	**type**\:  :py:class:`DnxQoseaShowIntfStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowIntfStatus>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.PolicyDetails, self).__init__()

                                    self.yang_name = "policy-details"
                                    self.yang_parent_name = "member-interface"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('npu_id', (YLeaf(YType.uint32, 'npu-id'), ['int'])),
                                        ('interface_handle', (YLeaf(YType.uint32, 'interface-handle'), ['int'])),
                                        ('interface_bandwidth_kbps', (YLeaf(YType.uint32, 'interface-bandwidth-kbps'), ['int'])),
                                        ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                        ('total_number_of_classes', (YLeaf(YType.uint16, 'total-number-of-classes'), ['int'])),
                                        ('voq_base_address', (YLeaf(YType.uint32, 'voq-base-address'), ['int'])),
                                        ('voq_stats_handle', (YLeaf(YType.uint64, 'voq-stats-handle'), ['int'])),
                                        ('stats_accounting_type', (YLeaf(YType.enumeration, 'stats-accounting-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'QosPolicyAccountEnum', '')])),
                                        ('policy_status', (YLeaf(YType.enumeration, 'policy-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowPolicyStatus', '')])),
                                        ('interface_status', (YLeaf(YType.enumeration, 'interface-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowIntfStatus', '')])),
                                    ])
                                    self.npu_id = None
                                    self.interface_handle = None
                                    self.interface_bandwidth_kbps = None
                                    self.policy_name = None
                                    self.total_number_of_classes = None
                                    self.voq_base_address = None
                                    self.voq_stats_handle = None
                                    self.stats_accounting_type = None
                                    self.policy_status = None
                                    self.interface_status = None
                                    self._segment_path = lambda: "policy-details"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.PolicyDetails, [u'npu_id', u'interface_handle', u'interface_bandwidth_kbps', u'policy_name', u'total_number_of_classes', u'voq_base_address', u'voq_stats_handle', u'stats_accounting_type', u'policy_status', u'interface_status'], name, value)


                            class ClassTable(Entity):
                                """
                                QoS list of class names
                                
                                .. attribute:: class_
                                
                                	QoS policy class
                                	**type**\: list of  		 :py:class:`Class <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable, self).__init__()

                                    self.yang_name = "class-table"
                                    self.yang_parent_name = "member-interface"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("class", ("class_", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class))])
                                    self._leafs = OrderedDict()

                                    self.class_ = YList(self)
                                    self._segment_path = lambda: "class-table"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable, [], name, value)


                                class Class(Entity):
                                    """
                                    QoS policy class
                                    
                                    .. attribute:: level_one_class_name  (key)
                                    
                                    	QoS policy class name at level 1
                                    	**type**\: str
                                    
                                    .. attribute:: level_two_class_name
                                    
                                    	QoS policy child class name at level 2
                                    	**type**\: str
                                    
                                    .. attribute:: config_max_rate
                                    
                                    	Configured maximum rate
                                    	**type**\:  :py:class:`ConfigMaxRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigMaxRate>`
                                    
                                    .. attribute:: config_min_rate
                                    
                                    	Configured minimum rate
                                    	**type**\:  :py:class:`ConfigMinRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigMinRate>`
                                    
                                    .. attribute:: config_queue_limit
                                    
                                    	Configured queue limit
                                    	**type**\:  :py:class:`ConfigQueueLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigQueueLimit>`
                                    
                                    .. attribute:: config_policer_average_rate
                                    
                                    	Configured policer average rate
                                    	**type**\:  :py:class:`ConfigPolicerAverageRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigPolicerAverageRate>`
                                    
                                    .. attribute:: config_policer_peak_rate
                                    
                                    	Config policer peak rate
                                    	**type**\:  :py:class:`ConfigPolicerPeakRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigPolicerPeakRate>`
                                    
                                    .. attribute:: config_policer_conform_burst
                                    
                                    	Configured policer conform burst
                                    	**type**\:  :py:class:`ConfigPolicerConformBurst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigPolicerConformBurst>`
                                    
                                    .. attribute:: config_policer_excess_burst
                                    
                                    	Configured policer excess burst
                                    	**type**\:  :py:class:`ConfigPolicerExcessBurst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigPolicerExcessBurst>`
                                    
                                    .. attribute:: conform_action
                                    
                                    	Conform action
                                    	**type**\:  :py:class:`ConformAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ConformAction>`
                                    
                                    .. attribute:: exceed_action
                                    
                                    	Exceed action
                                    	**type**\:  :py:class:`ExceedAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ExceedAction>`
                                    
                                    .. attribute:: violate_action
                                    
                                    	Violate action
                                    	**type**\:  :py:class:`ViolateAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ViolateAction>`
                                    
                                    .. attribute:: class_level
                                    
                                    	Class level
                                    	**type**\:  :py:class:`DnxQoseaShowLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowLevel>`
                                    
                                    .. attribute:: egress_queue_id
                                    
                                    	Egress Queue ID
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: queue_type
                                    
                                    	Queue type
                                    	**type**\:  :py:class:`DnxQoseaShowQueue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowQueue>`
                                    
                                    .. attribute:: priority_level
                                    
                                    	Priority level
                                    	**type**\:  :py:class:`DnxQoseaShowHpLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowHpLevel>`
                                    
                                    .. attribute:: hardware_max_rate_kbps
                                    
                                    	Hardware maximum rate in kbps
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**units**\: kbit/s
                                    
                                    .. attribute:: hardware_min_rate_kbps
                                    
                                    	Hardware minimum rate in kbps
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**units**\: kbit/s
                                    
                                    .. attribute:: config_excess_bandwidth_percent
                                    
                                    	Configured excess bandwidth percentage
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**units**\: percentage
                                    
                                    .. attribute:: config_excess_bandwidth_unit
                                    
                                    	Configured excess bandwidth unit
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: hardware_excess_bandwidth_weight
                                    
                                    	Hardware excess bandwidth weight
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: network_min_bandwidth_kbps
                                    
                                    	Network minimum Bandwith
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: hardware_queue_limit_bytes
                                    
                                    	Hardware queue limit in bytes
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: hardware_queue_limit_microseconds
                                    
                                    	Hardware queue limit in microseconds
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: microsecond
                                    
                                    .. attribute:: policer_bucket_id
                                    
                                    	PolicerBucketID
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: policer_stats_handle
                                    
                                    	PolicerStatsHandle
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: hardware_policer_average_rate_kbps
                                    
                                    	Hardware policer average in kbps
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**units**\: kbit/s
                                    
                                    .. attribute:: hardware_policer_peak_rate_kbps
                                    
                                    	Hardware policer peak rate
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: hardware_policer_conform_burst_bytes
                                    
                                    	Hardware policer conform burst
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: hardware_policer_excess_burst_bytes
                                    
                                    	Hardware policer excess burst
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: ip_mark
                                    
                                    	IP mark
                                    	**type**\: list of  		 :py:class:`IpMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.IpMark>`
                                    
                                    .. attribute:: common_mark
                                    
                                    	Common mark
                                    	**type**\: list of  		 :py:class:`CommonMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.CommonMark>`
                                    
                                    .. attribute:: mpls_mark
                                    
                                    	MPLS mark
                                    	**type**\: list of  		 :py:class:`MplsMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.MplsMark>`
                                    
                                    .. attribute:: wred
                                    
                                    	WRED parameters
                                    	**type**\: list of  		 :py:class:`Wred <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.Wred>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class, self).__init__()

                                        self.yang_name = "class"
                                        self.yang_parent_name = "class-table"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['level_one_class_name']
                                        self._child_classes = OrderedDict([("config-max-rate", ("config_max_rate", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigMaxRate)), ("config-min-rate", ("config_min_rate", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigMinRate)), ("config-queue-limit", ("config_queue_limit", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigQueueLimit)), ("config-policer-average-rate", ("config_policer_average_rate", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigPolicerAverageRate)), ("config-policer-peak-rate", ("config_policer_peak_rate", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigPolicerPeakRate)), ("config-policer-conform-burst", ("config_policer_conform_burst", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigPolicerConformBurst)), ("config-policer-excess-burst", ("config_policer_excess_burst", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigPolicerExcessBurst)), ("conform-action", ("conform_action", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ConformAction)), ("exceed-action", ("exceed_action", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ExceedAction)), ("violate-action", ("violate_action", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ViolateAction)), ("ip-mark", ("ip_mark", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.IpMark)), ("common-mark", ("common_mark", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.CommonMark)), ("mpls-mark", ("mpls_mark", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.MplsMark)), ("wred", ("wred", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.Wred))])
                                        self._leafs = OrderedDict([
                                            ('level_one_class_name', (YLeaf(YType.str, 'level-one-class-name'), ['str'])),
                                            ('level_two_class_name', (YLeaf(YType.str, 'level-two-class-name'), ['str'])),
                                            ('class_level', (YLeaf(YType.enumeration, 'class-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowLevel', '')])),
                                            ('egress_queue_id', (YLeaf(YType.int32, 'egress-queue-id'), ['int'])),
                                            ('queue_type', (YLeaf(YType.enumeration, 'queue-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowQueue', '')])),
                                            ('priority_level', (YLeaf(YType.enumeration, 'priority-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowHpLevel', '')])),
                                            ('hardware_max_rate_kbps', (YLeaf(YType.uint32, 'hardware-max-rate-kbps'), ['int'])),
                                            ('hardware_min_rate_kbps', (YLeaf(YType.uint32, 'hardware-min-rate-kbps'), ['int'])),
                                            ('config_excess_bandwidth_percent', (YLeaf(YType.uint32, 'config-excess-bandwidth-percent'), ['int'])),
                                            ('config_excess_bandwidth_unit', (YLeaf(YType.uint32, 'config-excess-bandwidth-unit'), ['int'])),
                                            ('hardware_excess_bandwidth_weight', (YLeaf(YType.uint32, 'hardware-excess-bandwidth-weight'), ['int'])),
                                            ('network_min_bandwidth_kbps', (YLeaf(YType.uint32, 'network-min-bandwidth-kbps'), ['int'])),
                                            ('hardware_queue_limit_bytes', (YLeaf(YType.uint64, 'hardware-queue-limit-bytes'), ['int'])),
                                            ('hardware_queue_limit_microseconds', (YLeaf(YType.uint64, 'hardware-queue-limit-microseconds'), ['int'])),
                                            ('policer_bucket_id', (YLeaf(YType.uint32, 'policer-bucket-id'), ['int'])),
                                            ('policer_stats_handle', (YLeaf(YType.uint64, 'policer-stats-handle'), ['int'])),
                                            ('hardware_policer_average_rate_kbps', (YLeaf(YType.uint32, 'hardware-policer-average-rate-kbps'), ['int'])),
                                            ('hardware_policer_peak_rate_kbps', (YLeaf(YType.uint32, 'hardware-policer-peak-rate-kbps'), ['int'])),
                                            ('hardware_policer_conform_burst_bytes', (YLeaf(YType.uint32, 'hardware-policer-conform-burst-bytes'), ['int'])),
                                            ('hardware_policer_excess_burst_bytes', (YLeaf(YType.uint32, 'hardware-policer-excess-burst-bytes'), ['int'])),
                                        ])
                                        self.level_one_class_name = None
                                        self.level_two_class_name = None
                                        self.class_level = None
                                        self.egress_queue_id = None
                                        self.queue_type = None
                                        self.priority_level = None
                                        self.hardware_max_rate_kbps = None
                                        self.hardware_min_rate_kbps = None
                                        self.config_excess_bandwidth_percent = None
                                        self.config_excess_bandwidth_unit = None
                                        self.hardware_excess_bandwidth_weight = None
                                        self.network_min_bandwidth_kbps = None
                                        self.hardware_queue_limit_bytes = None
                                        self.hardware_queue_limit_microseconds = None
                                        self.policer_bucket_id = None
                                        self.policer_stats_handle = None
                                        self.hardware_policer_average_rate_kbps = None
                                        self.hardware_policer_peak_rate_kbps = None
                                        self.hardware_policer_conform_burst_bytes = None
                                        self.hardware_policer_excess_burst_bytes = None

                                        self.config_max_rate = PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigMaxRate()
                                        self.config_max_rate.parent = self
                                        self._children_name_map["config_max_rate"] = "config-max-rate"

                                        self.config_min_rate = PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigMinRate()
                                        self.config_min_rate.parent = self
                                        self._children_name_map["config_min_rate"] = "config-min-rate"

                                        self.config_queue_limit = PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigQueueLimit()
                                        self.config_queue_limit.parent = self
                                        self._children_name_map["config_queue_limit"] = "config-queue-limit"

                                        self.config_policer_average_rate = PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigPolicerAverageRate()
                                        self.config_policer_average_rate.parent = self
                                        self._children_name_map["config_policer_average_rate"] = "config-policer-average-rate"

                                        self.config_policer_peak_rate = PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigPolicerPeakRate()
                                        self.config_policer_peak_rate.parent = self
                                        self._children_name_map["config_policer_peak_rate"] = "config-policer-peak-rate"

                                        self.config_policer_conform_burst = PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigPolicerConformBurst()
                                        self.config_policer_conform_burst.parent = self
                                        self._children_name_map["config_policer_conform_burst"] = "config-policer-conform-burst"

                                        self.config_policer_excess_burst = PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigPolicerExcessBurst()
                                        self.config_policer_excess_burst.parent = self
                                        self._children_name_map["config_policer_excess_burst"] = "config-policer-excess-burst"

                                        self.conform_action = PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ConformAction()
                                        self.conform_action.parent = self
                                        self._children_name_map["conform_action"] = "conform-action"

                                        self.exceed_action = PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ExceedAction()
                                        self.exceed_action.parent = self
                                        self._children_name_map["exceed_action"] = "exceed-action"

                                        self.violate_action = PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ViolateAction()
                                        self.violate_action.parent = self
                                        self._children_name_map["violate_action"] = "violate-action"

                                        self.ip_mark = YList(self)
                                        self.common_mark = YList(self)
                                        self.mpls_mark = YList(self)
                                        self.wred = YList(self)
                                        self._segment_path = lambda: "class" + "[level-one-class-name='" + str(self.level_one_class_name) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class, ['level_one_class_name', 'level_two_class_name', u'class_level', u'egress_queue_id', u'queue_type', u'priority_level', u'hardware_max_rate_kbps', u'hardware_min_rate_kbps', u'config_excess_bandwidth_percent', u'config_excess_bandwidth_unit', u'hardware_excess_bandwidth_weight', u'network_min_bandwidth_kbps', u'hardware_queue_limit_bytes', u'hardware_queue_limit_microseconds', u'policer_bucket_id', u'policer_stats_handle', u'hardware_policer_average_rate_kbps', u'hardware_policer_peak_rate_kbps', u'hardware_policer_conform_burst_bytes', u'hardware_policer_excess_burst_bytes'], name, value)


                                    class ConfigMaxRate(Entity):
                                        """
                                        Configured maximum rate
                                        
                                        .. attribute:: policy_value
                                        
                                        	Policy value
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: policy_unit
                                        
                                        	Policy unit
                                        	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigMaxRate, self).__init__()

                                            self.yang_name = "config-max-rate"
                                            self.yang_parent_name = "class"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                                ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                            ])
                                            self.policy_value = None
                                            self.policy_unit = None
                                            self._segment_path = lambda: "config-max-rate"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigMaxRate, [u'policy_value', u'policy_unit'], name, value)


                                    class ConfigMinRate(Entity):
                                        """
                                        Configured minimum rate
                                        
                                        .. attribute:: policy_value
                                        
                                        	Policy value
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: policy_unit
                                        
                                        	Policy unit
                                        	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigMinRate, self).__init__()

                                            self.yang_name = "config-min-rate"
                                            self.yang_parent_name = "class"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                                ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                            ])
                                            self.policy_value = None
                                            self.policy_unit = None
                                            self._segment_path = lambda: "config-min-rate"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigMinRate, [u'policy_value', u'policy_unit'], name, value)


                                    class ConfigQueueLimit(Entity):
                                        """
                                        Configured queue limit
                                        
                                        .. attribute:: policy_value
                                        
                                        	Policy value
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: policy_unit
                                        
                                        	Policy unit
                                        	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigQueueLimit, self).__init__()

                                            self.yang_name = "config-queue-limit"
                                            self.yang_parent_name = "class"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                                ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                            ])
                                            self.policy_value = None
                                            self.policy_unit = None
                                            self._segment_path = lambda: "config-queue-limit"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigQueueLimit, [u'policy_value', u'policy_unit'], name, value)


                                    class ConfigPolicerAverageRate(Entity):
                                        """
                                        Configured policer average rate
                                        
                                        .. attribute:: policy_value
                                        
                                        	Policy value
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: policy_unit
                                        
                                        	Policy unit
                                        	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigPolicerAverageRate, self).__init__()

                                            self.yang_name = "config-policer-average-rate"
                                            self.yang_parent_name = "class"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                                ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                            ])
                                            self.policy_value = None
                                            self.policy_unit = None
                                            self._segment_path = lambda: "config-policer-average-rate"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigPolicerAverageRate, [u'policy_value', u'policy_unit'], name, value)


                                    class ConfigPolicerPeakRate(Entity):
                                        """
                                        Config policer peak rate
                                        
                                        .. attribute:: policy_value
                                        
                                        	Policy value
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: policy_unit
                                        
                                        	Policy unit
                                        	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigPolicerPeakRate, self).__init__()

                                            self.yang_name = "config-policer-peak-rate"
                                            self.yang_parent_name = "class"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                                ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                            ])
                                            self.policy_value = None
                                            self.policy_unit = None
                                            self._segment_path = lambda: "config-policer-peak-rate"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigPolicerPeakRate, [u'policy_value', u'policy_unit'], name, value)


                                    class ConfigPolicerConformBurst(Entity):
                                        """
                                        Configured policer conform burst
                                        
                                        .. attribute:: policy_value
                                        
                                        	Policy value
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: policy_unit
                                        
                                        	Policy unit
                                        	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigPolicerConformBurst, self).__init__()

                                            self.yang_name = "config-policer-conform-burst"
                                            self.yang_parent_name = "class"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                                ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                            ])
                                            self.policy_value = None
                                            self.policy_unit = None
                                            self._segment_path = lambda: "config-policer-conform-burst"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigPolicerConformBurst, [u'policy_value', u'policy_unit'], name, value)


                                    class ConfigPolicerExcessBurst(Entity):
                                        """
                                        Configured policer excess burst
                                        
                                        .. attribute:: policy_value
                                        
                                        	Policy value
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: policy_unit
                                        
                                        	Policy unit
                                        	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigPolicerExcessBurst, self).__init__()

                                            self.yang_name = "config-policer-excess-burst"
                                            self.yang_parent_name = "class"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                                ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                            ])
                                            self.policy_value = None
                                            self.policy_unit = None
                                            self._segment_path = lambda: "config-policer-excess-burst"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ConfigPolicerExcessBurst, [u'policy_value', u'policy_unit'], name, value)


                                    class ConformAction(Entity):
                                        """
                                        Conform action
                                        
                                        .. attribute:: action_type
                                        
                                        	Policer action type
                                        	**type**\:  :py:class:`DnxQoseaShowAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowAction>`
                                        
                                        .. attribute:: mark
                                        
                                        	Action mark
                                        	**type**\: list of  		 :py:class:`Mark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ConformAction.Mark>`
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ConformAction, self).__init__()

                                            self.yang_name = "conform-action"
                                            self.yang_parent_name = "class"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("mark", ("mark", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ConformAction.Mark))])
                                            self._leafs = OrderedDict([
                                                ('action_type', (YLeaf(YType.enumeration, 'action-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowAction', '')])),
                                            ])
                                            self.action_type = None

                                            self.mark = YList(self)
                                            self._segment_path = lambda: "conform-action"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ConformAction, [u'action_type'], name, value)


                                        class Mark(Entity):
                                            """
                                            Action mark
                                            
                                            .. attribute:: mark_type
                                            
                                            	Mark type
                                            	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                            
                                            .. attribute:: mark_value
                                            
                                            	Mark value
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            

                                            """

                                            _prefix = 'ncs5500-qos-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ConformAction.Mark, self).__init__()

                                                self.yang_name = "mark"
                                                self.yang_parent_name = "conform-action"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                                    ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                                ])
                                                self.mark_type = None
                                                self.mark_value = None
                                                self._segment_path = lambda: "mark"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ConformAction.Mark, [u'mark_type', u'mark_value'], name, value)


                                    class ExceedAction(Entity):
                                        """
                                        Exceed action
                                        
                                        .. attribute:: action_type
                                        
                                        	Policer action type
                                        	**type**\:  :py:class:`DnxQoseaShowAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowAction>`
                                        
                                        .. attribute:: mark
                                        
                                        	Action mark
                                        	**type**\: list of  		 :py:class:`Mark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ExceedAction.Mark>`
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ExceedAction, self).__init__()

                                            self.yang_name = "exceed-action"
                                            self.yang_parent_name = "class"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("mark", ("mark", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ExceedAction.Mark))])
                                            self._leafs = OrderedDict([
                                                ('action_type', (YLeaf(YType.enumeration, 'action-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowAction', '')])),
                                            ])
                                            self.action_type = None

                                            self.mark = YList(self)
                                            self._segment_path = lambda: "exceed-action"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ExceedAction, [u'action_type'], name, value)


                                        class Mark(Entity):
                                            """
                                            Action mark
                                            
                                            .. attribute:: mark_type
                                            
                                            	Mark type
                                            	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                            
                                            .. attribute:: mark_value
                                            
                                            	Mark value
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            

                                            """

                                            _prefix = 'ncs5500-qos-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ExceedAction.Mark, self).__init__()

                                                self.yang_name = "mark"
                                                self.yang_parent_name = "exceed-action"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                                    ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                                ])
                                                self.mark_type = None
                                                self.mark_value = None
                                                self._segment_path = lambda: "mark"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ExceedAction.Mark, [u'mark_type', u'mark_value'], name, value)


                                    class ViolateAction(Entity):
                                        """
                                        Violate action
                                        
                                        .. attribute:: action_type
                                        
                                        	Policer action type
                                        	**type**\:  :py:class:`DnxQoseaShowAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowAction>`
                                        
                                        .. attribute:: mark
                                        
                                        	Action mark
                                        	**type**\: list of  		 :py:class:`Mark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ViolateAction.Mark>`
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ViolateAction, self).__init__()

                                            self.yang_name = "violate-action"
                                            self.yang_parent_name = "class"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("mark", ("mark", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ViolateAction.Mark))])
                                            self._leafs = OrderedDict([
                                                ('action_type', (YLeaf(YType.enumeration, 'action-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowAction', '')])),
                                            ])
                                            self.action_type = None

                                            self.mark = YList(self)
                                            self._segment_path = lambda: "violate-action"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ViolateAction, [u'action_type'], name, value)


                                        class Mark(Entity):
                                            """
                                            Action mark
                                            
                                            .. attribute:: mark_type
                                            
                                            	Mark type
                                            	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                            
                                            .. attribute:: mark_value
                                            
                                            	Mark value
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            

                                            """

                                            _prefix = 'ncs5500-qos-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ViolateAction.Mark, self).__init__()

                                                self.yang_name = "mark"
                                                self.yang_parent_name = "violate-action"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                                    ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                                ])
                                                self.mark_type = None
                                                self.mark_value = None
                                                self._segment_path = lambda: "mark"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.ViolateAction.Mark, [u'mark_type', u'mark_value'], name, value)


                                    class IpMark(Entity):
                                        """
                                        IP mark
                                        
                                        .. attribute:: mark_type
                                        
                                        	Mark type
                                        	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                        
                                        .. attribute:: mark_value
                                        
                                        	Mark value
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.IpMark, self).__init__()

                                            self.yang_name = "ip-mark"
                                            self.yang_parent_name = "class"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                                ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                            ])
                                            self.mark_type = None
                                            self.mark_value = None
                                            self._segment_path = lambda: "ip-mark"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.IpMark, [u'mark_type', u'mark_value'], name, value)


                                    class CommonMark(Entity):
                                        """
                                        Common mark
                                        
                                        .. attribute:: mark_type
                                        
                                        	Mark type
                                        	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                        
                                        .. attribute:: mark_value
                                        
                                        	Mark value
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.CommonMark, self).__init__()

                                            self.yang_name = "common-mark"
                                            self.yang_parent_name = "class"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                                ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                            ])
                                            self.mark_type = None
                                            self.mark_value = None
                                            self._segment_path = lambda: "common-mark"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.CommonMark, [u'mark_type', u'mark_value'], name, value)


                                    class MplsMark(Entity):
                                        """
                                        MPLS mark
                                        
                                        .. attribute:: mark_type
                                        
                                        	Mark type
                                        	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                        
                                        .. attribute:: mark_value
                                        
                                        	Mark value
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.MplsMark, self).__init__()

                                            self.yang_name = "mpls-mark"
                                            self.yang_parent_name = "class"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                                ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                            ])
                                            self.mark_type = None
                                            self.mark_value = None
                                            self._segment_path = lambda: "mpls-mark"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.MplsMark, [u'mark_type', u'mark_value'], name, value)


                                    class Wred(Entity):
                                        """
                                        WRED parameters
                                        
                                        .. attribute:: wred_match_value
                                        
                                        	WRED match values
                                        	**type**\:  :py:class:`WredMatchValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.Wred.WredMatchValue>`
                                        
                                        .. attribute:: config_min_threshold
                                        
                                        	Configured minimum threshold
                                        	**type**\:  :py:class:`ConfigMinThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.Wred.ConfigMinThreshold>`
                                        
                                        .. attribute:: config_max_threshold
                                        
                                        	Configured maximum threshold
                                        	**type**\:  :py:class:`ConfigMaxThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.Wred.ConfigMaxThreshold>`
                                        
                                        .. attribute:: wred_match_type
                                        
                                        	WREDMatchType
                                        	**type**\:  :py:class:`DnxQoseaShowWred <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowWred>`
                                        
                                        .. attribute:: hardware_min_threshold_bytes
                                        
                                        	Hardware minimum threshold
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: hardware_max_threshold_bytes
                                        
                                        	Hardware maximum threshold
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: first_segment
                                        
                                        	First segment
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: segment_size
                                        
                                        	Segment size
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.Wred, self).__init__()

                                            self.yang_name = "wred"
                                            self.yang_parent_name = "class"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("wred-match-value", ("wred_match_value", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.Wred.WredMatchValue)), ("config-min-threshold", ("config_min_threshold", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.Wred.ConfigMinThreshold)), ("config-max-threshold", ("config_max_threshold", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.Wred.ConfigMaxThreshold))])
                                            self._leafs = OrderedDict([
                                                ('wred_match_type', (YLeaf(YType.enumeration, 'wred-match-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowWred', '')])),
                                                ('hardware_min_threshold_bytes', (YLeaf(YType.uint32, 'hardware-min-threshold-bytes'), ['int'])),
                                                ('hardware_max_threshold_bytes', (YLeaf(YType.uint32, 'hardware-max-threshold-bytes'), ['int'])),
                                                ('first_segment', (YLeaf(YType.uint16, 'first-segment'), ['int'])),
                                                ('segment_size', (YLeaf(YType.uint32, 'segment-size'), ['int'])),
                                            ])
                                            self.wred_match_type = None
                                            self.hardware_min_threshold_bytes = None
                                            self.hardware_max_threshold_bytes = None
                                            self.first_segment = None
                                            self.segment_size = None

                                            self.wred_match_value = PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.Wred.WredMatchValue()
                                            self.wred_match_value.parent = self
                                            self._children_name_map["wred_match_value"] = "wred-match-value"

                                            self.config_min_threshold = PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.Wred.ConfigMinThreshold()
                                            self.config_min_threshold.parent = self
                                            self._children_name_map["config_min_threshold"] = "config-min-threshold"

                                            self.config_max_threshold = PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.Wred.ConfigMaxThreshold()
                                            self.config_max_threshold.parent = self
                                            self._children_name_map["config_max_threshold"] = "config-max-threshold"
                                            self._segment_path = lambda: "wred"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.Wred, [u'wred_match_type', u'hardware_min_threshold_bytes', u'hardware_max_threshold_bytes', u'first_segment', u'segment_size'], name, value)


                                        class WredMatchValue(Entity):
                                            """
                                            WRED match values
                                            
                                            .. attribute:: dnx_qosea_show_red_match_value
                                            
                                            	dnx qosea show red match value
                                            	**type**\: list of  		 :py:class:`DnxQoseaShowRedMatchValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue>`
                                            
                                            

                                            """

                                            _prefix = 'ncs5500-qos-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.Wred.WredMatchValue, self).__init__()

                                                self.yang_name = "wred-match-value"
                                                self.yang_parent_name = "wred"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("dnx-qosea-show-red-match-value", ("dnx_qosea_show_red_match_value", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue))])
                                                self._leafs = OrderedDict()

                                                self.dnx_qosea_show_red_match_value = YList(self)
                                                self._segment_path = lambda: "wred-match-value"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.Wred.WredMatchValue, [], name, value)


                                            class DnxQoseaShowRedMatchValue(Entity):
                                                """
                                                dnx qosea show red match value
                                                
                                                .. attribute:: range_start
                                                
                                                	Start value of a range
                                                	**type**\: int
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: range_end
                                                
                                                	End value of a range
                                                	**type**\: int
                                                
                                                	**range:** 0..255
                                                
                                                

                                                """

                                                _prefix = 'ncs5500-qos-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue, self).__init__()

                                                    self.yang_name = "dnx-qosea-show-red-match-value"
                                                    self.yang_parent_name = "wred-match-value"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('range_start', (YLeaf(YType.uint8, 'range-start'), ['int'])),
                                                        ('range_end', (YLeaf(YType.uint8, 'range-end'), ['int'])),
                                                    ])
                                                    self.range_start = None
                                                    self.range_end = None
                                                    self._segment_path = lambda: "dnx-qosea-show-red-match-value"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue, [u'range_start', u'range_end'], name, value)


                                        class ConfigMinThreshold(Entity):
                                            """
                                            Configured minimum threshold
                                            
                                            .. attribute:: policy_value
                                            
                                            	Policy value
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: policy_unit
                                            
                                            	Policy unit
                                            	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                            
                                            

                                            """

                                            _prefix = 'ncs5500-qos-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.Wred.ConfigMinThreshold, self).__init__()

                                                self.yang_name = "config-min-threshold"
                                                self.yang_parent_name = "wred"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                                    ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                                ])
                                                self.policy_value = None
                                                self.policy_unit = None
                                                self._segment_path = lambda: "config-min-threshold"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.Wred.ConfigMinThreshold, [u'policy_value', u'policy_unit'], name, value)


                                        class ConfigMaxThreshold(Entity):
                                            """
                                            Configured maximum threshold
                                            
                                            .. attribute:: policy_value
                                            
                                            	Policy value
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: policy_unit
                                            
                                            	Policy unit
                                            	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                            
                                            

                                            """

                                            _prefix = 'ncs5500-qos-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.Wred.ConfigMaxThreshold, self).__init__()

                                                self.yang_name = "config-max-threshold"
                                                self.yang_parent_name = "wred"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                                    ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                                ])
                                                self.policy_value = None
                                                self.policy_unit = None
                                                self._segment_path = lambda: "config-max-threshold"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.MemberInterfaces.MemberInterface.ClassTable.Class.Wred.ConfigMaxThreshold, [u'policy_value', u'policy_unit'], name, value)


                    class ClassTable(Entity):
                        """
                        QoS list of class names
                        
                        .. attribute:: class_
                        
                        	QoS policy class
                        	**type**\: list of  		 :py:class:`Class <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class>`
                        
                        

                        """

                        _prefix = 'ncs5500-qos-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable, self).__init__()

                            self.yang_name = "class-table"
                            self.yang_parent_name = "bundle-interface-single"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("class", ("class_", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class))])
                            self._leafs = OrderedDict()

                            self.class_ = YList(self)
                            self._segment_path = lambda: "class-table"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable, [], name, value)


                        class Class(Entity):
                            """
                            QoS policy class
                            
                            .. attribute:: level_one_class_name  (key)
                            
                            	QoS policy class name at level 1
                            	**type**\: str
                            
                            .. attribute:: level_two_class_name
                            
                            	QoS policy child class name at level 2
                            	**type**\: str
                            
                            .. attribute:: config_max_rate
                            
                            	Configured maximum rate
                            	**type**\:  :py:class:`ConfigMaxRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ConfigMaxRate>`
                            
                            .. attribute:: config_min_rate
                            
                            	Configured minimum rate
                            	**type**\:  :py:class:`ConfigMinRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ConfigMinRate>`
                            
                            .. attribute:: config_queue_limit
                            
                            	Configured queue limit
                            	**type**\:  :py:class:`ConfigQueueLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ConfigQueueLimit>`
                            
                            .. attribute:: config_policer_average_rate
                            
                            	Configured policer average rate
                            	**type**\:  :py:class:`ConfigPolicerAverageRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ConfigPolicerAverageRate>`
                            
                            .. attribute:: config_policer_peak_rate
                            
                            	Config policer peak rate
                            	**type**\:  :py:class:`ConfigPolicerPeakRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ConfigPolicerPeakRate>`
                            
                            .. attribute:: config_policer_conform_burst
                            
                            	Configured policer conform burst
                            	**type**\:  :py:class:`ConfigPolicerConformBurst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ConfigPolicerConformBurst>`
                            
                            .. attribute:: config_policer_excess_burst
                            
                            	Configured policer excess burst
                            	**type**\:  :py:class:`ConfigPolicerExcessBurst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ConfigPolicerExcessBurst>`
                            
                            .. attribute:: conform_action
                            
                            	Conform action
                            	**type**\:  :py:class:`ConformAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ConformAction>`
                            
                            .. attribute:: exceed_action
                            
                            	Exceed action
                            	**type**\:  :py:class:`ExceedAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ExceedAction>`
                            
                            .. attribute:: violate_action
                            
                            	Violate action
                            	**type**\:  :py:class:`ViolateAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ViolateAction>`
                            
                            .. attribute:: class_level
                            
                            	Class level
                            	**type**\:  :py:class:`DnxQoseaShowLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowLevel>`
                            
                            .. attribute:: egress_queue_id
                            
                            	Egress Queue ID
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: queue_type
                            
                            	Queue type
                            	**type**\:  :py:class:`DnxQoseaShowQueue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowQueue>`
                            
                            .. attribute:: priority_level
                            
                            	Priority level
                            	**type**\:  :py:class:`DnxQoseaShowHpLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowHpLevel>`
                            
                            .. attribute:: hardware_max_rate_kbps
                            
                            	Hardware maximum rate in kbps
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: kbit/s
                            
                            .. attribute:: hardware_min_rate_kbps
                            
                            	Hardware minimum rate in kbps
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: kbit/s
                            
                            .. attribute:: config_excess_bandwidth_percent
                            
                            	Configured excess bandwidth percentage
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: percentage
                            
                            .. attribute:: config_excess_bandwidth_unit
                            
                            	Configured excess bandwidth unit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hardware_excess_bandwidth_weight
                            
                            	Hardware excess bandwidth weight
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: network_min_bandwidth_kbps
                            
                            	Network minimum Bandwith
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hardware_queue_limit_bytes
                            
                            	Hardware queue limit in bytes
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: hardware_queue_limit_microseconds
                            
                            	Hardware queue limit in microseconds
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: microsecond
                            
                            .. attribute:: policer_bucket_id
                            
                            	PolicerBucketID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: policer_stats_handle
                            
                            	PolicerStatsHandle
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: hardware_policer_average_rate_kbps
                            
                            	Hardware policer average in kbps
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: kbit/s
                            
                            .. attribute:: hardware_policer_peak_rate_kbps
                            
                            	Hardware policer peak rate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hardware_policer_conform_burst_bytes
                            
                            	Hardware policer conform burst
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hardware_policer_excess_burst_bytes
                            
                            	Hardware policer excess burst
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ip_mark
                            
                            	IP mark
                            	**type**\: list of  		 :py:class:`IpMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.IpMark>`
                            
                            .. attribute:: common_mark
                            
                            	Common mark
                            	**type**\: list of  		 :py:class:`CommonMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.CommonMark>`
                            
                            .. attribute:: mpls_mark
                            
                            	MPLS mark
                            	**type**\: list of  		 :py:class:`MplsMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.MplsMark>`
                            
                            .. attribute:: wred
                            
                            	WRED parameters
                            	**type**\: list of  		 :py:class:`Wred <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.Wred>`
                            
                            

                            """

                            _prefix = 'ncs5500-qos-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class, self).__init__()

                                self.yang_name = "class"
                                self.yang_parent_name = "class-table"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['level_one_class_name']
                                self._child_classes = OrderedDict([("config-max-rate", ("config_max_rate", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ConfigMaxRate)), ("config-min-rate", ("config_min_rate", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ConfigMinRate)), ("config-queue-limit", ("config_queue_limit", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ConfigQueueLimit)), ("config-policer-average-rate", ("config_policer_average_rate", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ConfigPolicerAverageRate)), ("config-policer-peak-rate", ("config_policer_peak_rate", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ConfigPolicerPeakRate)), ("config-policer-conform-burst", ("config_policer_conform_burst", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ConfigPolicerConformBurst)), ("config-policer-excess-burst", ("config_policer_excess_burst", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ConfigPolicerExcessBurst)), ("conform-action", ("conform_action", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ConformAction)), ("exceed-action", ("exceed_action", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ExceedAction)), ("violate-action", ("violate_action", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ViolateAction)), ("ip-mark", ("ip_mark", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.IpMark)), ("common-mark", ("common_mark", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.CommonMark)), ("mpls-mark", ("mpls_mark", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.MplsMark)), ("wred", ("wred", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.Wred))])
                                self._leafs = OrderedDict([
                                    ('level_one_class_name', (YLeaf(YType.str, 'level-one-class-name'), ['str'])),
                                    ('level_two_class_name', (YLeaf(YType.str, 'level-two-class-name'), ['str'])),
                                    ('class_level', (YLeaf(YType.enumeration, 'class-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowLevel', '')])),
                                    ('egress_queue_id', (YLeaf(YType.int32, 'egress-queue-id'), ['int'])),
                                    ('queue_type', (YLeaf(YType.enumeration, 'queue-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowQueue', '')])),
                                    ('priority_level', (YLeaf(YType.enumeration, 'priority-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowHpLevel', '')])),
                                    ('hardware_max_rate_kbps', (YLeaf(YType.uint32, 'hardware-max-rate-kbps'), ['int'])),
                                    ('hardware_min_rate_kbps', (YLeaf(YType.uint32, 'hardware-min-rate-kbps'), ['int'])),
                                    ('config_excess_bandwidth_percent', (YLeaf(YType.uint32, 'config-excess-bandwidth-percent'), ['int'])),
                                    ('config_excess_bandwidth_unit', (YLeaf(YType.uint32, 'config-excess-bandwidth-unit'), ['int'])),
                                    ('hardware_excess_bandwidth_weight', (YLeaf(YType.uint32, 'hardware-excess-bandwidth-weight'), ['int'])),
                                    ('network_min_bandwidth_kbps', (YLeaf(YType.uint32, 'network-min-bandwidth-kbps'), ['int'])),
                                    ('hardware_queue_limit_bytes', (YLeaf(YType.uint64, 'hardware-queue-limit-bytes'), ['int'])),
                                    ('hardware_queue_limit_microseconds', (YLeaf(YType.uint64, 'hardware-queue-limit-microseconds'), ['int'])),
                                    ('policer_bucket_id', (YLeaf(YType.uint32, 'policer-bucket-id'), ['int'])),
                                    ('policer_stats_handle', (YLeaf(YType.uint64, 'policer-stats-handle'), ['int'])),
                                    ('hardware_policer_average_rate_kbps', (YLeaf(YType.uint32, 'hardware-policer-average-rate-kbps'), ['int'])),
                                    ('hardware_policer_peak_rate_kbps', (YLeaf(YType.uint32, 'hardware-policer-peak-rate-kbps'), ['int'])),
                                    ('hardware_policer_conform_burst_bytes', (YLeaf(YType.uint32, 'hardware-policer-conform-burst-bytes'), ['int'])),
                                    ('hardware_policer_excess_burst_bytes', (YLeaf(YType.uint32, 'hardware-policer-excess-burst-bytes'), ['int'])),
                                ])
                                self.level_one_class_name = None
                                self.level_two_class_name = None
                                self.class_level = None
                                self.egress_queue_id = None
                                self.queue_type = None
                                self.priority_level = None
                                self.hardware_max_rate_kbps = None
                                self.hardware_min_rate_kbps = None
                                self.config_excess_bandwidth_percent = None
                                self.config_excess_bandwidth_unit = None
                                self.hardware_excess_bandwidth_weight = None
                                self.network_min_bandwidth_kbps = None
                                self.hardware_queue_limit_bytes = None
                                self.hardware_queue_limit_microseconds = None
                                self.policer_bucket_id = None
                                self.policer_stats_handle = None
                                self.hardware_policer_average_rate_kbps = None
                                self.hardware_policer_peak_rate_kbps = None
                                self.hardware_policer_conform_burst_bytes = None
                                self.hardware_policer_excess_burst_bytes = None

                                self.config_max_rate = PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ConfigMaxRate()
                                self.config_max_rate.parent = self
                                self._children_name_map["config_max_rate"] = "config-max-rate"

                                self.config_min_rate = PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ConfigMinRate()
                                self.config_min_rate.parent = self
                                self._children_name_map["config_min_rate"] = "config-min-rate"

                                self.config_queue_limit = PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ConfigQueueLimit()
                                self.config_queue_limit.parent = self
                                self._children_name_map["config_queue_limit"] = "config-queue-limit"

                                self.config_policer_average_rate = PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ConfigPolicerAverageRate()
                                self.config_policer_average_rate.parent = self
                                self._children_name_map["config_policer_average_rate"] = "config-policer-average-rate"

                                self.config_policer_peak_rate = PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ConfigPolicerPeakRate()
                                self.config_policer_peak_rate.parent = self
                                self._children_name_map["config_policer_peak_rate"] = "config-policer-peak-rate"

                                self.config_policer_conform_burst = PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ConfigPolicerConformBurst()
                                self.config_policer_conform_burst.parent = self
                                self._children_name_map["config_policer_conform_burst"] = "config-policer-conform-burst"

                                self.config_policer_excess_burst = PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ConfigPolicerExcessBurst()
                                self.config_policer_excess_burst.parent = self
                                self._children_name_map["config_policer_excess_burst"] = "config-policer-excess-burst"

                                self.conform_action = PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ConformAction()
                                self.conform_action.parent = self
                                self._children_name_map["conform_action"] = "conform-action"

                                self.exceed_action = PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ExceedAction()
                                self.exceed_action.parent = self
                                self._children_name_map["exceed_action"] = "exceed-action"

                                self.violate_action = PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ViolateAction()
                                self.violate_action.parent = self
                                self._children_name_map["violate_action"] = "violate-action"

                                self.ip_mark = YList(self)
                                self.common_mark = YList(self)
                                self.mpls_mark = YList(self)
                                self.wred = YList(self)
                                self._segment_path = lambda: "class" + "[level-one-class-name='" + str(self.level_one_class_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class, ['level_one_class_name', 'level_two_class_name', u'class_level', u'egress_queue_id', u'queue_type', u'priority_level', u'hardware_max_rate_kbps', u'hardware_min_rate_kbps', u'config_excess_bandwidth_percent', u'config_excess_bandwidth_unit', u'hardware_excess_bandwidth_weight', u'network_min_bandwidth_kbps', u'hardware_queue_limit_bytes', u'hardware_queue_limit_microseconds', u'policer_bucket_id', u'policer_stats_handle', u'hardware_policer_average_rate_kbps', u'hardware_policer_peak_rate_kbps', u'hardware_policer_conform_burst_bytes', u'hardware_policer_excess_burst_bytes'], name, value)


                            class ConfigMaxRate(Entity):
                                """
                                Configured maximum rate
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ConfigMaxRate, self).__init__()

                                    self.yang_name = "config-max-rate"
                                    self.yang_parent_name = "class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                        ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                    ])
                                    self.policy_value = None
                                    self.policy_unit = None
                                    self._segment_path = lambda: "config-max-rate"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ConfigMaxRate, [u'policy_value', u'policy_unit'], name, value)


                            class ConfigMinRate(Entity):
                                """
                                Configured minimum rate
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ConfigMinRate, self).__init__()

                                    self.yang_name = "config-min-rate"
                                    self.yang_parent_name = "class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                        ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                    ])
                                    self.policy_value = None
                                    self.policy_unit = None
                                    self._segment_path = lambda: "config-min-rate"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ConfigMinRate, [u'policy_value', u'policy_unit'], name, value)


                            class ConfigQueueLimit(Entity):
                                """
                                Configured queue limit
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ConfigQueueLimit, self).__init__()

                                    self.yang_name = "config-queue-limit"
                                    self.yang_parent_name = "class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                        ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                    ])
                                    self.policy_value = None
                                    self.policy_unit = None
                                    self._segment_path = lambda: "config-queue-limit"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ConfigQueueLimit, [u'policy_value', u'policy_unit'], name, value)


                            class ConfigPolicerAverageRate(Entity):
                                """
                                Configured policer average rate
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ConfigPolicerAverageRate, self).__init__()

                                    self.yang_name = "config-policer-average-rate"
                                    self.yang_parent_name = "class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                        ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                    ])
                                    self.policy_value = None
                                    self.policy_unit = None
                                    self._segment_path = lambda: "config-policer-average-rate"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ConfigPolicerAverageRate, [u'policy_value', u'policy_unit'], name, value)


                            class ConfigPolicerPeakRate(Entity):
                                """
                                Config policer peak rate
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ConfigPolicerPeakRate, self).__init__()

                                    self.yang_name = "config-policer-peak-rate"
                                    self.yang_parent_name = "class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                        ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                    ])
                                    self.policy_value = None
                                    self.policy_unit = None
                                    self._segment_path = lambda: "config-policer-peak-rate"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ConfigPolicerPeakRate, [u'policy_value', u'policy_unit'], name, value)


                            class ConfigPolicerConformBurst(Entity):
                                """
                                Configured policer conform burst
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ConfigPolicerConformBurst, self).__init__()

                                    self.yang_name = "config-policer-conform-burst"
                                    self.yang_parent_name = "class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                        ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                    ])
                                    self.policy_value = None
                                    self.policy_unit = None
                                    self._segment_path = lambda: "config-policer-conform-burst"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ConfigPolicerConformBurst, [u'policy_value', u'policy_unit'], name, value)


                            class ConfigPolicerExcessBurst(Entity):
                                """
                                Configured policer excess burst
                                
                                .. attribute:: policy_value
                                
                                	Policy value
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: policy_unit
                                
                                	Policy unit
                                	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ConfigPolicerExcessBurst, self).__init__()

                                    self.yang_name = "config-policer-excess-burst"
                                    self.yang_parent_name = "class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                        ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                    ])
                                    self.policy_value = None
                                    self.policy_unit = None
                                    self._segment_path = lambda: "config-policer-excess-burst"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ConfigPolicerExcessBurst, [u'policy_value', u'policy_unit'], name, value)


                            class ConformAction(Entity):
                                """
                                Conform action
                                
                                .. attribute:: action_type
                                
                                	Policer action type
                                	**type**\:  :py:class:`DnxQoseaShowAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowAction>`
                                
                                .. attribute:: mark
                                
                                	Action mark
                                	**type**\: list of  		 :py:class:`Mark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ConformAction.Mark>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ConformAction, self).__init__()

                                    self.yang_name = "conform-action"
                                    self.yang_parent_name = "class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("mark", ("mark", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ConformAction.Mark))])
                                    self._leafs = OrderedDict([
                                        ('action_type', (YLeaf(YType.enumeration, 'action-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowAction', '')])),
                                    ])
                                    self.action_type = None

                                    self.mark = YList(self)
                                    self._segment_path = lambda: "conform-action"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ConformAction, [u'action_type'], name, value)


                                class Mark(Entity):
                                    """
                                    Action mark
                                    
                                    .. attribute:: mark_type
                                    
                                    	Mark type
                                    	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                    
                                    .. attribute:: mark_value
                                    
                                    	Mark value
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ConformAction.Mark, self).__init__()

                                        self.yang_name = "mark"
                                        self.yang_parent_name = "conform-action"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                            ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                        ])
                                        self.mark_type = None
                                        self.mark_value = None
                                        self._segment_path = lambda: "mark"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ConformAction.Mark, [u'mark_type', u'mark_value'], name, value)


                            class ExceedAction(Entity):
                                """
                                Exceed action
                                
                                .. attribute:: action_type
                                
                                	Policer action type
                                	**type**\:  :py:class:`DnxQoseaShowAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowAction>`
                                
                                .. attribute:: mark
                                
                                	Action mark
                                	**type**\: list of  		 :py:class:`Mark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ExceedAction.Mark>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ExceedAction, self).__init__()

                                    self.yang_name = "exceed-action"
                                    self.yang_parent_name = "class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("mark", ("mark", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ExceedAction.Mark))])
                                    self._leafs = OrderedDict([
                                        ('action_type', (YLeaf(YType.enumeration, 'action-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowAction', '')])),
                                    ])
                                    self.action_type = None

                                    self.mark = YList(self)
                                    self._segment_path = lambda: "exceed-action"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ExceedAction, [u'action_type'], name, value)


                                class Mark(Entity):
                                    """
                                    Action mark
                                    
                                    .. attribute:: mark_type
                                    
                                    	Mark type
                                    	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                    
                                    .. attribute:: mark_value
                                    
                                    	Mark value
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ExceedAction.Mark, self).__init__()

                                        self.yang_name = "mark"
                                        self.yang_parent_name = "exceed-action"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                            ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                        ])
                                        self.mark_type = None
                                        self.mark_value = None
                                        self._segment_path = lambda: "mark"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ExceedAction.Mark, [u'mark_type', u'mark_value'], name, value)


                            class ViolateAction(Entity):
                                """
                                Violate action
                                
                                .. attribute:: action_type
                                
                                	Policer action type
                                	**type**\:  :py:class:`DnxQoseaShowAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowAction>`
                                
                                .. attribute:: mark
                                
                                	Action mark
                                	**type**\: list of  		 :py:class:`Mark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ViolateAction.Mark>`
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ViolateAction, self).__init__()

                                    self.yang_name = "violate-action"
                                    self.yang_parent_name = "class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("mark", ("mark", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ViolateAction.Mark))])
                                    self._leafs = OrderedDict([
                                        ('action_type', (YLeaf(YType.enumeration, 'action-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowAction', '')])),
                                    ])
                                    self.action_type = None

                                    self.mark = YList(self)
                                    self._segment_path = lambda: "violate-action"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ViolateAction, [u'action_type'], name, value)


                                class Mark(Entity):
                                    """
                                    Action mark
                                    
                                    .. attribute:: mark_type
                                    
                                    	Mark type
                                    	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                    
                                    .. attribute:: mark_value
                                    
                                    	Mark value
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ViolateAction.Mark, self).__init__()

                                        self.yang_name = "mark"
                                        self.yang_parent_name = "violate-action"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                            ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                        ])
                                        self.mark_type = None
                                        self.mark_value = None
                                        self._segment_path = lambda: "mark"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.ViolateAction.Mark, [u'mark_type', u'mark_value'], name, value)


                            class IpMark(Entity):
                                """
                                IP mark
                                
                                .. attribute:: mark_type
                                
                                	Mark type
                                	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                
                                .. attribute:: mark_value
                                
                                	Mark value
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.IpMark, self).__init__()

                                    self.yang_name = "ip-mark"
                                    self.yang_parent_name = "class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                        ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                    ])
                                    self.mark_type = None
                                    self.mark_value = None
                                    self._segment_path = lambda: "ip-mark"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.IpMark, [u'mark_type', u'mark_value'], name, value)


                            class CommonMark(Entity):
                                """
                                Common mark
                                
                                .. attribute:: mark_type
                                
                                	Mark type
                                	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                
                                .. attribute:: mark_value
                                
                                	Mark value
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.CommonMark, self).__init__()

                                    self.yang_name = "common-mark"
                                    self.yang_parent_name = "class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                        ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                    ])
                                    self.mark_type = None
                                    self.mark_value = None
                                    self._segment_path = lambda: "common-mark"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.CommonMark, [u'mark_type', u'mark_value'], name, value)


                            class MplsMark(Entity):
                                """
                                MPLS mark
                                
                                .. attribute:: mark_type
                                
                                	Mark type
                                	**type**\:  :py:class:`DnxQoseaShowMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowMark>`
                                
                                .. attribute:: mark_value
                                
                                	Mark value
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.MplsMark, self).__init__()

                                    self.yang_name = "mpls-mark"
                                    self.yang_parent_name = "class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('mark_type', (YLeaf(YType.enumeration, 'mark-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMark', '')])),
                                        ('mark_value', (YLeaf(YType.uint16, 'mark-value'), ['int'])),
                                    ])
                                    self.mark_type = None
                                    self.mark_value = None
                                    self._segment_path = lambda: "mpls-mark"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.MplsMark, [u'mark_type', u'mark_value'], name, value)


                            class Wred(Entity):
                                """
                                WRED parameters
                                
                                .. attribute:: wred_match_value
                                
                                	WRED match values
                                	**type**\:  :py:class:`WredMatchValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.Wred.WredMatchValue>`
                                
                                .. attribute:: config_min_threshold
                                
                                	Configured minimum threshold
                                	**type**\:  :py:class:`ConfigMinThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.Wred.ConfigMinThreshold>`
                                
                                .. attribute:: config_max_threshold
                                
                                	Configured maximum threshold
                                	**type**\:  :py:class:`ConfigMaxThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.Wred.ConfigMaxThreshold>`
                                
                                .. attribute:: wred_match_type
                                
                                	WREDMatchType
                                	**type**\:  :py:class:`DnxQoseaShowWred <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.DnxQoseaShowWred>`
                                
                                .. attribute:: hardware_min_threshold_bytes
                                
                                	Hardware minimum threshold
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: hardware_max_threshold_bytes
                                
                                	Hardware maximum threshold
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: first_segment
                                
                                	First segment
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: segment_size
                                
                                	Segment size
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ncs5500-qos-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.Wred, self).__init__()

                                    self.yang_name = "wred"
                                    self.yang_parent_name = "class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("wred-match-value", ("wred_match_value", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.Wred.WredMatchValue)), ("config-min-threshold", ("config_min_threshold", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.Wred.ConfigMinThreshold)), ("config-max-threshold", ("config_max_threshold", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.Wred.ConfigMaxThreshold))])
                                    self._leafs = OrderedDict([
                                        ('wred_match_type', (YLeaf(YType.enumeration, 'wred-match-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowWred', '')])),
                                        ('hardware_min_threshold_bytes', (YLeaf(YType.uint32, 'hardware-min-threshold-bytes'), ['int'])),
                                        ('hardware_max_threshold_bytes', (YLeaf(YType.uint32, 'hardware-max-threshold-bytes'), ['int'])),
                                        ('first_segment', (YLeaf(YType.uint16, 'first-segment'), ['int'])),
                                        ('segment_size', (YLeaf(YType.uint32, 'segment-size'), ['int'])),
                                    ])
                                    self.wred_match_type = None
                                    self.hardware_min_threshold_bytes = None
                                    self.hardware_max_threshold_bytes = None
                                    self.first_segment = None
                                    self.segment_size = None

                                    self.wred_match_value = PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.Wred.WredMatchValue()
                                    self.wred_match_value.parent = self
                                    self._children_name_map["wred_match_value"] = "wred-match-value"

                                    self.config_min_threshold = PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.Wred.ConfigMinThreshold()
                                    self.config_min_threshold.parent = self
                                    self._children_name_map["config_min_threshold"] = "config-min-threshold"

                                    self.config_max_threshold = PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.Wred.ConfigMaxThreshold()
                                    self.config_max_threshold.parent = self
                                    self._children_name_map["config_max_threshold"] = "config-max-threshold"
                                    self._segment_path = lambda: "wred"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.Wred, [u'wred_match_type', u'hardware_min_threshold_bytes', u'hardware_max_threshold_bytes', u'first_segment', u'segment_size'], name, value)


                                class WredMatchValue(Entity):
                                    """
                                    WRED match values
                                    
                                    .. attribute:: dnx_qosea_show_red_match_value
                                    
                                    	dnx qosea show red match value
                                    	**type**\: list of  		 :py:class:`DnxQoseaShowRedMatchValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.Wred.WredMatchValue, self).__init__()

                                        self.yang_name = "wred-match-value"
                                        self.yang_parent_name = "wred"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("dnx-qosea-show-red-match-value", ("dnx_qosea_show_red_match_value", PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue))])
                                        self._leafs = OrderedDict()

                                        self.dnx_qosea_show_red_match_value = YList(self)
                                        self._segment_path = lambda: "wred-match-value"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.Wred.WredMatchValue, [], name, value)


                                    class DnxQoseaShowRedMatchValue(Entity):
                                        """
                                        dnx qosea show red match value
                                        
                                        .. attribute:: range_start
                                        
                                        	Start value of a range
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: range_end
                                        
                                        	End value of a range
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'ncs5500-qos-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue, self).__init__()

                                            self.yang_name = "dnx-qosea-show-red-match-value"
                                            self.yang_parent_name = "wred-match-value"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('range_start', (YLeaf(YType.uint8, 'range-start'), ['int'])),
                                                ('range_end', (YLeaf(YType.uint8, 'range-end'), ['int'])),
                                            ])
                                            self.range_start = None
                                            self.range_end = None
                                            self._segment_path = lambda: "dnx-qosea-show-red-match-value"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue, [u'range_start', u'range_end'], name, value)


                                class ConfigMinThreshold(Entity):
                                    """
                                    Configured minimum threshold
                                    
                                    .. attribute:: policy_value
                                    
                                    	Policy value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: policy_unit
                                    
                                    	Policy unit
                                    	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.Wred.ConfigMinThreshold, self).__init__()

                                        self.yang_name = "config-min-threshold"
                                        self.yang_parent_name = "wred"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                            ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                        ])
                                        self.policy_value = None
                                        self.policy_unit = None
                                        self._segment_path = lambda: "config-min-threshold"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.Wred.ConfigMinThreshold, [u'policy_value', u'policy_unit'], name, value)


                                class ConfigMaxThreshold(Entity):
                                    """
                                    Configured maximum threshold
                                    
                                    .. attribute:: policy_value
                                    
                                    	Policy value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: policy_unit
                                    
                                    	Policy unit
                                    	**type**\:  :py:class:`PolicyParamUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PolicyParamUnit>`
                                    
                                    

                                    """

                                    _prefix = 'ncs5500-qos-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.Wred.ConfigMaxThreshold, self).__init__()

                                        self.yang_name = "config-max-threshold"
                                        self.yang_parent_name = "wred"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('policy_value', (YLeaf(YType.uint32, 'policy-value'), ['int'])),
                                            ('policy_unit', (YLeaf(YType.enumeration, 'policy-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnit', '')])),
                                        ])
                                        self.policy_value = None
                                        self.policy_unit = None
                                        self._segment_path = lambda: "config-max-threshold"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaceSingles.BundleInterfaceSingle.ClassTable.Class.Wred.ConfigMaxThreshold, [u'policy_value', u'policy_unit'], name, value)


            class RemoteInterfaces(Entity):
                """
                QoS list of remote interfaces
                
                .. attribute:: remote_interface
                
                	QoS remote interface names
                	**type**\: list of  		 :py:class:`RemoteInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface>`
                
                

                """

                _prefix = 'ncs5500-qos-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PlatformQos.Nodes.Node.RemoteInterfaces, self).__init__()

                    self.yang_name = "remote-interfaces"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("remote-interface", ("remote_interface", PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface))])
                    self._leafs = OrderedDict()

                    self.remote_interface = YList(self)
                    self._segment_path = lambda: "remote-interfaces"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PlatformQos.Nodes.Node.RemoteInterfaces, [], name, value)


                class RemoteInterface(Entity):
                    """
                    QoS remote interface names
                    
                    .. attribute:: interface_name  (key)
                    
                    	The name of the remote interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: policy_name
                    
                    	Policy Name
                    	**type**\: str
                    
                    	**length:** 0..64
                    
                    .. attribute:: virtual_output_queue_statistics_handle
                    
                    	Virtual output queue statistics handle
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: interface_handle
                    
                    	Interface Handle
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_virtual_output_queues
                    
                    	Number of Virtual Output Queues
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_classes
                    
                    	Number of Classes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: remote_class
                    
                    	Remote Class array
                    	**type**\: list of  		 :py:class:`RemoteClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass>`
                    
                    

                    """

                    _prefix = 'ncs5500-qos-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface, self).__init__()

                        self.yang_name = "remote-interface"
                        self.yang_parent_name = "remote-interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([("remote-class", ("remote_class", PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                            ('virtual_output_queue_statistics_handle', (YLeaf(YType.uint64, 'virtual-output-queue-statistics-handle'), ['int'])),
                            ('interface_handle', (YLeaf(YType.uint32, 'interface-handle'), ['int'])),
                            ('number_of_virtual_output_queues', (YLeaf(YType.uint32, 'number-of-virtual-output-queues'), ['int'])),
                            ('number_of_classes', (YLeaf(YType.uint32, 'number-of-classes'), ['int'])),
                        ])
                        self.interface_name = None
                        self.policy_name = None
                        self.virtual_output_queue_statistics_handle = None
                        self.interface_handle = None
                        self.number_of_virtual_output_queues = None
                        self.number_of_classes = None

                        self.remote_class = YList(self)
                        self._segment_path = lambda: "remote-interface" + "[interface-name='" + str(self.interface_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface, ['interface_name', u'policy_name', u'virtual_output_queue_statistics_handle', u'interface_handle', u'number_of_virtual_output_queues', u'number_of_classes'], name, value)


                    class RemoteClass(Entity):
                        """
                        Remote Class array
                        
                        .. attribute:: class_name
                        
                        	Class Name
                        	**type**\: str
                        
                        	**length:** 0..64
                        
                        .. attribute:: class_id
                        
                        	Class ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: cos_q
                        
                        	Class of Service Queue
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: queue_limit
                        
                        	Default/Configured queue limit in bytes
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: byte
                        
                        .. attribute:: hardware_queue_limit
                        
                        	Hardware queue limit in bytes
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: byte
                        
                        .. attribute:: wred
                        
                        	Default/Configured WRED profiles
                        	**type**\: list of  		 :py:class:`Wred <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass.Wred>`
                        
                        .. attribute:: hw_wred
                        
                        	Hardware WRED profiles
                        	**type**\: list of  		 :py:class:`HwWred <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper.PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass.HwWred>`
                        
                        

                        """

                        _prefix = 'ncs5500-qos-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass, self).__init__()

                            self.yang_name = "remote-class"
                            self.yang_parent_name = "remote-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("wred", ("wred", PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass.Wred)), ("hw-wred", ("hw_wred", PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass.HwWred))])
                            self._leafs = OrderedDict([
                                ('class_name', (YLeaf(YType.str, 'class-name'), ['str'])),
                                ('class_id', (YLeaf(YType.uint32, 'class-id'), ['int'])),
                                ('cos_q', (YLeaf(YType.uint32, 'cos-q'), ['int'])),
                                ('queue_limit', (YLeaf(YType.uint32, 'queue-limit'), ['int'])),
                                ('hardware_queue_limit', (YLeaf(YType.uint32, 'hardware-queue-limit'), ['int'])),
                            ])
                            self.class_name = None
                            self.class_id = None
                            self.cos_q = None
                            self.queue_limit = None
                            self.hardware_queue_limit = None

                            self.wred = YList(self)
                            self.hw_wred = YList(self)
                            self._segment_path = lambda: "remote-class"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass, [u'class_name', u'class_id', u'cos_q', u'queue_limit', u'hardware_queue_limit'], name, value)


                        class Wred(Entity):
                            """
                            Default/Configured WRED profiles
                            
                            .. attribute:: min_threshold
                            
                            	Minimum Threshold
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: max_threshold
                            
                            	Maximum Threshold
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: drop_probability
                            
                            	Drop Probability
                            	**type**\: int
                            
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
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('min_threshold', (YLeaf(YType.uint32, 'min-threshold'), ['int'])),
                                    ('max_threshold', (YLeaf(YType.uint32, 'max-threshold'), ['int'])),
                                    ('drop_probability', (YLeaf(YType.uint32, 'drop-probability'), ['int'])),
                                ])
                                self.min_threshold = None
                                self.max_threshold = None
                                self.drop_probability = None
                                self._segment_path = lambda: "wred"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass.Wred, [u'min_threshold', u'max_threshold', u'drop_probability'], name, value)


                        class HwWred(Entity):
                            """
                            Hardware WRED profiles
                            
                            .. attribute:: min_threshold
                            
                            	Minimum Threshold
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: max_threshold
                            
                            	Maximum Threshold
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: drop_probability
                            
                            	Drop Probability
                            	**type**\: int
                            
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
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('min_threshold', (YLeaf(YType.uint32, 'min-threshold'), ['int'])),
                                    ('max_threshold', (YLeaf(YType.uint32, 'max-threshold'), ['int'])),
                                    ('drop_probability', (YLeaf(YType.uint32, 'drop-probability'), ['int'])),
                                ])
                                self.min_threshold = None
                                self.max_threshold = None
                                self.drop_probability = None
                                self._segment_path = lambda: "hw-wred"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass.HwWred, [u'min_threshold', u'max_threshold', u'drop_probability'], name, value)

    def clone_ptr(self):
        self._top_entity = PlatformQos()
        return self._top_entity


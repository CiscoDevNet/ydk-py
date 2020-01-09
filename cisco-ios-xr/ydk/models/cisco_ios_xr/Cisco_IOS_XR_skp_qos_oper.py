""" Cisco_IOS_XR_skp_qos_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR skp\-qos package operational data.

This module contains definitions
for the following management objects\:
  platform\-qos\: QoS Skywarp platform operational data
  platform\-qos\-ea\: platform qos ea

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Action(Enum):
    """
    Action (Enum Class)

    Action type

    .. data:: police_transmit = 0

    	Police action transmit

    .. data:: police_set_transmit = 1

    	Police action set transmit

    .. data:: police_drop = 2

    	Police action drop

    .. data:: police_unknown = 3

    	Police action unknown

    """

    police_transmit = Enum.YLeaf(0, "police-transmit")

    police_set_transmit = Enum.YLeaf(1, "police-set-transmit")

    police_drop = Enum.YLeaf(2, "police-drop")

    police_unknown = Enum.YLeaf(3, "police-unknown")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
        return meta._meta_table['Action']


class ActionOpcode(Enum):
    """
    ActionOpcode (Enum Class)

    Action opcode

    .. data:: precedence = 0

    	Precedence

    .. data:: dscp = 1

    	DSCP

    .. data:: discard_class = 2

    	Discard class

    .. data:: qos_group = 3

    	QoS group

    .. data:: cos_inner = 4

    	COS inner

    .. data:: cos = 5

    	COS

    .. data:: exp_top = 6

    	EXP top

    .. data:: exp_imp = 7

    	EXP IMP

    .. data:: tunnel_precedence = 8

    	Tunnel precedence

    .. data:: tunnel_dscp = 9

    	Tunnel DSCP

    .. data:: itag_dei = 10

    	ITAG DEI

    .. data:: itag_cos = 11

    	ITAG COS

    .. data:: cos_imposition = 12

    	COS imposition

    .. data:: dei_imposition = 13

    	DEI imposition

    .. data:: dei = 14

    	DEI

    .. data:: no_marking = 15

    	No marking

    """

    precedence = Enum.YLeaf(0, "precedence")

    dscp = Enum.YLeaf(1, "dscp")

    discard_class = Enum.YLeaf(2, "discard-class")

    qos_group = Enum.YLeaf(3, "qos-group")

    cos_inner = Enum.YLeaf(4, "cos-inner")

    cos = Enum.YLeaf(5, "cos")

    exp_top = Enum.YLeaf(6, "exp-top")

    exp_imp = Enum.YLeaf(7, "exp-imp")

    tunnel_precedence = Enum.YLeaf(8, "tunnel-precedence")

    tunnel_dscp = Enum.YLeaf(9, "tunnel-dscp")

    itag_dei = Enum.YLeaf(10, "itag-dei")

    itag_cos = Enum.YLeaf(11, "itag-cos")

    cos_imposition = Enum.YLeaf(12, "cos-imposition")

    dei_imposition = Enum.YLeaf(13, "dei-imposition")

    dei = Enum.YLeaf(14, "dei")

    no_marking = Enum.YLeaf(15, "no-marking")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
        return meta._meta_table['ActionOpcode']


class CacState(Enum):
    """
    CacState (Enum Class)

    CAC/UBRL class states

    .. data:: unknown = 0

    	unknown

    .. data:: admit = 1

    	admit

    .. data:: redirect = 2

    	redirect

    .. data:: ubrl = 3

    	ubrl

    """

    unknown = Enum.YLeaf(0, "unknown")

    admit = Enum.YLeaf(1, "admit")

    redirect = Enum.YLeaf(2, "redirect")

    ubrl = Enum.YLeaf(3, "ubrl")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
        return meta._meta_table['CacState']


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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
        return meta._meta_table['PolicyParamUnit']


class PolicyState(Enum):
    """
    PolicyState (Enum Class)

    Different Interface states

    .. data:: active = 0

    	active

    .. data:: suspended = 1

    	suspended

    """

    active = Enum.YLeaf(0, "active")

    suspended = Enum.YLeaf(1, "suspended")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
        return meta._meta_table['PolicyState']


class QosUnit(Enum):
    """
    QosUnit (Enum Class)

    QoS parameter unit

    .. data:: invalid = 0

    	Invalid type

    .. data:: bytes = 1

    	Bytes

    .. data:: kilobytes = 2

    	Kilobytes

    .. data:: megabytes = 3

    	Megabytes

    .. data:: gigabytes = 4

    	Gigabytes

    .. data:: bps = 5

    	Bits per second

    .. data:: kbps = 6

    	Kilo bits per second

    .. data:: mbps = 7

    	Mega bits per second

    .. data:: gbps = 8

    	Giga bits per second

    .. data:: cells_per_second = 9

    	Cells per second

    .. data:: packets_per_second = 10

    	Packets per second

    .. data:: microsecond = 11

    	Microsecond

    .. data:: millisecond = 12

    	Millisecond

    .. data:: packets = 13

    	Number of packets

    .. data:: cells = 14

    	Number of cells

    .. data:: percentage = 15

    	Percentage

    .. data:: ratio = 16

    	Ratio

    """

    invalid = Enum.YLeaf(0, "invalid")

    bytes = Enum.YLeaf(1, "bytes")

    kilobytes = Enum.YLeaf(2, "kilobytes")

    megabytes = Enum.YLeaf(3, "megabytes")

    gigabytes = Enum.YLeaf(4, "gigabytes")

    bps = Enum.YLeaf(5, "bps")

    kbps = Enum.YLeaf(6, "kbps")

    mbps = Enum.YLeaf(7, "mbps")

    gbps = Enum.YLeaf(8, "gbps")

    cells_per_second = Enum.YLeaf(9, "cells-per-second")

    packets_per_second = Enum.YLeaf(10, "packets-per-second")

    microsecond = Enum.YLeaf(11, "microsecond")

    millisecond = Enum.YLeaf(12, "millisecond")

    packets = Enum.YLeaf(13, "packets")

    cells = Enum.YLeaf(14, "cells")

    percentage = Enum.YLeaf(15, "percentage")

    ratio = Enum.YLeaf(16, "ratio")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
        return meta._meta_table['QosUnit']


class TbAlgorithm(Enum):
    """
    TbAlgorithm (Enum Class)

    Tokenbucket type

    .. data:: inactive = 0

    	Inactive, configured but disabled

    .. data:: single = 1

    	Single token bucket

    .. data:: single_rate_tcm = 2

    	Single rate three color marker

    .. data:: two_rate_tcm = 3

    	Two rate three color marker

    .. data:: mef_tcm = 4

    	Allows coupling between CIR and PIR tb's

    .. data:: dummy = 5

    	Internal dummy token bucket for coupled-policer

    	child

    """

    inactive = Enum.YLeaf(0, "inactive")

    single = Enum.YLeaf(1, "single")

    single_rate_tcm = Enum.YLeaf(2, "single-rate-tcm")

    two_rate_tcm = Enum.YLeaf(3, "two-rate-tcm")

    mef_tcm = Enum.YLeaf(4, "mef-tcm")

    dummy = Enum.YLeaf(5, "dummy")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
        return meta._meta_table['TbAlgorithm']


class Wred(Enum):
    """
    Wred (Enum Class)

    Wred

    .. data:: wred_cos_cmd = 0

    	wred cos cmd

    .. data:: wred_dscp_cmd = 1

    	wred dscp cmd

    .. data:: wred_precedence_cmd = 2

    	wred precedence cmd

    .. data:: wred_discard_class_cmd = 3

    	wred discard class cmd

    .. data:: wred_mpls_exp_cmd = 4

    	wred mpls exp cmd

    .. data:: red_with_user_min_max = 5

    	red with user min max

    .. data:: red_with_default_min_max = 6

    	red with default min max

    .. data:: wred_dei_cmd = 7

    	wred dei cmd

    .. data:: wred_ecn_cmd = 8

    	wred ecn cmd

    .. data:: wred_invalid_cmd = 9

    	wred invalid cmd

    """

    wred_cos_cmd = Enum.YLeaf(0, "wred-cos-cmd")

    wred_dscp_cmd = Enum.YLeaf(1, "wred-dscp-cmd")

    wred_precedence_cmd = Enum.YLeaf(2, "wred-precedence-cmd")

    wred_discard_class_cmd = Enum.YLeaf(3, "wred-discard-class-cmd")

    wred_mpls_exp_cmd = Enum.YLeaf(4, "wred-mpls-exp-cmd")

    red_with_user_min_max = Enum.YLeaf(5, "red-with-user-min-max")

    red_with_default_min_max = Enum.YLeaf(6, "red-with-default-min-max")

    wred_dei_cmd = Enum.YLeaf(7, "wred-dei-cmd")

    wred_ecn_cmd = Enum.YLeaf(8, "wred-ecn-cmd")

    wred_invalid_cmd = Enum.YLeaf(9, "wred-invalid-cmd")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
        return meta._meta_table['Wred']



class PlatformQos(_Entity_):
    """
    QoS Skywarp platform operational data 
    
    .. attribute:: nodes
    
    	List of nodes with platform specific QoS configuration
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes>`
    
    	**config**\: False
    
    

    """

    _prefix = 'skp-qos-oper'
    _revision = '2016-02-18'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(PlatformQos, self).__init__()
        self._top_entity = None

        self.yang_name = "platform-qos"
        self.yang_parent_name = "Cisco-IOS-XR-skp-qos-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", PlatformQos.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = PlatformQos.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-skp-qos-oper:platform-qos"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(PlatformQos, [], name, value)


    class Nodes(_Entity_):
        """
        List of nodes with platform specific QoS
        configuration
        
        .. attribute:: node
        
        	Node with platform specific QoS configuration
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node>`
        
        	**config**\: False
        
        

        """

        _prefix = 'skp-qos-oper'
        _revision = '2016-02-18'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
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
            self._absolute_path = lambda: "Cisco-IOS-XR-skp-qos-oper:platform-qos/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PlatformQos.Nodes, [], name, value)


        class Node(_Entity_):
            """
            Node with platform specific QoS configuration
            
            .. attribute:: node_name  (key)
            
            	Node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            	**config**\: False
            
            .. attribute:: bundle_interfaces
            
            	QoS list of bundle interfaces
            	**type**\:  :py:class:`BundleInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces>`
            
            	**config**\: False
            
            .. attribute:: capability
            
            	QoS system capability
            	**type**\:  :py:class:`Capability <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Capability>`
            
            	**config**\: False
            
            .. attribute:: interfaces
            
            	QoS list of interfaces
            	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces>`
            
            	**config**\: False
            
            

            """

            _prefix = 'skp-qos-oper'
            _revision = '2016-02-18'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(PlatformQos.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("bundle-interfaces", ("bundle_interfaces", PlatformQos.Nodes.Node.BundleInterfaces)), ("capability", ("capability", PlatformQos.Nodes.Node.Capability)), ("interfaces", ("interfaces", PlatformQos.Nodes.Node.Interfaces))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.bundle_interfaces = PlatformQos.Nodes.Node.BundleInterfaces()
                self.bundle_interfaces.parent = self
                self._children_name_map["bundle_interfaces"] = "bundle-interfaces"

                self.capability = PlatformQos.Nodes.Node.Capability()
                self.capability.parent = self
                self._children_name_map["capability"] = "capability"

                self.interfaces = PlatformQos.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-skp-qos-oper:platform-qos/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PlatformQos.Nodes.Node, ['node_name'], name, value)


            class BundleInterfaces(_Entity_):
                """
                QoS list of bundle interfaces
                
                .. attribute:: bundle_interface
                
                	QoS interface name
                	**type**\: list of  		 :py:class:`BundleInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface>`
                
                	**config**\: False
                
                

                """

                _prefix = 'skp-qos-oper'
                _revision = '2016-02-18'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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


                class BundleInterface(_Entity_):
                    """
                    QoS interface name
                    
                    .. attribute:: interface_name  (key)
                    
                    	Bundle interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: member_interfaces
                    
                    	QoS list of member interfaces
                    	**type**\:  :py:class:`MemberInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'skp-qos-oper'
                    _revision = '2016-02-18'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface, self).__init__()

                        self.yang_name = "bundle-interface"
                        self.yang_parent_name = "bundle-interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([("member-interfaces", ("member_interfaces", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ])
                        self.interface_name = None

                        self.member_interfaces = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces()
                        self.member_interfaces.parent = self
                        self._children_name_map["member_interfaces"] = "member-interfaces"
                        self._segment_path = lambda: "bundle-interface" + "[interface-name='" + str(self.interface_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface, ['interface_name'], name, value)


                    class MemberInterfaces(_Entity_):
                        """
                        QoS list of member interfaces
                        
                        .. attribute:: member_interface
                        
                        	QoS interface name
                        	**type**\: list of  		 :py:class:`MemberInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'skp-qos-oper'
                        _revision = '2016-02-18'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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


                        class MemberInterface(_Entity_):
                            """
                            QoS interface name
                            
                            .. attribute:: interface_name  (key)
                            
                            	Memeber interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            	**config**\: False
                            
                            .. attribute:: bundle_input
                            
                            	QoS policy direction input
                            	**type**\:  :py:class:`BundleInput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput>`
                            
                            	**config**\: False
                            
                            .. attribute:: bundle_output
                            
                            	QoS policy direction output
                            	**type**\:  :py:class:`BundleOutput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'skp-qos-oper'
                            _revision = '2016-02-18'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface, self).__init__()

                                self.yang_name = "member-interface"
                                self.yang_parent_name = "member-interfaces"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['interface_name']
                                self._child_classes = OrderedDict([("bundle-input", ("bundle_input", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput)), ("bundle-output", ("bundle_output", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput))])
                                self._leafs = OrderedDict([
                                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ])
                                self.interface_name = None

                                self.bundle_input = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput()
                                self.bundle_input.parent = self
                                self._children_name_map["bundle_input"] = "bundle-input"

                                self.bundle_output = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput()
                                self.bundle_output.parent = self
                                self._children_name_map["bundle_output"] = "bundle-output"
                                self._segment_path = lambda: "member-interface" + "[interface-name='" + str(self.interface_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface, ['interface_name'], name, value)


                            class BundleInput(_Entity_):
                                """
                                QoS policy direction input
                                
                                .. attribute:: header
                                
                                	QoS EA policy header
                                	**type**\:  :py:class:`Header <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Header>`
                                
                                	**config**\: False
                                
                                .. attribute:: interface_parameters
                                
                                	QoS Interface Parameters
                                	**type**\:  :py:class:`InterfaceParameters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters>`
                                
                                	**config**\: False
                                
                                .. attribute:: skywarp_qos_policy_class
                                
                                	Skywarp QoS policy class details
                                	**type**\:  :py:class:`SkywarpQosPolicyClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'skp-qos-oper'
                                _revision = '2016-02-18'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput, self).__init__()

                                    self.yang_name = "bundle-input"
                                    self.yang_parent_name = "member-interface"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("header", ("header", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Header)), ("interface-parameters", ("interface_parameters", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters)), ("skywarp-qos-policy-class", ("skywarp_qos_policy_class", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass))])
                                    self._leafs = OrderedDict()

                                    self.header = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Header()
                                    self.header.parent = self
                                    self._children_name_map["header"] = "header"

                                    self.interface_parameters = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters()
                                    self.interface_parameters.parent = self
                                    self._children_name_map["interface_parameters"] = "interface-parameters"

                                    self.skywarp_qos_policy_class = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass()
                                    self.skywarp_qos_policy_class.parent = self
                                    self._children_name_map["skywarp_qos_policy_class"] = "skywarp-qos-policy-class"
                                    self._segment_path = lambda: "bundle-input"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput, [], name, value)


                                class Header(_Entity_):
                                    """
                                    QoS EA policy header
                                    
                                    .. attribute:: interface_name
                                    
                                    	Interface Name
                                    	**type**\: str
                                    
                                    	**length:** 0..101
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: policy_name
                                    
                                    	Policy name
                                    	**type**\: str
                                    
                                    	**length:** 0..65
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: direction
                                    
                                    	Direction
                                    	**type**\: str
                                    
                                    	**length:** 0..11
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: classes
                                    
                                    	Number of classes
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'skp-qos-oper'
                                    _revision = '2016-02-18'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Header, self).__init__()

                                        self.yang_name = "header"
                                        self.yang_parent_name = "bundle-input"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                            ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                            ('direction', (YLeaf(YType.str, 'direction'), ['str'])),
                                            ('classes', (YLeaf(YType.uint16, 'classes'), ['int'])),
                                        ])
                                        self.interface_name = None
                                        self.policy_name = None
                                        self.direction = None
                                        self.classes = None
                                        self._segment_path = lambda: "header"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Header, ['interface_name', 'policy_name', 'direction', 'classes'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Header']['meta_info']


                                class InterfaceParameters(_Entity_):
                                    """
                                    QoS Interface Parameters
                                    
                                    .. attribute:: interface_config_rate
                                    
                                    	Interface Configured Rate
                                    	**type**\:  :py:class:`InterfaceConfigRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters.InterfaceConfigRate>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: interface_program_rate
                                    
                                    	Interface Programmed Rate
                                    	**type**\:  :py:class:`InterfaceProgramRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters.InterfaceProgramRate>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: port_shaper_rate
                                    
                                    	Port Shaper Rate
                                    	**type**\:  :py:class:`PortShaperRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters.PortShaperRate>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'skp-qos-oper'
                                    _revision = '2016-02-18'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters, self).__init__()

                                        self.yang_name = "interface-parameters"
                                        self.yang_parent_name = "bundle-input"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("interface-config-rate", ("interface_config_rate", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters.InterfaceConfigRate)), ("interface-program-rate", ("interface_program_rate", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters.InterfaceProgramRate)), ("port-shaper-rate", ("port_shaper_rate", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters.PortShaperRate))])
                                        self._leafs = OrderedDict()

                                        self.interface_config_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters.InterfaceConfigRate()
                                        self.interface_config_rate.parent = self
                                        self._children_name_map["interface_config_rate"] = "interface-config-rate"

                                        self.interface_program_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters.InterfaceProgramRate()
                                        self.interface_program_rate.parent = self
                                        self._children_name_map["interface_program_rate"] = "interface-program-rate"

                                        self.port_shaper_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters.PortShaperRate()
                                        self.port_shaper_rate.parent = self
                                        self._children_name_map["port_shaper_rate"] = "port-shaper-rate"
                                        self._segment_path = lambda: "interface-parameters"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters, [], name, value)


                                    class InterfaceConfigRate(_Entity_):
                                        """
                                        Interface Configured Rate
                                        
                                        .. attribute:: value
                                        
                                        	Config value
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: unit
                                        
                                        	Config unit
                                        	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters.InterfaceConfigRate, self).__init__()

                                            self.yang_name = "interface-config-rate"
                                            self.yang_parent_name = "interface-parameters"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                            ])
                                            self.value = None
                                            self.unit = None
                                            self._segment_path = lambda: "interface-config-rate"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters.InterfaceConfigRate, ['value', 'unit'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters.InterfaceConfigRate']['meta_info']


                                    class InterfaceProgramRate(_Entity_):
                                        """
                                        Interface Programmed Rate
                                        
                                        .. attribute:: value
                                        
                                        	Config value
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: unit
                                        
                                        	Config unit
                                        	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters.InterfaceProgramRate, self).__init__()

                                            self.yang_name = "interface-program-rate"
                                            self.yang_parent_name = "interface-parameters"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                            ])
                                            self.value = None
                                            self.unit = None
                                            self._segment_path = lambda: "interface-program-rate"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters.InterfaceProgramRate, ['value', 'unit'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters.InterfaceProgramRate']['meta_info']


                                    class PortShaperRate(_Entity_):
                                        """
                                        Port Shaper Rate
                                        
                                        .. attribute:: value
                                        
                                        	Config value
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: unit
                                        
                                        	Config unit
                                        	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters.PortShaperRate, self).__init__()

                                            self.yang_name = "port-shaper-rate"
                                            self.yang_parent_name = "interface-parameters"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                            ])
                                            self.value = None
                                            self.unit = None
                                            self._segment_path = lambda: "port-shaper-rate"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters.PortShaperRate, ['value', 'unit'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters.PortShaperRate']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.InterfaceParameters']['meta_info']


                                class SkywarpQosPolicyClass(_Entity_):
                                    """
                                    Skywarp QoS policy class details
                                    
                                    .. attribute:: qos_show_pclass_st
                                    
                                    	qos show pclass st
                                    	**type**\: list of  		 :py:class:`QosShowPclassSt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'skp-qos-oper'
                                    _revision = '2016-02-18'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass, self).__init__()

                                        self.yang_name = "skywarp-qos-policy-class"
                                        self.yang_parent_name = "bundle-input"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("qos-show-pclass-st", ("qos_show_pclass_st", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt))])
                                        self._leafs = OrderedDict()

                                        self.qos_show_pclass_st = YList(self)
                                        self._segment_path = lambda: "skywarp-qos-policy-class"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass, [], name, value)


                                    class QosShowPclassSt(_Entity_):
                                        """
                                        qos show pclass st
                                        
                                        .. attribute:: queue
                                        
                                        	QoS Queue parameters
                                        	**type**\:  :py:class:`Queue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Queue>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: shape
                                        
                                        	QoS EA Shaper parameters
                                        	**type**\:  :py:class:`Shape <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Shape>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: wfq
                                        
                                        	QoS WFQ parameters
                                        	**type**\:  :py:class:`Wfq <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: police
                                        
                                        	QoS Policer parameters
                                        	**type**\:  :py:class:`Police <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Police>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: marking
                                        
                                        	QoS Mark parameters
                                        	**type**\:  :py:class:`Marking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: class_level
                                        
                                        	Class level
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: class_name
                                        
                                        	Class name
                                        	**type**\: str
                                        
                                        	**length:** 0..65
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt, self).__init__()

                                            self.yang_name = "qos-show-pclass-st"
                                            self.yang_parent_name = "skywarp-qos-policy-class"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("queue", ("queue", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Queue)), ("shape", ("shape", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Shape)), ("wfq", ("wfq", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq)), ("police", ("police", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Police)), ("marking", ("marking", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking))])
                                            self._leafs = OrderedDict([
                                                ('class_level', (YLeaf(YType.uint8, 'class-level'), ['int'])),
                                                ('class_name', (YLeaf(YType.str, 'class-name'), ['str'])),
                                            ])
                                            self.class_level = None
                                            self.class_name = None

                                            self.queue = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Queue()
                                            self.queue.parent = self
                                            self._children_name_map["queue"] = "queue"

                                            self.shape = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Shape()
                                            self.shape.parent = self
                                            self._children_name_map["shape"] = "shape"

                                            self.wfq = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq()
                                            self.wfq.parent = self
                                            self._children_name_map["wfq"] = "wfq"

                                            self.police = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Police()
                                            self.police.parent = self
                                            self._children_name_map["police"] = "police"

                                            self.marking = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking()
                                            self.marking.parent = self
                                            self._children_name_map["marking"] = "marking"
                                            self._segment_path = lambda: "qos-show-pclass-st"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt, ['class_level', 'class_name'], name, value)


                                        class Queue(_Entity_):
                                            """
                                            QoS Queue parameters
                                            
                                            .. attribute:: queue_id
                                            
                                            	Queue ID
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: queue_type
                                            
                                            	Queue Type
                                            	**type**\: str
                                            
                                            	**length:** 0..101
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Queue, self).__init__()

                                                self.yang_name = "queue"
                                                self.yang_parent_name = "qos-show-pclass-st"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('queue_id', (YLeaf(YType.uint32, 'queue-id'), ['int'])),
                                                    ('queue_type', (YLeaf(YType.str, 'queue-type'), ['str'])),
                                                ])
                                                self.queue_id = None
                                                self.queue_type = None
                                                self._segment_path = lambda: "queue"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Queue, ['queue_id', 'queue_type'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Queue']['meta_info']


                                        class Shape(_Entity_):
                                            """
                                            QoS EA Shaper parameters
                                            
                                            .. attribute:: pir
                                            
                                            	PIR in kbps
                                            	**type**\:  :py:class:`Pir <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: pbs
                                            
                                            	PBS in bytes
                                            	**type**\:  :py:class:`Pbs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs>`
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Shape, self).__init__()

                                                self.yang_name = "shape"
                                                self.yang_parent_name = "qos-show-pclass-st"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("pir", ("pir", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir)), ("pbs", ("pbs", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs))])
                                                self._leafs = OrderedDict()

                                                self.pir = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir()
                                                self.pir.parent = self
                                                self._children_name_map["pir"] = "pir"

                                                self.pbs = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs()
                                                self.pbs.parent = self
                                                self._children_name_map["pbs"] = "pbs"
                                                self._segment_path = lambda: "shape"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Shape, [], name, value)


                                            class Pir(_Entity_):
                                                """
                                                PIR in kbps
                                                
                                                .. attribute:: value
                                                
                                                	Config value
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: unit
                                                
                                                	Config unit
                                                	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir, self).__init__()

                                                    self.yang_name = "pir"
                                                    self.yang_parent_name = "shape"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                        ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                                    ])
                                                    self.value = None
                                                    self.unit = None
                                                    self._segment_path = lambda: "pir"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir, ['value', 'unit'], name, value)

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir']['meta_info']


                                            class Pbs(_Entity_):
                                                """
                                                PBS in bytes
                                                
                                                .. attribute:: value
                                                
                                                	Config value
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: unit
                                                
                                                	Config unit
                                                	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs, self).__init__()

                                                    self.yang_name = "pbs"
                                                    self.yang_parent_name = "shape"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                        ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                                    ])
                                                    self.value = None
                                                    self.unit = None
                                                    self._segment_path = lambda: "pbs"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs, ['value', 'unit'], name, value)

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs']['meta_info']

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Shape']['meta_info']


                                        class Wfq(_Entity_):
                                            """
                                            QoS WFQ parameters
                                            
                                            .. attribute:: committed_weight
                                            
                                            	Committed Weight
                                            	**type**\:  :py:class:`CommittedWeight <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: programmed_wfq
                                            
                                            	QoS Programmed WFQ parameters
                                            	**type**\:  :py:class:`ProgrammedWfq <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: excess_weight
                                            
                                            	Excess Weight
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq, self).__init__()

                                                self.yang_name = "wfq"
                                                self.yang_parent_name = "qos-show-pclass-st"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("committed-weight", ("committed_weight", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight)), ("programmed-wfq", ("programmed_wfq", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq))])
                                                self._leafs = OrderedDict([
                                                    ('excess_weight', (YLeaf(YType.uint16, 'excess-weight'), ['int'])),
                                                ])
                                                self.excess_weight = None

                                                self.committed_weight = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight()
                                                self.committed_weight.parent = self
                                                self._children_name_map["committed_weight"] = "committed-weight"

                                                self.programmed_wfq = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq()
                                                self.programmed_wfq.parent = self
                                                self._children_name_map["programmed_wfq"] = "programmed-wfq"
                                                self._segment_path = lambda: "wfq"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq, ['excess_weight'], name, value)


                                            class CommittedWeight(_Entity_):
                                                """
                                                Committed Weight
                                                
                                                .. attribute:: value
                                                
                                                	Config value
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: unit
                                                
                                                	Config unit
                                                	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight, self).__init__()

                                                    self.yang_name = "committed-weight"
                                                    self.yang_parent_name = "wfq"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                        ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                                    ])
                                                    self.value = None
                                                    self.unit = None
                                                    self._segment_path = lambda: "committed-weight"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight, ['value', 'unit'], name, value)

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight']['meta_info']


                                            class ProgrammedWfq(_Entity_):
                                                """
                                                QoS Programmed WFQ parameters
                                                
                                                .. attribute:: bandwidth
                                                
                                                	Bandwidth
                                                	**type**\:  :py:class:`Bandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: sum_of_bandwidth
                                                
                                                	Sum of Bandwidth
                                                	**type**\:  :py:class:`SumOfBandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: excess_ratio
                                                
                                                	Excess Ratio
                                                	**type**\: int
                                                
                                                	**range:** 0..65535
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq, self).__init__()

                                                    self.yang_name = "programmed-wfq"
                                                    self.yang_parent_name = "wfq"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("bandwidth", ("bandwidth", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth)), ("sum-of-bandwidth", ("sum_of_bandwidth", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth))])
                                                    self._leafs = OrderedDict([
                                                        ('excess_ratio', (YLeaf(YType.uint16, 'excess-ratio'), ['int'])),
                                                    ])
                                                    self.excess_ratio = None

                                                    self.bandwidth = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth()
                                                    self.bandwidth.parent = self
                                                    self._children_name_map["bandwidth"] = "bandwidth"

                                                    self.sum_of_bandwidth = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth()
                                                    self.sum_of_bandwidth.parent = self
                                                    self._children_name_map["sum_of_bandwidth"] = "sum-of-bandwidth"
                                                    self._segment_path = lambda: "programmed-wfq"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq, ['excess_ratio'], name, value)


                                                class Bandwidth(_Entity_):
                                                    """
                                                    Bandwidth
                                                    
                                                    .. attribute:: value
                                                    
                                                    	Config value
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: unit
                                                    
                                                    	Config unit
                                                    	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                                    
                                                    	**config**\: False
                                                    
                                                    

                                                    """

                                                    _prefix = 'skp-qos-oper'
                                                    _revision = '2016-02-18'

                                                    def __init__(self):
                                                        if sys.version_info > (3,):
                                                            super().__init__()
                                                        else:
                                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth, self).__init__()

                                                        self.yang_name = "bandwidth"
                                                        self.yang_parent_name = "programmed-wfq"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                            ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                                        ])
                                                        self.value = None
                                                        self.unit = None
                                                        self._segment_path = lambda: "bandwidth"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth, ['value', 'unit'], name, value)

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth']['meta_info']


                                                class SumOfBandwidth(_Entity_):
                                                    """
                                                    Sum of Bandwidth
                                                    
                                                    .. attribute:: value
                                                    
                                                    	Config value
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: unit
                                                    
                                                    	Config unit
                                                    	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                                    
                                                    	**config**\: False
                                                    
                                                    

                                                    """

                                                    _prefix = 'skp-qos-oper'
                                                    _revision = '2016-02-18'

                                                    def __init__(self):
                                                        if sys.version_info > (3,):
                                                            super().__init__()
                                                        else:
                                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth, self).__init__()

                                                        self.yang_name = "sum-of-bandwidth"
                                                        self.yang_parent_name = "programmed-wfq"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                            ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                                        ])
                                                        self.value = None
                                                        self.unit = None
                                                        self._segment_path = lambda: "sum-of-bandwidth"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth, ['value', 'unit'], name, value)

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth']['meta_info']

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq']['meta_info']

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq']['meta_info']


                                        class Police(_Entity_):
                                            """
                                            QoS Policer parameters
                                            
                                            .. attribute:: cir
                                            
                                            	CIR
                                            	**type**\:  :py:class:`Cir <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: cbs
                                            
                                            	CBS
                                            	**type**\:  :py:class:`Cbs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: policer_id
                                            
                                            	policer ID
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: policer_type
                                            
                                            	Policer type
                                            	**type**\:  :py:class:`TbAlgorithm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.TbAlgorithm>`
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Police, self).__init__()

                                                self.yang_name = "police"
                                                self.yang_parent_name = "qos-show-pclass-st"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("cir", ("cir", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir)), ("cbs", ("cbs", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs))])
                                                self._leafs = OrderedDict([
                                                    ('policer_id', (YLeaf(YType.uint32, 'policer-id'), ['int'])),
                                                    ('policer_type', (YLeaf(YType.enumeration, 'policer-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'TbAlgorithm', '')])),
                                                ])
                                                self.policer_id = None
                                                self.policer_type = None

                                                self.cir = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir()
                                                self.cir.parent = self
                                                self._children_name_map["cir"] = "cir"

                                                self.cbs = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs()
                                                self.cbs.parent = self
                                                self._children_name_map["cbs"] = "cbs"
                                                self._segment_path = lambda: "police"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Police, ['policer_id', 'policer_type'], name, value)


                                            class Cir(_Entity_):
                                                """
                                                CIR
                                                
                                                .. attribute:: value
                                                
                                                	Config value
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: unit
                                                
                                                	Config unit
                                                	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir, self).__init__()

                                                    self.yang_name = "cir"
                                                    self.yang_parent_name = "police"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                        ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                                    ])
                                                    self.value = None
                                                    self.unit = None
                                                    self._segment_path = lambda: "cir"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir, ['value', 'unit'], name, value)

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir']['meta_info']


                                            class Cbs(_Entity_):
                                                """
                                                CBS
                                                
                                                .. attribute:: value
                                                
                                                	Config value
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: unit
                                                
                                                	Config unit
                                                	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs, self).__init__()

                                                    self.yang_name = "cbs"
                                                    self.yang_parent_name = "police"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                        ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                                    ])
                                                    self.value = None
                                                    self.unit = None
                                                    self._segment_path = lambda: "cbs"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs, ['value', 'unit'], name, value)

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs']['meta_info']

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Police']['meta_info']


                                        class Marking(_Entity_):
                                            """
                                            QoS Mark parameters
                                            
                                            .. attribute:: mark_only
                                            
                                            	Mark Only
                                            	**type**\:  :py:class:`MarkOnly <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: police_conform
                                            
                                            	Police conform mark
                                            	**type**\:  :py:class:`PoliceConform <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: police_exceed
                                            
                                            	Police exceed mark
                                            	**type**\:  :py:class:`PoliceExceed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed>`
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking, self).__init__()

                                                self.yang_name = "marking"
                                                self.yang_parent_name = "qos-show-pclass-st"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("mark-only", ("mark_only", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly)), ("police-conform", ("police_conform", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform)), ("police-exceed", ("police_exceed", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed))])
                                                self._leafs = OrderedDict()

                                                self.mark_only = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly()
                                                self.mark_only.parent = self
                                                self._children_name_map["mark_only"] = "mark-only"

                                                self.police_conform = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform()
                                                self.police_conform.parent = self
                                                self._children_name_map["police_conform"] = "police-conform"

                                                self.police_exceed = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed()
                                                self.police_exceed.parent = self
                                                self._children_name_map["police_exceed"] = "police-exceed"
                                                self._segment_path = lambda: "marking"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking, [], name, value)


                                            class MarkOnly(_Entity_):
                                                """
                                                Mark Only
                                                
                                                .. attribute:: action_type
                                                
                                                	Action type
                                                	**type**\:  :py:class:`Action <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.Action>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: mark_detail
                                                
                                                	Mark value
                                                	**type**\: list of  		 :py:class:`MarkDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly.MarkDetail>`
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly, self).__init__()

                                                    self.yang_name = "mark-only"
                                                    self.yang_parent_name = "marking"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("mark-detail", ("mark_detail", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly.MarkDetail))])
                                                    self._leafs = OrderedDict([
                                                        ('action_type', (YLeaf(YType.enumeration, 'action-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'Action', '')])),
                                                    ])
                                                    self.action_type = None

                                                    self.mark_detail = YList(self)
                                                    self._segment_path = lambda: "mark-only"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly, ['action_type'], name, value)


                                                class MarkDetail(_Entity_):
                                                    """
                                                    Mark value
                                                    
                                                    .. attribute:: mark_value
                                                    
                                                    	Mark value
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..255
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: action_opcode
                                                    
                                                    	Action opcode
                                                    	**type**\:  :py:class:`ActionOpcode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.ActionOpcode>`
                                                    
                                                    	**config**\: False
                                                    
                                                    

                                                    """

                                                    _prefix = 'skp-qos-oper'
                                                    _revision = '2016-02-18'

                                                    def __init__(self):
                                                        if sys.version_info > (3,):
                                                            super().__init__()
                                                        else:
                                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly.MarkDetail, self).__init__()

                                                        self.yang_name = "mark-detail"
                                                        self.yang_parent_name = "mark-only"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('mark_value', (YLeaf(YType.uint8, 'mark-value'), ['int'])),
                                                            ('action_opcode', (YLeaf(YType.enumeration, 'action-opcode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'ActionOpcode', '')])),
                                                        ])
                                                        self.mark_value = None
                                                        self.action_opcode = None
                                                        self._segment_path = lambda: "mark-detail"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly.MarkDetail, ['mark_value', 'action_opcode'], name, value)

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly.MarkDetail']['meta_info']

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly']['meta_info']


                                            class PoliceConform(_Entity_):
                                                """
                                                Police conform mark
                                                
                                                .. attribute:: action_type
                                                
                                                	Action type
                                                	**type**\:  :py:class:`Action <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.Action>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: mark_detail
                                                
                                                	Mark value
                                                	**type**\: list of  		 :py:class:`MarkDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform.MarkDetail>`
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform, self).__init__()

                                                    self.yang_name = "police-conform"
                                                    self.yang_parent_name = "marking"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("mark-detail", ("mark_detail", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform.MarkDetail))])
                                                    self._leafs = OrderedDict([
                                                        ('action_type', (YLeaf(YType.enumeration, 'action-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'Action', '')])),
                                                    ])
                                                    self.action_type = None

                                                    self.mark_detail = YList(self)
                                                    self._segment_path = lambda: "police-conform"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform, ['action_type'], name, value)


                                                class MarkDetail(_Entity_):
                                                    """
                                                    Mark value
                                                    
                                                    .. attribute:: mark_value
                                                    
                                                    	Mark value
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..255
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: action_opcode
                                                    
                                                    	Action opcode
                                                    	**type**\:  :py:class:`ActionOpcode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.ActionOpcode>`
                                                    
                                                    	**config**\: False
                                                    
                                                    

                                                    """

                                                    _prefix = 'skp-qos-oper'
                                                    _revision = '2016-02-18'

                                                    def __init__(self):
                                                        if sys.version_info > (3,):
                                                            super().__init__()
                                                        else:
                                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform.MarkDetail, self).__init__()

                                                        self.yang_name = "mark-detail"
                                                        self.yang_parent_name = "police-conform"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('mark_value', (YLeaf(YType.uint8, 'mark-value'), ['int'])),
                                                            ('action_opcode', (YLeaf(YType.enumeration, 'action-opcode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'ActionOpcode', '')])),
                                                        ])
                                                        self.mark_value = None
                                                        self.action_opcode = None
                                                        self._segment_path = lambda: "mark-detail"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform.MarkDetail, ['mark_value', 'action_opcode'], name, value)

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform.MarkDetail']['meta_info']

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform']['meta_info']


                                            class PoliceExceed(_Entity_):
                                                """
                                                Police exceed mark
                                                
                                                .. attribute:: action_type
                                                
                                                	Action type
                                                	**type**\:  :py:class:`Action <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.Action>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: mark_detail
                                                
                                                	Mark value
                                                	**type**\: list of  		 :py:class:`MarkDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed.MarkDetail>`
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed, self).__init__()

                                                    self.yang_name = "police-exceed"
                                                    self.yang_parent_name = "marking"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("mark-detail", ("mark_detail", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed.MarkDetail))])
                                                    self._leafs = OrderedDict([
                                                        ('action_type', (YLeaf(YType.enumeration, 'action-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'Action', '')])),
                                                    ])
                                                    self.action_type = None

                                                    self.mark_detail = YList(self)
                                                    self._segment_path = lambda: "police-exceed"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed, ['action_type'], name, value)


                                                class MarkDetail(_Entity_):
                                                    """
                                                    Mark value
                                                    
                                                    .. attribute:: mark_value
                                                    
                                                    	Mark value
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..255
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: action_opcode
                                                    
                                                    	Action opcode
                                                    	**type**\:  :py:class:`ActionOpcode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.ActionOpcode>`
                                                    
                                                    	**config**\: False
                                                    
                                                    

                                                    """

                                                    _prefix = 'skp-qos-oper'
                                                    _revision = '2016-02-18'

                                                    def __init__(self):
                                                        if sys.version_info > (3,):
                                                            super().__init__()
                                                        else:
                                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed.MarkDetail, self).__init__()

                                                        self.yang_name = "mark-detail"
                                                        self.yang_parent_name = "police-exceed"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('mark_value', (YLeaf(YType.uint8, 'mark-value'), ['int'])),
                                                            ('action_opcode', (YLeaf(YType.enumeration, 'action-opcode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'ActionOpcode', '')])),
                                                        ])
                                                        self.mark_value = None
                                                        self.action_opcode = None
                                                        self._segment_path = lambda: "mark-detail"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed.MarkDetail, ['mark_value', 'action_opcode'], name, value)

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed.MarkDetail']['meta_info']

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed']['meta_info']

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt.Marking']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass.QosShowPclassSt']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.SkywarpQosPolicyClass']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput']['meta_info']


                            class BundleOutput(_Entity_):
                                """
                                QoS policy direction output
                                
                                .. attribute:: header
                                
                                	QoS EA policy header
                                	**type**\:  :py:class:`Header <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Header>`
                                
                                	**config**\: False
                                
                                .. attribute:: interface_parameters
                                
                                	QoS Interface Parameters
                                	**type**\:  :py:class:`InterfaceParameters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters>`
                                
                                	**config**\: False
                                
                                .. attribute:: skywarp_qos_policy_class
                                
                                	Skywarp QoS policy class details
                                	**type**\:  :py:class:`SkywarpQosPolicyClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'skp-qos-oper'
                                _revision = '2016-02-18'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput, self).__init__()

                                    self.yang_name = "bundle-output"
                                    self.yang_parent_name = "member-interface"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("header", ("header", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Header)), ("interface-parameters", ("interface_parameters", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters)), ("skywarp-qos-policy-class", ("skywarp_qos_policy_class", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass))])
                                    self._leafs = OrderedDict()

                                    self.header = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Header()
                                    self.header.parent = self
                                    self._children_name_map["header"] = "header"

                                    self.interface_parameters = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters()
                                    self.interface_parameters.parent = self
                                    self._children_name_map["interface_parameters"] = "interface-parameters"

                                    self.skywarp_qos_policy_class = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass()
                                    self.skywarp_qos_policy_class.parent = self
                                    self._children_name_map["skywarp_qos_policy_class"] = "skywarp-qos-policy-class"
                                    self._segment_path = lambda: "bundle-output"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput, [], name, value)


                                class Header(_Entity_):
                                    """
                                    QoS EA policy header
                                    
                                    .. attribute:: interface_name
                                    
                                    	Interface Name
                                    	**type**\: str
                                    
                                    	**length:** 0..101
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: policy_name
                                    
                                    	Policy name
                                    	**type**\: str
                                    
                                    	**length:** 0..65
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: direction
                                    
                                    	Direction
                                    	**type**\: str
                                    
                                    	**length:** 0..11
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: classes
                                    
                                    	Number of classes
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'skp-qos-oper'
                                    _revision = '2016-02-18'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Header, self).__init__()

                                        self.yang_name = "header"
                                        self.yang_parent_name = "bundle-output"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                            ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                            ('direction', (YLeaf(YType.str, 'direction'), ['str'])),
                                            ('classes', (YLeaf(YType.uint16, 'classes'), ['int'])),
                                        ])
                                        self.interface_name = None
                                        self.policy_name = None
                                        self.direction = None
                                        self.classes = None
                                        self._segment_path = lambda: "header"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Header, ['interface_name', 'policy_name', 'direction', 'classes'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Header']['meta_info']


                                class InterfaceParameters(_Entity_):
                                    """
                                    QoS Interface Parameters
                                    
                                    .. attribute:: interface_config_rate
                                    
                                    	Interface Configured Rate
                                    	**type**\:  :py:class:`InterfaceConfigRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters.InterfaceConfigRate>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: interface_program_rate
                                    
                                    	Interface Programmed Rate
                                    	**type**\:  :py:class:`InterfaceProgramRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters.InterfaceProgramRate>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: port_shaper_rate
                                    
                                    	Port Shaper Rate
                                    	**type**\:  :py:class:`PortShaperRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters.PortShaperRate>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'skp-qos-oper'
                                    _revision = '2016-02-18'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters, self).__init__()

                                        self.yang_name = "interface-parameters"
                                        self.yang_parent_name = "bundle-output"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("interface-config-rate", ("interface_config_rate", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters.InterfaceConfigRate)), ("interface-program-rate", ("interface_program_rate", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters.InterfaceProgramRate)), ("port-shaper-rate", ("port_shaper_rate", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters.PortShaperRate))])
                                        self._leafs = OrderedDict()

                                        self.interface_config_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters.InterfaceConfigRate()
                                        self.interface_config_rate.parent = self
                                        self._children_name_map["interface_config_rate"] = "interface-config-rate"

                                        self.interface_program_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters.InterfaceProgramRate()
                                        self.interface_program_rate.parent = self
                                        self._children_name_map["interface_program_rate"] = "interface-program-rate"

                                        self.port_shaper_rate = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters.PortShaperRate()
                                        self.port_shaper_rate.parent = self
                                        self._children_name_map["port_shaper_rate"] = "port-shaper-rate"
                                        self._segment_path = lambda: "interface-parameters"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters, [], name, value)


                                    class InterfaceConfigRate(_Entity_):
                                        """
                                        Interface Configured Rate
                                        
                                        .. attribute:: value
                                        
                                        	Config value
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: unit
                                        
                                        	Config unit
                                        	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters.InterfaceConfigRate, self).__init__()

                                            self.yang_name = "interface-config-rate"
                                            self.yang_parent_name = "interface-parameters"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                            ])
                                            self.value = None
                                            self.unit = None
                                            self._segment_path = lambda: "interface-config-rate"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters.InterfaceConfigRate, ['value', 'unit'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters.InterfaceConfigRate']['meta_info']


                                    class InterfaceProgramRate(_Entity_):
                                        """
                                        Interface Programmed Rate
                                        
                                        .. attribute:: value
                                        
                                        	Config value
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: unit
                                        
                                        	Config unit
                                        	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters.InterfaceProgramRate, self).__init__()

                                            self.yang_name = "interface-program-rate"
                                            self.yang_parent_name = "interface-parameters"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                            ])
                                            self.value = None
                                            self.unit = None
                                            self._segment_path = lambda: "interface-program-rate"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters.InterfaceProgramRate, ['value', 'unit'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters.InterfaceProgramRate']['meta_info']


                                    class PortShaperRate(_Entity_):
                                        """
                                        Port Shaper Rate
                                        
                                        .. attribute:: value
                                        
                                        	Config value
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: unit
                                        
                                        	Config unit
                                        	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters.PortShaperRate, self).__init__()

                                            self.yang_name = "port-shaper-rate"
                                            self.yang_parent_name = "interface-parameters"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                            ])
                                            self.value = None
                                            self.unit = None
                                            self._segment_path = lambda: "port-shaper-rate"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters.PortShaperRate, ['value', 'unit'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters.PortShaperRate']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.InterfaceParameters']['meta_info']


                                class SkywarpQosPolicyClass(_Entity_):
                                    """
                                    Skywarp QoS policy class details
                                    
                                    .. attribute:: qos_show_pclass_st
                                    
                                    	qos show pclass st
                                    	**type**\: list of  		 :py:class:`QosShowPclassSt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'skp-qos-oper'
                                    _revision = '2016-02-18'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass, self).__init__()

                                        self.yang_name = "skywarp-qos-policy-class"
                                        self.yang_parent_name = "bundle-output"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("qos-show-pclass-st", ("qos_show_pclass_st", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt))])
                                        self._leafs = OrderedDict()

                                        self.qos_show_pclass_st = YList(self)
                                        self._segment_path = lambda: "skywarp-qos-policy-class"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass, [], name, value)


                                    class QosShowPclassSt(_Entity_):
                                        """
                                        qos show pclass st
                                        
                                        .. attribute:: queue
                                        
                                        	QoS Queue parameters
                                        	**type**\:  :py:class:`Queue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Queue>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: shape
                                        
                                        	QoS EA Shaper parameters
                                        	**type**\:  :py:class:`Shape <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Shape>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: wfq
                                        
                                        	QoS WFQ parameters
                                        	**type**\:  :py:class:`Wfq <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: police
                                        
                                        	QoS Policer parameters
                                        	**type**\:  :py:class:`Police <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Police>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: marking
                                        
                                        	QoS Mark parameters
                                        	**type**\:  :py:class:`Marking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: class_level
                                        
                                        	Class level
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: class_name
                                        
                                        	Class name
                                        	**type**\: str
                                        
                                        	**length:** 0..65
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt, self).__init__()

                                            self.yang_name = "qos-show-pclass-st"
                                            self.yang_parent_name = "skywarp-qos-policy-class"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("queue", ("queue", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Queue)), ("shape", ("shape", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Shape)), ("wfq", ("wfq", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq)), ("police", ("police", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Police)), ("marking", ("marking", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking))])
                                            self._leafs = OrderedDict([
                                                ('class_level', (YLeaf(YType.uint8, 'class-level'), ['int'])),
                                                ('class_name', (YLeaf(YType.str, 'class-name'), ['str'])),
                                            ])
                                            self.class_level = None
                                            self.class_name = None

                                            self.queue = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Queue()
                                            self.queue.parent = self
                                            self._children_name_map["queue"] = "queue"

                                            self.shape = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Shape()
                                            self.shape.parent = self
                                            self._children_name_map["shape"] = "shape"

                                            self.wfq = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq()
                                            self.wfq.parent = self
                                            self._children_name_map["wfq"] = "wfq"

                                            self.police = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Police()
                                            self.police.parent = self
                                            self._children_name_map["police"] = "police"

                                            self.marking = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking()
                                            self.marking.parent = self
                                            self._children_name_map["marking"] = "marking"
                                            self._segment_path = lambda: "qos-show-pclass-st"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt, ['class_level', 'class_name'], name, value)


                                        class Queue(_Entity_):
                                            """
                                            QoS Queue parameters
                                            
                                            .. attribute:: queue_id
                                            
                                            	Queue ID
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: queue_type
                                            
                                            	Queue Type
                                            	**type**\: str
                                            
                                            	**length:** 0..101
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Queue, self).__init__()

                                                self.yang_name = "queue"
                                                self.yang_parent_name = "qos-show-pclass-st"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('queue_id', (YLeaf(YType.uint32, 'queue-id'), ['int'])),
                                                    ('queue_type', (YLeaf(YType.str, 'queue-type'), ['str'])),
                                                ])
                                                self.queue_id = None
                                                self.queue_type = None
                                                self._segment_path = lambda: "queue"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Queue, ['queue_id', 'queue_type'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Queue']['meta_info']


                                        class Shape(_Entity_):
                                            """
                                            QoS EA Shaper parameters
                                            
                                            .. attribute:: pir
                                            
                                            	PIR in kbps
                                            	**type**\:  :py:class:`Pir <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: pbs
                                            
                                            	PBS in bytes
                                            	**type**\:  :py:class:`Pbs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs>`
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Shape, self).__init__()

                                                self.yang_name = "shape"
                                                self.yang_parent_name = "qos-show-pclass-st"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("pir", ("pir", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir)), ("pbs", ("pbs", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs))])
                                                self._leafs = OrderedDict()

                                                self.pir = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir()
                                                self.pir.parent = self
                                                self._children_name_map["pir"] = "pir"

                                                self.pbs = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs()
                                                self.pbs.parent = self
                                                self._children_name_map["pbs"] = "pbs"
                                                self._segment_path = lambda: "shape"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Shape, [], name, value)


                                            class Pir(_Entity_):
                                                """
                                                PIR in kbps
                                                
                                                .. attribute:: value
                                                
                                                	Config value
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: unit
                                                
                                                	Config unit
                                                	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir, self).__init__()

                                                    self.yang_name = "pir"
                                                    self.yang_parent_name = "shape"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                        ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                                    ])
                                                    self.value = None
                                                    self.unit = None
                                                    self._segment_path = lambda: "pir"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir, ['value', 'unit'], name, value)

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir']['meta_info']


                                            class Pbs(_Entity_):
                                                """
                                                PBS in bytes
                                                
                                                .. attribute:: value
                                                
                                                	Config value
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: unit
                                                
                                                	Config unit
                                                	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs, self).__init__()

                                                    self.yang_name = "pbs"
                                                    self.yang_parent_name = "shape"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                        ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                                    ])
                                                    self.value = None
                                                    self.unit = None
                                                    self._segment_path = lambda: "pbs"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs, ['value', 'unit'], name, value)

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs']['meta_info']

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Shape']['meta_info']


                                        class Wfq(_Entity_):
                                            """
                                            QoS WFQ parameters
                                            
                                            .. attribute:: committed_weight
                                            
                                            	Committed Weight
                                            	**type**\:  :py:class:`CommittedWeight <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: programmed_wfq
                                            
                                            	QoS Programmed WFQ parameters
                                            	**type**\:  :py:class:`ProgrammedWfq <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: excess_weight
                                            
                                            	Excess Weight
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq, self).__init__()

                                                self.yang_name = "wfq"
                                                self.yang_parent_name = "qos-show-pclass-st"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("committed-weight", ("committed_weight", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight)), ("programmed-wfq", ("programmed_wfq", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq))])
                                                self._leafs = OrderedDict([
                                                    ('excess_weight', (YLeaf(YType.uint16, 'excess-weight'), ['int'])),
                                                ])
                                                self.excess_weight = None

                                                self.committed_weight = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight()
                                                self.committed_weight.parent = self
                                                self._children_name_map["committed_weight"] = "committed-weight"

                                                self.programmed_wfq = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq()
                                                self.programmed_wfq.parent = self
                                                self._children_name_map["programmed_wfq"] = "programmed-wfq"
                                                self._segment_path = lambda: "wfq"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq, ['excess_weight'], name, value)


                                            class CommittedWeight(_Entity_):
                                                """
                                                Committed Weight
                                                
                                                .. attribute:: value
                                                
                                                	Config value
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: unit
                                                
                                                	Config unit
                                                	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight, self).__init__()

                                                    self.yang_name = "committed-weight"
                                                    self.yang_parent_name = "wfq"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                        ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                                    ])
                                                    self.value = None
                                                    self.unit = None
                                                    self._segment_path = lambda: "committed-weight"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight, ['value', 'unit'], name, value)

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight']['meta_info']


                                            class ProgrammedWfq(_Entity_):
                                                """
                                                QoS Programmed WFQ parameters
                                                
                                                .. attribute:: bandwidth
                                                
                                                	Bandwidth
                                                	**type**\:  :py:class:`Bandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: sum_of_bandwidth
                                                
                                                	Sum of Bandwidth
                                                	**type**\:  :py:class:`SumOfBandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: excess_ratio
                                                
                                                	Excess Ratio
                                                	**type**\: int
                                                
                                                	**range:** 0..65535
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq, self).__init__()

                                                    self.yang_name = "programmed-wfq"
                                                    self.yang_parent_name = "wfq"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("bandwidth", ("bandwidth", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth)), ("sum-of-bandwidth", ("sum_of_bandwidth", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth))])
                                                    self._leafs = OrderedDict([
                                                        ('excess_ratio', (YLeaf(YType.uint16, 'excess-ratio'), ['int'])),
                                                    ])
                                                    self.excess_ratio = None

                                                    self.bandwidth = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth()
                                                    self.bandwidth.parent = self
                                                    self._children_name_map["bandwidth"] = "bandwidth"

                                                    self.sum_of_bandwidth = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth()
                                                    self.sum_of_bandwidth.parent = self
                                                    self._children_name_map["sum_of_bandwidth"] = "sum-of-bandwidth"
                                                    self._segment_path = lambda: "programmed-wfq"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq, ['excess_ratio'], name, value)


                                                class Bandwidth(_Entity_):
                                                    """
                                                    Bandwidth
                                                    
                                                    .. attribute:: value
                                                    
                                                    	Config value
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: unit
                                                    
                                                    	Config unit
                                                    	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                                    
                                                    	**config**\: False
                                                    
                                                    

                                                    """

                                                    _prefix = 'skp-qos-oper'
                                                    _revision = '2016-02-18'

                                                    def __init__(self):
                                                        if sys.version_info > (3,):
                                                            super().__init__()
                                                        else:
                                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth, self).__init__()

                                                        self.yang_name = "bandwidth"
                                                        self.yang_parent_name = "programmed-wfq"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                            ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                                        ])
                                                        self.value = None
                                                        self.unit = None
                                                        self._segment_path = lambda: "bandwidth"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth, ['value', 'unit'], name, value)

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth']['meta_info']


                                                class SumOfBandwidth(_Entity_):
                                                    """
                                                    Sum of Bandwidth
                                                    
                                                    .. attribute:: value
                                                    
                                                    	Config value
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: unit
                                                    
                                                    	Config unit
                                                    	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                                    
                                                    	**config**\: False
                                                    
                                                    

                                                    """

                                                    _prefix = 'skp-qos-oper'
                                                    _revision = '2016-02-18'

                                                    def __init__(self):
                                                        if sys.version_info > (3,):
                                                            super().__init__()
                                                        else:
                                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth, self).__init__()

                                                        self.yang_name = "sum-of-bandwidth"
                                                        self.yang_parent_name = "programmed-wfq"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                            ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                                        ])
                                                        self.value = None
                                                        self.unit = None
                                                        self._segment_path = lambda: "sum-of-bandwidth"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth, ['value', 'unit'], name, value)

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth']['meta_info']

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq']['meta_info']

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Wfq']['meta_info']


                                        class Police(_Entity_):
                                            """
                                            QoS Policer parameters
                                            
                                            .. attribute:: cir
                                            
                                            	CIR
                                            	**type**\:  :py:class:`Cir <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: cbs
                                            
                                            	CBS
                                            	**type**\:  :py:class:`Cbs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: policer_id
                                            
                                            	policer ID
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: policer_type
                                            
                                            	Policer type
                                            	**type**\:  :py:class:`TbAlgorithm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.TbAlgorithm>`
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Police, self).__init__()

                                                self.yang_name = "police"
                                                self.yang_parent_name = "qos-show-pclass-st"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("cir", ("cir", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir)), ("cbs", ("cbs", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs))])
                                                self._leafs = OrderedDict([
                                                    ('policer_id', (YLeaf(YType.uint32, 'policer-id'), ['int'])),
                                                    ('policer_type', (YLeaf(YType.enumeration, 'policer-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'TbAlgorithm', '')])),
                                                ])
                                                self.policer_id = None
                                                self.policer_type = None

                                                self.cir = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir()
                                                self.cir.parent = self
                                                self._children_name_map["cir"] = "cir"

                                                self.cbs = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs()
                                                self.cbs.parent = self
                                                self._children_name_map["cbs"] = "cbs"
                                                self._segment_path = lambda: "police"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Police, ['policer_id', 'policer_type'], name, value)


                                            class Cir(_Entity_):
                                                """
                                                CIR
                                                
                                                .. attribute:: value
                                                
                                                	Config value
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: unit
                                                
                                                	Config unit
                                                	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir, self).__init__()

                                                    self.yang_name = "cir"
                                                    self.yang_parent_name = "police"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                        ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                                    ])
                                                    self.value = None
                                                    self.unit = None
                                                    self._segment_path = lambda: "cir"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir, ['value', 'unit'], name, value)

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir']['meta_info']


                                            class Cbs(_Entity_):
                                                """
                                                CBS
                                                
                                                .. attribute:: value
                                                
                                                	Config value
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: unit
                                                
                                                	Config unit
                                                	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs, self).__init__()

                                                    self.yang_name = "cbs"
                                                    self.yang_parent_name = "police"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                        ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                                    ])
                                                    self.value = None
                                                    self.unit = None
                                                    self._segment_path = lambda: "cbs"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs, ['value', 'unit'], name, value)

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs']['meta_info']

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Police']['meta_info']


                                        class Marking(_Entity_):
                                            """
                                            QoS Mark parameters
                                            
                                            .. attribute:: mark_only
                                            
                                            	Mark Only
                                            	**type**\:  :py:class:`MarkOnly <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: police_conform
                                            
                                            	Police conform mark
                                            	**type**\:  :py:class:`PoliceConform <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: police_exceed
                                            
                                            	Police exceed mark
                                            	**type**\:  :py:class:`PoliceExceed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed>`
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking, self).__init__()

                                                self.yang_name = "marking"
                                                self.yang_parent_name = "qos-show-pclass-st"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("mark-only", ("mark_only", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly)), ("police-conform", ("police_conform", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform)), ("police-exceed", ("police_exceed", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed))])
                                                self._leafs = OrderedDict()

                                                self.mark_only = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly()
                                                self.mark_only.parent = self
                                                self._children_name_map["mark_only"] = "mark-only"

                                                self.police_conform = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform()
                                                self.police_conform.parent = self
                                                self._children_name_map["police_conform"] = "police-conform"

                                                self.police_exceed = PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed()
                                                self.police_exceed.parent = self
                                                self._children_name_map["police_exceed"] = "police-exceed"
                                                self._segment_path = lambda: "marking"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking, [], name, value)


                                            class MarkOnly(_Entity_):
                                                """
                                                Mark Only
                                                
                                                .. attribute:: action_type
                                                
                                                	Action type
                                                	**type**\:  :py:class:`Action <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.Action>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: mark_detail
                                                
                                                	Mark value
                                                	**type**\: list of  		 :py:class:`MarkDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly.MarkDetail>`
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly, self).__init__()

                                                    self.yang_name = "mark-only"
                                                    self.yang_parent_name = "marking"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("mark-detail", ("mark_detail", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly.MarkDetail))])
                                                    self._leafs = OrderedDict([
                                                        ('action_type', (YLeaf(YType.enumeration, 'action-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'Action', '')])),
                                                    ])
                                                    self.action_type = None

                                                    self.mark_detail = YList(self)
                                                    self._segment_path = lambda: "mark-only"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly, ['action_type'], name, value)


                                                class MarkDetail(_Entity_):
                                                    """
                                                    Mark value
                                                    
                                                    .. attribute:: mark_value
                                                    
                                                    	Mark value
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..255
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: action_opcode
                                                    
                                                    	Action opcode
                                                    	**type**\:  :py:class:`ActionOpcode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.ActionOpcode>`
                                                    
                                                    	**config**\: False
                                                    
                                                    

                                                    """

                                                    _prefix = 'skp-qos-oper'
                                                    _revision = '2016-02-18'

                                                    def __init__(self):
                                                        if sys.version_info > (3,):
                                                            super().__init__()
                                                        else:
                                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly.MarkDetail, self).__init__()

                                                        self.yang_name = "mark-detail"
                                                        self.yang_parent_name = "mark-only"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('mark_value', (YLeaf(YType.uint8, 'mark-value'), ['int'])),
                                                            ('action_opcode', (YLeaf(YType.enumeration, 'action-opcode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'ActionOpcode', '')])),
                                                        ])
                                                        self.mark_value = None
                                                        self.action_opcode = None
                                                        self._segment_path = lambda: "mark-detail"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly.MarkDetail, ['mark_value', 'action_opcode'], name, value)

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly.MarkDetail']['meta_info']

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly']['meta_info']


                                            class PoliceConform(_Entity_):
                                                """
                                                Police conform mark
                                                
                                                .. attribute:: action_type
                                                
                                                	Action type
                                                	**type**\:  :py:class:`Action <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.Action>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: mark_detail
                                                
                                                	Mark value
                                                	**type**\: list of  		 :py:class:`MarkDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform.MarkDetail>`
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform, self).__init__()

                                                    self.yang_name = "police-conform"
                                                    self.yang_parent_name = "marking"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("mark-detail", ("mark_detail", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform.MarkDetail))])
                                                    self._leafs = OrderedDict([
                                                        ('action_type', (YLeaf(YType.enumeration, 'action-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'Action', '')])),
                                                    ])
                                                    self.action_type = None

                                                    self.mark_detail = YList(self)
                                                    self._segment_path = lambda: "police-conform"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform, ['action_type'], name, value)


                                                class MarkDetail(_Entity_):
                                                    """
                                                    Mark value
                                                    
                                                    .. attribute:: mark_value
                                                    
                                                    	Mark value
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..255
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: action_opcode
                                                    
                                                    	Action opcode
                                                    	**type**\:  :py:class:`ActionOpcode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.ActionOpcode>`
                                                    
                                                    	**config**\: False
                                                    
                                                    

                                                    """

                                                    _prefix = 'skp-qos-oper'
                                                    _revision = '2016-02-18'

                                                    def __init__(self):
                                                        if sys.version_info > (3,):
                                                            super().__init__()
                                                        else:
                                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform.MarkDetail, self).__init__()

                                                        self.yang_name = "mark-detail"
                                                        self.yang_parent_name = "police-conform"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('mark_value', (YLeaf(YType.uint8, 'mark-value'), ['int'])),
                                                            ('action_opcode', (YLeaf(YType.enumeration, 'action-opcode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'ActionOpcode', '')])),
                                                        ])
                                                        self.mark_value = None
                                                        self.action_opcode = None
                                                        self._segment_path = lambda: "mark-detail"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform.MarkDetail, ['mark_value', 'action_opcode'], name, value)

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform.MarkDetail']['meta_info']

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform']['meta_info']


                                            class PoliceExceed(_Entity_):
                                                """
                                                Police exceed mark
                                                
                                                .. attribute:: action_type
                                                
                                                	Action type
                                                	**type**\:  :py:class:`Action <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.Action>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: mark_detail
                                                
                                                	Mark value
                                                	**type**\: list of  		 :py:class:`MarkDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed.MarkDetail>`
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed, self).__init__()

                                                    self.yang_name = "police-exceed"
                                                    self.yang_parent_name = "marking"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("mark-detail", ("mark_detail", PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed.MarkDetail))])
                                                    self._leafs = OrderedDict([
                                                        ('action_type', (YLeaf(YType.enumeration, 'action-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'Action', '')])),
                                                    ])
                                                    self.action_type = None

                                                    self.mark_detail = YList(self)
                                                    self._segment_path = lambda: "police-exceed"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed, ['action_type'], name, value)


                                                class MarkDetail(_Entity_):
                                                    """
                                                    Mark value
                                                    
                                                    .. attribute:: mark_value
                                                    
                                                    	Mark value
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..255
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: action_opcode
                                                    
                                                    	Action opcode
                                                    	**type**\:  :py:class:`ActionOpcode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.ActionOpcode>`
                                                    
                                                    	**config**\: False
                                                    
                                                    

                                                    """

                                                    _prefix = 'skp-qos-oper'
                                                    _revision = '2016-02-18'

                                                    def __init__(self):
                                                        if sys.version_info > (3,):
                                                            super().__init__()
                                                        else:
                                                            super(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed.MarkDetail, self).__init__()

                                                        self.yang_name = "mark-detail"
                                                        self.yang_parent_name = "police-exceed"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('mark_value', (YLeaf(YType.uint8, 'mark-value'), ['int'])),
                                                            ('action_opcode', (YLeaf(YType.enumeration, 'action-opcode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'ActionOpcode', '')])),
                                                        ])
                                                        self.mark_value = None
                                                        self.action_opcode = None
                                                        self._segment_path = lambda: "mark-detail"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed.MarkDetail, ['mark_value', 'action_opcode'], name, value)

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed.MarkDetail']['meta_info']

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed']['meta_info']

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt.Marking']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass.QosShowPclassSt']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.SkywarpQosPolicyClass']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                            return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                        return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                    return meta._meta_table['PlatformQos.Nodes.Node.BundleInterfaces']['meta_info']


            class Capability(_Entity_):
                """
                QoS system capability
                
                .. attribute:: max_policy_maps
                
                	Maximum policy maps per system
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: max_policy_hierarchy
                
                	Maximum policy hierarchy
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: max_policy_name_length
                
                	Maximum policy name length
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: max_classes_per_policy
                
                	Maximum classes per policy
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: max_police_actions_per_class
                
                	Maximum police actions per class
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: max_marking_actions_per_class
                
                	Maximum marking action  per class
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: max_matches_per_class
                
                	Maximum matches per class
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: max_classmap_name_length
                
                	Maximum classmap name length
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: max_bundle_members
                
                	Maximum bundle members
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'skp-qos-oper'
                _revision = '2016-02-18'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(PlatformQos.Nodes.Node.Capability, self).__init__()

                    self.yang_name = "capability"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('max_policy_maps', (YLeaf(YType.uint32, 'max-policy-maps'), ['int'])),
                        ('max_policy_hierarchy', (YLeaf(YType.uint32, 'max-policy-hierarchy'), ['int'])),
                        ('max_policy_name_length', (YLeaf(YType.uint32, 'max-policy-name-length'), ['int'])),
                        ('max_classes_per_policy', (YLeaf(YType.uint32, 'max-classes-per-policy'), ['int'])),
                        ('max_police_actions_per_class', (YLeaf(YType.uint32, 'max-police-actions-per-class'), ['int'])),
                        ('max_marking_actions_per_class', (YLeaf(YType.uint32, 'max-marking-actions-per-class'), ['int'])),
                        ('max_matches_per_class', (YLeaf(YType.uint32, 'max-matches-per-class'), ['int'])),
                        ('max_classmap_name_length', (YLeaf(YType.uint32, 'max-classmap-name-length'), ['int'])),
                        ('max_bundle_members', (YLeaf(YType.uint32, 'max-bundle-members'), ['int'])),
                    ])
                    self.max_policy_maps = None
                    self.max_policy_hierarchy = None
                    self.max_policy_name_length = None
                    self.max_classes_per_policy = None
                    self.max_police_actions_per_class = None
                    self.max_marking_actions_per_class = None
                    self.max_matches_per_class = None
                    self.max_classmap_name_length = None
                    self.max_bundle_members = None
                    self._segment_path = lambda: "capability"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PlatformQos.Nodes.Node.Capability, ['max_policy_maps', 'max_policy_hierarchy', 'max_policy_name_length', 'max_classes_per_policy', 'max_police_actions_per_class', 'max_marking_actions_per_class', 'max_matches_per_class', 'max_classmap_name_length', 'max_bundle_members'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                    return meta._meta_table['PlatformQos.Nodes.Node.Capability']['meta_info']


            class Interfaces(_Entity_):
                """
                QoS list of interfaces
                
                .. attribute:: interface
                
                	QoS interface name
                	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface>`
                
                	**config**\: False
                
                

                """

                _prefix = 'skp-qos-oper'
                _revision = '2016-02-18'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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


                class Interface(_Entity_):
                    """
                    QoS interface name
                    
                    .. attribute:: interface_name  (key)
                    
                    	The name of the interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: output
                    
                    	QoS policy direction egress
                    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output>`
                    
                    	**config**\: False
                    
                    .. attribute:: input
                    
                    	QoS policy direction ingress
                    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'skp-qos-oper'
                    _revision = '2016-02-18'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(PlatformQos.Nodes.Node.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([("output", ("output", PlatformQos.Nodes.Node.Interfaces.Interface.Output)), ("input", ("input", PlatformQos.Nodes.Node.Interfaces.Interface.Input))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ])
                        self.interface_name = None

                        self.output = PlatformQos.Nodes.Node.Interfaces.Interface.Output()
                        self.output.parent = self
                        self._children_name_map["output"] = "output"

                        self.input = PlatformQos.Nodes.Node.Interfaces.Interface.Input()
                        self.input.parent = self
                        self._children_name_map["input"] = "input"
                        self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface, ['interface_name'], name, value)


                    class Output(_Entity_):
                        """
                        QoS policy direction egress
                        
                        .. attribute:: header
                        
                        	QoS EA policy header
                        	**type**\:  :py:class:`Header <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.Header>`
                        
                        	**config**\: False
                        
                        .. attribute:: interface_parameters
                        
                        	QoS Interface Parameters
                        	**type**\:  :py:class:`InterfaceParameters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters>`
                        
                        	**config**\: False
                        
                        .. attribute:: skywarp_qos_policy_class
                        
                        	Skywarp QoS policy class details
                        	**type**\:  :py:class:`SkywarpQosPolicyClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'skp-qos-oper'
                        _revision = '2016-02-18'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(PlatformQos.Nodes.Node.Interfaces.Interface.Output, self).__init__()

                            self.yang_name = "output"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("header", ("header", PlatformQos.Nodes.Node.Interfaces.Interface.Output.Header)), ("interface-parameters", ("interface_parameters", PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters)), ("skywarp-qos-policy-class", ("skywarp_qos_policy_class", PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass))])
                            self._leafs = OrderedDict()

                            self.header = PlatformQos.Nodes.Node.Interfaces.Interface.Output.Header()
                            self.header.parent = self
                            self._children_name_map["header"] = "header"

                            self.interface_parameters = PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters()
                            self.interface_parameters.parent = self
                            self._children_name_map["interface_parameters"] = "interface-parameters"

                            self.skywarp_qos_policy_class = PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass()
                            self.skywarp_qos_policy_class.parent = self
                            self._children_name_map["skywarp_qos_policy_class"] = "skywarp-qos-policy-class"
                            self._segment_path = lambda: "output"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output, [], name, value)


                        class Header(_Entity_):
                            """
                            QoS EA policy header
                            
                            .. attribute:: interface_name
                            
                            	Interface Name
                            	**type**\: str
                            
                            	**length:** 0..101
                            
                            	**config**\: False
                            
                            .. attribute:: policy_name
                            
                            	Policy name
                            	**type**\: str
                            
                            	**length:** 0..65
                            
                            	**config**\: False
                            
                            .. attribute:: direction
                            
                            	Direction
                            	**type**\: str
                            
                            	**length:** 0..11
                            
                            	**config**\: False
                            
                            .. attribute:: classes
                            
                            	Number of classes
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'skp-qos-oper'
                            _revision = '2016-02-18'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.Header, self).__init__()

                                self.yang_name = "header"
                                self.yang_parent_name = "output"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                    ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                    ('direction', (YLeaf(YType.str, 'direction'), ['str'])),
                                    ('classes', (YLeaf(YType.uint16, 'classes'), ['int'])),
                                ])
                                self.interface_name = None
                                self.policy_name = None
                                self.direction = None
                                self.classes = None
                                self._segment_path = lambda: "header"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.Header, ['interface_name', 'policy_name', 'direction', 'classes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.Header']['meta_info']


                        class InterfaceParameters(_Entity_):
                            """
                            QoS Interface Parameters
                            
                            .. attribute:: interface_config_rate
                            
                            	Interface Configured Rate
                            	**type**\:  :py:class:`InterfaceConfigRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters.InterfaceConfigRate>`
                            
                            	**config**\: False
                            
                            .. attribute:: interface_program_rate
                            
                            	Interface Programmed Rate
                            	**type**\:  :py:class:`InterfaceProgramRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters.InterfaceProgramRate>`
                            
                            	**config**\: False
                            
                            .. attribute:: port_shaper_rate
                            
                            	Port Shaper Rate
                            	**type**\:  :py:class:`PortShaperRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters.PortShaperRate>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'skp-qos-oper'
                            _revision = '2016-02-18'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters, self).__init__()

                                self.yang_name = "interface-parameters"
                                self.yang_parent_name = "output"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("interface-config-rate", ("interface_config_rate", PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters.InterfaceConfigRate)), ("interface-program-rate", ("interface_program_rate", PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters.InterfaceProgramRate)), ("port-shaper-rate", ("port_shaper_rate", PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters.PortShaperRate))])
                                self._leafs = OrderedDict()

                                self.interface_config_rate = PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters.InterfaceConfigRate()
                                self.interface_config_rate.parent = self
                                self._children_name_map["interface_config_rate"] = "interface-config-rate"

                                self.interface_program_rate = PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters.InterfaceProgramRate()
                                self.interface_program_rate.parent = self
                                self._children_name_map["interface_program_rate"] = "interface-program-rate"

                                self.port_shaper_rate = PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters.PortShaperRate()
                                self.port_shaper_rate.parent = self
                                self._children_name_map["port_shaper_rate"] = "port-shaper-rate"
                                self._segment_path = lambda: "interface-parameters"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters, [], name, value)


                            class InterfaceConfigRate(_Entity_):
                                """
                                Interface Configured Rate
                                
                                .. attribute:: value
                                
                                	Config value
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: unit
                                
                                	Config unit
                                	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'skp-qos-oper'
                                _revision = '2016-02-18'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters.InterfaceConfigRate, self).__init__()

                                    self.yang_name = "interface-config-rate"
                                    self.yang_parent_name = "interface-parameters"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                        ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                    ])
                                    self.value = None
                                    self.unit = None
                                    self._segment_path = lambda: "interface-config-rate"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters.InterfaceConfigRate, ['value', 'unit'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters.InterfaceConfigRate']['meta_info']


                            class InterfaceProgramRate(_Entity_):
                                """
                                Interface Programmed Rate
                                
                                .. attribute:: value
                                
                                	Config value
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: unit
                                
                                	Config unit
                                	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'skp-qos-oper'
                                _revision = '2016-02-18'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters.InterfaceProgramRate, self).__init__()

                                    self.yang_name = "interface-program-rate"
                                    self.yang_parent_name = "interface-parameters"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                        ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                    ])
                                    self.value = None
                                    self.unit = None
                                    self._segment_path = lambda: "interface-program-rate"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters.InterfaceProgramRate, ['value', 'unit'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters.InterfaceProgramRate']['meta_info']


                            class PortShaperRate(_Entity_):
                                """
                                Port Shaper Rate
                                
                                .. attribute:: value
                                
                                	Config value
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: unit
                                
                                	Config unit
                                	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'skp-qos-oper'
                                _revision = '2016-02-18'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters.PortShaperRate, self).__init__()

                                    self.yang_name = "port-shaper-rate"
                                    self.yang_parent_name = "interface-parameters"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                        ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                    ])
                                    self.value = None
                                    self.unit = None
                                    self._segment_path = lambda: "port-shaper-rate"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters.PortShaperRate, ['value', 'unit'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters.PortShaperRate']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.InterfaceParameters']['meta_info']


                        class SkywarpQosPolicyClass(_Entity_):
                            """
                            Skywarp QoS policy class details
                            
                            .. attribute:: qos_show_pclass_st
                            
                            	qos show pclass st
                            	**type**\: list of  		 :py:class:`QosShowPclassSt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'skp-qos-oper'
                            _revision = '2016-02-18'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass, self).__init__()

                                self.yang_name = "skywarp-qos-policy-class"
                                self.yang_parent_name = "output"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("qos-show-pclass-st", ("qos_show_pclass_st", PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt))])
                                self._leafs = OrderedDict()

                                self.qos_show_pclass_st = YList(self)
                                self._segment_path = lambda: "skywarp-qos-policy-class"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass, [], name, value)


                            class QosShowPclassSt(_Entity_):
                                """
                                qos show pclass st
                                
                                .. attribute:: queue
                                
                                	QoS Queue parameters
                                	**type**\:  :py:class:`Queue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Queue>`
                                
                                	**config**\: False
                                
                                .. attribute:: shape
                                
                                	QoS EA Shaper parameters
                                	**type**\:  :py:class:`Shape <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Shape>`
                                
                                	**config**\: False
                                
                                .. attribute:: wfq
                                
                                	QoS WFQ parameters
                                	**type**\:  :py:class:`Wfq <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq>`
                                
                                	**config**\: False
                                
                                .. attribute:: police
                                
                                	QoS Policer parameters
                                	**type**\:  :py:class:`Police <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Police>`
                                
                                	**config**\: False
                                
                                .. attribute:: marking
                                
                                	QoS Mark parameters
                                	**type**\:  :py:class:`Marking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking>`
                                
                                	**config**\: False
                                
                                .. attribute:: class_level
                                
                                	Class level
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                .. attribute:: class_name
                                
                                	Class name
                                	**type**\: str
                                
                                	**length:** 0..65
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'skp-qos-oper'
                                _revision = '2016-02-18'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt, self).__init__()

                                    self.yang_name = "qos-show-pclass-st"
                                    self.yang_parent_name = "skywarp-qos-policy-class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("queue", ("queue", PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Queue)), ("shape", ("shape", PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Shape)), ("wfq", ("wfq", PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq)), ("police", ("police", PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Police)), ("marking", ("marking", PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking))])
                                    self._leafs = OrderedDict([
                                        ('class_level', (YLeaf(YType.uint8, 'class-level'), ['int'])),
                                        ('class_name', (YLeaf(YType.str, 'class-name'), ['str'])),
                                    ])
                                    self.class_level = None
                                    self.class_name = None

                                    self.queue = PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Queue()
                                    self.queue.parent = self
                                    self._children_name_map["queue"] = "queue"

                                    self.shape = PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Shape()
                                    self.shape.parent = self
                                    self._children_name_map["shape"] = "shape"

                                    self.wfq = PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq()
                                    self.wfq.parent = self
                                    self._children_name_map["wfq"] = "wfq"

                                    self.police = PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Police()
                                    self.police.parent = self
                                    self._children_name_map["police"] = "police"

                                    self.marking = PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking()
                                    self.marking.parent = self
                                    self._children_name_map["marking"] = "marking"
                                    self._segment_path = lambda: "qos-show-pclass-st"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt, ['class_level', 'class_name'], name, value)


                                class Queue(_Entity_):
                                    """
                                    QoS Queue parameters
                                    
                                    .. attribute:: queue_id
                                    
                                    	Queue ID
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: queue_type
                                    
                                    	Queue Type
                                    	**type**\: str
                                    
                                    	**length:** 0..101
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'skp-qos-oper'
                                    _revision = '2016-02-18'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Queue, self).__init__()

                                        self.yang_name = "queue"
                                        self.yang_parent_name = "qos-show-pclass-st"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('queue_id', (YLeaf(YType.uint32, 'queue-id'), ['int'])),
                                            ('queue_type', (YLeaf(YType.str, 'queue-type'), ['str'])),
                                        ])
                                        self.queue_id = None
                                        self.queue_type = None
                                        self._segment_path = lambda: "queue"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Queue, ['queue_id', 'queue_type'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Queue']['meta_info']


                                class Shape(_Entity_):
                                    """
                                    QoS EA Shaper parameters
                                    
                                    .. attribute:: pir
                                    
                                    	PIR in kbps
                                    	**type**\:  :py:class:`Pir <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: pbs
                                    
                                    	PBS in bytes
                                    	**type**\:  :py:class:`Pbs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'skp-qos-oper'
                                    _revision = '2016-02-18'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Shape, self).__init__()

                                        self.yang_name = "shape"
                                        self.yang_parent_name = "qos-show-pclass-st"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("pir", ("pir", PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir)), ("pbs", ("pbs", PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs))])
                                        self._leafs = OrderedDict()

                                        self.pir = PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir()
                                        self.pir.parent = self
                                        self._children_name_map["pir"] = "pir"

                                        self.pbs = PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs()
                                        self.pbs.parent = self
                                        self._children_name_map["pbs"] = "pbs"
                                        self._segment_path = lambda: "shape"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Shape, [], name, value)


                                    class Pir(_Entity_):
                                        """
                                        PIR in kbps
                                        
                                        .. attribute:: value
                                        
                                        	Config value
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: unit
                                        
                                        	Config unit
                                        	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir, self).__init__()

                                            self.yang_name = "pir"
                                            self.yang_parent_name = "shape"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                            ])
                                            self.value = None
                                            self.unit = None
                                            self._segment_path = lambda: "pir"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir, ['value', 'unit'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir']['meta_info']


                                    class Pbs(_Entity_):
                                        """
                                        PBS in bytes
                                        
                                        .. attribute:: value
                                        
                                        	Config value
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: unit
                                        
                                        	Config unit
                                        	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs, self).__init__()

                                            self.yang_name = "pbs"
                                            self.yang_parent_name = "shape"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                            ])
                                            self.value = None
                                            self.unit = None
                                            self._segment_path = lambda: "pbs"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs, ['value', 'unit'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Shape']['meta_info']


                                class Wfq(_Entity_):
                                    """
                                    QoS WFQ parameters
                                    
                                    .. attribute:: committed_weight
                                    
                                    	Committed Weight
                                    	**type**\:  :py:class:`CommittedWeight <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: programmed_wfq
                                    
                                    	QoS Programmed WFQ parameters
                                    	**type**\:  :py:class:`ProgrammedWfq <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: excess_weight
                                    
                                    	Excess Weight
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'skp-qos-oper'
                                    _revision = '2016-02-18'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq, self).__init__()

                                        self.yang_name = "wfq"
                                        self.yang_parent_name = "qos-show-pclass-st"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("committed-weight", ("committed_weight", PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight)), ("programmed-wfq", ("programmed_wfq", PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq))])
                                        self._leafs = OrderedDict([
                                            ('excess_weight', (YLeaf(YType.uint16, 'excess-weight'), ['int'])),
                                        ])
                                        self.excess_weight = None

                                        self.committed_weight = PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight()
                                        self.committed_weight.parent = self
                                        self._children_name_map["committed_weight"] = "committed-weight"

                                        self.programmed_wfq = PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq()
                                        self.programmed_wfq.parent = self
                                        self._children_name_map["programmed_wfq"] = "programmed-wfq"
                                        self._segment_path = lambda: "wfq"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq, ['excess_weight'], name, value)


                                    class CommittedWeight(_Entity_):
                                        """
                                        Committed Weight
                                        
                                        .. attribute:: value
                                        
                                        	Config value
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: unit
                                        
                                        	Config unit
                                        	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight, self).__init__()

                                            self.yang_name = "committed-weight"
                                            self.yang_parent_name = "wfq"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                            ])
                                            self.value = None
                                            self.unit = None
                                            self._segment_path = lambda: "committed-weight"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight, ['value', 'unit'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight']['meta_info']


                                    class ProgrammedWfq(_Entity_):
                                        """
                                        QoS Programmed WFQ parameters
                                        
                                        .. attribute:: bandwidth
                                        
                                        	Bandwidth
                                        	**type**\:  :py:class:`Bandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: sum_of_bandwidth
                                        
                                        	Sum of Bandwidth
                                        	**type**\:  :py:class:`SumOfBandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: excess_ratio
                                        
                                        	Excess Ratio
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq, self).__init__()

                                            self.yang_name = "programmed-wfq"
                                            self.yang_parent_name = "wfq"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("bandwidth", ("bandwidth", PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth)), ("sum-of-bandwidth", ("sum_of_bandwidth", PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth))])
                                            self._leafs = OrderedDict([
                                                ('excess_ratio', (YLeaf(YType.uint16, 'excess-ratio'), ['int'])),
                                            ])
                                            self.excess_ratio = None

                                            self.bandwidth = PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth()
                                            self.bandwidth.parent = self
                                            self._children_name_map["bandwidth"] = "bandwidth"

                                            self.sum_of_bandwidth = PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth()
                                            self.sum_of_bandwidth.parent = self
                                            self._children_name_map["sum_of_bandwidth"] = "sum-of-bandwidth"
                                            self._segment_path = lambda: "programmed-wfq"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq, ['excess_ratio'], name, value)


                                        class Bandwidth(_Entity_):
                                            """
                                            Bandwidth
                                            
                                            .. attribute:: value
                                            
                                            	Config value
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: unit
                                            
                                            	Config unit
                                            	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth, self).__init__()

                                                self.yang_name = "bandwidth"
                                                self.yang_parent_name = "programmed-wfq"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                    ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                                ])
                                                self.value = None
                                                self.unit = None
                                                self._segment_path = lambda: "bandwidth"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth, ['value', 'unit'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth']['meta_info']


                                        class SumOfBandwidth(_Entity_):
                                            """
                                            Sum of Bandwidth
                                            
                                            .. attribute:: value
                                            
                                            	Config value
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: unit
                                            
                                            	Config unit
                                            	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth, self).__init__()

                                                self.yang_name = "sum-of-bandwidth"
                                                self.yang_parent_name = "programmed-wfq"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                    ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                                ])
                                                self.value = None
                                                self.unit = None
                                                self._segment_path = lambda: "sum-of-bandwidth"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth, ['value', 'unit'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Wfq']['meta_info']


                                class Police(_Entity_):
                                    """
                                    QoS Policer parameters
                                    
                                    .. attribute:: cir
                                    
                                    	CIR
                                    	**type**\:  :py:class:`Cir <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: cbs
                                    
                                    	CBS
                                    	**type**\:  :py:class:`Cbs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: policer_id
                                    
                                    	policer ID
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: policer_type
                                    
                                    	Policer type
                                    	**type**\:  :py:class:`TbAlgorithm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.TbAlgorithm>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'skp-qos-oper'
                                    _revision = '2016-02-18'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Police, self).__init__()

                                        self.yang_name = "police"
                                        self.yang_parent_name = "qos-show-pclass-st"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("cir", ("cir", PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir)), ("cbs", ("cbs", PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs))])
                                        self._leafs = OrderedDict([
                                            ('policer_id', (YLeaf(YType.uint32, 'policer-id'), ['int'])),
                                            ('policer_type', (YLeaf(YType.enumeration, 'policer-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'TbAlgorithm', '')])),
                                        ])
                                        self.policer_id = None
                                        self.policer_type = None

                                        self.cir = PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir()
                                        self.cir.parent = self
                                        self._children_name_map["cir"] = "cir"

                                        self.cbs = PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs()
                                        self.cbs.parent = self
                                        self._children_name_map["cbs"] = "cbs"
                                        self._segment_path = lambda: "police"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Police, ['policer_id', 'policer_type'], name, value)


                                    class Cir(_Entity_):
                                        """
                                        CIR
                                        
                                        .. attribute:: value
                                        
                                        	Config value
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: unit
                                        
                                        	Config unit
                                        	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir, self).__init__()

                                            self.yang_name = "cir"
                                            self.yang_parent_name = "police"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                            ])
                                            self.value = None
                                            self.unit = None
                                            self._segment_path = lambda: "cir"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir, ['value', 'unit'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir']['meta_info']


                                    class Cbs(_Entity_):
                                        """
                                        CBS
                                        
                                        .. attribute:: value
                                        
                                        	Config value
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: unit
                                        
                                        	Config unit
                                        	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs, self).__init__()

                                            self.yang_name = "cbs"
                                            self.yang_parent_name = "police"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                            ])
                                            self.value = None
                                            self.unit = None
                                            self._segment_path = lambda: "cbs"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs, ['value', 'unit'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Police']['meta_info']


                                class Marking(_Entity_):
                                    """
                                    QoS Mark parameters
                                    
                                    .. attribute:: mark_only
                                    
                                    	Mark Only
                                    	**type**\:  :py:class:`MarkOnly <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: police_conform
                                    
                                    	Police conform mark
                                    	**type**\:  :py:class:`PoliceConform <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: police_exceed
                                    
                                    	Police exceed mark
                                    	**type**\:  :py:class:`PoliceExceed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'skp-qos-oper'
                                    _revision = '2016-02-18'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking, self).__init__()

                                        self.yang_name = "marking"
                                        self.yang_parent_name = "qos-show-pclass-st"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("mark-only", ("mark_only", PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly)), ("police-conform", ("police_conform", PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform)), ("police-exceed", ("police_exceed", PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed))])
                                        self._leafs = OrderedDict()

                                        self.mark_only = PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly()
                                        self.mark_only.parent = self
                                        self._children_name_map["mark_only"] = "mark-only"

                                        self.police_conform = PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform()
                                        self.police_conform.parent = self
                                        self._children_name_map["police_conform"] = "police-conform"

                                        self.police_exceed = PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed()
                                        self.police_exceed.parent = self
                                        self._children_name_map["police_exceed"] = "police-exceed"
                                        self._segment_path = lambda: "marking"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking, [], name, value)


                                    class MarkOnly(_Entity_):
                                        """
                                        Mark Only
                                        
                                        .. attribute:: action_type
                                        
                                        	Action type
                                        	**type**\:  :py:class:`Action <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.Action>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: mark_detail
                                        
                                        	Mark value
                                        	**type**\: list of  		 :py:class:`MarkDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly.MarkDetail>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly, self).__init__()

                                            self.yang_name = "mark-only"
                                            self.yang_parent_name = "marking"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("mark-detail", ("mark_detail", PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly.MarkDetail))])
                                            self._leafs = OrderedDict([
                                                ('action_type', (YLeaf(YType.enumeration, 'action-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'Action', '')])),
                                            ])
                                            self.action_type = None

                                            self.mark_detail = YList(self)
                                            self._segment_path = lambda: "mark-only"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly, ['action_type'], name, value)


                                        class MarkDetail(_Entity_):
                                            """
                                            Mark value
                                            
                                            .. attribute:: mark_value
                                            
                                            	Mark value
                                            	**type**\: int
                                            
                                            	**range:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: action_opcode
                                            
                                            	Action opcode
                                            	**type**\:  :py:class:`ActionOpcode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.ActionOpcode>`
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly.MarkDetail, self).__init__()

                                                self.yang_name = "mark-detail"
                                                self.yang_parent_name = "mark-only"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('mark_value', (YLeaf(YType.uint8, 'mark-value'), ['int'])),
                                                    ('action_opcode', (YLeaf(YType.enumeration, 'action-opcode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'ActionOpcode', '')])),
                                                ])
                                                self.mark_value = None
                                                self.action_opcode = None
                                                self._segment_path = lambda: "mark-detail"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly.MarkDetail, ['mark_value', 'action_opcode'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly.MarkDetail']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly']['meta_info']


                                    class PoliceConform(_Entity_):
                                        """
                                        Police conform mark
                                        
                                        .. attribute:: action_type
                                        
                                        	Action type
                                        	**type**\:  :py:class:`Action <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.Action>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: mark_detail
                                        
                                        	Mark value
                                        	**type**\: list of  		 :py:class:`MarkDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform.MarkDetail>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform, self).__init__()

                                            self.yang_name = "police-conform"
                                            self.yang_parent_name = "marking"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("mark-detail", ("mark_detail", PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform.MarkDetail))])
                                            self._leafs = OrderedDict([
                                                ('action_type', (YLeaf(YType.enumeration, 'action-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'Action', '')])),
                                            ])
                                            self.action_type = None

                                            self.mark_detail = YList(self)
                                            self._segment_path = lambda: "police-conform"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform, ['action_type'], name, value)


                                        class MarkDetail(_Entity_):
                                            """
                                            Mark value
                                            
                                            .. attribute:: mark_value
                                            
                                            	Mark value
                                            	**type**\: int
                                            
                                            	**range:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: action_opcode
                                            
                                            	Action opcode
                                            	**type**\:  :py:class:`ActionOpcode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.ActionOpcode>`
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform.MarkDetail, self).__init__()

                                                self.yang_name = "mark-detail"
                                                self.yang_parent_name = "police-conform"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('mark_value', (YLeaf(YType.uint8, 'mark-value'), ['int'])),
                                                    ('action_opcode', (YLeaf(YType.enumeration, 'action-opcode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'ActionOpcode', '')])),
                                                ])
                                                self.mark_value = None
                                                self.action_opcode = None
                                                self._segment_path = lambda: "mark-detail"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform.MarkDetail, ['mark_value', 'action_opcode'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform.MarkDetail']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform']['meta_info']


                                    class PoliceExceed(_Entity_):
                                        """
                                        Police exceed mark
                                        
                                        .. attribute:: action_type
                                        
                                        	Action type
                                        	**type**\:  :py:class:`Action <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.Action>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: mark_detail
                                        
                                        	Mark value
                                        	**type**\: list of  		 :py:class:`MarkDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed.MarkDetail>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed, self).__init__()

                                            self.yang_name = "police-exceed"
                                            self.yang_parent_name = "marking"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("mark-detail", ("mark_detail", PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed.MarkDetail))])
                                            self._leafs = OrderedDict([
                                                ('action_type', (YLeaf(YType.enumeration, 'action-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'Action', '')])),
                                            ])
                                            self.action_type = None

                                            self.mark_detail = YList(self)
                                            self._segment_path = lambda: "police-exceed"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed, ['action_type'], name, value)


                                        class MarkDetail(_Entity_):
                                            """
                                            Mark value
                                            
                                            .. attribute:: mark_value
                                            
                                            	Mark value
                                            	**type**\: int
                                            
                                            	**range:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: action_opcode
                                            
                                            	Action opcode
                                            	**type**\:  :py:class:`ActionOpcode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.ActionOpcode>`
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed.MarkDetail, self).__init__()

                                                self.yang_name = "mark-detail"
                                                self.yang_parent_name = "police-exceed"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('mark_value', (YLeaf(YType.uint8, 'mark-value'), ['int'])),
                                                    ('action_opcode', (YLeaf(YType.enumeration, 'action-opcode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'ActionOpcode', '')])),
                                                ])
                                                self.mark_value = None
                                                self.action_opcode = None
                                                self._segment_path = lambda: "mark-detail"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed.MarkDetail, ['mark_value', 'action_opcode'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed.MarkDetail']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt.Marking']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass.QosShowPclassSt']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output.SkywarpQosPolicyClass']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Output']['meta_info']


                    class Input(_Entity_):
                        """
                        QoS policy direction ingress
                        
                        .. attribute:: header
                        
                        	QoS EA policy header
                        	**type**\:  :py:class:`Header <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.Header>`
                        
                        	**config**\: False
                        
                        .. attribute:: interface_parameters
                        
                        	QoS Interface Parameters
                        	**type**\:  :py:class:`InterfaceParameters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters>`
                        
                        	**config**\: False
                        
                        .. attribute:: skywarp_qos_policy_class
                        
                        	Skywarp QoS policy class details
                        	**type**\:  :py:class:`SkywarpQosPolicyClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'skp-qos-oper'
                        _revision = '2016-02-18'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(PlatformQos.Nodes.Node.Interfaces.Interface.Input, self).__init__()

                            self.yang_name = "input"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("header", ("header", PlatformQos.Nodes.Node.Interfaces.Interface.Input.Header)), ("interface-parameters", ("interface_parameters", PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters)), ("skywarp-qos-policy-class", ("skywarp_qos_policy_class", PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass))])
                            self._leafs = OrderedDict()

                            self.header = PlatformQos.Nodes.Node.Interfaces.Interface.Input.Header()
                            self.header.parent = self
                            self._children_name_map["header"] = "header"

                            self.interface_parameters = PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters()
                            self.interface_parameters.parent = self
                            self._children_name_map["interface_parameters"] = "interface-parameters"

                            self.skywarp_qos_policy_class = PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass()
                            self.skywarp_qos_policy_class.parent = self
                            self._children_name_map["skywarp_qos_policy_class"] = "skywarp-qos-policy-class"
                            self._segment_path = lambda: "input"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Input, [], name, value)


                        class Header(_Entity_):
                            """
                            QoS EA policy header
                            
                            .. attribute:: interface_name
                            
                            	Interface Name
                            	**type**\: str
                            
                            	**length:** 0..101
                            
                            	**config**\: False
                            
                            .. attribute:: policy_name
                            
                            	Policy name
                            	**type**\: str
                            
                            	**length:** 0..65
                            
                            	**config**\: False
                            
                            .. attribute:: direction
                            
                            	Direction
                            	**type**\: str
                            
                            	**length:** 0..11
                            
                            	**config**\: False
                            
                            .. attribute:: classes
                            
                            	Number of classes
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'skp-qos-oper'
                            _revision = '2016-02-18'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.Input.Header, self).__init__()

                                self.yang_name = "header"
                                self.yang_parent_name = "input"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                    ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                    ('direction', (YLeaf(YType.str, 'direction'), ['str'])),
                                    ('classes', (YLeaf(YType.uint16, 'classes'), ['int'])),
                                ])
                                self.interface_name = None
                                self.policy_name = None
                                self.direction = None
                                self.classes = None
                                self._segment_path = lambda: "header"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Input.Header, ['interface_name', 'policy_name', 'direction', 'classes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.Header']['meta_info']


                        class InterfaceParameters(_Entity_):
                            """
                            QoS Interface Parameters
                            
                            .. attribute:: interface_config_rate
                            
                            	Interface Configured Rate
                            	**type**\:  :py:class:`InterfaceConfigRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters.InterfaceConfigRate>`
                            
                            	**config**\: False
                            
                            .. attribute:: interface_program_rate
                            
                            	Interface Programmed Rate
                            	**type**\:  :py:class:`InterfaceProgramRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters.InterfaceProgramRate>`
                            
                            	**config**\: False
                            
                            .. attribute:: port_shaper_rate
                            
                            	Port Shaper Rate
                            	**type**\:  :py:class:`PortShaperRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters.PortShaperRate>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'skp-qos-oper'
                            _revision = '2016-02-18'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters, self).__init__()

                                self.yang_name = "interface-parameters"
                                self.yang_parent_name = "input"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("interface-config-rate", ("interface_config_rate", PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters.InterfaceConfigRate)), ("interface-program-rate", ("interface_program_rate", PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters.InterfaceProgramRate)), ("port-shaper-rate", ("port_shaper_rate", PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters.PortShaperRate))])
                                self._leafs = OrderedDict()

                                self.interface_config_rate = PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters.InterfaceConfigRate()
                                self.interface_config_rate.parent = self
                                self._children_name_map["interface_config_rate"] = "interface-config-rate"

                                self.interface_program_rate = PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters.InterfaceProgramRate()
                                self.interface_program_rate.parent = self
                                self._children_name_map["interface_program_rate"] = "interface-program-rate"

                                self.port_shaper_rate = PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters.PortShaperRate()
                                self.port_shaper_rate.parent = self
                                self._children_name_map["port_shaper_rate"] = "port-shaper-rate"
                                self._segment_path = lambda: "interface-parameters"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters, [], name, value)


                            class InterfaceConfigRate(_Entity_):
                                """
                                Interface Configured Rate
                                
                                .. attribute:: value
                                
                                	Config value
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: unit
                                
                                	Config unit
                                	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'skp-qos-oper'
                                _revision = '2016-02-18'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters.InterfaceConfigRate, self).__init__()

                                    self.yang_name = "interface-config-rate"
                                    self.yang_parent_name = "interface-parameters"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                        ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                    ])
                                    self.value = None
                                    self.unit = None
                                    self._segment_path = lambda: "interface-config-rate"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters.InterfaceConfigRate, ['value', 'unit'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters.InterfaceConfigRate']['meta_info']


                            class InterfaceProgramRate(_Entity_):
                                """
                                Interface Programmed Rate
                                
                                .. attribute:: value
                                
                                	Config value
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: unit
                                
                                	Config unit
                                	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'skp-qos-oper'
                                _revision = '2016-02-18'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters.InterfaceProgramRate, self).__init__()

                                    self.yang_name = "interface-program-rate"
                                    self.yang_parent_name = "interface-parameters"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                        ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                    ])
                                    self.value = None
                                    self.unit = None
                                    self._segment_path = lambda: "interface-program-rate"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters.InterfaceProgramRate, ['value', 'unit'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters.InterfaceProgramRate']['meta_info']


                            class PortShaperRate(_Entity_):
                                """
                                Port Shaper Rate
                                
                                .. attribute:: value
                                
                                	Config value
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: unit
                                
                                	Config unit
                                	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'skp-qos-oper'
                                _revision = '2016-02-18'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters.PortShaperRate, self).__init__()

                                    self.yang_name = "port-shaper-rate"
                                    self.yang_parent_name = "interface-parameters"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                        ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                    ])
                                    self.value = None
                                    self.unit = None
                                    self._segment_path = lambda: "port-shaper-rate"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters.PortShaperRate, ['value', 'unit'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters.PortShaperRate']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.InterfaceParameters']['meta_info']


                        class SkywarpQosPolicyClass(_Entity_):
                            """
                            Skywarp QoS policy class details
                            
                            .. attribute:: qos_show_pclass_st
                            
                            	qos show pclass st
                            	**type**\: list of  		 :py:class:`QosShowPclassSt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'skp-qos-oper'
                            _revision = '2016-02-18'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass, self).__init__()

                                self.yang_name = "skywarp-qos-policy-class"
                                self.yang_parent_name = "input"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("qos-show-pclass-st", ("qos_show_pclass_st", PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt))])
                                self._leafs = OrderedDict()

                                self.qos_show_pclass_st = YList(self)
                                self._segment_path = lambda: "skywarp-qos-policy-class"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass, [], name, value)


                            class QosShowPclassSt(_Entity_):
                                """
                                qos show pclass st
                                
                                .. attribute:: queue
                                
                                	QoS Queue parameters
                                	**type**\:  :py:class:`Queue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Queue>`
                                
                                	**config**\: False
                                
                                .. attribute:: shape
                                
                                	QoS EA Shaper parameters
                                	**type**\:  :py:class:`Shape <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Shape>`
                                
                                	**config**\: False
                                
                                .. attribute:: wfq
                                
                                	QoS WFQ parameters
                                	**type**\:  :py:class:`Wfq <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq>`
                                
                                	**config**\: False
                                
                                .. attribute:: police
                                
                                	QoS Policer parameters
                                	**type**\:  :py:class:`Police <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Police>`
                                
                                	**config**\: False
                                
                                .. attribute:: marking
                                
                                	QoS Mark parameters
                                	**type**\:  :py:class:`Marking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking>`
                                
                                	**config**\: False
                                
                                .. attribute:: class_level
                                
                                	Class level
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                .. attribute:: class_name
                                
                                	Class name
                                	**type**\: str
                                
                                	**length:** 0..65
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'skp-qos-oper'
                                _revision = '2016-02-18'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt, self).__init__()

                                    self.yang_name = "qos-show-pclass-st"
                                    self.yang_parent_name = "skywarp-qos-policy-class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("queue", ("queue", PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Queue)), ("shape", ("shape", PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Shape)), ("wfq", ("wfq", PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq)), ("police", ("police", PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Police)), ("marking", ("marking", PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking))])
                                    self._leafs = OrderedDict([
                                        ('class_level', (YLeaf(YType.uint8, 'class-level'), ['int'])),
                                        ('class_name', (YLeaf(YType.str, 'class-name'), ['str'])),
                                    ])
                                    self.class_level = None
                                    self.class_name = None

                                    self.queue = PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Queue()
                                    self.queue.parent = self
                                    self._children_name_map["queue"] = "queue"

                                    self.shape = PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Shape()
                                    self.shape.parent = self
                                    self._children_name_map["shape"] = "shape"

                                    self.wfq = PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq()
                                    self.wfq.parent = self
                                    self._children_name_map["wfq"] = "wfq"

                                    self.police = PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Police()
                                    self.police.parent = self
                                    self._children_name_map["police"] = "police"

                                    self.marking = PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking()
                                    self.marking.parent = self
                                    self._children_name_map["marking"] = "marking"
                                    self._segment_path = lambda: "qos-show-pclass-st"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt, ['class_level', 'class_name'], name, value)


                                class Queue(_Entity_):
                                    """
                                    QoS Queue parameters
                                    
                                    .. attribute:: queue_id
                                    
                                    	Queue ID
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: queue_type
                                    
                                    	Queue Type
                                    	**type**\: str
                                    
                                    	**length:** 0..101
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'skp-qos-oper'
                                    _revision = '2016-02-18'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Queue, self).__init__()

                                        self.yang_name = "queue"
                                        self.yang_parent_name = "qos-show-pclass-st"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('queue_id', (YLeaf(YType.uint32, 'queue-id'), ['int'])),
                                            ('queue_type', (YLeaf(YType.str, 'queue-type'), ['str'])),
                                        ])
                                        self.queue_id = None
                                        self.queue_type = None
                                        self._segment_path = lambda: "queue"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Queue, ['queue_id', 'queue_type'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Queue']['meta_info']


                                class Shape(_Entity_):
                                    """
                                    QoS EA Shaper parameters
                                    
                                    .. attribute:: pir
                                    
                                    	PIR in kbps
                                    	**type**\:  :py:class:`Pir <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: pbs
                                    
                                    	PBS in bytes
                                    	**type**\:  :py:class:`Pbs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'skp-qos-oper'
                                    _revision = '2016-02-18'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Shape, self).__init__()

                                        self.yang_name = "shape"
                                        self.yang_parent_name = "qos-show-pclass-st"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("pir", ("pir", PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir)), ("pbs", ("pbs", PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs))])
                                        self._leafs = OrderedDict()

                                        self.pir = PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir()
                                        self.pir.parent = self
                                        self._children_name_map["pir"] = "pir"

                                        self.pbs = PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs()
                                        self.pbs.parent = self
                                        self._children_name_map["pbs"] = "pbs"
                                        self._segment_path = lambda: "shape"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Shape, [], name, value)


                                    class Pir(_Entity_):
                                        """
                                        PIR in kbps
                                        
                                        .. attribute:: value
                                        
                                        	Config value
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: unit
                                        
                                        	Config unit
                                        	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir, self).__init__()

                                            self.yang_name = "pir"
                                            self.yang_parent_name = "shape"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                            ])
                                            self.value = None
                                            self.unit = None
                                            self._segment_path = lambda: "pir"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir, ['value', 'unit'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pir']['meta_info']


                                    class Pbs(_Entity_):
                                        """
                                        PBS in bytes
                                        
                                        .. attribute:: value
                                        
                                        	Config value
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: unit
                                        
                                        	Config unit
                                        	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs, self).__init__()

                                            self.yang_name = "pbs"
                                            self.yang_parent_name = "shape"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                            ])
                                            self.value = None
                                            self.unit = None
                                            self._segment_path = lambda: "pbs"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs, ['value', 'unit'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Shape.Pbs']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Shape']['meta_info']


                                class Wfq(_Entity_):
                                    """
                                    QoS WFQ parameters
                                    
                                    .. attribute:: committed_weight
                                    
                                    	Committed Weight
                                    	**type**\:  :py:class:`CommittedWeight <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: programmed_wfq
                                    
                                    	QoS Programmed WFQ parameters
                                    	**type**\:  :py:class:`ProgrammedWfq <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: excess_weight
                                    
                                    	Excess Weight
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'skp-qos-oper'
                                    _revision = '2016-02-18'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq, self).__init__()

                                        self.yang_name = "wfq"
                                        self.yang_parent_name = "qos-show-pclass-st"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("committed-weight", ("committed_weight", PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight)), ("programmed-wfq", ("programmed_wfq", PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq))])
                                        self._leafs = OrderedDict([
                                            ('excess_weight', (YLeaf(YType.uint16, 'excess-weight'), ['int'])),
                                        ])
                                        self.excess_weight = None

                                        self.committed_weight = PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight()
                                        self.committed_weight.parent = self
                                        self._children_name_map["committed_weight"] = "committed-weight"

                                        self.programmed_wfq = PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq()
                                        self.programmed_wfq.parent = self
                                        self._children_name_map["programmed_wfq"] = "programmed-wfq"
                                        self._segment_path = lambda: "wfq"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq, ['excess_weight'], name, value)


                                    class CommittedWeight(_Entity_):
                                        """
                                        Committed Weight
                                        
                                        .. attribute:: value
                                        
                                        	Config value
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: unit
                                        
                                        	Config unit
                                        	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight, self).__init__()

                                            self.yang_name = "committed-weight"
                                            self.yang_parent_name = "wfq"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                            ])
                                            self.value = None
                                            self.unit = None
                                            self._segment_path = lambda: "committed-weight"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight, ['value', 'unit'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.CommittedWeight']['meta_info']


                                    class ProgrammedWfq(_Entity_):
                                        """
                                        QoS Programmed WFQ parameters
                                        
                                        .. attribute:: bandwidth
                                        
                                        	Bandwidth
                                        	**type**\:  :py:class:`Bandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: sum_of_bandwidth
                                        
                                        	Sum of Bandwidth
                                        	**type**\:  :py:class:`SumOfBandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: excess_ratio
                                        
                                        	Excess Ratio
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq, self).__init__()

                                            self.yang_name = "programmed-wfq"
                                            self.yang_parent_name = "wfq"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("bandwidth", ("bandwidth", PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth)), ("sum-of-bandwidth", ("sum_of_bandwidth", PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth))])
                                            self._leafs = OrderedDict([
                                                ('excess_ratio', (YLeaf(YType.uint16, 'excess-ratio'), ['int'])),
                                            ])
                                            self.excess_ratio = None

                                            self.bandwidth = PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth()
                                            self.bandwidth.parent = self
                                            self._children_name_map["bandwidth"] = "bandwidth"

                                            self.sum_of_bandwidth = PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth()
                                            self.sum_of_bandwidth.parent = self
                                            self._children_name_map["sum_of_bandwidth"] = "sum-of-bandwidth"
                                            self._segment_path = lambda: "programmed-wfq"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq, ['excess_ratio'], name, value)


                                        class Bandwidth(_Entity_):
                                            """
                                            Bandwidth
                                            
                                            .. attribute:: value
                                            
                                            	Config value
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: unit
                                            
                                            	Config unit
                                            	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth, self).__init__()

                                                self.yang_name = "bandwidth"
                                                self.yang_parent_name = "programmed-wfq"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                    ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                                ])
                                                self.value = None
                                                self.unit = None
                                                self._segment_path = lambda: "bandwidth"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth, ['value', 'unit'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.Bandwidth']['meta_info']


                                        class SumOfBandwidth(_Entity_):
                                            """
                                            Sum of Bandwidth
                                            
                                            .. attribute:: value
                                            
                                            	Config value
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: unit
                                            
                                            	Config unit
                                            	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth, self).__init__()

                                                self.yang_name = "sum-of-bandwidth"
                                                self.yang_parent_name = "programmed-wfq"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                    ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                                ])
                                                self.value = None
                                                self.unit = None
                                                self._segment_path = lambda: "sum-of-bandwidth"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth, ['value', 'unit'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq.SumOfBandwidth']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq.ProgrammedWfq']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Wfq']['meta_info']


                                class Police(_Entity_):
                                    """
                                    QoS Policer parameters
                                    
                                    .. attribute:: cir
                                    
                                    	CIR
                                    	**type**\:  :py:class:`Cir <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: cbs
                                    
                                    	CBS
                                    	**type**\:  :py:class:`Cbs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: policer_id
                                    
                                    	policer ID
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: policer_type
                                    
                                    	Policer type
                                    	**type**\:  :py:class:`TbAlgorithm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.TbAlgorithm>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'skp-qos-oper'
                                    _revision = '2016-02-18'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Police, self).__init__()

                                        self.yang_name = "police"
                                        self.yang_parent_name = "qos-show-pclass-st"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("cir", ("cir", PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir)), ("cbs", ("cbs", PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs))])
                                        self._leafs = OrderedDict([
                                            ('policer_id', (YLeaf(YType.uint32, 'policer-id'), ['int'])),
                                            ('policer_type', (YLeaf(YType.enumeration, 'policer-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'TbAlgorithm', '')])),
                                        ])
                                        self.policer_id = None
                                        self.policer_type = None

                                        self.cir = PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir()
                                        self.cir.parent = self
                                        self._children_name_map["cir"] = "cir"

                                        self.cbs = PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs()
                                        self.cbs.parent = self
                                        self._children_name_map["cbs"] = "cbs"
                                        self._segment_path = lambda: "police"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Police, ['policer_id', 'policer_type'], name, value)


                                    class Cir(_Entity_):
                                        """
                                        CIR
                                        
                                        .. attribute:: value
                                        
                                        	Config value
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: unit
                                        
                                        	Config unit
                                        	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir, self).__init__()

                                            self.yang_name = "cir"
                                            self.yang_parent_name = "police"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                            ])
                                            self.value = None
                                            self.unit = None
                                            self._segment_path = lambda: "cir"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir, ['value', 'unit'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cir']['meta_info']


                                    class Cbs(_Entity_):
                                        """
                                        CBS
                                        
                                        .. attribute:: value
                                        
                                        	Config value
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: unit
                                        
                                        	Config unit
                                        	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs, self).__init__()

                                            self.yang_name = "cbs"
                                            self.yang_parent_name = "police"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                            ])
                                            self.value = None
                                            self.unit = None
                                            self._segment_path = lambda: "cbs"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs, ['value', 'unit'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Police.Cbs']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Police']['meta_info']


                                class Marking(_Entity_):
                                    """
                                    QoS Mark parameters
                                    
                                    .. attribute:: mark_only
                                    
                                    	Mark Only
                                    	**type**\:  :py:class:`MarkOnly <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: police_conform
                                    
                                    	Police conform mark
                                    	**type**\:  :py:class:`PoliceConform <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: police_exceed
                                    
                                    	Police exceed mark
                                    	**type**\:  :py:class:`PoliceExceed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'skp-qos-oper'
                                    _revision = '2016-02-18'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking, self).__init__()

                                        self.yang_name = "marking"
                                        self.yang_parent_name = "qos-show-pclass-st"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("mark-only", ("mark_only", PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly)), ("police-conform", ("police_conform", PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform)), ("police-exceed", ("police_exceed", PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed))])
                                        self._leafs = OrderedDict()

                                        self.mark_only = PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly()
                                        self.mark_only.parent = self
                                        self._children_name_map["mark_only"] = "mark-only"

                                        self.police_conform = PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform()
                                        self.police_conform.parent = self
                                        self._children_name_map["police_conform"] = "police-conform"

                                        self.police_exceed = PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed()
                                        self.police_exceed.parent = self
                                        self._children_name_map["police_exceed"] = "police-exceed"
                                        self._segment_path = lambda: "marking"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking, [], name, value)


                                    class MarkOnly(_Entity_):
                                        """
                                        Mark Only
                                        
                                        .. attribute:: action_type
                                        
                                        	Action type
                                        	**type**\:  :py:class:`Action <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.Action>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: mark_detail
                                        
                                        	Mark value
                                        	**type**\: list of  		 :py:class:`MarkDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly.MarkDetail>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly, self).__init__()

                                            self.yang_name = "mark-only"
                                            self.yang_parent_name = "marking"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("mark-detail", ("mark_detail", PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly.MarkDetail))])
                                            self._leafs = OrderedDict([
                                                ('action_type', (YLeaf(YType.enumeration, 'action-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'Action', '')])),
                                            ])
                                            self.action_type = None

                                            self.mark_detail = YList(self)
                                            self._segment_path = lambda: "mark-only"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly, ['action_type'], name, value)


                                        class MarkDetail(_Entity_):
                                            """
                                            Mark value
                                            
                                            .. attribute:: mark_value
                                            
                                            	Mark value
                                            	**type**\: int
                                            
                                            	**range:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: action_opcode
                                            
                                            	Action opcode
                                            	**type**\:  :py:class:`ActionOpcode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.ActionOpcode>`
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly.MarkDetail, self).__init__()

                                                self.yang_name = "mark-detail"
                                                self.yang_parent_name = "mark-only"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('mark_value', (YLeaf(YType.uint8, 'mark-value'), ['int'])),
                                                    ('action_opcode', (YLeaf(YType.enumeration, 'action-opcode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'ActionOpcode', '')])),
                                                ])
                                                self.mark_value = None
                                                self.action_opcode = None
                                                self._segment_path = lambda: "mark-detail"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly.MarkDetail, ['mark_value', 'action_opcode'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly.MarkDetail']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.MarkOnly']['meta_info']


                                    class PoliceConform(_Entity_):
                                        """
                                        Police conform mark
                                        
                                        .. attribute:: action_type
                                        
                                        	Action type
                                        	**type**\:  :py:class:`Action <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.Action>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: mark_detail
                                        
                                        	Mark value
                                        	**type**\: list of  		 :py:class:`MarkDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform.MarkDetail>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform, self).__init__()

                                            self.yang_name = "police-conform"
                                            self.yang_parent_name = "marking"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("mark-detail", ("mark_detail", PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform.MarkDetail))])
                                            self._leafs = OrderedDict([
                                                ('action_type', (YLeaf(YType.enumeration, 'action-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'Action', '')])),
                                            ])
                                            self.action_type = None

                                            self.mark_detail = YList(self)
                                            self._segment_path = lambda: "police-conform"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform, ['action_type'], name, value)


                                        class MarkDetail(_Entity_):
                                            """
                                            Mark value
                                            
                                            .. attribute:: mark_value
                                            
                                            	Mark value
                                            	**type**\: int
                                            
                                            	**range:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: action_opcode
                                            
                                            	Action opcode
                                            	**type**\:  :py:class:`ActionOpcode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.ActionOpcode>`
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform.MarkDetail, self).__init__()

                                                self.yang_name = "mark-detail"
                                                self.yang_parent_name = "police-conform"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('mark_value', (YLeaf(YType.uint8, 'mark-value'), ['int'])),
                                                    ('action_opcode', (YLeaf(YType.enumeration, 'action-opcode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'ActionOpcode', '')])),
                                                ])
                                                self.mark_value = None
                                                self.action_opcode = None
                                                self._segment_path = lambda: "mark-detail"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform.MarkDetail, ['mark_value', 'action_opcode'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform.MarkDetail']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceConform']['meta_info']


                                    class PoliceExceed(_Entity_):
                                        """
                                        Police exceed mark
                                        
                                        .. attribute:: action_type
                                        
                                        	Action type
                                        	**type**\:  :py:class:`Action <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.Action>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: mark_detail
                                        
                                        	Mark value
                                        	**type**\: list of  		 :py:class:`MarkDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed.MarkDetail>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed, self).__init__()

                                            self.yang_name = "police-exceed"
                                            self.yang_parent_name = "marking"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("mark-detail", ("mark_detail", PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed.MarkDetail))])
                                            self._leafs = OrderedDict([
                                                ('action_type', (YLeaf(YType.enumeration, 'action-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'Action', '')])),
                                            ])
                                            self.action_type = None

                                            self.mark_detail = YList(self)
                                            self._segment_path = lambda: "police-exceed"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed, ['action_type'], name, value)


                                        class MarkDetail(_Entity_):
                                            """
                                            Mark value
                                            
                                            .. attribute:: mark_value
                                            
                                            	Mark value
                                            	**type**\: int
                                            
                                            	**range:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: action_opcode
                                            
                                            	Action opcode
                                            	**type**\:  :py:class:`ActionOpcode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.ActionOpcode>`
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed.MarkDetail, self).__init__()

                                                self.yang_name = "mark-detail"
                                                self.yang_parent_name = "police-exceed"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('mark_value', (YLeaf(YType.uint8, 'mark-value'), ['int'])),
                                                    ('action_opcode', (YLeaf(YType.enumeration, 'action-opcode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'ActionOpcode', '')])),
                                                ])
                                                self.mark_value = None
                                                self.action_opcode = None
                                                self._segment_path = lambda: "mark-detail"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed.MarkDetail, ['mark_value', 'action_opcode'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed.MarkDetail']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking.PoliceExceed']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                        return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt.Marking']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass.QosShowPclassSt']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input.SkywarpQosPolicyClass']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                            return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Input']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                        return meta._meta_table['PlatformQos.Nodes.Node.Interfaces.Interface']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                    return meta._meta_table['PlatformQos.Nodes.Node.Interfaces']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                return meta._meta_table['PlatformQos.Nodes.Node']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
            return meta._meta_table['PlatformQos.Nodes']['meta_info']

    def clone_ptr(self):
        self._top_entity = PlatformQos()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
        return meta._meta_table['PlatformQos']['meta_info']


class PlatformQosEa(_Entity_):
    """
    platform qos ea
    
    .. attribute:: nodes
    
    	List of nodes with platform specific QoS\-EA configuration
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes>`
    
    	**config**\: False
    
    

    """

    _prefix = 'skp-qos-oper'
    _revision = '2016-02-18'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(PlatformQosEa, self).__init__()
        self._top_entity = None

        self.yang_name = "platform-qos-ea"
        self.yang_parent_name = "Cisco-IOS-XR-skp-qos-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", PlatformQosEa.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = PlatformQosEa.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-skp-qos-oper:platform-qos-ea"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(PlatformQosEa, [], name, value)


    class Nodes(_Entity_):
        """
        List of nodes with platform specific QoS\-EA
        configuration
        
        .. attribute:: node
        
        	Node with platform specific QoS\-EA configuration
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node>`
        
        	**config**\: False
        
        

        """

        _prefix = 'skp-qos-oper'
        _revision = '2016-02-18'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(PlatformQosEa.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "platform-qos-ea"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", PlatformQosEa.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-skp-qos-oper:platform-qos-ea/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PlatformQosEa.Nodes, [], name, value)


        class Node(_Entity_):
            """
            Node with platform specific QoS\-EA
            configuration
            
            .. attribute:: node_name  (key)
            
            	Node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            	**config**\: False
            
            .. attribute:: bundle_interfaces
            
            	QoS\-EA list of bundle interfaces
            	**type**\:  :py:class:`BundleInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces>`
            
            	**config**\: False
            
            .. attribute:: interfaces
            
            	QoS\-EA list of interfaces
            	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces>`
            
            	**config**\: False
            
            

            """

            _prefix = 'skp-qos-oper'
            _revision = '2016-02-18'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(PlatformQosEa.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("bundle-interfaces", ("bundle_interfaces", PlatformQosEa.Nodes.Node.BundleInterfaces)), ("interfaces", ("interfaces", PlatformQosEa.Nodes.Node.Interfaces))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.bundle_interfaces = PlatformQosEa.Nodes.Node.BundleInterfaces()
                self.bundle_interfaces.parent = self
                self._children_name_map["bundle_interfaces"] = "bundle-interfaces"

                self.interfaces = PlatformQosEa.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-skp-qos-oper:platform-qos-ea/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PlatformQosEa.Nodes.Node, ['node_name'], name, value)


            class BundleInterfaces(_Entity_):
                """
                QoS\-EA list of bundle interfaces
                
                .. attribute:: bundle_interface
                
                	QoS\-EA interface name
                	**type**\: list of  		 :py:class:`BundleInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface>`
                
                	**config**\: False
                
                

                """

                _prefix = 'skp-qos-oper'
                _revision = '2016-02-18'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(PlatformQosEa.Nodes.Node.BundleInterfaces, self).__init__()

                    self.yang_name = "bundle-interfaces"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("bundle-interface", ("bundle_interface", PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface))])
                    self._leafs = OrderedDict()

                    self.bundle_interface = YList(self)
                    self._segment_path = lambda: "bundle-interfaces"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PlatformQosEa.Nodes.Node.BundleInterfaces, [], name, value)


                class BundleInterface(_Entity_):
                    """
                    QoS\-EA interface name
                    
                    .. attribute:: interface_name  (key)
                    
                    	Bundle interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: member_interfaces
                    
                    	QoS\-EA list of member interfaces
                    	**type**\:  :py:class:`MemberInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'skp-qos-oper'
                    _revision = '2016-02-18'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface, self).__init__()

                        self.yang_name = "bundle-interface"
                        self.yang_parent_name = "bundle-interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([("member-interfaces", ("member_interfaces", PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ])
                        self.interface_name = None

                        self.member_interfaces = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces()
                        self.member_interfaces.parent = self
                        self._children_name_map["member_interfaces"] = "member-interfaces"
                        self._segment_path = lambda: "bundle-interface" + "[interface-name='" + str(self.interface_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface, ['interface_name'], name, value)


                    class MemberInterfaces(_Entity_):
                        """
                        QoS\-EA list of member interfaces
                        
                        .. attribute:: member_interface
                        
                        	QoS\-EA interface name
                        	**type**\: list of  		 :py:class:`MemberInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'skp-qos-oper'
                        _revision = '2016-02-18'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces, self).__init__()

                            self.yang_name = "member-interfaces"
                            self.yang_parent_name = "bundle-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("member-interface", ("member_interface", PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface))])
                            self._leafs = OrderedDict()

                            self.member_interface = YList(self)
                            self._segment_path = lambda: "member-interfaces"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces, [], name, value)


                        class MemberInterface(_Entity_):
                            """
                            QoS\-EA interface name
                            
                            .. attribute:: interface_name  (key)
                            
                            	Memeber interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            	**config**\: False
                            
                            .. attribute:: bundle_output
                            
                            	QoS\-EA policy direction output
                            	**type**\:  :py:class:`BundleOutput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput>`
                            
                            	**config**\: False
                            
                            .. attribute:: bundle_input
                            
                            	QoS\-EA policy direction input
                            	**type**\:  :py:class:`BundleInput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'skp-qos-oper'
                            _revision = '2016-02-18'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface, self).__init__()

                                self.yang_name = "member-interface"
                                self.yang_parent_name = "member-interfaces"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['interface_name']
                                self._child_classes = OrderedDict([("bundle-output", ("bundle_output", PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput)), ("bundle-input", ("bundle_input", PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput))])
                                self._leafs = OrderedDict([
                                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ])
                                self.interface_name = None

                                self.bundle_output = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput()
                                self.bundle_output.parent = self
                                self._children_name_map["bundle_output"] = "bundle-output"

                                self.bundle_input = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput()
                                self.bundle_input.parent = self
                                self._children_name_map["bundle_input"] = "bundle-input"
                                self._segment_path = lambda: "member-interface" + "[interface-name='" + str(self.interface_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface, ['interface_name'], name, value)


                            class BundleOutput(_Entity_):
                                """
                                QoS\-EA policy direction output
                                
                                .. attribute:: details
                                
                                	QoS\-EA policy details
                                	**type**\:  :py:class:`Details <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'skp-qos-oper'
                                _revision = '2016-02-18'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput, self).__init__()

                                    self.yang_name = "bundle-output"
                                    self.yang_parent_name = "member-interface"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("details", ("details", PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details))])
                                    self._leafs = OrderedDict()

                                    self.details = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details()
                                    self.details.parent = self
                                    self._children_name_map["details"] = "details"
                                    self._segment_path = lambda: "bundle-output"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput, [], name, value)


                                class Details(_Entity_):
                                    """
                                    QoS\-EA policy details
                                    
                                    .. attribute:: header
                                    
                                    	QoS EA policy header
                                    	**type**\:  :py:class:`Header <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.Header>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: interface_parameters
                                    
                                    	QoS EA Interface Parameters
                                    	**type**\:  :py:class:`InterfaceParameters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.InterfaceParameters>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: skywarp_qos_policy_class
                                    
                                    	Skywarp QoS EA policy class details
                                    	**type**\:  :py:class:`SkywarpQosPolicyClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'skp-qos-oper'
                                    _revision = '2016-02-18'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details, self).__init__()

                                        self.yang_name = "details"
                                        self.yang_parent_name = "bundle-output"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("header", ("header", PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.Header)), ("interface-parameters", ("interface_parameters", PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.InterfaceParameters)), ("skywarp-qos-policy-class", ("skywarp_qos_policy_class", PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass))])
                                        self._leafs = OrderedDict()

                                        self.header = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.Header()
                                        self.header.parent = self
                                        self._children_name_map["header"] = "header"

                                        self.interface_parameters = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.InterfaceParameters()
                                        self.interface_parameters.parent = self
                                        self._children_name_map["interface_parameters"] = "interface-parameters"

                                        self.skywarp_qos_policy_class = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass()
                                        self.skywarp_qos_policy_class.parent = self
                                        self._children_name_map["skywarp_qos_policy_class"] = "skywarp-qos-policy-class"
                                        self._segment_path = lambda: "details"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details, [], name, value)


                                    class Header(_Entity_):
                                        """
                                        QoS EA policy header
                                        
                                        .. attribute:: interface_name
                                        
                                        	Interface Name
                                        	**type**\: str
                                        
                                        	**length:** 0..101
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: policy_name
                                        
                                        	Policy name
                                        	**type**\: str
                                        
                                        	**length:** 0..65
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: direction
                                        
                                        	Direction
                                        	**type**\: str
                                        
                                        	**length:** 0..11
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: classes
                                        
                                        	Number of classes
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.Header, self).__init__()

                                            self.yang_name = "header"
                                            self.yang_parent_name = "details"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                                ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                                ('direction', (YLeaf(YType.str, 'direction'), ['str'])),
                                                ('classes', (YLeaf(YType.uint16, 'classes'), ['int'])),
                                            ])
                                            self.interface_name = None
                                            self.policy_name = None
                                            self.direction = None
                                            self.classes = None
                                            self._segment_path = lambda: "header"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.Header, ['interface_name', 'policy_name', 'direction', 'classes'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.Header']['meta_info']


                                    class InterfaceParameters(_Entity_):
                                        """
                                        QoS EA Interface Parameters
                                        
                                        .. attribute:: policy_name
                                        
                                        	Policy name
                                        	**type**\: str
                                        
                                        	**length:** 0..65
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: hierarchical_depth
                                        
                                        	Max Hierarchial Depth
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: interface_type
                                        
                                        	Interface Type
                                        	**type**\: str
                                        
                                        	**length:** 0..101
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: interface_rate
                                        
                                        	Interface Programmed Rate
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: port_shaper_rate
                                        
                                        	Port Shaper Rate
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: interface_handle
                                        
                                        	Interface Handle
                                        	**type**\: str
                                        
                                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: under_line_interface_handle
                                        
                                        	UnderLineInterface Handle
                                        	**type**\: str
                                        
                                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: bundle_id
                                        
                                        	Bundle Interface ID
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: uidb_index
                                        
                                        	UIDB Index
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: qos_interface_handle
                                        
                                        	QoS Interface handle
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: port
                                        
                                        	Local Port
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: policy_map_id
                                        
                                        	Policy Map ID
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.InterfaceParameters, self).__init__()

                                            self.yang_name = "interface-parameters"
                                            self.yang_parent_name = "details"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                                ('hierarchical_depth', (YLeaf(YType.uint8, 'hierarchical-depth'), ['int'])),
                                                ('interface_type', (YLeaf(YType.str, 'interface-type'), ['str'])),
                                                ('interface_rate', (YLeaf(YType.uint32, 'interface-rate'), ['int'])),
                                                ('port_shaper_rate', (YLeaf(YType.uint32, 'port-shaper-rate'), ['int'])),
                                                ('interface_handle', (YLeaf(YType.str, 'interface-handle'), ['str'])),
                                                ('under_line_interface_handle', (YLeaf(YType.str, 'under-line-interface-handle'), ['str'])),
                                                ('bundle_id', (YLeaf(YType.uint16, 'bundle-id'), ['int'])),
                                                ('uidb_index', (YLeaf(YType.uint16, 'uidb-index'), ['int'])),
                                                ('qos_interface_handle', (YLeaf(YType.uint64, 'qos-interface-handle'), ['int'])),
                                                ('port', (YLeaf(YType.uint32, 'port'), ['int'])),
                                                ('policy_map_id', (YLeaf(YType.uint16, 'policy-map-id'), ['int'])),
                                            ])
                                            self.policy_name = None
                                            self.hierarchical_depth = None
                                            self.interface_type = None
                                            self.interface_rate = None
                                            self.port_shaper_rate = None
                                            self.interface_handle = None
                                            self.under_line_interface_handle = None
                                            self.bundle_id = None
                                            self.uidb_index = None
                                            self.qos_interface_handle = None
                                            self.port = None
                                            self.policy_map_id = None
                                            self._segment_path = lambda: "interface-parameters"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.InterfaceParameters, ['policy_name', 'hierarchical_depth', 'interface_type', 'interface_rate', 'port_shaper_rate', 'interface_handle', 'under_line_interface_handle', 'bundle_id', 'uidb_index', 'qos_interface_handle', 'port', 'policy_map_id'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.InterfaceParameters']['meta_info']


                                    class SkywarpQosPolicyClass(_Entity_):
                                        """
                                        Skywarp QoS EA policy class details
                                        
                                        .. attribute:: qos_show_ea_pclass_st
                                        
                                        	qos show ea pclass st
                                        	**type**\: list of  		 :py:class:`QosShowEaPclassSt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass, self).__init__()

                                            self.yang_name = "skywarp-qos-policy-class"
                                            self.yang_parent_name = "details"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("qos-show-ea-pclass-st", ("qos_show_ea_pclass_st", PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt))])
                                            self._leafs = OrderedDict()

                                            self.qos_show_ea_pclass_st = YList(self)
                                            self._segment_path = lambda: "skywarp-qos-policy-class"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass, [], name, value)


                                        class QosShowEaPclassSt(_Entity_):
                                            """
                                            qos show ea pclass st
                                            
                                            .. attribute:: config
                                            
                                            	QoS EA Class Configuration
                                            	**type**\:  :py:class:`Config <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: result
                                            
                                            	QoS EA Class Result
                                            	**type**\:  :py:class:`Result <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: index
                                            
                                            	Class Index
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: class_level
                                            
                                            	Class level
                                            	**type**\: int
                                            
                                            	**range:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: class_name
                                            
                                            	Class name
                                            	**type**\: str
                                            
                                            	**length:** 0..65
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: policy_name
                                            
                                            	Policy name
                                            	**type**\: str
                                            
                                            	**length:** 0..65
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: node_flags
                                            
                                            	Node Flags
                                            	**type**\: str
                                            
                                            	**length:** 0..101
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: stats_flags
                                            
                                            	Statistical Flags
                                            	**type**\: str
                                            
                                            	**length:** 0..101
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt, self).__init__()

                                                self.yang_name = "qos-show-ea-pclass-st"
                                                self.yang_parent_name = "skywarp-qos-policy-class"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("config", ("config", PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config)), ("result", ("result", PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result))])
                                                self._leafs = OrderedDict([
                                                    ('index', (YLeaf(YType.uint16, 'index'), ['int'])),
                                                    ('class_level', (YLeaf(YType.uint8, 'class-level'), ['int'])),
                                                    ('class_name', (YLeaf(YType.str, 'class-name'), ['str'])),
                                                    ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                                    ('node_flags', (YLeaf(YType.str, 'node-flags'), ['str'])),
                                                    ('stats_flags', (YLeaf(YType.str, 'stats-flags'), ['str'])),
                                                ])
                                                self.index = None
                                                self.class_level = None
                                                self.class_name = None
                                                self.policy_name = None
                                                self.node_flags = None
                                                self.stats_flags = None

                                                self.config = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config()
                                                self.config.parent = self
                                                self._children_name_map["config"] = "config"

                                                self.result = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result()
                                                self.result.parent = self
                                                self._children_name_map["result"] = "result"
                                                self._segment_path = lambda: "qos-show-ea-pclass-st"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt, ['index', 'class_level', 'class_name', 'policy_name', 'node_flags', 'stats_flags'], name, value)


                                            class Config(_Entity_):
                                                """
                                                QoS EA Class Configuration
                                                
                                                .. attribute:: police
                                                
                                                	QoS EA Policer parameters
                                                	**type**\:  :py:class:`Police <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: shape
                                                
                                                	QoS EA Shaper parameters
                                                	**type**\:  :py:class:`Shape <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: wfq
                                                
                                                	QoS EA WFQ parameters
                                                	**type**\:  :py:class:`Wfq <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: node_config
                                                
                                                	Node Config
                                                	**type**\: str
                                                
                                                	**length:** 0..101
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config, self).__init__()

                                                    self.yang_name = "config"
                                                    self.yang_parent_name = "qos-show-ea-pclass-st"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("police", ("police", PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police)), ("shape", ("shape", PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape)), ("wfq", ("wfq", PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq))])
                                                    self._leafs = OrderedDict([
                                                        ('node_config', (YLeaf(YType.str, 'node-config'), ['str'])),
                                                    ])
                                                    self.node_config = None

                                                    self.police = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police()
                                                    self.police.parent = self
                                                    self._children_name_map["police"] = "police"

                                                    self.shape = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape()
                                                    self.shape.parent = self
                                                    self._children_name_map["shape"] = "shape"

                                                    self.wfq = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq()
                                                    self.wfq.parent = self
                                                    self._children_name_map["wfq"] = "wfq"
                                                    self._segment_path = lambda: "config"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config, ['node_config'], name, value)


                                                class Police(_Entity_):
                                                    """
                                                    QoS EA Policer parameters
                                                    
                                                    .. attribute:: cir
                                                    
                                                    	CIR
                                                    	**type**\:  :py:class:`Cir <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir>`
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: cbs
                                                    
                                                    	CBS
                                                    	**type**\:  :py:class:`Cbs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs>`
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: color_aware
                                                    
                                                    	Color Aware
                                                    	**type**\: bool
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: policer_type
                                                    
                                                    	Policer type
                                                    	**type**\:  :py:class:`TbAlgorithm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.TbAlgorithm>`
                                                    
                                                    	**config**\: False
                                                    
                                                    

                                                    """

                                                    _prefix = 'skp-qos-oper'
                                                    _revision = '2016-02-18'

                                                    def __init__(self):
                                                        if sys.version_info > (3,):
                                                            super().__init__()
                                                        else:
                                                            super(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police, self).__init__()

                                                        self.yang_name = "police"
                                                        self.yang_parent_name = "config"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([("cir", ("cir", PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir)), ("cbs", ("cbs", PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs))])
                                                        self._leafs = OrderedDict([
                                                            ('color_aware', (YLeaf(YType.boolean, 'color-aware'), ['bool'])),
                                                            ('policer_type', (YLeaf(YType.enumeration, 'policer-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'TbAlgorithm', '')])),
                                                        ])
                                                        self.color_aware = None
                                                        self.policer_type = None

                                                        self.cir = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir()
                                                        self.cir.parent = self
                                                        self._children_name_map["cir"] = "cir"

                                                        self.cbs = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs()
                                                        self.cbs.parent = self
                                                        self._children_name_map["cbs"] = "cbs"
                                                        self._segment_path = lambda: "police"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police, ['color_aware', 'policer_type'], name, value)


                                                    class Cir(_Entity_):
                                                        """
                                                        CIR
                                                        
                                                        .. attribute:: value
                                                        
                                                        	Config value
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: unit
                                                        
                                                        	Config unit
                                                        	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                                        
                                                        	**config**\: False
                                                        
                                                        

                                                        """

                                                        _prefix = 'skp-qos-oper'
                                                        _revision = '2016-02-18'

                                                        def __init__(self):
                                                            if sys.version_info > (3,):
                                                                super().__init__()
                                                            else:
                                                                super(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir, self).__init__()

                                                            self.yang_name = "cir"
                                                            self.yang_parent_name = "police"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                                ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                                            ])
                                                            self.value = None
                                                            self.unit = None
                                                            self._segment_path = lambda: "cir"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir, ['value', 'unit'], name, value)

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                            return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir']['meta_info']


                                                    class Cbs(_Entity_):
                                                        """
                                                        CBS
                                                        
                                                        .. attribute:: value
                                                        
                                                        	Config value
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: unit
                                                        
                                                        	Config unit
                                                        	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                                        
                                                        	**config**\: False
                                                        
                                                        

                                                        """

                                                        _prefix = 'skp-qos-oper'
                                                        _revision = '2016-02-18'

                                                        def __init__(self):
                                                            if sys.version_info > (3,):
                                                                super().__init__()
                                                            else:
                                                                super(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs, self).__init__()

                                                            self.yang_name = "cbs"
                                                            self.yang_parent_name = "police"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                                ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                                            ])
                                                            self.value = None
                                                            self.unit = None
                                                            self._segment_path = lambda: "cbs"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs, ['value', 'unit'], name, value)

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                            return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs']['meta_info']

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                        return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police']['meta_info']


                                                class Shape(_Entity_):
                                                    """
                                                    QoS EA Shaper parameters
                                                    
                                                    .. attribute:: pir
                                                    
                                                    	PIR in kbps
                                                    	**type**\:  :py:class:`Pir <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir>`
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: pbs
                                                    
                                                    	PBS in bytes
                                                    	**type**\:  :py:class:`Pbs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs>`
                                                    
                                                    	**config**\: False
                                                    
                                                    

                                                    """

                                                    _prefix = 'skp-qos-oper'
                                                    _revision = '2016-02-18'

                                                    def __init__(self):
                                                        if sys.version_info > (3,):
                                                            super().__init__()
                                                        else:
                                                            super(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape, self).__init__()

                                                        self.yang_name = "shape"
                                                        self.yang_parent_name = "config"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([("pir", ("pir", PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir)), ("pbs", ("pbs", PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs))])
                                                        self._leafs = OrderedDict()

                                                        self.pir = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir()
                                                        self.pir.parent = self
                                                        self._children_name_map["pir"] = "pir"

                                                        self.pbs = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs()
                                                        self.pbs.parent = self
                                                        self._children_name_map["pbs"] = "pbs"
                                                        self._segment_path = lambda: "shape"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape, [], name, value)


                                                    class Pir(_Entity_):
                                                        """
                                                        PIR in kbps
                                                        
                                                        .. attribute:: value
                                                        
                                                        	Config value
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: unit
                                                        
                                                        	Config unit
                                                        	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                                        
                                                        	**config**\: False
                                                        
                                                        

                                                        """

                                                        _prefix = 'skp-qos-oper'
                                                        _revision = '2016-02-18'

                                                        def __init__(self):
                                                            if sys.version_info > (3,):
                                                                super().__init__()
                                                            else:
                                                                super(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir, self).__init__()

                                                            self.yang_name = "pir"
                                                            self.yang_parent_name = "shape"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                                ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                                            ])
                                                            self.value = None
                                                            self.unit = None
                                                            self._segment_path = lambda: "pir"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir, ['value', 'unit'], name, value)

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                            return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir']['meta_info']


                                                    class Pbs(_Entity_):
                                                        """
                                                        PBS in bytes
                                                        
                                                        .. attribute:: value
                                                        
                                                        	Config value
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: unit
                                                        
                                                        	Config unit
                                                        	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                                        
                                                        	**config**\: False
                                                        
                                                        

                                                        """

                                                        _prefix = 'skp-qos-oper'
                                                        _revision = '2016-02-18'

                                                        def __init__(self):
                                                            if sys.version_info > (3,):
                                                                super().__init__()
                                                            else:
                                                                super(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs, self).__init__()

                                                            self.yang_name = "pbs"
                                                            self.yang_parent_name = "shape"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                                ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                                            ])
                                                            self.value = None
                                                            self.unit = None
                                                            self._segment_path = lambda: "pbs"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs, ['value', 'unit'], name, value)

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                            return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs']['meta_info']

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                        return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape']['meta_info']


                                                class Wfq(_Entity_):
                                                    """
                                                    QoS EA WFQ parameters
                                                    
                                                    .. attribute:: bandwidth
                                                    
                                                    	Bandwidth
                                                    	**type**\:  :py:class:`Bandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth>`
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: sum_of_bandwidth
                                                    
                                                    	Sum of Bandwidth
                                                    	**type**\:  :py:class:`SumOfBandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth>`
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: excess_ratio
                                                    
                                                    	Excess Ratio
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..65535
                                                    
                                                    	**config**\: False
                                                    
                                                    

                                                    """

                                                    _prefix = 'skp-qos-oper'
                                                    _revision = '2016-02-18'

                                                    def __init__(self):
                                                        if sys.version_info > (3,):
                                                            super().__init__()
                                                        else:
                                                            super(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq, self).__init__()

                                                        self.yang_name = "wfq"
                                                        self.yang_parent_name = "config"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([("bandwidth", ("bandwidth", PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth)), ("sum-of-bandwidth", ("sum_of_bandwidth", PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth))])
                                                        self._leafs = OrderedDict([
                                                            ('excess_ratio', (YLeaf(YType.uint16, 'excess-ratio'), ['int'])),
                                                        ])
                                                        self.excess_ratio = None

                                                        self.bandwidth = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth()
                                                        self.bandwidth.parent = self
                                                        self._children_name_map["bandwidth"] = "bandwidth"

                                                        self.sum_of_bandwidth = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth()
                                                        self.sum_of_bandwidth.parent = self
                                                        self._children_name_map["sum_of_bandwidth"] = "sum-of-bandwidth"
                                                        self._segment_path = lambda: "wfq"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq, ['excess_ratio'], name, value)


                                                    class Bandwidth(_Entity_):
                                                        """
                                                        Bandwidth
                                                        
                                                        .. attribute:: value
                                                        
                                                        	Config value
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: unit
                                                        
                                                        	Config unit
                                                        	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                                        
                                                        	**config**\: False
                                                        
                                                        

                                                        """

                                                        _prefix = 'skp-qos-oper'
                                                        _revision = '2016-02-18'

                                                        def __init__(self):
                                                            if sys.version_info > (3,):
                                                                super().__init__()
                                                            else:
                                                                super(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth, self).__init__()

                                                            self.yang_name = "bandwidth"
                                                            self.yang_parent_name = "wfq"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                                ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                                            ])
                                                            self.value = None
                                                            self.unit = None
                                                            self._segment_path = lambda: "bandwidth"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth, ['value', 'unit'], name, value)

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                            return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth']['meta_info']


                                                    class SumOfBandwidth(_Entity_):
                                                        """
                                                        Sum of Bandwidth
                                                        
                                                        .. attribute:: value
                                                        
                                                        	Config value
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: unit
                                                        
                                                        	Config unit
                                                        	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                                        
                                                        	**config**\: False
                                                        
                                                        

                                                        """

                                                        _prefix = 'skp-qos-oper'
                                                        _revision = '2016-02-18'

                                                        def __init__(self):
                                                            if sys.version_info > (3,):
                                                                super().__init__()
                                                            else:
                                                                super(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth, self).__init__()

                                                            self.yang_name = "sum-of-bandwidth"
                                                            self.yang_parent_name = "wfq"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                                ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                                            ])
                                                            self.value = None
                                                            self.unit = None
                                                            self._segment_path = lambda: "sum-of-bandwidth"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth, ['value', 'unit'], name, value)

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                            return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth']['meta_info']

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                        return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq']['meta_info']

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config']['meta_info']


                                            class Result(_Entity_):
                                                """
                                                QoS EA Class Result
                                                
                                                .. attribute:: queue
                                                
                                                	QoS EA Queue Result
                                                	**type**\:  :py:class:`Queue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: police
                                                
                                                	QoS EA Policer Result
                                                	**type**\:  :py:class:`Police <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: stats_id
                                                
                                                	Stats ID
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result, self).__init__()

                                                    self.yang_name = "result"
                                                    self.yang_parent_name = "qos-show-ea-pclass-st"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("queue", ("queue", PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue)), ("police", ("police", PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police))])
                                                    self._leafs = OrderedDict([
                                                        ('stats_id', (YLeaf(YType.uint32, 'stats-id'), ['int'])),
                                                    ])
                                                    self.stats_id = None

                                                    self.queue = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue()
                                                    self.queue.parent = self
                                                    self._children_name_map["queue"] = "queue"

                                                    self.police = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police()
                                                    self.police.parent = self
                                                    self._children_name_map["police"] = "police"
                                                    self._segment_path = lambda: "result"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result, ['stats_id'], name, value)


                                                class Queue(_Entity_):
                                                    """
                                                    QoS EA Queue Result
                                                    
                                                    .. attribute:: queue_id
                                                    
                                                    	Queue ID
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: commit_tx
                                                    
                                                    	Commit Tx
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: excess_tx
                                                    
                                                    	Excess Tx
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: drop
                                                    
                                                    	Drop
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    	**config**\: False
                                                    
                                                    

                                                    """

                                                    _prefix = 'skp-qos-oper'
                                                    _revision = '2016-02-18'

                                                    def __init__(self):
                                                        if sys.version_info > (3,):
                                                            super().__init__()
                                                        else:
                                                            super(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue, self).__init__()

                                                        self.yang_name = "queue"
                                                        self.yang_parent_name = "result"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('queue_id', (YLeaf(YType.uint32, 'queue-id'), ['int'])),
                                                            ('commit_tx', (YLeaf(YType.uint32, 'commit-tx'), ['int'])),
                                                            ('excess_tx', (YLeaf(YType.uint32, 'excess-tx'), ['int'])),
                                                            ('drop', (YLeaf(YType.uint32, 'drop'), ['int'])),
                                                        ])
                                                        self.queue_id = None
                                                        self.commit_tx = None
                                                        self.excess_tx = None
                                                        self.drop = None
                                                        self._segment_path = lambda: "queue"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue, ['queue_id', 'commit_tx', 'excess_tx', 'drop'], name, value)

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                        return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue']['meta_info']


                                                class Police(_Entity_):
                                                    """
                                                    QoS EA Policer Result
                                                    
                                                    .. attribute:: token_bucket_id
                                                    
                                                    	Token Bucket ID
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: conform
                                                    
                                                    	Conform Rate
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: exceed
                                                    
                                                    	Exceed Rate
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: violate
                                                    
                                                    	Violate Rate
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    	**config**\: False
                                                    
                                                    

                                                    """

                                                    _prefix = 'skp-qos-oper'
                                                    _revision = '2016-02-18'

                                                    def __init__(self):
                                                        if sys.version_info > (3,):
                                                            super().__init__()
                                                        else:
                                                            super(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police, self).__init__()

                                                        self.yang_name = "police"
                                                        self.yang_parent_name = "result"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('token_bucket_id', (YLeaf(YType.uint32, 'token-bucket-id'), ['int'])),
                                                            ('conform', (YLeaf(YType.uint32, 'conform'), ['int'])),
                                                            ('exceed', (YLeaf(YType.uint32, 'exceed'), ['int'])),
                                                            ('violate', (YLeaf(YType.uint32, 'violate'), ['int'])),
                                                        ])
                                                        self.token_bucket_id = None
                                                        self.conform = None
                                                        self.exceed = None
                                                        self.violate = None
                                                        self._segment_path = lambda: "police"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police, ['token_bucket_id', 'conform', 'exceed', 'violate'], name, value)

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                        return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police']['meta_info']

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result']['meta_info']

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details.SkywarpQosPolicyClass']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                        return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput.Details']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                    return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleOutput']['meta_info']


                            class BundleInput(_Entity_):
                                """
                                QoS\-EA policy direction input
                                
                                .. attribute:: details
                                
                                	QoS\-EA policy details
                                	**type**\:  :py:class:`Details <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'skp-qos-oper'
                                _revision = '2016-02-18'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput, self).__init__()

                                    self.yang_name = "bundle-input"
                                    self.yang_parent_name = "member-interface"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("details", ("details", PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details))])
                                    self._leafs = OrderedDict()

                                    self.details = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details()
                                    self.details.parent = self
                                    self._children_name_map["details"] = "details"
                                    self._segment_path = lambda: "bundle-input"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput, [], name, value)


                                class Details(_Entity_):
                                    """
                                    QoS\-EA policy details
                                    
                                    .. attribute:: header
                                    
                                    	QoS EA policy header
                                    	**type**\:  :py:class:`Header <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.Header>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: interface_parameters
                                    
                                    	QoS EA Interface Parameters
                                    	**type**\:  :py:class:`InterfaceParameters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.InterfaceParameters>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: skywarp_qos_policy_class
                                    
                                    	Skywarp QoS EA policy class details
                                    	**type**\:  :py:class:`SkywarpQosPolicyClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'skp-qos-oper'
                                    _revision = '2016-02-18'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details, self).__init__()

                                        self.yang_name = "details"
                                        self.yang_parent_name = "bundle-input"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("header", ("header", PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.Header)), ("interface-parameters", ("interface_parameters", PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.InterfaceParameters)), ("skywarp-qos-policy-class", ("skywarp_qos_policy_class", PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass))])
                                        self._leafs = OrderedDict()

                                        self.header = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.Header()
                                        self.header.parent = self
                                        self._children_name_map["header"] = "header"

                                        self.interface_parameters = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.InterfaceParameters()
                                        self.interface_parameters.parent = self
                                        self._children_name_map["interface_parameters"] = "interface-parameters"

                                        self.skywarp_qos_policy_class = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass()
                                        self.skywarp_qos_policy_class.parent = self
                                        self._children_name_map["skywarp_qos_policy_class"] = "skywarp-qos-policy-class"
                                        self._segment_path = lambda: "details"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details, [], name, value)


                                    class Header(_Entity_):
                                        """
                                        QoS EA policy header
                                        
                                        .. attribute:: interface_name
                                        
                                        	Interface Name
                                        	**type**\: str
                                        
                                        	**length:** 0..101
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: policy_name
                                        
                                        	Policy name
                                        	**type**\: str
                                        
                                        	**length:** 0..65
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: direction
                                        
                                        	Direction
                                        	**type**\: str
                                        
                                        	**length:** 0..11
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: classes
                                        
                                        	Number of classes
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.Header, self).__init__()

                                            self.yang_name = "header"
                                            self.yang_parent_name = "details"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                                ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                                ('direction', (YLeaf(YType.str, 'direction'), ['str'])),
                                                ('classes', (YLeaf(YType.uint16, 'classes'), ['int'])),
                                            ])
                                            self.interface_name = None
                                            self.policy_name = None
                                            self.direction = None
                                            self.classes = None
                                            self._segment_path = lambda: "header"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.Header, ['interface_name', 'policy_name', 'direction', 'classes'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.Header']['meta_info']


                                    class InterfaceParameters(_Entity_):
                                        """
                                        QoS EA Interface Parameters
                                        
                                        .. attribute:: policy_name
                                        
                                        	Policy name
                                        	**type**\: str
                                        
                                        	**length:** 0..65
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: hierarchical_depth
                                        
                                        	Max Hierarchial Depth
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: interface_type
                                        
                                        	Interface Type
                                        	**type**\: str
                                        
                                        	**length:** 0..101
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: interface_rate
                                        
                                        	Interface Programmed Rate
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: port_shaper_rate
                                        
                                        	Port Shaper Rate
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: interface_handle
                                        
                                        	Interface Handle
                                        	**type**\: str
                                        
                                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: under_line_interface_handle
                                        
                                        	UnderLineInterface Handle
                                        	**type**\: str
                                        
                                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: bundle_id
                                        
                                        	Bundle Interface ID
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: uidb_index
                                        
                                        	UIDB Index
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: qos_interface_handle
                                        
                                        	QoS Interface handle
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: port
                                        
                                        	Local Port
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: policy_map_id
                                        
                                        	Policy Map ID
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.InterfaceParameters, self).__init__()

                                            self.yang_name = "interface-parameters"
                                            self.yang_parent_name = "details"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                                ('hierarchical_depth', (YLeaf(YType.uint8, 'hierarchical-depth'), ['int'])),
                                                ('interface_type', (YLeaf(YType.str, 'interface-type'), ['str'])),
                                                ('interface_rate', (YLeaf(YType.uint32, 'interface-rate'), ['int'])),
                                                ('port_shaper_rate', (YLeaf(YType.uint32, 'port-shaper-rate'), ['int'])),
                                                ('interface_handle', (YLeaf(YType.str, 'interface-handle'), ['str'])),
                                                ('under_line_interface_handle', (YLeaf(YType.str, 'under-line-interface-handle'), ['str'])),
                                                ('bundle_id', (YLeaf(YType.uint16, 'bundle-id'), ['int'])),
                                                ('uidb_index', (YLeaf(YType.uint16, 'uidb-index'), ['int'])),
                                                ('qos_interface_handle', (YLeaf(YType.uint64, 'qos-interface-handle'), ['int'])),
                                                ('port', (YLeaf(YType.uint32, 'port'), ['int'])),
                                                ('policy_map_id', (YLeaf(YType.uint16, 'policy-map-id'), ['int'])),
                                            ])
                                            self.policy_name = None
                                            self.hierarchical_depth = None
                                            self.interface_type = None
                                            self.interface_rate = None
                                            self.port_shaper_rate = None
                                            self.interface_handle = None
                                            self.under_line_interface_handle = None
                                            self.bundle_id = None
                                            self.uidb_index = None
                                            self.qos_interface_handle = None
                                            self.port = None
                                            self.policy_map_id = None
                                            self._segment_path = lambda: "interface-parameters"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.InterfaceParameters, ['policy_name', 'hierarchical_depth', 'interface_type', 'interface_rate', 'port_shaper_rate', 'interface_handle', 'under_line_interface_handle', 'bundle_id', 'uidb_index', 'qos_interface_handle', 'port', 'policy_map_id'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.InterfaceParameters']['meta_info']


                                    class SkywarpQosPolicyClass(_Entity_):
                                        """
                                        Skywarp QoS EA policy class details
                                        
                                        .. attribute:: qos_show_ea_pclass_st
                                        
                                        	qos show ea pclass st
                                        	**type**\: list of  		 :py:class:`QosShowEaPclassSt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass, self).__init__()

                                            self.yang_name = "skywarp-qos-policy-class"
                                            self.yang_parent_name = "details"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("qos-show-ea-pclass-st", ("qos_show_ea_pclass_st", PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt))])
                                            self._leafs = OrderedDict()

                                            self.qos_show_ea_pclass_st = YList(self)
                                            self._segment_path = lambda: "skywarp-qos-policy-class"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass, [], name, value)


                                        class QosShowEaPclassSt(_Entity_):
                                            """
                                            qos show ea pclass st
                                            
                                            .. attribute:: config
                                            
                                            	QoS EA Class Configuration
                                            	**type**\:  :py:class:`Config <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: result
                                            
                                            	QoS EA Class Result
                                            	**type**\:  :py:class:`Result <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: index
                                            
                                            	Class Index
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: class_level
                                            
                                            	Class level
                                            	**type**\: int
                                            
                                            	**range:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: class_name
                                            
                                            	Class name
                                            	**type**\: str
                                            
                                            	**length:** 0..65
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: policy_name
                                            
                                            	Policy name
                                            	**type**\: str
                                            
                                            	**length:** 0..65
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: node_flags
                                            
                                            	Node Flags
                                            	**type**\: str
                                            
                                            	**length:** 0..101
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: stats_flags
                                            
                                            	Statistical Flags
                                            	**type**\: str
                                            
                                            	**length:** 0..101
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt, self).__init__()

                                                self.yang_name = "qos-show-ea-pclass-st"
                                                self.yang_parent_name = "skywarp-qos-policy-class"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("config", ("config", PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config)), ("result", ("result", PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result))])
                                                self._leafs = OrderedDict([
                                                    ('index', (YLeaf(YType.uint16, 'index'), ['int'])),
                                                    ('class_level', (YLeaf(YType.uint8, 'class-level'), ['int'])),
                                                    ('class_name', (YLeaf(YType.str, 'class-name'), ['str'])),
                                                    ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                                    ('node_flags', (YLeaf(YType.str, 'node-flags'), ['str'])),
                                                    ('stats_flags', (YLeaf(YType.str, 'stats-flags'), ['str'])),
                                                ])
                                                self.index = None
                                                self.class_level = None
                                                self.class_name = None
                                                self.policy_name = None
                                                self.node_flags = None
                                                self.stats_flags = None

                                                self.config = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config()
                                                self.config.parent = self
                                                self._children_name_map["config"] = "config"

                                                self.result = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result()
                                                self.result.parent = self
                                                self._children_name_map["result"] = "result"
                                                self._segment_path = lambda: "qos-show-ea-pclass-st"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt, ['index', 'class_level', 'class_name', 'policy_name', 'node_flags', 'stats_flags'], name, value)


                                            class Config(_Entity_):
                                                """
                                                QoS EA Class Configuration
                                                
                                                .. attribute:: police
                                                
                                                	QoS EA Policer parameters
                                                	**type**\:  :py:class:`Police <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: shape
                                                
                                                	QoS EA Shaper parameters
                                                	**type**\:  :py:class:`Shape <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: wfq
                                                
                                                	QoS EA WFQ parameters
                                                	**type**\:  :py:class:`Wfq <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: node_config
                                                
                                                	Node Config
                                                	**type**\: str
                                                
                                                	**length:** 0..101
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config, self).__init__()

                                                    self.yang_name = "config"
                                                    self.yang_parent_name = "qos-show-ea-pclass-st"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("police", ("police", PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police)), ("shape", ("shape", PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape)), ("wfq", ("wfq", PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq))])
                                                    self._leafs = OrderedDict([
                                                        ('node_config', (YLeaf(YType.str, 'node-config'), ['str'])),
                                                    ])
                                                    self.node_config = None

                                                    self.police = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police()
                                                    self.police.parent = self
                                                    self._children_name_map["police"] = "police"

                                                    self.shape = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape()
                                                    self.shape.parent = self
                                                    self._children_name_map["shape"] = "shape"

                                                    self.wfq = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq()
                                                    self.wfq.parent = self
                                                    self._children_name_map["wfq"] = "wfq"
                                                    self._segment_path = lambda: "config"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config, ['node_config'], name, value)


                                                class Police(_Entity_):
                                                    """
                                                    QoS EA Policer parameters
                                                    
                                                    .. attribute:: cir
                                                    
                                                    	CIR
                                                    	**type**\:  :py:class:`Cir <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir>`
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: cbs
                                                    
                                                    	CBS
                                                    	**type**\:  :py:class:`Cbs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs>`
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: color_aware
                                                    
                                                    	Color Aware
                                                    	**type**\: bool
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: policer_type
                                                    
                                                    	Policer type
                                                    	**type**\:  :py:class:`TbAlgorithm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.TbAlgorithm>`
                                                    
                                                    	**config**\: False
                                                    
                                                    

                                                    """

                                                    _prefix = 'skp-qos-oper'
                                                    _revision = '2016-02-18'

                                                    def __init__(self):
                                                        if sys.version_info > (3,):
                                                            super().__init__()
                                                        else:
                                                            super(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police, self).__init__()

                                                        self.yang_name = "police"
                                                        self.yang_parent_name = "config"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([("cir", ("cir", PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir)), ("cbs", ("cbs", PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs))])
                                                        self._leafs = OrderedDict([
                                                            ('color_aware', (YLeaf(YType.boolean, 'color-aware'), ['bool'])),
                                                            ('policer_type', (YLeaf(YType.enumeration, 'policer-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'TbAlgorithm', '')])),
                                                        ])
                                                        self.color_aware = None
                                                        self.policer_type = None

                                                        self.cir = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir()
                                                        self.cir.parent = self
                                                        self._children_name_map["cir"] = "cir"

                                                        self.cbs = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs()
                                                        self.cbs.parent = self
                                                        self._children_name_map["cbs"] = "cbs"
                                                        self._segment_path = lambda: "police"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police, ['color_aware', 'policer_type'], name, value)


                                                    class Cir(_Entity_):
                                                        """
                                                        CIR
                                                        
                                                        .. attribute:: value
                                                        
                                                        	Config value
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: unit
                                                        
                                                        	Config unit
                                                        	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                                        
                                                        	**config**\: False
                                                        
                                                        

                                                        """

                                                        _prefix = 'skp-qos-oper'
                                                        _revision = '2016-02-18'

                                                        def __init__(self):
                                                            if sys.version_info > (3,):
                                                                super().__init__()
                                                            else:
                                                                super(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir, self).__init__()

                                                            self.yang_name = "cir"
                                                            self.yang_parent_name = "police"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                                ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                                            ])
                                                            self.value = None
                                                            self.unit = None
                                                            self._segment_path = lambda: "cir"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir, ['value', 'unit'], name, value)

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                            return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir']['meta_info']


                                                    class Cbs(_Entity_):
                                                        """
                                                        CBS
                                                        
                                                        .. attribute:: value
                                                        
                                                        	Config value
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: unit
                                                        
                                                        	Config unit
                                                        	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                                        
                                                        	**config**\: False
                                                        
                                                        

                                                        """

                                                        _prefix = 'skp-qos-oper'
                                                        _revision = '2016-02-18'

                                                        def __init__(self):
                                                            if sys.version_info > (3,):
                                                                super().__init__()
                                                            else:
                                                                super(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs, self).__init__()

                                                            self.yang_name = "cbs"
                                                            self.yang_parent_name = "police"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                                ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                                            ])
                                                            self.value = None
                                                            self.unit = None
                                                            self._segment_path = lambda: "cbs"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs, ['value', 'unit'], name, value)

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                            return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs']['meta_info']

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                        return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police']['meta_info']


                                                class Shape(_Entity_):
                                                    """
                                                    QoS EA Shaper parameters
                                                    
                                                    .. attribute:: pir
                                                    
                                                    	PIR in kbps
                                                    	**type**\:  :py:class:`Pir <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir>`
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: pbs
                                                    
                                                    	PBS in bytes
                                                    	**type**\:  :py:class:`Pbs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs>`
                                                    
                                                    	**config**\: False
                                                    
                                                    

                                                    """

                                                    _prefix = 'skp-qos-oper'
                                                    _revision = '2016-02-18'

                                                    def __init__(self):
                                                        if sys.version_info > (3,):
                                                            super().__init__()
                                                        else:
                                                            super(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape, self).__init__()

                                                        self.yang_name = "shape"
                                                        self.yang_parent_name = "config"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([("pir", ("pir", PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir)), ("pbs", ("pbs", PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs))])
                                                        self._leafs = OrderedDict()

                                                        self.pir = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir()
                                                        self.pir.parent = self
                                                        self._children_name_map["pir"] = "pir"

                                                        self.pbs = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs()
                                                        self.pbs.parent = self
                                                        self._children_name_map["pbs"] = "pbs"
                                                        self._segment_path = lambda: "shape"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape, [], name, value)


                                                    class Pir(_Entity_):
                                                        """
                                                        PIR in kbps
                                                        
                                                        .. attribute:: value
                                                        
                                                        	Config value
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: unit
                                                        
                                                        	Config unit
                                                        	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                                        
                                                        	**config**\: False
                                                        
                                                        

                                                        """

                                                        _prefix = 'skp-qos-oper'
                                                        _revision = '2016-02-18'

                                                        def __init__(self):
                                                            if sys.version_info > (3,):
                                                                super().__init__()
                                                            else:
                                                                super(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir, self).__init__()

                                                            self.yang_name = "pir"
                                                            self.yang_parent_name = "shape"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                                ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                                            ])
                                                            self.value = None
                                                            self.unit = None
                                                            self._segment_path = lambda: "pir"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir, ['value', 'unit'], name, value)

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                            return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir']['meta_info']


                                                    class Pbs(_Entity_):
                                                        """
                                                        PBS in bytes
                                                        
                                                        .. attribute:: value
                                                        
                                                        	Config value
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: unit
                                                        
                                                        	Config unit
                                                        	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                                        
                                                        	**config**\: False
                                                        
                                                        

                                                        """

                                                        _prefix = 'skp-qos-oper'
                                                        _revision = '2016-02-18'

                                                        def __init__(self):
                                                            if sys.version_info > (3,):
                                                                super().__init__()
                                                            else:
                                                                super(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs, self).__init__()

                                                            self.yang_name = "pbs"
                                                            self.yang_parent_name = "shape"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                                ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                                            ])
                                                            self.value = None
                                                            self.unit = None
                                                            self._segment_path = lambda: "pbs"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs, ['value', 'unit'], name, value)

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                            return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs']['meta_info']

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                        return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape']['meta_info']


                                                class Wfq(_Entity_):
                                                    """
                                                    QoS EA WFQ parameters
                                                    
                                                    .. attribute:: bandwidth
                                                    
                                                    	Bandwidth
                                                    	**type**\:  :py:class:`Bandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth>`
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: sum_of_bandwidth
                                                    
                                                    	Sum of Bandwidth
                                                    	**type**\:  :py:class:`SumOfBandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth>`
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: excess_ratio
                                                    
                                                    	Excess Ratio
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..65535
                                                    
                                                    	**config**\: False
                                                    
                                                    

                                                    """

                                                    _prefix = 'skp-qos-oper'
                                                    _revision = '2016-02-18'

                                                    def __init__(self):
                                                        if sys.version_info > (3,):
                                                            super().__init__()
                                                        else:
                                                            super(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq, self).__init__()

                                                        self.yang_name = "wfq"
                                                        self.yang_parent_name = "config"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([("bandwidth", ("bandwidth", PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth)), ("sum-of-bandwidth", ("sum_of_bandwidth", PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth))])
                                                        self._leafs = OrderedDict([
                                                            ('excess_ratio', (YLeaf(YType.uint16, 'excess-ratio'), ['int'])),
                                                        ])
                                                        self.excess_ratio = None

                                                        self.bandwidth = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth()
                                                        self.bandwidth.parent = self
                                                        self._children_name_map["bandwidth"] = "bandwidth"

                                                        self.sum_of_bandwidth = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth()
                                                        self.sum_of_bandwidth.parent = self
                                                        self._children_name_map["sum_of_bandwidth"] = "sum-of-bandwidth"
                                                        self._segment_path = lambda: "wfq"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq, ['excess_ratio'], name, value)


                                                    class Bandwidth(_Entity_):
                                                        """
                                                        Bandwidth
                                                        
                                                        .. attribute:: value
                                                        
                                                        	Config value
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: unit
                                                        
                                                        	Config unit
                                                        	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                                        
                                                        	**config**\: False
                                                        
                                                        

                                                        """

                                                        _prefix = 'skp-qos-oper'
                                                        _revision = '2016-02-18'

                                                        def __init__(self):
                                                            if sys.version_info > (3,):
                                                                super().__init__()
                                                            else:
                                                                super(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth, self).__init__()

                                                            self.yang_name = "bandwidth"
                                                            self.yang_parent_name = "wfq"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                                ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                                            ])
                                                            self.value = None
                                                            self.unit = None
                                                            self._segment_path = lambda: "bandwidth"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth, ['value', 'unit'], name, value)

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                            return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth']['meta_info']


                                                    class SumOfBandwidth(_Entity_):
                                                        """
                                                        Sum of Bandwidth
                                                        
                                                        .. attribute:: value
                                                        
                                                        	Config value
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: unit
                                                        
                                                        	Config unit
                                                        	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                                        
                                                        	**config**\: False
                                                        
                                                        

                                                        """

                                                        _prefix = 'skp-qos-oper'
                                                        _revision = '2016-02-18'

                                                        def __init__(self):
                                                            if sys.version_info > (3,):
                                                                super().__init__()
                                                            else:
                                                                super(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth, self).__init__()

                                                            self.yang_name = "sum-of-bandwidth"
                                                            self.yang_parent_name = "wfq"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                                ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                                            ])
                                                            self.value = None
                                                            self.unit = None
                                                            self._segment_path = lambda: "sum-of-bandwidth"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth, ['value', 'unit'], name, value)

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                            return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth']['meta_info']

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                        return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq']['meta_info']

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config']['meta_info']


                                            class Result(_Entity_):
                                                """
                                                QoS EA Class Result
                                                
                                                .. attribute:: queue
                                                
                                                	QoS EA Queue Result
                                                	**type**\:  :py:class:`Queue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: police
                                                
                                                	QoS EA Policer Result
                                                	**type**\:  :py:class:`Police <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: stats_id
                                                
                                                	Stats ID
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result, self).__init__()

                                                    self.yang_name = "result"
                                                    self.yang_parent_name = "qos-show-ea-pclass-st"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("queue", ("queue", PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue)), ("police", ("police", PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police))])
                                                    self._leafs = OrderedDict([
                                                        ('stats_id', (YLeaf(YType.uint32, 'stats-id'), ['int'])),
                                                    ])
                                                    self.stats_id = None

                                                    self.queue = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue()
                                                    self.queue.parent = self
                                                    self._children_name_map["queue"] = "queue"

                                                    self.police = PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police()
                                                    self.police.parent = self
                                                    self._children_name_map["police"] = "police"
                                                    self._segment_path = lambda: "result"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result, ['stats_id'], name, value)


                                                class Queue(_Entity_):
                                                    """
                                                    QoS EA Queue Result
                                                    
                                                    .. attribute:: queue_id
                                                    
                                                    	Queue ID
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: commit_tx
                                                    
                                                    	Commit Tx
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: excess_tx
                                                    
                                                    	Excess Tx
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: drop
                                                    
                                                    	Drop
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    	**config**\: False
                                                    
                                                    

                                                    """

                                                    _prefix = 'skp-qos-oper'
                                                    _revision = '2016-02-18'

                                                    def __init__(self):
                                                        if sys.version_info > (3,):
                                                            super().__init__()
                                                        else:
                                                            super(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue, self).__init__()

                                                        self.yang_name = "queue"
                                                        self.yang_parent_name = "result"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('queue_id', (YLeaf(YType.uint32, 'queue-id'), ['int'])),
                                                            ('commit_tx', (YLeaf(YType.uint32, 'commit-tx'), ['int'])),
                                                            ('excess_tx', (YLeaf(YType.uint32, 'excess-tx'), ['int'])),
                                                            ('drop', (YLeaf(YType.uint32, 'drop'), ['int'])),
                                                        ])
                                                        self.queue_id = None
                                                        self.commit_tx = None
                                                        self.excess_tx = None
                                                        self.drop = None
                                                        self._segment_path = lambda: "queue"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue, ['queue_id', 'commit_tx', 'excess_tx', 'drop'], name, value)

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                        return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue']['meta_info']


                                                class Police(_Entity_):
                                                    """
                                                    QoS EA Policer Result
                                                    
                                                    .. attribute:: token_bucket_id
                                                    
                                                    	Token Bucket ID
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: conform
                                                    
                                                    	Conform Rate
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: exceed
                                                    
                                                    	Exceed Rate
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: violate
                                                    
                                                    	Violate Rate
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    	**config**\: False
                                                    
                                                    

                                                    """

                                                    _prefix = 'skp-qos-oper'
                                                    _revision = '2016-02-18'

                                                    def __init__(self):
                                                        if sys.version_info > (3,):
                                                            super().__init__()
                                                        else:
                                                            super(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police, self).__init__()

                                                        self.yang_name = "police"
                                                        self.yang_parent_name = "result"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('token_bucket_id', (YLeaf(YType.uint32, 'token-bucket-id'), ['int'])),
                                                            ('conform', (YLeaf(YType.uint32, 'conform'), ['int'])),
                                                            ('exceed', (YLeaf(YType.uint32, 'exceed'), ['int'])),
                                                            ('violate', (YLeaf(YType.uint32, 'violate'), ['int'])),
                                                        ])
                                                        self.token_bucket_id = None
                                                        self.conform = None
                                                        self.exceed = None
                                                        self.violate = None
                                                        self._segment_path = lambda: "police"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police, ['token_bucket_id', 'conform', 'exceed', 'violate'], name, value)

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                        return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police']['meta_info']

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result']['meta_info']

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass.QosShowEaPclassSt']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details.SkywarpQosPolicyClass']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                        return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput.Details']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                    return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.BundleInput']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                            return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                        return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces.BundleInterface']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                    return meta._meta_table['PlatformQosEa.Nodes.Node.BundleInterfaces']['meta_info']


            class Interfaces(_Entity_):
                """
                QoS\-EA list of interfaces
                
                .. attribute:: interface
                
                	QoS\-EA interface name
                	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface>`
                
                	**config**\: False
                
                

                """

                _prefix = 'skp-qos-oper'
                _revision = '2016-02-18'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(PlatformQosEa.Nodes.Node.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface", ("interface", PlatformQosEa.Nodes.Node.Interfaces.Interface))])
                    self._leafs = OrderedDict()

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PlatformQosEa.Nodes.Node.Interfaces, [], name, value)


                class Interface(_Entity_):
                    """
                    QoS\-EA interface name
                    
                    .. attribute:: interface_name  (key)
                    
                    	The name of the interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: output
                    
                    	QoS\-EA policy direction egress
                    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Output>`
                    
                    	**config**\: False
                    
                    .. attribute:: input
                    
                    	QoS\-EA policy direction ingress
                    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Input>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'skp-qos-oper'
                    _revision = '2016-02-18'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(PlatformQosEa.Nodes.Node.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([("output", ("output", PlatformQosEa.Nodes.Node.Interfaces.Interface.Output)), ("input", ("input", PlatformQosEa.Nodes.Node.Interfaces.Interface.Input))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ])
                        self.interface_name = None

                        self.output = PlatformQosEa.Nodes.Node.Interfaces.Interface.Output()
                        self.output.parent = self
                        self._children_name_map["output"] = "output"

                        self.input = PlatformQosEa.Nodes.Node.Interfaces.Interface.Input()
                        self.input.parent = self
                        self._children_name_map["input"] = "input"
                        self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PlatformQosEa.Nodes.Node.Interfaces.Interface, ['interface_name'], name, value)


                    class Output(_Entity_):
                        """
                        QoS\-EA policy direction egress
                        
                        .. attribute:: details
                        
                        	QoS\-EA policy details
                        	**type**\:  :py:class:`Details <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'skp-qos-oper'
                        _revision = '2016-02-18'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(PlatformQosEa.Nodes.Node.Interfaces.Interface.Output, self).__init__()

                            self.yang_name = "output"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("details", ("details", PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details))])
                            self._leafs = OrderedDict()

                            self.details = PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details()
                            self.details.parent = self
                            self._children_name_map["details"] = "details"
                            self._segment_path = lambda: "output"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PlatformQosEa.Nodes.Node.Interfaces.Interface.Output, [], name, value)


                        class Details(_Entity_):
                            """
                            QoS\-EA policy details
                            
                            .. attribute:: header
                            
                            	QoS EA policy header
                            	**type**\:  :py:class:`Header <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.Header>`
                            
                            	**config**\: False
                            
                            .. attribute:: interface_parameters
                            
                            	QoS EA Interface Parameters
                            	**type**\:  :py:class:`InterfaceParameters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.InterfaceParameters>`
                            
                            	**config**\: False
                            
                            .. attribute:: skywarp_qos_policy_class
                            
                            	Skywarp QoS EA policy class details
                            	**type**\:  :py:class:`SkywarpQosPolicyClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'skp-qos-oper'
                            _revision = '2016-02-18'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details, self).__init__()

                                self.yang_name = "details"
                                self.yang_parent_name = "output"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("header", ("header", PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.Header)), ("interface-parameters", ("interface_parameters", PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.InterfaceParameters)), ("skywarp-qos-policy-class", ("skywarp_qos_policy_class", PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass))])
                                self._leafs = OrderedDict()

                                self.header = PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.Header()
                                self.header.parent = self
                                self._children_name_map["header"] = "header"

                                self.interface_parameters = PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.InterfaceParameters()
                                self.interface_parameters.parent = self
                                self._children_name_map["interface_parameters"] = "interface-parameters"

                                self.skywarp_qos_policy_class = PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass()
                                self.skywarp_qos_policy_class.parent = self
                                self._children_name_map["skywarp_qos_policy_class"] = "skywarp-qos-policy-class"
                                self._segment_path = lambda: "details"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details, [], name, value)


                            class Header(_Entity_):
                                """
                                QoS EA policy header
                                
                                .. attribute:: interface_name
                                
                                	Interface Name
                                	**type**\: str
                                
                                	**length:** 0..101
                                
                                	**config**\: False
                                
                                .. attribute:: policy_name
                                
                                	Policy name
                                	**type**\: str
                                
                                	**length:** 0..65
                                
                                	**config**\: False
                                
                                .. attribute:: direction
                                
                                	Direction
                                	**type**\: str
                                
                                	**length:** 0..11
                                
                                	**config**\: False
                                
                                .. attribute:: classes
                                
                                	Number of classes
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'skp-qos-oper'
                                _revision = '2016-02-18'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.Header, self).__init__()

                                    self.yang_name = "header"
                                    self.yang_parent_name = "details"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                        ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                        ('direction', (YLeaf(YType.str, 'direction'), ['str'])),
                                        ('classes', (YLeaf(YType.uint16, 'classes'), ['int'])),
                                    ])
                                    self.interface_name = None
                                    self.policy_name = None
                                    self.direction = None
                                    self.classes = None
                                    self._segment_path = lambda: "header"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.Header, ['interface_name', 'policy_name', 'direction', 'classes'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                    return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.Header']['meta_info']


                            class InterfaceParameters(_Entity_):
                                """
                                QoS EA Interface Parameters
                                
                                .. attribute:: policy_name
                                
                                	Policy name
                                	**type**\: str
                                
                                	**length:** 0..65
                                
                                	**config**\: False
                                
                                .. attribute:: hierarchical_depth
                                
                                	Max Hierarchial Depth
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                .. attribute:: interface_type
                                
                                	Interface Type
                                	**type**\: str
                                
                                	**length:** 0..101
                                
                                	**config**\: False
                                
                                .. attribute:: interface_rate
                                
                                	Interface Programmed Rate
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: port_shaper_rate
                                
                                	Port Shaper Rate
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: interface_handle
                                
                                	Interface Handle
                                	**type**\: str
                                
                                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                
                                	**config**\: False
                                
                                .. attribute:: under_line_interface_handle
                                
                                	UnderLineInterface Handle
                                	**type**\: str
                                
                                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                
                                	**config**\: False
                                
                                .. attribute:: bundle_id
                                
                                	Bundle Interface ID
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                	**config**\: False
                                
                                .. attribute:: uidb_index
                                
                                	UIDB Index
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                	**config**\: False
                                
                                .. attribute:: qos_interface_handle
                                
                                	QoS Interface handle
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: port
                                
                                	Local Port
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: policy_map_id
                                
                                	Policy Map ID
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'skp-qos-oper'
                                _revision = '2016-02-18'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.InterfaceParameters, self).__init__()

                                    self.yang_name = "interface-parameters"
                                    self.yang_parent_name = "details"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                        ('hierarchical_depth', (YLeaf(YType.uint8, 'hierarchical-depth'), ['int'])),
                                        ('interface_type', (YLeaf(YType.str, 'interface-type'), ['str'])),
                                        ('interface_rate', (YLeaf(YType.uint32, 'interface-rate'), ['int'])),
                                        ('port_shaper_rate', (YLeaf(YType.uint32, 'port-shaper-rate'), ['int'])),
                                        ('interface_handle', (YLeaf(YType.str, 'interface-handle'), ['str'])),
                                        ('under_line_interface_handle', (YLeaf(YType.str, 'under-line-interface-handle'), ['str'])),
                                        ('bundle_id', (YLeaf(YType.uint16, 'bundle-id'), ['int'])),
                                        ('uidb_index', (YLeaf(YType.uint16, 'uidb-index'), ['int'])),
                                        ('qos_interface_handle', (YLeaf(YType.uint64, 'qos-interface-handle'), ['int'])),
                                        ('port', (YLeaf(YType.uint32, 'port'), ['int'])),
                                        ('policy_map_id', (YLeaf(YType.uint16, 'policy-map-id'), ['int'])),
                                    ])
                                    self.policy_name = None
                                    self.hierarchical_depth = None
                                    self.interface_type = None
                                    self.interface_rate = None
                                    self.port_shaper_rate = None
                                    self.interface_handle = None
                                    self.under_line_interface_handle = None
                                    self.bundle_id = None
                                    self.uidb_index = None
                                    self.qos_interface_handle = None
                                    self.port = None
                                    self.policy_map_id = None
                                    self._segment_path = lambda: "interface-parameters"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.InterfaceParameters, ['policy_name', 'hierarchical_depth', 'interface_type', 'interface_rate', 'port_shaper_rate', 'interface_handle', 'under_line_interface_handle', 'bundle_id', 'uidb_index', 'qos_interface_handle', 'port', 'policy_map_id'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                    return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.InterfaceParameters']['meta_info']


                            class SkywarpQosPolicyClass(_Entity_):
                                """
                                Skywarp QoS EA policy class details
                                
                                .. attribute:: qos_show_ea_pclass_st
                                
                                	qos show ea pclass st
                                	**type**\: list of  		 :py:class:`QosShowEaPclassSt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'skp-qos-oper'
                                _revision = '2016-02-18'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass, self).__init__()

                                    self.yang_name = "skywarp-qos-policy-class"
                                    self.yang_parent_name = "details"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("qos-show-ea-pclass-st", ("qos_show_ea_pclass_st", PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt))])
                                    self._leafs = OrderedDict()

                                    self.qos_show_ea_pclass_st = YList(self)
                                    self._segment_path = lambda: "skywarp-qos-policy-class"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass, [], name, value)


                                class QosShowEaPclassSt(_Entity_):
                                    """
                                    qos show ea pclass st
                                    
                                    .. attribute:: config
                                    
                                    	QoS EA Class Configuration
                                    	**type**\:  :py:class:`Config <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: result
                                    
                                    	QoS EA Class Result
                                    	**type**\:  :py:class:`Result <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: index
                                    
                                    	Class Index
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: class_level
                                    
                                    	Class level
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: class_name
                                    
                                    	Class name
                                    	**type**\: str
                                    
                                    	**length:** 0..65
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: policy_name
                                    
                                    	Policy name
                                    	**type**\: str
                                    
                                    	**length:** 0..65
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: node_flags
                                    
                                    	Node Flags
                                    	**type**\: str
                                    
                                    	**length:** 0..101
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: stats_flags
                                    
                                    	Statistical Flags
                                    	**type**\: str
                                    
                                    	**length:** 0..101
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'skp-qos-oper'
                                    _revision = '2016-02-18'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt, self).__init__()

                                        self.yang_name = "qos-show-ea-pclass-st"
                                        self.yang_parent_name = "skywarp-qos-policy-class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("config", ("config", PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config)), ("result", ("result", PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result))])
                                        self._leafs = OrderedDict([
                                            ('index', (YLeaf(YType.uint16, 'index'), ['int'])),
                                            ('class_level', (YLeaf(YType.uint8, 'class-level'), ['int'])),
                                            ('class_name', (YLeaf(YType.str, 'class-name'), ['str'])),
                                            ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                            ('node_flags', (YLeaf(YType.str, 'node-flags'), ['str'])),
                                            ('stats_flags', (YLeaf(YType.str, 'stats-flags'), ['str'])),
                                        ])
                                        self.index = None
                                        self.class_level = None
                                        self.class_name = None
                                        self.policy_name = None
                                        self.node_flags = None
                                        self.stats_flags = None

                                        self.config = PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config()
                                        self.config.parent = self
                                        self._children_name_map["config"] = "config"

                                        self.result = PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result()
                                        self.result.parent = self
                                        self._children_name_map["result"] = "result"
                                        self._segment_path = lambda: "qos-show-ea-pclass-st"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt, ['index', 'class_level', 'class_name', 'policy_name', 'node_flags', 'stats_flags'], name, value)


                                    class Config(_Entity_):
                                        """
                                        QoS EA Class Configuration
                                        
                                        .. attribute:: police
                                        
                                        	QoS EA Policer parameters
                                        	**type**\:  :py:class:`Police <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: shape
                                        
                                        	QoS EA Shaper parameters
                                        	**type**\:  :py:class:`Shape <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: wfq
                                        
                                        	QoS EA WFQ parameters
                                        	**type**\:  :py:class:`Wfq <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: node_config
                                        
                                        	Node Config
                                        	**type**\: str
                                        
                                        	**length:** 0..101
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config, self).__init__()

                                            self.yang_name = "config"
                                            self.yang_parent_name = "qos-show-ea-pclass-st"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("police", ("police", PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police)), ("shape", ("shape", PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape)), ("wfq", ("wfq", PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq))])
                                            self._leafs = OrderedDict([
                                                ('node_config', (YLeaf(YType.str, 'node-config'), ['str'])),
                                            ])
                                            self.node_config = None

                                            self.police = PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police()
                                            self.police.parent = self
                                            self._children_name_map["police"] = "police"

                                            self.shape = PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape()
                                            self.shape.parent = self
                                            self._children_name_map["shape"] = "shape"

                                            self.wfq = PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq()
                                            self.wfq.parent = self
                                            self._children_name_map["wfq"] = "wfq"
                                            self._segment_path = lambda: "config"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config, ['node_config'], name, value)


                                        class Police(_Entity_):
                                            """
                                            QoS EA Policer parameters
                                            
                                            .. attribute:: cir
                                            
                                            	CIR
                                            	**type**\:  :py:class:`Cir <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: cbs
                                            
                                            	CBS
                                            	**type**\:  :py:class:`Cbs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: color_aware
                                            
                                            	Color Aware
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: policer_type
                                            
                                            	Policer type
                                            	**type**\:  :py:class:`TbAlgorithm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.TbAlgorithm>`
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police, self).__init__()

                                                self.yang_name = "police"
                                                self.yang_parent_name = "config"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("cir", ("cir", PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir)), ("cbs", ("cbs", PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs))])
                                                self._leafs = OrderedDict([
                                                    ('color_aware', (YLeaf(YType.boolean, 'color-aware'), ['bool'])),
                                                    ('policer_type', (YLeaf(YType.enumeration, 'policer-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'TbAlgorithm', '')])),
                                                ])
                                                self.color_aware = None
                                                self.policer_type = None

                                                self.cir = PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir()
                                                self.cir.parent = self
                                                self._children_name_map["cir"] = "cir"

                                                self.cbs = PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs()
                                                self.cbs.parent = self
                                                self._children_name_map["cbs"] = "cbs"
                                                self._segment_path = lambda: "police"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police, ['color_aware', 'policer_type'], name, value)


                                            class Cir(_Entity_):
                                                """
                                                CIR
                                                
                                                .. attribute:: value
                                                
                                                	Config value
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: unit
                                                
                                                	Config unit
                                                	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir, self).__init__()

                                                    self.yang_name = "cir"
                                                    self.yang_parent_name = "police"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                        ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                                    ])
                                                    self.value = None
                                                    self.unit = None
                                                    self._segment_path = lambda: "cir"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir, ['value', 'unit'], name, value)

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir']['meta_info']


                                            class Cbs(_Entity_):
                                                """
                                                CBS
                                                
                                                .. attribute:: value
                                                
                                                	Config value
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: unit
                                                
                                                	Config unit
                                                	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs, self).__init__()

                                                    self.yang_name = "cbs"
                                                    self.yang_parent_name = "police"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                        ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                                    ])
                                                    self.value = None
                                                    self.unit = None
                                                    self._segment_path = lambda: "cbs"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs, ['value', 'unit'], name, value)

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs']['meta_info']

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police']['meta_info']


                                        class Shape(_Entity_):
                                            """
                                            QoS EA Shaper parameters
                                            
                                            .. attribute:: pir
                                            
                                            	PIR in kbps
                                            	**type**\:  :py:class:`Pir <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: pbs
                                            
                                            	PBS in bytes
                                            	**type**\:  :py:class:`Pbs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs>`
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape, self).__init__()

                                                self.yang_name = "shape"
                                                self.yang_parent_name = "config"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("pir", ("pir", PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir)), ("pbs", ("pbs", PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs))])
                                                self._leafs = OrderedDict()

                                                self.pir = PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir()
                                                self.pir.parent = self
                                                self._children_name_map["pir"] = "pir"

                                                self.pbs = PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs()
                                                self.pbs.parent = self
                                                self._children_name_map["pbs"] = "pbs"
                                                self._segment_path = lambda: "shape"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape, [], name, value)


                                            class Pir(_Entity_):
                                                """
                                                PIR in kbps
                                                
                                                .. attribute:: value
                                                
                                                	Config value
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: unit
                                                
                                                	Config unit
                                                	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir, self).__init__()

                                                    self.yang_name = "pir"
                                                    self.yang_parent_name = "shape"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                        ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                                    ])
                                                    self.value = None
                                                    self.unit = None
                                                    self._segment_path = lambda: "pir"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir, ['value', 'unit'], name, value)

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir']['meta_info']


                                            class Pbs(_Entity_):
                                                """
                                                PBS in bytes
                                                
                                                .. attribute:: value
                                                
                                                	Config value
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: unit
                                                
                                                	Config unit
                                                	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs, self).__init__()

                                                    self.yang_name = "pbs"
                                                    self.yang_parent_name = "shape"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                        ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                                    ])
                                                    self.value = None
                                                    self.unit = None
                                                    self._segment_path = lambda: "pbs"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs, ['value', 'unit'], name, value)

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs']['meta_info']

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape']['meta_info']


                                        class Wfq(_Entity_):
                                            """
                                            QoS EA WFQ parameters
                                            
                                            .. attribute:: bandwidth
                                            
                                            	Bandwidth
                                            	**type**\:  :py:class:`Bandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: sum_of_bandwidth
                                            
                                            	Sum of Bandwidth
                                            	**type**\:  :py:class:`SumOfBandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: excess_ratio
                                            
                                            	Excess Ratio
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq, self).__init__()

                                                self.yang_name = "wfq"
                                                self.yang_parent_name = "config"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("bandwidth", ("bandwidth", PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth)), ("sum-of-bandwidth", ("sum_of_bandwidth", PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth))])
                                                self._leafs = OrderedDict([
                                                    ('excess_ratio', (YLeaf(YType.uint16, 'excess-ratio'), ['int'])),
                                                ])
                                                self.excess_ratio = None

                                                self.bandwidth = PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth()
                                                self.bandwidth.parent = self
                                                self._children_name_map["bandwidth"] = "bandwidth"

                                                self.sum_of_bandwidth = PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth()
                                                self.sum_of_bandwidth.parent = self
                                                self._children_name_map["sum_of_bandwidth"] = "sum-of-bandwidth"
                                                self._segment_path = lambda: "wfq"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq, ['excess_ratio'], name, value)


                                            class Bandwidth(_Entity_):
                                                """
                                                Bandwidth
                                                
                                                .. attribute:: value
                                                
                                                	Config value
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: unit
                                                
                                                	Config unit
                                                	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth, self).__init__()

                                                    self.yang_name = "bandwidth"
                                                    self.yang_parent_name = "wfq"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                        ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                                    ])
                                                    self.value = None
                                                    self.unit = None
                                                    self._segment_path = lambda: "bandwidth"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth, ['value', 'unit'], name, value)

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth']['meta_info']


                                            class SumOfBandwidth(_Entity_):
                                                """
                                                Sum of Bandwidth
                                                
                                                .. attribute:: value
                                                
                                                	Config value
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: unit
                                                
                                                	Config unit
                                                	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth, self).__init__()

                                                    self.yang_name = "sum-of-bandwidth"
                                                    self.yang_parent_name = "wfq"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                        ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                                    ])
                                                    self.value = None
                                                    self.unit = None
                                                    self._segment_path = lambda: "sum-of-bandwidth"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth, ['value', 'unit'], name, value)

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth']['meta_info']

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config']['meta_info']


                                    class Result(_Entity_):
                                        """
                                        QoS EA Class Result
                                        
                                        .. attribute:: queue
                                        
                                        	QoS EA Queue Result
                                        	**type**\:  :py:class:`Queue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: police
                                        
                                        	QoS EA Policer Result
                                        	**type**\:  :py:class:`Police <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: stats_id
                                        
                                        	Stats ID
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result, self).__init__()

                                            self.yang_name = "result"
                                            self.yang_parent_name = "qos-show-ea-pclass-st"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("queue", ("queue", PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue)), ("police", ("police", PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police))])
                                            self._leafs = OrderedDict([
                                                ('stats_id', (YLeaf(YType.uint32, 'stats-id'), ['int'])),
                                            ])
                                            self.stats_id = None

                                            self.queue = PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue()
                                            self.queue.parent = self
                                            self._children_name_map["queue"] = "queue"

                                            self.police = PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police()
                                            self.police.parent = self
                                            self._children_name_map["police"] = "police"
                                            self._segment_path = lambda: "result"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result, ['stats_id'], name, value)


                                        class Queue(_Entity_):
                                            """
                                            QoS EA Queue Result
                                            
                                            .. attribute:: queue_id
                                            
                                            	Queue ID
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: commit_tx
                                            
                                            	Commit Tx
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: excess_tx
                                            
                                            	Excess Tx
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: drop
                                            
                                            	Drop
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue, self).__init__()

                                                self.yang_name = "queue"
                                                self.yang_parent_name = "result"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('queue_id', (YLeaf(YType.uint32, 'queue-id'), ['int'])),
                                                    ('commit_tx', (YLeaf(YType.uint32, 'commit-tx'), ['int'])),
                                                    ('excess_tx', (YLeaf(YType.uint32, 'excess-tx'), ['int'])),
                                                    ('drop', (YLeaf(YType.uint32, 'drop'), ['int'])),
                                                ])
                                                self.queue_id = None
                                                self.commit_tx = None
                                                self.excess_tx = None
                                                self.drop = None
                                                self._segment_path = lambda: "queue"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue, ['queue_id', 'commit_tx', 'excess_tx', 'drop'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue']['meta_info']


                                        class Police(_Entity_):
                                            """
                                            QoS EA Policer Result
                                            
                                            .. attribute:: token_bucket_id
                                            
                                            	Token Bucket ID
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: conform
                                            
                                            	Conform Rate
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: exceed
                                            
                                            	Exceed Rate
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: violate
                                            
                                            	Violate Rate
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police, self).__init__()

                                                self.yang_name = "police"
                                                self.yang_parent_name = "result"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('token_bucket_id', (YLeaf(YType.uint32, 'token-bucket-id'), ['int'])),
                                                    ('conform', (YLeaf(YType.uint32, 'conform'), ['int'])),
                                                    ('exceed', (YLeaf(YType.uint32, 'exceed'), ['int'])),
                                                    ('violate', (YLeaf(YType.uint32, 'violate'), ['int'])),
                                                ])
                                                self.token_bucket_id = None
                                                self.conform = None
                                                self.exceed = None
                                                self.violate = None
                                                self._segment_path = lambda: "police"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police, ['token_bucket_id', 'conform', 'exceed', 'violate'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                        return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass.QosShowEaPclassSt']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                    return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details.SkywarpQosPolicyClass']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output.Details']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                            return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Output']['meta_info']


                    class Input(_Entity_):
                        """
                        QoS\-EA policy direction ingress
                        
                        .. attribute:: details
                        
                        	QoS\-EA policy details
                        	**type**\:  :py:class:`Details <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'skp-qos-oper'
                        _revision = '2016-02-18'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(PlatformQosEa.Nodes.Node.Interfaces.Interface.Input, self).__init__()

                            self.yang_name = "input"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("details", ("details", PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details))])
                            self._leafs = OrderedDict()

                            self.details = PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details()
                            self.details.parent = self
                            self._children_name_map["details"] = "details"
                            self._segment_path = lambda: "input"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PlatformQosEa.Nodes.Node.Interfaces.Interface.Input, [], name, value)


                        class Details(_Entity_):
                            """
                            QoS\-EA policy details
                            
                            .. attribute:: header
                            
                            	QoS EA policy header
                            	**type**\:  :py:class:`Header <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.Header>`
                            
                            	**config**\: False
                            
                            .. attribute:: interface_parameters
                            
                            	QoS EA Interface Parameters
                            	**type**\:  :py:class:`InterfaceParameters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.InterfaceParameters>`
                            
                            	**config**\: False
                            
                            .. attribute:: skywarp_qos_policy_class
                            
                            	Skywarp QoS EA policy class details
                            	**type**\:  :py:class:`SkywarpQosPolicyClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'skp-qos-oper'
                            _revision = '2016-02-18'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details, self).__init__()

                                self.yang_name = "details"
                                self.yang_parent_name = "input"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("header", ("header", PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.Header)), ("interface-parameters", ("interface_parameters", PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.InterfaceParameters)), ("skywarp-qos-policy-class", ("skywarp_qos_policy_class", PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass))])
                                self._leafs = OrderedDict()

                                self.header = PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.Header()
                                self.header.parent = self
                                self._children_name_map["header"] = "header"

                                self.interface_parameters = PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.InterfaceParameters()
                                self.interface_parameters.parent = self
                                self._children_name_map["interface_parameters"] = "interface-parameters"

                                self.skywarp_qos_policy_class = PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass()
                                self.skywarp_qos_policy_class.parent = self
                                self._children_name_map["skywarp_qos_policy_class"] = "skywarp-qos-policy-class"
                                self._segment_path = lambda: "details"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details, [], name, value)


                            class Header(_Entity_):
                                """
                                QoS EA policy header
                                
                                .. attribute:: interface_name
                                
                                	Interface Name
                                	**type**\: str
                                
                                	**length:** 0..101
                                
                                	**config**\: False
                                
                                .. attribute:: policy_name
                                
                                	Policy name
                                	**type**\: str
                                
                                	**length:** 0..65
                                
                                	**config**\: False
                                
                                .. attribute:: direction
                                
                                	Direction
                                	**type**\: str
                                
                                	**length:** 0..11
                                
                                	**config**\: False
                                
                                .. attribute:: classes
                                
                                	Number of classes
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'skp-qos-oper'
                                _revision = '2016-02-18'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.Header, self).__init__()

                                    self.yang_name = "header"
                                    self.yang_parent_name = "details"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                        ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                        ('direction', (YLeaf(YType.str, 'direction'), ['str'])),
                                        ('classes', (YLeaf(YType.uint16, 'classes'), ['int'])),
                                    ])
                                    self.interface_name = None
                                    self.policy_name = None
                                    self.direction = None
                                    self.classes = None
                                    self._segment_path = lambda: "header"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.Header, ['interface_name', 'policy_name', 'direction', 'classes'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                    return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.Header']['meta_info']


                            class InterfaceParameters(_Entity_):
                                """
                                QoS EA Interface Parameters
                                
                                .. attribute:: policy_name
                                
                                	Policy name
                                	**type**\: str
                                
                                	**length:** 0..65
                                
                                	**config**\: False
                                
                                .. attribute:: hierarchical_depth
                                
                                	Max Hierarchial Depth
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                .. attribute:: interface_type
                                
                                	Interface Type
                                	**type**\: str
                                
                                	**length:** 0..101
                                
                                	**config**\: False
                                
                                .. attribute:: interface_rate
                                
                                	Interface Programmed Rate
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: port_shaper_rate
                                
                                	Port Shaper Rate
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: interface_handle
                                
                                	Interface Handle
                                	**type**\: str
                                
                                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                
                                	**config**\: False
                                
                                .. attribute:: under_line_interface_handle
                                
                                	UnderLineInterface Handle
                                	**type**\: str
                                
                                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                
                                	**config**\: False
                                
                                .. attribute:: bundle_id
                                
                                	Bundle Interface ID
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                	**config**\: False
                                
                                .. attribute:: uidb_index
                                
                                	UIDB Index
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                	**config**\: False
                                
                                .. attribute:: qos_interface_handle
                                
                                	QoS Interface handle
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: port
                                
                                	Local Port
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: policy_map_id
                                
                                	Policy Map ID
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'skp-qos-oper'
                                _revision = '2016-02-18'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.InterfaceParameters, self).__init__()

                                    self.yang_name = "interface-parameters"
                                    self.yang_parent_name = "details"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                        ('hierarchical_depth', (YLeaf(YType.uint8, 'hierarchical-depth'), ['int'])),
                                        ('interface_type', (YLeaf(YType.str, 'interface-type'), ['str'])),
                                        ('interface_rate', (YLeaf(YType.uint32, 'interface-rate'), ['int'])),
                                        ('port_shaper_rate', (YLeaf(YType.uint32, 'port-shaper-rate'), ['int'])),
                                        ('interface_handle', (YLeaf(YType.str, 'interface-handle'), ['str'])),
                                        ('under_line_interface_handle', (YLeaf(YType.str, 'under-line-interface-handle'), ['str'])),
                                        ('bundle_id', (YLeaf(YType.uint16, 'bundle-id'), ['int'])),
                                        ('uidb_index', (YLeaf(YType.uint16, 'uidb-index'), ['int'])),
                                        ('qos_interface_handle', (YLeaf(YType.uint64, 'qos-interface-handle'), ['int'])),
                                        ('port', (YLeaf(YType.uint32, 'port'), ['int'])),
                                        ('policy_map_id', (YLeaf(YType.uint16, 'policy-map-id'), ['int'])),
                                    ])
                                    self.policy_name = None
                                    self.hierarchical_depth = None
                                    self.interface_type = None
                                    self.interface_rate = None
                                    self.port_shaper_rate = None
                                    self.interface_handle = None
                                    self.under_line_interface_handle = None
                                    self.bundle_id = None
                                    self.uidb_index = None
                                    self.qos_interface_handle = None
                                    self.port = None
                                    self.policy_map_id = None
                                    self._segment_path = lambda: "interface-parameters"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.InterfaceParameters, ['policy_name', 'hierarchical_depth', 'interface_type', 'interface_rate', 'port_shaper_rate', 'interface_handle', 'under_line_interface_handle', 'bundle_id', 'uidb_index', 'qos_interface_handle', 'port', 'policy_map_id'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                    return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.InterfaceParameters']['meta_info']


                            class SkywarpQosPolicyClass(_Entity_):
                                """
                                Skywarp QoS EA policy class details
                                
                                .. attribute:: qos_show_ea_pclass_st
                                
                                	qos show ea pclass st
                                	**type**\: list of  		 :py:class:`QosShowEaPclassSt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'skp-qos-oper'
                                _revision = '2016-02-18'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass, self).__init__()

                                    self.yang_name = "skywarp-qos-policy-class"
                                    self.yang_parent_name = "details"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("qos-show-ea-pclass-st", ("qos_show_ea_pclass_st", PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt))])
                                    self._leafs = OrderedDict()

                                    self.qos_show_ea_pclass_st = YList(self)
                                    self._segment_path = lambda: "skywarp-qos-policy-class"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass, [], name, value)


                                class QosShowEaPclassSt(_Entity_):
                                    """
                                    qos show ea pclass st
                                    
                                    .. attribute:: config
                                    
                                    	QoS EA Class Configuration
                                    	**type**\:  :py:class:`Config <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: result
                                    
                                    	QoS EA Class Result
                                    	**type**\:  :py:class:`Result <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: index
                                    
                                    	Class Index
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: class_level
                                    
                                    	Class level
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: class_name
                                    
                                    	Class name
                                    	**type**\: str
                                    
                                    	**length:** 0..65
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: policy_name
                                    
                                    	Policy name
                                    	**type**\: str
                                    
                                    	**length:** 0..65
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: node_flags
                                    
                                    	Node Flags
                                    	**type**\: str
                                    
                                    	**length:** 0..101
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: stats_flags
                                    
                                    	Statistical Flags
                                    	**type**\: str
                                    
                                    	**length:** 0..101
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'skp-qos-oper'
                                    _revision = '2016-02-18'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt, self).__init__()

                                        self.yang_name = "qos-show-ea-pclass-st"
                                        self.yang_parent_name = "skywarp-qos-policy-class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("config", ("config", PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config)), ("result", ("result", PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result))])
                                        self._leafs = OrderedDict([
                                            ('index', (YLeaf(YType.uint16, 'index'), ['int'])),
                                            ('class_level', (YLeaf(YType.uint8, 'class-level'), ['int'])),
                                            ('class_name', (YLeaf(YType.str, 'class-name'), ['str'])),
                                            ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                            ('node_flags', (YLeaf(YType.str, 'node-flags'), ['str'])),
                                            ('stats_flags', (YLeaf(YType.str, 'stats-flags'), ['str'])),
                                        ])
                                        self.index = None
                                        self.class_level = None
                                        self.class_name = None
                                        self.policy_name = None
                                        self.node_flags = None
                                        self.stats_flags = None

                                        self.config = PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config()
                                        self.config.parent = self
                                        self._children_name_map["config"] = "config"

                                        self.result = PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result()
                                        self.result.parent = self
                                        self._children_name_map["result"] = "result"
                                        self._segment_path = lambda: "qos-show-ea-pclass-st"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt, ['index', 'class_level', 'class_name', 'policy_name', 'node_flags', 'stats_flags'], name, value)


                                    class Config(_Entity_):
                                        """
                                        QoS EA Class Configuration
                                        
                                        .. attribute:: police
                                        
                                        	QoS EA Policer parameters
                                        	**type**\:  :py:class:`Police <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: shape
                                        
                                        	QoS EA Shaper parameters
                                        	**type**\:  :py:class:`Shape <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: wfq
                                        
                                        	QoS EA WFQ parameters
                                        	**type**\:  :py:class:`Wfq <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: node_config
                                        
                                        	Node Config
                                        	**type**\: str
                                        
                                        	**length:** 0..101
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config, self).__init__()

                                            self.yang_name = "config"
                                            self.yang_parent_name = "qos-show-ea-pclass-st"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("police", ("police", PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police)), ("shape", ("shape", PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape)), ("wfq", ("wfq", PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq))])
                                            self._leafs = OrderedDict([
                                                ('node_config', (YLeaf(YType.str, 'node-config'), ['str'])),
                                            ])
                                            self.node_config = None

                                            self.police = PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police()
                                            self.police.parent = self
                                            self._children_name_map["police"] = "police"

                                            self.shape = PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape()
                                            self.shape.parent = self
                                            self._children_name_map["shape"] = "shape"

                                            self.wfq = PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq()
                                            self.wfq.parent = self
                                            self._children_name_map["wfq"] = "wfq"
                                            self._segment_path = lambda: "config"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config, ['node_config'], name, value)


                                        class Police(_Entity_):
                                            """
                                            QoS EA Policer parameters
                                            
                                            .. attribute:: cir
                                            
                                            	CIR
                                            	**type**\:  :py:class:`Cir <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: cbs
                                            
                                            	CBS
                                            	**type**\:  :py:class:`Cbs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: color_aware
                                            
                                            	Color Aware
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: policer_type
                                            
                                            	Policer type
                                            	**type**\:  :py:class:`TbAlgorithm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.TbAlgorithm>`
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police, self).__init__()

                                                self.yang_name = "police"
                                                self.yang_parent_name = "config"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("cir", ("cir", PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir)), ("cbs", ("cbs", PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs))])
                                                self._leafs = OrderedDict([
                                                    ('color_aware', (YLeaf(YType.boolean, 'color-aware'), ['bool'])),
                                                    ('policer_type', (YLeaf(YType.enumeration, 'policer-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'TbAlgorithm', '')])),
                                                ])
                                                self.color_aware = None
                                                self.policer_type = None

                                                self.cir = PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir()
                                                self.cir.parent = self
                                                self._children_name_map["cir"] = "cir"

                                                self.cbs = PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs()
                                                self.cbs.parent = self
                                                self._children_name_map["cbs"] = "cbs"
                                                self._segment_path = lambda: "police"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police, ['color_aware', 'policer_type'], name, value)


                                            class Cir(_Entity_):
                                                """
                                                CIR
                                                
                                                .. attribute:: value
                                                
                                                	Config value
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: unit
                                                
                                                	Config unit
                                                	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir, self).__init__()

                                                    self.yang_name = "cir"
                                                    self.yang_parent_name = "police"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                        ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                                    ])
                                                    self.value = None
                                                    self.unit = None
                                                    self._segment_path = lambda: "cir"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir, ['value', 'unit'], name, value)

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cir']['meta_info']


                                            class Cbs(_Entity_):
                                                """
                                                CBS
                                                
                                                .. attribute:: value
                                                
                                                	Config value
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: unit
                                                
                                                	Config unit
                                                	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs, self).__init__()

                                                    self.yang_name = "cbs"
                                                    self.yang_parent_name = "police"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                        ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                                    ])
                                                    self.value = None
                                                    self.unit = None
                                                    self._segment_path = lambda: "cbs"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs, ['value', 'unit'], name, value)

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police.Cbs']['meta_info']

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Police']['meta_info']


                                        class Shape(_Entity_):
                                            """
                                            QoS EA Shaper parameters
                                            
                                            .. attribute:: pir
                                            
                                            	PIR in kbps
                                            	**type**\:  :py:class:`Pir <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: pbs
                                            
                                            	PBS in bytes
                                            	**type**\:  :py:class:`Pbs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs>`
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape, self).__init__()

                                                self.yang_name = "shape"
                                                self.yang_parent_name = "config"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("pir", ("pir", PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir)), ("pbs", ("pbs", PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs))])
                                                self._leafs = OrderedDict()

                                                self.pir = PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir()
                                                self.pir.parent = self
                                                self._children_name_map["pir"] = "pir"

                                                self.pbs = PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs()
                                                self.pbs.parent = self
                                                self._children_name_map["pbs"] = "pbs"
                                                self._segment_path = lambda: "shape"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape, [], name, value)


                                            class Pir(_Entity_):
                                                """
                                                PIR in kbps
                                                
                                                .. attribute:: value
                                                
                                                	Config value
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: unit
                                                
                                                	Config unit
                                                	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir, self).__init__()

                                                    self.yang_name = "pir"
                                                    self.yang_parent_name = "shape"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                        ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                                    ])
                                                    self.value = None
                                                    self.unit = None
                                                    self._segment_path = lambda: "pir"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir, ['value', 'unit'], name, value)

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pir']['meta_info']


                                            class Pbs(_Entity_):
                                                """
                                                PBS in bytes
                                                
                                                .. attribute:: value
                                                
                                                	Config value
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: unit
                                                
                                                	Config unit
                                                	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs, self).__init__()

                                                    self.yang_name = "pbs"
                                                    self.yang_parent_name = "shape"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                        ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                                    ])
                                                    self.value = None
                                                    self.unit = None
                                                    self._segment_path = lambda: "pbs"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs, ['value', 'unit'], name, value)

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape.Pbs']['meta_info']

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Shape']['meta_info']


                                        class Wfq(_Entity_):
                                            """
                                            QoS EA WFQ parameters
                                            
                                            .. attribute:: bandwidth
                                            
                                            	Bandwidth
                                            	**type**\:  :py:class:`Bandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: sum_of_bandwidth
                                            
                                            	Sum of Bandwidth
                                            	**type**\:  :py:class:`SumOfBandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: excess_ratio
                                            
                                            	Excess Ratio
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq, self).__init__()

                                                self.yang_name = "wfq"
                                                self.yang_parent_name = "config"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("bandwidth", ("bandwidth", PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth)), ("sum-of-bandwidth", ("sum_of_bandwidth", PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth))])
                                                self._leafs = OrderedDict([
                                                    ('excess_ratio', (YLeaf(YType.uint16, 'excess-ratio'), ['int'])),
                                                ])
                                                self.excess_ratio = None

                                                self.bandwidth = PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth()
                                                self.bandwidth.parent = self
                                                self._children_name_map["bandwidth"] = "bandwidth"

                                                self.sum_of_bandwidth = PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth()
                                                self.sum_of_bandwidth.parent = self
                                                self._children_name_map["sum_of_bandwidth"] = "sum-of-bandwidth"
                                                self._segment_path = lambda: "wfq"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq, ['excess_ratio'], name, value)


                                            class Bandwidth(_Entity_):
                                                """
                                                Bandwidth
                                                
                                                .. attribute:: value
                                                
                                                	Config value
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: unit
                                                
                                                	Config unit
                                                	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth, self).__init__()

                                                    self.yang_name = "bandwidth"
                                                    self.yang_parent_name = "wfq"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                        ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                                    ])
                                                    self.value = None
                                                    self.unit = None
                                                    self._segment_path = lambda: "bandwidth"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth, ['value', 'unit'], name, value)

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.Bandwidth']['meta_info']


                                            class SumOfBandwidth(_Entity_):
                                                """
                                                Sum of Bandwidth
                                                
                                                .. attribute:: value
                                                
                                                	Config value
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: unit
                                                
                                                	Config unit
                                                	**type**\:  :py:class:`QosUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.QosUnit>`
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'skp-qos-oper'
                                                _revision = '2016-02-18'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth, self).__init__()

                                                    self.yang_name = "sum-of-bandwidth"
                                                    self.yang_parent_name = "wfq"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                        ('unit', (YLeaf(YType.enumeration, 'unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper', 'QosUnit', '')])),
                                                    ])
                                                    self.value = None
                                                    self.unit = None
                                                    self._segment_path = lambda: "sum-of-bandwidth"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth, ['value', 'unit'], name, value)

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                    return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq.SumOfBandwidth']['meta_info']

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config.Wfq']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Config']['meta_info']


                                    class Result(_Entity_):
                                        """
                                        QoS EA Class Result
                                        
                                        .. attribute:: queue
                                        
                                        	QoS EA Queue Result
                                        	**type**\:  :py:class:`Queue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: police
                                        
                                        	QoS EA Policer Result
                                        	**type**\:  :py:class:`Police <ydk.models.cisco_ios_xr.Cisco_IOS_XR_skp_qos_oper.PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: stats_id
                                        
                                        	Stats ID
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'skp-qos-oper'
                                        _revision = '2016-02-18'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result, self).__init__()

                                            self.yang_name = "result"
                                            self.yang_parent_name = "qos-show-ea-pclass-st"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("queue", ("queue", PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue)), ("police", ("police", PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police))])
                                            self._leafs = OrderedDict([
                                                ('stats_id', (YLeaf(YType.uint32, 'stats-id'), ['int'])),
                                            ])
                                            self.stats_id = None

                                            self.queue = PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue()
                                            self.queue.parent = self
                                            self._children_name_map["queue"] = "queue"

                                            self.police = PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police()
                                            self.police.parent = self
                                            self._children_name_map["police"] = "police"
                                            self._segment_path = lambda: "result"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result, ['stats_id'], name, value)


                                        class Queue(_Entity_):
                                            """
                                            QoS EA Queue Result
                                            
                                            .. attribute:: queue_id
                                            
                                            	Queue ID
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: commit_tx
                                            
                                            	Commit Tx
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: excess_tx
                                            
                                            	Excess Tx
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: drop
                                            
                                            	Drop
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue, self).__init__()

                                                self.yang_name = "queue"
                                                self.yang_parent_name = "result"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('queue_id', (YLeaf(YType.uint32, 'queue-id'), ['int'])),
                                                    ('commit_tx', (YLeaf(YType.uint32, 'commit-tx'), ['int'])),
                                                    ('excess_tx', (YLeaf(YType.uint32, 'excess-tx'), ['int'])),
                                                    ('drop', (YLeaf(YType.uint32, 'drop'), ['int'])),
                                                ])
                                                self.queue_id = None
                                                self.commit_tx = None
                                                self.excess_tx = None
                                                self.drop = None
                                                self._segment_path = lambda: "queue"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue, ['queue_id', 'commit_tx', 'excess_tx', 'drop'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Queue']['meta_info']


                                        class Police(_Entity_):
                                            """
                                            QoS EA Policer Result
                                            
                                            .. attribute:: token_bucket_id
                                            
                                            	Token Bucket ID
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: conform
                                            
                                            	Conform Rate
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: exceed
                                            
                                            	Exceed Rate
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: violate
                                            
                                            	Violate Rate
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'skp-qos-oper'
                                            _revision = '2016-02-18'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police, self).__init__()

                                                self.yang_name = "police"
                                                self.yang_parent_name = "result"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('token_bucket_id', (YLeaf(YType.uint32, 'token-bucket-id'), ['int'])),
                                                    ('conform', (YLeaf(YType.uint32, 'conform'), ['int'])),
                                                    ('exceed', (YLeaf(YType.uint32, 'exceed'), ['int'])),
                                                    ('violate', (YLeaf(YType.uint32, 'violate'), ['int'])),
                                                ])
                                                self.token_bucket_id = None
                                                self.conform = None
                                                self.exceed = None
                                                self.violate = None
                                                self._segment_path = lambda: "police"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police, ['token_bucket_id', 'conform', 'exceed', 'violate'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                                return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result.Police']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                            return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt.Result']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                        return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass.QosShowEaPclassSt']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                    return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details.SkywarpQosPolicyClass']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                                return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input.Details']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                            return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface.Input']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                        return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces.Interface']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                    return meta._meta_table['PlatformQosEa.Nodes.Node.Interfaces']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
                return meta._meta_table['PlatformQosEa.Nodes.Node']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
            return meta._meta_table['PlatformQosEa.Nodes']['meta_info']

    def clone_ptr(self):
        self._top_entity = PlatformQosEa()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_skp_qos_oper as meta
        return meta._meta_table['PlatformQosEa']['meta_info']


